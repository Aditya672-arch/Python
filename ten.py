"""
Simple Railway Reservation System (CLI)
Features:
- Preloaded trains with seat counts by class
- View trains, check availability
- Book ticket -> generates PNR
- Cancel ticket by PNR
- View booking by PNR
- Persist data to 'data.json'
Written for clarity and easy extension.
"""

import json
import os
import random
import string
import datetime
from dataclasses import dataclass, asdict, field
from typing import Dict, List, Optional

DATA_FILE = "data.json"


def generate_pnr():
    now = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{now}{rand}"


@dataclass
class TrainClassInfo:
    total_seats: int
    booked_seats: List[int] = field(default_factory=list)

    def available_count(self) -> int:
        return self.total_seats - len(self.booked_seats)

    def allocate_seat(self) -> Optional[int]:
        if self.available_count() <= 0:
            return None
        # allocate smallest available seat number starting from 1
        for seat_num in range(1, self.total_seats + 1):
            if seat_num not in self.booked_seats:
                self.booked_seats.append(seat_num)
                return seat_num
        return None

    def free_seat(self, seat_num: int) -> bool:
        if seat_num in self.booked_seats:
            self.booked_seats.remove(seat_num)
            return True
        return False


@dataclass
class Train:
    train_id: str
    name: str
    source: str
    destination: str
    classes: Dict[str, TrainClassInfo]  # e.g., {"SL": TrainClassInfo(100), "3A": TrainClassInfo(30)}


@dataclass
class Booking:
    pnr: str
    train_id: str
    train_name: str
    passenger_name: str
    age: int
    klass: str
    seat_no: int
    booking_time: str


class ReservationSystem:
    def __init__(self):
        self.trains: Dict[str, Train] = {}
        self.bookings: Dict[str, Booking] = {}
        self._load()

    def _default_trains(self):
        # Some sample trains - change or expand as needed
        return {
            "12301": Train(
                train_id="12301",
                name="InterCity Express",
                source="CityA",
                destination="CityB",
                classes={
                    "SL": TrainClassInfo(total_seats=80),
                    "3A": TrainClassInfo(total_seats=24),
                    "2A": TrainClassInfo(total_seats=10),
                },
            ),
            "12402": Train(
                train_id="12402",
                name="Coastal Express",
                source="CityC",
                destination="CityD",
                classes={
                    "SL": TrainClassInfo(total_seats=60),
                    "3A": TrainClassInfo(total_seats=18),
                },
            ),
        }

    def _load(self):
        if not os.path.exists(DATA_FILE):
            # initialize defaults
            self.trains = self._default_trains()
            self.bookings = {}
            self._save()
            return

        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        # load trains
        self.trains = {}
        for tid, tdata in data.get("trains", {}).items():
            classes = {}
            for cname, cinfo in tdata["classes"].items():
                classes[cname] = TrainClassInfo(total_seats=cinfo["total_seats"], booked_seats=cinfo["booked_seats"])
            self.trains[tid] = Train(
                train_id=tdata["train_id"],
                name=tdata["name"],
                source=tdata["source"],
                destination=tdata["destination"],
                classes=classes,
            )
        # load bookings
        self.bookings = {}
        for pnr, bdata in data.get("bookings", {}).items():
            self.bookings[pnr] = Booking(**bdata)

    def _save(self):
        data = {"trains": {}, "bookings": {}}
        for tid, train in self.trains.items():
            data["trains"][tid] = {
                "train_id": train.train_id,
                "name": train.name,
                "source": train.source,
                "destination": train.destination,
                "classes": {
                    cname: {"total_seats": cinfo.total_seats, "booked_seats": cinfo.booked_seats}
                    for cname, cinfo in train.classes.items()
                },
            }
        for pnr, booking in self.bookings.items():
            data["bookings"][pnr] = asdict(booking)
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def list_trains(self) -> List[Train]:
        return list(self.trains.values())

    def show_trains(self):
        print("Available trains:")
        for t in self.trains.values():
            print(f"{t.train_id} - {t.name} | {t.source} -> {t.destination}")
            for cname, cinfo in t.classes.items():
                print(f"   Class {cname}: {cinfo.available_count()}/{cinfo.total_seats} available")
        print()

    def check_availability(self, train_id: str, klass: str) -> int:
        train = self.trains.get(train_id)
        if not train:
            raise ValueError("Train not found")
        c = train.classes.get(klass)
        if not c:
            raise ValueError("Class not available on this train")
        return c.available_count()

    def book_ticket(self, train_id: str, klass: str, passenger_name: str, age: int) -> Booking:
        train = self.trains.get(train_id)
        if not train:
            raise ValueError("Train not found")
        cinfo = train.classes.get(klass)
        if not cinfo:
            raise ValueError("Class not found")
        seat = cinfo.allocate_seat()
        if seat is None:
            raise ValueError("No seats available in this class")
        pnr = generate_pnr()
        booking_time = datetime.datetime.now().isoformat()
        booking = Booking(
            pnr=pnr,
            train_id=train_id,
            train_name=train.name,
            passenger_name=passenger_name,
            age=age,
            klass=klass,
            seat_no=seat,
            booking_time=booking_time,
        )
        self.bookings[pnr] = booking
        self._save()
        return booking

    def cancel_booking(self, pnr: str) -> bool:
        booking = self.bookings.get(pnr)
        if not booking:
            return False
        train = self.trains.get(booking.train_id)
        if not train:
            # inconsistent data; still remove booking
            del self.bookings[pnr]
            self._save()
            return True
        cinfo = train.classes.get(booking.klass)
        if cinfo:
            cinfo.free_seat(booking.seat_no)
        del self.bookings[pnr]
        self._save()
        return True

    def view_booking(self, pnr: str) -> Optional[Booking]:
        return self.bookings.get(pnr)

    def show_all_bookings(self):
        if not self.bookings:
            print("No bookings yet.")
            return
        for b in self.bookings.values():
            self.print_booking(b)

    @staticmethod
    def print_booking(b: Booking):
        print("----- Booking -----")
        print(f"PNR        : {b.pnr}")
        print(f"Name       : {b.passenger_name} ({b.age})")
        print(f"Train      : {b.train_id} - {b.train_name}")
        print(f"Class/Seat : {b.klass} / {b.seat_no}")
        print(f"Booked At  : {b.booking_time}")
        print("-------------------\n")


def main_menu():
    rs = ReservationSystem()
    print("Welcome to Mini Railway Reservation System\n")

    while True:
        print("Menu:")
        print(" 1. Show trains")
        print(" 2. Check availability")
        print(" 3. Book ticket")
        print(" 4. Cancel ticket")
        print(" 5. View booking (PNR)")
        print(" 6. Show all bookings")
        print(" 0. Exit")
        choice = input("Choose option: ").strip()

        try:
            if choice == "1":
                rs.show_trains()

            elif choice == "2":
                tid = input("Enter train id: ").strip()
                cls = input("Enter class (e.g. SL, 3A, 2A): ").strip().upper()
                avail = rs.check_availability(tid, cls)
                print(f"Available seats in {cls} on train {tid}: {avail}\n")

            elif choice == "3":
                tid = input("Enter train id: ").strip()
                cls = input("Enter class (e.g. SL, 3A, 2A): ").strip().upper()
                name = input("Passenger name: ").strip()
                age = int(input("Age: ").strip())
                booking = rs.book_ticket(tid, cls, name, age)
                print("Booking successful! Details:")
                rs.print_booking(booking)

            elif choice == "4":
                pnr = input("Enter PNR to cancel: ").strip()
                ok = rs.cancel_booking(pnr)
                if ok:
                    print("Booking cancelled successfully.\n")
                else:
                    print("PNR not found.\n")

            elif choice == "5":
                pnr = input("Enter PNR: ").strip()
                b = rs.view_booking(pnr)
                if b:
                    rs.print_booking(b)
                else:
                    print("PNR not found.\n")

            elif choice == "6":
                rs.show_all_bookings()

            elif choice == "0":
                print("Goodbye — saving data.")
                rs._save()
                break

            else:
                print("Invalid choice. Try again.\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main_menu()

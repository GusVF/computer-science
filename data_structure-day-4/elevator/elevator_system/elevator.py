from enum import Enum
from elevator_system.motor import MotorSide


class Elevator():
    def __init__(self, motor):
        self.current_floor = 0
        self.door_is_open = False
        self._status = ElevatorStatus.STOPPED
        self.motor = motor

    def move(self, destination_floor):
        if self.current_floor == destination_floor:
            self._status = ElevatorStatus.STOPPED
            self.door_is_open = True
            return

        self.door_is_open = False

        if destination_floor > self.current_floor:
            self._status = ElevatorStatus.GOING_UP
            self.motor.turn_on(MotorSide.CLOCKWISE)
            self.motor.turn_off()

        else:
            self._status = ElevatorStatus.GOING_DOWN
            self.motor.turn_on(MotorSide.COUNTERCLOCKWISE)
            self.motor.turn_off()

        self.current_floor = destination_floor


class ElevatorStatus(Enum):
    STOPPED = 0
    GOING_UP = 1
    GOING_DOWN = 2
    LOCKED = 3

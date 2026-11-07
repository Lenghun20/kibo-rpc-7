# class RobotState:

#     def __init__(self, x=0, y=0.0, z=0.0):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.is_steady = False


class SafetyMonitor:
    def __init__(self):
        self._battery = 100.0 #private
    def update_battery(self, val):
        if 0.0 <= val <= 100.0:
            self._battery = val
        else:
            print("[ERROR] Invalid battery telemetry!")

    def get_battery(self):
        return self._battery

monitor = SafetyMonitor()

monitor.update_battery(120)

print(monitor.get_battery())
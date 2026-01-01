import datetime

class AuditLog:
    log_count = 0
    def __init__(self, object, action:str, quantity:int):
        self._object = object
        self._action = action
        self._quantity = quantity
        self._timestamp = datetime.datetime.now()
        AuditLog.log_count += 1
    
    def __repr__(self):
        return f"Log {AuditLog.log_count} [Time: {self._timestamp}, Action:{self._action}, Object:{self._object}, Quantity:{self._quantity}]"
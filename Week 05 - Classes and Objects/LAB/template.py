"""
RECORD CHECK  -  my version
===========================

Name  :Ruvarashe Gaka
Lane  :  AI / Cyber / IT      (delete two)
Date  : 22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


class record:
    
    over_limit_count = 0
    def __init__(self, label, value, limit):
        """Gives names/value to the attributes used in the method"""
        self.label = label
        self.value = value
        self.limit = limit
    def status(self):
        """Returns OVER LIMIT, WARNING AND OK based on the attributes"""
        if self.value >= self.limit:
            return "OVER LIMIT"
            record.over_limit_count += 1
         
        elif self.value >= self.limit * 0.9:
            return "WARNING"
        else:
            return "OK"


records = [
    record("R-001", 98.0, 100.0),
    record("R-002", 45.0, 100.0)
]   
for record in records:
    print(record.status())


for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print("Value:    :", "\t",       record.value)
    print("Limit     :", "\t",       record.limit)
    print("Status    :", "\t",       record.status())
   
    print("=" * 34)

print(record.over_limit_count)


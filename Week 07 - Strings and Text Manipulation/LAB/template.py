"""
RECORD CHECK  -  my version
===========================

Name  : Ruvarashe Gaka
Lane  : IT
Date  :05/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """Clean and parse a raw line into a dictionary."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()
    record = {"hostname": hostname}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())
    return record
def status_of(record):
    """Determine the status of a record based on its values."""
    percent_used = (record.get("used", 0) / record.get("total", 1)) * 100
    if percent_used >= 100:
        return "OVER LIMIT"
    elif percent_used >= 90:
        return "WARNING"
    else:
        return "OK"
""" making the messy lines"""
raw_records = ["Srv-01 , used=87 , total=100",
               "Srv-02 , used=45 , total=100",
               "Srv-03 , used=98 , total=100",
                "Srv-04 , used=120 , total=100",
                "Srv-05 , used=67 , total=100",
                 "Srv-06 , used=35 , total=100",
                  "Srv-07 , used=103 , total=100",
                  "Srv-08 , used=12 , total=100"]
"""adding a counter to count the number of records that are over the limit"""
OVER_LIMIT_count = 0
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    print(record, "Status:", status)
    if status == "OVER LIMIT":
        OVER_LIMIT_count += 1
"""printing the total number of records and the number of records that are over the limit"""
print(f"\nTotal records: {len(raw_records)}, Over limit: {OVER_LIMIT_count}")




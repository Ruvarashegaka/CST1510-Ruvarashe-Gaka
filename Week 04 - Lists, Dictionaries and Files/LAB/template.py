"""
RECORD CHECK  -  my version
===========================

Name  :Ruvarashe Gaka
Lane  :IT      
Date  : 16/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Calculates the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100 if limit != 0 else 0
    status = "OVER LIMIT" if percent >= 100 else "WARNING!" if percent >= 90 else "OK"
    return difference, percent, status

def print_report(difference, percent, status):
    """prints the report based on the given parameters."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {host_name}")
    print("=" * 34)
    print(f"GB used        :      {value:>10.2f}")
    print(f"GB total       :      {limit:>10.2f}")
    print(f"GB left        :      {difference:>+10.2f}")
    print(f"Percent used   :      {percent:>10.2f}%")
    print(f"Status         :      {status:>10}")
    print("=" * 34)



# ====================================================================== STORE

records = [{"host_name": "R-001", "GB_used": 80, "GB_total": 100}, 
           {"host_name": "R-002", "GB_used": 44, "GB_total": 100}, 
           {"host_name": "R-003", "GB_used": 95, "GB_total": 100}]  


# =============================================================== PROCESS + OUTPUT
over_limit_count = 0
for record in records:
    host_name = record["host_name"] 
    value = record["GB_used"]
    limit = record["GB_total"]
    difference, percent, status = check_record(value, limit)
    if status == "OVER LIMIT":
        over_limit_count += 1
    print_report(difference, percent, status)

print(over_limit_count)


    
    
  


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job

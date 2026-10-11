"""
RECORD CHECK  -  my version
===========================

Name  :Ruvarashe Gaka
Lane  : IT  
Date  : 08/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    """Returns the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
def check(value, limit):
    """Calculates the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100 if limit != 0 else 0
    return difference, percent

host_name = input("Enter the host name: ")  
GB_used= float(input("Enter the GB used: "))   
total_GB = float(input("Enter the total GB: "))   

difference, percent_used = check(GB_used, total_GB)
status = status_of(percent_used)

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {host_name}")
print("=" * 34)

print(f"GB used        :      {GB_used:>10.2f}")
print(f"GB total       :      {total_GB:>10.2f}")
print(f"GB left        :      {difference:>+10.2f}")
print(f"Percent used   :      {percent_used:>10.2f}%")
print(f"Status         :      {status:>10}")

print("=" * 34)


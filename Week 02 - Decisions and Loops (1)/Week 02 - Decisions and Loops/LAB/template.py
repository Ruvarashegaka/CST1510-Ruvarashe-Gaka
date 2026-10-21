"""
RECORD CHECK  -  my version
===========================

Name  : Ruvarashe Gaka
Lane  : IT      (delete two)
Date  : 01/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


host_name = input("Enter the host_name: ") 
gb_used = float(input("Enter the GB used: "))  
gb_total = float(input("Enter the GB total: "))  
difference = gb_total - gb_used  
percent_left = (difference / gb_total) * 100

"""conditional statement to determine the status based on the percentage left."""

if percent_left >= 100:
    status = "OVER LIMIT"
elif percent_left >= 90 and percent_left < 100:
    status = "OK"
else:
    status = "WARNING!!"

print(status)
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {host_name}")
print("=" * 34)
print(f"Gb_used        :      {gb_used:>10.2f}")
print(f"Gb_total       :      {gb_total:>10.2f}")
print(f"Gb_left        :      {difference:>+10.2f}")
print(f"Percent_left   :      {percent_left:>10.2f}%")
print(f"Status         :      {status:>10}")
print("=" * 34)


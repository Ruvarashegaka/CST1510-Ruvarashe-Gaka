"""
RECORD CHECK  -  my version
===========================

Name  :Ruvarashe Gaka
Lane  :IT  
Date  :25/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

Host_name = (input("Enter your hostname: "))    
Gb_used = float(input("Enter Gb used: "))     
Gb_total = float(input("Enter Gb total: "))   
Gb_left = Gb_total - Gb_used  
 
"""calculates the percent used """

percent = (Gb_used / Gb_total) * 100
print()
print("=" * 34)
print(f"RECORD CHECK  -  {Host_name}")
print("=" * 34)
print(f"Gb_used        :      {Gb_used:>10.2f}")
print(f"Gb_total       :      {Gb_total:>10.2f}")
print(f"Gb_left        :      {Gb_left:>+10.2f}")
print(f"Percent        :      {percent:>10.2f}%")
print("=" * 34)

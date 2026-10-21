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
GB_used = float(input("Enter Gb used: "))     
GB_total = float(input("Enter Gb total: "))   
GB_left = GB_total - GB_used  
 
"""calculates the percent used """

percent = (GB_used / GB_total) * 100
print()
print("=" * 34)
print(f"RECORD CHECK - {Host_name}")
print("=" * 34)
print(f"Gb_used        :      {GB_used:>10.2f}")
print(f"Gb_total       :      {GB_total:>10.2f}")
print(f"Gb_left        :      {GB_left:>+10.2f}")
print(f"Percent        :      {percent:>10.2f}%")
print("=" * 34)

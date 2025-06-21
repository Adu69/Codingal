import math

def main():
    angle_deg = float(input("Enter angle in degrees: "))
    angle_rad = math.radians(angle_deg)
    sin_val = math.sin(angle_rad)
    cos_val = math.cos(angle_rad)
    try:
        tan_val = math.tan(angle_rad)
    except Exception as e:
        tan_val = str(e)
    
    print(f"\nFor angle {angle_deg} degrees:")
    print(f"sin({angle_deg}) = {sin_val}")
    print(f"cos({angle_deg}) = {cos_val}")
    
    if abs(cos_val) < 1e-10:
        print(f"tan({angle_deg}) is undefined (division by zero)")
    else:
        print(f"tan({angle_deg}) = {tan_val}")

main()

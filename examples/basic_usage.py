#!/usr/bin/env python3
"""
Example script showing various ways to use the Vishal Info module
"""

from vishal_info import MobileInfo, lookup, quick_lookup

def main():
    print("🚀 Vishal Info Module Examples")
    print("=" * 50)
    
    # Example 1: Quick lookup (simplest)
    print("\n1️⃣ Quick Lookup Example:")
    quick_lookup("7068715523")
    
    # Example 2: Using the class
    print("\n2️⃣ Class-based Usage:")
    info = MobileInfo()
    
    # Get raw data
    data = info.get_info("7068715523")
    if data:
        print(f"\nFound {len(data)} record(s)")
        for record in data:
            print(f"  - Name: {record.get('name')}")
            print(f"  - Circle: {record.get('circle')}")
    
    # Example 3: Format address
    print("\n3️⃣ Address Formatting:")
    raw_addr = "S/O Shyam Lal!!40 Genda Kaboola!!Genda Kabola Jhansi!Uttar Pradesh!284302"
    formatted = info.format_address(raw_addr)
    print(f"Raw: {raw_addr}")
    print(f"Formatted: {formatted}")
    
    # Example 4: Error handling
    print("\n4️⃣ Error Handling:")
    try:
        # Try invalid number
        info.get_info("123")
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")
    
    # Example 5: Context manager
    print("\n5️⃣ Context Manager Usage:")
    with MobileInfo() as info:
        data = info.get_info("7068715523")
        if data:
            print("✅ Data fetched successfully within context")

if __name__ == "__main__":
    main()
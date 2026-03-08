#!/usr/bin/env python3
"""
Batch lookup example - process multiple numbers
"""

import csv
import json
from vishal_info import MobileInfo

def batch_lookup(numbers, output_file=None):
    """
    Lookup multiple numbers and optionally save results
    """
    results = {}
    
    with MobileInfo() as info:
        for idx, number in enumerate(numbers, 1):
            print(f"[{idx}/{len(numbers)}] Looking up {number}...")
            data = info.get_info(number)
            results[number] = data
    
    # Save to file if requested
    if output_file:
        if output_file.endswith('.json'):
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\n✅ Results saved to {output_file}")
        elif output_file.endswith('.csv'):
            with open(output_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Mobile', 'Name', 'Father', 'Circle', 'Address'])
                for num, data in results.items():
                    if data:
                        for record in data:
                            writer.writerow([
                                num,
                                record.get('name', ''),
                                record.get('fname', ''),
                                record.get('circle', ''),
                                record.get('address', '')
                            ])
            print(f"\n✅ Results saved to {output_file}")
    
    return results

def main():
    numbers = [
        "7068715523",
        "9936265021",
        # Add more numbers...
    ]
    
    print("📊 Batch Lookup Started")
    print("=" * 50)
    
    results = batch_lookup(numbers, output_file="lookup_results.json")
    
    # Print summary
    print("\n📈 Summary:")
    for num, data in results.items():
        status = "✅ Found" if data else "❌ Not Found"
        count = len(data) if data else 0
        print(f"  {num}: {status} ({count} records)")

if __name__ == "__main__":
    main()
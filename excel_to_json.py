#!/usr/bin/env python3
"""
Convert ISSUES.xlsx to JSON format for GitHub Pages website
This script reads the Excel file and creates JSON data files for the static website
"""

import pandas as pd
import json
import os
from datetime import datetime

def convert_excel_to_json():
    """Convert Excel data to JSON format for GitHub Pages"""
    
    try:
        # Read the Excel file
        print("Reading ISSUES.xlsx...")
        df = pd.read_excel('ISSUES.xlsx', sheet_name='Sheet1', skiprows=2)
        
        # Clean and prepare the data
        materials = []
        stock_data = []
        
        for index, row in df.iterrows():
            # Skip empty rows
            if pd.isna(row.iloc[1]) or pd.isna(row.iloc[2]):
                continue
                
            material_code = str(row.iloc[1]).strip()
            material_name = str(row.iloc[2]).strip()
            
            # Skip header rows
            if material_code in ['Material Code', 'nan'] or material_name in ['Material Name', 'nan']:
                continue
            
            # Extract stock data
            received = float(row.iloc[5]) if pd.notna(row.iloc[5]) else 0
            issued = float(row.iloc[6]) if pd.notna(row.iloc[6]) else 0
            returned = float(row.iloc[7]) if pd.notna(row.iloc[7]) else 0
            
            # Add to materials list (for dropdown)
            materials.append({
                'code': material_code,
                'name': material_name
            })
            
            # Add to stock data (for table display)
            stock_data.append({
                'material_code': material_code,
                'material_name': material_name,
                'received': received,
                'issued': issued,
                'returned': returned
            })
        
        # Create docs directory if it doesn't exist
        if not os.path.exists('docs'):
            os.makedirs('docs')
        
        # Save materials data
        with open('docs/materials.json', 'w', encoding='utf-8') as f:
            json.dump(materials, f, indent=2, ensure_ascii=False)
        
        # Save stock data
        with open('docs/stock_data.json', 'w', encoding='utf-8') as f:
            json.dump(stock_data, f, indent=2, ensure_ascii=False)
        
        # Create metadata
        metadata = {
            'last_updated': datetime.now().isoformat(),
            'total_materials': len(materials),
            'data_source': 'ISSUES.xlsx',
            'note': 'This is a static snapshot of the Excel data for GitHub Pages'
        }
        
        with open('docs/metadata.json', 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Successfully converted Excel data:")
        print(f"   - {len(materials)} materials saved to docs/materials.json")
        print(f"   - {len(stock_data)} stock records saved to docs/stock_data.json")
        print(f"   - Metadata saved to docs/metadata.json")
        
        return True
        
    except Exception as e:
        print(f"❌ Error converting Excel data: {e}")
        return False

def create_csv_backup():
    """Create CSV backup of the Excel data"""
    try:
        df = pd.read_excel('ISSUES.xlsx', sheet_name='Sheet1', skiprows=2)
        df.to_csv('docs/issues_backup.csv', index=False, encoding='utf-8')
        print("✅ CSV backup created: docs/issues_backup.csv")
    except Exception as e:
        print(f"❌ Error creating CSV backup: {e}")

if __name__ == "__main__":
    print("🔄 Converting ISSUES.xlsx to JSON format for GitHub Pages...")
    
    if convert_excel_to_json():
        create_csv_backup()
        print("\n🎉 Conversion completed successfully!")
        print("📁 Files created in docs/ folder:")
        print("   - materials.json (for dropdown options)")
        print("   - stock_data.json (for table display)")
        print("   - metadata.json (conversion info)")
        print("   - issues_backup.csv (CSV backup)")
    else:
        print("\n❌ Conversion failed!")

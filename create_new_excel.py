import pandas as pd
from openpyxl import Workbook
import os

# Create a new Excel file with proper structure
def create_inventory_excel():
    # Read the original file to get materials
    try:
        df_original = pd.read_excel('ISSUES.xlsx', skiprows=1)
        
        # Extract materials
        materials_data = []
        for index, row in df_original.iterrows():
            if pd.notna(row.iloc[1]) and pd.notna(row.iloc[2]):
                material_code = str(row.iloc[1]).strip()
                material_name = str(row.iloc[2]).strip()
                if material_code != 'Material Code' and material_name != 'Material Name':
                    materials_data.append([material_code, material_name])
        
        # Create new workbook
        wb = Workbook()
        
        # Materials sheet
        ws_materials = wb.active
        ws_materials.title = 'Materials'
        ws_materials['A1'] = 'Material Code'
        ws_materials['B1'] = 'Material Name'
        
        for i, (code, name) in enumerate(materials_data, start=2):
            ws_materials[f'A{i}'] = code
            ws_materials[f'B{i}'] = name
        
        # Transactions sheet
        ws_transactions = wb.create_sheet('Transactions')
        ws_transactions['A1'] = 'Timestamp'
        ws_transactions['B1'] = 'Material Code'
        ws_transactions['C1'] = 'Material Name'
        ws_transactions['D1'] = 'Transaction Type'
        ws_transactions['E1'] = 'Quantity'
        
        # Save the new file
        wb.save('INVENTORY.xlsx')
        print("Created new INVENTORY.xlsx file successfully!")
        
    except Exception as e:
        print(f"Error creating new Excel file: {e}")

if __name__ == "__main__":
    create_inventory_excel()

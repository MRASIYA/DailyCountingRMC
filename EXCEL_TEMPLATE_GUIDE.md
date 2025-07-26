# 📊 Excel Template Guide - ISSUES.xlsx Format

## 🎯 Required Excel Structure

Your **ISSUES.xlsx** file must follow this exact format for the application to work properly:

### Sheet Name: **Sheet1**

### Column Layout (Row 4 onwards):

| Column | Letter | Field Name | Description | Example |
|--------|--------|------------|-------------|---------|
| A | A | Reference | Any reference data | REF001 |
| B | B | **Material Code** | Unique material identifier | MAT001 |
| C | C | **Material Name** | Full material description | Steel Bars |
| D | D | Unit | Measurement unit | KG |
| E | E | Price | Unit price (optional) | 25.50 |
| F | F | **Received** | Received quantities | 150 |
| G | G | **Issues** | Issued quantities | 120 |
| H | H | **Return** | Returned quantities | 5 |

## 📝 Sample Excel Template

### Header Rows (1-3):
```
Row 1: Daily Counting System
Row 2: Inventory Management
Row 3: [Column Headers]
```

### Data Rows (4+):
```
Row 4: REF001 | MAT001 | Steel Bars | KG | 25.50 | 150 | 120 | 5
Row 5: REF002 | MAT002 | Concrete Mix | BAG | 15.00 | 200 | 180 | 10
Row 6: REF003 | MAT003 | Wood Planks | PCS | 8.75 | 75 | 60 | 2
```

## ⚠️ Critical Requirements

### Must Have:
- ✅ **Column B**: Material Code (unique identifier)
- ✅ **Column C**: Material Name (description)
- ✅ **Column F**: Received quantities (numbers only)
- ✅ **Column G**: Issues quantities (numbers only)
- ✅ **Column H**: Return quantities (numbers only)

### Data Rules:
- 🔢 **Numeric columns** (F, G, H) must contain numbers only
- 🆔 **Material codes** must be unique
- 📝 **Material names** should be descriptive
- 🚫 **No empty rows** between data
- 📊 **Start data from Row 4**

## 🛠️ How to Create Template

### Method 1: Use Existing File
1. Open your current ISSUES.xlsx
2. Verify column layout matches above
3. Ensure data starts from Row 4
4. Save and test with application

### Method 2: Create New File
1. Create new Excel workbook
2. Name first sheet "Sheet1"
3. Add headers in rows 1-3
4. Add column headers in row 3
5. Add your material data from row 4
6. Save as "ISSUES.xlsx"

### Method 3: Copy Sample Template
```
A       B       C               D    E      F        G      H
REF     Code    Name            Unit Price  Received Issues Return
---     ----    ----            ---- -----  --------  ------ ------
REF001  MAT001  Steel Bars      KG   25.50  150       120    5
REF002  MAT002  Concrete Mix    BAG  15.00  200       180    10
REF003  MAT003  Wood Planks     PCS  8.75   75        60     2
REF004  MAT004  Paint           LTR  12.00  50        45     3
REF005  MAT005  Screws          BOX  5.25   1000      800    20
```

## 🎨 Formatting Tips

### Recommended Formatting:
- **Bold headers** (Rows 1-3)
- **Number format** for quantity columns (F, G, H)
- **Text format** for material codes and names
- **Consistent alignment** for better readability

### Color Coding (Optional):
- 🟢 **Green**: Received column (F)
- 🔴 **Red**: Issues column (G)
- 🟡 **Yellow**: Return column (H)

## 🔧 Troubleshooting Excel Issues

### Common Problems:

**❌ "Material not found"**
- Check Column B has unique material codes
- Ensure no empty cells in material code column
- Verify spelling matches exactly

**❌ "Data not loading"**
- Confirm sheet name is "Sheet1"
- Check data starts from Row 4
- Ensure no merged cells in data area

**❌ "Number format error"**
- Convert quantity columns (F, G, H) to numbers
- Remove any text from numeric columns
- Check for hidden characters or spaces

**❌ "File access denied"**
- Close Excel before running application
- Check file is not read-only
- Ensure file permissions allow writing

## 📊 Data Validation

### Before Using:
1. **Check Column B** - All material codes are unique
2. **Check Column C** - All materials have names
3. **Check Columns F, G, H** - Only contain numbers
4. **Check Row Count** - Data starts from Row 4
5. **Check Sheet Name** - Named "Sheet1"

### Test Your Template:
1. Save your Excel file as "ISSUES.xlsx"
2. Run the application
3. Check if materials load in dropdown
4. Test adding a small quantity
5. Verify Excel file updates correctly

## 📈 Advanced Excel Features

### Formulas (Optional):
You can add calculated columns after Column H:
- **Column I**: Balance = F - G + H
- **Column J**: Last Updated = TODAY()
- **Column K**: Status = IF(Balance<10,"Low Stock","OK")

### Data Validation:
- Set number format for quantity columns
- Add dropdown lists for units
- Create data validation rules

### Protection:
- Protect formula cells
- Allow editing only in quantity columns
- Set password protection if needed

## 📋 Checklist Before First Use

- [ ] File named exactly "ISSUES.xlsx"
- [ ] Sheet named "Sheet1"
- [ ] Headers in rows 1-3
- [ ] Data starts from row 4
- [ ] Column B has material codes
- [ ] Column C has material names
- [ ] Columns F, G, H are numbers only
- [ ] No empty rows in data
- [ ] File saved and closed in Excel
- [ ] Application can read the file

## 🔄 Backup Recommendations

### Before Each Use:
1. **Create backup copy** of ISSUES.xlsx
2. **Name with date**: ISSUES_backup_2024-01-26.xlsx
3. **Store in separate folder**
4. **Test restore process**

### Automatic Backups:
The application creates automatic backups:
- **Location**: Same folder as ISSUES.xlsx
- **Name**: ISSUES.xlsx.backup
- **Created**: Before each update
- **Restored**: If update fails

## 📞 Support

If your Excel file doesn't work:
1. Compare with sample template above
2. Check all requirements are met
3. Test with minimal data first
4. Review error messages carefully

**Template working? Start counting! 📊✨**

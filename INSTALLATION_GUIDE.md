# 📋 Daily Counting - Installation & User Guide

## 🚀 Quick Start

### System Requirements
- **Windows 10/11**
- **Python 3.8+**
- **Microsoft Excel** (for ISSUES.xlsx file)
- **Web Browser** (Chrome, Firefox, Edge)

## 📦 Installation Methods

### Method 1: Direct Excel Integration (Recommended)

1. **Download or Clone Repository**
   ```bash
   git clone https://github.com/MRASIYA/DailyCountingRMC.git
   cd DailyCountingRMC
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   # Double-click this file:
   run_excel_app.bat
   
   # Or run manually:
   python excel_app.py
   ```

4. **Open in Browser**
   - Visit: http://localhost:5000
   - Application loads your ISSUES.xlsx automatically

### Method 2: Standalone HTML Version

1. **Open `local_app.html` in any browser**
2. **Drag & drop your ISSUES.xlsx file**
3. **Start using immediately**

### Method 3: GitHub Pages Demo

1. **Visit: https://mrasiya.github.io/DailyCountingRMC/**
2. **See live demo with sample data**

## 🎯 How to Use

### Step-by-Step Process

1. **Select Material**
   - Choose from dropdown (loaded from your Excel)
   - All materials from ISSUES.xlsx Sheet1

2. **Choose Transaction Type**
   - **Issues** → Adds to "Issued" column
   - **Received** → Adds to "Received" column  
   - **Return** → Adds to "Return" column

3. **Enter Quantity**
   - Any positive number
   - Supports decimals

4. **Submit Transaction**
   - Click "UPDATE ISSUES.xlsx"
   - See immediate updates in table
   - Excel file updated automatically

5. **Download Updated Excel**
   - Click "DOWNLOAD EXCEL"
   - Get updated ISSUES.xlsx file

## 📊 Excel File Format

Your ISSUES.xlsx file should have this structure in Sheet1:

| Row | A | B (Material Code) | C (Material Name) | D | E | F (Received) | G (Issues) | H (Return) |
|-----|---|-------------------|-------------------|---|---|--------------|------------|------------|
| 1   | Headers... |
| 2   | Headers... |
| 3   | Headers... |
| 4   | | MAT001 | Steel Bars | ... | ... | 150 | 120 | 5 |
| 5   | | MAT002 | Concrete Mix | ... | ... | 200 | 180 | 10 |

## 🔧 Troubleshooting

### Common Issues

**❌ "Excel file not found"**
- Make sure ISSUES.xlsx is in the same folder as the application
- Check file name spelling (case-sensitive)

**❌ "Permission denied"**
- Close Excel if ISSUES.xlsx is open
- Check file is not read-only
- Run as administrator if needed

**❌ "Module not found"**
- Install Python dependencies: `pip install -r requirements.txt`
- Make sure Python 3.8+ is installed

**❌ "Port already in use"**
- Close other applications using port 5000
- Or change port in excel_app.py

### File Permissions
- Ensure ISSUES.xlsx is not open in Excel
- Make sure you have write permissions to the folder
- Avoid running from OneDrive/Cloud folders while Excel is syncing

## 🌐 Web Interface Features

### Real-Time Updates
- ✅ Live connection to Excel file
- ✅ Immediate table updates
- ✅ Visual feedback on changes
- ✅ Row/column highlighting

### Data Validation
- ✅ Material code verification
- ✅ Quantity validation
- ✅ Transaction type checking
- ✅ Error messages for invalid inputs

### Excel Integration
- ✅ Direct read/write to ISSUES.xlsx
- ✅ Backup system for safety
- ✅ Retry mechanism for file locks
- ✅ Automatic file recovery

## 📱 Mobile App (DailyStockApp)

### Installation
1. Install Apache Cordova: `npm install -g cordova`
2. Navigate to DailyStockApp folder
3. Add platform: `cordova platform add android`
4. Build app: `cordova build android`

### Features
- 📱 Native mobile interface
- 🔄 Offline capability
- 📊 Touch-friendly forms
- ⚡ Fast performance

## 🎨 Customization

### Changing Excel File Location
Edit `excel_app.py`:
```python
EXCEL_FILE = 'path/to/your/ISSUES.xlsx'
```

### Adding New Transaction Types
1. Modify dropdown options in template
2. Update transaction processing logic
3. Add new Excel columns as needed

### Styling Changes
- Edit CSS in template files
- Modify Bulma classes
- Add custom animations

## 📈 Advanced Features

### API Endpoints
- `GET /api/materials` - Get all materials
- `GET /api/stock` - Get current stock levels
- `POST /api/transaction` - Add new transaction
- `GET /download` - Download updated Excel

### Backup System
- Automatic backups before each update
- Recovery from failed transactions
- Version control with timestamps

### Data Export
- Excel download with updates
- CSV backup generation
- JSON data export

## 🤝 Support

### Getting Help
1. Check this guide first
2. Review error messages carefully
3. Ensure Excel file format is correct
4. Check Python/dependency versions

### Common Solutions
- Restart the application
- Check file permissions
- Update Python packages
- Clear browser cache

## 🔄 Updates

### Keeping Up to Date
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

### Version History
- v1.0 - Basic Flask application
- v2.0 - Excel integration
- v3.0 - GitHub Pages demo
- v4.0 - Mobile app integration

---

## 📞 Contact

For issues or questions:
- 📧 Check GitHub Issues
- 📚 Review documentation
- 🔍 Search existing solutions

**Happy Counting! 📊✨**

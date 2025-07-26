# 📋 Daily Counting - Inventory Management System

[![Build and Test](https://github.com/MRASIYA/DailyCountingRMC/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/MRASIYA/DailyCountingRMC/actions/workflows/build-and-test.yml)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://mrasiya.github.io/DailyCountingRMC/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://github.com/MRASIYA/DailyCountingRMC/blob/main/Dockerfile)
[![Excel Integration](https://img.shields.io/badge/Excel-Connected-orange)](https://github.com/MRASIYA/DailyCountingRMC)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A professional Flask web application that directly connects to Excel files for real-time inventory management and daily stock tracking.

## 🌐 Live Demo

**GitHub Pages**: https://mrasiya.github.io/DailyCountingRMC/

## 🚀 Quick Start

### Method 1: Direct Excel Integration (Recommended)
```bash
git clone https://github.com/MRASIYA/DailyCountingRMC.git
cd DailyCountingRMC
pip install -r requirements.txt

# Run the application
run_excel_app.bat
# Or: python excel_app.py

# Open browser: http://localhost:5000
```

### Method 2: Docker Deployment
```bash
docker-compose up -d
# Access at: http://localhost:5000
```

### Method 3: Standalone HTML
```bash
# Simply open local_app.html in any browser
# Drag & drop your ISSUES.xlsx file to start
```

## Features

### 🌐 Web Interface
- **Modern UI**: Clean, responsive design using Bulma CSS framework
- **Animated Elements**: Smooth animations and transitions for better user experience
- **Color Gradients**: Beautiful gradient backgrounds and styling
- **Font Awesome Icons**: Professional iconography throughout the interface

### 📊 Inventory Management
- **Material Listing**: View all available materials from your inventory
- **Transaction Processing**: Handle three types of transactions:
  - **Issues/Issued**: Updates the "Issued" column (Column 6)
  - **Received**: Updates the "Received" column (Column 5)  
  - **Return**: Updates the "Return" column (Column 7)
- **Current Stock Display**: Real-time view of current inventory levels
- **Excel Integration**: Direct read/write operations with ISSUES.xlsx file

### 📁 File Management
- **Excel Download**: Download the current ISSUES.xlsx file directly from the web interface
- **Automatic Backup**: Changes are saved directly to the Excel file
- **Data Integrity**: Robust error handling and validation

## Requirements

### Python Dependencies
```
Flask
pandas
openpyxl
```

### Files Required
- `ISSUES.xlsx`: Excel file containing your inventory data
- Must have columns for Material, Received (Column 5), Issued (Column 6), and Return (Column 7)

## Installation & Setup

1. **Clone or download the project files**
   ```bash
   # Make sure you have the following files:
   # - app.py
   # - templates/index.html
   # - ISSUES.xlsx
   ```

2. **Install Python dependencies**
   ```bash
   pip install Flask pandas openpyxl
   ```

3. **Ensure your ISSUES.xlsx file is properly formatted**
   - Column structure should match the expected format
   - Material names in the appropriate column
   - Received, Issued, and Return columns properly labeled

## Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to: `http://localhost:5000`
   - The application will be available at this address

## Usage

### Web Interface Navigation

#### Main Dashboard
- **Title**: "Daily Counting" - your inventory management hub
- **Material Selection**: Dropdown menu with all available materials
- **Transaction Type**: Choose from Issues, Received, or Return
- **Quantity Input**: Enter the transaction quantity
- **Submit**: Process the transaction with a single click

#### Current Stock Table
- View real-time inventory levels
- Color-coded for easy reading
- Automatically updates after transactions

#### Download Feature
- **Download Button**: Located prominently on the main page
- Downloads the current ISSUES.xlsx file
- Includes all recent transactions and updates

### Transaction Types Explained

1. **Issues/Issued** 📤
   - Use when materials are issued/distributed
   - Updates the "Issued" column in your Excel file
   - Reduces available stock

2. **Received** 📥
   - Use when materials are received/restocked
   - Updates the "Received" column in your Excel file
   - Increases available stock

3. **Return** 🔄
   - Use when materials are returned to inventory
   - Updates the "Return" column in your Excel file
   - Adds back to available stock

## File Structure

```
DailyStock/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface template
├── ISSUES.xlsx           # Inventory data file
└── README.md            # This documentation
```

## Technical Details

### Backend (Flask)
- **Framework**: Flask web framework
- **Data Processing**: pandas for Excel data manipulation
- **Excel Operations**: openpyxl for reading/writing Excel files
- **Error Handling**: Comprehensive error handling with user feedback
- **File Security**: Absolute path checking for secure file downloads

### Frontend
- **CSS Framework**: Bulma for responsive design
- **Icons**: Font Awesome for professional iconography
- **Styling**: Custom gradients and animations
- **Responsiveness**: Mobile-friendly design
- **User Feedback**: Flash messages for transaction confirmations

### Data Flow
1. User selects material and transaction type
2. Flask processes the form submission
3. Excel file is updated using openpyxl
4. Current stock is recalculated
5. User interface is updated with confirmation
6. Changes are immediately available for download

## Troubleshooting

### Common Issues

**Excel file not found**
- Ensure ISSUES.xlsx is in the same directory as app.py
- Check file permissions

**Download not working**
- Verify Flask has read access to the Excel file
- Check browser download settings

**Transactions not saving**
- Ensure Excel file is not open in another application
- Verify write permissions on the file

### Error Messages
The application provides user-friendly error messages for:
- File access issues
- Invalid data entries
- Excel format problems
- Download failures

## 🔧 Build & Deployment

### Local Development
```bash
# 1. Clone repository
git clone https://github.com/MRASIYA/DailyCountingRMC.git
cd DailyCountingRMC

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run application
python excel_app.py

# 5. Open browser
# http://localhost:5000
```

### Production Deployment

#### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build manually
docker build -t daily-counting .
docker run -p 5000:5000 -v $(pwd)/ISSUES.xlsx:/app/ISSUES.xlsx daily-counting
```

#### GitHub Actions CI/CD
- Automated testing on push/PR
- Docker image building
- GitHub Pages deployment
- Quality checks and validation

### Build Status
- ✅ **Tests**: Automated testing with GitHub Actions
- ✅ **Docker**: Production-ready containerization
- ✅ **Pages**: Live demo deployment
- ✅ **Excel**: Direct file integration testing

## 📚 Documentation

- **[Installation Guide](INSTALLATION_GUIDE.md)** - Detailed setup instructions
- **[Excel Template Guide](EXCEL_TEMPLATE_GUIDE.md)** - Excel file format requirements
- **[API Documentation](#api-endpoints)** - REST API reference
- **[Docker Guide](Dockerfile)** - Container deployment

### API Endpoints
```
GET  /                    # Main web interface
GET  /api/materials       # Get all materials
GET  /api/stock          # Get current stock levels
POST /api/transaction    # Add new transaction
GET  /download           # Download Excel file
```

## Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## 🎯 Project Structure
```
DailyCountingRMC/
├── .github/
│   └── workflows/
│       └── build-and-test.yml    # CI/CD pipeline
├── docs/                         # GitHub Pages files
│   ├── index.html               # Static demo
│   ├── materials.json           # Materials data
│   └── stock_data.json          # Stock data
├── templates/
│   ├── index.html               # Original Flask template
│   └── excel_interface.html     # Enhanced Excel interface
├── DailyStockApp/               # Mobile app (Cordova)
├── app.py                       # Original Flask app
├── excel_app.py                 # Enhanced Excel integration
├── local_app.html               # Standalone HTML version
├── excel_to_json.py             # Excel to JSON converter
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── docker-compose.yml           # Docker Compose setup
├── .gitignore                   # Git ignore rules
└── ISSUES.xlsx                  # Your inventory data
```

## 🚀 Future Enhancements
- User authentication system
- Transaction history logging
- Bulk import/export operations
- Advanced reporting dashboard
- Real-time data visualization
- Multi-user collaboration
- Mobile app improvements
- Cloud deployment options

## License
This project is created for internal inventory management purposes.

---

**Daily Counting** - Streamlining your inventory management with modern web technology.

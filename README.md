# Daily Counting - Inventory Management Web Application

A modern Flask web application for managing daily inventory transactions with an intuitive user interface.

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

## Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Future Enhancements
- User authentication
- Transaction history logging
- Bulk operations
- Advanced reporting
- Data visualization

## License
This project is created for internal inventory management purposes.

---

**Daily Counting** - Streamlining your inventory management with modern web technology.

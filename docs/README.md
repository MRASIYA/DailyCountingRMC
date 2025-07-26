# Daily Counting - Inventory Management System

A modern web-based inventory management system for tracking daily stock movements.

## 🌐 Live Demo

Visit the live demo: [Your GitHub Pages URL will be here]

## 📋 Features

- **Material Management**: Track different materials with unique codes
- **Transaction Types**: Support for Issues, Received, and Return transactions
- **Real-time Updates**: Live updates to stock levels
- **Modern UI**: Beautiful, responsive design with animations
- **Excel Integration**: (Full version) Direct integration with Excel files

## 🚀 Demo Version

This GitHub Pages version is a **static demo** that showcases the user interface and basic functionality. The demo includes:

- Interactive form for adding transactions
- Live table updates with demo data
- All visual effects and animations
- Responsive design for mobile and desktop

### Demo Data
The demo uses sample materials:
- Steel Bars (MAT001)
- Concrete Mix (MAT002)
- Wood Planks (MAT003)
- Paint (MAT004)
- Screws (MAT005)

## 💻 Full Version Features

The complete Python Flask application includes:

- **Excel File Integration**: Direct read/write to ISSUES.xlsx
- **Data Persistence**: All transactions saved permanently
- **File Download**: Download updated Excel files
- **Error Handling**: Robust file locking and backup systems
- **API Endpoints**: RESTful API for external integrations

## 📁 Project Structure

```
DailyCountingRMC/
├── docs/                    # GitHub Pages files
│   ├── index.html          # Static demo version
│   └── README.md           # This file
├── app.py                  # Flask application
├── templates/              # Flask templates
├── requirements.txt        # Python dependencies
└── ISSUES.xlsx            # Excel data file
```

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript, Bulma CSS Framework
- **Backend**: Python Flask (full version)
- **Data Storage**: Excel files via pandas and openpyxl
- **Icons**: Font Awesome
- **Animations**: CSS keyframe animations

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones

## 🎨 Design Features

- **Gradient Backgrounds**: Modern gradient color schemes
- **Smooth Animations**: CSS keyframe animations throughout
- **Interactive Elements**: Hover effects and transitions
- **Visual Feedback**: Success messages and loading indicators
- **Accessibility**: Proper contrast and semantic HTML

## 🔧 Setup Instructions

### For GitHub Pages (Demo):
1. Fork this repository
2. Enable GitHub Pages in repository settings
3. Set source to `docs` folder
4. Visit your GitHub Pages URL

### For Full Version:
1. Clone the repository
2. Install Python dependencies: `pip install -r requirements.txt`
3. Run the Flask app: `python app.py`
4. Open `http://localhost:5000` in your browser

## 📊 Use Cases

Perfect for:
- Construction material tracking
- Warehouse inventory management
- Daily stock counting operations
- Material issue and return tracking
- Small to medium business inventory

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: This is the demo version hosted on GitHub Pages. For the full functionality with Excel integration, please use the Python Flask version.

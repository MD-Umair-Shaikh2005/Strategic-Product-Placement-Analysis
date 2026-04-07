# Strategic Product Placement Analysis

A comprehensive data analytics project analyzing the impact of product positioning on sales performance and consumer behavior using Flask and interactive visualizations.

## 📋 Project Overview

This project provides actionable insights on product placement strategies through data-driven analysis. It combines:
- **Data Processing**: Automated dataset cleaning and preparation
- **Interactive Visualizations**: 8+ visualizations powered by Plotly
- **Web Dashboard**: Real-time analytics dashboard built with Flask
- **Insights & Recommendations**: Data-driven strategic recommendations
- **Story Mode**: Narrative-driven presentation of findings

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Strategic-Product-Placement-Analysis.git
   cd Strategic-Product-Placement-Analysis
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare your dataset**
   - Obtain dataset from [Kaggle](https://www.kaggle.com/datasets/amitvkulkarni/impact-of-product-positioning-on-sales)
   - Place CSV file in the `data/` directory as `product_placement_data.csv`
   - Or upload via the web interface after starting the app

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the dashboard**
   - Open browser and navigate to: `http://localhost:5000`
   - Upload your dataset or use the sample data

## 📁 Project Structure

```
Strategic-Product-Placement-Analysis/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── data/                 # Dataset directory
│   └── product_placement_data.csv
├── scripts/
│   ├── data_preparation.py    # Data cleaning & processing
│   └── visualizations.py       # Visualization generation
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   ├── dashboard.html   # Main dashboard
│   ├── story.html       # Story/presentation
│   ├── insights.html    # Insights & recommendations
│   └── error.html       # Error page
├── static/
│   ├── css/
│   │   └── style.css    # Custom styling
│   └── js/
│       └── main.js      # JavaScript utilities
└── README.md            # This file
```

## 📊 Features

### 1. Data Processing
- ✅ Automatic dataset loading and validation
- ✅ Missing value handling
- ✅ Duplicate removal
- ✅ Data type conversion
- ✅ Statistical summaries

### 2. Visualizations (8+ Interactive Charts)
1. **Sales by Placement** - Comparative sales across locations
2. **Category Performance** - Sales metrics by product category
3. **Placement Efficiency** - Sales-per-unit analysis
4. **Sales Trend** - Temporal sales patterns
5. **Customer Demographics** - Regional and demographic insights
6. **Placement × Category Heatmap** - Performance matrix
7. **Profit Analysis** - Profit distribution by placement
8. **Transaction Metrics** - Average transaction values

### 3. Interactive Dashboard
- Real-time analytics with responsive design
- KPI cards showing key metrics
- Interactive filters and drill-down capabilities
- Dynamic visualization updates

### 4. Story Mode
- **5-Scene Narrative Journey**:
  1. Problem Statement
  2. Data Insights
  3. Patterns & Trends
  4. Key Findings
  5. Strategic Recommendations

### 5. Insights & Recommendations
- Key finding summaries
- Actionable business recommendations
- Implementation roadmap
- ROI projections
- Success metrics

## 🔧 Configuration

Edit `config.py` to customize:
- Application port and debug mode
- Dataset paths
- File size limits
- Environment-specific settings

```python
class Config:
    DEBUG = False
    PORT = 5000
    DATASET_PATH = 'data/product_placement_data.csv'
```

## 📈 Dataset Requirements

Your CSV should include columns such as:
- **Sales Metrics**: `Sales`, `Profit`, `Quantity`, `Discount`
- **Location Data**: `Placement`, `Region`, `Store`, `Category`
- **Customer Data**: `CustomerAge`, `Segment`, `Demographics`
- **Temporal Data**: `Date`, `Month`, or similar timestamp field

## 🎯 Use Cases

### Retail & Consumer Goods
- Optimize shelf placement strategies
- Identify high-performing product locations
- Maximize revenue from store layout

### E-commerce
- Optimize product positioning on website
- Improve category browsing experience
- Increase cross-sell opportunities

### Film & Television
- Analyze product placement effectiveness
- Measure audience engagement
- Optimize brand partnerships

## 🔍 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/dashboard` | GET | Main analytics dashboard |
| `/story` | GET | Story presentation |
| `/insights` | GET | Insights & recommendations |
| `/api/data-info` | GET | Dataset information |
| `/api/statistics` | GET | Statistical summary |
| `/api/visualization/<name>` | GET | Individual visualization |
| `/upload` | POST | Upload CSV file |

## 📊 Sample Output

Once data is uploaded, you'll see:
- **8+ Interactive visualizations** with hover details
- **KPI cards** showing top metrics
- **Heatmaps** revealing patterns
- **Trend charts** showing performance over time

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production (Gunicorn)
```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
```

### Docker (Optional)
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

## 📝 Documentation

Complete documentation is available in:
- **Data Processing**: [scripts/data_preparation.py](scripts/data_preparation.py)
- **Visualizations**: [scripts/visualizations.py](scripts/visualizations.py)
- **Flask Routes**: [app.py](app.py)

## 🤝 Contributing

To contribute:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- Dataset: [Kaggle - Impact of Product Positioning on Sales](https://www.kaggle.com/datasets/amitvkulkarni/impact-of-product-positioning-on-sales)
- Framework: Flask and Plotly
- Styling: Bootstrap 5

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [your-email]

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Plotly Python Guide](https://plotly.com/python/)
- [Pandas Data Analysis](https://pandas.pydata.org/docs/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Status**: Active Development

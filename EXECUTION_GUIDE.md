# 🚀 Execution Guide

## Option 1: Automated Setup (Recommended)

### Step 1: Run Setup Script
```bash
cd "c:\Users\mridu\Desktop\material hub\Strategic-Product-Placement-Analysis"
python setup.py
```

This will:
- ✅ Check Python 3.8+
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Create .env configuration
- ✅ Prepare data directory

### Step 2: Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Step 3: Download Dataset
**Option A: Automatic Download (requires Kaggle API)**
```bash
python download_dataset.py
```

**Option B: Manual Download**
1. Visit: https://www.kaggle.com/datasets/amitvkulkarni/impact-of-product-positioning-on-sales
2. Download CSV file
3. Place in `data/` folder as `product_placement_data.csv`

**Option C: Upload via Web Interface**
- Just start the app and upload the file through the browser interface

### Step 4: Start Application
```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

### Step 5: Access Dashboard
Open your browser and navigate to:
```
http://localhost:5000
```

---

## Option 2: Manual Setup

### Step 1: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Prepare Environment
```bash
copy .env.example .env
```

### Step 4: Start Application
```bash
python app.py
```

---

## 📋 Testing the Application

### Test 1: Home Page
- Navigate to `http://localhost:5000`
- Verify you see the upload form
- Check that all navigation links work

### Test 2: Upload Dataset
1. Download sample dataset from Kaggle
2. Go to home page
3. Click "Upload Dataset"
4. Select CSV file
5. Click "Upload"
6. Wait for confirmation message

### Test 3: Dashboard
1. After upload, navigate to Dashboard
2. Verify all 8 visualizations load
3. Check KPI cards for values
4. Try hovering over charts for details

### Test 4: Story
1. Click "Story" in navigation
2. Click through all 5 scenes
3. Verify visualizations render correctly

### Test 5: Insights
1. Click "Insights"
2. Scroll through recommendations
3. Expand accordion items
4. Check implementation roadmap

---

## 🔍 Troubleshooting

### Issue: Python not found
**Solution**: Ensure Python 3.8+ is installed and added to PATH
```bash
python --version
```

### Issue: Module not found (pip packages)
**Solution**: Make sure virtual environment is activated
```bash
# Windows
venv\Scripts\activate

# Should see (venv) in terminal prompt
```

### Issue: Port 5000 already in use
**Solution**: Change port in app.py or terminate process using port 5000

### Issue: CSV upload fails
**Solution**: Check:
- File is in CSV format
- File has required columns (Sales, Placement, Category, etc.)
- File size is under 16MB

### Issue: Visualizations don't load
**Solution**: 
- Check browser console for errors (F12)
- Verify data has correct column names
- Check that Plotly is loaded (should be in page source)

---

## 📊 Project Structure Verification

After setup, your project should look like:
```
Strategic-Product-Placement-Analysis/
├── venv/                      (Virtual environment)
├── data/                      (Dataset directory)
├── scripts/                   (Python modules)
│   ├── __init__.py
│   ├── data_preparation.py
│   └── visualizations.py
├── templates/                 (HTML files)
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── story.html
│   ├── insights.html
│   └── error.html
├── static/                    (CSS & JS)
│   ├── css/style.css
│   └── js/main.js
├── app.py                     (Main application)
├── config.py                  (Configuration)
├── requirements.txt           (Dependencies)
├── .env                       (Environment variables)
├── .env.example              (Template)
├── .gitignore                (Git ignore)
├── README.md                 (Documentation)
├── CHANGELOG.md              (Project status)
├── setup.py                  (Setup script)
├── download_dataset.py       (Dataset downloader)
└── EXECUTION_GUIDE.md       (This file)
```

---

## 🎯 Main Features to Test

### 1. Dashboard Features
- [ ] All 8 visualizations render
- [ ] KPI cards show data
- [ ] Charts are interactive (hover, zoom)
- [ ] Responsive on mobile

### 2. Story Features
- [ ] All 5 scenes accessible
- [ ] Scene buttons work
- [ ] Visualizations embedded in scenes
- [ ] Styling looks professional

### 3. Insights Features
- [ ] 5 recommendations expand/collapse
- [ ] Timeline displays correctly
- [ ] ROI projections visible
- [ ] Success metrics shown

### 4. API Endpoints
- [ ] `/api/data-info` returns JSON
- [ ] `/api/statistics` returns stats
- [ ] `/api/visualization/sales_by_placement` returns chart

---

## 🌐 Accessing the Application

Once running, access these routes:

| URL | Purpose |
|-----|---------|
| http://localhost:5000 | Home & Upload |
| http://localhost:5000/dashboard | Analytics Dashboard |
| http://localhost:5000/story | Story Presentation |
| http://localhost:5000/insights | Insights & Recommendations |
| http://localhost:5000/api/data-info | Data Info (JSON) |
| http://localhost:5000/api/statistics | Statistics (JSON) |

---

## 💾 File Upload Requirements

### Valid CSV Format
- Delimiter: comma (,)
- Encoding: UTF-8
- Size: < 16MB
- Rows: Recommended 100+

### Required Columns (at least some of):
```
Sales, Profit, Quantity, Discount
Placement, Category, Region, Store
Date/Month
Customer demographics
```

### Example Structure:
```csv
Date,Placement,Category,Sales,Quantity,Profit,Region,Store
2024-01-01,Shelf,Electronics,150.50,5,45.15,North,Store-1
2024-01-01,EndCap,FMCG,320.75,12,96.23,South,Store-2
...
```

---

## 📈 Performance Tips

### Optimize for Speed:
1. Use datasets with < 100k rows for optimal performance
2. Close unnecessary browser tabs
3. Use Chrome or Firefox for best visualization rendering
4. Ensure Flask debug mode is OFF in production

### Memory Usage:
- Typical dataset (10k rows): ~50MB RAM
- Large dataset (100k rows): ~200MB RAM
- With visualizations: Add ~100MB

---

## 🔒 Production Deployment

For deploying to production:

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app

# Or with specific timeout
gunicorn --workers 4 --timeout 120 --bind 0.0.0.0:5000 app:app
```

Don't forget to:
- [ ] Set `DEBUG = False` in .env
- [ ] Change `SECRET_KEY` 
- [ ] Use environment variables for sensitive data
- [ ] Set up HTTPS/SSL
- [ ] Configure CORS if needed

---

## 📞 Getting Help

If you encounter issues:

1. **Check the logs**: Look at Flask terminal output
2. **Check browser console**: Open DevTools (F12) → Console
3. **Verify data**: Ensure CSV has required columns
4. **Reset app**: Clear browser cache and restart Flask
5. **Review files**: Check config.py and app.py for any custom settings

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Ready to Run**: ✅ Yes

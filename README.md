# Placement Prediction Web Application

A clean and modern web application that predicts placement outcomes based on IQ and CGPA using a machine learning model.

## Features

- Clean, modern UI with gradient design
- Real-time form validation
- Loading animations
- Success/failure result indicators
- Responsive design
- Error handling

## File Structure

```
project/
│
├── app.py                      # Flask backend
├── placement_model.pkl         # ML model (pickle file)
├── templates/
│   └── index.html             # Frontend HTML
├── static/
│   └── css/
│       └── style.css          # Styling
└── README.md
```

## Requirements

```bash
pip install flask numpy scikit-learn
```

## How to Run

1. Make sure `placement_model.pkl` is in the same directory as `app.py`

2. Install dependencies:
   ```bash
   pip install flask numpy scikit-learn
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. Enter your IQ score in the first input field
2. Enter your CGPA (0-10) in the second input field
3. Click "Predict Placement" button
4. View the prediction result:
   - Green box with ✓: "You will get placed"
   - Red box with ✗: "You will not get placed"

## Model Format

The application expects a pickle file (`placement_model.pkl`) containing a trained scikit-learn model with:
- Input features: [IQ, CGPA]
- Output: Binary classification (1 = Placed, 0 = Not Placed)

## Notes

- CGPA must be between 0 and 10
- Both IQ and CGPA must be positive numbers
- The model file must be in the same directory as app.py

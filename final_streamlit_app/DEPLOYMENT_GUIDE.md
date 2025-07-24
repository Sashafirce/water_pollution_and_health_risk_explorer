# 🚀 Heroku Deployment Guide for Water Pollution & Health Risk Explorer

## Prerequisites
1. **Heroku Account**: Sign up at [heroku.com](https://heroku.com)
2. **Heroku CLI**: Download from [devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)
3. **Git**: Ensure Git is installed on your system

## Files Ready for Deployment ✅
- `water_pollution_app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `Procfile` - Heroku process configuration
- `setup.sh` - Streamlit configuration script
- `runtime.txt` - Python version specification
- `final_dataset_with_predictions.csv` - Dataset file
- `.gitignore` - Git ignore patterns

## Step-by-Step Deployment Instructions

### 1. Initialize Git Repository
```bash
# Navigate to your app directory
cd "final_streamlit_app"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit - Water Pollution Health Risk Explorer"
```

### 2. Login to Heroku
```bash
# Login to Heroku
heroku login
```

### 3. Create Heroku App
```bash
# Create a new Heroku app (replace 'your-app-name' with desired name)
heroku create water-pollution-health-explorer

# Or let Heroku generate a random name
heroku create
```

### 4. Deploy to Heroku
```bash
# Push to Heroku
git push heroku main

# If your default branch is 'master':
git push heroku master
```

### 5. Open Your App
```bash
# Open the deployed app in browser
heroku open
```

## Alternative: Deploy via GitHub Integration

### Option A: Using Heroku Dashboard
1. Go to [dashboard.heroku.com](https://dashboard.heroku.com)
2. Click "New" → "Create new app"
3. Enter app name: `water-pollution-health-explorer`
4. Choose region and click "Create app"
5. In "Deployment method", select "GitHub"
6. Connect your GitHub repository
7. Enable "Automatic deploys" if desired
8. Click "Deploy Branch"

### Option B: Push to GitHub First
```bash
# Create GitHub repository and push
git remote add origin https://github.com/yourusername/water-pollution-health-explorer.git
git branch -M main
git push -u origin main
```

## Environment Variables (if needed)
If you need to set environment variables:
```bash
heroku config:set VARIABLE_NAME=value
```

## Troubleshooting

### Common Issues:
1. **Build fails**: Check `requirements.txt` for correct package versions
2. **App crashes**: Check logs with `heroku logs --tail`
3. **File not found**: Ensure `final_dataset_with_predictions.csv` is in the repository

### Useful Heroku Commands:
```bash
# View logs
heroku logs --tail

# Restart app
heroku restart

# Check app status
heroku ps

# Open app in browser
heroku open

# Scale dynos (if needed)
heroku ps:scale web=1
```

## App URL
After deployment, your app will be available at:
`https://your-app-name.herokuapp.com`

## Cost
- Heroku offers a free tier with limited hours
- For production use, consider upgrading to a paid plan

## Next Steps
1. Test all functionality on the deployed app
2. Share your app URL with stakeholders
3. Consider setting up custom domain if needed
4. Monitor app performance and logs

---
🎉 **Congratulations! Your Water Pollution & Health Risk Explorer is now live on Heroku!**

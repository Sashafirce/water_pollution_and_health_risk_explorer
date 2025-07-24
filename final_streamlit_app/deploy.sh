#!/bin/bash

echo "🚀 Water Pollution Health Risk Explorer - Heroku Deployment Script"
echo "=================================================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
fi

# Add and commit files
echo "📝 Adding files to Git..."
git add .
git status

echo "💾 Committing changes..."
git commit -m "Deploy Water Pollution Health Risk Explorer to Heroku"

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI not found. Please install it first:"
    echo "   https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

# Login to Heroku
echo "🔐 Logging into Heroku..."
heroku login

# Create Heroku app
echo "🏗️  Creating Heroku app..."
read -p "Enter app name (or press Enter for auto-generated): " app_name

if [ -z "$app_name" ]; then
    heroku create
else
    heroku create "$app_name"
fi

# Deploy to Heroku
echo "🚀 Deploying to Heroku..."
git push heroku main

# Open the app
echo "🎉 Opening deployed app..."
heroku open

echo "✅ Deployment complete!"
echo "📊 Check your app status with: heroku ps"
echo "📝 View logs with: heroku logs --tail"

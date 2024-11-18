"Custom-Email-Sender-Breakout-AI-Assessment" 
A Flask-based application to schedule and send emails using Google Sheets as the data source. 
This project supports email throttling, analytics, and real-time updates via a dashboard.

Features:-
Schedule emails using data from Google Sheets.

Real-time analytics: View total emails sent, failed, pending, and scheduled.

Throttling support: Limit the number of emails sent per minute.

Integration with Sendinblue as the Email Service Provider (ESP).

Setup and Configuration Instructions
1. Prerequisites
Install Python (version 3.7+).

Install pip for package management.

A openai api account (to obtain an API key).

A Google Cloud account with access to the Google app passwords API.

2. Install Dependencies
Create and activate a virtual environment: python -m venv venv

source venv/bin/activate # On Windows: venv\Scripts\activate

Install required Python packages:

pip install -r requirements.txt

3. Obtain API Keys:
Openai API Key:

Log in to your openai api account.

API under the settings.

Generate an API key and copy it.

4.Configuartion
create .env file for storing secutity keys

Here we even add AI bot assistant which can customize the data and use for more implementation of data.


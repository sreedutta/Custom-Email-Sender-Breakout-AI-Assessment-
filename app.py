from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, EmailLog
from flask_mail import Mail, Message
from config import Config
import openai

app = Flask(__name__)
openai.api_key = "your openai_api key"
app.config.from_object(Config)


#configuration for email server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your email @example.com'
app.config['MAIL_PASSWORD'] = 'your mail_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

#create email instance

mail = Mail(app)

# Initialize database
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template("index.html")
global total_failed
total_failed=0
@app.route('/send_email', methods=["GET", "POST"])
def send_email():
    if request.method == "POST":
        recipient = request.form.get("recipient")
        subject = request.form.get("subject")
        body = request.form.get("body")
        

        # Simulate email sending (Replace this with actual email logic)
        try:
            # Simulate email sending logic here (e.g., SMTP or ESP API)
            msg = Message(subject=subject, sender=recipient, recipients=[recipient])
            msg.body = body
            mail.send(msg)
            
            email_log = EmailLog(recipient=recipient, subject=subject)
            db.session.add(email_log)
            db.session.commit()
            flash("Email sent successfully!", "success")
            return 'Email sent successfully'
        except Exception as e:
            total_failed+=1
            flash(f"Error sending email: {str(e)}", "danger")
        return redirect(url_for("send_email"))
    return render_template("send_email.html")

@app.route('/dashboard')
def dashboard():
    total_emails = EmailLog.query.count()
    total_sent = EmailLog.query.count()
    emails = EmailLog.query.order_by(EmailLog.timestamp.desc()).all()
    return render_template("dashboard.html", total_sent=total_sent, total_failed=total_failed, emails=emails)

if __name__ == '__main__':
    app.run(debug=True)

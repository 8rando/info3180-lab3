from flask import Flask, render_template
from flask_mail import Mail, Message
from app.forms import ContactForm  # Importing from the app package

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '746f2fe283918c'
app.config['MAIL_PASSWORD'] = 'fb5418e0cb007b'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        subject = form.subject.data
        sender = form.email.data
        recipients = ['your_email@example.com']
        body = f"From: {form.name.data}\nEmail: {sender}\n\n{form.message.data}"

        msg = Message(subject, sender=sender, recipients=recipients, body=body)
        mail.send(msg)

        # Redirect or notify the user that the message has been sent
        return 'Message sent successfully!', 200
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

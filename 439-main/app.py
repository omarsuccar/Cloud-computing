from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data structure to store contacts
contacts = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        # Retrieve contact details from the form
        name = request.form['name']
        email = request.form['email']
        profession = request.form['profession']
        phone = request.form['phone']
        address = request.form['address']

        # Create a contact dictionary
        contact = {'name': name, 'email': email, 'profession': profession, 'phone': phone, 'address': address}

        # Add the contact to the list
        contacts.append(contact)

        # Redirect to the contacts page
        return redirect(url_for('view_contacts'))

    return render_template('add_contact.html')

@app.route('/view_contacts')
def view_contacts():
    return render_template('view_contacts.html', contacts=contacts)

@app.route('/edit_contact/<int:index>', methods=['GET', 'POST'])
def edit_contact(index):
    if request.method == 'POST':
        # Retrieve updated contact details from the form
        name = request.form['name']
        email = request.form['email']
        profession = request.form['profession']
        phone = request.form['phone']
        address = request.form['address']

        # Update the contact in the list
        contacts[index] = {'name': name, 'email': email, 'profession': profession, 'phone': phone, 'address': address}

        # Redirect to the contacts page
        return redirect(url_for('view_contacts'))

    # Render the edit contact form
    return render_template('edit_contact.html', contact=contacts[index])

@app.route('/delete_contact/<int:index>')
def delete_contact(index):
    # Delete the contact from the list
    del contacts[index]

    # Redirect to the contacts page
    return redirect(url_for('view_contacts'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "YOUR-SECRET-KEY-HERE"  # Set a strong key in production!

# Home (Index)
@app.route('/')
def index():
    return render_template('index.html')

# About Us
@app.route('/about')
def about():
    return render_template('about.html')

# Packages list
@app.route('/packages')
def packages():
    return render_template('packages.html')

# Specific Package Details (if needed)
@app.route('/packages/<slug>')
def package_detail(slug):
    # Render a detailed package page if you create per-package templates
    template_name = f"{slug}_package.html"
    if os.path.exists(os.path.join('templates', template_name)):
        return render_template(template_name)
    return redirect(url_for('packages'))

# PDF Downloads
@app.route('/download/<filename>')
def download(filename):
    # PDFs placed in static/pdfs/
    return send_from_directory('static/pdfs', filename)

# Destinations
@app.route('/destinations')
def destinations():
    return render_template('destinations.html')

# Gallery
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Testimonials (Reviews)
@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

# Contact Form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Basic Notification - In production you would send an email, store in DB, etc.
        flash('Thank you for reaching out! Our team will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

# Serve static files for js/css/images as usual
# No extra route needed if Flask static_folder defaults to 'static'

if __name__ == '__main__':
    app.run(debug=True)

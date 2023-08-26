
def create_html_file(image_url, html_file_name):
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Image Page</title>
    </head>
    <body>
    <h1>ISRO Image</h1>
        <img src="{}" alt="Image">
    </body>
    </html>
    """

    with open(html_file_name, "w") as html_file:
        html_content = html_template.format(image_url)
        html_file.write(html_content)
        print(f"HTML file '{html_file_name}' created with image URL.")

if __name__ == "__main__":
    image_url = "https://apod.nasa.gov/apod/image/2308/Pistachio_Falls_960.jpg"  # Replace with the image URL
    html_file_name = "image_page.html"          # Choose a filename for the HTML file

    create_html_file(image_url, html_file_name)

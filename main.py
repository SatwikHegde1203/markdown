
import markdown

# Function to convert markdown to HTML
def convert_markdown_to_html(input_file_path, output_file_path):
    try:
        # Read the markdown file
        with open(input_file_path, "r") as file:
            markdown_content = file.read()

        # Convert markdown content to HTML
        html_content = markdown.markdown(markdown_content)

        # Write the HTML content to the output file
        with open(output_file_path, "w") as output_file:
            output_file.write(html_content)

        return True, output_file_path  # Conversion was successful
    except Exception as e:
        return False, str(e)  # Return error message
    

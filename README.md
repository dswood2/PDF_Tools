# PDF Tools

PDF Tools is a Python-based desktop application that provides a user-friendly interface for merging and rotating PDF files. With its intuitive design and powerful functionality, PDF Tools simplifies the process of working with multiple PDF documents.

## Features

- **PDF Merging**: Easily merge multiple PDF files into a single document. Select the desired pages from each PDF file and customize the merging order.
- **PDF Rotation**: Rotate individual pages or a range of pages within a PDF file. Choose to rotate pages left or right by 90 degrees.
- **Elegant User Interface**: PDF Tools features a modern and visually appealing user interface designed with the Tkinter library and themed using the ttkbootstrap package.
- **Thumbnail Previews**: Preview thumbnail images of PDF pages during the merging and rotation processes for better visual guidance.
- **Error Handling**: Robust error handling mechanisms ensure a smooth user experience by providing informative error messages and handling potential exceptions gracefully.
- **File Saving**: Save the merged or rotated PDF files to a desired location on your computer.

## Installation

1. Clone the repository to your local machine:
   
  - git clone https://github.com/your-username/pdf-tools.git

2. Navigate to the project directory:
   
  - cd pdf-tools

3. Install the required dependencies using pip:

  - pip install -r requirements.txt

4. Run the application:

  - python main.py

## Dependencies

PDF Tools relies on the following Python libraries:

- Tkinter: For creating the graphical user interface.
- ttkbootstrap: For applying modern and visually appealing themes to the Tkinter widgets.
- PyPDF2: For performing PDF merging and rotation operations.
- pdf2image: For converting PDF pages to image thumbnails.
- Pillow: For handling image-related operations.

Make sure to install these dependencies before running the application.

## Usage

1. Launch the PDF Tools application by running `main.py`.
2. Choose the desired operation:
- To merge PDF files, click on the "Merge PDFs" button.
- To rotate PDF pages, click on either the "Rotate Left" or "Rotate Right" button.
3. Select the PDF file(s) you want to merge or rotate.
4. In the page selection window, select the desired pages using the checkboxes next to the thumbnail previews.
5. Click on the "Merge Selected Pages" or "Rotate Selected Pages" button to proceed.
6. Choose a location to save the merged or rotated PDF file.
7. The application will display a success message upon completion.

## Contributing

Contributions to PDF Tools are welcome! If you find any bugs, have suggestions for improvements, or want to add new features, please open an issue or submit a pull request on the GitHub repository.

When contributing, please ensure that your code follows the project's coding style and conventions. Also, provide clear descriptions and explanations for your changes.

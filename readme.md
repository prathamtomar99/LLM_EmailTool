# Gmail Toolkit Setup

This project helps you interact with Gmail APIs.
Follow the steps below to set up and run the toolkit.

## Setup Instructions

### 1. Create a Python Virtual Environment
Open your terminal in the project directory and run:

```bash
python -m venv venv
```

Activate the virtual environment:

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies
Install required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Follow Setup Instructions
Open the documentation:

See `DOC/gmail_toolkit.pdf`

Follow any configuration steps mentioned.

### 4. Add Credentials
Obtain the downloaded Gmail API JSON credentials.

Copy and paste (or rename) the file as:
```
credentials.json
```

Place `credentials.json` in the project's root directory.

### 5. Run the Initial Setup Notebook
Open and run the initial setup Jupyter notebook:

```bash
jupyter notebook jaon_file.ipynb
```

Follow the prompts in the notebook.

### 6. Authorize with Gmail
A browser window will open; log in using the same Gmail ID for which you downloaded the credentials.

If you encounter any error, refer to the documentation in:
```
DOC/errors.pdf
```

### 7. (Troubleshooting) OAuth Test Users
If you're stuck with authentication:

- Check the Audience tab (OAuth) in your Google Cloud project.
- Ensure your email ID is listed as a "test user."
- Refer to `DOC/errors.pdf` for more error resolutions.

### 8. Run the Main Script
Once you have successfully generated token.json (after authorization), run:

```bash
python main.py
```

## Important Note

Do **NOT** share or commit your `credentials.json` or `token.json` files to public repositories.

If you face issues, consult the PDF documentation in the `DOC/` folder.
# My Work Showcase

This is a static website hosted on GitHub Pages.

## Project Setup

To run this project locally, please follow these steps:

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   uvicorn api.index:app --reload
   ```

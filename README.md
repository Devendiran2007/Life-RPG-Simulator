# Life RPG Simulator

A gamified life simulator where you level up by completing real-life tasks.

## Setup

1.  Clone the repository.
2.  Create a virtual environment:
    ```bash
    python -m venv myvenv
    ```
3.  Activate the virtual environment:
    -   Windows: `myvenv\Scripts\activate`
    -   macOS/Linux: `source myvenv/bin/activate`
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Database Setup
Ensure you have PostgreSQL installed and running.
Create a database named `life_rpg_database`.

## Running the App

```bash
uvicorn app.main:app --reload
```

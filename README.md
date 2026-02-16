# Life RPG Simulator

Welcome to the **Life RPG Simulator**! This project gamifies your life by tracking habits, quests, and user progress in an RPG style.

## Features

- **User Authentication**: Register and login securely.
- **Quest System**: Create and complete quests to earn XP.
- **Habit Tracking**: Monitor your daily habits and streaks.
- **RPG Elements**: Level up as you improve your real life!

## Tech Stack

- **Backend**: Python, FastAPI
- **Database**: PostgreSQL, SQLAlchemy
- **Authentication**: JWT, Passlib (bcrypt)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Life-RPG-Simulator.git
    cd Life-RPG-Simulator
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv myvenv
    source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    - Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    - Open `.env` and update `DATABASE_URL` with your local PostgreSQL credentials.

5.  **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```

## Usage

- Open your browser and navigate to `http://127.0.0.1:8000` to see the API root.
- Access the interactive documentation at `http://127.0.0.1:8000/docs`.

## License

[MIT License](LICENSE)

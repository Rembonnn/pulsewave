# Pulse Wave

Pulse Wave is a lightweight Python scaffolding designed for developing REST APIs with simplicity and flexibility. It includes features like environment-based database configuration, routing, CRUD operations, middleware, and JWT authentication.

## Features

- **Database Configuration**: Easily configure your database through a `.env` file.
- **Local Server**: Run a local server similar to `php artisan serve`.
- **Routing**: Supports GET, POST, PUT, and DELETE methods, with dynamic routing.
- **Models**: Includes a directory for models with support for table relationships.
- **Controllers**: Directory for controllers with typical controller behaviors.
- **Auto-Generation**: Automatically generate controllers, models, and middleware via the terminal.
- **Middleware**: Support for creating and using middleware.
- **JWT Authentication**: Includes JWT authentication with login controller and middleware.
- **Seeder**: Populate the `users` table with dummy data.

## Project Structure
```
    pulsewave/
    │
    ├── app/
    │ ├── controllers/
    │ ├── middleware/
    │ ├── models/
    │ ├── init.py
    │ └── main.py
    │
    ├── seeders/
    │ └── users_faker.py
    │
    ├── scripts/
    │ └── generate.py
    │
    ├── migrations/
    │ └── versions/
    │
    ├── .env.example
    ├── .gitignore
    ├── alembic.ini
    ├── Makefile
    ├── pulsewave.py
    ├── requirements.txt
    └── README.md
```

# Simplified-PLC

Simplified PLC is a nonprofit/passion project aimed towards advancing the quality of students’ education in public K-12 schools. They aim to do so by empowering teachers to create Professional Learning Communities (PLCs), where teachers get into teams to discuss learning strategies for students, implement those strategies, analyze the results, and then refine strategies based on those results. Simplified PLC wants to bring clarity to the process of implementing PLCs for teachers, with the goal of empowering students’ education downstream.

## Setup

### Tools

Before starting development, make sure you have these tools installed:

- [Node.js](https://nodejs.org/en) - this is our JS runtime for the frontend and the Git hooks. The version we use is in `.nvmrc`
- [Npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) - this is our package manager for the frontend
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - this is our Python package manager for the backend. It installs the Python version in `backend/.python-version` and all backend dependencies for you
- [make](https://www.gnu.org/software/make/) - runs the backend scripts. It is already installed on macOS and most Linux distributions. On Windows, install it with `winget install ezwinports.make`, `choco install make` or `scoop install make`
- [Postman](https://www.postman.com/downloads/) - helpful for testing API routes
- [MongoDB Community](https://www.mongodb.com/docs/manual/administration/install-community/) - necessary if you want to run database locally

### Environment

To define and manage environment variables, make sure to maintain `.env` files in both the `frontend` and `backend` directories. Ensure that `.env` is specified in your root `.gitignore` file to prevent pushing secrets. This should already be the case, but the secret scanner hook will check for this if something gets changed

Add the `.env.frontend` and `.env.backend` from the project google drive to their respective directories in your local branch. (not yet created)

### Git hooks

Everyone, including developers who only work on the backend, needs to run `npm install` in the `frontend` directory once. This installs the Husky pre-commit and pre-push hooks, which run the secret scanner and the lint checks for both the frontend and the backend. This is also why Node.js is required for backend development.

1. `cd frontend`
2. Run `npm install`

### Backend

1. `cd backend`
2. Run `uv sync` to install Python and all dependencies
3. If running the database locally, make sure to [start mongod](https://www.mongodb.com/docs/manual/tutorial/manage-mongodb-processes/#start-mongod-processes). For a local database, set `MONGODB_URI=mongodb://localhost:27017/simplified-plc` in `backend/.env`
4. `make start` to start the backend

If this works properly you should see these messages in the terminal:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

Follow this [url](http://localhost:8000/docs) to see the interactive API docs.

### Frontend

1. `cd frontend`
2. Run `npm install` to install all dependencies
3. Run `npm run dev` to start development server
4. Server is started on port 3000. Follow this [url](http://localhost:3000) and you should see the development page.

## Linting

Run these commands in the `frontend` directory for linting and formatting. Be sure to run these commands before pushing to github.

- `npm run lint-fix` - fixes all auto-fixable lint errors and reformats code
- `npm run lint-check` - check all lint errors or code style issues without modifying any files

Run these commands in the `backend` directory for linting, formatting and testing. Be sure to run these commands before pushing to github.

- `make lint-fix` - fixes all auto-fixable lint errors and reformats code
- `make lint-check` - check all lint errors, code style issues and type errors without modifying any files
- `make format` - reformats code without fixing lint errors
- `make test` - runs the backend tests

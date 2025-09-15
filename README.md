# Payment API Validator

A mock payment processing API built with FastAPI and a comprehensive test suite, designed to demonstrate Quality Engineering skills for a banking context.

## Tech Stack

- **API Framework:** FastAPI (Python)
- **Testing:** Pytest, Postman
- **CI/CD:** GitHub Actions

## API Endpoints

- `POST /payments` - Submit a new payment
- `GET /payments/{payment_id}` - Retrieve payment status
- `GET /health` - Health check

## Testing Strategy

This project includes both manual and automated testing:

1.  **Manual/Exploratory Testing:** A Postman collection is provided for initial API validation and documentation (`CIBC_Payment_API_Validator.postman_collection.json`).
2.  **Automated Testing:** A Pytest suite validates positive, negative, and edge cases.
3.  **CI/CD Integration:** Tests run automatically on every commit via GitHub Actions.

## How to Run

1.  Install dependencies: `pip install -r requirements.txt`
2.  Run the server: `uvicorn main:app --reload`
3.  Test the API: Navigate to `http://127.0.0.1:8000/docs`

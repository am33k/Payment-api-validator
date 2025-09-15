from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Optional
import uuid # thi sis used to generat eunique payment id's
from enum import Enum

# we need to define the statuses a payment can have
class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

# pydantic model to define the structure of a payment request
class PaymentCreate(BaseModel):
    amount: float
    currency: str = "USD"
    from_account: str
    to_account: str
    description: Optional[str] = None

# Pydantic model to define the structure of a payment Response
class PaymentResponse(BaseModel):
    payment_id: str
    status: PaymentStatus
    amount: float
    currency: str
    from_account: str
    to_account: str
    description: Optional[str] = None

app = FastAPI(title="Payment API Validator", version="0.1.0")

# In-memory "database" to store our payments 
payments_db: Dict[str, PaymentResponse] = {}

@app.get("/")
def read_root():
    return {"message": "Payment API Validator is runningt."}

@app.get("/health")
def health_check():
    return{"status": "OK"}

# Endpoint to submit a new payment
@app.post("/payments", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(payment: PaymentCreate):
    # Generate a unique ID for the payment
    payment_id = str(uuid.uuid4())
    # Create the payment response object with a PENDING staus
    payment_response = PaymentResponse(
        payment_id=payment_id, 
        status=PaymentStatus.PENDING,
        **payment.dict()
    )

    # Save it to our "database"
    payments_db[payment_id] = payment_response

    # In a real system, here we would talk to a bank API, etc.
    # We'll simulate some processing logic by updating the status after a delay.
    # For now, we just return the created payment.

    return payment_response


# Endpoint to get status of payment
@app.get("/payments/{payment_id}", response_model=PaymentResponse)
def get_payment(payment_id: str):
    # Look up the payment in our "database"
    payment = payments_db.get(payment_id)
    # if nor found it will raise a 404 error
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    # Simulate a status update for demonstration.
    # This is where logic would decide to mark it as COMPLETED or FAILED.
    # We'll just manually set some to COMPLETED for testing.
    if payment.status == PaymentStatus.PENDING and payment.amount > 0:
        # Simple rule for demo: good payments eventually complete
        payment.status = PaymentStatus.COMPLETED
    elif payment.amount <= 0:
        # Negative amount payments fail
        payment.status = PaymentStatus.FAILED

    # Update the "database" with the new status
    payments_db[payment_id] = payment

    return payment
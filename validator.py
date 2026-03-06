from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Union

# US-007: This class enforces the 'contract' you defined in US-006
class DriverEvent(BaseModel):
    driver_id: str = Field(..., description="Must be a non-empty string")
    latitude: float = Field(..., ge=-90, le=90, description="Range: -90 to 90")
    longitude: float = Field(..., ge=-180, le=180, description="Range: -180 to 180")
    timestamp: datetime = Field(..., description="Must be a valid ISO-8601 string")

def validate_event(data):
    try:
        event = DriverEvent(**data)
        print(f"✅ Validation Passed for Driver: {event.driver_id}")
        return True
    except ValidationError as e:
        print(f"❌ Validation Failed: {e.json()}")
        return False

# Quick test case
if __name__ == "__main__":
    test_data = {
        "driver_id": "DRV-123",
        "latitude": 12.9716, # Bangalore lat
        "longitude": 77.5946,
        "timestamp": "2026-03-06T23:00:00Z"
    }
    validate_event(test_data)
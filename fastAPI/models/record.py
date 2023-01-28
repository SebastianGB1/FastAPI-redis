from pydantic import BaseModel, Field
from datetime import datetime

def generate_date():
    return str(datetime.now())

class Record(BaseModel):
    ID: str
    temperature: str
    timestamp: str = Field(default_factory = generate_date)

    def to_json(self):
        return {
            "ID":self.ID,
            "temperature": self.temperature,
            "timestamp":self.timestamp
        }

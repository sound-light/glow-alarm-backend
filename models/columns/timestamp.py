from sqlalchemy import Column, DateTime, text
from datetime import datetime

class TimeStampedModel:
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        server_default=text('CURRENT_TIMESTAMP')
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=True,
        onupdate=datetime.utcnow,
        server_onupdate=text('CURRENT_TIMESTAMP')
    )
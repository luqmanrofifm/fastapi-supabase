from db.postgres import Base
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import String, Integer, DateTime

class Book(Base):
    __tablename__ = "book"

    id = Column(
        "id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )

    title = Column("title", String, index=True)
    author = Column("author", String, index=True)
    year = Column("year", Integer, index=True)

    created_at = Column("created_at", DateTime, index=True)
    updated_at = Column("updated_at", DateTime, index=True)
    created_by = Column("created_by", String, index=True)
    updated_by = Column("updated_by", String, index=True)
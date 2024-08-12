from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from config.database import Base
import uuid
import sqlalchemy as sa
import bcrypt

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=sa.text('uuid_generate_v4()'))
    name = Column(String(length=255), nullable=False)
    email = Column(String(length=255), nullable=False, unique=True)
    password = Column(String(length=255), nullable=False)
    email_verified_at = Column(TIMESTAMP(timezone=True), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=True)

    def set_uuid_to_string(self):
        self.id = str(self.id)

    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))

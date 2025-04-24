from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database setup
DATABASE_URL = "sqlite:///health_sys.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Program table
class HealthProgram(Base):
    __tablename__ = "health_programs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    desc = Column(String, nullable=False)

# Client table
class HealthClient(Base):
    __tablename__ = "health_clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_date = Column(String, nullable=False)  # Format: YYYY-MM-DD
    contact = Column(String, nullable=False)

# Enrollment table (links clients to programs)
class EnrollmentLink(Base):
    __tablename__ = "enrollment_links"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("health_clients.id"), nullable=False)
    program_id = Column(Integer, ForeignKey("health_programs.id"), nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)
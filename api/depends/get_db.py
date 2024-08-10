from db.session import SessionLocal

#### db 연결함수 ####
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
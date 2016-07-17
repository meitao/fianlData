from sqlalchemy import create_engine
def get_engine():
    engine = create_engine('mysql://root:123456@localhost:3306/test?charset=utf8')
    return engine
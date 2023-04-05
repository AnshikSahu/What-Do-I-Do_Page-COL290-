from sqlalchemy import create_engine
db_connection_string= "mysql+pymysql://9s68i8b2dldfaobfc7dw:pscale_pw_Qb9qRMvqtFJLQENOKCagTDGOSCUbR1a4BZJYSGmP9Oz@aws.connect.psdb.cloud/bijoy?charset=utf8mb4"
engine = create_engine(db_connection_string,connect_args={ "ssl" :{ "ca" :  "/etc/ssl/cert.pem" }})

# with engine.connect() as conn:
#     conn.execute(text( DROP TABLE user ))
#     conn.execute(text( CREATE TABLE user(username varchar(200),password varchar(200)) ))
#     conn.execute(text( INSERT INTO user (username,password) VALUES('Adithya','Bijoy') ))



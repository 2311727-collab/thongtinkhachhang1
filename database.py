import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-4fe7edc-dlu-9603.c.aivencloud.com",

        port=21209,

        user="avnadmin",

        password="AVNS_F_zFNT0ugsV0cJd0ZkZ",

        database="company",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn

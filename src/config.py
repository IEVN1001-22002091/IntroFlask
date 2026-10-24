class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='diana'
    MYSQL_PASSWORD='aelyn'
    MYSQL_DB='api_utl'
    MYSQL_CURSORCLASS = 'Cursor'

config={
    'development': DevelopmentConfig
}
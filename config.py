from redis import StrictRedis


class Config(object):
    '''项目的配置'''
    SECRET_KEY = "s/KftNY1GycFsr3qnYOpFhiTGXHgQoc3xDfvN9F970nWAaAfxv737ghi0SVVadzw"
    # 为mysql添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Redis的配置
    REDIS_HOST = "10.0.0.11"
    REDIS_PORT = 6379
    # Session保存位置
    SESSION_TYPE = "redis"
    # 开启Session签名
    SESSION_USE_SIGNER = True
    # 指定Session保存到redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


class DevelopmentConfig(Config):
    '''开发环境的配置'''
    DEBUG = True


class ProductionConfig(Config):
    '''生产环境的配置'''
    DEBUG = False


class TestingConfig(Config):
    '''单元测试环境的配置'''
    DEBUG = True
    Testing = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}

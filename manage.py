from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
# 可以用来指定Session保存的位置
from flask_session import Session
from flask_script import Manager
# 集成数据迁移
from flask_migrate import Migrate, MigrateCommand
from config import Config

app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启当前项目CSRF保护，只做服务器验证功能
CSRFProtect(app)
# 设置Session保存指定位置
Session(app)
manager = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session['name'] = 'python'
    return 'Index Page'


if __name__ == '__main__':
    manager.run()

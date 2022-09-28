import json
import os
import time
from functools import wraps

from flask import Flask, send_file, request, make_response, Response
from flask_cors import CORS

app = Flask(__name__)

CORS(app, supports_credentials=True, resources=r"/*")

# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 统计函数执行时间的装饰器
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print('timeit: %s cost %s' % (func.__name__, time.time() - start))
        return result

    return wrapper


@app.route('/')
def index():
    return 'INDEX!'


@timeit
@app.route('/files', methods=['GET', 'POST'], endpoint='files')
def file_api():
    """文件接口，客户端访问以获得可下载文件列表或下载文件"""
    if request.method == 'GET':
        files_storage_dir = os.path.join(BASE_DIR, 'files_storage')
        # 获取文件列表
        files_list = os.listdir(files_storage_dir)
        if files_list:
            data = {
                'code': 200,
                'msg': 'OK',
                'files_list': files_list
            }
            return json.dumps(data)
        else:
            data = {
                'code': 404,
                'msg': 'No files found',
                'files_list': []
            }
            return json.dumps(data)

    if request.method == 'POST':
        # 方式一：使用send_file，实现普通的下载接口，点击下载后，文件会直接下载到本地
        # 获取文件名
        file_name = request.form.get('filename')
        # 获取文件路径
        file_path = os.path.join(BASE_DIR, 'files_storage', file_name)
        # 直接返回文件
        response = make_response(send_file(file_path, as_attachment=True))
        return response

        # 方式二：使用文件流的方式，实现文件下载接口
        # filename = request.form.get('filename')
        #
        # def send_chunk():  # 流式读取
        #     file_path = os.path.join(BASE_DIR, 'files_storage/', filename)
        #     with open(file_path, 'rb') as target_file:
        #         while True:
        #             chunk = target_file.read(20 * 1024 * 1024)
        #             if not chunk:
        #                 break
        #             yield chunk
        # # 流式返回文件
        # return Response(send_chunk(), content_type='application/octet-stream')


if __name__ == '__main__':
    app.run()

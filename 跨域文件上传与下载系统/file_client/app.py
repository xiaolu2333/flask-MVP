import os
import time
from functools import wraps

import requests

from flask import Flask, request, render_template

app = Flask(__name__)

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
    return render_template('index.html')
    # url = 'http://127.0.0.1:8000/files'
    # response = requests.get(url)
    # files_list = response.json().get('files_list')
    # return render_template('index.html', filesName=files_list)


@timeit
@app.route('/download', methods=['GET', 'POST'], endpoint='download')
def download():
    """仅用于获取可用文件名列表"""
    url = 'http://172.28.79.101:8000/files'
    response = requests.get(url)
    files_list = response.json().get('files_list')
    return render_template('download.html', filesName=files_list)


@timeit
@app.route('/upload', methods=['GET', 'POST'], endpoint='upload')
def upload():
    return render_template('upload.html')
    # url = 'http://127.0.0.1:8000/files'
    # response = requests.get(url)
    # files_list = response.json().get('files_list')
    # return render_template('upload.html', filesName=files_list)


# @app.route('/file/upload', methods=['POST'])
# def upload_part():  # 接收前端上传的一个分片
#     task = request.form.get('task_id')  # 获取文件的唯一标识符
#     chunk = request.form.get('chunk', 0)  # 获取该分片在所有分片中的序号
#     filename = '%s%s' % (task, chunk)  # 构造该分片的唯一标识符
#
#     upload_file = request.files['file']
#     file_path = os.path.join(BASE_DIR, 'uploaded_files/', filename)
#     upload_file.save(file_path)  # 保存分片到本地
#     return render_template('./index.html')
#
#
# @app.route('/file/merge', methods=['GET'])
# def upload_success():  # 按序读出分片内容，并写入新文件
#     target_filename = request.args.get('filename')  # 获取上传文件的文件名
#     task = request.args.get('task_id')  # 获取文件的唯一标识符
#     chunk = 0  # 分片序号
#     file_path = os.path.join(BASE_DIR, 'uploaded_files/', target_filename)
#     with open(file_path, 'wb') as target_file:  # 创建新文件
#         while True:
#             try:
#                 filename = os.path.join(BASE_DIR, 'uploaded_files/') + '%s%d' % (task, chunk)
#                 source_file = open(filename, 'rb')  # 按序打开每个分片
#                 target_file.write(source_file.read())  # 读取分片内容写入新文件
#                 source_file.close()
#             except IOError:
#                 break
#
#             chunk += 1
#             os.remove(filename)  # 删除该分片，节约空间
#
#     return render_template('./index.html')


# @app.route('/fileslist', methods=['POST'], endpoint='fileslist')
# def get_files_list_from_server_A():
#     url = 'http://127.0.0.1:8000/files'
#     response = requests.get(url)
#     files_list = response.json().get('files_list')
#     return render_template('index.html', filesName=files_list)


# @app.route('/download', methods=['GET', 'POST'], endpoint='download')
# def download():
#     """下载文件"""
#     if request.method == 'POST':
#         server = request.form.get('server')
#         file_name = request.form.get('file_name')


if __name__ == '__main__':
    app.run()

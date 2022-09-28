#!/usr/bin/env python
# coding=utf-8

import os

from flask import Flask, request, Response, render_template as rt
from flask_cors import CORS

app = Flask(__name__)

CORS(app, supports_credentials=True, resources=r"/*")

# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # /home/dfl/learn/flask/upload-demo


@app.route('/', methods=['GET'])
def index():
    return rt('./index.html')


@app.route('/file/upload', methods=['POST'])
def upload_part():  # 接收前端上传的一个分片
    task = request.form.get('task_id')  # 获取文件的唯一标识符
    chunk = request.form.get('chunk', 0)  # 获取该分片在所有分片中的序号
    filename = '%s%s' % (task, chunk)  # 构造该分片的唯一标识符

    upload_file = request.files['file']
    file_path = os.path.join(BASE_DIR, 'uploaded_files/', filename)
    upload_file.save(file_path)  # 保存分片到本地
    return rt('./index.html')


@app.route('/file/merge', methods=['GET'])
def upload_success():  # 按序读出分片内容，并写入新文件
    target_filename = request.args.get('filename')  # 获取上传文件的文件名
    task = request.args.get('task_id')  # 获取文件的唯一标识符
    chunk = 0  # 分片序号
    file_path = os.path.join(BASE_DIR, 'uploaded_files/', target_filename)
    with open(file_path, 'wb') as target_file:  # 创建新文件
        while True:
            try:
                filename = os.path.join(BASE_DIR, 'uploaded_files/') + '%s%d' % (task, chunk)
                source_file = open(filename, 'rb')  # 按序打开每个分片
                target_file.write(source_file.read())  # 读取分片内容写入新文件
                source_file.close()
            except IOError:
                break

            chunk += 1
            os.remove(filename)  # 删除该分片，节约空间

    return rt('./index.html')


@app.route('/file/list', methods=['GET'])
def file_list():
    dir_path = os.path.join(BASE_DIR, 'uploaded_files/')
    files = os.listdir(dir_path)  # 获取文件目录
    # files = map(lambda x: x if isinstance(x, unicode) else x.decode('utf-8'), files)  # 注意编码
    return rt('./list.html', files=files)


# @app.route('/file/download/<filename>', methods=['GET'])
# def file_download(filename):
#     def send_chunk():  # 流式读取
#         file_path = os.path.join(BASE_DIR, 'downloaded_files/', filename)
#         store_path = file_path
#         with open(store_path, 'rb') as target_file:
#             while True:
#                 chunk = target_file.read(20 * 1024 * 1024)
#                 if not chunk:
#                     break
#                 yield chunk
#
#     return Response(send_chunk(), content_type='application/octet-stream')


if __name__ == '__main__':
    app.run(debug=False, threaded=True)

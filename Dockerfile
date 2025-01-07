# 使用官方Python镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 创建虚拟环境
RUN python -m venv /opt/venv

# 激活虚拟环境（通过设置PATH）
ENV PATH="/opt/venv/bin:$PATH"

# 更新pip, setuptools和wheel
RUN pip install --upgrade pip setuptools wheel

# 将当前目录的内容复制到容器中的/app目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用程序监听的端口（根据实际情况调整）
EXPOSE 5999

# 设置容器启动时运行的命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
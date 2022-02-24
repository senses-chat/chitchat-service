# 用plato-mini制作中文闲聊chatbot

以下是一个基于百度的plato-mini模型和FastAPI制作的中文闲聊API服务。

尽管paddlehub有提供便捷的serve方法，paddlehub的依赖更大，而且flask需要ASGI服务器才能支撑生产环境使用，特此使用FastAPI封装了一个简单的API服务器。

## install

```shell
pip install -r requirements.txt
# OR
pipenv install
```

## development

```shell
pipenv run uvicorn main:app --reload
```

开发服务器会在本地8000端口启动。

## API

请访问 `http://localhost:8000/docs` 或者 `http://localhost:8000/redoc` 查看API文档。


## deployment

部署推荐使用Docker部署，详细请参考Dockerfile。当前Docker镜像部署默认9000端口，便于部署到云平台的Serverless云函数服务。

## License

[Apache License 2.0](./LICENSE) since plato-mini is also under the same license.

from app import create_app


__author__ = "gaowenfeng"

app = create_app()

if __name__ == "__main__":
    print("id为" + str(id(app)) + "的app启动")
    app.run(host=app.config["HOST"], debug=app.config["DEBUG"], port=app.config["PORT"])

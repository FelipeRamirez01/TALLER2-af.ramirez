from db import create_app
from fastapi import FastAPI


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

# setup.py placed at root directory
from setuptools import setup

setup(
    name="tier_backend",
    version="0.0.0",
    author="Krisztian Gajdar",
    description="tier backend",
    install_requires=[
        "fastapi==0.105.0",
        "uvicorn==0.18.3",
        "sqlalchemy==1.4.40",
        "fastapi_sqlalchemy==0.2.1",
        "pydantic[dotenv]==1.10.0",
        "pybase62==0.5.0",
        "tenacity==8.0.1",
        "anyio==3.7.1",
        "requests==2.31.0",
        "httpx==0.25.2",
        "freezegun==1.4.0",
    ],
)

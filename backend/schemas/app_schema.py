from pydantic import BaseModel
from typing import List


class Column(BaseModel):
    name: str
    type: str


class Table(BaseModel):
    name: str
    columns: List[Column]


class Endpoint(BaseModel):
    path: str
    method: str
    table: str


class Page(BaseModel):
    name: str
    components: List[str]


class Role(BaseModel):
    name: str
    permissions: List[str]


class AppConfig(BaseModel):
    app_name: str
    tables: List[Table]
    endpoints: List[Endpoint]
    pages: List[Page]
    roles: List[Role]
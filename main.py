from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from models import Task

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods = ['*'],
    allow_headers = ['*']
)



@app.get("/tasks")
async def all():
    return [format(pk) for pk in Task.all_pks()]

def format(pk: str):
    task = Task.get(pk)
    return {
        'id': task.pk,
        'name': task.name,
        'complete': int(task.complete)
    }

@app.post('tasks')
async def create(task: Task):
    task.save()

@app.put('tasks/{pk}')
async def update(pk: str, request: Request):
    task = Task.get(pk)
    body = await request.json()
    task.complete = int(body['complete'])
    return task.save()

@app.delete('tasks/{pk}')
async def remove(pk: str):
    task = Task.get(pk)
    return task.delete(pk)
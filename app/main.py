from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="A simple CRUD API for tasks, built with FastAPI and PostgreSQL.",
    version="1.0.0",
)


@app.get("/", tags=["health"])
def health_check():
    return {"status": "ok"}


"""
app = FastAPI()


names_db = [
    {"id": 1, "name": "ali"},
    {"id": 2, "name": "maryam"},
    {"id": 3, "name": "arousha"},
]

# testing fast api


# GET (search with query parameter)
@app.get("/names")
def names_list(search: str | None = None):
    if search:
        filtered_names = [
            name for name in names_db if search.lower() in name["name"].lower()
        ]
        return filtered_names
    return names_db


# GET a specific item
@app.get("/names/{item_id}")
def names_detail(item_id: int):
    for name in names_db:
        if name["id"] == item_id:
            return name
    return {"message": "Name not found"}


# POST
@app.post("/names")
def names_create(name: str):
    new_name = {"id": random.randint(4, 100), "name": name}
    names_db.append(new_name)
    return new_name


# PUT
@app.put("/names/{item_id}")
def names_update(item_id: int, name: str):
    for n in names_db:
        if n["id"] == item_id:
            n["name"] = name
            return {"message": f"Name with ID {item_id} updated successfully"}
    return {"message": "Name not found"}


# DELETE
@app.delete("/names/{item_id}")
def names_delete(item_id: int):
    for i, n in enumerate(names_db):
        if n["id"] == item_id:
            del names_db[i]
            return {"message": f"Name with ID {item_id} deleted successfully"}
    return {"message": "Name not found"}


@app.get("/")
def read_root():
    return {"message": "Hello World"}
"""

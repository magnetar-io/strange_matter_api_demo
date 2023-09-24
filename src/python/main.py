import random

from fastapi import FastAPI

app = FastAPI()

# Random responses for stubbed out functions
async def Create_Collection(collection_name: str):
    random_responses = [
        "Collection created successfully!",
        "Oops, something went wrong while creating the collection.",
        "That collection name is already in use.",
    ]
    return random.choice(random_responses)

async def Create_Component(component_name: str):
    random_responses = [
        "Component created successfully!",
        "Oops, something went wrong while creating the component.",
        "That component name is already in use.",
    ]
    return random.choice(random_responses)

async def Add_Component_to_Collection(collection_name: str, component_name: str):
    random_responses = [
        "Component added to collection successfully!",
        "Oops, something went wrong while adding the component to the collection.",
        "That component is already in that collection.",
    ]
    return random.choice(random_responses)

@app.get("/")
async def hello_world():
    return {"message": "Hello, world!"}

@app.post("/create_collection")
async def create_collection(collection_name: str):
    response = await Create_Collection(collection_name)
    return {"message": response}

@app.get("/get_collection/{collection_name}")
async def get_collection(collection_name: str):
    # TODO: Implement this function to get the collection from the database.
    return {"collection": collection_name}

@app.post("/create_component")
async def create_component(component_name: str):
    response = await Create_Component(component_name)
    return {"message": response}

@app.get("/get_component/{component_name}")
async def get_component(component_name: str):
    # TODO: Implement this function to get the component from the database.
    return {"component": component_name}

@app.post("/add_component_to_collection")
async def add_component_to_collection(collection_name: str, component_name: str):
    response = await Add_Component_to_Collection(collection_name, component_name)
    return {"message": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8009)
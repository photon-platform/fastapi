from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class ActionRequest(BaseModel):
    input: str = Field(..., description="The input string to be processed")
    context: dict = Field(..., description="Contextual information in key-value pairs")

class ActionResponse(BaseModel):
    output: str = Field(..., description="The processed output string")
    modified_context: dict = Field(..., description="The modified context after processing")

@app.post("/action/", response_model=ActionResponse, summary="Perform Custom Action",
          description="Processes the input based on the provided context and returns the result.")
async def perform_action(request: ActionRequest):
    # Logic for the custom action
    output = f"Processed input: {request.input}"
    modified_context = {"processed": True}
    return ActionResponse(output=output, modified_context=modified_context)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


from pydantic import BaseModel


class Segment(BaseModel):
    role: str
    content: str


class Context(BaseModel):
    id: str
    segments: list[Segment]


class Provider(BaseModel):
    name: str
    model: str


class MCPRequest(BaseModel):
    context: Context
    persona: str
    instructions: list[str]
    provider: Provider


class MCPResponse(BaseModel):
    segment: Segment

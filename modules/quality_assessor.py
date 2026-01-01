"""quality_assessor module"""
from .base import LlamaClient
class QualityAssessor:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You are a helpful discussion forum moderator and assistant."
    def process(self, content: str, context: str = "") -> str:
        return self.client.generate(f"Process forum content:\n{content}\nContext: {context}\n\nProvide helpful, constructive assistance.", self.system_prompt)

import os

class Toolchain:
    def create_directory(name: str) -> str:
        try:
            os.makedirs(name)
            return f"I have created the directory '{name}'"
        except Exception as e:
            return f"I was unable to create the directory '{name}'. Reason: {e}"
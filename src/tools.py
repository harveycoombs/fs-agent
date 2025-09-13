import os

class Toolchain:
    def create_directory(name: str) -> str:
        try:
            os.makedirs(name)
            return f"I have created the directory '{name}'"
        except Exception as e:
            return f"I was unable to create the directory '{name}'. Reason: {e}"

    def delete_directory(name: str) -> str:
        try:
            os.rmdir(name)
            return f"I have deleted the directory '{name}'"
        except Exception as e:
            return f"I was unable to delete the directory '{name}'. Reason: {e}"
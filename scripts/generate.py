import sys
import os

def generate_model():
    model_name = input("Enter model name: ")
    # Logika untuk menghasilkan file model baru di direktori yang sesuai
    # Misalnya:
    with open(f'app/models/{model_name.lower()}.py', 'w') as f:
        f.write(f'''from sqlalchemy import Column, String, Integer
from config.database import Base

class {model_name.capitalize()}(Base):
    __tablename__ = '{model_name.lower()}'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
        ''')
    print(f"Model {model_name} generated successfully.")

def generate_controller():
    controller_name = input("Enter controller name: ")
    # Logika untuk menghasilkan file controller baru di direktori yang sesuai
    # Misalnya:
    with open(f'app/controllers/{controller_name.lower()}_controller.py', 'w') as f:
        f.write(f'''class {controller_name}Controller:
    def __init__(self):
        pass

    def index(self):
        pass

    def show(self, id):
        pass

    def create(self, data):
        pass

    def update(self, id, data):
        pass

    def delete(self, id):
        pass
        ''')
    print(f"Controller {controller_name} generated successfully.")

def generate_middleware():
    middleware_name = input("Enter middleware name: ")
    # Logika untuk menghasilkan file middleware baru di direktori yang sesuai
    # Misalnya:
    with open(f'app/middleware/{middleware_name.lower()}_middleware.py', 'w') as f:
        f.write(f'''class {middleware_name}Middleware:
    def __init__(self):
        pass

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        pass
        ''')
    print(f"Middleware {middleware_name} generated successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate.py [model|controller|middleware]")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'model':
        generate_model()
    elif command == 'controller':
        generate_controller()
    elif command == 'middleware':
        generate_middleware()
    else:
        print("Unknown command.")

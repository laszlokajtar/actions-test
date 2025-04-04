import httpx
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print(f"This is a test: {os.getenv('IS_TEST')}")
    
    response = httpx.get("https://httpbin.org/bearer", headers={"Authorization": f'Bearer {os.getenv("API_KEY")}'})

    print(response)

if __name__ == "__main__":
    main()

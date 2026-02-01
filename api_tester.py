import requests

def main():
    url = input("🔗 Enter the API URL you want to test (GET only): ")

    try:
        response = requests.get(url)
        print("\nStatus Code:", response.status_code)
        print("Response JSON:")
        print(response.json())
    except Exception as e:
        print("\nError:", e)

if __name__ == "__main__":
    main()

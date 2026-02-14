from agents.orchestrator import orchestrate

def main():
    print("Security Assistant Ready\n")

    while True:
        query = input("You: ")
        response = orchestrate(query)
        print("\nAssistant:", response, "\n")

if __name__ == "__main__":
    main()

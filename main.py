from rag.rag_pipeline import load_and_index_document, query_rag, refresh_document, delete_document

def main():
    while True:
        print("\nOptions:")
        print("1. Load a document from URL")
        print("2. Ask a question")
        print("3. Exit")
        print("4. Refresh a document")
        print("5. Delete a document")

        choice = input("Enter your choice: ")

        if choice == '1':
            url = input("Enter document URL: ")
            load_and_index_document(url)

        elif choice == '2':
            query = input("Enter your question: ")
            answer = query_rag(query)
            print(f"\nAnswer: {answer}")

        elif choice == '3':
            break

        elif choice == '4':
            source_id = input("Enter document source ID to refresh: ")
            refresh_document(source_id)

        elif choice == '5':
            source_id = input("Enter document source ID to delete: ")
            delete_document(source_id)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

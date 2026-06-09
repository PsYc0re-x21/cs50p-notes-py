file = input("Enter the file name here: ").strip().lower()

if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf") or file.endswith(".txt"):
    print("document/pdf")
elif file.endswith(".txt"):
    print("document/txt")
else:
    print("application/octet-stream")

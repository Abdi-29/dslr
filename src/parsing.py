def check_input(argv):
    if len(argv) != 2:
        print("Usage: python script.py <filename.csv>")
        exit(1)

    filename = argv[1]

    if not filename.endswith('.csv'):
        print("Error: The file must have a .csv extension.")
        exit(1)

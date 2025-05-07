import os

def create_slide_files(num_files=30, directory="."):
    """
    Creates a specified number of blank markdown files named slide_XX.md.

    Args:
        num_files (int): The number of slide files to create. Defaults to 30.
        directory (str): The directory where the files should be created.
            Defaults to the current directory.  If the directory does not exist,
            it will be created.

    Returns:
        None.  Prints a success message to the console upon completion.
        If any error occurs during file creation, it prints the error message.
    """
    # Ensure the directory exists.  Create it if it does not.
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        except OSError as e:
            print(f"Error creating directory {directory}: {e}")
            return  # Stop if directory creation fails.

    # Create the slide files.
    for i in range(1, num_files + 1):
        # Format the filename with leading zero if necessary.
        filename = f"slide_{i:02d}.md"
        filepath = os.path.join(directory, filename)

        try:
            # Open the file in write mode ('w') to create an empty file.
            with open(filepath, 'w') as f:
                pass  # No need to write anything, just create the file.
            print(f"Created file: {filepath}")
        except OSError as e:
            print(f"Error creating file {filepath}: {e}")
            # Continue to the next file, even if one fails.

    print(f"\nSuccessfully created {num_files} slide files in {directory}.")

if __name__ == "__main__":
    # Use a relative directory
    create_slide_files(num_files=30, directory="slides")
    # If you want to create files in the current directory, you can use:
    # create_slide_files(num_files=30)

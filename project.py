# Import json module
# Used for saving and loading job data from a JSON file
import json

# Import sys module
# Used to exit the program cleanly
import sys


# Allowed job statuses
# Using a constant list ensures users only choose valid options
STATUSES = ["Interested", "Applied", "Interviewing", "Offer", "Rejected"]


def main():
    """
    Main controller of the program.

    Responsibilities:
    1. Load saved jobs
    2. Display menu
    3. Run selected action
    4. Continue looping until user exits
    """

    # Load jobs from JSON file
    # If the file doesn't exist, an empty list will be returned
    jobs = load_jobs()

    # Infinite loop keeps the program running
    while True:

        # Display menu options to user
        display_menu()

        # Get validated user menu choice
        choice = get_menu_choice()

        # Option 1: Add a new job
        if choice == "1":
            add_job(jobs)
            save_jobs(jobs)

        # Option 2: View all jobs
        elif choice == "2":
            view_jobs(jobs)

        # Option 3: Update job status
        elif choice == "3":
            update_job_status(jobs)
            save_jobs(jobs)

        # Option 4: Delete a job
        elif choice == "4":
            delete_job(jobs)
            save_jobs(jobs)

        # Option 5: Exit program
        elif choice == "5":
            print("Goodbye!")
            sys.exit()


def load_jobs(filename="jobs.json"):
    """
    Loads saved jobs from a JSON file.

    Returns:
        list of job dictionaries
    """

    try:
        # Open the JSON file in read mode
        with open(filename, "r") as file:

            # Convert JSON data into Python list
            return json.load(file)

    # If file does not exist yet
    except FileNotFoundError:
        return []

    # If file exists but is empty or corrupted
    except json.JSONDecodeError:
        return []


def save_jobs(jobs, filename="jobs.json"):
    """
    Saves the jobs list to a JSON file.
    """

    # Open the file in write mode
    with open(filename, "w") as file:

        # Convert Python list into JSON format
        # indent=4 makes the file easier to read
        json.dump(jobs, file, indent=4)


def display_menu():
    """
    Prints the menu options.
    """

    print("\nJob Application Tracker")

    print("1. Add job")
    print("2. View jobs")
    print("3. Update job status")
    print("4. Delete job")
    print("5. Exit")


def get_menu_choice():
    """
    Gets and validates menu input.
    Ensures user enters a valid option.
    """

    while True:

        choice = input("Choose an option: ").strip()

        # Valid menu options
        if choice in ["1", "2", "3", "4", "5"]:
            return choice

        print("Invalid choice. Please enter 1-5.")


def add_job(jobs):
    """
    Adds a new job to the jobs list.
    """

    # Ask user for job information
    company = input("Company: ").strip()
    role = input("Role: ").strip()
    location = input("Location: ").strip()
    notes = input("Notes: ").strip()

    # Validate job status
    while True:

        status = input(f"Status {STATUSES}: ").strip().title()

        # Check if status is allowed
        if is_valid_status(status):
            break

        print("Invalid status.")

    # Create job dictionary
    job = {
        "company": company,
        "role": role,
        "location": location,
        "status": status,
        "notes": notes
    }

    # Add job to jobs list
    jobs.append(job)

    print("Job added.")


def view_jobs(jobs):
    """
    Displays all saved jobs.
    """

    # If list is empty
    if not jobs:
        print("No jobs saved.")
        return

    # Print each job with a number
    for i, job in enumerate(jobs, start=1):

        print(f"\nJob #{i}")

        print(f"Company: {job['company']}")
        print(f"Role: {job['role']}")
        print(f"Location: {job['location']}")
        print(f"Status: {job['status']}")
        print(f"Notes: {job['notes']}")


def update_job_status(jobs):
    """
    Updates the status of a selected job.
    """

    if not jobs:
        print("No jobs available.")
        return

    # Display jobs so user can select one
    view_jobs(jobs)

    while True:
        try:
            # Ask user which job to update
            choice = int(input("Enter job number: "))

            # Ensure job number is valid
            if 1 <= choice <= len(jobs):
                break

            print("Invalid number.")

        except ValueError:
            print("Enter a number.")

    # Ask for new status
    while True:

        new_status = input(f"New status {STATUSES}: ").strip().title()

        if is_valid_status(new_status):

            # Update selected job
            jobs[choice - 1]["status"] = new_status

            print("Status updated.")
            return

        print("Invalid status.")


def delete_job(jobs):
    """
    Deletes a selected job.
    """

    if not jobs:
        print("No jobs to delete.")
        return

    # Show jobs to user
    view_jobs(jobs)

    while True:
        try:
            choice = int(input("Enter job number to delete: "))

            # Ensure valid job selection
            if 1 <= choice <= len(jobs):

                # Remove job from list
                removed = jobs.pop(choice - 1)

                print(f"Deleted {removed['company']}.")
                return

            print("Invalid number.")

        except ValueError:
            print("Enter a number.")


def is_valid_status(status):
    """
    Checks if the provided status is allowed.
    """

    return status in STATUSES


# Entry point of the program
# Ensures main() runs only when file is executed directly
if __name__ == "__main__":
    main()
# Job Application Tracker

## Description

Job Application Tracker is a command-line Python application that helps users organize and manage job applications.

Users can:

- Add new job applications
- View saved applications
- Update the status of an application
- Delete applications

All job data is saved to a JSON file so that the information persists between program runs.

This project demonstrates several core Python programming concepts including:

- Functions
- Lists and dictionaries
- File input/output using JSON
- Input validation
- Program structure using a main controller
- Automated testing using pytest

---

## File Structure

project.py  
Main application logic.

test_project.py  
Contains automated tests using pytest.

jobs.json  
Stores job application data.

README.md  
Documentation explaining the project.

---

## How the Program Works

When the program starts, it loads any previously saved job applications from `jobs.json`.

The user is then presented with a menu allowing them to:

1. Add a job
2. View saved jobs
3. Update job status
4. Delete a job
5. Exit the program

Jobs are stored internally as dictionaries inside a list.

### Example job structure:

```json
{
  "company": "Birdstop",
  "role": "Drone Pilot",
  "location": "Detroit",
  "status": "Applied",
  "notes": "FAA license required"
}
```

Whenever a job is added, updated, or deleted, the program saves the updated data to the JSON file.

---

## Design Choices

JSON was chosen for storage because it is lightweight and easy to convert between Python data structures.

A list of dictionaries was used to represent job applications because it allows flexible storage of structured job data.

Status values are restricted to predefined options to ensure data consistency.

---

## Future Improvements

Possible improvements include:

- Adding search functionality
- Filtering jobs by status
- Adding application dates
- Exporting job data to CSV
- Creating a graphical user interface
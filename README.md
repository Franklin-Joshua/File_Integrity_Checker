# File_Integrity_Checker

Company : CODTECH IT SOLUTIONS

NAME : F. FRANKLIN JOSHUA

INTERN ID : CITS0D289

DOMAIN : CYBERSECURITY AND ETHICAL HACKING

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH

Description:

In the era of increasing cyber threats, ensuring the integrity of important files is a crucial part of cybersecurity. This project, titled "File Integrity Checker", is a simple but effective tool built in Python that helps monitor changes in files by calculating and comparing hash values. It allows users to detect if any file has been altered, deleted, or added, thus serving as an early warning system against tampering, accidental modifications, or malicious activity.

Objective
The main objective of this project is to build a tool that can:

-Calculate the digital fingerprint (hash) of each file.

-Store those fingerprints securely.

-Re-scan files later and detect any changes.
This tool can be used by anyone who wants to track file changes for security, auditing, or data protection purposes.

 How It Works
The tool uses the SHA-256 algorithm from Python’s built-in hashlib library to calculate a unique hash for each file. SHA-256 is a cryptographic hash function that produces a fixed-size 256-bit hash. Even a small change in the file will result in a completely different hash, making it ideal for detecting changes.

When the user runs the script in "save" mode, the program:

-Scans a specified folder (and its subfolders).

-Calculates the hash for each file.

-Saves the file paths and their corresponding hashes to a JSON file named hashes.json.

Later, when the script is run in "check" mode, it:

-Scans the same folder again.

-Recalculates the current hashes.

-Compares them with the previously stored hashes.

-Prints messages if a file was modified, deleted, or newly added.

This approach helps users quickly identify any unauthorized or unexpected file changes.

Technologies Used
-Python 3

-hashlib for hashing

-os and json for file system and data handling

-VS Code or any Python IDE

Usage
The tool is run from the command line with two modes:

-save: to store current file hashes

-check: to compare current state with saved hashes

Benefits
-Helps detect file tampering and data breaches

-Useful for monitoring system files, exam files, logs, and backups

-Lightweight, no external dependencies

-Beginner-friendly and customizable

Future Scope
-The tool can be improved by adding:

-A GUI using Tkinter or PyQt

-Email alerts for changes

-Auto-scheduling using Task Scheduler or cron

-Logging of results into a separate report file

Conclusion
The File Integrity Checker is a practical project that introduces students and beginners to the concepts of file monitoring, hashing, and basic security. It demonstrates how a simple script can serve an important purpose in securing digital data and building cybersecurity awareness.
![Screenshot 2025-06-29 002214](https://github.com/user-attachments/assets/0b334aa6-a58c-4a10-bed1-37c58e50ac7d)
![Screenshot 2025-06-29 002132](https://github.com/user-attachments/assets/e37e6766-507a-4113-ae28-67eba8037c54)
![Screenshot 2025-06-29 002049](https://github.com/user-attachments/assets/11334add-96cf-491b-8d3c-26c18039b111)


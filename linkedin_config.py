CONFIG = {
    # Your LinkedIn credentials
    "linkedin_email": "your_email@example.com",
    "linkedin_password": "your_password",
    # Your personal info (used to fill application forms)
    "first_name": "Evan",
    "last_name": "YourLastName",
    "email": "your_email@example.com",
    "phone": "647-000-0000",
    "location": "Milton, Ontario, Canada",
    "city": "Milton",
    "province": "Ontario",
    "country": "Canada",
    "postal_code": "L9T 0A1",
    # LinkedIn profile URL
    "linkedin_url": "https://www.linkedin.com/in/yourprofile",
    # Resume file path (PDF)
    "resume_path": "/path/to/your/resume.pdf",
    # Cover letter (optional - used when asked)
    "cover_letter": "I am excited to apply for this position...",
    # Work authorization
    "work_authorized": "Yes",
    "require_sponsorship": "No",
    # Experience
    "years_experience": "2",
    # Common screening question answers
    "screening_answers": {
        "years of experience": "2",
        "salary": "70000",
        "expected salary": "70000",
        "willing to relocate": "No",
        "available to start": "2 weeks",
        "gpa": "3.5",
        "bachelor": "Yes",
        "degree": "Yes",
        "legally authorized": "Yes",
        "sponsorship": "No",
        "remote": "Yes",
        "hybrid": "Yes",
    },
    # Account creation password (for external sites)
    "account_password": "YourSecurePassword123!",
    # Jobs to skip (keywords in title)
    "blacklist_titles": ["senior", "principal", "director", "VP", "vice president", "lead"],
    # Only apply to these (leave empty to apply to all saved jobs)
    "whitelist_titles": [],
    # Max jobs to apply to per run (safety limit)
    "max_applications": 25,
    # Delay between actions (seconds) - keeps it human-like
    "min_delay": 1.5,
    "max_delay": 3.5,
}

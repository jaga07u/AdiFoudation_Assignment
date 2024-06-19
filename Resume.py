
name = "Jagadish Pradhan "
title = "Full Stack Developer"
email = "john.doe@example.com"
phone = "(123) 456-7890"

# Skills
skills = ["HTML", "CSS", "JavaScript", "React", "Node.js"]

# Experience
experience = [
    {
        "position": "Senior Developer",
        "company": "TechCorp",
        "start_date": "January 2020",
        "end_date": "Present",
        "description": "Developed and maintained the company's main e-commerce platform."
    },
    {
        "position": "Frontend Developer",
        "company": "Webify",
        "start_date": "June 2017",
        "end_date": "December 2019",
        "description": "Worked on various client projects, creating responsive and dynamic websites."
    }
]

# Education
education = [
    {
        "degree": "Bachelor of Science in Computer Science",
        "institution": "University of Computer Science",
        "start_date": "2013",
        "end_date": "2017"
    }
]

def display_personal_info():
    """Display personal information."""
    print(f"Name: {name}")
    print(f"Title: {title}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print()

def display_skills():
    """Display skills."""
    print("Skills:")
    for skill in skills:
        print(f"- {skill}")
    print()

def display_experience():
    """Display experience."""
    print("Experience:")
    for job in experience:
        print(f"{job['position']} at {job['company']}")
        print(f"Dates: {job['start_date']} - {job['end_date']}")
        print(f"Description: {job['description']}")
        print()
    
def display_education():
    """Display education."""
    print("Education:")
    for edu in education:
        print(f"{edu['degree']}, {edu['institution']}")
        print(f"Dates: {edu['start_date']} - {edu['end_date']}")
        print()

def display_resume():
    """Display the entire resume."""
    display_personal_info()
    display_skills()
    display_experience()
    display_education()

if __name__ == "__main__":
    display_resume()

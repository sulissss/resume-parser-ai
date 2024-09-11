from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

# 1. Personal Information
class PersonalInformation(BaseModel):
    first_name: str
    last_name: str
    full_name: str
    date_of_birth: str
    gender: str
    nationality: str
    phone_number: str
    email_address: str
    address: str
    city: str
    state: str
    country: str
    linkedin_profile: Optional[str]
    website_url: Optional[str]
    photo: Optional[str]  # optional photo field

# 2. Objective or Summary
class ObjectiveSummary(BaseModel):
    objective: str
    career_summary: str
    personal_statement: Optional[str]

# 3. Professional Experience
class JobPosition(BaseModel):
    company_name: str
    job_title: str
    start_date: str
    end_date: Optional[date]  # or current position
    job_location: Optional[str]
    job_description: Optional[List[str]]
    achievements: Optional[List[str]]

class ProfessionalExperience(BaseModel):
    work_experience: List[JobPosition]

# 4. Education
class EducationDetail(BaseModel):
    degree: str
    institution: str
    start_date: date
    end_date: Optional[date]
    major: Optional[str]
    gpa: Optional[float]  # optional field
    location: Optional[str]

class Education(BaseModel):
    education: List[EducationDetail]

# 5. Skills
class Skills(BaseModel):
    technical_skills: List[str]
    soft_skills: Optional[List[str]]
    languages: Optional[List[str]]

# 6. Certifications and Courses
class Certification(BaseModel):
    certification_name: str
    issuing_organization: str
    date_issued: date
    date_expired: Optional[date]

class Course(BaseModel):
    course_name: str
    course_provider: str
    completion_date: date

class CertificationsAndCourses(BaseModel):
    certifications: List[Certification]
    courses: Optional[List[Course]]

# 7. Projects
class Project(BaseModel):
    project_title: str
    project_description: str
    role: str
    technologies_used: Optional[List[str]]
    start_date: date
    end_date: Optional[date]

class Projects(BaseModel):
    projects: List[Project]

# 8. Awards & Achievements
class Award(BaseModel):
    award_name: str
    issuing_organization: str
    date_received: date
    description: Optional[str]

class AwardsAndAchievements(BaseModel):
    awards_and_achievements: List[Award]

# 9. Publications and Research
class Publication(BaseModel):
    publication_title: str
    journal_or_conference: str
    publication_date: date
    doi: Optional[str]

class Research(BaseModel):
    research_title: str
    institution: str
    start_date: date
    end_date: Optional[date]
    description: Optional[str]

class PublicationsAndResearch(BaseModel):
    publications: Optional[List[Publication]]
    research: Optional[List[Research]]

# 10. Volunteering or Community Service
class VolunteerExperience(BaseModel):
    organization_name: str
    role: str
    start_date: date
    end_date: Optional[date]
    description: Optional[str]

class Volunteering(BaseModel):
    volunteer_experience: List[VolunteerExperience]

# 11. Hobbies and Interests (optional)
class HobbiesInterests(BaseModel):
    hobbies: Optional[List[str]]
    interests: Optional[List[str]]

# 12. References (optional)
class Reference(BaseModel):
    referee_name: str
    referee_position: str
    company_name: Optional[str]
    contact_information: str

class References(BaseModel):
    references: Optional[List[Reference]]

# 13. Additional Information
class AdditionalInformation(BaseModel):
    driver_license: Optional[str]
    availability: Optional[str]
    willingness_to_relocate: Optional[bool]
    expected_salary: Optional[str]

# Full CV Model
class CV(BaseModel):
    personal_information: PersonalInformation
    objective_summary: Optional[ObjectiveSummary]
    professional_experience: ProfessionalExperience
    education: Education
    skills: Skills
    certifications_and_courses: Optional[CertificationsAndCourses]
    projects: Optional[Projects]
    awards_and_achievements: Optional[AwardsAndAchievements]
    publications_and_research: Optional[PublicationsAndResearch]
    volunteering: Optional[Volunteering]
    hobbies_and_interests: Optional[HobbiesInterests]
    references: Optional[References]
    additional_information: Optional[AdditionalInformation]
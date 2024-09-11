from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


# 1. Personal Information
class PersonalInformation(BaseModel):
    """Represents the personal details of an individual."""
    first_name: str = Field(..., description="The individual's first name.")
    last_name: str = Field(..., description="The individual's last name.")
    full_name: str = Field(..., description="The individual's full name.")
    date_of_birth: str = Field(..., description="The individual's date of birth (YYYY-MM-DD).")
    gender: str = Field(..., description="The individual's gender.")
    nationality: str = Field(..., description="The individual's nationality.")
    phone_number: str = Field(..., description="The individual's primary contact number.")
    email_address: str = Field(..., description="The individual's email address.")
    address: str = Field(..., description="The individual's physical home address.")
    city: str = Field(..., description="City where the individual resides.")
    state: Optional[str] = Field(None, description="State where the individual resides (optional).")
    country: str = Field(..., description="Country where the individual resides.")
    linkedin_profile: Optional[str] = Field(None, description="URL to the individual's LinkedIn profile (optional).")
    website_url: Optional[str] = Field(None, description="URL to the individual's personal website (optional).")
    photo: Optional[str] = Field(None, description="URL to the individual's photo (optional).")

# 2. Objective or Summary
class ObjectiveSummary(BaseModel):
    """Represents the individual's career objective, summary, and personal statement."""
    objective: str = Field(..., description="The individual's career objective or goal.")
    career_summary: str = Field(..., description="A brief summary of the individual's career path.")
    personal_statement: str = Field(..., description="A personal statement highlighting the individual's values and aspirations.")

# 3. Professional Experience
class JobPosition(BaseModel):
    """Details about a specific job position held by the individual."""
    company_name: str = Field(..., description="The name of the company where the individual worked.")
    job_title: str = Field(..., description="The job title held by the individual.")
    start_date: str = Field(..., description="The start date of the job (YYYY-MM-DD).")
    end_date: str = Field(..., description="The end date of the job or 'current' if still employed (YYYY-MM-DD).")
    job_location: str = Field(..., description="The location of the job.")
    job_description: List[str] = Field(..., description="A list of responsibilities and duties of the job.")
    achievements: List[str] = Field(..., description="Key achievements and contributions made in the role.")

class ProfessionalExperience(BaseModel):
    """Represents the individual's professional work experience."""
    work_experience: List[JobPosition] = Field(..., description="A list of jobs and relevant professional experience.")

# 4. Education
class EducationDetail(BaseModel):
    """Details of an educational qualification obtained by the individual."""
    degree: str = Field(..., description="The degree or qualification obtained by the individual.")
    institution: str = Field(..., description="The name of the institution where the degree was earned.")
    start_date: str = Field(..., description="The start date of the educational program (YYYY-MM-DD).")
    end_date: str = Field(..., description="The end date of the educational program (YYYY-MM-DD).")
    major: str = Field(..., description="The major field of study.")
    gpa: str = Field(..., description="The individual's GPA or academic performance score.")
    location: str = Field(..., description="The location of the educational institution.")

class Education(BaseModel):
    """Represents the individual's educational background."""
    education: List[EducationDetail] = Field(..., description="A list of the individual's educational qualifications.")

# 5. Skills
class Skills(BaseModel):
    """Represents the technical and soft skills possessed by the individual."""
    technical_skills: List[str] = Field(..., description="A list of the individual's technical skills.")
    soft_skills: Optional[List[str]] = Field(None, description="A list of the individual's interpersonal and soft skills.")
    languages: Optional[List[str]] = Field(None, description="A list of languages spoken or known by the individual.")

# 6. Certifications and Courses
class Certification(BaseModel):
    """Represents a professional certification earned by the individual."""
    certification_name: str = Field(..., description="The name of the certification.")
    issuing_organization: str = Field(..., description="The organization that issued the certification.")
    date_issued: str = Field(..., description="The date the certification was issued (YYYY-MM-DD).")
    date_expired: str = Field(..., description="The expiration date of the certification (if applicable).")

class Course(BaseModel):
    """Represents a course completed by the individual."""
    course_name: str = Field(..., description="The name of the course completed.")
    course_provider: str = Field(..., description="The organization or platform offering the course.")
    completion_date: str = Field(..., description="The date the course was completed (YYYY-MM-DD).")

class CertificationsAndCourses(BaseModel):
    """Represents a collection of certifications and courses completed by the individual."""
    certifications: List[Certification] = Field(..., description="A list of professional certifications earned by the individual.")
    courses: List[Course] = Field(..., description="A list of additional courses completed by the individual.")

# 7. Projects
class Project(BaseModel):
    """Details about a project undertaken by the individual."""
    project_title: str = Field(..., description="The title of the project.")
    project_description: str = Field(..., description="A brief description of the project.")
    role: str = Field(..., description="The role the individual played in the project.")
    technologies_used: List[str] = Field(..., description="Technologies and tools used in the project.")
    start_date: str = Field(..., description="The start date of the project (YYYY-MM-DD).")
    end_date: str = Field(..., description="The end date of the project (YYYY-MM-DD).")

class Projects(BaseModel):
    """Represents a list of projects the individual has worked on."""
    projects: List[Project] = Field(..., description="A list of projects undertaken by the individual.")

# 8. Awards & Achievements
class Award(BaseModel):
    """Represents an award or achievement earned by the individual."""
    award_name: str = Field(..., description="The name of the award or achievement.")
    issuing_organization: str = Field(..., description="The organization that issued the award.")
    date_received: str = Field(..., description="The date the award was received (YYYY-MM-DD).")
    description: str = Field(..., description="A brief description of the award or achievement.")

class AwardsAndAchievements(BaseModel):
    """Represents a collection of awards and achievements."""
    awards_and_achievements: List[Award] = Field(..., description="A list of awards and achievements earned by the individual.")

# 9. Publications and Research
class Publication(BaseModel):
    """Represents a published work by the individual."""
    publication_title: str = Field(..., description="The title of the publication.")
    journal_or_conference: str = Field(..., description="The journal or conference where the publication appeared.")
    publication_date: str = Field(..., description="The publication date (YYYY-MM-DD).")
    doi: str = Field(..., description="The Digital Object Identifier (DOI) of the publication.")

class Research(BaseModel):
    """Represents a research project undertaken by the individual."""
    research_title: str = Field(..., description="The title of the research project.")
    institution: str = Field(..., description="The institution where the research was conducted.")
    start_date: str = Field(..., description="The start date of the research (YYYY-MM-DD).")
    end_date: str = Field(..., description="The end date of the research (YYYY-MM-DD).")
    description: str = Field(..., description="A brief description of the research.")

class PublicationsAndResearch(BaseModel):
    """Represents a collection of publications and research projects."""
    publications: List[Publication] = Field(..., description="A list of publications authored by the individual.")
    research: List[Research] = Field(..., description="A list of research projects conducted by the individual.")

# 10. Volunteering or Community Service
class VolunteerExperience(BaseModel):
    """Represents a volunteer experience undertaken by the individual."""
    organization_name: str = Field(..., description="The name of the organization where the individual volunteered.")
    role: str = Field(..., description="The role the individual played in the volunteer experience.")
    start_date: str = Field(..., description="The start date of the volunteer experience (YYYY-MM-DD).")
    end_date: str = Field(..., description="The end date of the volunteer experience (YYYY-MM-DD).")
    description: str = Field(..., description="A brief description of the volunteer experience.")

class Volunteering(BaseModel):
    """Represents a list of volunteer experiences."""
    volunteer_experience: List[VolunteerExperience] = Field(..., description="A list of volunteer experiences undertaken by the individual.")

# 11. Hobbies and Interests (optional)
class HobbiesInterests(BaseModel):
    """Represents the individual's hobbies and interests."""
    hobbies: List[str] = Field(..., description="A list of the individual's hobbies.")
    interests: List[str] = Field(..., description="A list of the individual's personal interests.")

# 12. References (optional)
class Reference(BaseModel):
    """Represents a reference provided by the individual."""
    referrer_name: str = Field(..., description="The name of the person providing the reference.")
    referrer_position: str = Field(..., description="The referrer's position or job title.")
    company: str = Field(..., description="The company where the referrer works.")
    email_address: str = Field(..., description="The referrer's email address.")
    phone_number: str = Field(..., description="The referrer's contact number.")

class References(BaseModel):
    """Represents a collection of professional references."""
    references: List[Reference] = Field(..., description="A list of professional references provided by the individual.")

# 13. Additional Information (optional)
class AdditionalInformation(BaseModel):
    """Represents any additional information the individual would like to include."""
    information: str = Field(..., description="Any other relevant information that does not fit into the other categories.")

# 14. CV (Comprehensive Model)
class CV(BaseModel):
    """Represents the entire CV of the individual, combining all sections."""
    personal_information: PersonalInformation = Field(..., description="Personal details of the individual.")
    objective_summary: ObjectiveSummary = Field(..., description="The individual's career objective or summary.")
    # professional_experience: ProfessionalExperience = Field(..., description="Details of the individual's professional work experience.")
    # education: Education = Field(..., description="The individual's educational background.")
    # skills: Skills = Field(..., description="A list of technical and soft skills possessed by the individual.")
    # certifications_and_courses: CertificationsAndCourses = Field(..., description="Certifications and courses completed by the individual.")
    # projects: Projects = Field(..., description="Details about projects the individual has worked on.")
    # awards_and_achievements: AwardsAndAchievements = Field(..., description="A list of awards and achievements earned by the individual.")
    # publications_and_research: PublicationsAndResearch = Field(..., description="Details about publications and research projects by the individual.")
    # volunteering: Volunteering = Field(..., description="A list of volunteer experiences.")
    # hobbies_and_interests: Optional[HobbiesInterests] = Field(None, description="The individual's hobbies and interests (optional).")
    # references: Optional[References] = Field(None, description="A list of professional references (optional).")
    # additional_information: Optional[AdditionalInformation] = Field(None, description="Any other additional information the individual wishes to include (optional).")
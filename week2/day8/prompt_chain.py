import os                                              ## Saari library access kiye 
from pathlib import Path 
from groq import Groq
from dotenv import load_dotenv
import time

load_dotenv()

my_api = os.getenv("GROQ_API_KEY")

if not my_api:
    raise ValueError("API nhi mila")

client = Groq(api_key = my_api)

model = "llama-3.3-70b-versatile"

Job_D = """

PR & Outreach SpecialistDepartment: Communications / MarketingEmployment Type: Full-TimeLocation: [Remote / Hybrid / On-Site]Reports To: Head of Marketing / Director of CommunicationsPosition OverviewWe are seeking a proactive, highly persuasive, and strategic PR & Outreach Specialist to drive our brand visibility, build media relations, and expand our partnership ecosystem. In this role, you will be responsible for crafting compelling narratives, pitching stories to journalists and influencers, securing guest media opportunities, and building long-term strategic relationships.The ideal candidate possesses exceptional written communication skills, a natural networking mindset, and a data-driven approach to tracking outreach performance.Key Responsibilities1. Public Relations & Media ManagementPress Strategy & Execution: Draft and distribute press releases, media kits, and thought-leadership pitches tailored to specific journalists, publications, and media outlets.Media Relations: Build, maintain, and expand a CRM database of key journalists, editors, podcasters, and industry influencers.Crisis Communications: Assist in monitoring brand sentiment and developing proactive communication plans to manage risk or address negative publicity.Speaking & Awards Strategy: Identify and submit applications for high-value speaking engagements, industry awards, and conference panel opportunities for executive leadership.2. Outreach & Partnership BuildingBrand Partnerships: Research, qualify, and initiate cold and warm outreach to complementary brands, industry partners, and community leaders for co-marketing opportunities.Influencer & Creator Relations: Lead end-to-end influencer outreach campaigns, including contract negotiation, briefing, performance tracking, and relationship management.Content Amplification: Pitch corporate content, research reports, and case studies to external blogs, newsletters, and publications for syndicated coverage and backlinks.3. Monitoring, Tracking & ReportingMedia Monitoring: Track real-time news coverage, brand mentions, competitor PR campaigns, and industry trends to identify reactive pitching opportunities (newsjacking).PR Analytics: Measure and report monthly PR and outreach metrics, including earned media value (EMV), backlink acquisition, response rates, placement reach, and domain authority impact.Position RequirementsCategoryRequirementsExperience2–4 years of proven experience in PR, media outreach, corporate communications, or digital outreach agency/in-house roles.Technical ToolsProficiency with PR and outreach tools (e.g., Cision, Meltwater, Muck Rack, BuzzStream, Hunter.io, or Pitchbox).CommunicationTop-tier written and verbal communication skills; ability to distill complex topics into pitch-ready hooks.PortfolioA track record of secured media placements, published press releases, or successful outreach campaigns.Key Competencies & Soft SkillsPersuasive Storytelling: Ability to frame company updates into genuinely compelling news stories for external audiences.Persistence & Resilience: Comfortable managing high volume, cold outreach, follow-ups, and managing rejection productively.Relationship First Mindset: Focused on nurturing genuine, mutually beneficial, long-term media connections rather than transactional spam.Project Management: High attention to detail with the ability to manage multiple pitch timelines and campaigns simultaneously.Preferred Qualifications (Nice-to-Haves)Pre-existing contacts in top-tier business, tech, or industry-specific media outlets.Solid understanding of digital marketing principles, content strategy, and SEO (link-building).Experience managing crisis communications or executive media training.What We OfferCompetitive base salary with performance bonuses tied to key PR placements.Flexible working options (Remote/Hybrid arrangements).Health, dental, and vision insurance options.Generous paid time off (PTO) and company holidays.Professional development stipend for conferences, media databases, and training.How to ApplyInterested candidates should submit the following:Updated Resume / CV.A brief cover letter outlining your top two PR or outreach achievements.2–3 examples of media coverage, press releases, or successful pitches you personally executed.

"""

Resume = """

Alex Morgan
PR & Outreach Specialist

San Francisco, CA | (555) 019-2834 | alex.morgan@email.com | linkedin.com/in/alexmorgan-pr | alexmorganpr.com

Professional Summary
Results-driven PR & Outreach Specialist with 3+ years of experience building media relations, executing high-yield outreach campaigns, and securing earned media coverage across tech, business, and consumer sectors. Proven track record of securing 120+ tier-1 press placements, managing end-to-end influencer partnerships, and driving organic brand visibility. Proficient in modern PR stacks (Muck Rack, Cision, BuzzStream) and skilled at transforming complex company updates into compelling news angles.

Key Competencies & Technical Skills
PR & Media Relations: Press Release Drafting, Media Kit Creation, Crisis Communication, Executive Thought Leadership, Newsjacking, Media Monitoring.

Outreach & Partnerships: Influencer Marketing, Brand Collaborations, Guest Pitching, Event/Award Submissions, Link Building.

Tools & Software: Muck Rack, Cision, BuzzStream, Meltwater, Hunter.io, Pitchbox, Google Analytics, Notion.

Analytics & Performance: Earned Media Value (EMV), Share of Voice (SOV), Referral Traffic Tracking, Pitch Open/Response Rates.

Professional Experience
PR & Outreach Specialist
Apex Communications Agency | San Francisco, CA

January 2024 – Present

Campaign Execution: Spearhead media outreach strategies for 10+ B2B and consumer accounts, securing over 120+ organic press placements in 18 months across publications like TechCrunch, Forbes, and Business Insider.

Media Database Management: Curate and maintain a personalized database of 600+ journalists, editors, and podcast hosts using Muck Rack and Cision.

Influencer Outreach: Lead end-to-end influencer campaigns from discovery and contract negotiation to brief creation, achieving a 240% ROI across targeted social placements.

Performance Tracking: Build monthly analytics reports measuring Earned Media Value (EMV), domain authority impact, and pitch performance (maintaining an average 38% open rate and 19% response rate).

Communications & Outreach Associate
GrowthMetrics Inc. | San Jose, CA

June 2022 – December 2023

Content Amplification: Conducted targeted cold and warm outreach to pitch research reports and case studies to external blogs, securing 80+ high-authority backlinks per year to support organic SEO efforts.

Newsjacking & Monitoring: Monitored daily industry news and sentiment using Meltwater to identify reactive pitching opportunities, landing executive commentary in 15+ major industry publications.

Speaking & Awards Strategy: Authored and submitted 20+ successful speaker applications and award entries, landing C-suite executives on panel discussions at top industry conferences.

Media Asset Creation: Drafted press releases, media advisories, and executive bios for product launches and corporate milestone announcements.

Key Achievements
Feature Placement Launch: Executed a product launch media strategy that resulted in 14 top-tier articles within 48 hours, driving a 160% spike in direct web traffic.

Process Optimization: Standardized the agency’s pitch follow-up sequence using BuzzStream, improving client response rates from journalists by 28%.

Education & Certifications
Bachelor of Arts in Public Relations & Mass Communication

University of California, Berkeley | Graduated May 2022

Certifications:

HubSpot Inbound Marketing Certification (2023)

Google Analytics Individual Qualification (GA4) (2023)

Active Member, Public Relations Society of America (PRSA)

"""

def LLM_response(system_prompt, user_prompt):
    sys_msg = {
        "role": "system",
        "content": system_prompt
    }

    user_msg = {
        "role": "user",
        "content": user_prompt
    }

    messages = [sys_msg, user_msg]

    response = client.chat.completions.create(model=model, messages=messages)
    
    return response.choices[0].message.content

def step1_Resume_Evaluation(Resume):

    print("Step 1: Resume Evaluation")

    system_prompt = """
    You are a highly skilled PR & Outreach Specialist with expertise in media relations, influencer marketing, and strategic communication. Your task is to evaluate a candidate's resume against a detailed job description for a PR & Outreach Specialist role. You will assess the candidate's qualifications, experience, and skills, and provide a comprehensive evaluation of their suitability for the position. Your evaluation should include strengths, weaknesses, and any recommendations for improvement. Do not invent any information; base your assessment solely on the provided resume and job description. Provide a clear and concise summary of your evaluation, highlighting key points that demonstrate the candidate's fit for the role.
    """

    user_prompt = f"""
    Extract the skills from:
    {Resume}
    """

    return LLM_response(system_prompt, user_prompt)

def step2_Job_Description_Analysis(Job_D):

    print("Step 2: Job Description Analysis")

    system_prompt = """
    You are a highly skilled PR & Outreach Specialist with expertise in media relations, influencer marketing, and strategic communication. Your task is to analyze a detailed job description for a PR & Outreach Specialist role. You will identify the key responsibilities, required qualifications, and desired skills outlined in the job description. Your analysis should provide a clear understanding of what the employer is seeking in a candidate for this position. Do not invent any information; base your analysis solely on the provided job description. Provide a concise summary of your findings, highlighting the most important aspects of the role.
    """

    user_prompt = f"""
    Extract the skills from:
    {Job_D}
    """

    return LLM_response(system_prompt, user_prompt)

def step3_Resume_Job_Description_Comparison(candidate_skills, job_description_skills):

    print("Step 3: Resume and Job Description Comparison")

    system_prompt = """
    You are a highly skilled PR & Outreach Specialist with expertise in media relations, influencer marketing, and strategic communication. Your task is to compare a candidate's resume against a detailed job description for a PR & Outreach Specialist role. You will assess how well the candidate's qualifications, experience, and skills align with the requirements and responsibilities outlined in the job description. Your comparison should highlight areas of strong alignment, potential gaps, and any recommendations for improvement. Do not invent any information; base your assessment solely on the provided resume and job description. Provide a clear and concise summary of your comparison, emphasizing key points that demonstrate the candidate's fit for the role.
    Output format: Give me a score out of 100 and a verdict of "Strong Fit", "Moderate Fit", or "Weak Fit" based on the comparison of the candidate's skills and the job description requirements.
    Score = candidate score
    verdict = final verdict of matching skills.
    """

    user_prompt = f"""
    Compare the skills from:
    {Resume}
    with the skills from:
    {Job_D}
    """

    return LLM_response(system_prompt, user_prompt)

candidate_skills = step1_Resume_Evaluation(Resume)
# print(candidate_skills)
time.sleep(2)
job_description_skills = step2_Job_Description_Analysis(Job_D)
# print(job_description_skills)
time.sleep(2)
score = step3_Resume_Job_Description_Comparison(candidate_skills, job_description_skills)
print(score)

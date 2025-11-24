from typing import List
from .models import AnalysisResult, Profile
from .keyword_extractor import extract_keywords


def analyze_job(job_text: str, profile: Profile) -> AnalysisResult:
    extracted = extract_keywords(job_text, profile.tech_skills, profile.soft_skills)

    job_tech_set = set(extracted["job_tech_skills"])
    job_soft_set = set(extracted["job_soft_skills"])

    profile_tech_set = set(profile.tech_skills)
    profile_soft_set = set(profile.soft_skills)

    matched_tech = sorted(job_tech_set & profile_tech_set)
    missing_tech = sorted(job_tech_set - profile_tech_set)

    matched_soft = sorted(job_soft_set & profile_soft_set)
    missing_soft = sorted(job_soft_set - profile_soft_set)

    suggestions = build_suggestions(
        matched_tech=matched_tech,
        missing_tech=missing_tech,
        matched_soft=matched_soft,
        common_keywords=extracted["common_keywords"],
        profile=profile,
    )

    return AnalysisResult(
        job_tech_skills=extracted["job_tech_skills"],
        job_soft_skills=extracted["job_soft_skills"],
        matched_tech=matched_tech,
        missing_tech=missing_tech,
        matched_soft=matched_soft,
        missing_soft=missing_soft,
        common_keywords=extracted["common_keywords"],
        suggestions=suggestions,
    )


def build_suggestions(
    matched_tech: List[str],
    missing_tech: List[str],
    matched_soft: List[str],
    common_keywords: List[str],
    profile: Profile,
) -> List[str]:
    s: List[str] = []

    if matched_tech:
        s.append(
            f"I have hands-on experience with {', '.join(matched_tech)}, "
            f"which are key technologies mentioned in your job description."
        )

    if matched_soft:
        s.append(
            "In addition to technical skills, I bring strong " +
            ", ".join(matched_soft) +
            " abilities that align well with how you describe your ideal candidate."
        )

    if missing_tech:
        s.append(
            "I am also open to learning and working with " +
            ", ".join(missing_tech) +
            " if needed for this project."
        )

    if common_keywords:
        s.append(
            "I noticed you emphasize " +
            ", ".join(common_keywords[:5]) +
            ", and I would tailor my approach to support those priorities."
        )

    if not s:
        s.append(
            "I can adapt my skills and experience to match the requirements of this job "
            "and would be happy to discuss the details further."
        )

    return s

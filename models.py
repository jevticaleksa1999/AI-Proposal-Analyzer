from dataclasses import dataclass
from typing import List


@dataclass
class Profile:
    name: str
    title: str
    tech_skills: List[str]
    soft_skills: List[str]


@dataclass
class AnalysisResult:
    job_tech_skills: List[str]
    job_soft_skills: List[str]
    matched_tech: List[str]
    missing_tech: List[str]
    matched_soft: List[str]
    missing_soft: List[str]
    common_keywords: List[str]
    suggestions: List[str]

import re
from collections import Counter
from typing import List, Dict


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> List[str]:
    return normalize(text).split()


def extract_keywords(job_text: str, known_tech: List[str], known_soft: List[str]) -> Dict[str, List[str]]:
    normalized = normalize(job_text)

    job_tech = sorted({kw for kw in known_tech if kw in normalized})
    job_soft = sorted({kw for kw in known_soft if kw in normalized})

    words = tokenize(job_text)
    counts = Counter(words)
    common = [w for w, c in counts.most_common() if len(w) > 4][:15]

    return {
        "job_tech_skills": job_tech,
        "job_soft_skills": job_soft,
        "common_keywords": common,
    }

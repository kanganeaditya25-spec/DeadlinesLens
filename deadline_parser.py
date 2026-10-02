import json
from google.genai import types


def extract_deadlines(client, image, system_prompt):

    prompt = """
Look at this academic document carefully.

Find all deadlines, exams, assignments, practicals,
projects, presentations, quizzes, tests, and other
academic events that have a date or time.

Return ONLY valid JSON.

Use this format:

[
    {
        "subject": "Subject name",
        "task": "Assignment or event",
        "date": "Date",
        "time": "Time if available",
        "notes": "Important notes if available"
    }
]

Rules:

- Do not invent information.
- Only use information visible in the image.
- If something is unclear, write "Unclear".
- Include all identifiable deadlines.
- If there are no deadlines, return an empty list.
"""

    image_part = types.Part.from_bytes(
        data=image.getvalue(),
        mime_type=image.type
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=[
            prompt,
            image_part
        ]
    )

    result = response.text

    # Remove JSON code fences if Gemini adds them
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:

        deadlines = json.loads(result)

        return deadlines

    except:

        return []
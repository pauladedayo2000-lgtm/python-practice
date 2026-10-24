"""Count words in sample.txt and save the top 5 to output.txt."""

import re
from collections import Counter
from pathlib import Path

folder = Path(__file__).parent
input_file = folder / "sample.txt"
output_file = folder / "output.txt"

try:
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"Could not find {input_file}")
else:
    words = re.findall(r"[a-z']+", text.lower())
    counts = Counter(words)

    lines = [f"Total words: {len(words)}", "Top 5 words:"]
    for word, count in counts.most_common(5):
        lines.append(f"{word}: {count}")
    result = "\n".join(lines)

    print(result)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)

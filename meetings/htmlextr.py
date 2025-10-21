from bs4 import BeautifulSoup
import re

file = "meeting2/audio/elvn.html"
savepath = "meeting2/audio"
with open(file, "r", encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")
output_lines = []
current_line = ""
for block in soup.select("div.f-paragraph-03"):
    text = block.get_text(" ", strip=True)
    text = re.sub(r"\s+", " ", text).strip()
    match = re.match(r"^(Speaker\s*\d+)", text)
    if match:
        if current_line:
            output_lines.append(current_line.strip())
        current_line = text
    else:
        current_line += " " + text
if current_line:
    output_lines.append(current_line.strip())
final_text = "\n".join(output_lines)
print(final_text)
with open(f"{savepath}/transcript.txt", "w", encoding="utf-8") as f:
    f.write(final_text)

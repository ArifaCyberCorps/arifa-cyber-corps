import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Names to remove with more specific patterns
names_patterns = [
    (r'<div data-w-id="[^"]*?" class="testimonial_card"><div[^>]*?</div><div class="testimonial_content">.*?<div class="text-weight-semibold">Lina Rodriguez</div>.*?</div></div>', 'Lina Rodriguez'),
    (r'<div data-w-id="[^"]*?" class="testimonial_card"><div[^>]*?</div><div class="testimonial_content">.*?<div class="text-weight-semibold">Markus Lenz</div>.*?</div></div>', 'Markus Lenz'),
    (r'<div data-w-id="[^"]*?" class="testimonial_card"><div[^>]*?</div><div class="testimonial_content">.*?<div class="text-weight-semibold">Jason Mehta</div>.*?</div></div>', 'Jason Mehta'),
    (r'<div data-w-id="[^"]*?" class="testimonial_card"><div[^>]*?</div><div class="testimonial_content">.*?<div class="text-weight-semibold">Claire Dubois</div>.*?</div></div>', 'Claire Dubois'),
    (r'<div data-w-id="[^"]*?" class="testimonial_card"><div[^>]*?</div><div class="testimonial_content">.*?<div class="text-weight-semibold">Thomas Karl</div>.*?</div></div>', 'Thomas Karl'),
]

removed = []
# For each name, find and remove ALL occurrences of that testimonial card
for pattern, name in names_patterns:
    count = len(re.findall(pattern, html, flags=re.DOTALL))
    if count > 0:
        html = re.sub(pattern, '', html, flags=re.DOTALL)
        removed.append(f"{name} ({count}x)")

# Write the modified HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Removed testimonials for: {', '.join(removed)}")

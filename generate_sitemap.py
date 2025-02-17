# generate_sitemap.py
sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
</urlset>"""

with open("sitemap.xml", "w") as f:
    f.write(sitemap_content)

print("Generated an empty sitemap.xml")

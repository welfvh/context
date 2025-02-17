# generate_sitemap.py
import os
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

def generate_sitemap():
    # Update base URL to correct domain
    base_url = "https://welfvh.github.io/context"  # Changed from "https://yoursite.com"
    
    # Initialize sitemap XML
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Supported file extensions
    supported_extensions = {'.txt', '.md', '.pdf', '.webloc', '.html', '.htm'}
    
    # Walk through the Arena directory
    for root, dirs, files in os.walk('Arena'):
        for file in files:
            # Get file extension
            _, ext = os.path.splitext(file)
            
            # Check if file extension is supported
            if ext.lower() in supported_extensions:
                # Create full path
                file_path = os.path.join(root, file)
                
                # Create URL element
                url = ET.SubElement(urlset, "url")
                
                # Create loc element (URL)
                loc = ET.SubElement(url, "loc")
                loc.text = f"{base_url}/{file_path}"
                
                # Add lastmod element
                lastmod = ET.SubElement(url, "lastmod")
                timestamp = os.path.getmtime(file_path)
                lastmod.text = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    
    # Create the XML string
    xmlstr = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent="   ")
    
    # Write to file
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xmlstr)

if __name__ == "__main__":
    generate_sitemap()

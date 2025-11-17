"""Script to create sample document images for testing."""
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

# Create data directory
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)


def create_invoice_image():
    """Create a sample invoice image."""
    # Create image
    img = Image.new('RGB', (800, 1000), color='white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fallback to default if not available
    try:
        font_large = ImageFont.truetype("arial.ttf", 24)
        font_medium = ImageFont.truetype("arial.ttf", 18)
        font_small = ImageFont.truetype("arial.ttf", 14)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    y = 50
    
    # Header
    draw.text((50, y), "INVOICE", fill='black', font=font_large)
    y += 40
    
    # Invoice details
    draw.text((50, y), "Invoice Number: INV-2025-321", fill='black', font=font_medium)
    y += 30
    draw.text((50, y), "Invoice Date: 01/15/2025", fill='black', font=font_medium)
    y += 30
    draw.text((50, y), "Due Date: 02/15/2025", fill='black', font=font_medium)
    y += 50
    
    # Vendor
    draw.text((50, y), "Vendor: ABC Solutions Pvt Ltd", fill='black', font=font_medium)
    y += 30
    draw.text((50, y), "123 Business Street, City, State 12345", fill='black', font=font_small)
    y += 50
    
    # Bill To
    draw.text((50, y), "Bill To:", fill='black', font=font_medium)
    y += 30
    draw.text((50, y), "XYZ Corporation", fill='black', font=font_small)
    y += 30
    
    # Items
    draw.text((50, y), "Items:", fill='black', font=font_medium)
    y += 40
    
    items = [
        ("Product A", "10", "$500.00", "$5,000.00"),
        ("Product B", "5", "$800.00", "$4,000.00"),
        ("Service C", "1", "$1,200.00", "$1,200.00")
    ]
    
    draw.text((50, y), "Item | Quantity | Unit Price | Total", fill='black', font=font_small)
    y += 30
    
    for item, qty, price, total in items:
        draw.text((50, y), f"{item} | {qty} | {price} | {total}", fill='black', font=font_small)
        y += 25
    
    y += 20
    
    # Totals
    draw.text((500, y), "Subtotal: $10,200.00", fill='black', font=font_medium)
    y += 30
    draw.text((500, y), "Tax (10%): $1,020.00", fill='black', font=font_medium)
    y += 30
    draw.text((500, y), "Total Amount: $11,220.00", fill='black', font=font_large)
    
    # Save
    img.save(data_dir / "sample_invoice.png")
    print("Created sample_invoice.png")


def create_resume_image():
    """Create a sample resume image."""
    img = Image.new('RGB', (800, 1000), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        font_large = ImageFont.truetype("arial.ttf", 24)
        font_medium = ImageFont.truetype("arial.ttf", 18)
        font_small = ImageFont.truetype("arial.ttf", 14)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    y = 50
    
    # Name
    draw.text((50, y), "John Doe", fill='black', font=font_large)
    y += 40
    
    # Contact
    draw.text((50, y), "Email: john.doe@email.com", fill='black', font=font_small)
    y += 25
    draw.text((50, y), "Phone: +1 (555) 123-4567", fill='black', font=font_small)
    y += 25
    draw.text((50, y), "Location: New York, NY", fill='black', font=font_small)
    y += 50
    
    # Objective
    draw.text((50, y), "OBJECTIVE", fill='black', font=font_medium)
    y += 30
    draw.text((50, y), "Experienced software engineer seeking opportunities", fill='black', font=font_small)
    y += 50
    
    # Education
    draw.text((50, y), "EDUCATION", fill='black', font=font_medium)
    y += 30
    draw.text((50, y), "Bachelor of Science in Computer Science", fill='black', font=font_small)
    y += 25
    draw.text((50, y), "University of Technology, 2015-2019", fill='black', font=font_small)
    y += 50
    
    # Experience
    draw.text((50, y), "EXPERIENCE", fill='black', font=font_medium)
    y += 30
    draw.text((50, y), "Senior Software Engineer - Tech Corp (2020-Present)", fill='black', font=font_small)
    y += 25
    draw.text((50, y), "Developed and maintained web applications", fill='black', font=font_small)
    y += 30
    draw.text((50, y), "Software Engineer - Startup Inc (2019-2020)", fill='black', font=font_small)
    y += 50
    
    # Skills
    draw.text((50, y), "SKILLS", fill='black', font=font_medium)
    y += 30
    draw.text((50, y), "Python, JavaScript, React, Node.js, SQL, Docker, AWS", fill='black', font=font_small)
    
    img.save(data_dir / "sample_resume.png")
    print("Created sample_resume.png")


def create_report_image():
    """Create a sample report image."""
    img = Image.new('RGB', (800, 1000), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        font_large = ImageFont.truetype("arial.ttf", 24)
        font_medium = ImageFont.truetype("arial.ttf", 18)
        font_small = ImageFont.truetype("arial.ttf", 14)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    y = 50
    
    # Title
    draw.text((50, y), "Quarterly Business Analysis Report", fill='black', font=font_large)
    y += 50
    
    # Author
    draw.text((50, y), "Author: Jane Smith", fill='black', font=font_medium)
    y += 30
    
    # Date
    draw.text((50, y), "Date: January 2025", fill='black', font=font_medium)
    y += 50
    
    # Abstract
    draw.text((50, y), "ABSTRACT", fill='black', font=font_medium)
    y += 30
    abstract_text = "This report analyzes the business performance for Q4 2024. " \
                    "Key findings include revenue growth of 15%, customer satisfaction " \
                    "scores above 90%, and successful launch of three new products. " \
                    "Recommendations focus on expanding market presence and optimizing operations."
    
    # Wrap text
    words = abstract_text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + " " + word if current_line else word
        if len(test_line) * 6 < 700:  # Rough width estimation
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    for line in lines:
        draw.text((50, y), line, fill='black', font=font_small)
        y += 20
    
    y += 30
    
    # Keywords
    draw.text((50, y), "Keywords: Business Analysis, Revenue, Growth, Performance", fill='black', font=font_small)
    y += 50
    
    # Introduction
    draw.text((50, y), "INTRODUCTION", fill='black', font=font_medium)
    y += 30
    intro_text = "This report provides a comprehensive analysis of business metrics " \
                 "and performance indicators for the fourth quarter."
    draw.text((50, y), intro_text, fill='black', font=font_small)
    y += 50
    
    # Findings
    draw.text((50, y), "KEY FINDINGS", fill='black', font=font_medium)
    y += 30
    findings = [
        "Revenue increased by 15% compared to previous quarter",
        "Customer satisfaction maintained above 90%",
        "Three new products successfully launched"
    ]
    for finding in findings:
        draw.text((50, y), f"• {finding}", fill='black', font=font_small)
        y += 25
    
    y += 20
    
    # Conclusion
    draw.text((50, y), "CONCLUSION", fill='black', font=font_medium)
    y += 30
    conclusion = "The quarter showed strong performance with significant growth " \
                "and successful product launches. Continued focus on customer " \
                "satisfaction and innovation is recommended."
    draw.text((50, y), conclusion, fill='black', font=font_small)
    
    img.save(data_dir / "sample_report.png")
    print("Created sample_report.png")


if __name__ == "__main__":
    print("Creating sample documents...")
    create_invoice_image()
    create_resume_image()
    create_report_image()
    print("\nSample documents created in 'data/' directory")


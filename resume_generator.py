from fpdf import FPDF
import argparse

# Content configuration moved to top
RESUME_CONTENT = {
    "name": "Lorna Alvarado",
    "title": "Marketing Manager",
    "contact_info": [
        "123 Anywhere St., Any City, ST 12345",
        "lmao@fr.com",
        "+123-456-7890"
    ],
    "about_me": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "skills": [
        "Management Skills", "Creativity", "Digital Marketing",
        "Negotiation", "Critical Thinking", "Leadership"
    ],
    "education": [
        {
            "degree": "Bachelor of Business Management",
            "university": "British University",
            "years": "2016 - 2020",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet sem nec risus egestas accumsan. In enim nunc, tincidunt ut quam eget, luctus sollicitudin neque. Sed leo nisl, semper ac hendrerit a, sollicitudin in arcu."
        },
        {
            "degree": "Bachelor of Business Management",
            "university": "British University",
            "years": "2020 - 2023",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet sem nec risus egestas accumsan. In enim nunc, tincidunt ut quam eget, luctus sollicitudin neque. Sed leo nisl, semper ac hendrerit a, sollicitudin in arcu."
        }
    ],
    "experience": [
        {
            "position": "Product Design Manager",
            "org": "Ned Industries",
            "years": "2016 - 2020",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet sem nec risus egestas accumsan. In enim nunc, tincidunt ut quam eget, luctus sollicitudin neque. Sed leo nisl, semper ac hendrerit a, sollicitudin in arcu."
        },
        {
            "position": "Marketing Junior",
            "org": "Playright Media",
            "years": "2020-2022",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet sem nec risus egestas accumsan. In enim nunc, tincidunt ut quam eget, luctus sollicitudin neque. Sed leo nisl, semper ac hendrerit a, sollicitudin in arcu."
        },
        {
            "position": "Marketing Manager",
            "org": "Playright Media",
            "years": "2022-2024",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet sem nec risus egestas accumsan. In enim nunc, tincidunt ut quam eget, luctus sollicitudin neque. Sed leo nisl, semper ac hendrerit a, sollicitudin in arcu."
        }
    ]
}

def parse_color(color_str):
    if color_str.startswith('#'):
        color_str = color_str.lstrip('#')
        if len(color_str) == 3:
            color_str = ''.join([c * 2 for c in color_str])
        if len(color_str) != 6:
            raise ValueError(f"Invalid hex color: {color_str}")
        return tuple(int(color_str[i:i+2], 16) for i in (0, 2, 4))
    
    color_names = {
        'black': (0, 0, 0), 'white': (255, 255, 255),
        'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255),
        'gray': (128, 128, 128), 'lightgray': (211, 211, 211),
        'darkgray': (169, 169, 169), 'cyan': (0, 255, 255),
        'magenta': (255, 0, 255), 'yellow': (255, 255, 0),
        'orange': (255, 165, 0), 'purple': (128, 0, 128),
        'pink': (255, 192, 203)
    }
    lower_str = color_str.lower()
    if lower_str in color_names:
        return color_names[lower_str]
    raise ValueError(f"Unsupported color name: {color_str}")

class ModernResume(FPDF):
    def __init__(self, font_size=10, font_color=(0, 0, 0), background_color=(245, 245, 245)):
        super().__init__()
        self.base_font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
        self.name_font_size = round(2.8 * self.base_font_size)
        self.title_font_size = round(1.4 * self.base_font_size)
        self.header_font_size = round(1.6 * self.base_font_size)
        self.small_font_size = round(0.9 * self.base_font_size)
        self.set_auto_page_break(auto=False)
        self.add_page(format=(210, 230))
        self.set_margins(0, 0, 0)

    def add_left_column(self):
        self.set_fill_color(*self.background_color)
        self.rect(0, 0, 80, 230, 'F')

        # Personal Info from config
        self.set_xy(1, 20)
        self.set_font("Arial", style="B", size=self.name_font_size)
        self.set_text_color(*self.font_color)
        self.cell(0, 10, RESUME_CONTENT["name"], ln=True)

        self.set_xy(8, 30)
        self.set_font("Arial", style="", size=self.title_font_size)
        self.set_text_color(100, 100, 100)
        self.cell(70, 15, RESUME_CONTENT["title"], ln=True)

        # Contact Section
        self.ln(10)
        self.set_x(5)
        self.set_font("Arial", style="B", size=self.header_font_size)
        self.set_text_color(*self.font_color)
        self.cell(100, 10, "Contact", ln=True)

        self.set_draw_color(100, 150, 255)
        self.set_line_width(0.5)
        self.line(2, self.get_y() - 2, 70, self.get_y() - 2)

        self.set_font("Arial", size=self.base_font_size)
        self.set_text_color(80, 80, 80)
        for line in RESUME_CONTENT["contact_info"]:
            self.cell(60, 10, line, ln=True)

        # About Me
        self.ln(10)
        self.set_x(5)
        self.set_font("Arial", style="B", size=self.header_font_size)
        self.set_text_color(*self.font_color)
        self.cell(80, 10, "About Me", ln=True)

        self.set_draw_color(100, 150, 255)
        self.set_line_width(0.5)
        self.line(2, self.get_y() - 2, 70, self.get_y() - 2)

        self.set_font("Arial", size=self.base_font_size)
        self.set_text_color(80, 80, 80)
        self.multi_cell(70, 5, RESUME_CONTENT["about_me"])

        # Skills
        self.ln(10)
        self.set_x(5)
        self.set_font("Arial", style="B", size=self.header_font_size)
        self.set_text_color(*self.font_color)
        self.cell(80, 10, "Skills", ln=True)
    
        self.set_draw_color(100, 150, 255)
        self.set_line_width(0.5)
        self.line(2, self.get_y() - 2, 70, self.get_y() - 2)
        
        self.set_font("Arial", size=self.base_font_size)
        self.set_text_color(80, 80, 80)
        for skill in RESUME_CONTENT["skills"]:
            self.cell(60, 5, f"\x95 {skill}", ln=True)

    def add_right_column(self):
        start_x = 90
        start_y = 30
        line_spacing = 35

        # Education Section
        self.set_xy(start_x+2, start_y - 10)
        self.set_font("Arial", style="B", size=self.header_font_size)
        self.set_text_color(*self.font_color)
        self.cell(100, 10, "Education", ln=True)

        self.set_draw_color(100, 150, 255)
        self.set_line_width(0.5)
        self.line(start_x, self.get_y() - 1, start_x + 110, self.get_y() - 1)

        self.set_draw_color(100, 150, 255)
        self.set_line_width(0.5)
        self.line(start_x, start_y + 6, start_x, start_y + len(RESUME_CONTENT["education"]) * line_spacing - 10)

        for idx, entry in enumerate(RESUME_CONTENT["education"]):
            entry_y = start_y + idx * line_spacing
            self.set_fill_color(100, 150, 255)
            self.ellipse(start_x-2, entry_y +2, 4, 4, 'F')

            self.set_xy(start_x+3, entry_y + 1)
            self.set_font("Arial", style="B", size=self.base_font_size)
            self.set_text_color(*self.font_color)
            self.cell(0, 5, entry["degree"], ln=True)

            self.set_xy(start_x+3, entry_y + 5)
            self.set_font("Arial", style="I", size=self.base_font_size)
            self.set_text_color(80, 80, 80)
            self.cell(0, 5, entry["university"], ln=True)

            self.set_xy(start_x+90, entry_y + 5)
            self.cell(0, 5, entry["years"], ln=True)

            self.ln(5)
            self.set_xy(start_x+3, entry_y + 10)
            self.set_font("Arial", size=self.small_font_size)
            self.set_text_color(100, 100, 100)
            self.multi_cell(110, 5, entry["description"])
            self.ln(5)

        # Experience Section
        self.set_x(start_x+2)
        self.set_font("Arial", style="B", size=self.header_font_size)
        self.set_text_color(*self.font_color)
        self.cell(110, 10, "Experience", ln=True)
        
        self.set_draw_color(100, 150, 255)
        self.line(start_x-2, self.get_y() - 1, start_x+110, self.get_y() - 1)
        
        start_y = self.get_y() + 2
        self.set_draw_color(100, 150, 255)
        self.set_line_width(0.5)
        self.line(start_x, start_y + 6, start_x, start_y + len(RESUME_CONTENT["experience"]) * line_spacing - 10)
        
        for idx, entry in enumerate(RESUME_CONTENT["experience"]):
            entry_y = start_y + idx * line_spacing
            self.set_fill_color(100, 150, 255)
            self.ellipse(start_x-2, entry_y +2, 4, 4, 'F')

            self.set_xy(start_x+3, entry_y + 1)
            self.set_font("Arial", style="B", size=self.base_font_size)
            self.set_text_color(*self.font_color)
            self.cell(0, 5, entry["position"], ln=True)

            self.set_xy(start_x+3, entry_y + 5)
            self.set_font("Arial", style="I", size=self.base_font_size)
            self.set_text_color(80, 80, 80)
            self.cell(0, 5, entry["org"], ln=True)

            self.set_xy(start_x+90, entry_y + 5)
            self.cell(0, 5, entry["years"], ln=True)

            self.ln(5)
            self.set_xy(start_x+3, entry_y + 10)
            self.set_font("Arial", size=self.small_font_size)
            self.set_text_color(100, 100, 100)
            self.multi_cell(110, 5, entry["description"])
            self.ln(5)

    def generate_resume(self):
        self.add_left_column()
        self.add_right_column()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate modern resume PDF')
    parser.add_argument('--font-size', type=int, default=10, 
                       help='Base font size (default: 10)')
    parser.add_argument('--font-color', type=str, default='#000000',
                       help='Text color (name/hex, default: black)')
    parser.add_argument('--background-color', type=str, default='#f5f5f5',
                       help='Left column color (name/hex, default: #f5f5f5)')
    
    args = parser.parse_args()
    
    try:
        font_color = parse_color(args.font_color)
        bg_color = parse_color(args.background_color)
    except ValueError as e:
        print(f"Color error: {e}")
        exit(1)

    pdf = ModernResume(
        font_size=args.font_size,
        font_color=font_color,
        background_color=bg_color
    )
    pdf.generate_resume()
    pdf.output("resume.pdf")
    print("Resume successfully created: resume.pdf")
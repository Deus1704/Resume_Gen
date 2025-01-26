# Modern Resume Generator Script

A Python script that generates clean, modern resume PDFs with customizable styling. Perfect for quickly creating resumes that can be tailored to different applications.

![Resume Example](pic.png) 


## Requirements
This script mainly requires FPDF2 along with a working python (version>3.6) installation. FPDF2 can be installed using the command,

```bash
pip install fpdf2
```

## Using the script
The script has the following basic command for generating the resume with pre-defined data and style.

```
python3 resume_generator.py
```

It supports the following customization options,

|  Argument             |   Description                    |    Default Value   |
| --------------------- | -------------------------------- | ------------------ |    
| `--font-size`         |  Base font size (scales all text)|   10               |    
|  `--font-color`       |  Text color (hex/named color)    |     #000000        |        
| `--background-color`  |  Left column background color    |     #f5f5f5        |    

## Examples

1. ```python
    python resume_generator.py --font-size 11 --font-color "#2d3436" --background-color "#f0f8ff"
    ```
2. ```python
    python resume_generator.py --font-color white --background-color "#2d3436"
    ```


## Customizing Content

Edit the RESUME_CONTENT dictionary in the script to update:

```python
RESUME_CONTENT = {
    "name": "Your Name Here",
    "title": "Your Professional Title",
    "contact_info": [
        "123 Main St, City", 
        "email@domain.com",
        "+1-555-123-4567"
    ],
    # Other fields like education, experience, skills etc.
}
```
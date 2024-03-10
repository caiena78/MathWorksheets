from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random

def generate_problems(start:int,end:int):
    # Generate addition problems
    addition_problems = []
    for i in range(start, end):
        for j in range(start, end):
            addition_problems.append((i, j))    
#    Shuffle the list to randomize the order of problems
    random.shuffle(addition_problems) 
    return addition_problems
    

def generate_addition_worksheet(pdf_file:str,addition_problems:list):
    # Initialize the canvas
    c = canvas.Canvas(pdf_file, pagesize=letter)    
    # Set up the font
    c.setFont("Helvetica", 12)    
    x_start = 50  # Starting x-coordinate for the first column
    y_start = 750  # Starting y-coordinate
    row_count = 0
    col_count = 0    
    for i, problem in enumerate(addition_problems):
        x = x_start + (col_count * 200)  # Adjust x-coordinate for each column
        y = y_start - ((row_count % 25) * 25)  # Adjust y-coordinate for each row
        c.drawString(x, y, f"{problem[0]} + {problem[1]} = _____")        
        # Move to the next row or start a new page after every 20 rows
        if (i + 1) % 75 == 0:
            c.showPage()
            col_count = 0
            row_count = 0
        else:
            col_count += 1
            if col_count % 3 == 0:
                col_count=0
                row_count += 1    
    # Save the PDF
    c.save()


def generate_addition_answers(pdf_file:str,addition_problems:list):
    # Initialize the canvas
    c = canvas.Canvas(pdf_file, pagesize=letter)    
    # Set up the font
    c.setFont("Helvetica", 12)    
    x_start = 50  # Starting x-coordinate for the first column
    y_start = 750  # Starting y-coordinate
    row_count = 0
    col_count = 0    
    for i, problem in enumerate(addition_problems):
        x = x_start + (col_count * 200)  # Adjust x-coordinate for each column
        y = y_start - ((row_count % 25) * 25)  # Adjust y-coordinate for each row
        c.drawString(x, y, f"{problem[0]} + {problem[1]} = {problem[0]+problem[1]}")        
        # Move to the next row or start a new page after every 20 rows
        if (i + 1) % 75 == 0:
            c.showPage()
            col_count = 0
            row_count = 0
        else:
            col_count += 1
            if col_count % 3 == 0:
                col_count=0
                row_count += 1    
    # Save the PDF
    c.save()



problems=generate_problems(1,13)
# Generate the PDF worksheet
generate_addition_worksheet("addition_worksheet.pdf",problems)
generate_addition_answers("addition_answers.pdf",problems)


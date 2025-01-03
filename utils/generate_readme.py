import requests
import os
import re
import math

def find_solved_problems(base_dir):
    problem_numbers = []
    # Regular expression to match "problem_xxxx.jl" and extract the number
    pattern = re.compile(r"problem_(\d{4})\.jl")

    # Walk through the directory tree up to two levels deep
    for root, dirs, files in os.walk(base_dir):
        # Calculate depth by counting the number of separators in the path
        depth = root[len(base_dir):].count(os.sep)
        if depth > 2:  # Limit search to two levels deep
            continue
        
        for file in files:
            match = pattern.match(file)
            if match:  # Check if the file matches the pattern
                problem_number = int(match.group(1))  # Extract the number as an integer
                problem_numbers.append(problem_number)
    
    return sorted(problem_numbers)


def problem_url(problem_num):
    f1_n = (problem_num - 1) // 200
    f2_n = (problem_num - 1) // 25

    folder1 = f'/problems_{f1_n*200+1:04}_{(f1_n+1)*200:04}'
    folder2 = f'/{f2_n*25+1:04}_{(f2_n+1)*25:04}'
    file = f'/problem_{problem_num:04}.jl'

    base_url = "https://github.com/inigorrix/project_euler/blob/main"
    
    return base_url + folder1 + folder2 + file


def generate_markdown_table(filename, total_numbers, numbers_per_table, numbers_per_row, solved_problems):
    """
    Generates an HTML table in a markdown file with inline styles for consistent cell formatting.
    
    Args:
        filename (str): The output markdown filename.
        total_numbers (int): Total numbers to display in the table.
        numbers_per_row (int): Numbers per row in the table.
        solved_problems (list): List of solved problem numbers.
    """

    table = ""
    
    for t in range(0, math.ceil(total_numbers / numbers_per_table)):

        table += f'### Problems {t*numbers_per_table + 1} to {min((t+1)*numbers_per_table, total_numbers)}\n\n'
    
        # Start the HTML table with consistent cell styling
        table += '<table style="font-size: 10px; text-align: center; border-collapse: collapse; width: 100%; margin-bottom: 20px;">\n'
        
        # Loop through the numbers and organize them into rows
        for i in range(t*numbers_per_table + 1 , (t+1)*numbers_per_table + 1, numbers_per_row):
            table += "  <tr>\n"
            for j in range(i, min(i + numbers_per_row, total_numbers + 1)):
                if j in solved_problems:
                    # Make the solved cell a clickable link
                    table += f'    <td style="background-color: orange; color: black; padding: 8px;">' \
                             f'<a href="{problem_url(j)}" style="color: black; text-decoration: none; font-weight: bold;">{j}</a></td>\n'
                else:
                    table += f'    <td style="padding: 8px;">{j}</td>\n'
            table += "  </tr>\n"
    
        # End the HTML table structure
        table += "</table>\n\n\n"
    
    # Write the table to a markdown file
    with open(filename, 'w') as file:
        file.write(table)


def concatenate_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()

    # Writing the concatenated content to the output file in the parent directory
    with open(output_file, 'w') as out_file:
        out_file.write(content1)
        out_file.write("\n\n")  # Add some space between the two files
        out_file.write(content2)


# Find the latest available problem in the Project Euler website
r = requests.get("https://projecteuler.net/recent").text
a = r.find('<td class="id_column">')
latest_problem = r[a+22:a+25]

# Set the desired number of rows and columns
total_numbers = int(latest_problem)
numbers_per_table = 200
numbers_per_row = 20

# Dynamically determine the base directory (one level up from the script)
base_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Get the list of solved problem numbers
solved_problem_numbers = find_solved_problems(base_directory)

# Generate the markdown file
generate_markdown_table("generated_table.md", total_numbers, numbers_per_table, numbers_per_row, solved_problem_numbers)

print("Table file generated successfully!")

file1 = "base_readme.md"
file2 = "generated_table.md"
output_file = "../README.md"

concatenate_files(file1, file2, output_file)

print("README file generated successfully!")

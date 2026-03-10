import os
import ollama
import sys

def read_project(folder):
    code = ""

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith((".js", ".html", ".css", ".py")):
                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:
                        code += f"\n\nFILE: {file}\n"
                        code += f.read()
                except:
                    pass

    return code


def analyze_code(code):

    prompt = f"""
You are a senior software engineer.

Analyze the following project files.

Find:
1. unused variables
2. redundant functions
3. duplicate css
4. bad coding practices
5. performance improvements

Return the result in a structured report format.

CODE:
{code}
"""

    response = ollama.chat(
        model="deepseek-coder:6.7b",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response['message']['content']

    print("\nAI Analysis:\n")
    print(result)

    # save report
    with open("analysis_report.txt", "w", encoding="utf-8") as f:
        f.write("AI CODE ANALYSIS REPORT\n")
        f.write("=======================\n\n")
        f.write(result)

    print("\nReport saved as analysis_report.txt")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python agent.py <project-folder>")
        exit()

    folder = sys.argv[1]

    print("Reading project files...")

    code = read_project(folder)

    analyze_code(code)
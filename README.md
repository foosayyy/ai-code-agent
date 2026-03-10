# Local AI Codebase Analyzer Agent

## Overview

This project is a **local AI-powered code analysis agent**.
It scans a project folder, reads the code files, and uses an AI model running on your computer to analyze the code.

The agent can detect common coding issues such as:

* Unused variables
* Redundant functions
* Duplicate CSS
* Performance problems
* Bad coding practices

It then generates:

* **A structured JSON report** describing the problems found
* **A patch file** containing suggested fixes

The entire system runs **locally on your machine**, so your code never needs to leave your computer.

---

# How It Works

The workflow of the agent looks like this:

User runs agent
↓
Agent reads project files
↓
AI analyzes the code
↓
Agent generates a report
↓
Agent generates suggested fixes

Outputs created:

```
reports/analysis_report.json
patches/fixes.patch
```

---

# Project Structure

```
AI-Code-Agent/
│
├── agent.py
├── analyzer.py
├── patch_generator.py
│
├── reports/
│   └── analysis_report.json
│
├── patches/
│   └── fixes.patch
│
├── projects/
│   └── test-project/
│       ├── index.html
│       ├── style.css
│       └── script.js
```

Explanation of important files:

| File               | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| agent.py           | Main controller that runs the agent            |
| analyzer.py        | Reads project files and sends them to the AI   |
| patch_generator.py | Creates suggested code fixes                   |
| reports/           | Stores AI analysis reports                     |
| patches/           | Stores suggested fixes                         |
| projects/          | Folder containing projects you want to analyze |

---

# Features

This AI agent can:

* Scan entire project folders
* Analyze HTML, CSS, JavaScript, and Python
* Generate structured analysis reports
* Suggest code improvements
* Run completely **offline**

---

# Requirements

You need the following installed:

* Python 3
* Ollama (local AI runtime)
* A coding AI model

---

# Step 1 — Install Ollama

Download and install Ollama from:

https://ollama.com

Check installation:

```
ollama --version
```

---

# Step 2 — Install the AI Model

Download the coding model used for analysis:

```
ollama pull deepseek-coder:6.7b
```

---

# Step 3 — Install Python Dependency

Install the Ollama Python package:

```
pip install ollama
```

---

# Step 4 — Add Your Project

Put any project you want to analyze inside:

```
projects/
```

Example:

```
projects/my-project
```

Inside that folder you can place files like:

```
index.html
script.js
style.css
```

---

# Step 5 — Run the AI Agent

Run the agent using:

```
python agent.py projects/my-project
```

The agent will:

1. Read the project files
2. Send them to the AI model
3. Generate a report
4. Generate suggested fixes

---

# Output Files

After running the agent you will see:

## JSON Report

```
reports/analysis_report.json
```

Example output:

```
{
 "unused_variables": ["temp"],
 "unused_functions": ["unusedFunction"],
 "duplicate_css": [],
 "performance_issues": [],
 "suggestions": [
   "Avoid global variables"
 ]
}
```

---

## Patch File

```
patches/fixes.patch
```

Example:

```
# Suggested Fix
Remove unusedFunction() from script.js
```

This file contains suggestions for improving the code.

---

# Example Workflow

Typical usage looks like this:

1. Add project to `projects/`
2. Run the agent
3. Check the generated report
4. Apply suggested improvements

---

# Why This Project Exists

Developers often work with large codebases where it is difficult to manually find inefficiencies.

This project demonstrates how **AI agents can assist developers by automatically reviewing code and suggesting improvements.**

It is also a demonstration of:

* Local AI development
* AI-powered developer tools
* Code analysis automation

---

# Future Improvements

Possible upgrades for this project include:

* Automatic code refactoring
* Support for larger repositories
* Integration with Git workflows
* Vector database for large codebases
* Multi-agent architecture

---

# Technologies Used

* Python
* Ollama
* DeepSeek Coder
* Local AI models

---

# Author

Created as a learning project exploring **local AI agents for software development tools**.

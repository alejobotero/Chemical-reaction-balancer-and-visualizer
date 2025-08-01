# Chemical Reaction Visualizer & Balancer

This web application allows users to input chemical reactions to be balanced automatically and visualize molecular structures using SMILES notation. It is built with Python using the Flask framework, styled with Tailwind CSS, and uses RDKit for molecular rendering.

---

## Features

- **Chemical Reaction Balancer**  
  Accepts chemical equations (e.g., `H2 + O2 -> H2O`) and returns a properly balanced equation using matrix-based stoichiometry logic.

- **Molecule Visualizer (SMILES)**  
  Accepts SMILES strings (e.g., `CCO + O=O`) and generates molecular structure images.

- **Dark Mode Support**  
  Includes a toggle for light/dark themes with persistent preference using localStorage.

- **Responsive Design**  
  Built with Tailwind CSS to support a clean, accessible interface across screen sizes.

---

## Technologies Used

- **Python** – Core backend logic  
- **Flask** – Web framework for routing and form handling  
- **RDKit** – Molecule rendering from SMILES  
- **Tailwind CSS** – Utility-first styling for UI  
- **HTML / Jinja2** – Template rendering  
- **JavaScript** – Frontend logic for dark mode  
- **Base64** – Image encoding for inline rendering

---


## Getting Started

1. **Clone the Repository**

``bash
git clone https://github.com/your-username/chemical-reaction-balancer.git
cd chemical-reaction-balancer
Install Dependencies

You need Python 3 and pip installed. Then run:

bash
Copy
Edit
pip install flask rdkit-pypi
Note: rdkit-pypi may require additional system dependencies. See RDKit installation instructions for more details if needed.

Run the Application

bash
Copy
Edit
python app.py
Open your browser and go to:
http://localhost:5001/

How It Works
The reaction balancer parses the equation into reactants and products, converts the problem into a system of linear equations, and solves for the coefficients.

The visualizer parses SMILES strings using RDKit and renders molecule images, which are then base64-encoded and embedded directly into the HTML.

Dark mode is handled on the frontend with JavaScript and Tailwind's dark: classes.

Future Improvements
User authentication and history of balanced reactions

Client-side validation for input formats

Export options for balanced equations or images

3D molecular visualization support



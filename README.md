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

## Project Structure


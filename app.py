from flask import Flask, render_template, request, session, redirect, url_for
from balancer import balance, draw_molecules
import io
import base64

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session management

def fmt_coeff(x):
    if abs(x - round(x)) < 1e-6:
        return str(int(round(x)))
    else:
        return f"{x:.2f}"

@app.route('/', methods=['GET', 'POST'])
def index():
    balanced_equation = ''
    balance_msg = ''
    img_data = None
    visualize_msg = ''

    # Initialize dark mode if not set
    if 'dark_mode' not in session:
        session['dark_mode'] = False

    if request.method == 'POST':
        if 'toggle_dark_mode' in request.form:
            # Toggle dark mode flag in session
            session['dark_mode'] = not session['dark_mode']
            # Redirect to GET so that form resubmission doesn't happen on refresh
            return redirect(url_for('index'))

        # Reaction Balancer form
        elif 'balance_submit' in request.form:
            formula = request.form.get('reaction_formula', '').strip()
            if '->' in formula:
                try:
                    reactants, products, balanced = balance(formula)
                    balanced_equation = ' + '.join(
                        f"{fmt_coeff(balanced[i])} {reactants[i]}" for i in range(len(reactants))
                    )
                    balanced_equation += ' -> '
                    balanced_equation += ' + '.join(
                        f"{fmt_coeff(balanced[i+len(reactants)])} {products[i]}" for i in range(len(products))
                    )
                    balance_msg = "Reaction Balanced Successfully!"
                except Exception as e:
                    balance_msg = f"Error balancing reaction: {e}"
            else:
                balance_msg = "Invalid reaction format. Use '->' to separate reactants and products."

        # Molecule Visualizer form
        elif 'visualize_submit' in request.form:
            smiles_input = request.form.get('smiles_input', '').strip()
            compounds = [s.strip() for s in smiles_input.split('+') if s.strip()]
            try:
                if compounds:
                    img = draw_molecules(compounds)
                    buf = io.BytesIO()
                    img.save(buf, format='PNG')
                    buf.seek(0)
                    img_data = base64.b64encode(buf.read()).decode('utf-8')
                    visualize_msg = "Molecules Rendered Successfully!"
                else:
                    visualize_msg = "Please enter valid SMILES strings."
            except Exception as e:
                visualize_msg = f"Error rendering molecules: {e}"

    return render_template('index.html',
                           balanced_equation=balanced_equation,
                           balance_msg=balance_msg,
                           img_data=img_data,
                           visualize_msg=visualize_msg,
                           dark_mode=session['dark_mode'])

if __name__ == '__main__':
    app.run(debug=True, port=5001)

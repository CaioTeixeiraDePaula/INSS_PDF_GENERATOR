from flask import Flask, render_template, request, send_file
# from weasyprint import HTML
import io
from helpers import notes_date_data_generator

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/generate/notes", methods=['POST'])
def gen_notes_data():
    """Gera os dados dos recibos e exibe na página."""
    
    # Coletando os dados do formulário
    data = {
        "constructor_name": request.form['constructorName'],
        "construction_year_start": request.form['constructionYearStart'],
        "construction_year_end": request.form['constructionYearEnd'],
        "construction_month_start": request.form['constructionMonthStart'],
        "construction_month_end": request.form['constructionMonthEnd'],
        "note_price_number": request.form['notePriceNumber'],
        "note_price_text": request.form['notePriceText'],
        "construction_road": request.form['constructionRoad'],
        "construction_road_number": request.form['constructionRoadNumber'],
        "construction_complement": request.form.get('constructionComplement', ''),
        "construction_city": request.form['constructionCity'],
        "construction_federal_state": request.form['federalStateAbreviation'],
        "note_emiter_name": request.form['noteEmiterName'],
        "note_emiter_cpf": request.form['noteEmiterCPF'],
        "note_emiter_rg": request.form['noteEmiterRG'],
        "note_emiter_rg_organ_emiter": request.form['noteEmiterRGOrganEmiter'],
        "note_emiter_road": request.form['noteEmiterRoad'],
        "note_emiter_road_number": request.form['noteEmiterRoadNumber'],
        "note_emiter_road_complement": request.form.get('noteEmiterRoadComplement', ''),
        "note_emiter_cep": request.form['noteEmiterCEP'],
        "note_emiter_city": request.form['noteEmiterCity'],
        "note_emiter_federal_state": request.form['noteEmitorFederalStateAbreviation'],
        "note_emiter_cell_phone": request.form['noteEmiterCellPhone'],
        "note_emiter_fixed_phone": request.form.get('noteEmiterFixedPhone', ""),
        "notes_data": notes_date_data_generator(
            request.form['constructionYearStart'], request.form['constructionMonthStart'],
            request.form['constructionYearEnd'], request.form['constructionMonthEnd']
        )
    }

    return render_template("recibo.html", **data)

# @app.route('/generate/pdf', methods=['POST'])
# def generate_pdf():
#     """Gera o PDF com os recibos exibidos na página."""
#     html_content = render_template('recibo_template.html', **request.form.to_dict())

#     pdf = HTML(string=html_content).write_pdf()

#     return send_file(
#         io.BytesIO(pdf),
#         mimetype='application/pdf',
#         as_attachment=True,
#         download_name="recibos.pdf"
#     )

if __name__ == "__main__":
    app.run(debug=True)

from weasyprint import HTML
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, send_file
from helpers import *
import io

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def test():
    return render_template("form.html")

@app.route("/generate/notes", methods=['POST'])
def gen_notes_data():
    """
    Função que recebe os valores do formulário e gera os dados dos recibos
    """

    # Variáveis de informações da obra e do construtor
    constructor_name = request.form['constructorName']
    construction_year_start = request.form['constructionYearStart']
    construction_year_end = request.form['constructionYearEnd']
    construction_month_start = request.form['constructionMonthStart']
    construction_month_end = request.form['constructionMonthEnd']
    
    # Valores do serviço
    note_price_number = request.form['notePriceNumber']
    note_price_text = request.form['notePriceText']
    
    # Localização da obra
    construction_road = request.form['constructionRoad']
    construction_road_number = request.form['constructionRoadNumber']
    construction_complement = request.form['constructionComplement']
    construction_city = request.form['constructionCity']
    construction_federal_state = request.form['federalStateAbreviation']
    
    # Dados do emitente
    note_emiter_name = request.form['noteEmiterName']
    note_emiter_cpf = request.form['noteEmiterCPF']
    note_emiter_rg = request.form['noteEmiterRG']
    note_emiter_rg_organ_emiter = request.form['noteEmiterRGOrganEmiter']
    
    note_emiter_road = request.form['noteEmiterRoad']
    note_emiter_road_number = request.form['noteEmiterRoadNumber']
    note_emiter_road_complement = request.form.get('noteEmiterRoadComplement', '')
    note_emiter_cep = request.form['noteEmiterCEP']
    note_emiter_city = request.form['noteEmiterCity']
    note_emiter_federal_state = request.form['noteEmitorFederalStateAbreviation']
    
    note_emiter_cell_phone = request.form['noteEmiterCellPhone']
    note_emiter_fixed_phone = request.form.get('noteEmiterFixedPhone', "")

    # Gerar os dados dos recibos
    notes_data = notes_date_data_generator(
        construction_year_start, construction_month_start,
        construction_year_end, construction_month_end
    )

    # Criar contexto para o template
    context = {
        "constructor_name": constructor_name,
        "construction_road": construction_road,
        "construction_road_number": construction_road_number,
        "construction_complement": construction_complement,
        "construction_city": construction_city,
        "construction_federal_state": construction_federal_state,
        "note_price_number": note_price_number,
        "note_price_text": note_price_text,
        "note_emiter_name": note_emiter_name,
        "note_emiter_cpf": note_emiter_cpf,
        "note_emiter_rg": note_emiter_rg,
        "note_emiter_rg_organ_emiter": note_emiter_rg_organ_emiter,
        "note_emiter_road": note_emiter_road,
        "note_emiter_road_number": note_emiter_road_number,
        "note_emiter_road_complement": note_emiter_road_complement,
        "note_emiter_cep": note_emiter_cep,
        "note_emiter_city": note_emiter_city,
        "note_emiter_federal_state": note_emiter_federal_state,
        "note_emiter_cell_phone": note_emiter_cell_phone,
        "note_emiter_fixed_phone": note_emiter_fixed_phone,
        "notes_data": notes_data
    }

    # Retorna o HTML com o contexto
    return render_template("recibo.html", **context)

@app.route('/generate/pdf', methods=['POST'])
def generate_pdf():
    """
    Rota para gerar o PDF a partir do HTML
    """
    # Obter dados enviados pelo formulário
    constructor_name = request.form['constructorName']
    construction_year_start = request.form['constructionYearStart']
    construction_year_end = request.form['constructionYearEnd']
    construction_month_start = request.form['constructionMonthStart']
    construction_month_end = request.form['constructionMonthEnd']
    # Continue com os outros campos de dados necessários...

    # Gerar os dados dos recibos
    notes_data = notes_date_data_generator(
        construction_year_start, construction_month_start,
        construction_year_end, construction_month_end
    )

    # Criar contexto para o template
    context = {
        "constructor_name": constructor_name,
        "notes_data": notes_data
    }

    # Renderizar o HTML com o contexto
    html_content = render_template('recibo.html', **context)

    # Gerar o PDF
    pdf = HTML(string=html_content).write_pdf()

    # Enviar o PDF para o usuário
    return send_file(
        io.BytesIO(pdf),
        mimetype='application/pdf',
        as_attachment=True,
        download_name="recibos.pdf"
    )

if __name__ == "__main__":
    app.run(debug=True)

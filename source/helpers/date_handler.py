from datetime import datetime
from dateutil.relativedelta import relativedelta 

months_linking_data:dict = {
    "janeiro"  : {"code" : 1,  "emition_day" : 31},
    "fevereiro": {"code" : 2,  "emition_day" : 28},
    "março"    : {"code" : 3,  "emition_day" : 31},
    "abril"    : {"code" : 4,  "emition_day" : 30},
    "maio"     : {"code" : 5,  "emition_day" : 31},
    "junho"    : {"code" : 6,  "emition_day" : 30},
    "julho"    : {"code" : 7,  "emition_day" : 31},
    "agosto"   : {"code" : 8,  "emition_day" : 31},
    "setembro" : {"code" : 9,  "emition_day" : 30},
    "outubro"  : {"code" : 10, "emition_day" : 31},
    "novembro" : {"code" : 11, "emition_day" : 30},
    "dezembro" : {"code" : 12, "emition_day" : 31}
}

def total_notes_num_generator(start_year:str, start_month:str, end_year:str, end_month:str) -> int:
    year_diference:int = int(end_year) - int(start_year)
    
    if int(end_year) < int(start_year):
        return "Ano de término inválido. Favor verificar novamente"

    if months_linking_data[start_month] == months_linking_data[end_month]:
        match year_diference:
            case 0:
                return 1
            case _:
                return 12 * year_diference + 1

    else:
        if months_linking_data[end_month]["code"] > months_linking_data[start_month]["code"]:
            return (months_linking_data[end_month]["code"] - months_linking_data[start_month]['code'] ) + (( year_diference ) * 12) + 1
        
        elif months_linking_data[end_month]["code"] < months_linking_data[start_month]["code"]:
            match year_diference:
                case 0:
                    return ((months_linking_data['dezembro']["code"] - months_linking_data[start_month]['code']) + (months_linking_data[end_month]["code"])) + (( year_diference +1 ) * 12) +1
                case _:
                    return ((months_linking_data['dezembro']["code"] - months_linking_data[start_month]['code']) + (months_linking_data[end_month]["code"])) + (( year_diference -1 ) * 12) +1


def notes_date_data_generator(start_year: str, start_month: str, end_year: str, end_month: str):
    total_notes = total_notes_num_generator(start_year, start_month, end_year, end_month)
    
    start_date = datetime(int(start_year), months_linking_data[start_month]["code"], 1)
    notes_data = {}

    for i in range(total_notes):
        note_date = start_date + relativedelta(months=i)  # Avança corretamente de mês a mês
        month_name = [key for key, value in months_linking_data.items() if value["code"] == note_date.month][0]

        notes_data[i + 1] = {
            "month": month_name,
            "year": note_date.year,
            "emition_day": months_linking_data[month_name]["emition_day"],
        }

    return notes_data

# Teste do código
notes = notes_date_data_generator("2023", "agosto", "2024", "agosto")
print(notes)
import openpyxl

def convert_text_to_excel(input_file, output_file):
    # Ouvrir le fichier texte en lecture
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Créer un nouveau classeur Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Parcourir les lignes du fichier texte et les écrire dans le classeur Excel
    for row_index, line in enumerate(lines, start=1):
        cells = line.strip().split(',')  # Utiliser la virgule comme délimiteur
        for col_index, cell_value in enumerate(cells, start=1):
            sheet.cell(row=row_index, column=col_index).value = cell_value.strip()

    # Enregistrer le classeur Excel dans un fichier
    workbook.save(output_file)
    print("convertion terminee") 

# Exemple d'utilisation
input_file = r'D:/projets/fichier.txt'   # Chemin du fichier texte à convertir
output_file = r'D:/projets/output.xlsx'  # Chemin du fichier Excel de sortie

convert_text_to_excel(input_file, output_file)
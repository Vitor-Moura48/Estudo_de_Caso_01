# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
# from reportlab.lib.styles import getSampleStyleSheet

# def GeneratePDF():
#     try:
#         doc = SimpleDocTemplate('d.pdf', pagesize=letter, leftMargin=20, rightMargin=20, topMargin=20, bottomMargin=20)
#         story = []

#         # Define the PDF styles
#         styles = getSampleStyleSheet()
#         title_style = styles['Title']
#         body_style = styles['Normal']

#         # Add a title to the PDF
#         title = "Sistema de Informação EcoEnergy".upper()
#         title_paragraph = Paragraph(title, title_style)
#         story.append(title_paragraph)

#         # Add a section for consumption report
#         consumption_section = "Módulo de Relatório de Consumo de Energia"
#         consumption_paragraph = Paragraph(consumption_section, body_style)
#         story.append(consumption_paragraph)

#         # Add a table for energy expenses
#         data = [
#             ["Date", "Description", "Amount"],
#             ["2023-01-01", "Electricity bill", "$200"],
#             ["2023-02-01", "Gas bill", "$100"],
#             ["2023-03-01", "Water bill", "$50"],
#         ]

#         # Create a table and set its style
#         table = Table(data, colWidths=120, rowHeights=30)
#         table.setStyle(TableStyle([
#             ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
#             ('BACKGROUND', (0, 1), (-1, -1), colors.white),
#             ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
#             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#             ('GRID', (0, 0), (-1, -1), 1, colors.black),
#             ('WIDTH', (0, 0), (-1, -1), 850),  # Increase the width of the cells
#         ]))

#         story.append(Spacer(1, 20))  # Add some space before the table
#         story.append(table)

#         # Add more content as needed

#         doc.build(story)
#     except Exception as e:
#         print(f'Error while generating the PDF: {e}')

# GeneratePDF()

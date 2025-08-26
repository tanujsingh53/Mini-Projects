from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many PDF's do you want to merge?\n"))

for i in range(0, n):
    name = input(f"Enter the name of the {i + 1}: ")
    pdfs.append(name)

try:

    for pdf in pdfs:
        merger.append(pdf)

    output_name = "merged-pdf.pdf"
    merger.write(output_name)
    merger.close()

    print(f"✅ Successfully merged {n} PDFs into '{output_name}'")

except FileNotFoundError as e:
    print(f"❌ Error: {e}. Please check if the file name/path is correct.")
except Exception as e:
    print(f"⚠️ Something went wrong: {e}")
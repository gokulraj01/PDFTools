import PyPDF2 as pdf
pdf_file_1 = open("sample1.pdf", 'rb')
pdf_file_2 = open("sample2.pdf", 'rb')

pdf_read1 = pdf.PdfFileReader(pdf_file_1)
pdf_read2 = pdf.PdfFileReader(pdf_file_2)

pdf_merger = pdf.PdfFileMerger()

pdf_merger.append(pdf_read1)
pdf_merger.append(pdf_read2)

op_file = open("op.pdf", 'wb')
pdf_merger.write(op_file)
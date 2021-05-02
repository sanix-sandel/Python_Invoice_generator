from weasyprint import HTML
import flask

if __name__=='__main__':
    html=HTML('invoice.html')
    html.write_pdf('invoice.pdf')
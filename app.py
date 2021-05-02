from flask import Flask, render_template, send_file
import os 
from datetime import datetime
from weasyprint import HTML
import io

app=Flask(__name__)


@app.route('/')
def hello_world():
    today=datetime.today().strftime("%B %-d, %Y")
    invoice_number=123
    from_addr={
        'company_name':'Python Tip',
        'addr1':'12345 Sunny Road',
        'addr2':'Sunnyvill, CA 12345'
    }
    to_addr={
        'company_name':'Acme Corp',
        'person_name':'John Dilly',
        'person_email':'john@example.com'
    }
    items=[
        {
            'title':'website design',
            'charge':300.00
        },
        {
            'title':'Hosting (3 months)',
            'charge':75.00
        },
        {
            'title':'Domain name (1 year)',
            'charge':10.00
        }
    ]
    duedate="August 1, 2018"
    total=sum([i['charge'] for i in items])
    rendered = render_template('invoice.html', date=today, 
                                            from_addr=from_addr, 
                                            to_addr=to_addr,
                                            items=items,
                                            total=total,
                                            invoice_number=invoice_number,
                                            duedate=duedate)
    html=HTML(string=rendered)
    rendered_pdf=html.write_pdf()
    return send_file(
        io.BytesIO(rendered_pdf),
        attachement_filename='invoice.pdf'
    )


if __name__=='__main__':
    port=int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)    
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import codecs
import pdfkit
import errno
import os
import glob

# https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python#600612
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

df = pd.read_excel("funny-quotes.xlsx")
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")

mkdir_p("output")
images = glob.glob("images/*")
img_count = len(images)

for row_id, row in df.iterrows():
    print row_id
    quote = row["Quote"]
    author = row["Author"]
    img_idx = row_id % img_count
    image = "../%s" % images[img_idx]
    template_data = {
        "quote": quote,
        "author": author,
        "image": image
    }

    html_filename = "output/output%02d.html" % (row_id)
    pdf_filename = "output/output%02d.pdf" % (row_id)
    html_out = template.render(template_data)

    print "Generate HTML: ", html_filename
    with codecs.open(html_filename, "w", encoding="utf8") as f:
        f.write(html_out)
        f.close()

    print "Generate PDF: ", pdf_filename
    pdfkit.from_file(html_filename, pdf_filename)

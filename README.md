# What?

This is a tool to generate single page PDFs with an image and a funny inspirational quote.

Just edit the file `funny-quotes.xlsx`, and place your Images in `images/` folder, then follow the instructions below.

## Setup

```
sudo dnf install -y wkhtmltopdf
virtualenv --system-site-packages env
source env/bin/activate
pip install -r requirements.txt
```

## Run

```
$ python script.py
0
Generate HTML:  output/output00.html
Generate PDF:  output/output00.pdf
Loading page (1/2)
Printing pages (2/2)
Done
1
Generate HTML:  output/output01.html
Generate PDF:  output/output01.pdf
Loading page (1/2)n
Printing pages (2/2)
Done
2
Generate HTML:  output/output02.html
Generate PDF:  output/output02.pdf
Loading page (1/2)
Printing pages (2/2)
Done
...
...
45
Generate HTML:  output/output45.html
Generate PDF:  output/output45.pdf
Loading page (1/2)
Printing pages (2/2)
Done
```



*Image Source*

[Flickr](https://www.flickr.com/search/?license=4%2C5%2C6%2C9%2C10&advanced=1&media=photos&color_codes=e%2Cc&dimension_search_mode=min&height=640&width=640&text=red%20hat&sort=relevance)

*Quotes Source*

[Funny Quotes](http://www.curatedquotes.com/inspirational-quotes/funny/)


# Reads in top, bottom, middle HTML file for INDEX
top_template = open('./templates/top.html').read()
bottom_template = open('./templates/bottom.html').read()
content = open('./content/index.html').read()
index_html = top_template + content + bottom_template
open('docs/index.html', 'w+').write(index_html)

# Reads in top, bottom, middle HTML file for ABOUT
content = open('./content/about.html').read()
about_html = top_template + content + bottom_template
open('docs/about.html', 'w+').write(about_html)

# Reads in top, bottom, middle HTML file for PORTFOLIO
content = open('./content/portfolio.html').read()
portfolio_html = top_template + content + bottom_template
open('docs/portfolio.html', 'w+').write(portfolio_html)

# Reads in top, bottom, middle HTML file for CONTACT
content = open('./content/contact.html').read()
contact_html = top_template + content + bottom_template
open('docs/contact.html', 'w+').write(about_html)
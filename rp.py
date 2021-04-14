import webbrowser

pub_year = input('pub_year e.g., "2020"')
pages = input('pages e.g., "634-645"')

url_ = "https://pubmed.ncbi.nlm.nih.gov/?term={0}[Date - Publication] AND {1}[Pagination]".format(pub_year, pages)
webbrowser.open(url_)
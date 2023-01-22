import utils
import wikipedia
import soup
import graph

BASE_URL = "https://en.wikipedia.org/w/api.php"
PARAMS = {
    "action": "parse",
    "format": "json",
    # "page": "Timeline_of_programming_languages",
    "pageid": 23696,
    "prop": "text|revid|parsewarnings",
    "utf8": 1,
    "formatversion": 2,
}


def main():
    url = utils.build_url(BASE_URL, PARAMS)
    html = wikipedia.get_html(url)
    rows = soup.get_table_rows(html)
    rows = [soup.tr_to_dict(tr) for tr in rows]
    g = graph.build_graph(rows)
    for node in g:
        print(node, node.predecessor_nodes)


main()

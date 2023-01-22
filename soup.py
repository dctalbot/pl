from typing import Dict
from bs4 import BeautifulSoup, ResultSet, Tag
import re


def get_table_rows(html: str) -> ResultSet:
    soup = BeautifulSoup(html, "html.parser")
    tables = soup("table", class_="wikitable sortable")
    result = []
    for table in tables:
        rows = table("tr")
        for index, tr in enumerate(rows):
            # if first or last row, skip
            if index == 0 or index == len(rows) - 1:
                continue

            # if not 4 columns, skip
            if len(tr("td")) != 4:
                continue

            result.append(tr)

    return result


def common_fmt(text: str) -> str:
    result = text.strip()
    result = re.sub("[\(\[].*?[\)\]]", "", result)
    return result.strip()


def tr_to_dict(tr: Tag) -> Dict:
    data = tr("td")

    predecessors = data[3].get_text().strip().split(",")
    predecessors = [common_fmt(p) for p in predecessors if p]
    if any("unique lang" in p.lower() for p in predecessors):
        predecessors = []
    predecessors = set(predecessors)

    return {
        "year": common_fmt(data[0].get_text().strip()),
        "name": common_fmt(data[1].get_text().strip()),
        "creator": common_fmt(data[2].get_text().strip()),
        "predecessors": predecessors,
    }

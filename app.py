from sanic import Sanic
from sanic.response import html
from jinja2 import Environment, PackageLoader

from sqlalchemy import create_engine

env = Environment(loader=PackageLoader('app', 'templates'))

app = Sanic(__name__)
conn_uri = "mssql+pymssql://dungnt:Password01`@172.20.2.110/RecommendDB"

app.static('/flip', './flip')


@app.route('/')
async def index(request):
    db = create_engine(conn_uri).connect()

    cur = db.execute("exec PBI_GetTotalContractActive")
    row = cur.fetchall()

    db.close()

    template = env.get_template('index.html')
    html_content = template.render(totalContract=(2000000 + row[0][1] - row[0][0]), newTotalContract=row[0][1])

    return html(html_content)


if __name__ == '__main__':
    app.run(debug=True)
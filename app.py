from sanic import Sanic
from sanic.response import html, json
from jinja2 import Environment, PackageLoader
from datetime import datetime

from sqlalchemy import create_engine

env = Environment(loader=PackageLoader('app', 'templates'))

app = Sanic(__name__)
conn_uri = "mssql+pymssql://dungnt:Password01`@172.20.2.110/RecommendDB"

app.static('/static', './static')


@app.route('/')
async def index(request):
    now = datetime.now()
    db = create_engine(conn_uri).connect()

    cur = db.execute("exec PBI_GetTotalContractActive")
    row = cur.fetchall()

    db.close()

    template = env.get_template('index.html')
    html_content = template.render(totalContract=row[0][0], current_time=now.strftime("%d/%m/%Y %H:%M:%S"))

    return html(html_content)


@app.route('/get_count')
async def get_count(request):
    db = create_engine(conn_uri).connect()

    cur = db.execute("exec PBI_GetTotalContractActive")
    row = cur.fetchall()

    db.close()

    return json ({'newTotalContract':row[0][0]})


if __name__ == '__main__':
    app.run(debug=True)
import aiohttp_jinja2
from aiohttp import web
import pandas
import typing as tp

FLAT_COLUMNS = ['totsp', 'livesp', 'kitsp', 'dist', 'code']


@aiohttp_jinja2.template('index.html')
async def handle(request: web.Request) -> tp.Dict[str, str]:
    request.app.logger.info(f'got request')

    data = await request.post()
    data_list = [float(data[column]) for column in FLAT_COLUMNS]

    features_df = pandas.DataFrame(data=[data_list], columns=FLAT_COLUMNS)

    flat_model = request.app['model']
    prediction = flat_model.predict(features_df)[0][0]

    return {'result': f'{prediction:.2f} thousands of dollars'}

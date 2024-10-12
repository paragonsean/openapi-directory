from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def convert(request: web.Request, hundreds_form=None, the_number=None, unit=None) -> web.Response:
    """convert

    Convert the number into its Arabic text representation حول العدد إلى ما يقابله كتابة

    :param hundreds_form: Some use مائة others use مئة , both works in Arabic. If left empty the default is مائة 
    :type hundreds_form: str
    :param the_number: Put the number here. Decimal is supported by most units.
    :type the_number: str
    :param unit: The counted subject, be it a currency like درهم إماراتي  or a size unit like متر مربع If the unit does not appear in the text result, it may not be supported. Please contact us to add it.
    :type unit: str

    """
    return web.Response(status=200)

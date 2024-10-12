from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def list_vendors_get(request: web.Request, naics, setasides=None, vehicle=None) -> web.Response:
    """This endpoint returns a list of vendors filtered by a NAICS code

    &lt;p&gt;This endpoint returns a list of vendors filtered by a NAICS code. The NAICS code maps to an OASIS pool and is used to retrieve vendors in that pool only.&lt;/p&gt; &lt;p&gt;OASIS pools are groupings of NAICS codes that have the same small business size standard. Because contracts solicited to OASIS vendors can only be issued to one pool, much of the data is presented as part of a pool grouping. Using the NAICS code is a shortcut, so that you don&#39;t have to explicitly map the NAICS code to a pool in OASIS yourself.&lt;/p&gt; &lt;p&gt;Vendors can also be filtered by a particular setaside. Valid values for the setasides are two-character codes which include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;A6 (8(a))&lt;/li&gt; &lt;li&gt;XX (Hubzone)&lt;/li&gt; &lt;li&gt;QF (service disabled veteran owned)&lt;/li&gt; &lt;li&gt;A2 (women owned)&lt;/li&gt; &lt;li&gt;A5 (veteran owned)&lt;/li&gt; &lt;li&gt;27 (small disadvantaged business).&lt;/li&gt; &lt;/ul&gt;

    :param naics: a six digit NAICS code (required)
    :type naics: str
    :param setasides: a comma delimited list of two character setaside codes to filter by.  Ex. setasides&#x3D;A6,A5  will filter by 8a and veteran owned business.
    :type setasides: List[str]
    :param vehicle: Choices are either oasis or oasissb. Will filter vendors by their presence in either the OASIS unrestricted vehicle or the OASIS Small Business vehicle.
    :type vehicle: str

    """
    return web.Response(status=200)

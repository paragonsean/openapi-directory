from typing import List, Dict
from aiohttp import web

from openapi_server.models.bca_definition_meta import BCADefinitionMeta
from openapi_server.models.error_definition400 import ErrorDefinition400
from openapi_server.models.error_definition408 import ErrorDefinition408
from openapi_server.models.error_definition429 import ErrorDefinition429
from openapi_server.models.error_definition500 import ErrorDefinition500
from openapi_server.models.error_definition503 import ErrorDefinition503
from openapi_server import util


async def open_banking_v22_business_current_accounts_get(request: web.Request, ) -> web.Response:
    """open_banking_v22_business_current_accounts_get

    This API will return data about all BCA products and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.


    """
    return web.Response(status=200)


async def x_open_banking_v22_business_current_accounts_segment_segment_get(request: web.Request, segment) -> web.Response:
    """x_open_banking_v22_business_current_accounts_segment_segment_get

    This extended API will return data about all BCA products for the specified segment. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

    :param segment: Segment name from this list&amp;#58; &amp;quot;ClientAccount&amp;quot;, &amp;quot;Standard&amp;quot;, &amp;quot;NonCommercial&amp;quot;, &amp;quot;Religious&amp;quot;, &amp;quot;SectorSpecific&amp;quot;, &amp;quot;Startup&amp;quot;, &amp;quot;Switcher&amp;quot;.
    :type segment: str

    """
    return web.Response(status=200)

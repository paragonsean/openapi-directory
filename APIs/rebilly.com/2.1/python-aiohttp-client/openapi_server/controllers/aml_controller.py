from typing import List, Dict
from aiohttp import web

from openapi_server.models.aml import AML
from openapi_server import util


async def get_aml_entry(request: web.Request, first_name, last_name, organization_id=None, dob=None, country=None) -> web.Response:
    """Search PEP/Sanctions/Adverse Media lists

    Search multiple PEP/Sanctions/Adverse Media lists with first and last name to find any blocklisted identities. Performs a fuzzy search including soundex. Not all fields are guaranteed to be filled. 

    :param first_name: First name of individual to search.
    :type first_name: str
    :param last_name: Last name of individual to search.
    :type last_name: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param dob: Date of birth in format YYYY-MM-DD.
    :type dob: str
    :param country: Country of individual as an ISO Alpha-2 code.
    :type country: str

    """
    return web.Response(status=200)

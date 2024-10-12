from typing import List, Dict
from aiohttp import web

from openapi_server.models.category_results import CategoryResults
from openapi_server.models.law_result import LawResult
from openapi_server.models.laws_response import LawsResponse
from openapi_server.models.poc_results import PocResults
from openapi_server import util


async def transportation_incentives_laws_all(request: web.Request, output_format, api_key, limit=None, jurisdiction=None, technology=None, incentive_type=None, regulation_type=None, user_type=None, poc=None, recent=None, expired=None, law_type=None, keyword=None, local=None) -> web.Response:
    """Return a full list of laws and incentives that match your query.

    

    :param output_format: Response format
    :type output_format: str
    :param api_key: API Key
    :type api_key: str
    :param limit: Limit the number of laws returned
    :type limit: int
    :param jurisdiction: Return laws for the given Jurisdiction. Jurisdiction must be given as a two character state code (eg, &#39;CO&#39; for Colorado). A single jurisdiction, or a comma-separate list of multiple jurisdiction, may be given.  Use the code &#39;US&#39; for federal laws and the code &#39;DC&#39; for Washington D.C.
    :type jurisdiction: str
    :param technology: Search by the technology type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: &#39;BIOD&#39; for Biodiesel, &#39;ETH&#39; for Ethanol / Flexible Fuel Vehicles, &#39;NG&#39; for Natural Gas / Natural Gas Vehicles, &#39;LPG&#39; for Liquefied Petroleum Gas (Propane) / Propane Vehicles, &#39;HY&#39; for Hydrogen / Fuel Cell Electric Vehicles, &#39;ELEC&#39; for All-Electric Vehicles (EVs), &#39;PHEV&#39; for Plug-In Hybrid Electric Vehicles (PHEVs), &#39;HEV&#39; for Hybrid Electric Vehicles (HEVs), &#39;NEVS&#39; for Neighborhood Electric Vehicles (NEVs), &#39;RD&#39; for Renewable Diesel, &#39;AFTMKTCONV&#39; for Aftermarket Conversions, &#39;EFFEC&#39; for Fuel Economy / Efficiency, &#39;IR&#39; for Idle Reduction, &#39;AUTONOMOUS&#39; for Connected and Autonomous Vehicles, and &#39;OTHER&#39; for Other.
    :type technology: str
    :param incentive_type: Search by the incentive type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: &#39;GNT&#39; for Grants, &#39;TAX&#39; for Tax Incentives, &#39;LOANS&#39; for Loans and Leases, &#39;RBATE&#39; for Rebates, &#39;EXEM&#39; for Exemptions, &#39;TOU&#39; for Time-of-Use Rate, and &#39;OTHER&#39; for Other.
    :type incentive_type: str
    :param regulation_type: Search by the regulation type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: &#39;REQ&#39; for Acquisition / Fuel Use, &#39;DREST&#39; for Driving / Idling, &#39;REGIS&#39; for Registration / Licensing, &#39;EVFEE&#39; for EV Registration Fee, &#39;FUEL&#39; for Fuel Taxes, &#39;STD&#39; for Fuel Production / Quality, &#39;RFS&#39; for Renewable Fuel Standard / Mandate, &#39;AIRQEMISSIONS&#39; for Air Quality / Emissions, &#39;CCEINIT&#39; for Climate Change / Energy Initiatives, &#39;UTILITY&#39; for Utility Definition, &#39;BUILD&#39; for Building Codes, &#39;RTC&#39; for Right-to-Charge, and &#39;OTHER&#39; for Other.
    :type regulation_type: str
    :param user_type: Search by the user type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: &#39;FLEET&#39; for Commercial, &#39;GOV&#39; for Government Entity, &#39;TRIBAL&#39; for Tribal Government, &#39;IND&#39; for Personal Vehicle Owner or Driver, &#39;STATION&#39; for Alternative Fuel Infrastructure Operator, &#39;AFP&#39; for Alternative Fuel Producer, &#39;PURCH&#39; for Alternative Fuel Purchaser, &#39;MAN&#39; for Alternative Fuel Vehicle (AFV) Manufacturer or Retrofitter, &#39;MUD&#39; for Multi-Unit Dwelling, &#39;TRANS&#39; for Transit, and &#39;OTHER&#39; for Other.
    :type user_type: str
    :param poc: Include points of contacts in the return value.
    :type poc: bool
    :param recent: Return only recently added or updated laws and incentives
    :type recent: bool
    :param expired: The &#39;true&#39; value returns only expired, repealed, or archived laws and incentives. The default &#39;false&#39; value returns only current laws and incentives.
    :type expired: bool
    :param law_type: Search by the law type. A single type, or a comma-separate list of multiple types, may be given. Values are as follows: &#39;STATEINC&#39; for State Incentives, &#39;UPINC &#39; for Utility/Private Incentives, &#39;LAWREG&#39; for Laws and Regulations, &#39;INC&#39; for Incentives, &#39;PROG&#39; for Programs, &#39;LUP&#39; for Last Updated, &#39;OVIEW&#39; for Overview, and &#39;HILITE&#39; for Highlights.
    :type law_type: str
    :param keyword: Search laws by keyword in title or text.
    :type keyword: str
    :param local: Show only local examples of laws and incentives.
    :type local: bool

    """
    return web.Response(status=200)


async def transportation_incentives_laws_categories(request: web.Request, output_format, api_key, type=None) -> web.Response:
    """Return the law categories for a given category type.

    

    :param output_format: Response format
    :type output_format: str
    :param api_key: API Key
    :type api_key: str
    :param type: Search by the category type.
    :type type: str

    """
    return web.Response(status=200)


async def transportation_incentives_laws_id(request: web.Request, output_format, api_key, id, poc=None, expired=None) -> web.Response:
    """Fetch the details of a specific law given the law&#39;s ID.

    

    :param output_format: Response format
    :type output_format: str
    :param api_key: API Key
    :type api_key: str
    :param id: The id of the law that you are searching
    :type id: int
    :param poc: Include points of contacts in the return value.
    :type poc: bool
    :param expired: The &#39;true&#39; value returns a record no matter its status (current, expired, archived, or repealed). The default &#39;false&#39; value returns only current laws and incentives.
    :type expired: bool

    """
    return web.Response(status=200)


async def transportation_incentives_laws_pocs(request: web.Request, output_format, api_key, jurisdiction) -> web.Response:
    """Get the points of contact for a given jurisdiction.

    

    :param output_format: Response format
    :type output_format: str
    :param api_key: API Key
    :type api_key: str
    :param jurisdiction: Return the points of contact for the given Jurisdiction. Jurisdiction must be given as a two character state code (eg, &#39;CO&#39; for Colorado). A single jurisdiction, or a comma-separate list of multiple jurisdiction, may be given.  Use the code &#39;US&#39; for federal laws and the code &#39;DC&#39; for Washington D.C.
    :type jurisdiction: str

    """
    return web.Response(status=200)

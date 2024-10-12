from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.pay_statement_details import PayStatementDetails
from openapi_server.models.pay_statement_summary import PayStatementSummary
from openapi_server import util


async def gets_employee_pay_statement_detail_data_based_on_the_specified_year(request: web.Request, company_id, employee_id, year, pagesize=None, pagenumber=None, includetotalcount=None, codegroup=None) -> web.Response:
    """Get employee pay statement details data for the specified year.

    Get pay statement details API will return employee pay statement details data currently available in Web Pay for the specified year.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param year: The year for which to retrieve pay statement data
    :type year: str
    :param pagesize: Number of records per page. Default value is 25.
    :type pagesize: int
    :param pagenumber: Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0.
    :type pagenumber: int
    :param includetotalcount: Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true.
    :type includetotalcount: bool
    :param codegroup: Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
    :type codegroup: str

    """
    return web.Response(status=200)


async def gets_employee_pay_statement_detail_data_based_on_the_specified_year_and_check_date(request: web.Request, company_id, employee_id, year, check_date, pagesize=None, pagenumber=None, includetotalcount=None, codegroup=None) -> web.Response:
    """Get employee pay statement details data for the specified year and check date.

    Get pay statement details API will return employee pay statement detail data currently available in Web Pay for the specified year and check date.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param year: The year for which to retrieve pay statement data
    :type year: str
    :param check_date: The check date for which to retrieve pay statement data
    :type check_date: str
    :param pagesize: Number of records per page. Default value is 25.
    :type pagesize: int
    :param pagenumber: Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0.
    :type pagenumber: int
    :param includetotalcount: Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true.
    :type includetotalcount: bool
    :param codegroup: Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
    :type codegroup: str

    """
    return web.Response(status=200)


async def gets_employee_pay_statement_summary_data_based_on_the_specified_year(request: web.Request, company_id, employee_id, year, pagesize=None, pagenumber=None, includetotalcount=None, codegroup=None) -> web.Response:
    """Get employee pay statement summary data for the specified year.

    Get pay statement summary API will return employee pay statement summary data currently available in Web Pay for the specified year.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param year: The year for which to retrieve pay statement data
    :type year: str
    :param pagesize: Number of records per page. Default value is 25.
    :type pagesize: int
    :param pagenumber: Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0.
    :type pagenumber: int
    :param includetotalcount: Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true.
    :type includetotalcount: bool
    :param codegroup: Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
    :type codegroup: str

    """
    return web.Response(status=200)


async def gets_employee_pay_statement_summary_data_based_on_the_specified_year_and_check_date(request: web.Request, company_id, employee_id, year, check_date, pagesize=None, pagenumber=None, includetotalcount=None, codegroup=None) -> web.Response:
    """Get employee pay statement summary data for the specified year and check date.

    Get pay statement summary API will return employee pay statement summary data currently available in Web Pay for the specified year and check date.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param year: The year for which to retrieve pay statement data
    :type year: str
    :param check_date: The check date for which to retrieve pay statement data
    :type check_date: str
    :param pagesize: Number of records per page. Default value is 25.
    :type pagesize: int
    :param pagenumber: Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0.
    :type pagenumber: int
    :param includetotalcount: Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true.
    :type includetotalcount: bool
    :param codegroup: Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
    :type codegroup: str

    """
    return web.Response(status=200)

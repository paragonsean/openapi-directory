from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def security_advisories_cvrf_advisory_advisory_id_get(request: web.Request, advisory_id) -> web.Response:
    """security_advisories_cvrf_advisory_advisory_id_get

    Used to obtain an advisory in CVRF format for a given advisory ID &#x60;advisory_id&#x60; (i.e., cisco-sa-20150819-pcp) 

    :param advisory_id: advisory ID
    :type advisory_id: str

    """
    return web.Response(status=200)


async def security_advisories_cvrf_all_get(request: web.Request, ) -> web.Response:
    """security_advisories_cvrf_all_get

    Used to obtain all advisories in Common Vulnerability Reporting Format (CVRF). For more information about CVRF go to https://communities.cisco.com/docs/DOC-63156 . By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/cvrf/all.xml 


    """
    return web.Response(status=200)


async def security_advisories_cvrf_cve_cve_id_get(request: web.Request, cve_id) -> web.Response:
    """security_advisories_cvrf_cve_cve_id_get

    Used to obtain an advisory in CVRF format for a given Common Vulnerability Enumerator (CVE). The &#x60;cve_id&#x60; format is CVE-YYYY-NNNN. For more information about CVE visit http://cve.mitre.org/ 

    :param cve_id: CVE Identifier (i.e., CVE-YYYY-NNNN)
    :type cve_id: str

    """
    return web.Response(status=200)


async def security_advisories_cvrf_latest_number_get(request: web.Request, number) -> web.Response:
    """security_advisories_cvrf_latest_number_get

    Used to obtain all the latest security advisories in CVRF format given an absolute number. For instance, the latest 10 or latest 5. 

    :param number: An absolute number to obtain the latest security advisories.
    :type number: int

    """
    return web.Response(status=200)


async def security_advisories_cvrf_product_get(request: web.Request, product) -> web.Response:
    """security_advisories_cvrf_product_get

    Used to obtain all the advisories that affects the given product name. 

    :param product: An product name to obtain security advisories that matches given product name.
    :type product: str

    """
    return web.Response(status=200)


async def security_advisories_cvrf_severity_severity_firstpublished_get(request: web.Request, severity, start_date, end_date) -> web.Response:
    """security_advisories_cvrf_severity_severity_firstpublished_get

    Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format and additionally filter based of firstpublished start date and enddate 

    :param severity: Used to obtain all advisories that have a security impact rating of critical
    :type severity: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def security_advisories_cvrf_severity_severity_get(request: web.Request, severity) -> web.Response:
    """security_advisories_cvrf_severity_severity_get

    Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format. 

    :param severity: Critical, High, Medium, Low
    :type severity: str

    """
    return web.Response(status=200)


async def security_advisories_cvrf_severity_severity_lastpublished_get(request: web.Request, severity, start_date, end_date) -> web.Response:
    """security_advisories_cvrf_severity_severity_lastpublished_get

    Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in CVRF format. 

    :param severity: Used to obtain all advisories that have a security impact rating of critical
    :type severity: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def security_advisories_cvrf_year_year_get(request: web.Request, year) -> web.Response:
    """security_advisories_cvrf_year_year_get

    Used to obtain all security advisories that have were orginally published in a specific year &#x60;YYYY&#x60;. 

    :param year: The four digit year.
    :type year: str

    """
    return web.Response(status=200)


async def security_advisories_ios_get(request: web.Request, version) -> web.Response:
    """security_advisories_ios_get

    Used to obtain all advisories that affects the given ios version 

    :param version: IOS version to obtain security advisories
    :type version: str

    """
    return web.Response(status=200)


async def security_advisories_iosxe_get(request: web.Request, version) -> web.Response:
    """security_advisories_iosxe_get

    Used to obtain all advisories that affects the given ios version 

    :param version: IOS version to obtain security advisories
    :type version: str

    """
    return web.Response(status=200)


async def security_advisories_oval_advisory_advisory_id_get(request: web.Request, advisory_id) -> web.Response:
    """security_advisories_oval_advisory_advisory_id_get

    Used to obtain OVAL definitions for a given advisory ID &#x60;advisory_id&#x60; (i.e., cisco-sa-20150819-pcp) 

    :param advisory_id: advisory ID
    :type advisory_id: str

    """
    return web.Response(status=200)


async def security_advisories_oval_all_get(request: web.Request, ) -> web.Response:
    """security_advisories_oval_all_get

    Used to obtain all Open Vulnerability and Assessment Language (OVAL) definitions available for Cisco security vulnerabilities. For more information about OVAL go to https://communities.cisco.com/docs/DOC-63158 . By default the output is in JSON. To obtain the output in XML use the .xml extension. For example, /advisories/oval/all.xml 


    """
    return web.Response(status=200)


async def security_advisories_oval_cve_cve_id_get(request: web.Request, cve_id) -> web.Response:
    """security_advisories_oval_cve_cve_id_get

    Used to obtain OVAL definitions for a given CVE Identifier. The &#x60;cve_id&#x60; format is CVE-YYYY-NNNN. 

    :param cve_id: CVE Identifier (i.e., CVE-YYYY-NNNN)
    :type cve_id: str

    """
    return web.Response(status=200)


async def security_advisories_oval_latest_number_get(request: web.Request, number) -> web.Response:
    """security_advisories_oval_latest_number_get

    Used to obtain all the latest OVAL definitions given an absolute number. For instance, the latest 10 or latest 5. 

    :param number: The latest OVAL definitions (absolute number).
    :type number: int

    """
    return web.Response(status=200)


async def security_advisories_oval_product_get(request: web.Request, product) -> web.Response:
    """security_advisories_oval_product_get

    Used to obtain all the oval advisories that affects the given product name. 

    :param product: An product name to obtain security advisories that matches given product name.
    :type product: str

    """
    return web.Response(status=200)


async def security_advisories_oval_severity_severity_firstpublished_get(request: web.Request, severity, start_date, end_date) -> web.Response:
    """security_advisories_oval_severity_severity_firstpublished_get

    Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in OVAL format. 

    :param severity: Critical, High, Medium, Low
    :type severity: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def security_advisories_oval_severity_severity_get(request: web.Request, severity) -> web.Response:
    """security_advisories_oval_severity_severity_get

    Used to obtain all OVAL definitions for a given security impact rating (critical, high, medium, or low). 

    :param severity: Used to obtain all OVAL definitions for advisories that have a security impact rating of critical
    :type severity: str

    """
    return web.Response(status=200)


async def security_advisories_oval_severity_severity_lastpublished_get(request: web.Request, severity, start_date, end_date) -> web.Response:
    """security_advisories_oval_severity_severity_lastpublished_get

    Used to obtain all security advisories for a given security impact rating (critical, high, medium, or low) in OVAL format. 

    :param severity: Critical, High, Medium, Low
    :type severity: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)

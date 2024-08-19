from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_latest_product_files_by_product_id_and_time(request: web.Request, short_name, year=None, hierarchy=None) -> web.Response:
    """Returns products along with their latest files by short names.

    Use this GET to search for latest released bulk data products by their short names and release year. The return response will include the latest files within the year specified.  An error message will be returned if product(s) cannot be found for the year specified

    :param short_name: Short name of the product, for example, \&quot;PTGRSP\&quot;
    :type short_name: str
    :param year: Year of the product files  needed, for example, 2001.
    :type year: int
    :param hierarchy: Boolean flag (possible values: true and false) to indicate if product hierarchy needs to be return in the response. By default it doesn&#39;t return the hierarchy in the response.
    :type hierarchy: str

    """
    return web.Response(status=200)


async def get_populart_products(request: web.Request, ) -> web.Response:
    """Returns popular products along with latest files.

    Use this GET to retrieve these bulk data files by their popularity. The response includes product fields such as title, description, frequency, and level.


    """
    return web.Response(status=200)


async def get_product_sub_tree(request: web.Request, short_name) -> web.Response:
    """Returns products&#39; hierarchical subtree.

    Use this GET to search for bulk data products by their short names. This works almost like products/tree GET, the difference is that it returns subtree data starting from a particular tree node (i.e. the GET returns all children if parent short name is entered). If a product cannot be found by its short name (has to be exact match and is not case sensitive), then an error message will appear in response body.

    :param short_name: Short name of the product, for example, \&quot;PTISSD\&quot;
    :type short_name: str

    """
    return web.Response(status=200)


async def get_products_by_name(request: web.Request, product_name, from_year=None, to_year=None, from_month=None, to_month=None, from_day=None, to_day=None, hierarchy=None, max_files=None) -> web.Response:
    """Returns files associated with products (of level PRODUCT) based on their full or partial names.

    Use this GET to search for bulk data services by product name or description. An error message will be returned if the product cannot be found by name. Note that product name is not case sensitive. You can enter full or partial name of an existing product to receive bulk data services. Default values for field names are as follows - if both years are not defined, toYear will be set equal to current year, fromYear will be set equal to previous year - if fromYear is defined, toYear will be set equal to fromYear+1 - if fromMonth not defined, current month will be used - if toMonth not defined, it will be set equal to fromMonth - if fromDay is not defined, it will be set equal to current day (today) - if toDay is not defined, it will be set to the last day of toMonth/toYear

    :param product_name: Name of the product, for example, \&quot;Trademark\&quot;
    :type product_name: str
    :param from_year: Year from when the product files are needed, for example, 1999.
    :type from_year: int
    :param to_year: Year until when the product files are needed, for example, 2000.
    :type to_year: int
    :param from_month: Month from when the product files are needed, for example, 01.
    :type from_month: int
    :param to_month: Month until when the product files are needed, for example, 12.
    :type to_month: int
    :param from_day: Day from when the product files are needed, for example, 01.
    :type from_day: int
    :param to_day: Day until when the product files are needed, for example, 31.
    :type to_day: int
    :param hierarchy: Boolean flag to indicate if product hierarchy needs to be return in the response. By default it doesn&#39;t return the hierarchy in the response.
    :type hierarchy: str
    :param max_files: Max. number of files to retrieve, per product. Set value to -1 to get all files
    :type max_files: int

    """
    return web.Response(status=200)


async def get_products_by_short_name(request: web.Request, short_name, from_year=None, to_year=None, from_month=None, to_month=None, from_day=None, to_day=None, from_date=None, to_date=None, hierarchy=None) -> web.Response:
    """Returns products along with their associated files by short names.

    Use this GET to search for bulk data products by their short names and description. Note that \&quot;From\&quot; and \&quot;To\&quot; dates can be inputted separately as year/month/day values or as a single date string in format \&quot;YYYY-MM-DD\&quot;. If all values are entered, single date strings have a higher priority For the list of default values rules, see GET /products/byname/{productName} above

    :param short_name: Short name  of the product, for example, \&quot;PTGRSP\&quot;
    :type short_name: str
    :param from_year: Year from when the product files are needed, for example, 1999.
    :type from_year: int
    :param to_year: Year until when the product files are needed, for example, 2000.
    :type to_year: int
    :param from_month: Month from when the product files are needed, for example, 01.
    :type from_month: int
    :param to_month: Month until when the product files are needed, for example, 12.
    :type to_month: int
    :param from_day: Day from when the product files are needed, for example, 01.
    :type from_day: int
    :param to_day: Day until when the product files are needed, for example, 31.
    :type to_day: int
    :param from_date: Year from when the product files are needed, for example, 1999-01-01.
    :type from_date: str
    :param to_date: Year until when the product files are needed, for example, 2001-12-31.
    :type to_date: str
    :param hierarchy: Boolean flag (possible values: true and false) to indicate if product hierarchy needs to be return in the response. By default it doesn&#39;t return the hierarchy in the response.
    :type hierarchy: str

    """
    return web.Response(status=200)


async def get_products_tree(request: web.Request, ) -> web.Response:
    """Returns products&#39; hierarchical tree.

    Use this GET to retrieve short name and parent/child relationships for bulk data products. Short names are unique IDs of the products and should be used in other GETs where {shortName} parameter is required Use this GET to perform initial exploration of the existing products hierarchy Short names are unique IDs of the products and should be used in other GETs where {shortName} parameter is required


    """
    return web.Response(status=200)


async def get_products_with_latest_product_files(request: web.Request, ) -> web.Response:
    """Returns all products with Latest Files.

    Use this GET to retrieve latest released bulk data products. Note that there is one file per product. The response includes product fields such as title, description, frequency, and level.


    """
    return web.Response(status=200)

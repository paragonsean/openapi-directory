from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_lists_best_sellers_history_json200_response import GETListsBestSellersHistoryJson200Response
from openapi_server.models.get_lists_date_list_json200_response import GETListsDateListJson200Response
from openapi_server.models.get_lists_format200_response import GETListsFormat200Response
from openapi_server.models.get_lists_names_format200_response import GETListsNamesFormat200Response
from openapi_server.models.get_lists_overview_format200_response import GETListsOverviewFormat200Response
from openapi_server.models.get_reviews_format200_response import GETReviewsFormat200Response
from openapi_server import util


async def g_et_lists_best_sellers_history_json(request: web.Request, age_group=None, author=None, contributor=None, isbn=None, price=None, publisher=None, title=None) -> web.Response:
    """Best Seller History List

    

    :param age_group: The target age group for the best seller.
    :type age_group: str
    :param author: The author of the best seller. The author field does not include additional contributors (see Data Structure for more details about the author and contributor fields).  When searching the author field, you can specify any combination of first, middle and last names.  When sort-by is set to author, the results will be sorted by author&#39;s first name. 
    :type author: str
    :param contributor: The author of the best seller, as well as other contributors such as the illustrator (to search or sort by author name only, use author instead).  When searching, you can specify any combination of first, middle and last names of any of the contributors.  When sort-by is set to contributor, the results will be sorted by the first name of the first contributor listed. 
    :type contributor: str
    :param isbn: International Standard Book Number, 10 or 13 digits  A best seller may have both 10-digit and 13-digit ISBNs, and may have multiple ISBNs of each type. To search on multiple ISBNs, separate the ISBNs with semicolons (example: 9780446579933;0061374229).
    :type isbn: str
    :param price: The publisher&#39;s list price of the best seller, including decimal point
    :type price: str
    :param publisher: The standardized name of the publisher
    :type publisher: str
    :param title: The title of the best seller  When searching, you can specify a portion of a title or a full title.
    :type title: str

    """
    return web.Response(status=200)


async def g_et_lists_date_list_json(request: web.Request, _date, list, isbn=None, list_name=None, published_date=None, bestsellers_date=None, weeks_on_list=None, rank=None, rank_last_week=None, offset=None, sort_order=None) -> web.Response:
    """Best Seller List by Date

    

    :param _date: 
    :type _date: str
    :param list: Name of the Best Sellers List. You can get the full list from /lists/names.json
    :type list: str
    :param isbn: International Standard Book Number, 10 or 13 digits
    :type isbn: int
    :param list_name: The name of the Times best-seller list. To get valid values, use a list names request.  Be sure to replace spaces with hyphens (e.g., e-book-fiction or hardcover-fiction, not E-Book Fiction or Hardcover Fiction). (The parameter is not case sensitive.)
    :type list_name: str
    :param published_date: YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date)
    :type published_date: str
    :param bestsellers_date: YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best-seller lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29).
    :type bestsellers_date: str
    :param weeks_on_list: The number of weeks that the best seller has been on list-name, as of bestsellers-date
    :type weeks_on_list: int
    :param rank: The rank of the best seller on list-name as of bestsellers-date
    :type rank: str
    :param rank_last_week: The rank of the best seller on list-name one week prior to bestsellers-date
    :type rank_last_week: int
    :param offset: Sets the starting point of the result set
    :type offset: int
    :param sort_order: The default is ASC (ascending). The sort-order parameter is used with the sort-by parameter — for details, see each request type.
    :type sort_order: str

    """
    published_date = util.deserialize_datetime(published_date)
    return web.Response(status=200)


async def g_et_lists_format(request: web.Request, format, list=None, weeks_on_list=None, bestsellers_date=None, _date=None, isbn=None, published_date=None, rank=None, rank_last_week=None, offset=None, sort_order=None) -> web.Response:
    """Best Seller List

    

    :param format: 
    :type format: str
    :param list: The name of the Times best-seller list. To get valid values, use a list names request.  Be sure to replace spaces with hyphens (e.g., e-book-fiction or hardcover-fiction, not E-Book Fiction or Hardcover Fiction). (The parameter is not case sensitive.)
    :type list: str
    :param weeks_on_list: The number of weeks that the best seller has been on list-name, as of bestsellers-date
    :type weeks_on_list: int
    :param bestsellers_date: YYYY-MM-DD  The week-ending date for the sales reflected on list-name. Times best-seller lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29).
    :type bestsellers_date: str
    :param _date: YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date)
    :type _date: str
    :param isbn: International Standard Book Number, 10 or 13 digits
    :type isbn: str
    :param published_date: YYYY-MM-DD  The date the best-seller list was published on NYTimes.com (compare bestsellers-date)
    :type published_date: str
    :param rank: The rank of the best seller on list-name as of bestsellers-date
    :type rank: int
    :param rank_last_week: The rank of the best seller on list-name one week prior to bestsellers-date
    :type rank_last_week: int
    :param offset: Sets the starting point of the result set
    :type offset: int
    :param sort_order: Sets the sort order of the result set
    :type sort_order: str

    """
    bestsellers_date = util.deserialize_datetime(bestsellers_date)
    return web.Response(status=200)


async def g_et_lists_names_format(request: web.Request, format, api_key=None) -> web.Response:
    """Best Seller List Names

    

    :param format: 
    :type format: str
    :param api_key: 
    :type api_key: str

    """
    return web.Response(status=200)


async def g_et_lists_overview_format(request: web.Request, format, published_date=None, api_key=None) -> web.Response:
    """Best Seller List Overview

    

    :param format: 
    :type format: str
    :param published_date: The best-seller list publication date. YYYY-MM-DD  You do not have to specify the exact date the list was published. The service will search forward (into the future) for the closest publication date to the date you specify. For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26.  If you do not include a published_date, the current week&#39;s best-sellers lists will be returned.
    :type published_date: str
    :param api_key: 
    :type api_key: str

    """
    return web.Response(status=200)


async def g_et_reviews_format(request: web.Request, format, isbn=None, title=None, author=None, api_key=None) -> web.Response:
    """Reviews

    

    :param format: 
    :type format: str
    :param isbn: Searching by ISBN is the recommended method. You can enter 10- or 13-digit ISBNs.
    :type isbn: int
    :param title: You’ll need to enter the full title of the book. Spaces in the title will be converted into the characters %20.
    :type title: str
    :param author: You’ll need to enter the author’s first and last name, separated by a space. This space will be converted into the characters %20.
    :type author: str
    :param api_key: 
    :type api_key: str

    """
    return web.Response(status=200)

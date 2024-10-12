from typing import List, Dict
from aiohttp import web

from openapi_server.models.articlesearch_json_get200_response import ArticlesearchJsonGet200Response
from openapi_server import util


async def articlesearch_json_get(request: web.Request, q=None, fq=None, begin_date=None, end_date=None, sort=None, fl=None, hl=None, page=None, facet_field=None, facet_filter=None) -> web.Response:
    """Article Search

    Article Search requests use the following URI structure: 

    :param q: Search query term. Search is performed on the article body, headline and byline. 
    :type q: str
    :param fq: \&quot;Filtered search query using standard Lucene syntax.   The filter query can be specified with or without a limiting field: label.   See Filtering Your Search for more information about filtering.\&quot; 
    :type fq: str
    :param begin_date: \&quot;Format: YYYYMMDD   Restricts responses to results with publication dates of the date specified or later.\&quot; 
    :type begin_date: str
    :param end_date: \&quot;Format: YYYYMMDD   Restricts responses to results with publication dates of the date specified or earlier.\&quot; 
    :type end_date: str
    :param sort: \&quot;By default, search results are sorted by their relevance to the query term (q). Use the sort parameter to sort by pub_date.\&quot; 
    :type sort: str
    :param fl: \&quot;Comma-delimited list of fields (no limit)    Limits the fields returned in your search results. By default (unless you include an fl list in your request), the following fields are returned:       web_url      snippet      lead_paragraph      abstract      print_page      blog      source      multimedia      headline      keywords      pub_date      document_type      news_desk      byline      type_of_material      _id      word_count\&quot; 
    :type fl: str
    :param hl: Enables highlighting in search results. When set to true, the query term (q) is highlighted in the headline and lead_paragraph fields.  Note: If highlighting is enabled, snippet will be returned even if it is not specified in your fl list.\&quot; 
    :type hl: bool
    :param page: \&quot;The value of page corresponds to a set of 10 results (it does not indicate the starting number of the result set). For example, page&#x3D;0 corresponds to records 0-9. To return records 10-19, set page to 1, not 10.\&quot; 
    :type page: int
    :param facet_field: Comma-delimited list of facets  Specifies the sets of facet values to include in the facets array at the end of response, which collects the facet values from all the search results. By default no facet fields will be returned. Below is the list of valid facets:  section_name  document_type  type_of_material  source  day_of_week  To learn more about using facets, see Using Facets. 
    :type facet_field: str
    :param facet_filter: When set to true, facet counts will respect any applied filters (fq, date range, etc.) in addition to the main query term. To filter facet counts, specifying at least one facet_field is required. To learn more about using facets, see Using Facets. 
    :type facet_filter: bool

    """
    return web.Response(status=200)

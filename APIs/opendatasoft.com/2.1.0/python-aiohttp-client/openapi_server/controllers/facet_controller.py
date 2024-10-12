from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_records_facets200_response import GetRecordsFacets200Response
from openapi_server import util


async def get_datasets_facets_0(request: web.Request, source, facet=None, refine=None, exclude=None, where=None, search=None, timezone=None) -> web.Response:
    """get_datasets_facets_0

    Enumerate facets values for datasets and return a list of values for each facet. Can be used to implement guided navigation in large result sets.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#enumerating-facets-values) for more details. 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param search: An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    :type search: List[str]
    :param timezone: Set timezone for datetime fields
    :type timezone: str

    """
    return web.Response(status=200)


async def get_records_facets_0(request: web.Request, source, dataset_id, where=None, facet=None, refine=None, exclude=None, search=None, timezone=None) -> web.Response:
    """get_records_facets_0

    Enumerate facets values for records and return a list of values for each facet. Can be used to implement guided navigation in large result sets.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#enumerating-facets-values) for more details. 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]
    :param search: An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    :type search: List[str]
    :param timezone: Set timezone for datetime fields
    :type timezone: str

    """
    return web.Response(status=200)

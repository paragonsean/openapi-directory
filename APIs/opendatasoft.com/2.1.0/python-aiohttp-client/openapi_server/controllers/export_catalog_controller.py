from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def export_datasets_csv(request: web.Request, source, where=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, timezone=None, include_app_metas=None, delimiter=None) -> web.Response:
    """export_datasets_csv

    Export catalog (source) in CSV format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param limit: Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    :type limit: int
    :param offset: Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    :type offset: int
    :param search: An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    :type search: List[str]
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]
    :param timezone: Set timezone for datetime fields
    :type timezone: str
    :param include_app_metas: Explicitely request application metas for each datasets. 
    :type include_app_metas: bool
    :param delimiter: Provide a different delimiter (default &#39;,&#39;).
    :type delimiter: str

    """
    return web.Response(status=200)


async def export_datasets_json(request: web.Request, source, where=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, pretty=None, timezone=None, include_app_metas=None) -> web.Response:
    """export_datasets_json

    Export catalog (source) in JSON format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param limit: Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    :type limit: int
    :param offset: Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    :type offset: int
    :param search: An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    :type search: List[str]
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]
    :param pretty: Activate pretty print
    :type pretty: bool
    :param timezone: Set timezone for datetime fields
    :type timezone: str
    :param include_app_metas: Explicitely request application metas for each datasets. 
    :type include_app_metas: bool

    """
    return web.Response(status=200)


async def export_datasets_rdf(request: web.Request, source, where=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, timezone=None, include_app_metas=None) -> web.Response:
    """export_datasets_rdf

    Export catalog (source) in RDF/XML format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param limit: Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    :type limit: int
    :param offset: Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    :type offset: int
    :param search: An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    :type search: List[str]
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]
    :param timezone: Set timezone for datetime fields
    :type timezone: str
    :param include_app_metas: Explicitely request application metas for each datasets. 
    :type include_app_metas: bool

    """
    return web.Response(status=200)


async def export_datasets_rss(request: web.Request, source, where=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, timezone=None, include_app_metas=None) -> web.Response:
    """export_datasets_rss

    Export catalog (source) in RSS format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param limit: Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    :type limit: int
    :param offset: Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    :type offset: int
    :param search: An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    :type search: List[str]
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]
    :param timezone: Set timezone for datetime fields
    :type timezone: str
    :param include_app_metas: Explicitely request application metas for each datasets. 
    :type include_app_metas: bool

    """
    return web.Response(status=200)


async def export_datasets_ttl(request: web.Request, source, where=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, timezone=None, include_app_metas=None) -> web.Response:
    """export_datasets_ttl

    Export catalog (source) in TTL (turtle/rdf) format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param limit: Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    :type limit: int
    :param offset: Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    :type offset: int
    :param search: An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    :type search: List[str]
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]
    :param timezone: Set timezone for datetime fields
    :type timezone: str
    :param include_app_metas: Explicitely request application metas for each datasets. 
    :type include_app_metas: bool

    """
    return web.Response(status=200)


async def export_datasets_xls(request: web.Request, source, where=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, timezone=None, include_app_metas=None) -> web.Response:
    """export_datasets_xls

    Export catalog (source) in XLS (Excel) format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param limit: Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    :type limit: int
    :param offset: Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    :type offset: int
    :param search: An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    :type search: List[str]
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]
    :param timezone: Set timezone for datetime fields
    :type timezone: str
    :param include_app_metas: Explicitely request application metas for each datasets. 
    :type include_app_metas: bool

    """
    return web.Response(status=200)

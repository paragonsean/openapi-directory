from typing import List, Dict
from aiohttp import web

from openapi_server.models.aggregate_datasets200_response import AggregateDatasets200Response
from openapi_server import util


async def aggregate_datasets_0(request: web.Request, source, select=None, where=None, group_by=None, order_by=None, limit=None, offset=None, facet=None, refine=None, exclude=None) -> web.Response:
    """aggregate_datasets_0

    **Deprecated, use &#x60;/datasets&#x60; instead.** 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param group_by: A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date It is possible to specify a custom name with the &#39;as name&#39; notation. For instance: group_by&#x3D;&#39;city_field as city&#39;. 
    :type group_by: str
    :param order_by: A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60; 
    :type order_by: List[str]
    :param limit: Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    :type limit: int
    :param offset: Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    :type offset: int
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def aggregate_records_0(request: web.Request, source, dataset_id, select=None, where=None, group_by=None, order_by=None, limit=None, offset=None, facet=None, refine=None, exclude=None) -> web.Response:
    """aggregate_records_0

    **Deprecated, use &#x60;/records&#x60; instead.** 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param group_by: A group by expression defines a grouping function for an aggregation. It can be:  - a field name: group result by each value of this field  - a range function: group result by range  - a date function: group result by date It is possible to specify a custom name with the &#39;as name&#39; notation. For instance: group_by&#x3D;&#39;city_field as city&#39;. 
    :type group_by: str
    :param order_by: A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60; 
    :type order_by: List[str]
    :param limit: Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    :type limit: int
    :param offset: Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    :type offset: int
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]

    """
    return web.Response(status=200)

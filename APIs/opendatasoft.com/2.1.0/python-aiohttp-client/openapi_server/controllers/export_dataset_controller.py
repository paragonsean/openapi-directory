from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def export_records_csv(request: web.Request, source, dataset_id, select=None, where=None, sort=None, order_by=None, limit=None, offset=None, facet=None, refine=None, exclude=None, timezone=None, delimiter=None) -> web.Response:
    """export_records_csv

    Export dataset in CSV format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param sort: **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
    :type sort: List[str]
    :param order_by: A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60; 
    :type order_by: List[str]
    :param limit: Number of items to return in export.  Use -1 (default) to retrieve all records 
    :type limit: int
    :param offset: Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    :type offset: int
    :param facet: A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    :type facet: List[str]
    :param refine: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    :type refine: List[str]
    :param exclude: An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    :type exclude: List[str]
    :param timezone: Set timezone for datetime fields
    :type timezone: str
    :param delimiter: Provide a different delimiter (default &#39;,&#39;).
    :type delimiter: str

    """
    return web.Response(status=200)


async def export_records_geojson(request: web.Request, source, dataset_id, select=None, where=None, sort=None, order_by=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, timezone=None, pretty=None) -> web.Response:
    """export_records_geojson

    Export dataset in GEOJSON format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param sort: **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
    :type sort: List[str]
    :param order_by: A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60; 
    :type order_by: List[str]
    :param limit: Number of items to return in export.  Use -1 (default) to retrieve all records 
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
    :param pretty: Activate pretty print
    :type pretty: bool

    """
    return web.Response(status=200)


async def export_records_ical(request: web.Request, source, dataset_id, select=None, where=None, sort=None, order_by=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, timezone=None) -> web.Response:
    """export_records_ical

    Export dataset in ICAL format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param sort: **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
    :type sort: List[str]
    :param order_by: A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60; 
    :type order_by: List[str]
    :param limit: Number of items to return in export.  Use -1 (default) to retrieve all records 
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

    """
    return web.Response(status=200)


async def export_records_json(request: web.Request, source, dataset_id, select=None, where=None, sort=None, order_by=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, pretty=None, timezone=None) -> web.Response:
    """export_records_json

    Export dataset in JSON format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param sort: **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
    :type sort: List[str]
    :param order_by: A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60; 
    :type order_by: List[str]
    :param limit: Number of items to return in export.  Use -1 (default) to retrieve all records 
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

    """
    return web.Response(status=200)


async def export_records_ov2(request: web.Request, source, dataset_id, select=None, where=None, sort=None, order_by=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, timezone=None) -> web.Response:
    """export_records_ov2

    Export dataset in OV2 format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param sort: **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
    :type sort: List[str]
    :param order_by: A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60; 
    :type order_by: List[str]
    :param limit: Number of items to return in export.  Use -1 (default) to retrieve all records 
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

    """
    return web.Response(status=200)


async def export_records_shp(request: web.Request, source, dataset_id, select=None, where=None, sort=None, order_by=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, timezone=None) -> web.Response:
    """export_records_shp

    Export dataset in Esri shapefile (shp) format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param sort: **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
    :type sort: List[str]
    :param order_by: A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60; 
    :type order_by: List[str]
    :param limit: Number of items to return in export.  Use -1 (default) to retrieve all records 
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

    """
    return web.Response(status=200)


async def export_records_xls(request: web.Request, source, dataset_id, select=None, where=None, sort=None, order_by=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, timezone=None) -> web.Response:
    """export_records_xls

    Export dataset in XLS (Excel) format 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param where: An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    :type where: List[str]
    :param sort: **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
    :type sort: List[str]
    :param order_by: A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60; 
    :type order_by: List[str]
    :param limit: Number of items to return in export.  Use -1 (default) to retrieve all records 
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

    """
    return web.Response(status=200)

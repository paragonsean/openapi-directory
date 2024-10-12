from typing import List, Dict
from aiohttp import web

from openapi_server.models.aggregate_datasets200_response import AggregateDatasets200Response
from openapi_server.models.get_dataset_attachements200_response import GetDatasetAttachements200Response
from openapi_server.models.get_dataset_reuse200_response import GetDatasetReuse200Response
from openapi_server.models.get_dataset_reuses200_response import GetDatasetReuses200Response
from openapi_server.models.get_dataset_snapshots200_response import GetDatasetSnapshots200Response
from openapi_server.models.get_datasets200_response_datasets_inner import GetDatasets200ResponseDatasetsInner
from openapi_server.models.get_records200_response import GetRecords200Response
from openapi_server.models.get_records200_response_records_inner import GetRecords200ResponseRecordsInner
from openapi_server.models.get_records_facets200_response import GetRecordsFacets200Response
from openapi_server.models.send_dataset_feedback_request import SendDatasetFeedbackRequest
from openapi_server import util


async def aggregate_records(request: web.Request, source, dataset_id, select=None, where=None, group_by=None, order_by=None, limit=None, offset=None, facet=None, refine=None, exclude=None) -> web.Response:
    """aggregate_records

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


async def download_dataset_attachement(request: web.Request, source, dataset_id, attachment_id) -> web.Response:
    """download_dataset_attachement

    Download attachment 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param attachment_id: 
    :type attachment_id: str

    """
    return web.Response(status=200)


async def download_dataset_snapshot(request: web.Request, source, dataset_id, snapshot_id, timezone=None) -> web.Response:
    """download_dataset_snapshot

    List of all snapshots for this dataset. 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param snapshot_id: 
    :type snapshot_id: str
    :param timezone: Set timezone for datetime fields
    :type timezone: str

    """
    return web.Response(status=200)


async def get_dataset(request: web.Request, source, dataset_id, select=None, pretty=None, timezone=None, include_app_metas=None) -> web.Response:
    """get_dataset

    List of available endpoints for the specified dataset, with metadata and endpoints.  Will provide links for: * the attachments endpoint * the files endpoint * the records endpoint * the catalog endpoint 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param pretty: Activate pretty print
    :type pretty: bool
    :param timezone: Set timezone for datetime fields
    :type timezone: str
    :param include_app_metas: Explicitely request application metas for each datasets. 
    :type include_app_metas: bool

    """
    return web.Response(status=200)


async def get_dataset_attachements(request: web.Request, source, dataset_id) -> web.Response:
    """get_dataset_attachements

    Get list of all available attachments 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str

    """
    return web.Response(status=200)


async def get_dataset_file(request: web.Request, source, dataset_id, file_id, thumbnail_size=None) -> web.Response:
    """get_dataset_file

    Download file 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param file_id: 
    :type file_id: str
    :param thumbnail_size: Set the size of the thumbnail representing the resource (attachment, image or file)
    :type thumbnail_size: str

    """
    return web.Response(status=200)


async def get_dataset_reuse(request: web.Request, source, dataset_id, reuse_id, timezone=None) -> web.Response:
    """get_dataset_reuse

    Retrieve a single reuse based on its ID. 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param reuse_id: 
    :type reuse_id: str
    :param timezone: Set timezone for datetime fields
    :type timezone: str

    """
    return web.Response(status=200)


async def get_dataset_reuses(request: web.Request, source, dataset_id, limit=None, offset=None, timezone=None) -> web.Response:
    """get_dataset_reuses

    Get list of reuses 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param limit: Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    :type limit: int
    :param offset: Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    :type offset: int
    :param timezone: Set timezone for datetime fields
    :type timezone: str

    """
    return web.Response(status=200)


async def get_dataset_snapshots(request: web.Request, source, dataset_id, timezone=None) -> web.Response:
    """get_dataset_snapshots

    List of all snapshots for this dataset. 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param timezone: Set timezone for datetime fields
    :type timezone: str

    """
    return web.Response(status=200)


async def get_record(request: web.Request, source, dataset_id, record_id, select=None, pretty=None, timezone=None) -> web.Response:
    """get_record

    Retrieve a single record based on its ID. 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param record_id: 
    :type record_id: str
    :param select: A select expression can be used to add, remove or change fields to return. An expression can be:   - a wildcard (&#39;*&#39;): return all fields   - a field name: return only this field   - an include/exclude function. Include (resp exclude) all field matching include/exclude expression. This expression can contain wildcard. For example: include(spa*) will return all fields begining with &#39;spa&#39;   - a complex expression: return the result of this expression. A label can be set for this expression, in that case, field will be named with this label. For instance: &#39;size * 2 as bigger_size&#39; will return a new field named bigger_size and containing the double of size field value. 
    :type select: str
    :param pretty: Activate pretty print
    :type pretty: bool
    :param timezone: Set timezone for datetime fields
    :type timezone: str

    """
    return web.Response(status=200)


async def get_records(request: web.Request, source, dataset_id, select=None, where=None, group_by=None, sort=None, order_by=None, limit=None, offset=None, search=None, facet=None, refine=None, exclude=None, pretty=None, timezone=None) -> web.Response:
    """get_records

    Search dataset&#39;s records. 

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
    :param sort: **Deprecated, use &#x60;order_by&#x60; instead.**  A list of field names, each possibly prefixed with a minus (-).  Sorts results according to the specified fields&#39; values. By default, the sort is ascending (from the smallest value to the biggest value). A minus sign (‘-‘) may be used to perform a descending sort. Sorting is only available on numeric fields (int, double, date and datetime) and on text fields which have the sortable annotation. 
    :type sort: List[str]
    :param order_by: A comma-separated list of field names or aggregations to sort on, followed by an order (&#x60;asc&#x60; or &#x60;desc&#x60;).  Sorts results according to the specified fields&#39; values in ascending order by default. To sort results in descending order, use the &#x60;desc&#x60; keyword.  Example: &#x60;sum(age) desc, name asc&#x60; 
    :type order_by: List[str]
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

    """
    return web.Response(status=200)


async def get_records_facets(request: web.Request, source, dataset_id, where=None, facet=None, refine=None, exclude=None, search=None, timezone=None) -> web.Response:
    """get_records_facets

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


async def send_dataset_feedback(request: web.Request, source, dataset_id, feedback) -> web.Response:
    """send_dataset_feedback

    Create new feedback entry. 

    :param source: Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    :type source: str
    :param dataset_id: Dataset identifier.  Can be found in the \&quot;information\&quot; tab of the dataset page. 
    :type dataset_id: str
    :param feedback: Feedback entry
    :type feedback: dict | bytes

    """
    feedback = SendDatasetFeedbackRequest.from_dict(feedback)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_association_filter_0(request: web.Request, target=None, disease=None, therapeutic_area=None, datasource=None, datatype=None, pathway=None, target_class=None, uniprotkw=None, direct=None, datastructure=None, fields=None, facets=None, scorevalue_min=None, scorevalue_max=None, scorevalue_types=None, size=None, _from=None, format=None, sort=None, search=None) -> web.Response:
    """Filter available associations

    More complex queries for associations scores and objects can be done using this method, which allows to sort in different order, restrict to a specific class of diseases or targets, as well as filtering results by score and associated pathways. 

    :param target: A target identifier listed as target.id.
    :type target: str
    :param disease: An EFO code listed as disease.id.
    :type disease: str
    :param therapeutic_area: An EFO code of a therapeutic area.
    :type therapeutic_area: str
    :param datasource: Data source to consider.
    :type datasource: str
    :param datatype: Data type to consider.
    :type datatype: str
    :param pathway: A Reactome pathway identifier (returning only those targets linked to the specified pathway).
    :type pathway: str
    :param target_class: A ChEMBL target class identifier (returning only those targets belonging to the specified class).
    :type target_class: str
    :param uniprotkw: A UniProt keyword (meaning all the targets linked to that keyword).
    :type uniprotkw: str
    :param direct: If &#x60;true&#x60;, it returns associations that have at least one direct evidence connecting the target and the disease. If &#x60;false&#x60; it only returns associations for which there is no direct evidence connecting the target and the disease, but only evidence connecting the target to a children of the disease in the EFO ontology.
    :type direct: bool
    :param datastructure: Type of data structure to return. Can be &#39;full&#39;, &#39;simple&#39;, &#39;ids&#39;, or &#39;count&#39;.
    :type datastructure: str
    :param fields: Fields you want to retrieve. This will get priority over the data structure requested.
    :type fields: str
    :param facets: Returns facets
    :type facets: bool
    :param scorevalue_min: Filter by minimum score value. The default is 0, but using 0.2 is a good trade-off to filter lower quality data points.
    :type scorevalue_min: float
    :param scorevalue_max: Filter by maximum score value.
    :type scorevalue_max: float
    :param scorevalue_types: Score types to apply the score value min and max filters. The default is &#x60;overall&#x60;.
    :type scorevalue_types: str
    :param size: Maximum amount of results to return. Defaults to 10, max is 10000.
    :type size: 
    :param _from: How many initial results should be skipped. Defaults to 0.
    :type _from: 
    :param format: Format to get the data back. Can be &#39;json&#39;, &#39;xml&#39;, &#39;tab&#39; or &#39;csv&#39;. **Note** that this option can only be used when calling the API directly and will not work in this page. The response here will always be JSON.
    :type format: str
    :param sort: Sort by the given score type. Defaults to &#39;overall&#39; and descending order. Use &#39;~&#39; prefix to do ascending order e.g. &#39;~overall&#39;. You will call a data type score like: &#39;datatypes.literature&#39;, and a data source as &#39;datasources.gwas&#39;. Supports multiple entries. 
    :type sort: str
    :param search: Restrict the filtered results to those matching the passed string. The matching is done with a phrase match prefix. 
    :type search: str

    """
    return web.Response(status=200)


async def get_evidence_filter_0(request: web.Request, target=None, disease=None, data_source=None, datatype=None, pathway=None, uniprotkw=None, datastructure=None, fields=None, scorevalue_min=None, scorevalue_max=None, sort=None, size=None, _from=None, format=None) -> web.Response:
    """Filter available evidence

    The filter method allows to retrieve the specific data that supports a connection between targets and diseases. Filters can be used to restrict the results by source and type of data, or limit results to targets which are part of a particular pathway. Minimum and maximum scores can be specified as well as the type of evidence linking target and disease. **Note** that multiple genes and diseases can be specified in the same request. 

    :param target: A target identifier listed as target.id.
    :type target: str
    :param disease: An EFO code listed as disease.id.
    :type disease: str
    :param data_source: Data source to consider.
    :type data_source: str
    :param datatype: Data type to consider.
    :type datatype: str
    :param pathway: A pathway identifier (meaning all the targets linked to that pathway).
    :type pathway: str
    :param uniprotkw: A UniProt keyword (meaning all the targets linked to that keyword).
    :type uniprotkw: str
    :param datastructure: Type of data structure to return. Can be &#39;full&#39;, &#39;simple&#39;, &#39;ids&#39;, or &#39;count&#39;.
    :type datastructure: str
    :param fields: The fields you want to retrieve. This will get priority over the data structure requested.
    :type fields: str
    :param scorevalue_min: Filter by minimum score value. The default is 0, but using 0.2 is a good trade-off to filter lower quality data points.
    :type scorevalue_min: float
    :param scorevalue_max: Filter by maximum score value.
    :type scorevalue_max: float
    :param sort: Sort by the given field. The default is &#39;scores.association_score&#39; in descending order. Use &#39;~&#39; prefix to do ascending order e.g. &#39;~scores.association_score&#39;. It supports multiple entries. 
    :type sort: str
    :param size: Maximum amount of results to return. Defaults to 10, max is 10000.
    :type size: 
    :param _from: How many initial results should be skipped. Defaults to 0.
    :type _from: 
    :param format: Format to get the data back. Can be &#39;json&#39;, &#39;xml&#39;, &#39;tab&#39; or &#39;csv&#39;. **Note** that this option can only be used when calling the API directly and will not work in this page. The response here will always be JSON.
    :type format: str

    """
    return web.Response(status=200)


async def post_association_filter_0(request: web.Request, body) -> web.Response:
    """Batch query available associations

    Complex queries and filters for association objects can also be submitted using a JSON object and the equivalent POST method. 

    :param body: Filters to apply when retrieving association objects.
    :type body: str

    """
    return web.Response(status=200)


async def post_evidence_filter_0(request: web.Request, body) -> web.Response:
    """Batch filter available evidence

    POST version of [/public/evidence/filter](#!/public/get_public_evidence_filter). Filters can be specified as part of a &#x60;json&#x60; object in the body, simplifying the submission of queries. 

    :param body: Filters to apply when retrieving evidence string objects.
    :type body: str

    """
    return web.Response(status=200)

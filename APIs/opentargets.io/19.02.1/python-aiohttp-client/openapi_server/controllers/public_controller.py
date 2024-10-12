from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_association_by_id(request: web.Request, id) -> web.Response:
    """Get association by id

    Once we integrate all evidence connecting a target to a specific disease, we  compute an association score by the means of an harmonic sum. This *association score* provides  an indication of how strong the evidence behind each connection is and can be  used to rank genes in order of likelihood as drug targets.  The association ID is constructed by using the Ensembl ID of the gene and the  EFO ID for the disease (e.g. ENSG00000073756-EFO_0003767).  The method returns an association object, which contains the data and summary  on each evidence type included in the calculation of the score, as well as the score itself. 

    :param id: An association ID usually in the form of &#x60;TARGET_ID-DISEASE_ID&#x60;.
    :type id: str

    """
    return web.Response(status=200)


async def get_association_filter(request: web.Request, target=None, disease=None, therapeutic_area=None, datasource=None, datatype=None, pathway=None, target_class=None, uniprotkw=None, direct=None, datastructure=None, fields=None, facets=None, scorevalue_min=None, scorevalue_max=None, scorevalue_types=None, size=None, _from=None, format=None, sort=None, search=None) -> web.Response:
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


async def get_data_metrics(request: web.Request, ) -> web.Response:
    """Get metrics about the current data release

    Returns the metrics about associations and evidences, divided by datasource, genes and so on. 


    """
    return web.Response(status=200)


async def get_data_stats(request: web.Request, ) -> web.Response:
    """Get statistics about the current data release

    Returns the number of associations and evidences, divided by datasource. 


    """
    return web.Response(status=200)


async def get_evidence_by_id(request: web.Request, id) -> web.Response:
    """Get evidence by ID

    We call **evidence** a unit of data that support a connection between a target and a disease. The Open Targets Platform integrates multiple types of evidence including genetic associations, somatic mutations, RNA expression and target-disease associations mined from the literature. This method allows you to retrieve a single evidence item or a list of pieces of evidence by using their targetvalidation.org ID.  Evidence IDs are unique within each data release (e.g. &#x60;8ed3d7568a8c6cac9c95cfb869bac762&#x60; for release 1.2). You can obtain a list of evidence and their IDs from other API calls such as [/public/evidence/filter](#!/public/get_public_evidence_filter).  **Please note** that a specific evidence ID may change between data releases. We can not guarantee that a specific evidence ID will refer to the same piece of evidence connecting a target and its diseases. 

    :param id: Internal unique ID of the evidence string to retrieve.
    :type id: str

    """
    return web.Response(status=200)


async def get_evidence_filter(request: web.Request, target=None, disease=None, data_source=None, datatype=None, pathway=None, uniprotkw=None, datastructure=None, fields=None, scorevalue_min=None, scorevalue_max=None, sort=None, size=None, _from=None, format=None) -> web.Response:
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


async def get_ping(request: web.Request, ) -> web.Response:
    """Ping service

    Check if the API is up 


    """
    return web.Response(status=200)


async def get_search(request: web.Request, q, size=None, _from=None, filter=None) -> web.Response:
    """Search for a disease or a target

    This method allows you to look for gene or diseases of interest using a free text search, replicating the functionality of the search box on our homepage. It should be used to identify the best match for a disease or target of interest, rather than gathering a specific set of evidence. 

    :param q: A full text query.
    :type q: str
    :param size: Maximum amount of results to return. Defaults to 10, max is 10000.
    :type size: str
    :param _from: How many initial results should be skipped. Defaults to 0.
    :type _from: str
    :param filter: Restrict the search to the type requested. Eg. &#x60;target&#x60; or &#x60;disease&#x60;.
    :type filter: str

    """
    return web.Response(status=200)


async def get_therapeutic_areas(request: web.Request, ) -> web.Response:
    """Get the list of therapeutic areas about the current data release

    Returns the list of therapeutic areas for the current data release 


    """
    return web.Response(status=200)


async def get_version(request: web.Request, ) -> web.Response:
    """Get API version

    Returns current API version. 


    """
    return web.Response(status=200)


async def post_association_filter(request: web.Request, body) -> web.Response:
    """Batch query available associations

    Complex queries and filters for association objects can also be submitted using a JSON object and the equivalent POST method. 

    :param body: Filters to apply when retrieving association objects.
    :type body: str

    """
    return web.Response(status=200)


async def post_evidence_by_id(request: web.Request, body) -> web.Response:
    """Get evidence for a list of IDs

    This is the POST version of [/public/evidence](#!/public/get_public_evidence). It allows to query for a list of evidence strings encoded in a &#x60;json&#x60; object to be passed in the body. 

    :param body: IDs of the evidence string to retrieve.
    :type body: str

    """
    return web.Response(status=200)


async def post_evidence_filter(request: web.Request, body) -> web.Response:
    """Batch filter available evidence

    POST version of [/public/evidence/filter](#!/public/get_public_evidence_filter). Filters can be specified as part of a &#x60;json&#x60; object in the body, simplifying the submission of queries. 

    :param body: Filters to apply when retrieving evidence string objects.
    :type body: str

    """
    return web.Response(status=200)

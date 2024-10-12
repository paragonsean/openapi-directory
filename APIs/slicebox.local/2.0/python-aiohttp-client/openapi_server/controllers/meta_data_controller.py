from typing import List, Dict
from aiohttp import web

from openapi_server.models.flat_series import FlatSeries
from openapi_server.models.idsquery import Idsquery
from openapi_server.models.image import Image
from openapi_server.models.patient import Patient
from openapi_server.models.query import Query
from openapi_server.models.series import Series
from openapi_server.models.seriesidseriestypesresult import Seriesidseriestypesresult
from openapi_server.models.seriestag import Seriestag
from openapi_server.models.seriestype import Seriestype
from openapi_server.models.source import Source
from openapi_server.models.study import Study
from openapi_server import util


async def metadata_flatseries_get(request: web.Request, startindex=None, count=None, orderby=None, orderascending=None, filter=None, sources=None, seriestypes=None, seriestags=None) -> web.Response:
    """metadata_flatseries_get

    Returns a list of flattened metadata on the patient, study and series levels

    :param startindex: start index of returned slice of flat series
    :type startindex: int
    :param count: size of returned slice of flat series
    :type count: int
    :param orderby: flat series property to order results by
    :type orderby: str
    :param orderascending: order result ascendingly if true, descendingly otherwise
    :type orderascending: bool
    :param filter: filter the results by matching substrings of flat series properties against this value
    :type filter: str
    :param sources: filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    :type sources: str
    :param seriestypes: filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
    :type seriestypes: str
    :param seriestags: filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
    :type seriestags: str

    """
    return web.Response(status=200)


async def metadata_flatseries_id_get(request: web.Request, id) -> web.Response:
    """metadata_flatseries_id_get

    Return the flat series with the supplied ID

    :param id: ID of flat series
    :type id: int

    """
    return web.Response(status=200)


async def metadata_flatseries_query_post(request: web.Request, query) -> web.Response:
    """metadata_flatseries_query_post

    submit a query for flat series

    :param query: parameters of flat series query
    :type query: dict | bytes

    """
    query = Query.from_dict(query)
    return web.Response(status=200)


async def metadata_images_get(request: web.Request, seriesid, startindex=None, count=None) -> web.Response:
    """metadata_images_get

    Returns a list of metadata on the image level of the DICOM hierarchy

    :param seriesid: reference to series to list images for
    :type seriesid: int
    :param startindex: start index of returned slice of images
    :type startindex: int
    :param count: size of returned slice of images
    :type count: int

    """
    return web.Response(status=200)


async def metadata_images_id_get(request: web.Request, id) -> web.Response:
    """metadata_images_id_get

    Return the image with the supplied ID

    :param id: ID of image
    :type id: int

    """
    return web.Response(status=200)


async def metadata_images_query_post(request: web.Request, query) -> web.Response:
    """metadata_images_query_post

    submit a query for images

    :param query: parameters of images query
    :type query: dict | bytes

    """
    query = Query.from_dict(query)
    return web.Response(status=200)


async def metadata_patients_get(request: web.Request, startindex=None, count=None, orderby=None, orderascending=None, filter=None, sources=None, seriestypes=None, seriestags=None) -> web.Response:
    """metadata_patients_get

    Returns a list of metadata on the patient level of the DICOM hierarchy

    :param startindex: start index of returned slice of patients
    :type startindex: int
    :param count: size of returned slice of patients
    :type count: int
    :param orderby: patient property to order results by
    :type orderby: str
    :param orderascending: order result ascendingly if true, descendingly otherwise
    :type orderascending: bool
    :param filter: filter the results by matching substrings of patient properties against this value
    :type filter: str
    :param sources: filter the results by matching on one or more underlying series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    :type sources: str
    :param seriestypes: filter the results by matching on one or more underlying series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows results including series assigned to either of the series types with ids 3, 7 and 22.
    :type seriestypes: str
    :param seriestags: filter the results by matching on one or more underlying series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows results including series with either of the series tags with ids 6, 2 and 11.
    :type seriestags: str

    """
    return web.Response(status=200)


async def metadata_patients_id_get(request: web.Request, id) -> web.Response:
    """metadata_patients_id_get

    Return the patient with the supplied ID

    :param id: ID of patient
    :type id: int

    """
    return web.Response(status=200)


async def metadata_patients_id_images_get(request: web.Request, id, sources=None, seriestypes=None, seriestags=None) -> web.Response:
    """metadata_patients_id_images_get

    Returns all images for the patient with the supplied patient ID

    :param id: ID of patient
    :type id: int
    :param sources: filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    :type sources: str
    :param seriestypes: filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
    :type seriestypes: str
    :param seriestags: filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
    :type seriestags: str

    """
    return web.Response(status=200)


async def metadata_patients_query_post(request: web.Request, query) -> web.Response:
    """metadata_patients_query_post

    submit a query for patients

    :param query: parameters of patient query
    :type query: dict | bytes

    """
    query = Query.from_dict(query)
    return web.Response(status=200)


async def metadata_series_get(request: web.Request, studyid, startindex=None, count=None, sources=None, seriestypes=None, seriestags=None) -> web.Response:
    """metadata_series_get

    Returns a list of metadata on the series level of the DICOM hierarchy

    :param studyid: reference to study to list series for
    :type studyid: int
    :param startindex: start index of returned slice of series
    :type startindex: int
    :param count: size of returned slice of series
    :type count: int
    :param sources: filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    :type sources: str
    :param seriestypes: filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
    :type seriestypes: str
    :param seriestags: filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
    :type seriestags: str

    """
    return web.Response(status=200)


async def metadata_series_id_get(request: web.Request, id) -> web.Response:
    """metadata_series_id_get

    Return the series with the supplied ID

    :param id: ID of series
    :type id: int

    """
    return web.Response(status=200)


async def metadata_series_id_seriestags_get(request: web.Request, id) -> web.Response:
    """metadata_series_id_seriestags_get

    get the list of series tags for the series with the supplied ID.

    :param id: ID of series
    :type id: int

    """
    return web.Response(status=200)


async def metadata_series_id_seriestags_post(request: web.Request, id, query) -> web.Response:
    """metadata_series_id_seriestags_post

    add a series tag to the series with the supplied ID

    :param id: ID of series
    :type id: int
    :param query: series tag to add
    :type query: dict | bytes

    """
    query = Seriestag.from_dict(query)
    return web.Response(status=200)


async def metadata_series_id_seriestypes_delete(request: web.Request, id) -> web.Response:
    """metadata_series_id_seriestypes_delete

    Delete all series types for the series with the supplied ID

    :param id: ID of series
    :type id: int

    """
    return web.Response(status=200)


async def metadata_series_id_seriestypes_get(request: web.Request, id) -> web.Response:
    """metadata_series_id_seriestypes_get

    get the list of series types for the series with the supplied ID.

    :param id: ID of series
    :type id: int

    """
    return web.Response(status=200)


async def metadata_series_id_source_get(request: web.Request, id) -> web.Response:
    """metadata_series_id_source_get

    Return the source of the series with the supplied ID

    :param id: ID of series
    :type id: int

    """
    return web.Response(status=200)


async def metadata_series_query_post(request: web.Request, query) -> web.Response:
    """metadata_series_query_post

    submit a query for series

    :param query: parameters of series query
    :type query: dict | bytes

    """
    query = Query.from_dict(query)
    return web.Response(status=200)


async def metadata_series_series_id_seriestags_series_tag_id_delete(request: web.Request, series_id, series_tag_id) -> web.Response:
    """metadata_series_series_id_seriestags_series_tag_id_delete

    Delete the series tag with the supplied series tag ID from the series with the supplied series ID

    :param series_id: ID of series
    :type series_id: int
    :param series_tag_id: ID of series tag to remove
    :type series_tag_id: int

    """
    return web.Response(status=200)


async def metadata_series_series_id_seriestypes_series_type_id_delete(request: web.Request, series_id, series_type_id) -> web.Response:
    """metadata_series_series_id_seriestypes_series_type_id_delete

    Delete the series type with the supplied series type ID from the series with the supplied series ID

    :param series_id: ID of series
    :type series_id: int
    :param series_type_id: ID of series type to remove
    :type series_type_id: int

    """
    return web.Response(status=200)


async def metadata_series_series_id_seriestypes_series_type_id_put(request: web.Request, series_id, series_type_id) -> web.Response:
    """metadata_series_series_id_seriestypes_series_type_id_put

    Add the series type with the supplied series type ID to the series with the supplied series ID

    :param series_id: ID of series
    :type series_id: int
    :param series_type_id: ID of series type to add
    :type series_type_id: int

    """
    return web.Response(status=200)


async def metadata_seriestags_get(request: web.Request, ) -> web.Response:
    """metadata_seriestags_get

    Returns a list of series tags currently currently in use.


    """
    return web.Response(status=200)


async def metadata_studies_get(request: web.Request, patientid, startindex=None, count=None, sources=None, seriestypes=None, seriestags=None) -> web.Response:
    """metadata_studies_get

    Returns a list of metadata on the study level of the DICOM hierarchy

    :param patientid: reference to patient to list studies for
    :type patientid: int
    :param startindex: start index of returned slice of studies
    :type startindex: int
    :param count: size of returned slice of studies
    :type count: int
    :param sources: filter the results by matching on one or more underlying series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    :type sources: str
    :param seriestypes: filter the results by matching on one or more underlying series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows results including series assigned to either of the series types with ids 3, 7 and 22.
    :type seriestypes: str
    :param seriestags: filter the results by matching on one or more underlying series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows results including series with either of the series tags with ids 6, 2 and 11.
    :type seriestags: str

    """
    return web.Response(status=200)


async def metadata_studies_id_get(request: web.Request, id) -> web.Response:
    """metadata_studies_id_get

    Return the study with the supplied ID

    :param id: ID of study
    :type id: int

    """
    return web.Response(status=200)


async def metadata_studies_id_images_get(request: web.Request, id, sources=None, seriestypes=None, seriestags=None) -> web.Response:
    """metadata_studies_id_images_get

    Returns all images for the study with the supplied study ID

    :param id: ID of study
    :type id: int
    :param sources: filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    :type sources: str
    :param seriestypes: filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
    :type seriestypes: str
    :param seriestags: filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
    :type seriestags: str

    """
    return web.Response(status=200)


async def metadata_studies_query_post(request: web.Request, query) -> web.Response:
    """metadata_studies_query_post

    submit a query for studies

    :param query: parameters of study query
    :type query: dict | bytes

    """
    query = Query.from_dict(query)
    return web.Response(status=200)


async def seriestypes_series_query_post(request: web.Request, query) -> web.Response:
    """seriestypes_series_query_post

    submit a query for seriestypes for a list of series

    :param query: parameters of series query
    :type query: dict | bytes

    """
    query = Idsquery.from_dict(query)
    return web.Response(status=200)

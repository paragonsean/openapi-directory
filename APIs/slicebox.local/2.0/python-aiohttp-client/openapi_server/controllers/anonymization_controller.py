from typing import List, Dict
from aiohttp import web

from openapi_server.models.anonymization_data import AnonymizationData
from openapi_server.models.anonymization_key import AnonymizationKey
from openapi_server.models.anonymization_key_query import AnonymizationKeyQuery
from openapi_server.models.anonymization_key_value import AnonymizationKeyValue
from openapi_server.models.confidentiality_option import ConfidentialityOption
from openapi_server.models.image import Image
from openapi_server.models.image_tag_values import ImageTagValues
from openapi_server import util


async def anonymization_anonymize_post(request: web.Request, query) -> web.Response:
    """anonymization_anonymize_post

    anonymize the images corresponding to the supplied list of image IDs (each paired with a list of DICOM tag translation). This route corresponds to repeated use of the route /images/{id}/anonymize.

    :param query: parameters of anonymization key query
    :type query: list | bytes

    """
    query = [ImageTagValues.from_dict(d) for d in query]
    return web.Response(status=200)


async def anonymization_keys_export_csv_get(request: web.Request, ) -> web.Response:
    """anonymization_keys_export_csv_get

    export all anonymization keys as a csv file


    """
    return web.Response(status=200)


async def anonymization_keys_get(request: web.Request, startindex=None, count=None, orderby=None, orderascending=None, filter=None) -> web.Response:
    """anonymization_keys_get

    get a list of anonymization keys, each specifying how vital DICOM attributes have been anonymized for a particular image

    :param startindex: start index of returned slice of anonymization keys
    :type startindex: int
    :param count: size of returned slice of anonymization keys
    :type count: int
    :param orderby: property to order results by
    :type orderby: str
    :param orderascending: order result ascendingly if true, descendingly otherwise
    :type orderascending: bool
    :param filter: filter the results by matching substrings of properties against this value
    :type filter: str

    """
    return web.Response(status=200)


async def anonymization_keys_id_delete(request: web.Request, id) -> web.Response:
    """anonymization_keys_id_delete

    delete an anonymization key that is no longer of interest

    :param id: ID of anonymization key
    :type id: int

    """
    return web.Response(status=200)


async def anonymization_keys_id_get(request: web.Request, id) -> web.Response:
    """anonymization_keys_id_get

    get the anonymization key with the supplied ID

    :param id: ID of anonymization key
    :type id: int

    """
    return web.Response(status=200)


async def anonymization_keys_id_keyvalues_get(request: web.Request, id) -> web.Response:
    """anonymization_keys_id_keyvalues_get

    get pointers to the images corresponding to the anonymization key with the supplied ID

    :param id: ID of anonymization key
    :type id: int

    """
    return web.Response(status=200)


async def anonymization_keys_query_post(request: web.Request, query) -> web.Response:
    """anonymization_keys_query_post

    submit a query for anonymization keys

    :param query: parameters of anonymization key query
    :type query: dict | bytes

    """
    query = AnonymizationKeyQuery.from_dict(query)
    return web.Response(status=200)


async def anonymization_options_get(request: web.Request, ) -> web.Response:
    """anonymization_options_get

    list all supported anonymization options defining an anonymization profile


    """
    return web.Response(status=200)


async def images_id_anonymize_put(request: web.Request, id, tag_values) -> web.Response:
    """images_id_anonymize_put

    delete the selected image and replace it with an anonymized version

    :param id: ID of image to anonymize
    :type id: int
    :param tag_values: specification of values for anonymous DICOM attributes
    :type tag_values: dict | bytes

    """
    tag_values = AnonymizationData.from_dict(tag_values)
    return web.Response(status=200)


async def images_id_anonymized_post(request: web.Request, id, tag_values) -> web.Response:
    """images_id_anonymized_post

    get an anonymized version of the image with the supplied ID

    :param id: ID of image for which to get anonymized dataset
    :type id: int
    :param tag_values: specification of values for anonymous DICOM attributes
    :type tag_values: dict | bytes

    """
    tag_values = AnonymizationData.from_dict(tag_values)
    return web.Response(status=200)

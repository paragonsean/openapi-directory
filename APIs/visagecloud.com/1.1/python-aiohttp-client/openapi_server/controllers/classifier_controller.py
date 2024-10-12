from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_response import RestResponse
from openapi_server import util


async def add_svm_classifier_using_post(request: web.Request, access_key, secret_key, name, collection_ids, classification_attribute_name, preprocessor=None, consider_view_points=None, seed=None, training_ratio=None, probability_parameter=None, gamma_parameter=None, nu_parameter=None, c_parameter=None, svm_type_parameter=None, kernel_type_parameter=None, cache_size_parameter=None, eps_parameter=None) -> web.Response:
    """Create new SVM classifier with given name

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param name: The name of the SVM classifier that will be created
    :type name: str
    :param collection_ids: Collection ids
    :type collection_ids: List[str]
    :param classification_attribute_name: Classification attribute name
    :type classification_attribute_name: str
    :param preprocessor: Preprocessor
    :type preprocessor: str
    :param consider_view_points: Consider view point
    :type consider_view_points: bool
    :param seed: Seed for divididing training and evaluation sets
    :type seed: int
    :param training_ratio: Training ratio
    :type training_ratio: float
    :param probability_parameter: Probability parameter
    :type probability_parameter: int
    :param gamma_parameter: Gamma parameter
    :type gamma_parameter: float
    :param nu_parameter: Nu parameter
    :type nu_parameter: float
    :param c_parameter: c parameter
    :type c_parameter: float
    :param svm_type_parameter: SVM type parameter
    :type svm_type_parameter: int
    :param kernel_type_parameter: Kernel type parameter
    :type kernel_type_parameter: int
    :param cache_size_parameter: Cache size parameter
    :type cache_size_parameter: float
    :param eps_parameter: Eps parameter
    :type eps_parameter: float

    """
    return web.Response(status=200)


async def get_classifer_full_using_get(request: web.Request, access_key, secret_key, id) -> web.Response:
    """Get classifier full

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param id: The id of the classifier that you want the status for
    :type id: str

    """
    return web.Response(status=200)


async def get_classifer_status_using_get(request: web.Request, access_key, secret_key, id) -> web.Response:
    """Get classifer status

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param id: The id of the classifier that you want the status for
    :type id: str

    """
    return web.Response(status=200)


async def remove_classifer_using_delete(request: web.Request, access_key, secret_key, id) -> web.Response:
    """Delete existing classifier

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param id: The id of the classifier that will be removed
    :type id: str

    """
    return web.Response(status=200)

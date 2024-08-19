from typing import List, Dict
from aiohttp import web

from openapi_server.models.dataset_type_collection_output import DatasetTypeCollectionOutput
from openapi_server.models.dataset_type_output import DatasetTypeOutput
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def query_datataset_information_of_all_the_resource_types_v1_dataset_ip_get(request: web.Request, ) -> web.Response:
    """Get the list of all the datasets available in the platform.

    ### What Obtain the list of all the datasets available in the platform. A dataset is a collection of different data sources that are related to a specific topic. The name of the dataset describes the specific topic.  ### Parameters No parameters are required.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;types&#x60;&#x60;: a list of JSON objects with the following fields:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual dataset information.     - &#x60;&#x60;type&#x60;&#x60;: what type of dataset is this. The only allowed value is &#x60;&#x60;ip&#x60;&#x60;.     - &#x60;&#x60;name&#x60;&#x60;: the name of the dataset in human readable form.     - &#x60;&#x60;description&#x60;&#x60;: a human readable long description of the dataset.     - &#x60;&#x60;status&#x60;&#x60;: the status of the dataset. The only allowed value is &#x60;&#x60;ENABLED&#x60;&#x60;.     - &#x60;&#x60;items&#x60;&#x60;: the number of &#39;live&#39; items in the dataset when the request is performed.  ### Errors It will return the API Global errors described in the API description.


    """
    return web.Response(status=200)


async def query_datataset_information_of_the_resource_type_v1_dataset_ip_name_get(request: web.Request, name) -> web.Response:
    """Get the detailed information of the dataset queried.

    ### What Get the detailed information of the dataset queried by the name. A dataset is a collection of different data sources that are related to a specific topic. The name of the dataset describes the specific topic.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;name&#x60;&#x60;: (Mandatory) The code name that identifies uniquely the dataset in the platform. It must be composed of uppercase letters, numbers and underscores.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual dataset information. - &#x60;&#x60;type&#x60;&#x60;: what type of dataset is this. The only allowed value is &#x60;&#x60;ip&#x60;&#x60;. - &#x60;&#x60;name&#x60;&#x60;: the name of the dataset in human readable form. - &#x60;&#x60;description&#x60;&#x60;: a human readable long description of the dataset. - &#x60;&#x60;status&#x60;&#x60;: the status of the dataset. The only allowed value is &#x60;&#x60;ENABLED&#x60;&#x60;. - &#x60;&#x60;items&#x60;&#x60;: the number of &#39;live&#39; items in the dataset when the request is performed.  ### Errors - a &#x60;404 Not Found&#x60; error if the dataset code name was not found. - a &#x60;422 Unprocessable Entity&#x60; error if dataset code name does not follow the naming convention.  It will also return the API Global errors described in the API description.

    :param name: 
    :type name: str

    """
    return web.Response(status=200)

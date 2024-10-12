from typing import List, Dict
from aiohttp import web

from openapi_server.models.dictionary_entity import DictionaryEntity
from openapi_server.models.many_values_per_type_dto import ManyValuesPerTypeDTO
from openapi_server.models.service_dto import ServiceDTO
from openapi_server import util


async def get_active(request: web.Request, ) -> web.Response:
    """Returns active dictionary entities for all types.

    Returns active dictionary entities for all types.


    """
    return web.Response(status=200)


async def get_active_by_type(request: web.Request, type, name_equals=None) -> web.Response:
    """Returns active values from a given dictionary.

    Returns active values from a given dictionary.

    :param type: dictionary type
    :type type: str
    :param name_equals: exact name of entity
    :type name_equals: str

    """
    return web.Response(status=200)


async def get_all1(request: web.Request, ) -> web.Response:
    """Returns dictionary entities for all types. Both active and not active ones.

    &lt;div&gt;   &lt;p&gt;     XTRF holds many user-defined dictionaries (ie. countries).     Each dictionary contains a set of values (ie. Poland or Germany).     A default value may be defined for a dictionary.   &lt;/p&gt;   &lt;p&gt;     Dictionary values are identified using internal identifier which is constant and unique among other values from the same dictionary.     Please note that name used in dictionary values is presented in the locale of the current identity.     The same dictionary value can have different names, ie. \&quot;Poland\&quot; for one user, \&quot;Polska\&quot; for another one.   &lt;/p&gt;   &lt;p&gt;     Possible dictionary types with short explanation:     &lt;ul&gt;       &lt;li&gt;calculationUnit - predefined values of how to calculate the volume of work into the price&lt;/li&gt;       &lt;li&gt;category - labels to organize data on the platform&lt;/li&gt;       &lt;li&gt;country - list of countries used on the platform&lt;/li&gt;       &lt;li&gt;currency - currencies used in financial operations in the system&lt;/li&gt;       &lt;li&gt;industry - industry sectors which clients specialize in&lt;/li&gt;       &lt;li&gt;jobType - services offered by a company used in customized workflows&lt;/li&gt;       &lt;li&gt;language - list of languages and its values used on the platform&lt;/li&gt;       &lt;li&gt;leadSource - lead/recruitment places where new clients and vendors may be found&lt;/li&gt;       &lt;li&gt;personDepartment - departments in which contact person may be assigned to&lt;/li&gt;       &lt;li&gt;personPosition - positions in which user may be associated with&lt;/li&gt;       &lt;li&gt;province - states and provinces used in various documents on the platform&lt;/li&gt;       &lt;li&gt;specialization - list of specific qualifications required to perform a specific job in the task, for ex. medical, military&lt;/li&gt;     &lt;/ul&gt;   &lt;/p&gt; &lt;/div&gt;


    """
    return web.Response(status=200)


async def get_all3(request: web.Request, name_equals=None) -> web.Response:
    """Returns services list

    Returns workflows list. Both active and not active ones.

    :param name_equals: exact name of entity
    :type name_equals: str

    """
    return web.Response(status=200)


async def get_all_active(request: web.Request, name_equals=None) -> web.Response:
    """Returns active services list

    Returns active workflows list

    :param name_equals: exact name of entity
    :type name_equals: str

    """
    return web.Response(status=200)


async def get_all_by_type(request: web.Request, type, name_equals=None) -> web.Response:
    """Returns all values (both active and not active) from a given dictionary.

    Returns all values (both active and not active) from a given dictionary.

    :param type: dictionary type
    :type type: str
    :param name_equals: exact name of entity
    :type name_equals: str

    """
    return web.Response(status=200)


async def get_by_type_and_id(request: web.Request, type, id) -> web.Response:
    """Returns specific value from a given dictionary.

    Returns specific value from a given dictionary.

    :param type: dictionary type
    :type type: str
    :param id: dictionary value identifier
    :type id: int

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def create_a_map(request: web.Request, variable, entity_id, constraint=None, app_token=None, x_app_token=None) -> web.Response:
    """Create a map

    

    :param variable: A single variable ID.
    :type variable: str
    :param entity_id: A comma separated list of entity IDs. Entities must have the same type and represent geographical regions.
    :type entity_id: str
    :param constraint: Values must be specified for each constraint in the dataset. For example, to generate map data for &#x60;demographics.population.count&#x60;, you must specify a value for &#x60;year&#x60; by passing &#x60;year&#x3D;2013&#x60;.
    :type constraint: str
    :param app_token: The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    :type app_token: str
    :param x_app_token: e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    :type x_app_token: str

    """
    return web.Response(status=200)


async def find_all_available_data_for_some_entities(request: web.Request, entity_id, app_token=None, x_app_token=None) -> web.Response:
    """Find all available data for some entities

    

    :param entity_id: Comma separated list of entity IDs.
    :type entity_id: str
    :param app_token: The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    :type app_token: str
    :param x_app_token: e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    :type x_app_token: str

    """
    return web.Response(status=200)


async def find_the_relatives_of_an_entity(request: web.Request, relation, entity_id, variable_id=None, limit=None, app_token=None, x_app_token=None) -> web.Response:
    """Find the relatives of an entity

    

    :param relation: The type of relation to find.
    :type relation: str
    :param entity_id: ID of the target entity.
    :type entity_id: str
    :param variable_id: If this parameter is included, only entities with data for the given variable will be returned. Note that this may cause the number of entities returned to be less than the specified &#x60;limit&#x60;.
    :type variable_id: str
    :param limit: Maximum number of entities in each group. Must be an integer from 1 to 1000.
    :type limit: 
    :param app_token: The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    :type app_token: str
    :param x_app_token: e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    :type x_app_token: str

    """
    return web.Response(status=200)


async def get_constraint_permutations_for_entities(request: web.Request, variable, entity_id, constraint, app_token=None, x_app_token=None) -> web.Response:
    """Get constraint permutations for entities

    

    :param variable: Full ID of the variable to retrieve.
    :type variable: str
    :param entity_id: Comma separated list of entity IDs.
    :type entity_id: str
    :param constraint: Constraint to use.
    :type constraint: str
    :param app_token: The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    :type app_token: str
    :param x_app_token: e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    :type x_app_token: str

    """
    return web.Response(status=200)


async def get_datasets(request: web.Request, entity_id=None, dataset_id=None, limit=None, offset=None, app_token=None, x_app_token=None) -> web.Response:
    """Get datasets

    

    :param entity_id: Entities to use in formulating the query.
    :type entity_id: str
    :param dataset_id: If included, the search terms of the dataset will be used in the query.
    :type dataset_id: str
    :param limit: Maximum number of results to return. Must be an integer from 0 to 50000.
    :type limit: 
    :param offset: Number of results to skip. Used for pagination.
    :type offset: 
    :param app_token: The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    :type app_token: str
    :param x_app_token: e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    :type x_app_token: str

    """
    return web.Response(status=200)


async def get_entities(request: web.Request, entity_id=None, entity_name=None, entity_type=None, app_token=None, x_app_token=None) -> web.Response:
    """Get Entities

    

    :param entity_id: ID of the entity.
    :type entity_id: str
    :param entity_name: Name of the entity.
    :type entity_name: str
    :param entity_type: Type of the entity.
    :type entity_type: str
    :param app_token: The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    :type app_token: str
    :param x_app_token: e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    :type x_app_token: str

    """
    return web.Response(status=200)


async def get_questions(request: web.Request, query, limit=None, offset=None, app_token=None, x_app_token=None) -> web.Response:
    """Get questions

    

    :param query: String to search against.
    :type query: str
    :param limit: Maximum number of results to return. Must be an integer from 0 to 50000.
    :type limit: 
    :param offset: Number of results to skip. Used for pagination.
    :type offset: 
    :param app_token: The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    :type app_token: str
    :param x_app_token: e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    :type x_app_token: str

    """
    return web.Response(status=200)


async def get_suggestions(request: web.Request, type, query, limit=None, variable_id=None, app_token=None, x_app_token=None) -> web.Response:
    """Get suggestions

    

    :param type: Type of the object to find.
    :type type: str
    :param query: Query to match.
    :type query: str
    :param limit: Maximum number of results to return. Must be an integer from 0 to 100.
    :type limit: 
    :param variable_id: This parameter is only available when suggesting entities with &#x60;type&#x3D;entity&#x60;. If it is provided, suggestions will be filtered to include only entities that have data for the given variable.  If the variable provided is invalid, no entities will be returned.  Note that this filtering will increase response time significantly, so it should only be used when necessary.
    :type variable_id: str
    :param app_token: The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    :type app_token: str
    :param x_app_token: e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    :type x_app_token: str

    """
    return web.Response(status=200)


async def get_values_for_variables(request: web.Request, variable, entity_id=None, forecast=None, describe=None, format=None, app_token=None, x_app_token=None) -> web.Response:
    """Get values for variables

    

    :param variable: Comma separated list of variable IDs. Defaults to retrieving all variables. It is also possible to pass in a topic such as &#x60;demographics&#x60;, or a dataset such as &#x60;demographics.population&#x60;, which would both be equivalent to specifying &#x60;demographics.population.count&#x60; and &#x60;demographics.population.change&#x60;. Note that only variables in the same dataset are allowed.
    :type variable: str
    :param entity_id: Comma separated list of entity IDs. Defaults to retrieving all entities. Note that since there is currently no results pagination, retrieving values for all entities may produce incomplete results.
    :type entity_id: str
    :param forecast: Number of steps to forecast. Must be an integer between 0 and 20. Forecasts are produced using linear extrapolation on the data. They are only available when retrieving data for a single variable across many numerical constraint options.  + Default &#x60;0&#x60;
    :type forecast: 
    :param describe: Whether or not to produce a description of the data. Set to &#x60;true&#x60; to produce a description. Descriptions are not available if no entities are specified.  + Default &#x60;false&#x60;
    :type describe: bool
    :param format: If format is set to &#x60;google&#x60;, the data frame will be formatted as a [Google Visualizations data table](https://developers.google.com/chart/interactive/docs/reference#datatable-class). If the format is not provided or invalid, then the frame will be formatted normally.
    :type format: str
    :param app_token: The [Socrata App Token](https://dev.socrata.com/docs/app-tokens.html) to be used with your request. The &#x60;app_token&#x60; parameter is required if an app token is not passed via the &#x60;X-App-Token&#x60; HTTP header. Clients must [register for their own app tokens](https://dev.socrata.com/docs/app-tokens.html).
    :type app_token: str
    :param x_app_token: e.g. cQovpGcdUT1CSzgYk0KPYdAI0
    :type x_app_token: str

    """
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.auto_complete_suggestions import AutoCompleteSuggestions
from openapi_server.models.converted_jql_queries import ConvertedJQLQueries
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.jql_personal_data_migration_request import JQLPersonalDataMigrationRequest
from openapi_server.models.jql_reference_data import JQLReferenceData
from openapi_server.models.jql_queries_to_parse import JqlQueriesToParse
from openapi_server.models.jql_queries_to_sanitize import JqlQueriesToSanitize
from openapi_server.models.parsed_jql_queries import ParsedJqlQueries
from openapi_server.models.sanitized_jql_queries import SanitizedJqlQueries
from openapi_server.models.search_auto_complete_filter import SearchAutoCompleteFilter
from openapi_server import util


async def get_auto_complete(request: web.Request, ) -> web.Response:
    """Get field reference data (GET)

    Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.  To filter visible field details by project or collapse non-unique fields by field type then [Get field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.


    """
    return web.Response(status=200)


async def get_auto_complete_post(request: web.Request, body) -> web.Response:
    """Get field reference data (POST)

    Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.  This operation can filter the custom fields returned by project. Invalid project IDs in &#x60;projectIds&#x60; are ignored. System fields are always returned.  It can also return the collapsed field for custom fields. Collapsed fields enable searches to be performed across all fields with the same name and of the same field type. For example, the collapsed field &#x60;Component - Component[Dropdown]&#x60; enables dropdown fields &#x60;Component - cf[10061]&#x60; and &#x60;Component - cf[10062]&#x60; to be searched simultaneously.  **[Permissions](#permissions) required:** None.

    :param body: 
    :type body: dict | bytes

    """
    body = SearchAutoCompleteFilter.from_dict(body)
    return web.Response(status=200)


async def get_field_auto_complete_for_query_string(request: web.Request, field_name=None, field_value=None, predicate_name=None, predicate_value=None) -> web.Response:
    """Get field auto complete suggestions

    Returns the JQL search auto complete suggestions for a field.  Suggestions can be obtained by providing:   *  &#x60;fieldName&#x60; to get a list of all values for the field.  *  &#x60;fieldName&#x60; and &#x60;fieldValue&#x60; to get a list of values containing the text in &#x60;fieldValue&#x60;.  *  &#x60;fieldName&#x60; and &#x60;predicateName&#x60; to get a list of all predicate values for the field.  *  &#x60;fieldName&#x60;, &#x60;predicateName&#x60;, and &#x60;predicateValue&#x60; to get a list of predicate values containing the text in &#x60;predicateValue&#x60;.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

    :param field_name: The name of the field.
    :type field_name: str
    :param field_value: The partial field item name entered by the user.
    :type field_value: str
    :param predicate_name: The name of the [ CHANGED operator predicate](https://confluence.atlassian.com/x/hQORLQ#Advancedsearching-operatorsreference-CHANGEDCHANGED) for which the suggestions are generated. The valid predicate operators are *by*, *from*, and *to*.
    :type predicate_name: str
    :param predicate_value: The partial predicate item name entered by the user.
    :type predicate_value: str

    """
    return web.Response(status=200)


async def migrate_queries(request: web.Request, body) -> web.Response:
    """Convert user identifiers to account IDs in JQL queries

    Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL queries with account IDs.  You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-compliant. For more information about GDPR-related changes, see the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/).  **[Permissions](#permissions) required:** Permission to access Jira.

    :param body: 
    :type body: dict | bytes

    """
    body = JQLPersonalDataMigrationRequest.from_dict(body)
    return web.Response(status=200)


async def parse_jql_queries(request: web.Request, body, validation=None) -> web.Response:
    """Parse JQL query

    Parses and validates JQL queries.  Validation is performed in context of the current user.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

    :param body: 
    :type body: dict | bytes
    :param validation: How to validate the JQL query and treat the validation results. Validation options include:   *  &#x60;strict&#x60; Returns all errors. If validation fails, the query structure is not returned.  *  &#x60;warn&#x60; Returns all errors. If validation fails but the JQL query is correctly formed, the query structure is returned.  *  &#x60;none&#x60; No validation is performed. If JQL query is correctly formed, the query structure is returned.
    :type validation: str

    """
    body = JqlQueriesToParse.from_dict(body)
    return web.Response(status=200)


async def sanitise_jql_queries(request: web.Request, body) -> web.Response:
    """Sanitize JQL queries

    Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn&#39;t have permission to view the entity.  For example, if the query contains the clause *project &#x3D; &#39;Secret project&#39;*, and a user does not have browse permission for the project \&quot;Secret project\&quot;, the sanitized query replaces the clause with *project &#x3D; 12345\&quot;* (where 12345 is the ID of the project). If a user has the required permission, the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous user.  Note that sanitization doesn&#39;t make the queries GDPR-compliant, because it doesn&#39;t remove user identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user identifiers to account IDs in JQL queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql/#api-rest-api-3-jql-sanitize-post).  Before sanitization each JQL query is parsed. The queries are returned in the same order that they were passed.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = JqlQueriesToSanitize.from_dict(body)
    return web.Response(status=200)

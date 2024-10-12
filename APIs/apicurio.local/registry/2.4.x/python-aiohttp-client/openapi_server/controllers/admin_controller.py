from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_type_info import ArtifactTypeInfo
from openapi_server.models.configuration_property import ConfigurationProperty
from openapi_server.models.download_ref import DownloadRef
from openapi_server.models.error import Error
from openapi_server.models.log_configuration import LogConfiguration
from openapi_server.models.named_log_configuration import NamedLogConfiguration
from openapi_server.models.role_mapping import RoleMapping
from openapi_server.models.rule import Rule
from openapi_server.models.rule_type import RuleType
from openapi_server.models.update_configuration_property import UpdateConfigurationProperty
from openapi_server.models.update_role import UpdateRole
from openapi_server import util


async def create_global_rule_0(request: web.Request, body) -> web.Response:
    """Create global rule

    Adds a rule to the list of globally configured rules.  This operation can fail for the following reasons:  * The rule type is unknown (HTTP error &#x60;400&#x60;) * The rule already exists (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param body: 
    :type body: dict | bytes

    """
    body = Rule.from_dict(body)
    return web.Response(status=200)


async def create_role_mapping(request: web.Request, body) -> web.Response:
    """Create a new role mapping

    Creates a new mapping between a user/principal and a role.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;)  

    :param body: 
    :type body: dict | bytes

    """
    body = RoleMapping.from_dict(body)
    return web.Response(status=200)


async def delete_all_global_rules_0(request: web.Request, ) -> web.Response:
    """Delete all global rules

    Deletes all globally configured rules.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 


    """
    return web.Response(status=200)


async def delete_global_rule_0(request: web.Request, rule) -> web.Response:
    """Delete global rule

    Deletes a single global rule.  If this is the only rule configured, this is the same as deleting **all** rules.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * Rule cannot be deleted (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param rule: The unique name/type of a rule.
    :type rule: dict | bytes

    """
    rule = .from_dict(rule)
    return web.Response(status=200)


async def delete_role_mapping(request: web.Request, principal_id) -> web.Response:
    """Delete a role mapping

    Deletes a single role mapping, effectively denying access to a user/principal.  This operation can fail for the following reasons:  * No role mapping for the principalId exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param principal_id: Unique id of a principal (typically either a user or service account).
    :type principal_id: str

    """
    return web.Response(status=200)


async def export_data(request: web.Request, for_browser=None) -> web.Response:
    """Export registry data

    Exports registry data as a ZIP archive.

    :param for_browser: Indicates if the operation is done for a browser.  If true, the response will be a JSON payload with a property called &#x60;href&#x60;.  This &#x60;href&#x60; will be a single-use, naked download link suitable for use by a web browser to download the content.
    :type for_browser: bool

    """
    return web.Response(status=200)


async def get_config_property(request: web.Request, property_name) -> web.Response:
    """Get configuration property value

    Returns the value of a single configuration property.  This operation may fail for one of the following reasons:  * Property not found or not configured (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param property_name: The name of a configuration property.
    :type property_name: str

    """
    return web.Response(status=200)


async def get_global_rule_config_0(request: web.Request, rule) -> web.Response:
    """Get global rule configuration

    Returns information about the named globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param rule: The unique name/type of a rule.
    :type rule: dict | bytes

    """
    rule = .from_dict(rule)
    return web.Response(status=200)


async def get_log_configuration(request: web.Request, logger) -> web.Response:
    """Get a single logger configuration

    Returns the configured logger configuration for the provided logger name, if no logger configuration is persisted it will return the current default log configuration in the system.

    :param logger: The name of a single logger.
    :type logger: str

    """
    return web.Response(status=200)


async def get_role_mapping(request: web.Request, principal_id) -> web.Response:
    """Return a single role mapping

    Gets the details of a single role mapping (by &#x60;principalId&#x60;).  This operation can fail for the following reasons:  * No role mapping for the &#x60;principalId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param principal_id: Unique id of a principal (typically either a user or service account).
    :type principal_id: str

    """
    return web.Response(status=200)


async def import_data(request: web.Request, body, x_registry_preserve_global_id=None, x_registry_preserve_content_id=None) -> web.Response:
    """Import registry data

    Imports registry data that was previously exported using the &#x60;/admin/export&#x60; operation.

    :param body: The ZIP file representing the previously exported registry data.
    :type body: str
    :param x_registry_preserve_global_id: If this header is set to false, global ids of imported data will be ignored and replaced by next id in global id sequence. This allows to import any data even thought the global ids would cause a conflict.
    :type x_registry_preserve_global_id: bool
    :param x_registry_preserve_content_id: If this header is set to false, content ids of imported data will be ignored and replaced by next id in content id sequence. The mapping between content and artifacts will be preserved. This allows to import any data even thought the content ids would cause a conflict.
    :type x_registry_preserve_content_id: bool

    """
    return web.Response(status=200)


async def list_artifact_types_0(request: web.Request, ) -> web.Response:
    """List artifact types

    Gets a list of all the configured artifact types.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 


    """
    return web.Response(status=200)


async def list_config_properties(request: web.Request, ) -> web.Response:
    """List all configuration properties

    Returns a list of all configuration properties that have been set.  The list is not paged.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 


    """
    return web.Response(status=200)


async def list_global_rules_0(request: web.Request, ) -> web.Response:
    """List global rules

    Gets a list of all the currently configured global rules (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 


    """
    return web.Response(status=200)


async def list_log_configurations(request: web.Request, ) -> web.Response:
    """List logging configurations

    List all of the configured logging levels.  These override the default logging configuration.


    """
    return web.Response(status=200)


async def list_role_mappings(request: web.Request, ) -> web.Response:
    """List all role mappings

    Gets a list of all role mappings configured in the registry (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 


    """
    return web.Response(status=200)


async def remove_log_configuration(request: web.Request, logger) -> web.Response:
    """Removes logger configuration

    Removes the configured logger configuration (if any) for the given logger.

    :param logger: The name of a single logger.
    :type logger: str

    """
    return web.Response(status=200)


async def reset_config_property(request: web.Request, property_name) -> web.Response:
    """Reset a configuration property

    Resets the value of a single configuration property.  This will return the property to its default value (see external documentation for supported properties and their default values).  This operation may fail for one of the following reasons:  * Property not found or not configured (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param property_name: The name of a configuration property.
    :type property_name: str

    """
    return web.Response(status=200)


async def set_log_configuration(request: web.Request, logger, body) -> web.Response:
    """Set a logger&#39;s configuration

    Configures the logger referenced by the provided logger name with the given configuration.

    :param logger: The name of a single logger.
    :type logger: str
    :param body: The new logger configuration.
    :type body: dict | bytes

    """
    body = LogConfiguration.from_dict(body)
    return web.Response(status=200)


async def update_config_property(request: web.Request, property_name, body) -> web.Response:
    """Update a configuration property

    Updates the value of a single configuration property.  This operation may fail for one of the following reasons:  * Property not found or not configured (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param property_name: The name of a configuration property.
    :type property_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateConfigurationProperty.from_dict(body)
    return web.Response(status=200)


async def update_global_rule_config_0(request: web.Request, rule, body) -> web.Response:
    """Update global rule configuration

    Updates the configuration for a globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param rule: The unique name/type of a rule.
    :type rule: dict | bytes
    :param body: 
    :type body: dict | bytes

    """
    rule = .from_dict(rule)
    body = Rule.from_dict(body)
    return web.Response(status=200)


async def update_role_mapping(request: web.Request, principal_id, body) -> web.Response:
    """Update a role mapping

    Updates a single role mapping for one user/principal.  This operation can fail for the following reasons:  * No role mapping for the principalId exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param principal_id: Unique id of a principal (typically either a user or service account).
    :type principal_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateRole.from_dict(body)
    return web.Response(status=200)

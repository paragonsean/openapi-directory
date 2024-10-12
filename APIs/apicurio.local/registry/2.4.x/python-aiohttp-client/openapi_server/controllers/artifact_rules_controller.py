from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.rule import Rule
from openapi_server.models.rule_type import RuleType
from openapi_server.models.rule_violation_error import RuleViolationError
from openapi_server import util


async def create_artifact_rule(request: web.Request, group_id, artifact_id, body) -> web.Response:
    """Create artifact rule

    Adds a rule to the list of rules that get applied to the artifact when adding new versions.  All configured rules must pass to successfully add a new artifact version.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * Rule (named in the request body) is unknown (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Rule.from_dict(body)
    return web.Response(status=200)


async def delete_artifact_rule(request: web.Request, group_id, artifact_id, rule) -> web.Response:
    """Delete artifact rule

    Deletes a rule from the artifact.  This results in the rule no longer applying for this artifact.  If this is the only rule configured for the artifact, this is the  same as deleting **all** rules, and the globally configured rules now apply to this artifact.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No rule with this name/type is configured for this artifact (HTTP error &#x60;404&#x60;) * Invalid rule type (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param rule: The unique name/type of a rule.
    :type rule: str

    """
    return web.Response(status=200)


async def delete_artifact_rules(request: web.Request, group_id, artifact_id) -> web.Response:
    """Delete artifact rules

    Deletes all of the rules configured for the artifact.  After this is done, the global rules apply to the artifact again.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str

    """
    return web.Response(status=200)


async def get_artifact_rule_config(request: web.Request, group_id, artifact_id, rule) -> web.Response:
    """Get artifact rule configuration

    Returns information about a single rule configured for an artifact.  This is useful when you want to know what the current configuration settings are for a specific rule.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No rule with this name/type is configured for this artifact (HTTP error &#x60;404&#x60;) * Invalid rule type (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param rule: The unique name/type of a rule.
    :type rule: str

    """
    return web.Response(status=200)


async def list_artifact_rules(request: web.Request, group_id, artifact_id) -> web.Response:
    """List artifact rules

    Returns a list of all rules configured for the artifact.  The set of rules determines how the content of an artifact can evolve over time.  If no rules are configured for an artifact, the set of globally configured rules are used.  If no global rules  are defined, there are no restrictions on content evolution.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str

    """
    return web.Response(status=200)


async def test_update_artifact(request: web.Request, group_id, artifact_id, body) -> web.Response:
    """Test update artifact

    Tests whether an update to the artifact&#39;s content *would* succeed for the provided content. Ultimately, this applies any rules configured for the artifact against the given content to determine whether the rules would pass or fail, but without actually updating the artifact content.  The body of the request should be the raw content of the artifact.  This is typically in  JSON format for *most* of the supported types, but may be in another format for a few  (for example, &#x60;PROTOBUF&#x60;).  The update could fail for a number of reasons including:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * The new content violates one of the rules configured for the artifact (HTTP error &#x60;409&#x60;) * The provided artifact type is not recognized (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)  When successful, this operation simply returns a *No Content* response.  This response indicates that the content is valid against the configured content rules for the  artifact (or the global rules if no artifact rules are enabled).

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param body: The content of the artifact being tested. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;) 
    :type body: str

    """
    return web.Response(status=200)


async def update_artifact_rule_config(request: web.Request, group_id, artifact_id, rule, body) -> web.Response:
    """Update artifact rule configuration

    Updates the configuration of a single rule for the artifact.  The configuration data is specific to each rule type, so the configuration of the &#x60;COMPATIBILITY&#x60; rule  is in a different format from the configuration of the &#x60;VALIDITY&#x60; rule.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No rule with this name/type is configured for this artifact (HTTP error &#x60;404&#x60;) * Invalid rule type (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param rule: The unique name/type of a rule.
    :type rule: str
    :param body: 
    :type body: dict | bytes

    """
    body = Rule.from_dict(body)
    return web.Response(status=200)

from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_bot_alias_response import GetBotAliasResponse
from openapi_server.models.get_bot_aliases_response import GetBotAliasesResponse
from openapi_server.models.get_bot_channel_association_response import GetBotChannelAssociationResponse
from openapi_server.models.get_bot_channel_associations_response import GetBotChannelAssociationsResponse
from openapi_server.models.get_bot_response import GetBotResponse
from openapi_server.models.get_bot_versions_response import GetBotVersionsResponse
from openapi_server.models.get_bots_response import GetBotsResponse
from openapi_server.models.get_builtin_intent_response import GetBuiltinIntentResponse
from openapi_server.models.get_builtin_intents_response import GetBuiltinIntentsResponse
from openapi_server.models.get_builtin_slot_types_response import GetBuiltinSlotTypesResponse
from openapi_server.models.get_export_response import GetExportResponse
from openapi_server.models.get_import_response import GetImportResponse
from openapi_server.models.get_intent_response import GetIntentResponse
from openapi_server.models.get_intent_versions_response import GetIntentVersionsResponse
from openapi_server.models.get_intents_response import GetIntentsResponse
from openapi_server.models.get_migration_response import GetMigrationResponse
from openapi_server.models.get_migrations_response import GetMigrationsResponse
from openapi_server.models.get_slot_type_response import GetSlotTypeResponse
from openapi_server.models.get_slot_type_versions_response import GetSlotTypeVersionsResponse
from openapi_server.models.get_slot_types_response import GetSlotTypesResponse
from openapi_server.models.get_utterances_view_response import GetUtterancesViewResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_bot_alias_request import PutBotAliasRequest
from openapi_server.models.put_bot_alias_response import PutBotAliasResponse
from openapi_server.models.put_bot_request import PutBotRequest
from openapi_server.models.put_bot_response import PutBotResponse
from openapi_server.models.put_intent_request import PutIntentRequest
from openapi_server.models.put_intent_response import PutIntentResponse
from openapi_server.models.put_slot_type_request import PutSlotTypeRequest
from openapi_server.models.put_slot_type_response import PutSlotTypeResponse
from openapi_server.models.start_import_request import StartImportRequest
from openapi_server.models.start_import_response import StartImportResponse
from openapi_server.models.start_migration_request import StartMigrationRequest
from openapi_server.models.start_migration_response import StartMigrationResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server import util


async def delete_bot(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_bot

    &lt;p&gt;Deletes all versions of the bot, including the &lt;code&gt;$LATEST&lt;/code&gt; version. To delete a specific version of the bot, use the &lt;a&gt;DeleteBotVersion&lt;/a&gt; operation. The &lt;code&gt;DeleteBot&lt;/code&gt; operation doesn&#39;t immediately remove the bot schema. Instead, it is marked for deletion and removed later.&lt;/p&gt; &lt;p&gt;Amazon Lex stores utterances indefinitely for improving the ability of your bot to respond to user inputs. These utterances are not removed when the bot is deleted. To remove the utterances, use the &lt;a&gt;DeleteUtterances&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;If a bot has an alias, you can&#39;t delete it. Instead, the &lt;code&gt;DeleteBot&lt;/code&gt; operation returns a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception that includes a reference to the alias that refers to the bot. To remove the reference to the bot, delete the alias. If you get the same exception again, delete the referring alias until the &lt;code&gt;DeleteBot&lt;/code&gt; operation is successful.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteBot&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the bot. The name is case sensitive. 
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_bot_alias(request: web.Request, name, bot_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_bot_alias

    &lt;p&gt;Deletes an alias for the specified bot. &lt;/p&gt; &lt;p&gt;You can&#39;t delete an alias that is used in the association between a bot and a messaging channel. If an alias is used in a channel association, the &lt;code&gt;DeleteBot&lt;/code&gt; operation returns a &lt;code&gt;ResourceInUseException&lt;/code&gt; exception that includes a reference to the channel association that refers to the bot. You can remove the reference to the alias by deleting the channel association. If you get the same exception again, delete the referring association until the &lt;code&gt;DeleteBotAlias&lt;/code&gt; operation is successful.&lt;/p&gt;

    :param name: The name of the alias to delete. The name is case sensitive. 
    :type name: str
    :param bot_name: The name of the bot that the alias points to.
    :type bot_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_bot_channel_association(request: web.Request, name, bot_name, alias_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_bot_channel_association

    &lt;p&gt;Deletes the association between an Amazon Lex bot and a messaging platform.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:DeleteBotChannelAssociation&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the association. The name is case sensitive. 
    :type name: str
    :param bot_name: The name of the Amazon Lex bot.
    :type bot_name: str
    :param alias_name: An alias that points to the specific version of the Amazon Lex bot to which this association is being made.
    :type alias_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_bot_version(request: web.Request, name, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_bot_version

    &lt;p&gt;Deletes a specific version of a bot. To delete all versions of a bot, use the &lt;a&gt;DeleteBot&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteBotVersion&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the bot.
    :type name: str
    :param version: The version of the bot to delete. You cannot delete the &lt;code&gt;$LATEST&lt;/code&gt; version of the bot. To delete the &lt;code&gt;$LATEST&lt;/code&gt; version, use the &lt;a&gt;DeleteBot&lt;/a&gt; operation.
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_intent(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_intent

    &lt;p&gt;Deletes all versions of the intent, including the &lt;code&gt;$LATEST&lt;/code&gt; version. To delete a specific version of the intent, use the &lt;a&gt;DeleteIntentVersion&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt; You can delete a version of an intent only if it is not referenced. To delete an intent that is referred to in one or more bots (see &lt;a&gt;how-it-works&lt;/a&gt;), you must remove those references first. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you get the &lt;code&gt;ResourceInUseException&lt;/code&gt; exception, it provides an example reference that shows where the intent is referenced. To remove the reference to the intent, either update the bot or delete it. If you get the same exception when you attempt to delete the intent again, repeat until the intent has no references and the call to &lt;code&gt;DeleteIntent&lt;/code&gt; is successful. &lt;/p&gt; &lt;/note&gt; &lt;p&gt; This operation requires permission for the &lt;code&gt;lex:DeleteIntent&lt;/code&gt; action. &lt;/p&gt;

    :param name: The name of the intent. The name is case sensitive. 
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_intent_version(request: web.Request, name, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_intent_version

    &lt;p&gt;Deletes a specific version of an intent. To delete all versions of a intent, use the &lt;a&gt;DeleteIntent&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteIntentVersion&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the intent.
    :type name: str
    :param version: The version of the intent to delete. You cannot delete the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent. To delete the &lt;code&gt;$LATEST&lt;/code&gt; version, use the &lt;a&gt;DeleteIntent&lt;/a&gt; operation.
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_slot_type(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_slot_type

    &lt;p&gt;Deletes all versions of the slot type, including the &lt;code&gt;$LATEST&lt;/code&gt; version. To delete a specific version of the slot type, use the &lt;a&gt;DeleteSlotTypeVersion&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt; You can delete a version of a slot type only if it is not referenced. To delete a slot type that is referred to in one or more intents, you must remove those references first. &lt;/p&gt; &lt;note&gt; &lt;p&gt; If you get the &lt;code&gt;ResourceInUseException&lt;/code&gt; exception, the exception provides an example reference that shows the intent where the slot type is referenced. To remove the reference to the slot type, either update the intent or delete it. If you get the same exception when you attempt to delete the slot type again, repeat until the slot type has no references and the &lt;code&gt;DeleteSlotType&lt;/code&gt; call is successful. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:DeleteSlotType&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the slot type. The name is case sensitive. 
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_slot_type_version(request: web.Request, name, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_slot_type_version

    &lt;p&gt;Deletes a specific version of a slot type. To delete all versions of a slot type, use the &lt;a&gt;DeleteSlotType&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteSlotTypeVersion&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the slot type.
    :type name: str
    :param version: The version of the slot type to delete. You cannot delete the &lt;code&gt;$LATEST&lt;/code&gt; version of the slot type. To delete the &lt;code&gt;$LATEST&lt;/code&gt; version, use the &lt;a&gt;DeleteSlotType&lt;/a&gt; operation.
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_utterances(request: web.Request, bot_name, user_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_utterances

    &lt;p&gt;Deletes stored utterances.&lt;/p&gt; &lt;p&gt;Amazon Lex stores the utterances that users send to your bot. Utterances are stored for 15 days for use with the &lt;a&gt;GetUtterancesView&lt;/a&gt; operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation to manually delete stored utterances for a specific user. When you use the &lt;code&gt;DeleteUtterances&lt;/code&gt; operation, utterances stored for improving your bot&#39;s ability to respond to user input are deleted immediately. Utterances stored for use with the &lt;code&gt;GetUtterancesView&lt;/code&gt; operation are deleted after 15 days.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:DeleteUtterances&lt;/code&gt; action.&lt;/p&gt;

    :param bot_name: The name of the bot that stored the utterances.
    :type bot_name: str
    :param user_id:  The unique identifier for the user that made the utterances. This is the user ID that was sent in the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html\&quot;&gt;PostContent&lt;/a&gt; or &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html\&quot;&gt;PostText&lt;/a&gt; operation request that contained the utterance.
    :type user_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_bot(request: web.Request, name, versionoralias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_bot

    &lt;p&gt;Returns metadata information for a specific bot. You must provide the bot name and the bot version or alias. &lt;/p&gt; &lt;p&gt; This operation requires permissions for the &lt;code&gt;lex:GetBot&lt;/code&gt; action. &lt;/p&gt;

    :param name: The name of the bot. The name is case sensitive. 
    :type name: str
    :param versionoralias: The version or alias of the bot.
    :type versionoralias: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_bot_alias(request: web.Request, name, bot_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_bot_alias

    &lt;p&gt;Returns information about an Amazon Lex bot alias. For more information about aliases, see &lt;a&gt;versioning-aliases&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotAlias&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the bot alias. The name is case sensitive.
    :type name: str
    :param bot_name: The name of the bot.
    :type bot_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_bot_aliases(request: web.Request, bot_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, name_contains=None) -> web.Response:
    """get_bot_aliases

    &lt;p&gt;Returns a list of aliases for a specified Amazon Lex bot.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotAliases&lt;/code&gt; action.&lt;/p&gt;

    :param bot_name: The name of the bot.
    :type bot_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A pagination token for fetching the next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request. 
    :type next_token: str
    :param max_results: The maximum number of aliases to return in the response. The default is 50. . 
    :type max_results: int
    :param name_contains: Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot;
    :type name_contains: str

    """
    return web.Response(status=200)


async def get_bot_channel_association(request: web.Request, name, bot_name, alias_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_bot_channel_association

    &lt;p&gt;Returns information about the association between an Amazon Lex bot and a messaging platform.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotChannelAssociation&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the association between the bot and the channel. The name is case sensitive. 
    :type name: str
    :param bot_name: The name of the Amazon Lex bot.
    :type bot_name: str
    :param alias_name: An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.
    :type alias_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_bot_channel_associations(request: web.Request, bot_name, alias_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, name_contains=None) -> web.Response:
    """get_bot_channel_associations

    &lt;p&gt; Returns a list of all of the channels associated with the specified bot. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetBotChannelAssociations&lt;/code&gt; operation requires permissions for the &lt;code&gt;lex:GetBotChannelAssociations&lt;/code&gt; action.&lt;/p&gt;

    :param bot_name: The name of the Amazon Lex bot in the association.
    :type bot_name: str
    :param alias_name: An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.
    :type alias_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A pagination token for fetching the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request. 
    :type next_token: str
    :param max_results: The maximum number of associations to return in the response. The default is 50. 
    :type max_results: int
    :param name_contains: Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; To return all bot channel associations, use a hyphen (\&quot;-\&quot;) as the &lt;code&gt;nameContains&lt;/code&gt; parameter.
    :type name_contains: str

    """
    return web.Response(status=200)


async def get_bot_versions(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """get_bot_versions

    &lt;p&gt;Gets information about all of the versions of a bot.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetBotVersions&lt;/code&gt; operation returns a &lt;code&gt;BotMetadata&lt;/code&gt; object for each version of a bot. For example, if a bot has three numbered versions, the &lt;code&gt;GetBotVersions&lt;/code&gt; operation returns four &lt;code&gt;BotMetadata&lt;/code&gt; objects in the response, one for each numbered version and one for the &lt;code&gt;$LATEST&lt;/code&gt; version. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetBotVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetBotVersions&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the bot for which versions should be returned.
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 
    :type next_token: str
    :param max_results: The maximum number of bot versions to return in the response. The default is 10.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_bots(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, name_contains=None) -> web.Response:
    """get_bots

    &lt;p&gt;Returns bot information as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you provide the &lt;code&gt;nameContains&lt;/code&gt; field, the response includes information for the &lt;code&gt;$LATEST&lt;/code&gt; version of all bots whose name contains the specified string.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you don&#39;t specify the &lt;code&gt;nameContains&lt;/code&gt; field, the operation returns information about the &lt;code&gt;$LATEST&lt;/code&gt; version of all of your bots.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBots&lt;/code&gt; action.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A pagination token that fetches the next page of bots. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of bots, specify the pagination token in the next request. 
    :type next_token: str
    :param max_results: The maximum number of bots to return in the response that the request will return. The default is 10.
    :type max_results: int
    :param name_contains: Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot;
    :type name_contains: str

    """
    return web.Response(status=200)


async def get_builtin_intent(request: web.Request, signature, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_builtin_intent

    &lt;p&gt;Returns information about a built-in intent.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBuiltinIntent&lt;/code&gt; action.&lt;/p&gt;

    :param signature: The unique identifier for a built-in intent. To find the signature for an intent, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\&quot;&gt;Standard Built-in Intents&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.
    :type signature: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_builtin_intents(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, locale=None, signature_contains=None, next_token=None, max_results=None) -> web.Response:
    """get_builtin_intents

    &lt;p&gt;Gets a list of built-in intents that meet the specified criteria.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBuiltinIntents&lt;/code&gt; action.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param locale: A list of locales that the intent supports.
    :type locale: str
    :param signature_contains: Substring to match in built-in intent signatures. An intent will be returned if any part of its signature matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot; To find the signature for an intent, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\&quot;&gt;Standard Built-in Intents&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.
    :type signature_contains: str
    :param next_token: A pagination token that fetches the next page of intents. If this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, use the pagination token in the next request.
    :type next_token: str
    :param max_results: The maximum number of intents to return in the response. The default is 10.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_builtin_slot_types(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, locale=None, signature_contains=None, next_token=None, max_results=None) -> web.Response:
    """get_builtin_slot_types

    &lt;p&gt;Gets a list of built-in slot types that meet the specified criteria.&lt;/p&gt; &lt;p&gt;For a list of built-in slot types, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference\&quot;&gt;Slot Type Reference&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;lex:GetBuiltInSlotTypes&lt;/code&gt; action.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param locale: A list of locales that the slot type supports.
    :type locale: str
    :param signature_contains: Substring to match in built-in slot type signatures. A slot type will be returned if any part of its signature matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot;
    :type signature_contains: str
    :param next_token: A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of slot types, specify the pagination token in the next request.
    :type next_token: str
    :param max_results: The maximum number of slot types to return in the response. The default is 10.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_export(request: web.Request, name, version, resource_type, export_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_export

    Exports the contents of a Amazon Lex resource in a specified format. 

    :param name: The name of the bot to export.
    :type name: str
    :param version: The version of the bot to export.
    :type version: str
    :param resource_type: The type of resource to export. 
    :type resource_type: str
    :param export_type: The format of the exported data.
    :type export_type: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_import(request: web.Request, import_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_import

    Gets information about an import job started with the &lt;code&gt;StartImport&lt;/code&gt; operation.

    :param import_id: The identifier of the import job information to return.
    :type import_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_intent(request: web.Request, name, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_intent

    &lt;p&gt; Returns information about an intent. In addition to the intent name, you must specify the intent version. &lt;/p&gt; &lt;p&gt; This operation requires permissions to perform the &lt;code&gt;lex:GetIntent&lt;/code&gt; action. &lt;/p&gt;

    :param name: The name of the intent. The name is case sensitive. 
    :type name: str
    :param version: The version of the intent.
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_intent_versions(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """get_intent_versions

    &lt;p&gt;Gets information about all of the versions of an intent.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetIntentVersions&lt;/code&gt; operation returns an &lt;code&gt;IntentMetadata&lt;/code&gt; object for each version of an intent. For example, if an intent has three numbered versions, the &lt;code&gt;GetIntentVersions&lt;/code&gt; operation returns four &lt;code&gt;IntentMetadata&lt;/code&gt; objects in the response, one for each numbered version and one for the &lt;code&gt;$LATEST&lt;/code&gt; version. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetIntentVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetIntentVersions&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the intent for which versions should be returned.
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 
    :type next_token: str
    :param max_results: The maximum number of intent versions to return in the response. The default is 10.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_intents(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, name_contains=None) -> web.Response:
    """get_intents

    &lt;p&gt;Returns intent information as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns the &lt;code&gt;$LATEST&lt;/code&gt; version of all intents that contain the specified string.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If you don&#39;t specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns information about the &lt;code&gt;$LATEST&lt;/code&gt; version of all intents. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; The operation requires permission for the &lt;code&gt;lex:GetIntents&lt;/code&gt; action. &lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request. 
    :type next_token: str
    :param max_results: The maximum number of intents to return in the response. The default is 10.
    :type max_results: int
    :param name_contains: Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot;
    :type name_contains: str

    """
    return web.Response(status=200)


async def get_migration(request: web.Request, migration_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_migration

    Provides details about an ongoing or complete migration from an Amazon Lex V1 bot to an Amazon Lex V2 bot. Use this operation to view the migration alerts and warnings related to the migration.

    :param migration_id: The unique identifier of the migration to view. The &lt;code&gt;migrationID&lt;/code&gt; is returned by the operation.
    :type migration_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_migrations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sort_by_attribute=None, sort_by_order=None, v1_bot_name_contains=None, migration_status_equals=None, max_results=None, next_token=None) -> web.Response:
    """get_migrations

    Gets a list of migrations between Amazon Lex V1 and Amazon Lex V2.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sort_by_attribute: The field to sort the list of migrations by. You can sort by the Amazon Lex V1 bot name or the date and time that the migration was started.
    :type sort_by_attribute: str
    :param sort_by_order: The order so sort the list.
    :type sort_by_order: str
    :param v1_bot_name_contains: Filters the list to contain only bots whose name contains the specified string. The string is matched anywhere in bot name.
    :type v1_bot_name_contains: str
    :param migration_status_equals: Filters the list to contain only migrations in the specified state.
    :type migration_status_equals: str
    :param max_results: The maximum number of migrations to return in the response. The default is 10.
    :type max_results: int
    :param next_token: A pagination token that fetches the next page of migrations. If the response to this operation is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of migrations, specify the pagination token in the request.
    :type next_token: str

    """
    return web.Response(status=200)


async def get_slot_type(request: web.Request, name, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_slot_type

    &lt;p&gt;Returns information about a specific version of a slot type. In addition to specifying the slot type name, you must specify the slot type version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetSlotType&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the slot type. The name is case sensitive. 
    :type name: str
    :param version: The version of the slot type. 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_slot_type_versions(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """get_slot_type_versions

    &lt;p&gt;Gets information about all versions of a slot type.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetSlotTypeVersions&lt;/code&gt; operation returns a &lt;code&gt;SlotTypeMetadata&lt;/code&gt; object for each version of a slot type. For example, if a slot type has three numbered versions, the &lt;code&gt;GetSlotTypeVersions&lt;/code&gt; operation returns four &lt;code&gt;SlotTypeMetadata&lt;/code&gt; objects in the response, one for each numbered version and one for the &lt;code&gt;$LATEST&lt;/code&gt; version. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetSlotTypeVersions&lt;/code&gt; operation always returns at least one version, the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetSlotTypeVersions&lt;/code&gt; action.&lt;/p&gt;

    :param name: The name of the slot type for which versions should be returned.
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 
    :type next_token: str
    :param max_results: The maximum number of slot type versions to return in the response. The default is 10.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_slot_types(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, name_contains=None) -> web.Response:
    """get_slot_types

    &lt;p&gt;Returns slot type information as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns the &lt;code&gt;$LATEST&lt;/code&gt; version of all slot types that contain the specified string.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; If you don&#39;t specify the &lt;code&gt;nameContains&lt;/code&gt; field, returns information about the &lt;code&gt;$LATEST&lt;/code&gt; version of all slot types. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; The operation requires permission for the &lt;code&gt;lex:GetSlotTypes&lt;/code&gt; action. &lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch next page of slot types, specify the pagination token in the next request.
    :type next_token: str
    :param max_results: The maximum number of slot types to return in the response. The default is 10.
    :type max_results: int
    :param name_contains: Substring to match in slot type names. A slot type will be returned if any part of its name matches the substring. For example, \&quot;xyz\&quot; matches both \&quot;xyzabc\&quot; and \&quot;abcxyz.\&quot;
    :type name_contains: str

    """
    return web.Response(status=200)


async def get_utterances_view(request: web.Request, botname, bot_versions, status_type, view, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_utterances_view

    &lt;p&gt;Use the &lt;code&gt;GetUtterancesView&lt;/code&gt; operation to get information about the utterances that your users have made to your bot. You can use this list to tune the utterances that your bot responds to.&lt;/p&gt; &lt;p&gt;For example, say that you have created a bot to order flowers. After your users have used your bot for a while, use the &lt;code&gt;GetUtterancesView&lt;/code&gt; operation to see the requests that they have made and whether they have been successful. You might find that the utterance \&quot;I want flowers\&quot; is not being recognized. You could add this utterance to the &lt;code&gt;OrderFlowers&lt;/code&gt; intent so that your bot recognizes that utterance.&lt;/p&gt; &lt;p&gt;After you publish a new version of a bot, you can get information about the old version and the new so that you can compare the performance across the two versions. &lt;/p&gt; &lt;p&gt;Utterance statistics are generated once a day. Data is available for the last 15 days. You can request information for up to 5 versions of your bot in each request. Amazon Lex returns the most frequent utterances received by the bot in the last 15 days. The response contains information about a maximum of 100 utterances for each version.&lt;/p&gt; &lt;p&gt;If you set &lt;code&gt;childDirected&lt;/code&gt; field to true when you created your bot, if you are using slot obfuscation with one or more slots, or if you opted out of participating in improving Amazon Lex, utterances are not available.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:GetUtterancesView&lt;/code&gt; action.&lt;/p&gt;

    :param botname: The name of the bot for which utterance information should be returned.
    :type botname: str
    :param bot_versions: An array of bot versions for which utterance information should be returned. The limit is 5 versions per request.
    :type bot_versions: List[str]
    :param status_type: To return utterances that were recognized and handled, use &lt;code&gt;Detected&lt;/code&gt;. To return utterances that were not recognized, use &lt;code&gt;Missed&lt;/code&gt;.
    :type status_type: str
    :param view: 
    :type view: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Gets a list of tags associated with the specified resource. Only bots, bot aliases, and bot channels can have tags associated with them.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to get a list of tags for.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def put_bot(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_bot

    &lt;p&gt;Creates an Amazon Lex conversational bot or replaces an existing bot. When you create or update a bot you are only required to specify a name, a locale, and whether the bot is directed toward children under age 13. You can use this to add intents later, or to remove intents from an existing bot. When you create a bot with the minimum information, the bot is created or updated but Amazon Lex returns the &lt;code/&gt; response &lt;code&gt;FAILED&lt;/code&gt;. You can build the bot after you add one or more intents. For more information about Amazon Lex bots, see &lt;a&gt;how-it-works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;If you specify the name of an existing bot, the fields in the request replace the existing values in the &lt;code&gt;$LATEST&lt;/code&gt; version of the bot. Amazon Lex removes any fields that you don&#39;t provide values for in the request, except for the &lt;code&gt;idleTTLInSeconds&lt;/code&gt; and &lt;code&gt;privacySettings&lt;/code&gt; fields, which are set to their default values. If you don&#39;t specify values for required fields, Amazon Lex throws an exception.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutBot&lt;/code&gt; action. For more information, see &lt;a&gt;security-iam&lt;/a&gt;.&lt;/p&gt;

    :param name: The name of the bot. The name is &lt;i&gt;not&lt;/i&gt; case sensitive. 
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutBotRequest.from_dict(body)
    return web.Response(status=200)


async def put_bot_alias(request: web.Request, name, bot_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_bot_alias

    &lt;p&gt;Creates an alias for the specified version of the bot or replaces an alias for the specified bot. To change the version of the bot that the alias points to, replace the alias. For more information about aliases, see &lt;a&gt;versioning-aliases&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutBotAlias&lt;/code&gt; action. &lt;/p&gt;

    :param name: The name of the alias. The name is &lt;i&gt;not&lt;/i&gt; case sensitive.
    :type name: str
    :param bot_name: The name of the bot.
    :type bot_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutBotAliasRequest.from_dict(body)
    return web.Response(status=200)


async def put_intent(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_intent

    &lt;p&gt;Creates an intent or replaces an existing intent.&lt;/p&gt; &lt;p&gt;To define the interaction between the user and your bot, you use one or more intents. For a pizza ordering bot, for example, you would create an &lt;code&gt;OrderPizza&lt;/code&gt; intent. &lt;/p&gt; &lt;p&gt;To create an intent or replace an existing intent, you must provide the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Intent name. For example, &lt;code&gt;OrderPizza&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Sample utterances. For example, \&quot;Can I order a pizza, please.\&quot; and \&quot;I want to order a pizza.\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Information to be gathered. You specify slot types for the information that your bot will request from the user. You can specify standard slot types, such as a date or a time, or custom slot types such as the size and crust of a pizza.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;How the intent will be fulfilled. You can provide a Lambda function or configure the intent to return the intent information to the client application. If you use a Lambda function, when all of the intent information is available, Amazon Lex invokes your Lambda function. If you configure your intent to return the intent information to the client application. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can specify other optional information in the request, such as:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A confirmation prompt to ask the user to confirm an intent. For example, \&quot;Shall I order your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A conclusion statement to send to the user after the intent has been fulfilled. For example, \&quot;I placed your pizza order.\&quot;&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A follow-up prompt that asks the user for additional activity. For example, asking \&quot;Do you want to order a drink with your pizza?\&quot;&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you specify an existing intent name to update the intent, Amazon Lex replaces the values in the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent with the values in the request. Amazon Lex removes fields that you don&#39;t provide in the request. If you don&#39;t specify the required fields, Amazon Lex throws an exception. When you update the &lt;code&gt;$LATEST&lt;/code&gt; version of an intent, the &lt;code&gt;status&lt;/code&gt; field of any bot that uses the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent is set to &lt;code&gt;NOT_BUILT&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a&gt;how-it-works&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutIntent&lt;/code&gt; action.&lt;/p&gt;

    :param name: &lt;p&gt;The name of the intent. The name is &lt;i&gt;not&lt;/i&gt; case sensitive. &lt;/p&gt; &lt;p&gt;The name can&#39;t match a built-in intent name, or a built-in intent name with \&quot;AMAZON.\&quot; removed. For example, because there is a built-in intent called &lt;code&gt;AMAZON.HelpIntent&lt;/code&gt;, you can&#39;t create a custom intent called &lt;code&gt;HelpIntent&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For a list of built-in intents, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\&quot;&gt;Standard Built-in Intents&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.&lt;/p&gt;
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutIntentRequest.from_dict(body)
    return web.Response(status=200)


async def put_slot_type(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_slot_type

    &lt;p&gt;Creates a custom slot type or replaces an existing custom slot type.&lt;/p&gt; &lt;p&gt;To create a custom slot type, specify a name for the slot type and a set of enumeration values, which are the values that a slot of this type can assume. For more information, see &lt;a&gt;how-it-works&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you specify the name of an existing slot type, the fields in the request replace the existing values in the &lt;code&gt;$LATEST&lt;/code&gt; version of the slot type. Amazon Lex removes the fields that you don&#39;t provide in the request. If you don&#39;t specify required fields, Amazon Lex throws an exception. When you update the &lt;code&gt;$LATEST&lt;/code&gt; version of a slot type, if a bot uses the &lt;code&gt;$LATEST&lt;/code&gt; version of an intent that contains the slot type, the bot&#39;s &lt;code&gt;status&lt;/code&gt; field is set to &lt;code&gt;NOT_BUILT&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions for the &lt;code&gt;lex:PutSlotType&lt;/code&gt; action.&lt;/p&gt;

    :param name: &lt;p&gt;The name of the slot type. The name is &lt;i&gt;not&lt;/i&gt; case sensitive. &lt;/p&gt; &lt;p&gt;The name can&#39;t match a built-in slot type name, or a built-in slot type name with \&quot;AMAZON.\&quot; removed. For example, because there is a built-in slot type called &lt;code&gt;AMAZON.DATE&lt;/code&gt;, you can&#39;t create a custom slot type called &lt;code&gt;DATE&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For a list of built-in slot types, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference\&quot;&gt;Slot Type Reference&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;.&lt;/p&gt;
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutSlotTypeRequest.from_dict(body)
    return web.Response(status=200)


async def start_import(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_import

    Starts a job to import a resource to Amazon Lex.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartImportRequest.from_dict(body)
    return web.Response(status=200)


async def start_migration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_migration

    &lt;p&gt;Starts migrating a bot from Amazon Lex V1 to Amazon Lex V2. Migrate your bot when you want to take advantage of the new features of Amazon Lex V2.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/migrate.html\&quot;&gt;Migrating a bot&lt;/a&gt; in the &lt;i&gt;Amazon Lex developer guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartMigrationRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds the specified tags to the specified resource. If a tag key already exists, the existing value is replaced with the new value.

    :param resource_arn: The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes tags from a bot, bot alias or bot channel.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to remove the tags from.
    :type resource_arn: str
    :param tag_keys: A list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)

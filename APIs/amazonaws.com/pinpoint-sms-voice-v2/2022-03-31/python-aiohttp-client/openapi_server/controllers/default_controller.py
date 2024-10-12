from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_origination_identity_request import AssociateOriginationIdentityRequest
from openapi_server.models.associate_origination_identity_result import AssociateOriginationIdentityResult
from openapi_server.models.create_configuration_set_request import CreateConfigurationSetRequest
from openapi_server.models.create_configuration_set_result import CreateConfigurationSetResult
from openapi_server.models.create_event_destination_request import CreateEventDestinationRequest
from openapi_server.models.create_event_destination_result import CreateEventDestinationResult
from openapi_server.models.create_opt_out_list_request import CreateOptOutListRequest
from openapi_server.models.create_opt_out_list_result import CreateOptOutListResult
from openapi_server.models.create_pool_request import CreatePoolRequest
from openapi_server.models.create_pool_result import CreatePoolResult
from openapi_server.models.delete_configuration_set_request import DeleteConfigurationSetRequest
from openapi_server.models.delete_configuration_set_result import DeleteConfigurationSetResult
from openapi_server.models.delete_default_message_type_request import DeleteDefaultMessageTypeRequest
from openapi_server.models.delete_default_message_type_result import DeleteDefaultMessageTypeResult
from openapi_server.models.delete_default_sender_id_request import DeleteDefaultSenderIdRequest
from openapi_server.models.delete_default_sender_id_result import DeleteDefaultSenderIdResult
from openapi_server.models.delete_event_destination_request import DeleteEventDestinationRequest
from openapi_server.models.delete_event_destination_result import DeleteEventDestinationResult
from openapi_server.models.delete_keyword_request import DeleteKeywordRequest
from openapi_server.models.delete_keyword_result import DeleteKeywordResult
from openapi_server.models.delete_opt_out_list_request import DeleteOptOutListRequest
from openapi_server.models.delete_opt_out_list_result import DeleteOptOutListResult
from openapi_server.models.delete_opted_out_number_request import DeleteOptedOutNumberRequest
from openapi_server.models.delete_opted_out_number_result import DeleteOptedOutNumberResult
from openapi_server.models.delete_pool_request import DeletePoolRequest
from openapi_server.models.delete_pool_result import DeletePoolResult
from openapi_server.models.delete_text_message_spend_limit_override_result import DeleteTextMessageSpendLimitOverrideResult
from openapi_server.models.delete_voice_message_spend_limit_override_result import DeleteVoiceMessageSpendLimitOverrideResult
from openapi_server.models.describe_account_attributes_request import DescribeAccountAttributesRequest
from openapi_server.models.describe_account_attributes_result import DescribeAccountAttributesResult
from openapi_server.models.describe_account_limits_request import DescribeAccountLimitsRequest
from openapi_server.models.describe_account_limits_result import DescribeAccountLimitsResult
from openapi_server.models.describe_configuration_sets_request import DescribeConfigurationSetsRequest
from openapi_server.models.describe_configuration_sets_result import DescribeConfigurationSetsResult
from openapi_server.models.describe_keywords_request import DescribeKeywordsRequest
from openapi_server.models.describe_keywords_result import DescribeKeywordsResult
from openapi_server.models.describe_opt_out_lists_request import DescribeOptOutListsRequest
from openapi_server.models.describe_opt_out_lists_result import DescribeOptOutListsResult
from openapi_server.models.describe_opted_out_numbers_request import DescribeOptedOutNumbersRequest
from openapi_server.models.describe_opted_out_numbers_result import DescribeOptedOutNumbersResult
from openapi_server.models.describe_phone_numbers_request import DescribePhoneNumbersRequest
from openapi_server.models.describe_phone_numbers_result import DescribePhoneNumbersResult
from openapi_server.models.describe_pools_request import DescribePoolsRequest
from openapi_server.models.describe_pools_result import DescribePoolsResult
from openapi_server.models.describe_sender_ids_request import DescribeSenderIdsRequest
from openapi_server.models.describe_sender_ids_result import DescribeSenderIdsResult
from openapi_server.models.describe_spend_limits_request import DescribeSpendLimitsRequest
from openapi_server.models.describe_spend_limits_result import DescribeSpendLimitsResult
from openapi_server.models.disassociate_origination_identity_request import DisassociateOriginationIdentityRequest
from openapi_server.models.disassociate_origination_identity_result import DisassociateOriginationIdentityResult
from openapi_server.models.list_pool_origination_identities_request import ListPoolOriginationIdentitiesRequest
from openapi_server.models.list_pool_origination_identities_result import ListPoolOriginationIdentitiesResult
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_result import ListTagsForResourceResult
from openapi_server.models.put_keyword_request import PutKeywordRequest
from openapi_server.models.put_keyword_result import PutKeywordResult
from openapi_server.models.put_opted_out_number_request import PutOptedOutNumberRequest
from openapi_server.models.put_opted_out_number_result import PutOptedOutNumberResult
from openapi_server.models.release_phone_number_request import ReleasePhoneNumberRequest
from openapi_server.models.release_phone_number_result import ReleasePhoneNumberResult
from openapi_server.models.request_phone_number_request import RequestPhoneNumberRequest
from openapi_server.models.request_phone_number_result import RequestPhoneNumberResult
from openapi_server.models.send_text_message_request import SendTextMessageRequest
from openapi_server.models.send_text_message_result import SendTextMessageResult
from openapi_server.models.send_voice_message_request import SendVoiceMessageRequest
from openapi_server.models.send_voice_message_result import SendVoiceMessageResult
from openapi_server.models.set_default_message_type_request import SetDefaultMessageTypeRequest
from openapi_server.models.set_default_message_type_result import SetDefaultMessageTypeResult
from openapi_server.models.set_default_sender_id_request import SetDefaultSenderIdRequest
from openapi_server.models.set_default_sender_id_result import SetDefaultSenderIdResult
from openapi_server.models.set_text_message_spend_limit_override_request import SetTextMessageSpendLimitOverrideRequest
from openapi_server.models.set_text_message_spend_limit_override_result import SetTextMessageSpendLimitOverrideResult
from openapi_server.models.set_voice_message_spend_limit_override_request import SetVoiceMessageSpendLimitOverrideRequest
from openapi_server.models.set_voice_message_spend_limit_override_result import SetVoiceMessageSpendLimitOverrideResult
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_event_destination_request import UpdateEventDestinationRequest
from openapi_server.models.update_event_destination_result import UpdateEventDestinationResult
from openapi_server.models.update_phone_number_request import UpdatePhoneNumberRequest
from openapi_server.models.update_phone_number_result import UpdatePhoneNumberResult
from openapi_server.models.update_pool_request import UpdatePoolRequest
from openapi_server.models.update_pool_result import UpdatePoolResult
from openapi_server import util


async def associate_origination_identity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_origination_identity

    &lt;p&gt;Associates the specified origination identity with a pool.&lt;/p&gt; &lt;p&gt;If the origination identity is a phone number and is already associated with another pool, an Error is returned. A sender ID can be associated with multiple pools.&lt;/p&gt; &lt;p&gt;If the origination identity configuration doesn&#39;t match the pool&#39;s configuration, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = AssociateOriginationIdentityRequest.from_dict(body)
    return web.Response(status=200)


async def create_configuration_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_configuration_set

    &lt;p&gt;Creates a new configuration set. After you create the configuration set, you can add one or more event destinations to it.&lt;/p&gt; &lt;p&gt;A configuration set is a set of rules that you apply to the SMS and voice messages that you send.&lt;/p&gt; &lt;p&gt;When you send a message, you can optionally specify a single configuration set.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateConfigurationSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_event_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_event_destination

    &lt;p&gt;Creates a new event destination in a configuration set.&lt;/p&gt; &lt;p&gt;An event destination is a location where you send message events. The event options are Amazon CloudWatch, Amazon Kinesis Data Firehose, or Amazon SNS. For example, when a message is delivered successfully, you can send information about that event to an event destination, or send notifications to endpoints that are subscribed to an Amazon SNS topic.&lt;/p&gt; &lt;p&gt;Each configuration set can contain between 0 and 5 event destinations. Each event destination can contain a reference to a single destination, such as a CloudWatch or Kinesis Data Firehose destination.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateEventDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def create_opt_out_list(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_opt_out_list

    &lt;p&gt;Creates a new opt-out list.&lt;/p&gt; &lt;p&gt;If the opt-out list name already exists, an Error is returned.&lt;/p&gt; &lt;p&gt;An opt-out list is a list of phone numbers that are opted out, meaning you can&#39;t send SMS or voice messages to them. If end user replies with the keyword \&quot;STOP,\&quot; an entry for the phone number is added to the opt-out list. In addition to STOP, your recipients can use any supported opt-out keyword, such as CANCEL or OPTOUT. For a list of supported opt-out keywords, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-manage.html#channels-sms-manage-optout\&quot;&gt; SMS opt out &lt;/a&gt; in the &lt;i&gt;Amazon Pinpoint User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateOptOutListRequest.from_dict(body)
    return web.Response(status=200)


async def create_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_pool

    &lt;p&gt;Creates a new pool and associates the specified origination identity to the pool. A pool can include one or more phone numbers and SenderIds that are associated with your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;The new pool inherits its configuration from the specified origination identity. This includes keywords, message type, opt-out list, two-way configuration, and self-managed opt-out configuration. Deletion protection isn&#39;t inherited from the origination identity and defaults to false.&lt;/p&gt; &lt;p&gt;If the origination identity is a phone number and is already associated with another pool, an Error is returned. A sender ID can be associated with multiple pools.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreatePoolRequest.from_dict(body)
    return web.Response(status=200)


async def delete_configuration_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_configuration_set

    &lt;p&gt;Deletes an existing configuration set.&lt;/p&gt; &lt;p&gt;A configuration set is a set of rules that you apply to voice and SMS messages that you send. In a configuration set, you can specify a destination for specific types of events related to voice and SMS messages. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteConfigurationSetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_default_message_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_default_message_type

    &lt;p&gt;Deletes an existing default message type on a configuration set.&lt;/p&gt; &lt;p&gt; A message type is a type of messages that you plan to send. If you send account-related messages or time-sensitive messages such as one-time passcodes, choose &lt;b&gt;Transactional&lt;/b&gt;. If you plan to send messages that contain marketing material or other promotional content, choose &lt;b&gt;Promotional&lt;/b&gt;. This setting applies to your entire Amazon Web Services account. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteDefaultMessageTypeRequest.from_dict(body)
    return web.Response(status=200)


async def delete_default_sender_id(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_default_sender_id

    &lt;p&gt;Deletes an existing default sender ID on a configuration set.&lt;/p&gt; &lt;p&gt;A default sender ID is the identity that appears on recipients&#39; devices when they receive SMS messages. Support for sender ID capabilities varies by country or region.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteDefaultSenderIdRequest.from_dict(body)
    return web.Response(status=200)


async def delete_event_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_event_destination

    &lt;p&gt;Deletes an existing event destination.&lt;/p&gt; &lt;p&gt;An event destination is a location where you send response information about the messages that you send. For example, when a message is delivered successfully, you can send information about that event to an Amazon CloudWatch destination, or send notifications to endpoints that are subscribed to an Amazon SNS topic.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteEventDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_keyword(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_keyword

    &lt;p&gt;Deletes an existing keyword from an origination phone number or pool.&lt;/p&gt; &lt;p&gt;A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, Amazon Pinpoint responds with a customizable message.&lt;/p&gt; &lt;p&gt;Keywords \&quot;HELP\&quot; and \&quot;STOP\&quot; can&#39;t be deleted or modified.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteKeywordRequest.from_dict(body)
    return web.Response(status=200)


async def delete_opt_out_list(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_opt_out_list

    &lt;p&gt;Deletes an existing opt-out list. All opted out phone numbers in the opt-out list are deleted.&lt;/p&gt; &lt;p&gt;If the specified opt-out list name doesn&#39;t exist or is in-use by an origination phone number or pool, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteOptOutListRequest.from_dict(body)
    return web.Response(status=200)


async def delete_opted_out_number(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_opted_out_number

    &lt;p&gt;Deletes an existing opted out destination phone number from the specified opt-out list.&lt;/p&gt; &lt;p&gt;Each destination phone number can only be deleted once every 30 days.&lt;/p&gt; &lt;p&gt;If the specified destination phone number doesn&#39;t exist or if the opt-out list doesn&#39;t exist, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteOptedOutNumberRequest.from_dict(body)
    return web.Response(status=200)


async def delete_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_pool

    &lt;p&gt;Deletes an existing pool. Deleting a pool disassociates all origination identities from that pool.&lt;/p&gt; &lt;p&gt;If the pool status isn&#39;t active or if deletion protection is enabled, an Error is returned.&lt;/p&gt; &lt;p&gt;A pool is a collection of phone numbers and SenderIds. A pool can include one or more phone numbers and SenderIds that are associated with your Amazon Web Services account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeletePoolRequest.from_dict(body)
    return web.Response(status=200)


async def delete_text_message_spend_limit_override(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_text_message_spend_limit_override

    Deletes an account-level monthly spending limit override for sending text messages. Deleting a spend limit override will set the &lt;code&gt;EnforcedLimit&lt;/code&gt; to equal the &lt;code&gt;MaxLimit&lt;/code&gt;, which is controlled by Amazon Web Services. For more information on spend limits (quotas) see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/quotas.html\&quot;&gt;Amazon Pinpoint quotas &lt;/a&gt; in the &lt;i&gt;Amazon Pinpoint Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
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


async def delete_voice_message_spend_limit_override(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_voice_message_spend_limit_override

    Deletes an account level monthly spend limit override for sending voice messages. Deleting a spend limit override sets the &lt;code&gt;EnforcedLimit&lt;/code&gt; equal to the &lt;code&gt;MaxLimit&lt;/code&gt;, which is controlled by Amazon Web Services. For more information on spending limits (quotas) see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/quotas.html\&quot;&gt;Amazon Pinpoint quotas&lt;/a&gt; in the &lt;i&gt;Amazon Pinpoint Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
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


async def describe_account_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_account_attributes

    &lt;p&gt;Describes attributes of your Amazon Web Services account. The supported account attributes include account tier, which indicates whether your account is in the sandbox or production environment. When you&#39;re ready to move your account out of the sandbox, create an Amazon Web Services Support case for a service limit increase request.&lt;/p&gt; &lt;p&gt;New Amazon Pinpoint accounts are placed into an SMS or voice sandbox. The sandbox protects both Amazon Web Services end recipients and SMS or voice recipients from fraud and abuse. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeAccountAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_account_limits(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_account_limits

    &lt;p&gt;Describes the current Amazon Pinpoint SMS Voice V2 resource quotas for your account. The description for a quota includes the quota name, current usage toward that quota, and the quota&#39;s maximum value.&lt;/p&gt; &lt;p&gt;When you establish an Amazon Web Services account, the account has initial quotas on the maximum number of configuration sets, opt-out lists, phone numbers, and pools that you can create in a given Region. For more information see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/quotas.html\&quot;&gt; Amazon Pinpoint quotas &lt;/a&gt; in the &lt;i&gt;Amazon Pinpoint Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeAccountLimitsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_configuration_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_configuration_sets

    &lt;p&gt;Describes the specified configuration sets or all in your account.&lt;/p&gt; &lt;p&gt;If you specify configuration set names, the output includes information for only the specified configuration sets. If you specify filters, the output includes information for only those configuration sets that meet the filter criteria. If you don&#39;t specify configuration set names or filters, the output includes information for all configuration sets.&lt;/p&gt; &lt;p&gt;If you specify a configuration set name that isn&#39;t valid, an error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeConfigurationSetsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_keywords(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_keywords

    &lt;p&gt;Describes the specified keywords or all keywords on your origination phone number or pool.&lt;/p&gt; &lt;p&gt;A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, Amazon Pinpoint responds with a customizable message.&lt;/p&gt; &lt;p&gt;If you specify a keyword that isn&#39;t valid, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeKeywordsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_opt_out_lists(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_opt_out_lists

    &lt;p&gt;Describes the specified opt-out list or all opt-out lists in your account.&lt;/p&gt; &lt;p&gt;If you specify opt-out list names, the output includes information for only the specified opt-out lists. Opt-out lists include only those that meet the filter criteria. If you don&#39;t specify opt-out list names or filters, the output includes information for all opt-out lists.&lt;/p&gt; &lt;p&gt;If you specify an opt-out list name that isn&#39;t valid, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeOptOutListsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_opted_out_numbers(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_opted_out_numbers

    &lt;p&gt;Describes the specified opted out destination numbers or all opted out destination numbers in an opt-out list.&lt;/p&gt; &lt;p&gt;If you specify opted out numbers, the output includes information for only the specified opted out numbers. If you specify filters, the output includes information for only those opted out numbers that meet the filter criteria. If you don&#39;t specify opted out numbers or filters, the output includes information for all opted out destination numbers in your opt-out list.&lt;/p&gt; &lt;p&gt;If you specify an opted out number that isn&#39;t valid, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeOptedOutNumbersRequest.from_dict(body)
    return web.Response(status=200)


async def describe_phone_numbers(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_phone_numbers

    &lt;p&gt;Describes the specified origination phone number, or all the phone numbers in your account.&lt;/p&gt; &lt;p&gt;If you specify phone number IDs, the output includes information for only the specified phone numbers. If you specify filters, the output includes information for only those phone numbers that meet the filter criteria. If you don&#39;t specify phone number IDs or filters, the output includes information for all phone numbers.&lt;/p&gt; &lt;p&gt;If you specify a phone number ID that isn&#39;t valid, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribePhoneNumbersRequest.from_dict(body)
    return web.Response(status=200)


async def describe_pools(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_pools

    &lt;p&gt;Retrieves the specified pools or all pools associated with your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;If you specify pool IDs, the output includes information for only the specified pools. If you specify filters, the output includes information for only those pools that meet the filter criteria. If you don&#39;t specify pool IDs or filters, the output includes information for all pools.&lt;/p&gt; &lt;p&gt;If you specify a pool ID that isn&#39;t valid, an Error is returned.&lt;/p&gt; &lt;p&gt;A pool is a collection of phone numbers and SenderIds. A pool can include one or more phone numbers and SenderIds that are associated with your Amazon Web Services account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribePoolsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_sender_ids(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_sender_ids

    &lt;p&gt;Describes the specified SenderIds or all SenderIds associated with your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;If you specify SenderIds, the output includes information for only the specified SenderIds. If you specify filters, the output includes information for only those SenderIds that meet the filter criteria. If you don&#39;t specify SenderIds or filters, the output includes information for all SenderIds.&lt;/p&gt; &lt;p&gt;f you specify a sender ID that isn&#39;t valid, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeSenderIdsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_spend_limits(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_spend_limits

    &lt;p&gt;Describes the current Amazon Pinpoint monthly spend limits for sending voice and text messages.&lt;/p&gt; &lt;p&gt;When you establish an Amazon Web Services account, the account has initial monthly spend limit in a given Region. For more information on increasing your monthly spend limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-awssupport-spend-threshold.html\&quot;&gt; Requesting increases to your monthly SMS spending quota for Amazon Pinpoint &lt;/a&gt; in the &lt;i&gt;Amazon Pinpoint User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeSpendLimitsRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_origination_identity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_origination_identity

    &lt;p&gt;Removes the specified origination identity from an existing pool.&lt;/p&gt; &lt;p&gt;If the origination identity isn&#39;t associated with the specified pool, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DisassociateOriginationIdentityRequest.from_dict(body)
    return web.Response(status=200)


async def list_pool_origination_identities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_pool_origination_identities

    &lt;p&gt;Lists all associated origination identities in your pool.&lt;/p&gt; &lt;p&gt;If you specify filters, the output includes information for only those origination identities that meet the filter criteria.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListPoolOriginationIdentitiesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    List all tags associated with a resource.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def put_keyword(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_keyword

    &lt;p&gt;Creates or updates a keyword configuration on an origination phone number or pool.&lt;/p&gt; &lt;p&gt; A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, Amazon Pinpoint responds with a customizable message.&lt;/p&gt; &lt;p&gt;If you specify a keyword that isn&#39;t valid, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = PutKeywordRequest.from_dict(body)
    return web.Response(status=200)


async def put_opted_out_number(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_opted_out_number

    &lt;p&gt;Creates an opted out destination phone number in the opt-out list.&lt;/p&gt; &lt;p&gt;If the destination phone number isn&#39;t valid or if the specified opt-out list doesn&#39;t exist, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = PutOptedOutNumberRequest.from_dict(body)
    return web.Response(status=200)


async def release_phone_number(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """release_phone_number

    &lt;p&gt;Releases an existing origination phone number in your account. Once released, a phone number is no longer available for sending messages.&lt;/p&gt; &lt;p&gt;If the origination phone number has deletion protection enabled or is associated with a pool, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ReleasePhoneNumberRequest.from_dict(body)
    return web.Response(status=200)


async def request_phone_number(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """request_phone_number

    Request an origination phone number for use in your account. For more information on phone number request see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/userguide/settings-sms-request-number.html\&quot;&gt; Requesting a number &lt;/a&gt; in the &lt;i&gt;Amazon Pinpoint User Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RequestPhoneNumberRequest.from_dict(body)
    return web.Response(status=200)


async def send_text_message(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_text_message

    &lt;p&gt;Creates a new text message and sends it to a recipient&#39;s phone number.&lt;/p&gt; &lt;p&gt;SMS throughput limits are measured in Message Parts per Second (MPS). Your MPS limit depends on the destination country of your messages, as well as the type of phone number (origination number) that you use to send the message. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-limitations-mps.html\&quot;&gt;Message Parts per Second (MPS) limits&lt;/a&gt; in the &lt;i&gt;Amazon Pinpoint User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = SendTextMessageRequest.from_dict(body)
    return web.Response(status=200)


async def send_voice_message(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_voice_message

    Allows you to send a request that sends a text message through Amazon Pinpoint. This operation uses &lt;a href&#x3D;\&quot;http://aws.amazon.com/polly/\&quot;&gt;Amazon Polly&lt;/a&gt; to convert a text script into a voice message.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = SendVoiceMessageRequest.from_dict(body)
    return web.Response(status=200)


async def set_default_message_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_default_message_type

    &lt;p&gt;Sets the default message type on a configuration set.&lt;/p&gt; &lt;p&gt;Choose the category of SMS messages that you plan to send from this account. If you send account-related messages or time-sensitive messages such as one-time passcodes, choose &lt;b&gt;Transactional&lt;/b&gt;. If you plan to send messages that contain marketing material or other promotional content, choose &lt;b&gt;Promotional&lt;/b&gt;. This setting applies to your entire Amazon Web Services account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = SetDefaultMessageTypeRequest.from_dict(body)
    return web.Response(status=200)


async def set_default_sender_id(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_default_sender_id

    &lt;p&gt;Sets default sender ID on a configuration set.&lt;/p&gt; &lt;p&gt;When sending a text message to a destination country that supports sender IDs, the default sender ID on the configuration set specified will be used if no dedicated origination phone numbers or registered sender IDs are available in your account.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = SetDefaultSenderIdRequest.from_dict(body)
    return web.Response(status=200)


async def set_text_message_spend_limit_override(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_text_message_spend_limit_override

    Sets an account level monthly spend limit override for sending text messages. The requested spend limit must be less than or equal to the &lt;code&gt;MaxLimit&lt;/code&gt;, which is set by Amazon Web Services. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = SetTextMessageSpendLimitOverrideRequest.from_dict(body)
    return web.Response(status=200)


async def set_voice_message_spend_limit_override(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_voice_message_spend_limit_override

    Sets an account level monthly spend limit override for sending voice messages. The requested spend limit must be less than or equal to the &lt;code&gt;MaxLimit&lt;/code&gt;, which is set by Amazon Web Services. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = SetVoiceMessageSpendLimitOverrideRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds or overwrites only the specified tags for the specified Amazon Pinpoint SMS Voice, version 2 resource. When you specify an existing tag key, the value is overwritten with the new value. Each resource can have a maximum of 50 tags. Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/tagging-resources.html\&quot;&gt; Tagging Amazon Pinpoint resources&lt;/a&gt; in the &lt;i&gt;Amazon Pinpoint Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
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


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes the association of the specified tags from an Amazon Pinpoint SMS Voice V2 resource. For more information on tags see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/tagging-resources.html\&quot;&gt; Tagging Amazon Pinpoint resources&lt;/a&gt; in the &lt;i&gt;Amazon Pinpoint Developer Guide&lt;/i&gt;. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_event_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_event_destination

    &lt;p&gt;Updates an existing event destination in a configuration set. You can update the IAM role ARN for CloudWatch Logs and Kinesis Data Firehose. You can also enable or disable the event destination.&lt;/p&gt; &lt;p&gt;You may want to update an event destination to change its matching event types or updating the destination resource ARN. You can&#39;t change an event destination&#39;s type between CloudWatch Logs, Kinesis Data Firehose, and Amazon SNS.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateEventDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def update_phone_number(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_phone_number

    &lt;p&gt;Updates the configuration of an existing origination phone number. You can update the opt-out list, enable or disable two-way messaging, change the TwoWayChannelArn, enable or disable self-managed opt-outs, and enable or disable deletion protection.&lt;/p&gt; &lt;p&gt;If the origination phone number is associated with a pool, an Error is returned.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdatePhoneNumberRequest.from_dict(body)
    return web.Response(status=200)


async def update_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_pool

    Updates the configuration of an existing pool. You can update the opt-out list, enable or disable two-way messaging, change the &lt;code&gt;TwoWayChannelArn&lt;/code&gt;, enable or disable self-managed opt-outs, enable or disable deletion protection, and enable or disable shared routes.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdatePoolRequest.from_dict(body)
    return web.Response(status=200)

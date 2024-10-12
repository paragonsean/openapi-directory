from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.message import Message
from openapi_server.models.submission_entry import SubmissionEntry
from openapi_server import util


async def messages_get(request: web.Request, limit=None, filter=None, sort_order=None) -> web.Response:
    """Retrieve Messages

    Retrieve the messages you have sent or received.    Scheduled messages are available for retrieval only after the delivery date.  All the parameters are optional.  If a value is not supplied for &#x60;filter&#x60;, the messages are not filtered.  Messages can be filtered by supplying query clauses in the &#x60;filter&#x60; parameter. Each clause has the form &#x60;name&#x3D;value&#x60; where &#x60;name&#x60; is the name of a filter field and &#x60;value&#x60; is a valid value for that field.  A value for a field is optional. Include a clause for a field in the filter only when there is a need to fetch messages that match some value for that field. For a numeric filter field, you can also use the less than operator (&#x60;&lt;&#x60;).  If present, the filter value must have at least one clause, but it can contain a combination of clauses. Multiple clauses are separated with the &#x60;&amp;&#x60; symbol.  Semantically, multiple clauses form a [logical conjunction](https://en.wikipedia.org/wiki/Logical_conjunction).  For example, if you want to list all messages that were sent as part of a particular submission, your filter contains two clauses and will look something like this &#x60;&#x60;&#x60; type%3DSENT&amp;submission.id%3D1-00000000000522347562 &#x60;&#x60;&#x60; Because &#x60;filter&#x60; is a request parameter, it is important to note that the value for this parameter must be *URL encoded*. In particular, the &#x60;&#x3D;&#x60; encodes to &#x60;%3D&#x60; and the &#x60;&amp;&#x60; encodes to &#x60;%26&#x60;.  Note that you do not have to encode the &#x60;&lt;&#x60; character.  Using the previous example to illustrate; after encoding and encasing it, the clauses are transformed into a request that looks like this &#x60;&#x60;&#x60; GET /v1/messages?filter&#x3D;type%3DSENT%26submission.id%3D1-00000000000522347562 &#x60;&#x60;&#x60; If the field name or the field value of a clause is not valid, a [bad_request error](errors#bad-request) is returned instead of the usual result.  The &#x60;detail&#x60; field of this error provides more information about the problem.  The table below lists the fields available for filtering  | Field | Type   | Values | Note and example | |-------|------|--------------------|------| | id            | Integer  | Positive integer  | Use the &#x60;id&#x60; field with &#x60;&lt;&#x60; (or with &#x60;&gt;&#x60;) to fetch messages that are older (or newer) than those that are already fetched. &lt;br/&gt;&#x60;filter&#x3D;id&lt;123456&#x60; | | type          | String  | SENT, RECEIVED  | SENT are Mobile Terminating (MT) SMSs; RECEIVED are Mobile Originating (MO) SMSs.&lt;br/&gt;&#x60;filter&#x3D;type%3DSENT&#x60; | | submission.id | String  |  | &#x60;filter&#x3D;submission.id%3D1-00000000000522347562&#x60; | | status.type   | String  | ACCEPTED, SENT, DELIVERED, FAILED  | See the message &#x60;status.type&#x60; field for more information. &lt;br/&gt;&#x60;filter&#x3D;status.type%3DDELIVERED&#x60; | | status.id| String  |  | See the message &#x60;status.id&#x60; field for more information. &#x60;filter&#x3D;status.id%3DFAILED.EXPIRED&#x60;| | submission.date | String | Formatted Date | A fully specified date (e.g. 2017-01-01T10:00:00+01:00).  Use this field with &#x60;&lt;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60; or &#x60;&gt;&#x3D;&#x60; to limit the values. &lt;br/&gt;&#x60;filter&#x3D;submission.date%3E%3D2017-01-01T10%3A00%3A00%2B01%3A00&#x60; | | userSuppliedId  | String | | Use a string value you specified in the &#x60;userSuppliedId&#x60; property when you sent the message. Only &#x60;SENT&#x60; messages will be retrieved. &lt;br/&gt;&#x60;filter&#x3D;userSuppliedId%3Dacc009876&#x60; | 

    :param limit: The maximum number of messages that are returned.  The default is 1000. The value of &#x60;limit&#x60; is not a guarantee that a specific number of messages will be in the response, even if there are more messages available.  Consider the case where you have 150 messages and you specify &#x60;limit&#x3D;50&#x60;.  It is possible that only 49 messages will be returned.  The  way to make sure that there are no more messages is to submit a new call using the &#x60;id&#x60; filter field with the &#x60;&lt;&#x60; operator (described below).
    :type limit: 
    :param filter: See the message filtering for more information.
    :type filter: str
    :param sort_order: The default value is DESCENDING  If the &#x60;sortOrder&#x60; is DESCENDING, the newest messages be first in the result.  ASCENDING places the oldest messages on top of the response. 
    :type sort_order: str

    """
    return web.Response(status=200)


async def messages_id_get(request: web.Request, id) -> web.Response:
    """Show Message

    Get a the message by &#x60;id&#x60;. &#x60;&#x60;&#x60;http GET /v1/messages/4023457654 &#x60;&#x60;&#x60; 

    :param id: The &#x60;id&#x60; of the message you want to retrieve
    :type id: str

    """
    return web.Response(status=200)


async def messages_id_related_received_messages_get(request: web.Request, id) -> web.Response:
    """List Related Messages

    Get the messages related to a sent message identified by &#x60;id&#x60;.  For more information how this work, see the &#x60;relatedSentMessageId&#x60; field in the message. 

    :param id: The &#x60;id&#x60; of the sent message
    :type id: str

    """
    return web.Response(status=200)


async def messages_post(request: web.Request, body, deduplication_id=None, auto_unicode=None, schedule_date=None, schedule_description=None) -> web.Response:
    """Send Messages

    Send messages to one or more recipients.  You can post up to &#x60;30 000&#x60; messages in a batch.  But note that the &#x60;deduplication-id&#x60; is set per submission, so it is recommended that you use a smaller number, like &#x60;4000&#x60; per submission in order to make resubmissions on network failures more practical.  #### Repliability  When a sent message is _repliable_,  the BulkSMS system can process an SMS response sent by your recipient.  The message sent by your customer is called a mobile originating (MO) message and would be available under &#x60;RECEIVED&#x60; messages.  You can obtain a list of MOs using the [retrieve messages API call](#tag/Message%2Fpaths%2F~1messages%2Fget). In addition you can also get a list of the MOs that are associated with a specific sent message (see the [list related messages API call](#tag/Message%2Fpaths%2F~1messages~1%7Bid%7D~1relatedReceivedMessages%2Fget)).  If you use a specific _sender id_ in the &#x60;from&#x60; property of the send message, the message will not be repliable. If you want a message to be repliable, you need to specify &#x60;REPLIABLE&#x60; in the &#x60;from.type&#x60; property.  If you do not set the &#x60;from&#x60; property, your account settings are considered to determine whether or not the message is repliable. If the _default repliable_ setting on your account is _yes_ then the message will be repliable.  If this setting is _no_, the message will not be repliable.   #### Body templates  When sending a message you can use template fields to customise the message text.  *Field based templates* allow you to create a message with place-holders for custom fields.  Fields are identified by a zero based index; the first field is &#x60;F0&#x60;, the second is &#x60;F1&#x60; and so on.    For example, let&#39;s say you want to send a daily SMS message to all your clients that tell them what their current balance is.  The &#x60;body&#x60; of the message could look something like this   &#x60;&#x60;&#x60; Good morning {F0######}, your balance is {F1######} &#x60;&#x60;&#x60;  In this message, the first field, &#x60;F0&#x60;, is the name  of the customer and he second field &#x60;F1&#x60; is the balance for that customer.  The &#x60;#&#x60; used to specify the maximum length  of the field.  Note that the maximum length allowed for the value includes the space taken by the braces, template name and hash symbol.  For example, the value &#x60;{F0#}&#x60; specifies a maximum length of &#x60;5&#x60;.  If the data is longer than this length, the data will be truncated when the message body is constructed.  The data fields are provided in the property named &#x60;fields&#x60; in the &#x60;to&#x60; element.  Here is a complete example of how this might look  &#x60;&#x60;&#x60; {   \&quot;body\&quot;: \&quot;Good morning {F0######}, your balance is {F1######}\&quot;,   \&quot;to\&quot;:  [       {\&quot;address\&quot;: \&quot;27456789\&quot;,\&quot;fields\&quot;: [\&quot;Harry\&quot;, \&quot;$1345.23\&quot;] },       {\&quot;address\&quot;: \&quot;27456785\&quot;,\&quot;fields\&quot;: [\&quot;Sally\&quot;, \&quot;$2345.58\&quot;] }   ] } &#x60;&#x60;&#x60;  If you are sending to contacts (or to groups) in your phonebook, you can use the *Phonebook based templates*.  These are similar to the templates described above, but they have specific names. The template for the contact&#39;s first name is identified by &#x60;fn&#x60; and the template for the contact&#39;s surname is identified by &#x60;sn&#x60;.  Below in an example that will work if the numbers are registered in your phonebook.   &#x60;&#x60;&#x60; {   \&quot;body\&quot;: \&quot;Hi {fn######} {sn######}, have a great day!\&quot;,   \&quot;to\&quot;:  [       {\&quot;address\&quot;: \&quot;27456789\&quot; },       {\&quot;address\&quot;: \&quot;27456785\&quot; }   ] } &#x60;&#x60;&#x60; 

    :param body: Contains details of the message (or messages) that you want to send.  One &#x60;SubmissionEntry&#x60; can produce many messages, and your request may contain multiple such entries. 
    :type body: list | bytes
    :param deduplication_id: Safeguards against the possibility of sending the same messages more than once.  If a communication failure occurs during a submission, you cannot be sure that the submission was processed; therefore you would have to submit it again. When you post the retry, you must use the &#x60;deduplication-id&#x60; of the original post. The BulkSMS system uses this ID to check that the request was not previously processed. (If it was previously processed, the submission will succeed, and the behaviour will be indistinguishable to you from a non-duplicated submission). The ID expires after about 12 hours. 
    :type deduplication_id: int
    :param auto_unicode: Specifies how to deal with message text that contains characters not present in the GSM 03.38 character set.  Messages that contain only GSM 03.38 characters are not affected by this setting.  If the value is &#x60;true&#x60; then a message containing non-GSM 03.38 characters will be transmitted as a Unicode SMS (which is most likely more costly).   Please note: when &#x60;auto-unicode&#x60; is &#x60;true&#x60; and the value of the &#x60;encoding&#x60; property is specified as &#x60;UNICODE&#x60;, the message will always be sent as &#x60;UNICODE&#x60;.  If the value is &#x60;false&#x60; and the &#x60;encoding&#x60; property is &#x60;TEXT&#x60; then non-GSM 03.38 characters will be replaced by the &#x60;?&#x60; character.  When using this setting on the API, you should take case to ensure that your message is _clean_.    Invisible unicode and unexpected characters could unintentionally convert an message to &#x60;UNICODE&#x60;.  A common mistake is to use the backtick character (\\&#x60;) which is unicode and will turn your &#x60;TEXT&#x60; message into a &#x60;UNICODE&#x60; message. 
    :type auto_unicode: bool
    :param schedule_date: Allows you to send a message in the future.  An example value is &#x60;2019-02-18T13:00:00+02:00&#x60;.  It encodes to &#x60;2019-02-18T13%3A00%3A00%2B02%3A00&#x60;. Credits are deducted from your account immediately. Once submitted, scheduled messages cannot be changed or cancelled. The date can be a maximum of two years in the future. If the value is in the past, the message will be sent immediately. The date format requires you to supply an offset from UTC. You can decide to use the offset of your timezone, or maybe the zone of the recipient&#39;s location is more appropriate. If the destination is a group, the group members are determined at the time that you submit the message; not the time the message is scheduled to be sent. 
    :type schedule_date: str
    :param schedule_description: A note that is stored together with a scheduled submission, which could be used to more easily identify the scheduled submission at a later date.  The value of this field is ignored if the &#x60;schedule-date&#x60; is not provided. A value that is longer than 256 characters is truncated. 
    :type schedule_description: str

    """
    body = [SubmissionEntry.from_dict(d) for d in body]
    schedule_date = util.deserialize_datetime(schedule_date)
    return web.Response(status=200)


async def messages_send_get(request: web.Request, to, body, deduplication_id=None) -> web.Response:
    """Send message by simple GET or POST

    A really simple interface for people who require a GET mechanism to submit a single message.  The URI is interpreted as UTF-8. HTTP Basic Auth is used for authentication.  __Note__ BulkSMS recommends that you use the more flexible Send Messages Operation when submitting SMS messages from your application.  Here is an example of a GET &#x60;&#x60;&#x60;http GET /v1/messages/send?to&#x3D;%2b270000000&amp;body&#x3D;Hello%20World &#x60;&#x60;&#x60;  You can also use the same parameters to POST form encoded fields to &#x60;/messages&#x60;. Here is an example of a POST &#x60;&#x60;&#x60;http POST /v1/messages Content-Type: application/x-www-form-urlencoded  to&#x3D;%2b27000000000&amp;body&#x3D;Hello+World &#x60;&#x60;&#x60; 

    :param to: The phone number of the recipient.
    :type to: str
    :param body: The text you want to send.
    :type body: str
    :param deduplication_id: Refer to the &#x60;deduplication-id&#x60; parameter.
    :type deduplication_id: int

    """
    return web.Response(status=200)

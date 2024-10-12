# TwilioApi.Api20100401MessageApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMessage**](Api20100401MessageApi.md#createMessage) | **POST** /2010-04-01/Accounts/{AccountSid}/Messages.json | 
[**deleteMessage**](Api20100401MessageApi.md#deleteMessage) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json | 
[**fetchMessage**](Api20100401MessageApi.md#fetchMessage) | **GET** /2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json | 
[**listMessage**](Api20100401MessageApi.md#listMessage) | **GET** /2010-04-01/Accounts/{AccountSid}/Messages.json | 
[**updateMessage**](Api20100401MessageApi.md#updateMessage) | **POST** /2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json | 



## createMessage

> ApiV2010AccountMessage createMessage(accountSid, to, opts)



Send a message

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MessageApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) creating the Message resource.
let to = "to_example"; // String | The recipient's phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (for SMS/MMS) or [channel address](https://www.twilio.com/docs/messaging/channels), e.g. `whatsapp:+15552229999`.
let opts = {
  'addressRetention': "addressRetention_example", // MessageEnumAddressRetention | 
  'applicationSid': "applicationSid_example", // String | The SID of the associated [TwiML Application](https://www.twilio.com/docs/usage/api/applications). If this parameter is provided, the `status_callback` parameter of this request is ignored; [Message status callback requests](https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url) are sent to the TwiML App's `message_status_callback` URL.
  'attempt': 56, // Number | Total number of attempts made (including this request) to send the message regardless of the provider used
  'body': "body_example", // String | The text content of the outgoing message. Can be up to 1,600 characters in length. SMS only: If the `body` contains more than 160 [GSM-7](https://www.twilio.com/docs/glossary/what-is-gsm-7-character-encoding) characters (or 70 [UCS-2](https://www.twilio.com/docs/glossary/what-is-ucs-2-character-encoding) characters), the message is segmented and charged accordingly. For long `body` text, consider using the [send_as_mms parameter](https://www.twilio.com/blog/mms-for-long-text-messages).
  'contentRetention': "contentRetention_example", // MessageEnumContentRetention | 
  'contentSid': "contentSid_example", // String | For [Content Editor/API](https://www.twilio.com/docs/content) only: The SID of the Content Template to be used with the Message, e.g., `HXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`. If this parameter is not provided, a Content Template is not used. Find the SID in the Console on the Content Editor page. For Content API users, the SID is found in Twilio's response when [creating the Template](https://www.twilio.com/docs/content/content-api-resources#create-templates) or by [fetching your Templates](https://www.twilio.com/docs/content/content-api-resources#fetch-all-content-resources).
  'contentVariables': "contentVariables_example", // String | For [Content Editor/API](https://www.twilio.com/docs/content) only: Key-value pairs of [Template variables](https://www.twilio.com/docs/content/using-variables-with-content-api) and their substitution values. `content_sid` parameter must also be provided. If values are not defined in the `content_variables` parameter, the [Template's default placeholder values](https://www.twilio.com/docs/content/content-api-resources#create-templates) are used.
  'forceDelivery': true, // Boolean | Reserved
  'from': "from_example", // String | The sender's Twilio phone number (in [E.164](https://en.wikipedia.org/wiki/E.164) format), [alphanumeric sender ID](https://www.twilio.com/docs/sms/quickstart), [Wireless SIM](https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands), [short code](https://www.twilio.com/en-us/messaging/channels/sms/short-codes), or [channel address](https://www.twilio.com/docs/messaging/channels) (e.g., `whatsapp:+15554449999`). The value of the `from` parameter must be a sender that is hosted within Twilio and belongs to the Account creating the Message. If you are using `messaging_service_sid`, this parameter can be empty (Twilio assigns a `from` value from the Messaging Service's Sender Pool) or you can provide a specific sender from your Sender Pool.
  'maxPrice': 3.4, // Number | The maximum price in US dollars that you are willing to pay for this Message's delivery. The value can have up to four decimal places. When the `max_price` parameter is provided, the cost of a message is checked before it is sent. If the cost exceeds `max_price`, the message is not sent and the Message `status` is `failed`.
  'mediaUrl': ["null"], // [String] | The URL of media to include in the Message content. `jpeg`, `jpg`, `gif`, and `png` file types are fully supported by Twilio and content is formatted for delivery on destination devices. The media size limit is 5 MB for supported file types (`jpeg`, `jpg`, `png`, `gif`) and 500 KB for [other types](https://www.twilio.com/docs/messaging/guides/accepted-mime-types) of accepted media. To send more than one image in the message, provide multiple `media_url` parameters in the POST request. You can include up to ten `media_url` parameters per message. [International](https://support.twilio.com/hc/en-us/articles/223179808-Sending-and-receiving-MMS-messages) and [carrier](https://support.twilio.com/hc/en-us/articles/223133707-Is-MMS-supported-for-all-carriers-in-US-and-Canada-) limits apply.
  'messagingServiceSid': "messagingServiceSid_example", // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services) you want to associate with the Message. When this parameter is provided and the `from` parameter is omitted, Twilio selects the optimal sender from the Messaging Service's Sender Pool. You may also provide a `from` parameter if you want to use a specific Sender from the Sender Pool.
  'persistentAction': ["null"], // [String] | Rich actions for non-SMS/MMS channels. Used for [sending location in WhatsApp messages](https://www.twilio.com/docs/whatsapp/message-features#location-messages-with-whatsapp).
  'provideFeedback': true, // Boolean | Boolean indicating whether or not you intend to provide delivery confirmation feedback to Twilio (used in conjunction with the [Message Feedback subresource](https://www.twilio.com/docs/sms/api/message-feedback-resource)). Default value is `false`.
  'riskCheck': "riskCheck_example", // MessageEnumRiskCheck | 
  'scheduleType': "scheduleType_example", // MessageEnumScheduleType | 
  'sendAsMms': true, // Boolean | If set to `true`, Twilio delivers the message as a single MMS message, regardless of the presence of media.
  'sendAt': new Date("2013-10-20T19:20:30+01:00"), // Date | The time that Twilio will send the message. Must be in ISO 8601 format.
  'shortenUrls': true, // Boolean | For Messaging Services with [Link Shortening configured](https://www.twilio.com/docs/messaging/features/link-shortening) only: A Boolean indicating whether or not Twilio should shorten links in the `body` of the Message. Default value is `false`. If `true`, the `messaging_service_sid` parameter must also be provided.
  'smartEncoded': true, // Boolean | Whether to detect Unicode characters that have a similar GSM-7 character and replace them. Can be: `true` or `false`.
  'statusCallback': "statusCallback_example", // String | The URL of the endpoint to which Twilio sends [Message status callback requests](https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url). URL must contain a valid hostname and underscores are not allowed. If you include this parameter with the `messaging_service_sid`, Twilio uses this URL instead of the Status Callback URL of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource). 
  'validityPeriod': 56 // Number | The maximum length in seconds that the Message can remain in Twilio's outgoing message queue. If a queued Message exceeds the `validity_period`, the Message is not sent. Accepted values are integers from `1` to `14400`. Default value is `14400`. A `validity_period` greater than `5` is recommended. [Learn more about the validity period](https://www.twilio.com/blog/take-more-control-of-outbound-messages-using-validity-period-html)
};
apiInstance.createMessage(accountSid, to, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) creating the Message resource. | 
 **to** | **String**| The recipient&#39;s phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (for SMS/MMS) or [channel address](https://www.twilio.com/docs/messaging/channels), e.g. &#x60;whatsapp:+15552229999&#x60;. | 
 **addressRetention** | **MessageEnumAddressRetention**|  | [optional] 
 **applicationSid** | **String**| The SID of the associated [TwiML Application](https://www.twilio.com/docs/usage/api/applications). If this parameter is provided, the &#x60;status_callback&#x60; parameter of this request is ignored; [Message status callback requests](https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url) are sent to the TwiML App&#39;s &#x60;message_status_callback&#x60; URL. | [optional] 
 **attempt** | **Number**| Total number of attempts made (including this request) to send the message regardless of the provider used | [optional] 
 **body** | **String**| The text content of the outgoing message. Can be up to 1,600 characters in length. SMS only: If the &#x60;body&#x60; contains more than 160 [GSM-7](https://www.twilio.com/docs/glossary/what-is-gsm-7-character-encoding) characters (or 70 [UCS-2](https://www.twilio.com/docs/glossary/what-is-ucs-2-character-encoding) characters), the message is segmented and charged accordingly. For long &#x60;body&#x60; text, consider using the [send_as_mms parameter](https://www.twilio.com/blog/mms-for-long-text-messages). | [optional] 
 **contentRetention** | **MessageEnumContentRetention**|  | [optional] 
 **contentSid** | **String**| For [Content Editor/API](https://www.twilio.com/docs/content) only: The SID of the Content Template to be used with the Message, e.g., &#x60;HXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&#x60;. If this parameter is not provided, a Content Template is not used. Find the SID in the Console on the Content Editor page. For Content API users, the SID is found in Twilio&#39;s response when [creating the Template](https://www.twilio.com/docs/content/content-api-resources#create-templates) or by [fetching your Templates](https://www.twilio.com/docs/content/content-api-resources#fetch-all-content-resources). | [optional] 
 **contentVariables** | **String**| For [Content Editor/API](https://www.twilio.com/docs/content) only: Key-value pairs of [Template variables](https://www.twilio.com/docs/content/using-variables-with-content-api) and their substitution values. &#x60;content_sid&#x60; parameter must also be provided. If values are not defined in the &#x60;content_variables&#x60; parameter, the [Template&#39;s default placeholder values](https://www.twilio.com/docs/content/content-api-resources#create-templates) are used. | [optional] 
 **forceDelivery** | **Boolean**| Reserved | [optional] 
 **from** | **String**| The sender&#39;s Twilio phone number (in [E.164](https://en.wikipedia.org/wiki/E.164) format), [alphanumeric sender ID](https://www.twilio.com/docs/sms/quickstart), [Wireless SIM](https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands), [short code](https://www.twilio.com/en-us/messaging/channels/sms/short-codes), or [channel address](https://www.twilio.com/docs/messaging/channels) (e.g., &#x60;whatsapp:+15554449999&#x60;). The value of the &#x60;from&#x60; parameter must be a sender that is hosted within Twilio and belongs to the Account creating the Message. If you are using &#x60;messaging_service_sid&#x60;, this parameter can be empty (Twilio assigns a &#x60;from&#x60; value from the Messaging Service&#39;s Sender Pool) or you can provide a specific sender from your Sender Pool. | [optional] 
 **maxPrice** | **Number**| The maximum price in US dollars that you are willing to pay for this Message&#39;s delivery. The value can have up to four decimal places. When the &#x60;max_price&#x60; parameter is provided, the cost of a message is checked before it is sent. If the cost exceeds &#x60;max_price&#x60;, the message is not sent and the Message &#x60;status&#x60; is &#x60;failed&#x60;. | [optional] 
 **mediaUrl** | [**[String]**](String.md)| The URL of media to include in the Message content. &#x60;jpeg&#x60;, &#x60;jpg&#x60;, &#x60;gif&#x60;, and &#x60;png&#x60; file types are fully supported by Twilio and content is formatted for delivery on destination devices. The media size limit is 5 MB for supported file types (&#x60;jpeg&#x60;, &#x60;jpg&#x60;, &#x60;png&#x60;, &#x60;gif&#x60;) and 500 KB for [other types](https://www.twilio.com/docs/messaging/guides/accepted-mime-types) of accepted media. To send more than one image in the message, provide multiple &#x60;media_url&#x60; parameters in the POST request. You can include up to ten &#x60;media_url&#x60; parameters per message. [International](https://support.twilio.com/hc/en-us/articles/223179808-Sending-and-receiving-MMS-messages) and [carrier](https://support.twilio.com/hc/en-us/articles/223133707-Is-MMS-supported-for-all-carriers-in-US-and-Canada-) limits apply. | [optional] 
 **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services) you want to associate with the Message. When this parameter is provided and the &#x60;from&#x60; parameter is omitted, Twilio selects the optimal sender from the Messaging Service&#39;s Sender Pool. You may also provide a &#x60;from&#x60; parameter if you want to use a specific Sender from the Sender Pool. | [optional] 
 **persistentAction** | [**[String]**](String.md)| Rich actions for non-SMS/MMS channels. Used for [sending location in WhatsApp messages](https://www.twilio.com/docs/whatsapp/message-features#location-messages-with-whatsapp). | [optional] 
 **provideFeedback** | **Boolean**| Boolean indicating whether or not you intend to provide delivery confirmation feedback to Twilio (used in conjunction with the [Message Feedback subresource](https://www.twilio.com/docs/sms/api/message-feedback-resource)). Default value is &#x60;false&#x60;. | [optional] 
 **riskCheck** | **MessageEnumRiskCheck**|  | [optional] 
 **scheduleType** | **MessageEnumScheduleType**|  | [optional] 
 **sendAsMms** | **Boolean**| If set to &#x60;true&#x60;, Twilio delivers the message as a single MMS message, regardless of the presence of media. | [optional] 
 **sendAt** | **Date**| The time that Twilio will send the message. Must be in ISO 8601 format. | [optional] 
 **shortenUrls** | **Boolean**| For Messaging Services with [Link Shortening configured](https://www.twilio.com/docs/messaging/features/link-shortening) only: A Boolean indicating whether or not Twilio should shorten links in the &#x60;body&#x60; of the Message. Default value is &#x60;false&#x60;. If &#x60;true&#x60;, the &#x60;messaging_service_sid&#x60; parameter must also be provided. | [optional] 
 **smartEncoded** | **Boolean**| Whether to detect Unicode characters that have a similar GSM-7 character and replace them. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **statusCallback** | **String**| The URL of the endpoint to which Twilio sends [Message status callback requests](https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url). URL must contain a valid hostname and underscores are not allowed. If you include this parameter with the &#x60;messaging_service_sid&#x60;, Twilio uses this URL instead of the Status Callback URL of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource).  | [optional] 
 **validityPeriod** | **Number**| The maximum length in seconds that the Message can remain in Twilio&#39;s outgoing message queue. If a queued Message exceeds the &#x60;validity_period&#x60;, the Message is not sent. Accepted values are integers from &#x60;1&#x60; to &#x60;14400&#x60;. Default value is &#x60;14400&#x60;. A &#x60;validity_period&#x60; greater than &#x60;5&#x60; is recommended. [Learn more about the validity period](https://www.twilio.com/blog/take-more-control-of-outbound-messages-using-validity-period-html) | [optional] 

### Return type

[**ApiV2010AccountMessage**](ApiV2010AccountMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteMessage

> deleteMessage(accountSid, sid)



Deletes a Message resource from your account

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MessageApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource
let sid = "sid_example"; // String | The SID of the Message resource you wish to delete
apiInstance.deleteMessage(accountSid, sid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource | 
 **sid** | **String**| The SID of the Message resource you wish to delete | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchMessage

> ApiV2010AccountMessage fetchMessage(accountSid, sid)



Fetch a specific Message

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MessageApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource
let sid = "sid_example"; // String | The SID of the Message resource to be fetched
apiInstance.fetchMessage(accountSid, sid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource | 
 **sid** | **String**| The SID of the Message resource to be fetched | 

### Return type

[**ApiV2010AccountMessage**](ApiV2010AccountMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMessage

> ListMessageResponse listMessage(accountSid, opts)



Retrieve a list of Message resources associated with a Twilio Account

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MessageApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resources.
let opts = {
  'to': "to_example", // String | Filter by recipient. For example: Set this `to` parameter to `+15558881111` to retrieve a list of Message resources with `to` properties of `+15558881111`
  'from': "from_example", // String | Filter by sender. For example: Set this `from` parameter to `+15552229999` to retrieve a list of Message resources with `from` properties of `+15552229999`
  'dateSent': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter by Message `sent_date`. Accepts GMT dates in the following formats: `YYYY-MM-DD` (to find Messages with a specific `sent_date`), `<=YYYY-MM-DD` (to find Messages with `sent_date`s on and before a specific date), and `>=YYYY-MM-DD` (to find Messages with `sent_dates` on and after a specific date).
  'dateSent2': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter by Message `sent_date`. Accepts GMT dates in the following formats: `YYYY-MM-DD` (to find Messages with a specific `sent_date`), `<=YYYY-MM-DD` (to find Messages with `sent_date`s on and before a specific date), and `>=YYYY-MM-DD` (to find Messages with `sent_dates` on and after a specific date).
  'dateSent3': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter by Message `sent_date`. Accepts GMT dates in the following formats: `YYYY-MM-DD` (to find Messages with a specific `sent_date`), `<=YYYY-MM-DD` (to find Messages with `sent_date`s on and before a specific date), and `>=YYYY-MM-DD` (to find Messages with `sent_dates` on and after a specific date).
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMessage(accountSid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resources. | 
 **to** | **String**| Filter by recipient. For example: Set this &#x60;to&#x60; parameter to &#x60;+15558881111&#x60; to retrieve a list of Message resources with &#x60;to&#x60; properties of &#x60;+15558881111&#x60; | [optional] 
 **from** | **String**| Filter by sender. For example: Set this &#x60;from&#x60; parameter to &#x60;+15552229999&#x60; to retrieve a list of Message resources with &#x60;from&#x60; properties of &#x60;+15552229999&#x60; | [optional] 
 **dateSent** | **Date**| Filter by Message &#x60;sent_date&#x60;. Accepts GMT dates in the following formats: &#x60;YYYY-MM-DD&#x60; (to find Messages with a specific &#x60;sent_date&#x60;), &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_date&#x60;s on and before a specific date), and &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_dates&#x60; on and after a specific date). | [optional] 
 **dateSent2** | **Date**| Filter by Message &#x60;sent_date&#x60;. Accepts GMT dates in the following formats: &#x60;YYYY-MM-DD&#x60; (to find Messages with a specific &#x60;sent_date&#x60;), &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_date&#x60;s on and before a specific date), and &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_dates&#x60; on and after a specific date). | [optional] 
 **dateSent3** | **Date**| Filter by Message &#x60;sent_date&#x60;. Accepts GMT dates in the following formats: &#x60;YYYY-MM-DD&#x60; (to find Messages with a specific &#x60;sent_date&#x60;), &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_date&#x60;s on and before a specific date), and &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_dates&#x60; on and after a specific date). | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMessageResponse**](ListMessageResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMessage

> ApiV2010AccountMessage updateMessage(accountSid, sid, opts)



Update a Message resource (used to redact Message &#x60;body&#x60; text and to cancel not-yet-sent messages)

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MessageApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to update.
let sid = "sid_example"; // String | The SID of the Message resource to be updated
let opts = {
  'body': "body_example", // String | The new `body` of the Message resource. To redact the text content of a Message, this parameter's value must be an empty string
  'status': "status_example" // MessageEnumUpdateStatus | 
};
apiInstance.updateMessage(accountSid, sid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to update. | 
 **sid** | **String**| The SID of the Message resource to be updated | 
 **body** | **String**| The new &#x60;body&#x60; of the Message resource. To redact the text content of a Message, this parameter&#39;s value must be an empty string | [optional] 
 **status** | **MessageEnumUpdateStatus**|  | [optional] 

### Return type

[**ApiV2010AccountMessage**](ApiV2010AccountMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


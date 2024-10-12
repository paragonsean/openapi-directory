# TwilioMessaging.MessagingV1ServiceApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createService**](MessagingV1ServiceApi.md#createService) | **POST** /v1/Services | 
[**deleteService**](MessagingV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} | 
[**fetchService**](MessagingV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} | 
[**listService**](MessagingV1ServiceApi.md#listService) | **GET** /v1/Services | 
[**updateService**](MessagingV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} | 



## createService

> MessagingV1Service createService(friendlyName, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1ServiceApi();
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
let opts = {
  'areaCodeGeomatch': true, // Boolean | Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/messaging/services#area-code-geomatch) on the Service Instance.
  'fallbackMethod': "fallbackMethod_example", // String | The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.
  'fallbackToLongCode': true, // Boolean | [OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures.
  'fallbackUrl': "fallbackUrl_example", // String | The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.
  'inboundMethod': "inboundMethod_example", // String | The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.
  'inboundRequestUrl': "inboundRequestUrl_example", // String | The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.
  'mmsConverter': true, // Boolean | Whether to enable the [MMS Converter](https://www.twilio.com/docs/messaging/services#mms-converter) for messages sent through the Service instance.
  'scanMessageContent': "scanMessageContent_example", // ServiceEnumScanMessageContent | 
  'smartEncoding': true, // Boolean | Whether to enable [Smart Encoding](https://www.twilio.com/docs/messaging/services#smart-encoding) for messages sent through the Service instance.
  'statusCallback': "statusCallback_example", // String | The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
  'stickySender': true, // Boolean | Whether to enable [Sticky Sender](https://www.twilio.com/docs/messaging/services#sticky-sender) on the Service instance.
  'synchronousValidation': true, // Boolean | Reserved.
  'useInboundWebhookOnNumber': true, // Boolean | A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.
  'usecase': "usecase_example", // String | A string that describes the scenario in which the Messaging Service will be used. Possible values are `notifications`, `marketing`, `verification`, `discussion`, `poll`, `undeclared`.
  'validityPeriod': 56 // Number | How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.
};
apiInstance.createService(friendlyName, opts, (error, data, response) => {
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
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | 
 **areaCodeGeomatch** | **Boolean**| Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/messaging/services#area-code-geomatch) on the Service Instance. | [optional] 
 **fallbackMethod** | **String**| The HTTP method we should use to call &#x60;fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **fallbackToLongCode** | **Boolean**| [OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures. | [optional] 
 **fallbackUrl** | **String**| The URL that we call using &#x60;fallback_method&#x60; if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the &#x60;use_inbound_webhook_on_number&#x60; field is enabled then the webhook url defined on the phone number will override the &#x60;fallback_url&#x60; defined for the Messaging Service. | [optional] 
 **inboundMethod** | **String**| The HTTP method we should use to call &#x60;inbound_request_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional] 
 **inboundRequestUrl** | **String**| The URL we call using &#x60;inbound_method&#x60; when a message is received by any phone number or short code in the Service. When this property is &#x60;null&#x60;, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the &#x60;use_inbound_webhook_on_number&#x60; field is enabled then the webhook url defined on the phone number will override the &#x60;inbound_request_url&#x60; defined for the Messaging Service. | [optional] 
 **mmsConverter** | **Boolean**| Whether to enable the [MMS Converter](https://www.twilio.com/docs/messaging/services#mms-converter) for messages sent through the Service instance. | [optional] 
 **scanMessageContent** | **ServiceEnumScanMessageContent**|  | [optional] 
 **smartEncoding** | **Boolean**| Whether to enable [Smart Encoding](https://www.twilio.com/docs/messaging/services#smart-encoding) for messages sent through the Service instance. | [optional] 
 **statusCallback** | **String**| The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery. | [optional] 
 **stickySender** | **Boolean**| Whether to enable [Sticky Sender](https://www.twilio.com/docs/messaging/services#sticky-sender) on the Service instance. | [optional] 
 **synchronousValidation** | **Boolean**| Reserved. | [optional] 
 **useInboundWebhookOnNumber** | **Boolean**| A boolean value that indicates either the webhook url configured on the phone number will be used or &#x60;inbound_request_url&#x60;/&#x60;fallback_url&#x60; url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the &#x60;inbound_request_url&#x60;/&#x60;fallback_url&#x60; defined for the Messaging Service. | [optional] 
 **usecase** | **String**| A string that describes the scenario in which the Messaging Service will be used. Possible values are &#x60;notifications&#x60;, &#x60;marketing&#x60;, &#x60;verification&#x60;, &#x60;discussion&#x60;, &#x60;poll&#x60;, &#x60;undeclared&#x60;. | [optional] 
 **validityPeriod** | **Number**| How long, in seconds, messages sent from the Service are valid. Can be an integer from &#x60;1&#x60; to &#x60;14,400&#x60;. | [optional] 

### Return type

[**MessagingV1Service**](MessagingV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteService

> deleteService(sid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1ServiceApi();
let sid = "sid_example"; // String | The SID of the Service resource to delete.
apiInstance.deleteService(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Service resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchService

> MessagingV1Service fetchService(sid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1ServiceApi();
let sid = "sid_example"; // String | The SID of the Service resource to fetch.
apiInstance.fetchService(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Service resource to fetch. | 

### Return type

[**MessagingV1Service**](MessagingV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listService

> ListServiceResponse listService(opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1ServiceApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listService(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateService

> MessagingV1Service updateService(sid, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1ServiceApi();
let sid = "sid_example"; // String | The SID of the Service resource to update.
let opts = {
  'areaCodeGeomatch': true, // Boolean | Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/messaging/services#area-code-geomatch) on the Service Instance.
  'fallbackMethod': "fallbackMethod_example", // String | The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.
  'fallbackToLongCode': true, // Boolean | [OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures.
  'fallbackUrl': "fallbackUrl_example", // String | The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'inboundMethod': "inboundMethod_example", // String | The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.
  'inboundRequestUrl': "inboundRequestUrl_example", // String | The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.
  'mmsConverter': true, // Boolean | Whether to enable the [MMS Converter](https://www.twilio.com/docs/messaging/services#mms-converter) for messages sent through the Service instance.
  'scanMessageContent': "scanMessageContent_example", // ServiceEnumScanMessageContent | 
  'smartEncoding': true, // Boolean | Whether to enable [Smart Encoding](https://www.twilio.com/docs/messaging/services#smart-encoding) for messages sent through the Service instance.
  'statusCallback': "statusCallback_example", // String | The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
  'stickySender': true, // Boolean | Whether to enable [Sticky Sender](https://www.twilio.com/docs/messaging/services#sticky-sender) on the Service instance.
  'synchronousValidation': true, // Boolean | Reserved.
  'useInboundWebhookOnNumber': true, // Boolean | A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.
  'usecase': "usecase_example", // String | A string that describes the scenario in which the Messaging Service will be used. Possible values are `notifications`, `marketing`, `verification`, `discussion`, `poll`, `undeclared`.
  'validityPeriod': 56 // Number | How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.
};
apiInstance.updateService(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the Service resource to update. | 
 **areaCodeGeomatch** | **Boolean**| Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/messaging/services#area-code-geomatch) on the Service Instance. | [optional] 
 **fallbackMethod** | **String**| The HTTP method we should use to call &#x60;fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **fallbackToLongCode** | **Boolean**| [OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures. | [optional] 
 **fallbackUrl** | **String**| The URL that we call using &#x60;fallback_method&#x60; if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the &#x60;use_inbound_webhook_on_number&#x60; field is enabled then the webhook url defined on the phone number will override the &#x60;fallback_url&#x60; defined for the Messaging Service. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **inboundMethod** | **String**| The HTTP method we should use to call &#x60;inbound_request_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional] 
 **inboundRequestUrl** | **String**| The URL we call using &#x60;inbound_method&#x60; when a message is received by any phone number or short code in the Service. When this property is &#x60;null&#x60;, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the &#x60;use_inbound_webhook_on_number&#x60; field is enabled then the webhook url defined on the phone number will override the &#x60;inbound_request_url&#x60; defined for the Messaging Service. | [optional] 
 **mmsConverter** | **Boolean**| Whether to enable the [MMS Converter](https://www.twilio.com/docs/messaging/services#mms-converter) for messages sent through the Service instance. | [optional] 
 **scanMessageContent** | **ServiceEnumScanMessageContent**|  | [optional] 
 **smartEncoding** | **Boolean**| Whether to enable [Smart Encoding](https://www.twilio.com/docs/messaging/services#smart-encoding) for messages sent through the Service instance. | [optional] 
 **statusCallback** | **String**| The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery. | [optional] 
 **stickySender** | **Boolean**| Whether to enable [Sticky Sender](https://www.twilio.com/docs/messaging/services#sticky-sender) on the Service instance. | [optional] 
 **synchronousValidation** | **Boolean**| Reserved. | [optional] 
 **useInboundWebhookOnNumber** | **Boolean**| A boolean value that indicates either the webhook url configured on the phone number will be used or &#x60;inbound_request_url&#x60;/&#x60;fallback_url&#x60; url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the &#x60;inbound_request_url&#x60;/&#x60;fallback_url&#x60; defined for the Messaging Service. | [optional] 
 **usecase** | **String**| A string that describes the scenario in which the Messaging Service will be used. Possible values are &#x60;notifications&#x60;, &#x60;marketing&#x60;, &#x60;verification&#x60;, &#x60;discussion&#x60;, &#x60;poll&#x60;, &#x60;undeclared&#x60;. | [optional] 
 **validityPeriod** | **Number**| How long, in seconds, messages sent from the Service are valid. Can be an integer from &#x60;1&#x60; to &#x60;14,400&#x60;. | [optional] 

### Return type

[**MessagingV1Service**](MessagingV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


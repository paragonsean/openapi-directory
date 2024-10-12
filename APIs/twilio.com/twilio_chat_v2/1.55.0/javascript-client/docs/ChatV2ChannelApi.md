# TwilioChat.ChatV2ChannelApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createChannel**](ChatV2ChannelApi.md#createChannel) | **POST** /v2/Services/{ServiceSid}/Channels | 
[**deleteChannel**](ChatV2ChannelApi.md#deleteChannel) | **DELETE** /v2/Services/{ServiceSid}/Channels/{Sid} | 
[**fetchChannel**](ChatV2ChannelApi.md#fetchChannel) | **GET** /v2/Services/{ServiceSid}/Channels/{Sid} | 
[**listChannel**](ChatV2ChannelApi.md#listChannel) | **GET** /v2/Services/{ServiceSid}/Channels | 
[**updateChannel**](ChatV2ChannelApi.md#updateChannel) | **POST** /v2/Services/{ServiceSid}/Channels/{Sid} | 



## createChannel

> ChatV2ServiceChannel createChannel(serviceSid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2ChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Channel resource under.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | A valid JSON string that contains application-specific data.
  'createdBy': "createdBy_example", // String | The `identity` of the User that created the channel. Default is: `system`.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this should only be used in cases where a Channel is being recreated from a backup/separate source.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. The default value is `null`. Note that this parameter should only be used in cases where a Channel is being recreated from a backup/separate source  and where a Message was previously updated.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
  'type': "type_example", // ChannelEnumChannelType | 
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the Channel resource's `sid` in the URL. This value must be 64 characters or less in length and be unique within the Service.
};
apiInstance.createChannel(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Channel resource under. | 
 **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] 
 **createdBy** | **String**| The &#x60;identity&#x60; of the User that created the channel. Default is: &#x60;system&#x60;. | [optional] 
 **dateCreated** | **Date**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this should only be used in cases where a Channel is being recreated from a backup/separate source. | [optional] 
 **dateUpdated** | **Date**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. The default value is &#x60;null&#x60;. Note that this parameter should only be used in cases where a Channel is being recreated from a backup/separate source  and where a Message was previously updated. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the new resource. It can be up to 64 characters long. | [optional] 
 **type** | **ChannelEnumChannelType**|  | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the Channel resource&#39;s &#x60;sid&#x60; in the URL. This value must be 64 characters or less in length and be unique within the Service. | [optional] 

### Return type

[**ChatV2ServiceChannel**](ChatV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteChannel

> deleteChannel(serviceSid, sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2ChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.
let sid = "sid_example"; // String | The SID of the Channel resource to delete.  This value can be either the `sid` or the `unique_name` of the Channel resource to delete.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteChannel(serviceSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from. | 
 **sid** | **String**| The SID of the Channel resource to delete.  This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel resource to delete. | 
 **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchChannel

> ChatV2ServiceChannel fetchChannel(serviceSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2ChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Channel resource from.
let sid = "sid_example"; // String | The SID of the Channel resource to fetch. This value can be either the `sid` or the `unique_name` of the Channel resource to fetch.
apiInstance.fetchChannel(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Channel resource from. | 
 **sid** | **String**| The SID of the Channel resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel resource to fetch. | 

### Return type

[**ChatV2ServiceChannel**](ChatV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannel

> ListChannelResponse listChannel(serviceSid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2ChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Channel resources from.
let opts = {
  'type': ["null"], // [ChannelEnumChannelType] | The visibility of the Channels to read. Can be: `public` or `private` and defaults to `public`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listChannel(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Channel resources from. | 
 **type** | [**[ChannelEnumChannelType]**](ChannelEnumChannelType.md)| The visibility of the Channels to read. Can be: &#x60;public&#x60; or &#x60;private&#x60; and defaults to &#x60;public&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListChannelResponse**](ListChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateChannel

> ChatV2ServiceChannel updateChannel(serviceSid, sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2ChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Channel resource in.
let sid = "sid_example"; // String | The SID of the Channel resource to update. This value can be either the `sid` or the `unique_name` of the Channel resource to update.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | A valid JSON string that contains application-specific data.
  'createdBy': "createdBy_example", // String | The `identity` of the User that created the channel. Default is: `system`.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this should only be used in cases where a Channel is being recreated from a backup/separate source.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 256 characters long.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL. This value must be 256 characters or less in length and unique within the Service.
};
apiInstance.updateChannel(serviceSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Channel resource in. | 
 **sid** | **String**| The SID of the Channel resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel resource to update. | 
 **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] 
 **createdBy** | **String**| The &#x60;identity&#x60; of the User that created the channel. Default is: &#x60;system&#x60;. | [optional] 
 **dateCreated** | **Date**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this should only be used in cases where a Channel is being recreated from a backup/separate source. | [optional] 
 **dateUpdated** | **Date**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 256 characters long. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. This value must be 256 characters or less in length and unique within the Service. | [optional] 

### Return type

[**ChatV2ServiceChannel**](ChatV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


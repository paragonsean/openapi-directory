# TwilioChat.ChatV1ChannelApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createChannel**](ChatV1ChannelApi.md#createChannel) | **POST** /v1/Services/{ServiceSid}/Channels | 
[**deleteChannel**](ChatV1ChannelApi.md#deleteChannel) | **DELETE** /v1/Services/{ServiceSid}/Channels/{Sid} | 
[**fetchChannel**](ChatV1ChannelApi.md#fetchChannel) | **GET** /v1/Services/{ServiceSid}/Channels/{Sid} | 
[**listChannel**](ChatV1ChannelApi.md#listChannel) | **GET** /v1/Services/{ServiceSid}/Channels | 
[**updateChannel**](ChatV1ChannelApi.md#updateChannel) | **POST** /v1/Services/{ServiceSid}/Channels/{Sid} | 



## createChannel

> ChatV1ServiceChannel createChannel(serviceSid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1ChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under.
let opts = {
  'attributes': "attributes_example", // String | A valid JSON string that contains application-specific data.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
  'type': "type_example", // ChannelEnumChannelType | 
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL. This value must be 64 characters or less in length and be unique within the Service.
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under. | 
 **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the new resource. It can be up to 64 characters long. | [optional] 
 **type** | **ChannelEnumChannelType**|  | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. This value must be 64 characters or less in length and be unique within the Service. | [optional] 

### Return type

[**ChatV1ServiceChannel**](ChatV1ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteChannel

> deleteChannel(serviceSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1ChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Channel resource to delete.
apiInstance.deleteChannel(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Channel resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchChannel

> ChatV1ServiceChannel fetchChannel(serviceSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1ChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Channel resource to fetch.
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Channel resource to fetch. | 

### Return type

[**ChatV1ServiceChannel**](ChatV1ServiceChannel.md)

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

let apiInstance = new TwilioChat.ChatV1ChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from. | 
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

> ChatV1ServiceChannel updateChannel(serviceSid, sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1ChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Channel resource to update.
let opts = {
  'attributes': "attributes_example", // String | A valid JSON string that contains application-specific data.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL. This value must be 64 characters or less in length and be unique within the Service.
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Channel resource to update. | 
 **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. This value must be 64 characters or less in length and be unique within the Service. | [optional] 

### Return type

[**ChatV1ServiceChannel**](ChatV1ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


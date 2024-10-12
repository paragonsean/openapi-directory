# TwilioFlex.FlexV1WebChannelApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWebChannel**](FlexV1WebChannelApi.md#createWebChannel) | **POST** /v1/WebChannels | 
[**deleteWebChannel**](FlexV1WebChannelApi.md#deleteWebChannel) | **DELETE** /v1/WebChannels/{Sid} | 
[**fetchWebChannel**](FlexV1WebChannelApi.md#fetchWebChannel) | **GET** /v1/WebChannels/{Sid} | 
[**listWebChannel**](FlexV1WebChannelApi.md#listWebChannel) | **GET** /v1/WebChannels | 
[**updateWebChannel**](FlexV1WebChannelApi.md#updateWebChannel) | **POST** /v1/WebChannels/{Sid} | 



## createWebChannel

> FlexV1WebChannel createWebChannel(chatFriendlyName, customerFriendlyName, flexFlowSid, identity, opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1WebChannelApi();
let chatFriendlyName = "chatFriendlyName_example"; // String | The chat channel's friendly name.
let customerFriendlyName = "customerFriendlyName_example"; // String | The chat participant's friendly name.
let flexFlowSid = "flexFlowSid_example"; // String | The SID of the Flex Flow.
let identity = "identity_example"; // String | The chat identity.
let opts = {
  'chatUniqueName': "chatUniqueName_example", // String | The chat channel's unique name.
  'preEngagementData': "preEngagementData_example" // String | The pre-engagement data.
};
apiInstance.createWebChannel(chatFriendlyName, customerFriendlyName, flexFlowSid, identity, opts, (error, data, response) => {
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
 **chatFriendlyName** | **String**| The chat channel&#39;s friendly name. | 
 **customerFriendlyName** | **String**| The chat participant&#39;s friendly name. | 
 **flexFlowSid** | **String**| The SID of the Flex Flow. | 
 **identity** | **String**| The chat identity. | 
 **chatUniqueName** | **String**| The chat channel&#39;s unique name. | [optional] 
 **preEngagementData** | **String**| The pre-engagement data. | [optional] 

### Return type

[**FlexV1WebChannel**](FlexV1WebChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteWebChannel

> deleteWebChannel(sid)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1WebChannelApi();
let sid = "sid_example"; // String | The SID of the WebChannel resource to delete.
apiInstance.deleteWebChannel(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the WebChannel resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchWebChannel

> FlexV1WebChannel fetchWebChannel(sid)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1WebChannelApi();
let sid = "sid_example"; // String | The SID of the WebChannel resource to fetch.
apiInstance.fetchWebChannel(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the WebChannel resource to fetch. | 

### Return type

[**FlexV1WebChannel**](FlexV1WebChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWebChannel

> ListWebChannelResponse listWebChannel(opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1WebChannelApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listWebChannel(opts, (error, data, response) => {
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

[**ListWebChannelResponse**](ListWebChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWebChannel

> FlexV1WebChannel updateWebChannel(sid, opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1WebChannelApi();
let sid = "sid_example"; // String | The SID of the WebChannel resource to update.
let opts = {
  'chatStatus': "chatStatus_example", // WebChannelEnumChatStatus | 
  'postEngagementData': "postEngagementData_example" // String | The post-engagement data.
};
apiInstance.updateWebChannel(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the WebChannel resource to update. | 
 **chatStatus** | **WebChannelEnumChatStatus**|  | [optional] 
 **postEngagementData** | **String**| The post-engagement data. | [optional] 

### Return type

[**FlexV1WebChannel**](FlexV1WebChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


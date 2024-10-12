# TwilioFlex.FlexV1ChannelApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createChannel**](FlexV1ChannelApi.md#createChannel) | **POST** /v1/Channels | 
[**deleteChannel**](FlexV1ChannelApi.md#deleteChannel) | **DELETE** /v1/Channels/{Sid} | 
[**fetchChannel**](FlexV1ChannelApi.md#fetchChannel) | **GET** /v1/Channels/{Sid} | 
[**listChannel**](FlexV1ChannelApi.md#listChannel) | **GET** /v1/Channels | 



## createChannel

> FlexV1Channel createChannel(chatFriendlyName, chatUserFriendlyName, flexFlowSid, identity, opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1ChannelApi();
let chatFriendlyName = "chatFriendlyName_example"; // String | The chat channel's friendly name.
let chatUserFriendlyName = "chatUserFriendlyName_example"; // String | The chat participant's friendly name.
let flexFlowSid = "flexFlowSid_example"; // String | The SID of the Flex Flow.
let identity = "identity_example"; // String | The `identity` value that uniquely identifies the new resource's chat User.
let opts = {
  'chatUniqueName': "chatUniqueName_example", // String | The chat channel's unique name.
  'longLived': true, // Boolean | Whether to create the channel as long-lived.
  'preEngagementData': "preEngagementData_example", // String | The pre-engagement data.
  'target': "target_example", // String | The Target Contact Identity, for example the phone number of an SMS.
  'taskAttributes': "taskAttributes_example", // String | The Task attributes to be added for the TaskRouter Task.
  'taskSid': "taskSid_example" // String | The SID of the TaskRouter Task. Only valid when integration type is `task`. `null` for integration types `studio` & `external`
};
apiInstance.createChannel(chatFriendlyName, chatUserFriendlyName, flexFlowSid, identity, opts, (error, data, response) => {
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
 **chatUserFriendlyName** | **String**| The chat participant&#39;s friendly name. | 
 **flexFlowSid** | **String**| The SID of the Flex Flow. | 
 **identity** | **String**| The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s chat User. | 
 **chatUniqueName** | **String**| The chat channel&#39;s unique name. | [optional] 
 **longLived** | **Boolean**| Whether to create the channel as long-lived. | [optional] 
 **preEngagementData** | **String**| The pre-engagement data. | [optional] 
 **target** | **String**| The Target Contact Identity, for example the phone number of an SMS. | [optional] 
 **taskAttributes** | **String**| The Task attributes to be added for the TaskRouter Task. | [optional] 
 **taskSid** | **String**| The SID of the TaskRouter Task. Only valid when integration type is &#x60;task&#x60;. &#x60;null&#x60; for integration types &#x60;studio&#x60; &amp; &#x60;external&#x60; | [optional] 

### Return type

[**FlexV1Channel**](FlexV1Channel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteChannel

> deleteChannel(sid)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1ChannelApi();
let sid = "sid_example"; // String | The SID of the Flex chat channel resource to delete.
apiInstance.deleteChannel(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Flex chat channel resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchChannel

> FlexV1Channel fetchChannel(sid)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1ChannelApi();
let sid = "sid_example"; // String | The SID of the Flex chat channel resource to fetch.
apiInstance.fetchChannel(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Flex chat channel resource to fetch. | 

### Return type

[**FlexV1Channel**](FlexV1Channel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannel

> ListChannelResponse listChannel(opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1ChannelApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listChannel(opts, (error, data, response) => {
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

[**ListChannelResponse**](ListChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


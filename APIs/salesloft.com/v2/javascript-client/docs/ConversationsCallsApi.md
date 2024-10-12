# SalesLoftPlatform.ConversationsCallsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2ConversationsCallsPost**](ConversationsCallsApi.md#v2ConversationsCallsPost) | **POST** /v2/conversations/calls | Create Conversations Call



## v2ConversationsCallsPost

> ConversationsCall v2ConversationsCallsPost(duration, from, recording, to, opts)

Create Conversations Call

Enqueue a Conversations Call for processing

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.ConversationsCallsApi();
let duration = 3.4; // Number | Duration of call in seconds
let from = "from_example"; // String | Phone number that call was made from
let recording = {key: null}; // Object | Object containing recording info including the audio file (.mp3, .wav, .ogg, .m4a)
let to = "to_example"; // String |  Phone number that was called
let opts = {
  'callCreatedAt': "callCreatedAt_example", // String | Timestamp for when the call started. If not provided, will default to the time the request was received
  'direction': "direction_example", // String | Call direction
  'userGuid': "userGuid_example" // String | Guid of the Salesloft User to assign the call to. If not provided, will default to the user within the authentication token
};
apiInstance.v2ConversationsCallsPost(duration, from, recording, to, opts, (error, data, response) => {
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
 **duration** | **Number**| Duration of call in seconds | 
 **from** | **String**| Phone number that call was made from | 
 **recording** | [**Object**](Object.md)| Object containing recording info including the audio file (.mp3, .wav, .ogg, .m4a) | 
 **to** | **String**|  Phone number that was called | 
 **callCreatedAt** | **String**| Timestamp for when the call started. If not provided, will default to the time the request was received | [optional] 
 **direction** | **String**| Call direction | [optional] 
 **userGuid** | **String**| Guid of the Salesloft User to assign the call to. If not provided, will default to the user within the authentication token | [optional] 

### Return type

[**ConversationsCall**](ConversationsCall.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


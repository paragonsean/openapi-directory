# VoiceApi.CallsApi

All URIs are relative to *https://api.nexmo.com/v1/calls*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCall**](CallsApi.md#createCall) | **POST** / | Create an outbound call
[**getCall**](CallsApi.md#getCall) | **GET** /{uuid} | Get detail of a specific call
[**getCalls**](CallsApi.md#getCalls) | **GET** / | Get details of your calls
[**updateCall**](CallsApi.md#updateCall) | **PUT** /{uuid} | Modify an in progress call



## createCall

> CreateCallResponse createCall(opts)

Create an outbound call

Create an outbound Call

### Example

```javascript
import VoiceApi from 'voice_api';
let defaultClient = VoiceApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new VoiceApi.CallsApi();
let opts = {
  'createCallRequest': new VoiceApi.CreateCallRequest() // CreateCallRequest | Call Details
};
apiInstance.createCall(opts, (error, data, response) => {
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
 **createCallRequest** | [**CreateCallRequest**](CreateCallRequest.md)| Call Details | [optional] 

### Return type

[**CreateCallResponse**](CreateCallResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCall

> GetCallResponse getCall(uuid)

Get detail of a specific call

Get detail of a specific call

### Example

```javascript
import VoiceApi from 'voice_api';
let defaultClient = VoiceApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new VoiceApi.CallsApi();
let uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call
apiInstance.getCall(uuid, (error, data, response) => {
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
 **uuid** | **String**| UUID of the Call | 

### Return type

[**GetCallResponse**](GetCallResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCalls

> GetCallsResponse getCalls(opts)

Get details of your calls

Get details of your calls

### Example

```javascript
import VoiceApi from 'voice_api';
let defaultClient = VoiceApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new VoiceApi.CallsApi();
let opts = {
  'status': "started", // String | Filter by call status
  'dateStart': new Date("2016-11-14T07:45:14Z"), // Date | Return the records that occurred after this point in time
  'dateEnd': new Date("2016-11-14T07:45:14Z"), // Date | Return the records that occurred before this point in time
  'pageSize': 10, // Number | Return this amount of records in the response
  'recordIndex': 0, // Number | Return calls from this index in the response
  'order': "'asc'", // String | Either ascending or  descending order.
  'conversationUuid': "conversationUuid_example" // String | Return all the records associated with a specific conversation.
};
apiInstance.getCalls(opts, (error, data, response) => {
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
 **status** | **String**| Filter by call status | [optional] 
 **dateStart** | **Date**| Return the records that occurred after this point in time | [optional] 
 **dateEnd** | **Date**| Return the records that occurred before this point in time | [optional] 
 **pageSize** | **Number**| Return this amount of records in the response | [optional] [default to 10]
 **recordIndex** | **Number**| Return calls from this index in the response | [optional] [default to 0]
 **order** | **String**| Either ascending or  descending order. | [optional] [default to &#39;asc&#39;]
 **conversationUuid** | **String**| Return all the records associated with a specific conversation. | [optional] 

### Return type

[**GetCallsResponse**](GetCallsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCall

> updateCall(uuid, updateCallRequest)

Modify an in progress call

Modify an in progress call

### Example

```javascript
import VoiceApi from 'voice_api';
let defaultClient = VoiceApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new VoiceApi.CallsApi();
let uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call
let updateCallRequest = new VoiceApi.UpdateCallRequest(); // UpdateCallRequest | 
apiInstance.updateCall(uuid, updateCallRequest, (error, data, response) => {
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
 **uuid** | **String**| UUID of the Call | 
 **updateCallRequest** | [**UpdateCallRequest**](UpdateCallRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


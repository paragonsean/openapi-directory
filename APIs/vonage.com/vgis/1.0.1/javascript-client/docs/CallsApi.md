# VonageIntegrationSuite.CallsApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/vis/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callAnswer**](CallsApi.md#callAnswer) | **PUT** /self/calls/{id}/answer | Answer call (On supported devices)
[**callHold**](CallsApi.md#callHold) | **PUT** /self/calls/{id}/hold | Put call on hold
[**callTransfer**](CallsApi.md#callTransfer) | **POST** /self/calls/{id}/transfer | Transfer call
[**callUnold**](CallsApi.md#callUnold) | **DELETE** /self/calls/{id}/hold | Unhold
[**callVMTransfer**](CallsApi.md#callVMTransfer) | **PUT** /self/calls/{id}/vmtransfer | Send call to voicemail
[**createCall**](CallsApi.md#createCall) | **POST** /self/calls | Place a call
[**destroyCall**](CallsApi.md#destroyCall) | **DELETE** /self/calls/{id} | End a call
[**getCallsCount**](CallsApi.md#getCallsCount) | **GET** /self/calls/count | Get calls count
[**getRoles**](CallsApi.md#getRoles) | **GET** /self/calls/{id} | Get a call
[**listCalls**](CallsApi.md#listCalls) | **GET** /self/calls | List active calls



## callAnswer

> Call callAnswer(id)

Answer call (On supported devices)

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.CallsApi();
let id = "id_example"; // String | Unique identifier of the call
apiInstance.callAnswer(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of the call | 

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## callHold

> Call callHold(id)

Put call on hold

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.CallsApi();
let id = "id_example"; // String | Unique identifier of the call
apiInstance.callHold(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of the call | 

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## callTransfer

> Call callTransfer(id, callTransfer)

Transfer call

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.CallsApi();
let id = "id_example"; // String | Unique identifier of the call
let callTransfer = new VonageIntegrationSuite.CallTransfer(); // CallTransfer | Call transfer parameters
apiInstance.callTransfer(id, callTransfer, (error, data, response) => {
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
 **id** | **String**| Unique identifier of the call | 
 **callTransfer** | [**CallTransfer**](CallTransfer.md)| Call transfer parameters | 

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## callUnold

> Call callUnold(id)

Unhold

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.CallsApi();
let id = "id_example"; // String | Unique identifier of the call
apiInstance.callUnold(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of the call | 

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## callVMTransfer

> Call callVMTransfer(id)

Send call to voicemail

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.CallsApi();
let id = "id_example"; // String | Unique identifier of the call
apiInstance.callVMTransfer(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of the call | 

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createCall

> [Call] createCall(callCreate)

Place a call

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.CallsApi();
let callCreate = new VonageIntegrationSuite.CallCreate(); // CallCreate | Place call parameters
apiInstance.createCall(callCreate, (error, data, response) => {
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
 **callCreate** | [**CallCreate**](CallCreate.md)| Place call parameters | 

### Return type

[**[Call]**](Call.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## destroyCall

> [Call] destroyCall(id)

End a call

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.CallsApi();
let id = "id_example"; // String | Unique identifier of the call
apiInstance.destroyCall(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of the call | 

### Return type

[**[Call]**](Call.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCallsCount

> EventsCount getCallsCount(opts)

Get calls count

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.CallsApi();
let opts = {
  'fromDate': 56, // Number | Return calls that occurred after this point in time
  'toDate': 56, // Number | Return calls that occurred before this point in time
  'direction': "INBOUND,OUTBOUND", // String | Filter by call direction. For multiple criteria, seperate values by a comma.
  'states': "ACTIVE,RINGING" // String | Filter calls by state. For multiple criteria, seperate values by a comma.
};
apiInstance.getCallsCount(opts, (error, data, response) => {
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
 **fromDate** | **Number**| Return calls that occurred after this point in time | [optional] 
 **toDate** | **Number**| Return calls that occurred before this point in time | [optional] 
 **direction** | **String**| Filter by call direction. For multiple criteria, seperate values by a comma. | [optional] 
 **states** | **String**| Filter calls by state. For multiple criteria, seperate values by a comma. | [optional] [default to &#39;ACTIVE&#39;]

### Return type

[**EventsCount**](EventsCount.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRoles

> [Call] getRoles(id)

Get a call

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.CallsApi();
let id = "id_example"; // String | Unique identifier of the call
apiInstance.getRoles(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of the call | 

### Return type

[**[Call]**](Call.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCalls

> [Call] listCalls(opts)

List active calls

Lists currently active calls

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.CallsApi();
let opts = {
  'fromDate': 56, // Number | Return calls that occurred after this point in time
  'toDate': 56, // Number | Return calls that occurred before this point in time
  'direction': "INBOUND,OUTBOUND", // String | Filter by call direction. For multiple criteria, seperate values by a comma.
  'states': "ACTIVE,RINGING", // String | Filter calls by state. For multiple criteria, seperate values by a comma.
  'offset': 789, // Number | Page number of calls to return
  'size': 20, // Number | Return this amount of calls in the response
  'order': "'ASC'", // String | Sort in either ascending or descending order
  'sort': "sort_example" // String | Sort calls by property
};
apiInstance.listCalls(opts, (error, data, response) => {
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
 **fromDate** | **Number**| Return calls that occurred after this point in time | [optional] 
 **toDate** | **Number**| Return calls that occurred before this point in time | [optional] 
 **direction** | **String**| Filter by call direction. For multiple criteria, seperate values by a comma. | [optional] 
 **states** | **String**| Filter calls by state. For multiple criteria, seperate values by a comma. | [optional] [default to &#39;ACTIVE&#39;]
 **offset** | **Number**| Page number of calls to return | [optional] 
 **size** | **Number**| Return this amount of calls in the response | [optional] [default to 20]
 **order** | **String**| Sort in either ascending or descending order | [optional] [default to &#39;ASC&#39;]
 **sort** | **String**| Sort calls by property | [optional] 

### Return type

[**[Call]**](Call.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


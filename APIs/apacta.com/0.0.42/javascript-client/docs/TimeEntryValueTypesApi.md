# Apacta.TimeEntryValueTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeEntryValueTypesGet**](TimeEntryValueTypesApi.md#timeEntryValueTypesGet) | **GET** /time_entry_value_types | List possible time entry value types
[**timeEntryValueTypesTimeEntryValueTypeIdGet**](TimeEntryValueTypesApi.md#timeEntryValueTypesTimeEntryValueTypeIdGet) | **GET** /time_entry_value_types/{time_entry_value_type_id} | View time entry value type



## timeEntryValueTypesGet

> TimeEntryValueTypesGet200Response timeEntryValueTypesGet()

List possible time entry value types

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.TimeEntryValueTypesApi();
apiInstance.timeEntryValueTypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TimeEntryValueTypesGet200Response**](TimeEntryValueTypesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntryValueTypesTimeEntryValueTypeIdGet

> TimeEntryValueTypesTimeEntryValueTypeIdGet200Response timeEntryValueTypesTimeEntryValueTypeIdGet(timeEntryValueTypeId)

View time entry value type

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.TimeEntryValueTypesApi();
let timeEntryValueTypeId = "timeEntryValueTypeId_example"; // String | 
apiInstance.timeEntryValueTypesTimeEntryValueTypeIdGet(timeEntryValueTypeId, (error, data, response) => {
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
 **timeEntryValueTypeId** | **String**|  | 

### Return type

[**TimeEntryValueTypesTimeEntryValueTypeIdGet200Response**](TimeEntryValueTypesTimeEntryValueTypeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


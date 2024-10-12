# Apacta.TimeEntryUnitTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeEntryUnitTypesGet**](TimeEntryUnitTypesApi.md#timeEntryUnitTypesGet) | **GET** /time_entry_unit_types | List possible time entry unit types
[**timeEntryUnitTypesTimeEntryUnitTypeIdGet**](TimeEntryUnitTypesApi.md#timeEntryUnitTypesTimeEntryUnitTypeIdGet) | **GET** /time_entry_unit_types/{time_entry_unit_type_id} | View time entry unit type



## timeEntryUnitTypesGet

> TimeEntryUnitTypesGet200Response timeEntryUnitTypesGet()

List possible time entry unit types

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

let apiInstance = new Apacta.TimeEntryUnitTypesApi();
apiInstance.timeEntryUnitTypesGet((error, data, response) => {
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

[**TimeEntryUnitTypesGet200Response**](TimeEntryUnitTypesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntryUnitTypesTimeEntryUnitTypeIdGet

> TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response timeEntryUnitTypesTimeEntryUnitTypeIdGet(timeEntryUnitTypeId)

View time entry unit type

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

let apiInstance = new Apacta.TimeEntryUnitTypesApi();
let timeEntryUnitTypeId = "timeEntryUnitTypeId_example"; // String | 
apiInstance.timeEntryUnitTypesTimeEntryUnitTypeIdGet(timeEntryUnitTypeId, (error, data, response) => {
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
 **timeEntryUnitTypeId** | **String**|  | 

### Return type

[**TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response**](TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


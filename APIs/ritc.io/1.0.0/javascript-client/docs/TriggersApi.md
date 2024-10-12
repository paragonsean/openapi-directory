# Ritc.TriggersApi

All URIs are relative to *https://api.ritc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTrigger**](TriggersApi.md#addTrigger) | **POST** /triggers | 
[**getTrigger**](TriggersApi.md#getTrigger) | **GET** /triggers/{trigger_id} | 
[**listTriggers**](TriggersApi.md#listTriggers) | **GET** /triggers | 
[**removeTrigger**](TriggersApi.md#removeTrigger) | **DELETE** /triggers/{trigger_id} | 
[**updateTrigger**](TriggersApi.md#updateTrigger) | **PATCH** /triggers/{trigger_id} | 



## addTrigger

> TriggerShortResponse addTrigger(triggerObject)



Create a new trigger in an app

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.TriggersApi();
let triggerObject = new Ritc.Trigger54(); // Trigger54 | Trigger parameters and configuration
apiInstance.addTrigger(triggerObject, (error, data, response) => {
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
 **triggerObject** | [**Trigger54**](Trigger54.md)| Trigger parameters and configuration | 

### Return type

[**TriggerShortResponse**](TriggerShortResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTrigger

> [TriggerFullResponse] getTrigger(triggerId)



Get a trigger

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.TriggersApi();
let triggerId = "triggerId_example"; // String | Id of Trigger
apiInstance.getTrigger(triggerId, (error, data, response) => {
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
 **triggerId** | **String**| Id of Trigger | 

### Return type

[**[TriggerFullResponse]**](TriggerFullResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTriggers

> [TriggerShortResponse] listTriggers()



Triggers in an app

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.TriggersApi();
apiInstance.listTriggers((error, data, response) => {
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

[**[TriggerShortResponse]**](TriggerShortResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeTrigger

> removeTrigger(triggerId)



Delete a trigger

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.TriggersApi();
let triggerId = "triggerId_example"; // String | Id of Trigger
apiInstance.removeTrigger(triggerId, (error, data, response) => {
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
 **triggerId** | **String**| Id of Trigger | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTrigger

> TriggerShortResponse updateTrigger(triggerId, triggerObject)



Update a trigger

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.TriggersApi();
let triggerId = "triggerId_example"; // String | Id of user
let triggerObject = new Ritc.Trigger54(); // Trigger54 | Trigger information
apiInstance.updateTrigger(triggerId, triggerObject, (error, data, response) => {
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
 **triggerId** | **String**| Id of user | 
 **triggerObject** | [**Trigger54**](Trigger54.md)| Trigger information | 

### Return type

[**TriggerShortResponse**](TriggerShortResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


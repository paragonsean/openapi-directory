# Mailscript.TriggersApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTrigger**](TriggersApi.md#addTrigger) | **POST** /triggers | Setup a trigger
[**deleteTrigger**](TriggersApi.md#deleteTrigger) | **DELETE** /triggers/{trigger} | Delete a trigger
[**getAllTriggers**](TriggersApi.md#getAllTriggers) | **GET** /triggers | Get all triggers you have access to
[**updateTrigger**](TriggersApi.md#updateTrigger) | **PUT** /triggers/{trigger} | Update a trigger



## addTrigger

> AddTriggerResponse addTrigger(addTriggerRequest)

Setup a trigger



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.TriggersApi();
let addTriggerRequest = new Mailscript.AddTriggerRequest(); // AddTriggerRequest | Trigger body
apiInstance.addTrigger(addTriggerRequest, (error, data, response) => {
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
 **addTriggerRequest** | [**AddTriggerRequest**](AddTriggerRequest.md)| Trigger body | 

### Return type

[**AddTriggerResponse**](AddTriggerResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTrigger

> deleteTrigger(trigger)

Delete a trigger

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.TriggersApi();
let trigger = "trigger_example"; // String | ID of the trigger
apiInstance.deleteTrigger(trigger, (error, data, response) => {
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
 **trigger** | **String**| ID of the trigger | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllTriggers

> GetAllTriggersResponse getAllTriggers()

Get all triggers you have access to



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.TriggersApi();
apiInstance.getAllTriggers((error, data, response) => {
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

[**GetAllTriggersResponse**](GetAllTriggersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTrigger

> updateTrigger(trigger, addTriggerRequest)

Update a trigger

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.TriggersApi();
let trigger = "trigger_example"; // String | ID of the trigger
let addTriggerRequest = new Mailscript.AddTriggerRequest(); // AddTriggerRequest | Trigger body
apiInstance.updateTrigger(trigger, addTriggerRequest, (error, data, response) => {
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
 **trigger** | **String**| ID of the trigger | 
 **addTriggerRequest** | [**AddTriggerRequest**](AddTriggerRequest.md)| Trigger body | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


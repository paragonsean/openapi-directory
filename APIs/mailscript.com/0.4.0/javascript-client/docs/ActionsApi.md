# Mailscript.ActionsApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addAction**](ActionsApi.md#addAction) | **POST** /actions | Add an action
[**deleteAction**](ActionsApi.md#deleteAction) | **DELETE** /actions/{action} | Delete an action
[**getAllActions**](ActionsApi.md#getAllActions) | **GET** /actions | Get all actions for the user
[**updateAction**](ActionsApi.md#updateAction) | **PUT** /actions/{action} | Update an action key



## addAction

> AddActionResponse addAction(addActionRequest)

Add an action

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.ActionsApi();
let addActionRequest = new Mailscript.AddActionRequest(); // AddActionRequest | Add action body
apiInstance.addAction(addActionRequest, (error, data, response) => {
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
 **addActionRequest** | [**AddActionRequest**](AddActionRequest.md)| Add action body | 

### Return type

[**AddActionResponse**](AddActionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAction

> deleteAction(action)

Delete an action

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.ActionsApi();
let action = "action_example"; // String | ID of the action
apiInstance.deleteAction(action, (error, data, response) => {
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
 **action** | **String**| ID of the action | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllActions

> GetAllActionsResponse getAllActions()

Get all actions for the user

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.ActionsApi();
apiInstance.getAllActions((error, data, response) => {
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

[**GetAllActionsResponse**](GetAllActionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAction

> Key updateAction(action, addActionRequest)

Update an action key

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.ActionsApi();
let action = "action_example"; // String | ID of action
let addActionRequest = new Mailscript.AddActionRequest(); // AddActionRequest | Action body
apiInstance.updateAction(action, addActionRequest, (error, data, response) => {
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
 **action** | **String**| ID of action | 
 **addActionRequest** | [**AddActionRequest**](AddActionRequest.md)| Action body | 

### Return type

[**Key**](Key.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


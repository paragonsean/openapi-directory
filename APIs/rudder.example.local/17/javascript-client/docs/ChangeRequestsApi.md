# RudderApi.ChangeRequestsApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptChangeRequest**](ChangeRequestsApi.md#acceptChangeRequest) | **POST** /changeRequests/{changeRequestId}/accept | Accept a request details
[**changeRequestDetails**](ChangeRequestsApi.md#changeRequestDetails) | **GET** /changeRequests/{changeRequestId} | Get a change request details
[**declineChangeRequest**](ChangeRequestsApi.md#declineChangeRequest) | **DELETE** /changeRequests/{changeRequestId} | Decline a request details
[**listChangeRequests**](ChangeRequestsApi.md#listChangeRequests) | **GET** /api/changeRequests | List all change requests
[**listUsers**](ChangeRequestsApi.md#listUsers) | **GET** /users | List user
[**removeValidatedUser**](ChangeRequestsApi.md#removeValidatedUser) | **DELETE** /validatedUsers/{username} | Remove an user from validated user list
[**saveWorkflowUser**](ChangeRequestsApi.md#saveWorkflowUser) | **POST** /validatedUsers | Update validated user list
[**updateChangeRequest**](ChangeRequestsApi.md#updateChangeRequest) | **POST** /changeRequests/{changeRequestId} | Update a request details



## acceptChangeRequest

> AcceptChangeRequest200Response acceptChangeRequest(changeRequestId, acceptChangeRequestRequest)

Accept a request details

Accept a change request

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ChangeRequestsApi();
let changeRequestId = 37; // Number | 
let acceptChangeRequestRequest = new RudderApi.AcceptChangeRequestRequest(); // AcceptChangeRequestRequest | 
apiInstance.acceptChangeRequest(changeRequestId, acceptChangeRequestRequest, (error, data, response) => {
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
 **changeRequestId** | **Number**|  | 
 **acceptChangeRequestRequest** | [**AcceptChangeRequestRequest**](AcceptChangeRequestRequest.md)|  | 

### Return type

[**AcceptChangeRequest200Response**](AcceptChangeRequest200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changeRequestDetails

> ChangeRequestDetails200Response changeRequestDetails(changeRequestId)

Get a change request details

Get a change request details

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ChangeRequestsApi();
let changeRequestId = 37; // Number | 
apiInstance.changeRequestDetails(changeRequestId, (error, data, response) => {
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
 **changeRequestId** | **Number**|  | 

### Return type

[**ChangeRequestDetails200Response**](ChangeRequestDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## declineChangeRequest

> DeclineChangeRequest200Response declineChangeRequest(changeRequestId)

Decline a request details

Refuse a change request

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ChangeRequestsApi();
let changeRequestId = 37; // Number | 
apiInstance.declineChangeRequest(changeRequestId, (error, data, response) => {
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
 **changeRequestId** | **Number**|  | 

### Return type

[**DeclineChangeRequest200Response**](DeclineChangeRequest200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChangeRequests

> ListChangeRequests200Response listChangeRequests()

List all change requests

List all change requests

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ChangeRequestsApi();
apiInstance.listChangeRequests((error, data, response) => {
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

[**ListChangeRequests200Response**](ListChangeRequests200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsers

> ListUsers200Response listUsers()

List user

List all validated and unvalidated users

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ChangeRequestsApi();
apiInstance.listUsers((error, data, response) => {
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

[**ListUsers200Response**](ListUsers200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeValidatedUser

> RemoveValidatedUser200Response removeValidatedUser(username)

Remove an user from validated user list

The user is again subject to workflow validation

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ChangeRequestsApi();
let username = "JaneDoe"; // String | Username of an user (unique)
apiInstance.removeValidatedUser(username, (error, data, response) => {
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
 **username** | **String**| Username of an user (unique) | 

### Return type

[**RemoveValidatedUser200Response**](RemoveValidatedUser200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveWorkflowUser

> SaveWorkflowUser200Response saveWorkflowUser(saveWorkflowUserRequest)

Update validated user list

Add and remove user from validated users

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ChangeRequestsApi();
let saveWorkflowUserRequest = new RudderApi.SaveWorkflowUserRequest(); // SaveWorkflowUserRequest | 
apiInstance.saveWorkflowUser(saveWorkflowUserRequest, (error, data, response) => {
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
 **saveWorkflowUserRequest** | [**SaveWorkflowUserRequest**](SaveWorkflowUserRequest.md)|  | 

### Return type

[**SaveWorkflowUser200Response**](SaveWorkflowUser200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChangeRequest

> UpdateChangeRequest200Response updateChangeRequest(changeRequestId, updateChangeRequestRequest)

Update a request details

Update a change request

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ChangeRequestsApi();
let changeRequestId = 37; // Number | 
let updateChangeRequestRequest = new RudderApi.UpdateChangeRequestRequest(); // UpdateChangeRequestRequest | 
apiInstance.updateChangeRequest(changeRequestId, updateChangeRequestRequest, (error, data, response) => {
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
 **changeRequestId** | **Number**|  | 
 **updateChangeRequestRequest** | [**UpdateChangeRequestRequest**](UpdateChangeRequestRequest.md)|  | 

### Return type

[**UpdateChangeRequest200Response**](UpdateChangeRequest200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


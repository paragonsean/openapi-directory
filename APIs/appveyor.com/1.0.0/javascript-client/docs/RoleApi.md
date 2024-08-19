# AppVeyorRestApi.RoleApi

All URIs are relative to *https://ci.appveyor.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addRole**](RoleApi.md#addRole) | **POST** /roles | Add role
[**deleteRole**](RoleApi.md#deleteRole) | **DELETE** /roles/{roleId} | Delete role
[**getRole**](RoleApi.md#getRole) | **GET** /roles/{roleId} | Get role
[**getRoles**](RoleApi.md#getRoles) | **GET** /roles | Get roles
[**updateRole**](RoleApi.md#updateRole) | **PUT** /roles | Update role



## addRole

> RoleWithGroups addRole(body)

Add role

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.RoleApi();
let body = new AppVeyorRestApi.RoleAddition(); // RoleAddition | 
apiInstance.addRole(body, (error, data, response) => {
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
 **body** | [**RoleAddition**](RoleAddition.md)|  | 

### Return type

[**RoleWithGroups**](RoleWithGroups.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## deleteRole

> deleteRole(roleId)

Delete role

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.RoleApi();
let roleId = 56; // Number | Role ID
apiInstance.deleteRole(roleId, (error, data, response) => {
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
 **roleId** | **Number**| Role ID | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRole

> RoleWithGroups getRole(roleId)

Get role

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.RoleApi();
let roleId = 56; // Number | Role ID
apiInstance.getRole(roleId, (error, data, response) => {
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
 **roleId** | **Number**| Role ID | 

### Return type

[**RoleWithGroups**](RoleWithGroups.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRoles

> [Role] getRoles()

Get roles

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.RoleApi();
apiInstance.getRoles((error, data, response) => {
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

[**[Role]**](Role.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateRole

> RoleWithGroups updateRole(body)

Update role

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.RoleApi();
let body = new AppVeyorRestApi.RoleWithGroups(); // RoleWithGroups | 
apiInstance.updateRole(body, (error, data, response) => {
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
 **body** | [**RoleWithGroups**](RoleWithGroups.md)|  | 

### Return type

[**RoleWithGroups**](RoleWithGroups.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


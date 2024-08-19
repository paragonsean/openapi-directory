# AdafruitIoRestApi.PermissionsApi

All URIs are relative to *https://io.adafruit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allPermissions**](PermissionsApi.md#allPermissions) | **GET** /{username}/{type}/{type_id}/acl | All permissions for current user and type
[**createPermission**](PermissionsApi.md#createPermission) | **POST** /{username}/{type}/{type_id}/acl | Create a new Permission
[**destroyPermission**](PermissionsApi.md#destroyPermission) | **DELETE** /{username}/{type}/{type_id}/acl/{id} | Delete an existing Permission
[**getPermission**](PermissionsApi.md#getPermission) | **GET** /{username}/{type}/{type_id}/acl/{id} | Returns Permission based on ID
[**replacePermission**](PermissionsApi.md#replacePermission) | **PUT** /{username}/{type}/{type_id}/acl/{id} | Replace an existing Permission
[**updatePermission**](PermissionsApi.md#updatePermission) | **PATCH** /{username}/{type}/{type_id}/acl/{id} | Update properties of an existing Permission



## allPermissions

> [Permission] allPermissions(username, type, typeId)

All permissions for current user and type

The Permissions endpoint returns information about the user&#39;s permissions. 

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.PermissionsApi();
let username = "username_example"; // String | a valid username string
let type = "type_example"; // String | 
let typeId = "typeId_example"; // String | 
apiInstance.allPermissions(username, type, typeId, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **type** | **String**|  | 
 **typeId** | **String**|  | 

### Return type

[**[Permission]**](Permission.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## createPermission

> Permission createPermission(username, type, typeId, permission)

Create a new Permission

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.PermissionsApi();
let username = "username_example"; // String | a valid username string
let type = "type_example"; // String | 
let typeId = "typeId_example"; // String | 
let permission = new AdafruitIoRestApi.CreatePermissionRequest(); // CreatePermissionRequest | 
apiInstance.createPermission(username, type, typeId, permission, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **type** | **String**|  | 
 **typeId** | **String**|  | 
 **permission** | [**CreatePermissionRequest**](CreatePermissionRequest.md)|  | 

### Return type

[**Permission**](Permission.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## destroyPermission

> String destroyPermission(username, type, typeId, id)

Delete an existing Permission

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.PermissionsApi();
let username = "username_example"; // String | a valid username string
let type = "type_example"; // String | 
let typeId = "typeId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.destroyPermission(username, type, typeId, id, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **type** | **String**|  | 
 **typeId** | **String**|  | 
 **id** | **String**|  | 

### Return type

**String**

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## getPermission

> Permission getPermission(username, type, typeId, id)

Returns Permission based on ID

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.PermissionsApi();
let username = "username_example"; // String | a valid username string
let type = "type_example"; // String | 
let typeId = "typeId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getPermission(username, type, typeId, id, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **type** | **String**|  | 
 **typeId** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**Permission**](Permission.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## replacePermission

> Permission replacePermission(username, type, typeId, id, permission)

Replace an existing Permission

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.PermissionsApi();
let username = "username_example"; // String | a valid username string
let type = "type_example"; // String | 
let typeId = "typeId_example"; // String | 
let id = "id_example"; // String | 
let permission = new AdafruitIoRestApi.CreatePermissionRequest(); // CreatePermissionRequest | 
apiInstance.replacePermission(username, type, typeId, id, permission, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **type** | **String**|  | 
 **typeId** | **String**|  | 
 **id** | **String**|  | 
 **permission** | [**CreatePermissionRequest**](CreatePermissionRequest.md)|  | 

### Return type

[**Permission**](Permission.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## updatePermission

> Permission updatePermission(username, type, typeId, id, permission)

Update properties of an existing Permission

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.PermissionsApi();
let username = "username_example"; // String | a valid username string
let type = "type_example"; // String | 
let typeId = "typeId_example"; // String | 
let id = "id_example"; // String | 
let permission = new AdafruitIoRestApi.CreatePermissionRequest(); // CreatePermissionRequest | 
apiInstance.updatePermission(username, type, typeId, id, permission, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **type** | **String**|  | 
 **typeId** | **String**|  | 
 **id** | **String**|  | 
 **permission** | [**CreatePermissionRequest**](CreatePermissionRequest.md)|  | 

### Return type

[**Permission**](Permission.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


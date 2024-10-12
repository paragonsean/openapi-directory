# RubrikRestApi.UserDefinedTagApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUserDefinedTag**](UserDefinedTagApi.md#createUserDefinedTag) | **POST** /user_defined_tag | Create a user-defined resource tag for tagging cloud compute resources
[**deleteUserDefinedTag**](UserDefinedTagApi.md#deleteUserDefinedTag) | **DELETE** /user_defined_tag/{id} | Delete a user-defined resource tag
[**deleteUserDefinedTagBulk**](UserDefinedTagApi.md#deleteUserDefinedTagBulk) | **DELETE** /user_defined_tag | Delete a list of user-defined resource tags
[**getUserDefinedTag**](UserDefinedTagApi.md#getUserDefinedTag) | **GET** /user_defined_tag/{id} | Get user-defined tag
[**queryUserDefinedTag**](UserDefinedTagApi.md#queryUserDefinedTag) | **GET** /user_defined_tag | Get user-defined resource tags
[**updateUserDefinedTag**](UserDefinedTagApi.md#updateUserDefinedTag) | **PATCH** /user_defined_tag/{id} | Update the value of a user-defined resource tag



## createUserDefinedTag

> ResourceTagDetail createUserDefinedTag(resourceTagDefinition)

Create a user-defined resource tag for tagging cloud compute resources

Create a user-defined resource tag for tagging cloud compute resources created by CloudOn and CloutOut. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserDefinedTagApi();
let resourceTagDefinition = new RubrikRestApi.ResourceTagDefinition(); // ResourceTagDefinition | The definition of a new user-defined resource tag to be created. 
apiInstance.createUserDefinedTag(resourceTagDefinition, (error, data, response) => {
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
 **resourceTagDefinition** | [**ResourceTagDefinition**](ResourceTagDefinition.md)| The definition of a new user-defined resource tag to be created.  | 

### Return type

[**ResourceTagDetail**](ResourceTagDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteUserDefinedTag

> deleteUserDefinedTag(id)

Delete a user-defined resource tag

Delete a user-defined resource tag.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserDefinedTagApi();
let id = "id_example"; // String | ID of the user-defined resource tag.
apiInstance.deleteUserDefinedTag(id, (error, data, response) => {
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
 **id** | **String**| ID of the user-defined resource tag. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteUserDefinedTagBulk

> ResourceTagDeleteResponse deleteUserDefinedTagBulk(ids)

Delete a list of user-defined resource tags

Delete a list of user-defined resource tags in one delete operation. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserDefinedTagApi();
let ids = ["null"]; // [String] | An array of IDs of the user-defined resource tags to be deleted. Any non-existent ID in the array will be ignored. 
apiInstance.deleteUserDefinedTagBulk(ids, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| An array of IDs of the user-defined resource tags to be deleted. Any non-existent ID in the array will be ignored.  | 

### Return type

[**ResourceTagDeleteResponse**](ResourceTagDeleteResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserDefinedTag

> ResourceTagDetail getUserDefinedTag(id)

Get user-defined tag

Retrieve details of a user-defined resource tag.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserDefinedTagApi();
let id = "id_example"; // String | ID of the user-defined resource tag.
apiInstance.getUserDefinedTag(id, (error, data, response) => {
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
 **id** | **String**| ID of the user-defined resource tag. | 

### Return type

[**ResourceTagDetail**](ResourceTagDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryUserDefinedTag

> ResourceTagGetResponse queryUserDefinedTag(opts)

Get user-defined resource tags

Get user-defined resource tags for the cloud compute resources created by CloudOn and CloudOut. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserDefinedTagApi();
let opts = {
  'key': "key_example", // String | Filter results by resource tag.
  'scopeRefId': "scopeRefId_example" // String | Filter results by archival location id.
};
apiInstance.queryUserDefinedTag(opts, (error, data, response) => {
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
 **key** | **String**| Filter results by resource tag. | [optional] 
 **scopeRefId** | **String**| Filter results by archival location id. | [optional] 

### Return type

[**ResourceTagGetResponse**](ResourceTagGetResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUserDefinedTag

> ResourceTagDetail updateUserDefinedTag(id, resourceTagUpdate)

Update the value of a user-defined resource tag

Update the value of a user-defined resource tag. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.UserDefinedTagApi();
let id = "id_example"; // String | ID of the user-defined resource tag.
let resourceTagUpdate = new RubrikRestApi.ResourceTagUpdate(); // ResourceTagUpdate | Properties to update.
apiInstance.updateUserDefinedTag(id, resourceTagUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the user-defined resource tag. | 
 **resourceTagUpdate** | [**ResourceTagUpdate**](ResourceTagUpdate.md)| Properties to update. | 

### Return type

[**ResourceTagDetail**](ResourceTagDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


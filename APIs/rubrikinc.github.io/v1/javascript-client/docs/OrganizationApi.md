# RubrikRestApi.OrganizationApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkCreateEnvoys**](OrganizationApi.md#bulkCreateEnvoys) | **POST** /organization/{id}/envoy/bulk | Create a list of Rubrik Envoy objects
[**bulkDeleteEnvoys**](OrganizationApi.md#bulkDeleteEnvoys) | **DELETE** /organization/{id}/envoy/bulk | Remove a list of Rubrik Envoy objects
[**bulkUpdateEnvoys**](OrganizationApi.md#bulkUpdateEnvoys) | **PATCH** /organization/{id}/envoy/bulk | Update a list of Rubrik Envoy objects



## bulkCreateEnvoys

> EnvoyDetailList bulkCreateEnvoys(id, envoyCreate)

Create a list of Rubrik Envoy objects

Create a list of Rubrik Envoy objects for a specified organization and specify the properties to assign to the Rubrik Envoy objects.

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

let apiInstance = new RubrikRestApi.OrganizationApi();
let id = "id_example"; // String | ID assigned to an organization object.
let envoyCreate = [new RubrikRestApi.EnvoyCreate()]; // [EnvoyCreate] | Properties to assign to the Rubrik Envoy objects.
apiInstance.bulkCreateEnvoys(id, envoyCreate, (error, data, response) => {
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
 **id** | **String**| ID assigned to an organization object. | 
 **envoyCreate** | [**[EnvoyCreate]**](EnvoyCreate.md)| Properties to assign to the Rubrik Envoy objects. | 

### Return type

[**EnvoyDetailList**](EnvoyDetailList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkDeleteEnvoys

> bulkDeleteEnvoys(id, envoyIdList)

Remove a list of Rubrik Envoy objects

Remove a list of Rubrik Envoy objects from an organization and delete the objects from the Rubrik cluster.

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

let apiInstance = new RubrikRestApi.OrganizationApi();
let id = "id_example"; // String | ID assigned to an organization object.
let envoyIdList = new RubrikRestApi.EnvoyIdList(); // EnvoyIdList | A list of Rubrik Envoy objects IDs.
apiInstance.bulkDeleteEnvoys(id, envoyIdList, (error, data, response) => {
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
 **id** | **String**| ID assigned to an organization object. | 
 **envoyIdList** | [**EnvoyIdList**](EnvoyIdList.md)| A list of Rubrik Envoy objects IDs. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## bulkUpdateEnvoys

> EnvoyDetailList bulkUpdateEnvoys(id, envoyBulkUpdate)

Update a list of Rubrik Envoy objects

Change one or more of the properties of a list of Rubrik Envoy objects.

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

let apiInstance = new RubrikRestApi.OrganizationApi();
let id = "id_example"; // String | ID assigned to an organization object.
let envoyBulkUpdate = [new RubrikRestApi.EnvoyBulkUpdate()]; // [EnvoyBulkUpdate] | Properties to assign to the Rubrik Envoy objects.
apiInstance.bulkUpdateEnvoys(id, envoyBulkUpdate, (error, data, response) => {
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
 **id** | **String**| ID assigned to an organization object. | 
 **envoyBulkUpdate** | [**[EnvoyBulkUpdate]**](EnvoyBulkUpdate.md)| Properties to assign to the Rubrik Envoy objects. | 

### Return type

[**EnvoyDetailList**](EnvoyDetailList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


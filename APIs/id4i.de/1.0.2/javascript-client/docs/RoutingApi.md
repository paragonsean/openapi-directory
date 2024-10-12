# Id4iApi.RoutingApi

All URIs are relative to *http://backend.id4i.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllRoutes**](RoutingApi.md#getAllRoutes) | **GET** /api/v1/routingfiles/{id4n}/routes/{type} | Retrieve all routes of a GUID (or ID4N)
[**getRoute**](RoutingApi.md#getRoute) | **GET** /api/v1/routingfiles/{id4n}/route/{type} | Retrieve current route of a GUID (or ID4N)
[**getRoutingFile**](RoutingApi.md#getRoutingFile) | **GET** /api/v1/routingfiles/{id4n} | Retrieve routing file
[**updateRoutingFile**](RoutingApi.md#updateRoutingFile) | **PUT** /api/v1/routingfiles/{id4n} | Store routing file



## getAllRoutes

> [Route] getAllRoutes(id4n, type, opts)

Retrieve all routes of a GUID (or ID4N)

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.RoutingApi();
let id4n = "id4n_example"; // String | id4n
let type = "type_example"; // String | The type of route you want to have
let opts = {
  'organizationId': "organizationId_example", // String | organizationId
  'interpolate': true // Boolean | interpolate
};
apiInstance.getAllRoutes(id4n, type, opts, (error, data, response) => {
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
 **id4n** | **String**| id4n | 
 **type** | **String**| The type of route you want to have | 
 **organizationId** | **String**| organizationId | [optional] 
 **interpolate** | **Boolean**| interpolate | [optional] [default to true]

### Return type

[**[Route]**](Route.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRoute

> Route getRoute(id4n, type, opts)

Retrieve current route of a GUID (or ID4N)

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.RoutingApi();
let id4n = "id4n_example"; // String | id4n
let type = "type_example"; // String | The type of route you want to have
let opts = {
  'privateRoutes': true, // Boolean | privateRoutes
  'publicRoutes': true, // Boolean | publicRoutes
  'interpolate': true // Boolean | interpolate
};
apiInstance.getRoute(id4n, type, opts, (error, data, response) => {
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
 **id4n** | **String**| id4n | 
 **type** | **String**| The type of route you want to have | 
 **privateRoutes** | **Boolean**| privateRoutes | [optional] [default to true]
 **publicRoutes** | **Boolean**| publicRoutes | [optional] [default to true]
 **interpolate** | **Boolean**| interpolate | [optional] [default to true]

### Return type

[**Route**](Route.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRoutingFile

> RoutingFile getRoutingFile(id4n, opts)

Retrieve routing file

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.RoutingApi();
let id4n = "id4n_example"; // String | id4n
let opts = {
  'organizationId': "organizationId_example" // String | organizationId
};
apiInstance.getRoutingFile(id4n, opts, (error, data, response) => {
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
 **id4n** | **String**| id4n | 
 **organizationId** | **String**| organizationId | [optional] 

### Return type

[**RoutingFile**](RoutingFile.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateRoutingFile

> updateRoutingFile(id4n, routingFileRequest)

Store routing file

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.RoutingApi();
let id4n = "id4n_example"; // String | id4n
let routingFileRequest = new Id4iApi.RoutingFileRequest(); // RoutingFileRequest | rfr
apiInstance.updateRoutingFile(id4n, routingFileRequest, (error, data, response) => {
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
 **id4n** | **String**| id4n | 
 **routingFileRequest** | [**RoutingFileRequest**](RoutingFileRequest.md)| rfr | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


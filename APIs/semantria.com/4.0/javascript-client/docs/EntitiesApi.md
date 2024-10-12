# Semantria.EntitiesApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addEntities**](EntitiesApi.md#addEntities) | **POST** /entities.{content_type} | Add user entities
[**deleteEntities**](EntitiesApi.md#deleteEntities) | **DELETE** /entities.{content_type} | Remove user entities
[**getEntities**](EntitiesApi.md#getEntities) | **GET** /entities.{content_type} | Retrieve user entities
[**updateEntities**](EntitiesApi.md#updateEntities) | **PUT** /entities.{content_type} | Update user entities



## addEntities

> [EntityResponseVersion] addEntities(contentType, userEntities, opts)

Add user entities

This method adds user entities on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.EntitiesApi();
let contentType = "contentType_example"; // String | 
let userEntities = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration user entities linked to.
};
apiInstance.addEntities(contentType, userEntities, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **userEntities** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration user entities linked to. | [optional] 

### Return type

[**[EntityResponseVersion]**](EntityResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteEntities

> deleteEntities(contentType)

Remove user entities

This method removes certain user entities by their names on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.EntitiesApi();
let contentType = "contentType_example"; // String | 
apiInstance.deleteEntities(contentType, (error, data, response) => {
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
 **contentType** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getEntities

> [EntityResponseVersion] getEntities(contentType, opts)

Retrieve user entities

This method retrieves list of user entities available on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.EntitiesApi();
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration user entities linked to.
};
apiInstance.getEntities(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration user entities linked to. | [optional] 

### Return type

[**[EntityResponseVersion]**](EntityResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateEntities

> [EntityResponseVersion] updateEntities(contentType, userEntities, opts)

Update user entities

This method updates user entities by unique IDs on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.EntitiesApi();
let contentType = "contentType_example"; // String | 
let userEntities = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration user entities linked to.
};
apiInstance.updateEntities(contentType, userEntities, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **userEntities** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration user entities linked to. | [optional] 

### Return type

[**[EntityResponseVersion]**](EntityResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


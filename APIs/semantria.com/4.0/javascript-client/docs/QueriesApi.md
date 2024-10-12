# Semantria.QueriesApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addQueries**](QueriesApi.md#addQueries) | **POST** /queries.{content_type} | Add or update queries
[**deleteQueries**](QueriesApi.md#deleteQueries) | **DELETE** /queries.{content_type} | Remove queries
[**getQueries**](QueriesApi.md#getQueries) | **GET** /queries.{content_type} | Retrieve queries
[**updateQueries**](QueriesApi.md#updateQueries) | **PUT** /queries.{content_type} | Update queries



## addQueries

> [QueryResponseVersion] addQueries(contentType, queries, opts)

Add or update queries

This method adds queries on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.QueriesApi();
let contentType = "contentType_example"; // String | 
let queries = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration queries linked to.
};
apiInstance.addQueries(contentType, queries, opts, (error, data, response) => {
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
 **queries** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration queries linked to. | [optional] 

### Return type

[**[QueryResponseVersion]**](QueryResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteQueries

> deleteQueries(contentType, queryIDs, opts)

Remove queries

This method removes certain queries by their IDs on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.QueriesApi();
let contentType = "contentType_example"; // String | 
let queryIDs = ["null"]; // [String] | List of query identifiers.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration queries linked to.
};
apiInstance.deleteQueries(contentType, queryIDs, opts, (error, data, response) => {
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
 **queryIDs** | [**[String]**](String.md)| List of query identifiers. | 
 **configId** | **String**| Identifier of configuration queries linked to. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getQueries

> [QueryResponseVersion] getQueries(contentType, opts)

Retrieve queries

This method retrieves list of queries available on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.QueriesApi();
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration queries linked to.
};
apiInstance.getQueries(contentType, opts, (error, data, response) => {
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
 **configId** | **String**| Identifier of configuration queries linked to. | [optional] 

### Return type

[**[QueryResponseVersion]**](QueryResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateQueries

> [QueryResponseVersion] updateQueries(contentType, queries, opts)

Update queries

This method updates queries by unique IDs on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.QueriesApi();
let contentType = "contentType_example"; // String | 
let queries = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration queries linked to.
};
apiInstance.updateQueries(contentType, queries, opts, (error, data, response) => {
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
 **queries** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration queries linked to. | [optional] 

### Return type

[**[QueryResponseVersion]**](QueryResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


# ExLibrisApis.TestApi

All URIs are relative to *https://api-eu.hosted.exlibrisgroup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAlmawsV1TaskListsTest**](TestApi.md#getAlmawsV1TaskListsTest) | **GET** /almaws/v1/task-lists/test | GET Task-lists Test API
[**postAlmawsV1TaskListsTest**](TestApi.md#postAlmawsV1TaskListsTest) | **POST** /almaws/v1/task-lists/test | POST Task-lists Test API



## getAlmawsV1TaskListsTest

> Object getAlmawsV1TaskListsTest()

GET Task-lists Test API

This API is used to test if the API key was configured correctly.It returns a short XML (no schema available - the output is subject to changes) with the following structure:&lt;test&gt;GET - OK - institutionCode: 01ABC_INST&lt;/test&gt;

### Example

```javascript
import ExLibrisApis from 'ex_libris_apis';
let defaultClient = ExLibrisApis.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ExLibrisApis.TestApi();
apiInstance.getAlmawsV1TaskListsTest((error, data, response) => {
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

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## postAlmawsV1TaskListsTest

> Object postAlmawsV1TaskListsTest()

POST Task-lists Test API

This API is used to test if the API key was configured correctly, including read/write permissions.It returns a short XML (no schema available - the output is subject to changes) with the following structure:&lt;test&gt;POST - OK&lt;/test&gt;

### Example

```javascript
import ExLibrisApis from 'ex_libris_apis';
let defaultClient = ExLibrisApis.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ExLibrisApis.TestApi();
apiInstance.postAlmawsV1TaskListsTest((error, data, response) => {
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

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


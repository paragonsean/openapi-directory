# VismaEConomicOpenApi.ProjectStatusesApi

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllProjectStatuses**](ProjectStatusesApi.md#getAllProjectStatuses) | **GET** /projectstatuses | Retrieve all Project Statuses
[**getNumberOfProjectStatuses**](ProjectStatusesApi.md#getNumberOfProjectStatuses) | **GET** /projectstatuses/count | Retrieve the number of Project Statuses
[**getPageOfProjectStatuses**](ProjectStatusesApi.md#getPageOfProjectStatuses) | **GET** /projectstatuses/paged | Retrieve a page of Project Statuses
[**getProjectStatusById**](ProjectStatusesApi.md#getProjectStatusById) | **GET** /projectstatuses/{number} | Retrieve single Project Status



## getAllProjectStatuses

> ProjectStatusCursorResults getAllProjectStatuses(opts)

Retrieve all Project Statuses

Use this endpoint to retrieve all Project Statuses in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectStatusesApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'filter': "filter_example" // String | 
};
apiInstance.getAllProjectStatuses(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **filter** | **String**|  | [optional] 

### Return type

[**ProjectStatusCursorResults**](ProjectStatusCursorResults.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNumberOfProjectStatuses

> Number getNumberOfProjectStatuses(opts)

Retrieve the number of Project Statuses

Call this endpoint to get the number of Project Statuses. You can use a filtering as well.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectStatusesApi();
let opts = {
  'filter': "filter_example" // String | 
};
apiInstance.getNumberOfProjectStatuses(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] 

### Return type

**Number**

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPageOfProjectStatuses

> [ProjectStatus] getPageOfProjectStatuses(opts)

Retrieve a page of Project Statuses

Use this endpoint to load a page of Project Statuses.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectStatusesApi();
let opts = {
  'filter': "filter_example", // String | 
  'sort': "sort_example", // String | 
  'pageSize': 20, // Number | 
  'skipPages': 0 // Number | 
};
apiInstance.getPageOfProjectStatuses(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] [default to 20]
 **skipPages** | **Number**|  | [optional] [default to 0]

### Return type

[**[ProjectStatus]**](ProjectStatus.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectStatusById

> ProjectStatus getProjectStatusById(number)

Retrieve single Project Status

Use this endpoint to load a single Project Status by id/number.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectStatusesApi();
let number = 56; // Number | 
apiInstance.getProjectStatusById(number, (error, data, response) => {
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
 **number** | **Number**|  | 

### Return type

[**ProjectStatus**](ProjectStatus.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


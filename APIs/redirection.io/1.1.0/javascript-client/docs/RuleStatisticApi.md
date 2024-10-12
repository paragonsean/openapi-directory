# RedirectionIo.RuleStatisticApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRuleStatisticCollection**](RuleStatisticApi.md#getRuleStatisticCollection) | **GET** /rule-statistics | Retrieves the collection of RuleStatistic resources.
[**getRuleStatisticItem**](RuleStatisticApi.md#getRuleStatisticItem) | **GET** /rule-statistics/{id} | Retrieves a RuleStatistic resource.



## getRuleStatisticCollection

> [RuleStatistic] getRuleStatisticCollection(projectId)

Retrieves the collection of RuleStatistic resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleStatisticApi();
let projectId = "projectId_example"; // String | 
apiInstance.getRuleStatisticCollection(projectId, (error, data, response) => {
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
 **projectId** | **String**|  | 

### Return type

[**[RuleStatistic]**](RuleStatistic.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getRuleStatisticItem

> RuleStatistic getRuleStatisticItem(id)

Retrieves a RuleStatistic resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleStatisticApi();
let id = "id_example"; // String | 
apiInstance.getRuleStatisticItem(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**RuleStatistic**](RuleStatistic.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


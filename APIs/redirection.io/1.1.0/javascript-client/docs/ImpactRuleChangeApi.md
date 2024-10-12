# RedirectionIo.ImpactRuleChangeApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getImpactRuleChangeItem**](ImpactRuleChangeApi.md#getImpactRuleChangeItem) | **GET** /impact-rule-changes/{id} | Retrieves a ImpactRuleChange resource.
[**postImpactRuleChangeCollection**](ImpactRuleChangeApi.md#postImpactRuleChangeCollection) | **POST** /impact-rule-changes | Creates a ImpactRuleChange resource.



## getImpactRuleChangeItem

> ImpactRuleChangeRead getImpactRuleChangeItem(id)

Retrieves a ImpactRuleChange resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.ImpactRuleChangeApi();
let id = "id_example"; // String | 
apiInstance.getImpactRuleChangeItem(id, (error, data, response) => {
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

[**ImpactRuleChangeRead**](ImpactRuleChangeRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postImpactRuleChangeCollection

> ImpactRuleChangeRead postImpactRuleChangeCollection(opts)

Creates a ImpactRuleChange resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.ImpactRuleChangeApi();
let opts = {
  'impactRuleChange': new RedirectionIo.ImpactRuleChangeWrite() // ImpactRuleChangeWrite | The new ImpactRuleChange resource
};
apiInstance.postImpactRuleChangeCollection(opts, (error, data, response) => {
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
 **impactRuleChange** | [**ImpactRuleChangeWrite**](ImpactRuleChangeWrite.md)| The new ImpactRuleChange resource | [optional] 

### Return type

[**ImpactRuleChangeRead**](ImpactRuleChangeRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


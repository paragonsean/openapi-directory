# RedirectionIo.RuleChangeApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRuleChangeItem**](RuleChangeApi.md#deleteRuleChangeItem) | **DELETE** /rule-changes/{id} | Removes the RuleChange resource.
[**getRuleChangeCollection**](RuleChangeApi.md#getRuleChangeCollection) | **GET** /rule-changes | Retrieves the collection of RuleChange resources.
[**getRuleChangeItem**](RuleChangeApi.md#getRuleChangeItem) | **GET** /rule-changes/{id} | Retrieves a RuleChange resource.
[**postRuleChangeCollection**](RuleChangeApi.md#postRuleChangeCollection) | **POST** /rule-changes | Creates a RuleChange resource.



## deleteRuleChangeItem

> deleteRuleChangeItem(id)

Removes the RuleChange resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleChangeApi();
let id = "id_example"; // String | 
apiInstance.deleteRuleChangeItem(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRuleChangeCollection

> [RuleChangeRead] getRuleChangeCollection(versionId, opts)

Retrieves the collection of RuleChange resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleChangeApi();
let versionId = "versionId_example"; // String | 
let opts = {
  'page': 56 // Number | The collection page number
};
apiInstance.getRuleChangeCollection(versionId, opts, (error, data, response) => {
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
 **versionId** | **String**|  | 
 **page** | **Number**| The collection page number | [optional] 

### Return type

[**[RuleChangeRead]**](RuleChangeRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getRuleChangeItem

> RuleChangeRead getRuleChangeItem(id)

Retrieves a RuleChange resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleChangeApi();
let id = "id_example"; // String | 
apiInstance.getRuleChangeItem(id, (error, data, response) => {
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

[**RuleChangeRead**](RuleChangeRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postRuleChangeCollection

> RuleChangeRead postRuleChangeCollection(opts)

Creates a RuleChange resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleChangeApi();
let opts = {
  'ruleChange': new RedirectionIo.RuleChangeWrite() // RuleChangeWrite | The new RuleChange resource
};
apiInstance.postRuleChangeCollection(opts, (error, data, response) => {
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
 **ruleChange** | [**RuleChangeWrite**](RuleChangeWrite.md)| The new RuleChange resource | [optional] 

### Return type

[**RuleChangeRead**](RuleChangeRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


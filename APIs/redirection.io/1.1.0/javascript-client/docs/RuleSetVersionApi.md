# RedirectionIo.RuleSetVersionApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clearRuleSetVersionItem**](RuleSetVersionApi.md#clearRuleSetVersionItem) | **POST** /rule-set-versions/{id}/clear | Clear a version
[**getRuleSetVersionCollection**](RuleSetVersionApi.md#getRuleSetVersionCollection) | **GET** /rule-set-versions | Retrieves the collection of RuleSetVersion resources.
[**getRuleSetVersionItem**](RuleSetVersionApi.md#getRuleSetVersionItem) | **GET** /rule-set-versions/{id} | Retrieves a RuleSetVersion resource.
[**publishRuleSetVersionItem**](RuleSetVersionApi.md#publishRuleSetVersionItem) | **POST** /rule-set-versions/{id}/publish | Publish a version



## clearRuleSetVersionItem

> RuleSetVersionRead clearRuleSetVersionItem(id, ruleSetVersion)

Clear a version

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleSetVersionApi();
let id = "id_example"; // String | The id of the version
let ruleSetVersion = new RedirectionIo.RuleSetVersion(); // RuleSetVersion | The new RuleSetVersion resource
apiInstance.clearRuleSetVersionItem(id, ruleSetVersion, (error, data, response) => {
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
 **id** | **String**| The id of the version | 
 **ruleSetVersion** | [**RuleSetVersion**](RuleSetVersion.md)| The new RuleSetVersion resource | 

### Return type

[**RuleSetVersionRead**](RuleSetVersionRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getRuleSetVersionCollection

> [RuleSetVersionRead] getRuleSetVersionCollection(projectId, opts)

Retrieves the collection of RuleSetVersion resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleSetVersionApi();
let projectId = "projectId_example"; // String | 
let opts = {
  'sortCreatedAt': "sortCreatedAt_example", // String | 
  'page': 56 // Number | The collection page number
};
apiInstance.getRuleSetVersionCollection(projectId, opts, (error, data, response) => {
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
 **sortCreatedAt** | **String**|  | [optional] 
 **page** | **Number**| The collection page number | [optional] 

### Return type

[**[RuleSetVersionRead]**](RuleSetVersionRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getRuleSetVersionItem

> RuleSetVersionRead getRuleSetVersionItem(id)

Retrieves a RuleSetVersion resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleSetVersionApi();
let id = "id_example"; // String | 
apiInstance.getRuleSetVersionItem(id, (error, data, response) => {
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

[**RuleSetVersionRead**](RuleSetVersionRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## publishRuleSetVersionItem

> RuleSetVersionRead publishRuleSetVersionItem(id, ruleSetVersion)

Publish a version

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleSetVersionApi();
let id = "id_example"; // String | The id of the version
let ruleSetVersion = new RedirectionIo.RuleSetVersion(); // RuleSetVersion | The new RuleSetVersion resource
apiInstance.publishRuleSetVersionItem(id, ruleSetVersion, (error, data, response) => {
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
 **id** | **String**| The id of the version | 
 **ruleSetVersion** | [**RuleSetVersion**](RuleSetVersion.md)| The new RuleSetVersion resource | 

### Return type

[**RuleSetVersionRead**](RuleSetVersionRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


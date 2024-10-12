# RedirectionIo.RuleApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agentLegacyComplexRuleCollection**](RuleApi.md#agentLegacyComplexRuleCollection) | **GET** /agent-rule-complexes | Retrieves the collection of Rule resources.
[**agentLegacyStraightRuleCollection**](RuleApi.md#agentLegacyStraightRuleCollection) | **GET** /agent-rule-straights | Retrieves the collection of Rule resources.
[**agentRuleCollection**](RuleApi.md#agentRuleCollection) | **GET** /agent-rules | Retrieves the collection of Rule resources.
[**exportRuleCollection**](RuleApi.md#exportRuleCollection) | **GET** /export-rules | Retrieves the collection of Rule resources.
[**getRuleCollection**](RuleApi.md#getRuleCollection) | **GET** /rules | Retrieves the collection of Rule resources.
[**getRuleItem**](RuleApi.md#getRuleItem) | **GET** /rules/{id} | Retrieves a Rule resource.



## agentLegacyComplexRuleCollection

> [RuleRead] agentLegacyComplexRuleCollection(projectId)

Retrieves the collection of Rule resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleApi();
let projectId = "projectId_example"; // String | 
apiInstance.agentLegacyComplexRuleCollection(projectId, (error, data, response) => {
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

[**[RuleRead]**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## agentLegacyStraightRuleCollection

> [RuleRead] agentLegacyStraightRuleCollection(projectId)

Retrieves the collection of Rule resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleApi();
let projectId = "projectId_example"; // String | 
apiInstance.agentLegacyStraightRuleCollection(projectId, (error, data, response) => {
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

[**[RuleRead]**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## agentRuleCollection

> [RuleRead] agentRuleCollection(projectId)

Retrieves the collection of Rule resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleApi();
let projectId = "projectId_example"; // String | 
apiInstance.agentRuleCollection(projectId, (error, data, response) => {
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

[**[RuleRead]**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## exportRuleCollection

> [RuleRead] exportRuleCollection(projectId, opts)

Retrieves the collection of Rule resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleApi();
let projectId = "projectId_example"; // String | 
let opts = {
  'sortId': "sortId_example", // String | 
  'sortViewCount': "sortViewCount_example" // String | 
};
apiInstance.exportRuleCollection(projectId, opts, (error, data, response) => {
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
 **sortId** | **String**|  | [optional] 
 **sortViewCount** | **String**|  | [optional] 

### Return type

[**[RuleRead]**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getRuleCollection

> [RuleRead] getRuleCollection(projectId, opts)

Retrieves the collection of Rule resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleApi();
let projectId = "projectId_example"; // String | 
let opts = {
  'sortId': "sortId_example", // String | 
  'sortViewCount': "sortViewCount_example", // String | 
  'page': 56 // Number | The collection page number
};
apiInstance.getRuleCollection(projectId, opts, (error, data, response) => {
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
 **sortId** | **String**|  | [optional] 
 **sortViewCount** | **String**|  | [optional] 
 **page** | **Number**| The collection page number | [optional] 

### Return type

[**[RuleRead]**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getRuleItem

> RuleRead getRuleItem(id)

Retrieves a Rule resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.RuleApi();
let id = "id_example"; // String | 
apiInstance.getRuleItem(id, (error, data, response) => {
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

[**RuleRead**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


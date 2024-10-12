# Ritc.RulesApi

All URIs are relative to *https://api.ritc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addRule**](RulesApi.md#addRule) | **POST** /rules | 
[**getRule**](RulesApi.md#getRule) | **GET** /rules/{rule_id} | 
[**listRules**](RulesApi.md#listRules) | **GET** /rules | 
[**removeRule**](RulesApi.md#removeRule) | **DELETE** /rules/{rule_id} | 
[**runRule**](RulesApi.md#runRule) | **POST** /rules/{rule_id}/run | 
[**updateRule**](RulesApi.md#updateRule) | **PATCH** /rules/{rule_id} | 



## addRule

> RuleFullResponse addRule(ruleObject)



Create a new rule

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.RulesApi();
let ruleObject = new Ritc.Rule(); // Rule | Rule information
apiInstance.addRule(ruleObject, (error, data, response) => {
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
 **ruleObject** | [**Rule**](Rule.md)| Rule information | 

### Return type

[**RuleFullResponse**](RuleFullResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRule

> [RuleFullResponse] getRule(ruleId)



Get a rule

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.RulesApi();
let ruleId = "ruleId_example"; // String | Id of rule
apiInstance.getRule(ruleId, (error, data, response) => {
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
 **ruleId** | **String**| Id of rule | 

### Return type

[**[RuleFullResponse]**](RuleFullResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRules

> [RuleShortResponse] listRules()



List rules

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.RulesApi();
apiInstance.listRules((error, data, response) => {
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

[**[RuleShortResponse]**](RuleShortResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeRule

> removeRule(ruleId)



Delete a rule

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.RulesApi();
let ruleId = "ruleId_example"; // String | Id of rule
apiInstance.removeRule(ruleId, (error, data, response) => {
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
 **ruleId** | **String**| Id of rule | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runRule

> Object runRule(ruleId, opts)



Run a rule

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.RulesApi();
let ruleId = "ruleId_example"; // String | Id of rule
let opts = {
  'initialData': {key: null} // Object | Initial data
};
apiInstance.runRule(ruleId, opts, (error, data, response) => {
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
 **ruleId** | **String**| Id of rule | 
 **initialData** | **Object**| Initial data | [optional] 

### Return type

**Object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRule

> RuleFullResponse updateRule(ruleId, ruleObject)



Update information about a specific rule

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.RulesApi();
let ruleId = "ruleId_example"; // String | Id of user
let ruleObject = new Ritc.Rule(); // Rule | Rule information
apiInstance.updateRule(ruleId, ruleObject, (error, data, response) => {
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
 **ruleId** | **String**| Id of user | 
 **ruleObject** | [**Rule**](Rule.md)| Rule information | 

### Return type

[**RuleFullResponse**](RuleFullResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


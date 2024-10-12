# RudderApi.RulesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRule**](RulesApi.md#createRule) | **PUT** /rules | Create a rule
[**createRuleCategory**](RulesApi.md#createRuleCategory) | **PUT** /rules/categories | Create a rule category
[**deleteRule**](RulesApi.md#deleteRule) | **DELETE** /rules/{ruleId} | Delete a rule
[**deleteRuleCategory**](RulesApi.md#deleteRuleCategory) | **DELETE** /rules/categories/{ruleCategoryId} | Delete group category
[**getRuleCategoryDetails**](RulesApi.md#getRuleCategoryDetails) | **GET** /rules/categories/{ruleCategoryId} | Get rule category details
[**getRuleTree**](RulesApi.md#getRuleTree) | **GET** /rules/tree | Get rules tree
[**listRules**](RulesApi.md#listRules) | **GET** /rules | List all rules
[**ruleDetails**](RulesApi.md#ruleDetails) | **GET** /rules/{ruleId} | Get a rule details
[**updateRule**](RulesApi.md#updateRule) | **POST** /rules/{ruleId} | Update a rule details
[**updateRuleCategory**](RulesApi.md#updateRuleCategory) | **POST** /rules/categories/{ruleCategoryId} | Update rule category details



## createRule

> CreateRule200Response createRule(opts)

Create a rule

Create a new rule. You can specify a source rule to clone it.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.RulesApi();
let opts = {
  'ruleNew': new RudderApi.RuleNew() // RuleNew | 
};
apiInstance.createRule(opts, (error, data, response) => {
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
 **ruleNew** | [**RuleNew**](RuleNew.md)|  | [optional] 

### Return type

[**CreateRule200Response**](CreateRule200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRuleCategory

> CreateRuleCategory200Response createRuleCategory(ruleCategory)

Create a rule category

Create a new rule category

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.RulesApi();
let ruleCategory = new RudderApi.RuleCategory(); // RuleCategory | 
apiInstance.createRuleCategory(ruleCategory, (error, data, response) => {
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
 **ruleCategory** | [**RuleCategory**](RuleCategory.md)|  | 

### Return type

[**CreateRuleCategory200Response**](CreateRuleCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteRule

> DeleteRule200Response deleteRule(ruleId)

Delete a rule

Delete a rule.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.RulesApi();
let ruleId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target rule
apiInstance.deleteRule(ruleId, (error, data, response) => {
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
 **ruleId** | **String**| Id of the target rule | 

### Return type

[**DeleteRule200Response**](DeleteRule200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRuleCategory

> DeleteRuleCategory200Response deleteRuleCategory(ruleCategoryId)

Delete group category

Delete a group category. It must have no child groups and no children categories.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.RulesApi();
let ruleCategoryId = "e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"; // String | 
apiInstance.deleteRuleCategory(ruleCategoryId, (error, data, response) => {
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
 **ruleCategoryId** | **String**|  | 

### Return type

[**DeleteRuleCategory200Response**](DeleteRuleCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRuleCategoryDetails

> GetRuleCategoryDetails200Response getRuleCategoryDetails(ruleCategoryId)

Get rule category details

Get detailed information about a rule category

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.RulesApi();
let ruleCategoryId = "e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"; // String | 
apiInstance.getRuleCategoryDetails(ruleCategoryId, (error, data, response) => {
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
 **ruleCategoryId** | **String**|  | 

### Return type

[**GetRuleCategoryDetails200Response**](GetRuleCategoryDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRuleTree

> GetRuleTree200Response getRuleTree()

Get rules tree

Get all available rules and their categories in a tree

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.RulesApi();
apiInstance.getRuleTree((error, data, response) => {
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

[**GetRuleTree200Response**](GetRuleTree200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRules

> ListRules200Response listRules()

List all rules

List all rules

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.RulesApi();
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

[**ListRules200Response**](ListRules200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ruleDetails

> RuleDetails200Response ruleDetails(ruleId)

Get a rule details

Get the details of a rule

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.RulesApi();
let ruleId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target rule
apiInstance.ruleDetails(ruleId, (error, data, response) => {
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
 **ruleId** | **String**| Id of the target rule | 

### Return type

[**RuleDetails200Response**](RuleDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRule

> UpdateRule200Response updateRule(ruleId, ruleWithCategory)

Update a rule details

Update the details of a rule

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.RulesApi();
let ruleId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target rule
let ruleWithCategory = new RudderApi.RuleWithCategory(); // RuleWithCategory | 
apiInstance.updateRule(ruleId, ruleWithCategory, (error, data, response) => {
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
 **ruleId** | **String**| Id of the target rule | 
 **ruleWithCategory** | [**RuleWithCategory**](RuleWithCategory.md)|  | 

### Return type

[**UpdateRule200Response**](UpdateRule200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRuleCategory

> UpdateRuleCategory200Response updateRuleCategory(ruleCategoryId, ruleCategoryUpdate)

Update rule category details

Update detailed information about a rule category

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.RulesApi();
let ruleCategoryId = "e0a311fa-f7b2-4f9e-89a9-db517b9c6b90"; // String | 
let ruleCategoryUpdate = new RudderApi.RuleCategoryUpdate(); // RuleCategoryUpdate | 
apiInstance.updateRuleCategory(ruleCategoryId, ruleCategoryUpdate, (error, data, response) => {
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
 **ruleCategoryId** | **String**|  | 
 **ruleCategoryUpdate** | [**RuleCategoryUpdate**](RuleCategoryUpdate.md)|  | 

### Return type

[**UpdateRuleCategory200Response**](UpdateRuleCategory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


# BeezUpMerchantApi.AnalyticsRulesApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRule**](AnalyticsRulesApi.md#createRule) | **POST** /v2/user/analytics/{storeId}/rules | Rule creation
[**deleteRule**](AnalyticsRulesApi.md#deleteRule) | **DELETE** /v2/user/analytics/{storeId}/rules/{ruleId} | Delete Rule
[**disableRule**](AnalyticsRulesApi.md#disableRule) | **POST** /v2/user/analytics/{storeId}/rules/{ruleId}/disable | Disable rule
[**enableRule**](AnalyticsRulesApi.md#enableRule) | **POST** /v2/user/analytics/{storeId}/rules/{ruleId}/enable | Enable rule
[**getRule**](AnalyticsRulesApi.md#getRule) | **GET** /v2/user/analytics/{storeId}/rules/{ruleId} | Gets the rule
[**getRules**](AnalyticsRulesApi.md#getRules) | **GET** /v2/user/analytics/{storeId}/rules | Gets the list of rules for a given store
[**getRulesExecutions**](AnalyticsRulesApi.md#getRulesExecutions) | **GET** /v2/user/analytics/{storeId}/rules/executions | Get the rules execution history
[**moveDownRule**](AnalyticsRulesApi.md#moveDownRule) | **POST** /v2/user/analytics/{storeId}/rules/{ruleId}/movedown | Move the rule down
[**moveUpRule**](AnalyticsRulesApi.md#moveUpRule) | **POST** /v2/user/analytics/{storeId}/rules/{ruleId}/moveup | Move the rule up
[**runRule**](AnalyticsRulesApi.md#runRule) | **POST** /v2/user/analytics/{storeId}/rules/{ruleId}/run | Run rule
[**runRules**](AnalyticsRulesApi.md#runRules) | **POST** /v2/user/analytics/{storeId}/rules/run | Run all rules for this store
[**updateRule**](AnalyticsRulesApi.md#updateRule) | **PATCH** /v2/user/analytics/{storeId}/rules/{ruleId} | Update Rule



## createRule

> createRule(storeId, createRuleRequest)

Rule creation

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
let createRuleRequest = new BeezUpMerchantApi.CreateRuleRequest(); // CreateRuleRequest | 
apiInstance.createRule(storeId, createRuleRequest, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **createRuleRequest** | [**CreateRuleRequest**](CreateRuleRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*, application/json


## deleteRule

> deleteRule(storeId, ruleId)

Delete Rule

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
let ruleId = "ruleId_example"; // String | Your rule identifier
apiInstance.deleteRule(storeId, ruleId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **ruleId** | **String**| Your rule identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disableRule

> disableRule(storeId, ruleId)

Disable rule

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
let ruleId = "ruleId_example"; // String | Your rule identifier
apiInstance.disableRule(storeId, ruleId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **ruleId** | **String**| Your rule identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableRule

> enableRule(storeId, ruleId)

Enable rule

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
let ruleId = "ruleId_example"; // String | Your rule identifier
apiInstance.enableRule(storeId, ruleId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **ruleId** | **String**| Your rule identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRule

> Rule getRule(storeId, ruleId)

Gets the rule

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
let ruleId = "ruleId_example"; // String | Your rule identifier
apiInstance.getRule(storeId, ruleId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **ruleId** | **String**| Your rule identifier | 

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRules

> RuleList getRules(storeId)

Gets the list of rules for a given store

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.getRules(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

[**RuleList**](RuleList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRulesExecutions

> RuleExecutionReportings getRulesExecutions(storeId, pageNumber, pageSize)

Get the rules execution history

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
let pageNumber = 56; // Number | The page to retrieve
let pageSize = 56; // Number | The count of rule history to retrieve
apiInstance.getRulesExecutions(storeId, pageNumber, pageSize, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **pageNumber** | **Number**| The page to retrieve | 
 **pageSize** | **Number**| The count of rule history to retrieve | 

### Return type

[**RuleExecutionReportings**](RuleExecutionReportings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## moveDownRule

> moveDownRule(storeId, ruleId)

Move the rule down

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
let ruleId = "ruleId_example"; // String | Your rule identifier
apiInstance.moveDownRule(storeId, ruleId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **ruleId** | **String**| Your rule identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## moveUpRule

> moveUpRule(storeId, ruleId)

Move the rule up

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
let ruleId = "ruleId_example"; // String | Your rule identifier
apiInstance.moveUpRule(storeId, ruleId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **ruleId** | **String**| Your rule identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runRule

> runRule(storeId, ruleId)

Run rule

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
let ruleId = "ruleId_example"; // String | Your rule identifier
apiInstance.runRule(storeId, ruleId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **ruleId** | **String**| Your rule identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runRules

> runRules(storeId)

Run all rules for this store

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.runRules(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRule

> updateRule(storeId, ruleId, updateRuleRequest)

Update Rule

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.AnalyticsRulesApi();
let storeId = "storeId_example"; // String | Your store identifier
let ruleId = "ruleId_example"; // String | Your rule identifier
let updateRuleRequest = new BeezUpMerchantApi.UpdateRuleRequest(); // UpdateRuleRequest | 
apiInstance.updateRule(storeId, ruleId, updateRuleRequest, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **ruleId** | **String**| Your rule identifier | 
 **updateRuleRequest** | [**UpdateRuleRequest**](UpdateRuleRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


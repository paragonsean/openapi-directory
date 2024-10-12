# ApicurioRegistryApi.GlobalRulesApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGlobalRule**](GlobalRulesApi.md#createGlobalRule) | **POST** /rules | Create global rule
[**deleteAllGlobalRules**](GlobalRulesApi.md#deleteAllGlobalRules) | **DELETE** /rules | Delete all global rules
[**deleteGlobalRule**](GlobalRulesApi.md#deleteGlobalRule) | **DELETE** /rules/{rule} | Delete global rule
[**getGlobalRuleConfig**](GlobalRulesApi.md#getGlobalRuleConfig) | **GET** /rules/{rule} | Get global rule configuration
[**listGlobalRules**](GlobalRulesApi.md#listGlobalRules) | **GET** /rules | List global rules
[**updateGlobalRuleConfig**](GlobalRulesApi.md#updateGlobalRuleConfig) | **PUT** /rules/{rule} | Update global rule configuration



## createGlobalRule

> createGlobalRule(rule)

Create global rule

Adds a rule to the list of globally configured rules.  This operation can fail for the following reasons:  * The rule type is unknown (HTTP error &#x60;400&#x60;) * The rule already exists (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.GlobalRulesApi();
let rule = new ApicurioRegistryApi.Rule(); // Rule | 
apiInstance.createGlobalRule(rule, (error, data, response) => {
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
 **rule** | [**Rule**](Rule.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAllGlobalRules

> deleteAllGlobalRules()

Delete all global rules

Deletes all globally configured rules.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.GlobalRulesApi();
apiInstance.deleteAllGlobalRules((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteGlobalRule

> deleteGlobalRule(rule)

Delete global rule

Deletes a single global rule.  If this is the only rule configured, this is the same as deleting **all** rules.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * Rule cannot be deleted (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.GlobalRulesApi();
let rule = "rule_example"; // String | The unique name/type of a rule.
apiInstance.deleteGlobalRule(rule, (error, data, response) => {
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
 **rule** | **String**| The unique name/type of a rule. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGlobalRuleConfig

> Rule getGlobalRuleConfig(rule)

Get global rule configuration

Returns information about the named globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.GlobalRulesApi();
let rule = "rule_example"; // String | The unique name/type of a rule.
apiInstance.getGlobalRuleConfig(rule, (error, data, response) => {
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
 **rule** | **String**| The unique name/type of a rule. | 

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listGlobalRules

> [RuleType] listGlobalRules()

List global rules

Gets a list of all the currently configured global rules (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.GlobalRulesApi();
apiInstance.listGlobalRules((error, data, response) => {
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

[**[RuleType]**](RuleType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateGlobalRuleConfig

> Rule updateGlobalRuleConfig(rule, rule2)

Update global rule configuration

Updates the configuration for a globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.GlobalRulesApi();
let rule = "rule_example"; // String | The unique name/type of a rule.
let rule2 = new ApicurioRegistryApi.Rule(); // Rule | 
apiInstance.updateGlobalRuleConfig(rule, rule2, (error, data, response) => {
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
 **rule** | **String**| The unique name/type of a rule. | 
 **rule2** | [**Rule**](Rule.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


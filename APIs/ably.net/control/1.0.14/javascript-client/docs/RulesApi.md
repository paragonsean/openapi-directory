# ControlApiV1.RulesApi

All URIs are relative to *https://control.ably.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAppIdRulesGet**](RulesApi.md#appsAppIdRulesGet) | **GET** /apps/{app_id}/rules | Lists Reactor rules
[**appsAppIdRulesPost**](RulesApi.md#appsAppIdRulesPost) | **POST** /apps/{app_id}/rules | Creates a Reactor rule
[**appsAppIdRulesRuleIdDelete**](RulesApi.md#appsAppIdRulesRuleIdDelete) | **DELETE** /apps/{app_id}/rules/{rule_id} | Deletes a Reactor rule
[**appsAppIdRulesRuleIdGet**](RulesApi.md#appsAppIdRulesRuleIdGet) | **GET** /apps/{app_id}/rules/{rule_id} | Gets a reactor rule by rule ID
[**appsAppIdRulesRuleIdPatch**](RulesApi.md#appsAppIdRulesRuleIdPatch) | **PATCH** /apps/{app_id}/rules/{rule_id} | Updates a Reactor rule



## appsAppIdRulesGet

> [RuleResponse] appsAppIdRulesGet(appId)

Lists Reactor rules

Lists the rules for the application specified by the application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.RulesApi();
let appId = "appId_example"; // String | The application ID.
apiInstance.appsAppIdRulesGet(appId, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 

### Return type

[**[RuleResponse]**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdRulesPost

> RuleResponse appsAppIdRulesPost(appId, opts)

Creates a Reactor rule

Creates a rule for the application with the specified application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.RulesApi();
let appId = "appId_example"; // String | The application ID.
let opts = {
  'rulePost': new ControlApiV1.RulePost() // RulePost | The rule properties.
};
apiInstance.appsAppIdRulesPost(appId, opts, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 
 **rulePost** | [**RulePost**](RulePost.md)| The rule properties. | [optional] 

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsAppIdRulesRuleIdDelete

> appsAppIdRulesRuleIdDelete(appId, ruleId)

Deletes a Reactor rule

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.RulesApi();
let appId = "appId_example"; // String | The application ID.
let ruleId = "ruleId_example"; // String | The rule ID.
apiInstance.appsAppIdRulesRuleIdDelete(appId, ruleId, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 
 **ruleId** | **String**| The rule ID. | 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdRulesRuleIdGet

> RuleResponse appsAppIdRulesRuleIdGet(appId, ruleId)

Gets a reactor rule by rule ID

Returns the rule specified by the rule ID, for the application specified by application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.RulesApi();
let appId = "appId_example"; // String | The application ID.
let ruleId = "ruleId_example"; // String | The rule ID.
apiInstance.appsAppIdRulesRuleIdGet(appId, ruleId, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 
 **ruleId** | **String**| The rule ID. | 

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdRulesRuleIdPatch

> RuleResponse appsAppIdRulesRuleIdPatch(appId, ruleId, opts)

Updates a Reactor rule

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.RulesApi();
let appId = "appId_example"; // String | The application ID.
let ruleId = "ruleId_example"; // String | The rule ID.
let opts = {
  'rulePatch': new ControlApiV1.RulePatch() // RulePatch | Properties for the rule.
};
apiInstance.appsAppIdRulesRuleIdPatch(appId, ruleId, opts, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 
 **ruleId** | **String**| The rule ID. | 
 **rulePatch** | [**RulePatch**](RulePatch.md)| Properties for the rule. | [optional] 

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


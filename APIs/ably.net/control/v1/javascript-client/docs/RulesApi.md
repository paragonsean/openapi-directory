# ApiV1.RulesApi

All URIs are relative to *https://control.ably.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAppIdRulesGet**](RulesApi.md#appsAppIdRulesGet) | **GET** /apps/{app_id}/rules | Lists Integration rules
[**appsAppIdRulesPost**](RulesApi.md#appsAppIdRulesPost) | **POST** /apps/{app_id}/rules | Creates a Integration Rule
[**appsAppIdRulesRuleIdDelete**](RulesApi.md#appsAppIdRulesRuleIdDelete) | **DELETE** /apps/{app_id}/rules/{rule_id} | Deletes a Integration Rule
[**appsAppIdRulesRuleIdGet**](RulesApi.md#appsAppIdRulesRuleIdGet) | **GET** /apps/{app_id}/rules/{rule_id} | Gets a Integration Rule by ID
[**appsAppIdRulesRuleIdPatch**](RulesApi.md#appsAppIdRulesRuleIdPatch) | **PATCH** /apps/{app_id}/rules/{rule_id} | Updates a Integration Rule



## appsAppIdRulesGet

> [RuleResponse] appsAppIdRulesGet(appId)

Lists Integration rules

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.RulesApi();
let appId = "appId_example"; // String | 
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
 **appId** | **String**|  | 

### Return type

[**[RuleResponse]**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdRulesPost

> RuleResponse appsAppIdRulesPost(appId, opts)

Creates a Integration Rule

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.RulesApi();
let appId = "appId_example"; // String | 
let opts = {
  'rulePost': new ApiV1.RulePost() // RulePost | 
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
 **appId** | **String**|  | 
 **rulePost** | [**RulePost**](RulePost.md)|  | [optional] 

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsAppIdRulesRuleIdDelete

> appsAppIdRulesRuleIdDelete(appId, ruleId)

Deletes a Integration Rule

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.RulesApi();
let appId = "appId_example"; // String | 
let ruleId = "ruleId_example"; // String | 
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
 **appId** | **String**|  | 
 **ruleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdRulesRuleIdGet

> RuleResponse appsAppIdRulesRuleIdGet(appId, ruleId)

Gets a Integration Rule by ID

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.RulesApi();
let appId = "appId_example"; // String | 
let ruleId = "ruleId_example"; // String | 
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
 **appId** | **String**|  | 
 **ruleId** | **String**|  | 

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdRulesRuleIdPatch

> RuleResponse appsAppIdRulesRuleIdPatch(appId, ruleId, opts)

Updates a Integration Rule

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.RulesApi();
let appId = "appId_example"; // String | 
let ruleId = "ruleId_example"; // String | 
let opts = {
  'rulePatch': new ApiV1.RulePatch() // RulePatch | 
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
 **appId** | **String**|  | 
 **ruleId** | **String**|  | 
 **rulePatch** | [**RulePatch**](RulePatch.md)|  | [optional] 

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


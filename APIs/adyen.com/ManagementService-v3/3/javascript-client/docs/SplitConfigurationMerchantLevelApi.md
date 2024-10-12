# ManagementApi.SplitConfigurationMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**](SplitConfigurationMerchantLevelApi.md#deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId) | **DELETE** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | Delete a split configuration
[**deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId**](SplitConfigurationMerchantLevelApi.md#deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId) | **DELETE** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId} | Delete a split configuration rule
[**getMerchantsMerchantIdSplitConfigurations**](SplitConfigurationMerchantLevelApi.md#getMerchantsMerchantIdSplitConfigurations) | **GET** /merchants/{merchantId}/splitConfigurations | Get a list of split configurations
[**getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**](SplitConfigurationMerchantLevelApi.md#getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId) | **GET** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | Get a split configuration
[**patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**](SplitConfigurationMerchantLevelApi.md#patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId) | **PATCH** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | Update split configuration description
[**patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId**](SplitConfigurationMerchantLevelApi.md#patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId) | **PATCH** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId} | Update split conditions
[**patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId**](SplitConfigurationMerchantLevelApi.md#patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId) | **PATCH** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId}/rules/{ruleId}/splitLogic/{splitLogicId} | Update the split logic
[**postMerchantsMerchantIdSplitConfigurations**](SplitConfigurationMerchantLevelApi.md#postMerchantsMerchantIdSplitConfigurations) | **POST** /merchants/{merchantId}/splitConfigurations | Create a split configuration
[**postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId**](SplitConfigurationMerchantLevelApi.md#postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId) | **POST** /merchants/{merchantId}/splitConfigurations/{splitConfigurationId} | Create a rule



## deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId

> SplitConfiguration deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId)

Delete a split configuration

Deletes the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.SplitConfigurationMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
apiInstance.deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **splitConfigurationId** | **String**| The unique identifier of the split configuration. | 

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId

> SplitConfiguration deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId(merchantId, splitConfigurationId, ruleId)

Delete a split configuration rule

Deletes the split configuration rule specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.SplitConfigurationMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
let ruleId = "ruleId_example"; // String | 
apiInstance.deleteMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId(merchantId, splitConfigurationId, ruleId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **splitConfigurationId** | **String**| The unique identifier of the split configuration. | 
 **ruleId** | **String**|  | 

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdSplitConfigurations

> SplitConfigurationList getMerchantsMerchantIdSplitConfigurations(merchantId)

Get a list of split configurations

Returns the list of split configurations for the merchant account.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.SplitConfigurationMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
apiInstance.getMerchantsMerchantIdSplitConfigurations(merchantId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 

### Return type

[**SplitConfigurationList**](SplitConfigurationList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId

> SplitConfiguration getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId)

Get a split configuration

Returns the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.SplitConfigurationMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
apiInstance.getMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **splitConfigurationId** | **String**| The unique identifier of the split configuration. | 

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId

> SplitConfiguration patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId, opts)

Update split configuration description

Changes the description of the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.SplitConfigurationMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
let opts = {
  'updateSplitConfigurationRequest': new ManagementApi.UpdateSplitConfigurationRequest() // UpdateSplitConfigurationRequest | 
};
apiInstance.patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **splitConfigurationId** | **String**| The unique identifier of the split configuration. | 
 **updateSplitConfigurationRequest** | [**UpdateSplitConfigurationRequest**](UpdateSplitConfigurationRequest.md)|  | [optional] 

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId

> SplitConfiguration patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId(merchantId, splitConfigurationId, ruleId, opts)

Update split conditions

Changes the conditions of the split configuration rule specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.SplitConfigurationMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let splitConfigurationId = "splitConfigurationId_example"; // String | The identifier of the split configuration.
let ruleId = "ruleId_example"; // String | The unique identifier of the split configuration rule.
let opts = {
  'updateSplitConfigurationRuleRequest': new ManagementApi.UpdateSplitConfigurationRuleRequest() // UpdateSplitConfigurationRuleRequest | 
};
apiInstance.patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleId(merchantId, splitConfigurationId, ruleId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **splitConfigurationId** | **String**| The identifier of the split configuration. | 
 **ruleId** | **String**| The unique identifier of the split configuration rule. | 
 **updateSplitConfigurationRuleRequest** | [**UpdateSplitConfigurationRuleRequest**](UpdateSplitConfigurationRuleRequest.md)|  | [optional] 

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId

> SplitConfiguration patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId(merchantId, splitConfigurationId, ruleId, splitLogicId, opts)

Update the split logic

Changes the split logic specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.SplitConfigurationMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
let ruleId = "ruleId_example"; // String | The unique identifier of the split configuration rule.
let splitLogicId = "splitLogicId_example"; // String | The unique identifier of the split configuration split.
let opts = {
  'updateSplitConfigurationLogicRequest': new ManagementApi.UpdateSplitConfigurationLogicRequest() // UpdateSplitConfigurationLogicRequest | 
};
apiInstance.patchMerchantsMerchantIdSplitConfigurationsSplitConfigurationIdRulesRuleIdSplitLogicSplitLogicId(merchantId, splitConfigurationId, ruleId, splitLogicId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **splitConfigurationId** | **String**| The unique identifier of the split configuration. | 
 **ruleId** | **String**| The unique identifier of the split configuration rule. | 
 **splitLogicId** | **String**| The unique identifier of the split configuration split. | 
 **updateSplitConfigurationLogicRequest** | [**UpdateSplitConfigurationLogicRequest**](UpdateSplitConfigurationLogicRequest.md)|  | [optional] 

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMerchantsMerchantIdSplitConfigurations

> SplitConfiguration postMerchantsMerchantIdSplitConfigurations(merchantId, opts)

Create a split configuration

Creates a split configuration for the merchant account specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.SplitConfigurationMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let opts = {
  'splitConfiguration': new ManagementApi.SplitConfiguration() // SplitConfiguration | 
};
apiInstance.postMerchantsMerchantIdSplitConfigurations(merchantId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **splitConfiguration** | [**SplitConfiguration**](SplitConfiguration.md)|  | [optional] 

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId

> SplitConfiguration postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId, opts)

Create a rule

Creates a rule in the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.SplitConfigurationMerchantLevelApi();
let merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
let splitConfigurationId = "splitConfigurationId_example"; // String | The unique identifier of the split configuration.
let opts = {
  'splitConfigurationRule': new ManagementApi.SplitConfigurationRule() // SplitConfigurationRule | 
};
apiInstance.postMerchantsMerchantIdSplitConfigurationsSplitConfigurationId(merchantId, splitConfigurationId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The unique identifier of the merchant account. | 
 **splitConfigurationId** | **String**| The unique identifier of the split configuration. | 
 **splitConfigurationRule** | [**SplitConfigurationRule**](SplitConfigurationRule.md)|  | [optional] 

### Return type

[**SplitConfiguration**](SplitConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


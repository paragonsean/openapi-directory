# ZapierNaturalLanguageActionsNlaApiBeta.DefaultApi

All URIs are relative to *https://nla.zapier.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check**](DefaultApi.md#check) | **GET** /api/v1/check/ | Check
[**executeAppActionEndpoint**](DefaultApi.md#executeAppActionEndpoint) | **POST** /api/v1/exposed/{exposed_app_action_id}/execute/ | Execute App Action Endpoint
[**getConfigurationLink**](DefaultApi.md#getConfigurationLink) | **GET** /api/v1/configuration-link/ | Get Configuration Link
[**getExecutionLogEndpoint**](DefaultApi.md#getExecutionLogEndpoint) | **GET** /api/v1/execution-log/{execution_log_id}/ | Get Execution Log Endpoint
[**listExposedActions**](DefaultApi.md#listExposedActions) | **GET** /api/v1/exposed/ | List Exposed Actions



## check

> check()

Check

Test that the API and auth are working.

### Example

```javascript
import ZapierNaturalLanguageActionsNlaApiBeta from 'zapier_natural_language_actions__nla_api_beta';
let defaultClient = ZapierNaturalLanguageActionsNlaApiBeta.ApiClient.instance;
// Configure API key authorization: AccessPointApiKeyQuery
let AccessPointApiKeyQuery = defaultClient.authentications['AccessPointApiKeyQuery'];
AccessPointApiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AccessPointApiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: SessionAuth
let SessionAuth = defaultClient.authentications['SessionAuth'];
SessionAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SessionAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: AccessPointApiKeyHeader
let AccessPointApiKeyHeader = defaultClient.authentications['AccessPointApiKeyHeader'];
AccessPointApiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AccessPointApiKeyHeader.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: AccessPointOAuth
let AccessPointOAuth = defaultClient.authentications['AccessPointOAuth'];
AccessPointOAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ZapierNaturalLanguageActionsNlaApiBeta.DefaultApi();
apiInstance.check((error, data, response) => {
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

[AccessPointApiKeyQuery](../README.md#AccessPointApiKeyQuery), [SessionAuth](../README.md#SessionAuth), [AccessPointApiKeyHeader](../README.md#AccessPointApiKeyHeader), [AccessPointOAuth](../README.md#AccessPointOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## executeAppActionEndpoint

> ExecuteResponse executeAppActionEndpoint(exposedAppActionId, executeRequest)

Execute App Action Endpoint

Give us a plain english description of exact action you want to do. There should be dynamically generated documentation for this endpoint for each action that is exposed.

### Example

```javascript
import ZapierNaturalLanguageActionsNlaApiBeta from 'zapier_natural_language_actions__nla_api_beta';
let defaultClient = ZapierNaturalLanguageActionsNlaApiBeta.ApiClient.instance;
// Configure API key authorization: AccessPointApiKeyQuery
let AccessPointApiKeyQuery = defaultClient.authentications['AccessPointApiKeyQuery'];
AccessPointApiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AccessPointApiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: SessionAuth
let SessionAuth = defaultClient.authentications['SessionAuth'];
SessionAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SessionAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: AccessPointApiKeyHeader
let AccessPointApiKeyHeader = defaultClient.authentications['AccessPointApiKeyHeader'];
AccessPointApiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AccessPointApiKeyHeader.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: AccessPointOAuth
let AccessPointOAuth = defaultClient.authentications['AccessPointOAuth'];
AccessPointOAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ZapierNaturalLanguageActionsNlaApiBeta.DefaultApi();
let exposedAppActionId = "exposedAppActionId_example"; // String | 
let executeRequest = new ZapierNaturalLanguageActionsNlaApiBeta.ExecuteRequest(); // ExecuteRequest | 
apiInstance.executeAppActionEndpoint(exposedAppActionId, executeRequest, (error, data, response) => {
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
 **exposedAppActionId** | **String**|  | 
 **executeRequest** | [**ExecuteRequest**](ExecuteRequest.md)|  | 

### Return type

[**ExecuteResponse**](ExecuteResponse.md)

### Authorization

[AccessPointApiKeyQuery](../README.md#AccessPointApiKeyQuery), [SessionAuth](../README.md#SessionAuth), [AccessPointApiKeyHeader](../README.md#AccessPointApiKeyHeader), [AccessPointOAuth](../README.md#AccessPointOAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getConfigurationLink

> getConfigurationLink()

Get Configuration Link

Provides a link to configure more actions. Alternatively, searching through apps and actions will provide more specific configuration links.

### Example

```javascript
import ZapierNaturalLanguageActionsNlaApiBeta from 'zapier_natural_language_actions__nla_api_beta';
let defaultClient = ZapierNaturalLanguageActionsNlaApiBeta.ApiClient.instance;
// Configure API key authorization: AccessPointApiKeyQuery
let AccessPointApiKeyQuery = defaultClient.authentications['AccessPointApiKeyQuery'];
AccessPointApiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AccessPointApiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: SessionAuth
let SessionAuth = defaultClient.authentications['SessionAuth'];
SessionAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SessionAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: AccessPointApiKeyHeader
let AccessPointApiKeyHeader = defaultClient.authentications['AccessPointApiKeyHeader'];
AccessPointApiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AccessPointApiKeyHeader.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: AccessPointOAuth
let AccessPointOAuth = defaultClient.authentications['AccessPointOAuth'];
AccessPointOAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ZapierNaturalLanguageActionsNlaApiBeta.DefaultApi();
apiInstance.getConfigurationLink((error, data, response) => {
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

[AccessPointApiKeyQuery](../README.md#AccessPointApiKeyQuery), [SessionAuth](../README.md#SessionAuth), [AccessPointApiKeyHeader](../README.md#AccessPointApiKeyHeader), [AccessPointOAuth](../README.md#AccessPointOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getExecutionLogEndpoint

> ExecuteResponse getExecutionLogEndpoint(executionLogId)

Get Execution Log Endpoint

Get the execution log for a given execution log id.

### Example

```javascript
import ZapierNaturalLanguageActionsNlaApiBeta from 'zapier_natural_language_actions__nla_api_beta';
let defaultClient = ZapierNaturalLanguageActionsNlaApiBeta.ApiClient.instance;
// Configure API key authorization: AccessPointApiKeyQuery
let AccessPointApiKeyQuery = defaultClient.authentications['AccessPointApiKeyQuery'];
AccessPointApiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AccessPointApiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: SessionAuth
let SessionAuth = defaultClient.authentications['SessionAuth'];
SessionAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SessionAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: AccessPointApiKeyHeader
let AccessPointApiKeyHeader = defaultClient.authentications['AccessPointApiKeyHeader'];
AccessPointApiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AccessPointApiKeyHeader.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: AccessPointOAuth
let AccessPointOAuth = defaultClient.authentications['AccessPointOAuth'];
AccessPointOAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ZapierNaturalLanguageActionsNlaApiBeta.DefaultApi();
let executionLogId = "executionLogId_example"; // String | 
apiInstance.getExecutionLogEndpoint(executionLogId, (error, data, response) => {
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
 **executionLogId** | **String**|  | 

### Return type

[**ExecuteResponse**](ExecuteResponse.md)

### Authorization

[AccessPointApiKeyQuery](../README.md#AccessPointApiKeyQuery), [SessionAuth](../README.md#SessionAuth), [AccessPointApiKeyHeader](../README.md#AccessPointApiKeyHeader), [AccessPointOAuth](../README.md#AccessPointOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listExposedActions

> ExposedActionResponseSchema listExposedActions()

List Exposed Actions

List all the currently exposed actions for the given account.

### Example

```javascript
import ZapierNaturalLanguageActionsNlaApiBeta from 'zapier_natural_language_actions__nla_api_beta';
let defaultClient = ZapierNaturalLanguageActionsNlaApiBeta.ApiClient.instance;
// Configure API key authorization: AccessPointApiKeyQuery
let AccessPointApiKeyQuery = defaultClient.authentications['AccessPointApiKeyQuery'];
AccessPointApiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AccessPointApiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: SessionAuth
let SessionAuth = defaultClient.authentications['SessionAuth'];
SessionAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SessionAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: AccessPointApiKeyHeader
let AccessPointApiKeyHeader = defaultClient.authentications['AccessPointApiKeyHeader'];
AccessPointApiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AccessPointApiKeyHeader.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: AccessPointOAuth
let AccessPointOAuth = defaultClient.authentications['AccessPointOAuth'];
AccessPointOAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ZapierNaturalLanguageActionsNlaApiBeta.DefaultApi();
apiInstance.listExposedActions((error, data, response) => {
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

[**ExposedActionResponseSchema**](ExposedActionResponseSchema.md)

### Authorization

[AccessPointApiKeyQuery](../README.md#AccessPointApiKeyQuery), [SessionAuth](../README.md#SessionAuth), [AccessPointApiKeyHeader](../README.md#AccessPointApiKeyHeader), [AccessPointOAuth](../README.md#AccessPointOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


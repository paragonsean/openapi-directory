# AmazonPrometheusService.DefaultApi

All URIs are relative to *http://aps.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAlertManagerDefinition**](DefaultApi.md#createAlertManagerDefinition) | **POST** /workspaces/{workspaceId}/alertmanager/definition | 
[**createLoggingConfiguration**](DefaultApi.md#createLoggingConfiguration) | **POST** /workspaces/{workspaceId}/logging | 
[**createRuleGroupsNamespace**](DefaultApi.md#createRuleGroupsNamespace) | **POST** /workspaces/{workspaceId}/rulegroupsnamespaces | 
[**createWorkspace**](DefaultApi.md#createWorkspace) | **POST** /workspaces | 
[**deleteAlertManagerDefinition**](DefaultApi.md#deleteAlertManagerDefinition) | **DELETE** /workspaces/{workspaceId}/alertmanager/definition | 
[**deleteLoggingConfiguration**](DefaultApi.md#deleteLoggingConfiguration) | **DELETE** /workspaces/{workspaceId}/logging | 
[**deleteRuleGroupsNamespace**](DefaultApi.md#deleteRuleGroupsNamespace) | **DELETE** /workspaces/{workspaceId}/rulegroupsnamespaces/{name} | 
[**deleteWorkspace**](DefaultApi.md#deleteWorkspace) | **DELETE** /workspaces/{workspaceId} | 
[**describeAlertManagerDefinition**](DefaultApi.md#describeAlertManagerDefinition) | **GET** /workspaces/{workspaceId}/alertmanager/definition | 
[**describeLoggingConfiguration**](DefaultApi.md#describeLoggingConfiguration) | **GET** /workspaces/{workspaceId}/logging | 
[**describeRuleGroupsNamespace**](DefaultApi.md#describeRuleGroupsNamespace) | **GET** /workspaces/{workspaceId}/rulegroupsnamespaces/{name} | 
[**describeWorkspace**](DefaultApi.md#describeWorkspace) | **GET** /workspaces/{workspaceId} | 
[**listRuleGroupsNamespaces**](DefaultApi.md#listRuleGroupsNamespaces) | **GET** /workspaces/{workspaceId}/rulegroupsnamespaces | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**listWorkspaces**](DefaultApi.md#listWorkspaces) | **GET** /workspaces | 
[**putAlertManagerDefinition**](DefaultApi.md#putAlertManagerDefinition) | **PUT** /workspaces/{workspaceId}/alertmanager/definition | 
[**putRuleGroupsNamespace**](DefaultApi.md#putRuleGroupsNamespace) | **PUT** /workspaces/{workspaceId}/rulegroupsnamespaces/{name} | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateLoggingConfiguration**](DefaultApi.md#updateLoggingConfiguration) | **PUT** /workspaces/{workspaceId}/logging | 
[**updateWorkspaceAlias**](DefaultApi.md#updateWorkspaceAlias) | **POST** /workspaces/{workspaceId}/alias | 



## createAlertManagerDefinition

> CreateAlertManagerDefinitionResponse createAlertManagerDefinition(workspaceId, putAlertManagerDefinitionRequest, opts)



Create an alert manager definition.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace in which to create the alert manager definition.
let putAlertManagerDefinitionRequest = new AmazonPrometheusService.PutAlertManagerDefinitionRequest(); // PutAlertManagerDefinitionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAlertManagerDefinition(workspaceId, putAlertManagerDefinitionRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace in which to create the alert manager definition. | 
 **putAlertManagerDefinitionRequest** | [**PutAlertManagerDefinitionRequest**](PutAlertManagerDefinitionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAlertManagerDefinitionResponse**](CreateAlertManagerDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLoggingConfiguration

> CreateLoggingConfigurationResponse createLoggingConfiguration(workspaceId, updateLoggingConfigurationRequest, opts)



Create logging configuration.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to vend logs to.
let updateLoggingConfigurationRequest = new AmazonPrometheusService.UpdateLoggingConfigurationRequest(); // UpdateLoggingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createLoggingConfiguration(workspaceId, updateLoggingConfigurationRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to vend logs to. | 
 **updateLoggingConfigurationRequest** | [**UpdateLoggingConfigurationRequest**](UpdateLoggingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateLoggingConfigurationResponse**](CreateLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRuleGroupsNamespace

> CreateRuleGroupsNamespaceResponse createRuleGroupsNamespace(workspaceId, createRuleGroupsNamespaceRequest, opts)



Create a rule group namespace.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace in which to create the rule group namespace.
let createRuleGroupsNamespaceRequest = new AmazonPrometheusService.CreateRuleGroupsNamespaceRequest(); // CreateRuleGroupsNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRuleGroupsNamespace(workspaceId, createRuleGroupsNamespaceRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace in which to create the rule group namespace. | 
 **createRuleGroupsNamespaceRequest** | [**CreateRuleGroupsNamespaceRequest**](CreateRuleGroupsNamespaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRuleGroupsNamespaceResponse**](CreateRuleGroupsNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWorkspace

> CreateWorkspaceResponse createWorkspace(createWorkspaceRequest, opts)



Creates a new AMP workspace.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let createWorkspaceRequest = new AmazonPrometheusService.CreateWorkspaceRequest(); // CreateWorkspaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWorkspace(createWorkspaceRequest, opts, (error, data, response) => {
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
 **createWorkspaceRequest** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWorkspaceResponse**](CreateWorkspaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAlertManagerDefinition

> deleteAlertManagerDefinition(workspaceId, opts)



Deletes an alert manager definition.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace in which to delete the alert manager definition.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | Optional, unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
};
apiInstance.deleteAlertManagerDefinition(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace in which to delete the alert manager definition. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| Optional, unique, case-sensitive, user-provided identifier to ensure the idempotency of the request. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLoggingConfiguration

> deleteLoggingConfiguration(workspaceId, opts)



Delete logging configuration.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to vend logs to.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | Optional, unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
};
apiInstance.deleteLoggingConfiguration(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to vend logs to. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| Optional, unique, case-sensitive, user-provided identifier to ensure the idempotency of the request. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRuleGroupsNamespace

> deleteRuleGroupsNamespace(workspaceId, name, opts)



Delete a rule groups namespace.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to delete rule group definition.
let name = "name_example"; // String | The rule groups namespace name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | Optional, unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
};
apiInstance.deleteRuleGroupsNamespace(workspaceId, name, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to delete rule group definition. | 
 **name** | **String**| The rule groups namespace name. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| Optional, unique, case-sensitive, user-provided identifier to ensure the idempotency of the request. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWorkspace

> deleteWorkspace(workspaceId, opts)



Deletes an AMP workspace.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | Optional, unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
};
apiInstance.deleteWorkspace(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| Optional, unique, case-sensitive, user-provided identifier to ensure the idempotency of the request. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeAlertManagerDefinition

> DescribeAlertManagerDefinitionResponse describeAlertManagerDefinition(workspaceId, opts)



Describes an alert manager definition.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAlertManagerDefinition(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAlertManagerDefinitionResponse**](DescribeAlertManagerDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeLoggingConfiguration

> DescribeLoggingConfigurationResponse describeLoggingConfiguration(workspaceId, opts)



Describes logging configuration.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to vend logs to.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeLoggingConfiguration(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to vend logs to. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeLoggingConfigurationResponse**](DescribeLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeRuleGroupsNamespace

> DescribeRuleGroupsNamespaceResponse describeRuleGroupsNamespace(workspaceId, name, opts)



Describe a rule groups namespace.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to describe.
let name = "name_example"; // String | The rule groups namespace.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeRuleGroupsNamespace(workspaceId, name, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to describe. | 
 **name** | **String**| The rule groups namespace. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeRuleGroupsNamespaceResponse**](DescribeRuleGroupsNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeWorkspace

> DescribeWorkspaceResponse describeWorkspace(workspaceId, opts)



Describes an existing AMP workspace.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeWorkspace(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeWorkspaceResponse**](DescribeWorkspaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRuleGroupsNamespaces

> ListRuleGroupsNamespacesResponse listRuleGroupsNamespaces(workspaceId, opts)



Lists rule groups namespaces.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'name': "name_example", // String | Optional filter for rule groups namespace name. Only the rule groups namespace that begin with this value will be returned.
  'nextToken': "nextToken_example", // String | Pagination token to request the next page in a paginated list. This token is obtained from the output of the previous ListRuleGroupsNamespaces request.
  'maxResults': 56 // Number | Maximum results to return in response (default=100, maximum=1000).
};
apiInstance.listRuleGroupsNamespaces(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **name** | **String**| Optional filter for rule groups namespace name. Only the rule groups namespace that begin with this value will be returned. | [optional] 
 **nextToken** | **String**| Pagination token to request the next page in a paginated list. This token is obtained from the output of the previous ListRuleGroupsNamespaces request. | [optional] 
 **maxResults** | **Number**| Maximum results to return in response (default&#x3D;100, maximum&#x3D;1000). | [optional] 

### Return type

[**ListRuleGroupsNamespacesResponse**](ListRuleGroupsNamespacesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists the tags you have assigned to the resource.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The ARN of the resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWorkspaces

> ListWorkspacesResponse listWorkspaces(opts)



Lists all AMP workspaces, including workspaces being created or deleted.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | Pagination token to request the next page in a paginated list. This token is obtained from the output of the previous ListWorkspaces request.
  'alias': "alias_example", // String | Optional filter for workspace alias. Only the workspaces with aliases that begin with this value will be returned.
  'maxResults': 56 // Number | Maximum results to return in response (default=100, maximum=1000).
};
apiInstance.listWorkspaces(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Pagination token to request the next page in a paginated list. This token is obtained from the output of the previous ListWorkspaces request. | [optional] 
 **alias** | **String**| Optional filter for workspace alias. Only the workspaces with aliases that begin with this value will be returned. | [optional] 
 **maxResults** | **Number**| Maximum results to return in response (default&#x3D;100, maximum&#x3D;1000). | [optional] 

### Return type

[**ListWorkspacesResponse**](ListWorkspacesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putAlertManagerDefinition

> PutAlertManagerDefinitionResponse putAlertManagerDefinition(workspaceId, putAlertManagerDefinitionRequest, opts)



Update an alert manager definition.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace in which to update the alert manager definition.
let putAlertManagerDefinitionRequest = new AmazonPrometheusService.PutAlertManagerDefinitionRequest(); // PutAlertManagerDefinitionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAlertManagerDefinition(workspaceId, putAlertManagerDefinitionRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace in which to update the alert manager definition. | 
 **putAlertManagerDefinitionRequest** | [**PutAlertManagerDefinitionRequest**](PutAlertManagerDefinitionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutAlertManagerDefinitionResponse**](PutAlertManagerDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putRuleGroupsNamespace

> PutRuleGroupsNamespaceResponse putRuleGroupsNamespace(workspaceId, name, putRuleGroupsNamespaceRequest, opts)



Update a rule groups namespace.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace in which to update the rule group namespace.
let name = "name_example"; // String | The rule groups namespace name.
let putRuleGroupsNamespaceRequest = new AmazonPrometheusService.PutRuleGroupsNamespaceRequest(); // PutRuleGroupsNamespaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putRuleGroupsNamespace(workspaceId, name, putRuleGroupsNamespaceRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace in which to update the rule group namespace. | 
 **name** | **String**| The rule groups namespace name. | 
 **putRuleGroupsNamespaceRequest** | [**PutRuleGroupsNamespaceRequest**](PutRuleGroupsNamespaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutRuleGroupsNamespaceResponse**](PutRuleGroupsNamespaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



Creates tags for the specified resource.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource.
let tagResourceRequest = new AmazonPrometheusService.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The ARN of the resource. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(resourceArn, tagKeys, opts)



Deletes tags from the specified resource.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource.
let tagKeys = ["null"]; // [String] | One or more tag keys
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The ARN of the resource. | 
 **tagKeys** | [**[String]**](String.md)| One or more tag keys | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateLoggingConfiguration

> UpdateLoggingConfigurationResponse updateLoggingConfiguration(workspaceId, updateLoggingConfigurationRequest, opts)



Update logging configuration.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to vend logs to.
let updateLoggingConfigurationRequest = new AmazonPrometheusService.UpdateLoggingConfigurationRequest(); // UpdateLoggingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateLoggingConfiguration(workspaceId, updateLoggingConfigurationRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to vend logs to. | 
 **updateLoggingConfigurationRequest** | [**UpdateLoggingConfigurationRequest**](UpdateLoggingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateLoggingConfigurationResponse**](UpdateLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkspaceAlias

> updateWorkspaceAlias(workspaceId, updateWorkspaceAliasRequest, opts)



Updates an AMP workspace alias.

### Example

```javascript
import AmazonPrometheusService from 'amazon_prometheus_service';
let defaultClient = AmazonPrometheusService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPrometheusService.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace being updated.
let updateWorkspaceAliasRequest = new AmazonPrometheusService.UpdateWorkspaceAliasRequest(); // UpdateWorkspaceAliasRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateWorkspaceAlias(workspaceId, updateWorkspaceAliasRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace being updated. | 
 **updateWorkspaceAliasRequest** | [**UpdateWorkspaceAliasRequest**](UpdateWorkspaceAliasRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


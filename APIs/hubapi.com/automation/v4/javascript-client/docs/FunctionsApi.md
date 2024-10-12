# AutomationActionsV4.FunctionsApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType**](FunctionsApi.md#deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType) | **DELETE** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType} | Delete a function for a definition
[**deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive**](FunctionsApi.md#deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive) | **DELETE** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId} | Archive a function for a definition
[**getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById**](FunctionsApi.md#getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById) | **GET** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId} | Get a function for a given definition
[**getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType**](FunctionsApi.md#getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType) | **GET** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType} | Get all functions by a type for a given definition
[**getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage**](FunctionsApi.md#getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage) | **GET** /automation/v4/actions/{appId}/{definitionId}/functions | Get all functions for a given definition
[**putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType**](FunctionsApi.md#putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType) | **PUT** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType} | Insert a function for a definition
[**putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace**](FunctionsApi.md#putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace) | **PUT** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId} | Insert a function for a definition



## deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType

> deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType(definitionId, functionType, appId)

Delete a function for a definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.FunctionsApi();
let definitionId = "definitionId_example"; // String | 
let functionType = "functionType_example"; // String | 
let appId = 56; // Number | 
apiInstance.deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType(definitionId, functionType, appId, (error, data, response) => {
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
 **definitionId** | **String**|  | 
 **functionType** | **String**|  | 
 **appId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive

> deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive(definitionId, functionType, functionId, appId)

Archive a function for a definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.FunctionsApi();
let definitionId = "definitionId_example"; // String | 
let functionType = "functionType_example"; // String | 
let functionId = "functionId_example"; // String | 
let appId = 56; // Number | 
apiInstance.deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive(definitionId, functionType, functionId, appId, (error, data, response) => {
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
 **definitionId** | **String**|  | 
 **functionType** | **String**|  | 
 **functionId** | **String**|  | 
 **appId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById

> PublicActionFunction getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById(definitionId, functionType, functionId, appId)

Get a function for a given definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.FunctionsApi();
let definitionId = "definitionId_example"; // String | 
let functionType = "functionType_example"; // String | 
let functionId = "functionId_example"; // String | 
let appId = 56; // Number | 
apiInstance.getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById(definitionId, functionType, functionId, appId, (error, data, response) => {
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
 **definitionId** | **String**|  | 
 **functionType** | **String**|  | 
 **functionId** | **String**|  | 
 **appId** | **Number**|  | 

### Return type

[**PublicActionFunction**](PublicActionFunction.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType

> PublicActionFunction getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType(definitionId, functionType, appId)

Get all functions by a type for a given definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.FunctionsApi();
let definitionId = "definitionId_example"; // String | 
let functionType = "functionType_example"; // String | 
let appId = 56; // Number | 
apiInstance.getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType(definitionId, functionType, appId, (error, data, response) => {
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
 **definitionId** | **String**|  | 
 **functionType** | **String**|  | 
 **appId** | **Number**|  | 

### Return type

[**PublicActionFunction**](PublicActionFunction.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage

> CollectionResponsePublicActionFunctionIdentifierNoPaging getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage(definitionId, appId)

Get all functions for a given definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.FunctionsApi();
let definitionId = "definitionId_example"; // String | 
let appId = 56; // Number | 
apiInstance.getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage(definitionId, appId, (error, data, response) => {
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
 **definitionId** | **String**|  | 
 **appId** | **Number**|  | 

### Return type

[**CollectionResponsePublicActionFunctionIdentifierNoPaging**](CollectionResponsePublicActionFunctionIdentifierNoPaging.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType

> PublicActionFunctionIdentifier putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType(definitionId, functionType, appId, body)

Insert a function for a definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.FunctionsApi();
let definitionId = "definitionId_example"; // String | 
let functionType = "functionType_example"; // String | 
let appId = 56; // Number | 
let body = "body_example"; // String | 
apiInstance.putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType(definitionId, functionType, appId, body, (error, data, response) => {
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
 **definitionId** | **String**|  | 
 **functionType** | **String**|  | 
 **appId** | **Number**|  | 
 **body** | **String**|  | 

### Return type

[**PublicActionFunctionIdentifier**](PublicActionFunctionIdentifier.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json, */*


## putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace

> PublicActionFunctionIdentifier putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace(definitionId, functionType, functionId, appId, body)

Insert a function for a definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.FunctionsApi();
let definitionId = "definitionId_example"; // String | 
let functionType = "functionType_example"; // String | 
let functionId = "functionId_example"; // String | 
let appId = 56; // Number | 
let body = "body_example"; // String | 
apiInstance.putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace(definitionId, functionType, functionId, appId, body, (error, data, response) => {
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
 **definitionId** | **String**|  | 
 **functionType** | **String**|  | 
 **functionId** | **String**|  | 
 **appId** | **Number**|  | 
 **body** | **String**|  | 

### Return type

[**PublicActionFunctionIdentifier**](PublicActionFunctionIdentifier.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json, */*


# AutomationActionsV4.DefinitionsApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAutomationV4ActionsAppIdDefinitionIdArchive**](DefinitionsApi.md#deleteAutomationV4ActionsAppIdDefinitionIdArchive) | **DELETE** /automation/v4/actions/{appId}/{definitionId} | Archive an extension definition
[**getAutomationV4ActionsAppIdDefinitionIdGetById**](DefinitionsApi.md#getAutomationV4ActionsAppIdDefinitionIdGetById) | **GET** /automation/v4/actions/{appId}/{definitionId} | Get extension definition by Id
[**getAutomationV4ActionsAppIdGetPage**](DefinitionsApi.md#getAutomationV4ActionsAppIdGetPage) | **GET** /automation/v4/actions/{appId} | Get paged extension definitions
[**patchAutomationV4ActionsAppIdDefinitionIdUpdate**](DefinitionsApi.md#patchAutomationV4ActionsAppIdDefinitionIdUpdate) | **PATCH** /automation/v4/actions/{appId}/{definitionId} | Patch an existing extension definition
[**postAutomationV4ActionsAppIdCreate**](DefinitionsApi.md#postAutomationV4ActionsAppIdCreate) | **POST** /automation/v4/actions/{appId} | Create a new extension definition



## deleteAutomationV4ActionsAppIdDefinitionIdArchive

> deleteAutomationV4ActionsAppIdDefinitionIdArchive(definitionId, appId)

Archive an extension definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.DefinitionsApi();
let definitionId = "definitionId_example"; // String | 
let appId = 56; // Number | 
apiInstance.deleteAutomationV4ActionsAppIdDefinitionIdArchive(definitionId, appId, (error, data, response) => {
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
 **appId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAutomationV4ActionsAppIdDefinitionIdGetById

> PublicActionDefinition getAutomationV4ActionsAppIdDefinitionIdGetById(definitionId, appId, opts)

Get extension definition by Id

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.DefinitionsApi();
let definitionId = "definitionId_example"; // String | 
let appId = 56; // Number | 
let opts = {
  'archived': false // Boolean | Whether to return only results that have been archived.
};
apiInstance.getAutomationV4ActionsAppIdDefinitionIdGetById(definitionId, appId, opts, (error, data, response) => {
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
 **archived** | **Boolean**| Whether to return only results that have been archived. | [optional] [default to false]

### Return type

[**PublicActionDefinition**](PublicActionDefinition.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getAutomationV4ActionsAppIdGetPage

> CollectionResponsePublicActionDefinitionForwardPaging getAutomationV4ActionsAppIdGetPage(appId, opts)

Get paged extension definitions

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.DefinitionsApi();
let appId = 56; // Number | 
let opts = {
  'limit': 56, // Number | The maximum number of results to display per page.
  'after': "after_example", // String | The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
  'archived': false // Boolean | Whether to return only results that have been archived.
};
apiInstance.getAutomationV4ActionsAppIdGetPage(appId, opts, (error, data, response) => {
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
 **appId** | **Number**|  | 
 **limit** | **Number**| The maximum number of results to display per page. | [optional] 
 **after** | **String**| The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results. | [optional] 
 **archived** | **Boolean**| Whether to return only results that have been archived. | [optional] [default to false]

### Return type

[**CollectionResponsePublicActionDefinitionForwardPaging**](CollectionResponsePublicActionDefinitionForwardPaging.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## patchAutomationV4ActionsAppIdDefinitionIdUpdate

> PublicActionDefinition patchAutomationV4ActionsAppIdDefinitionIdUpdate(definitionId, appId, publicActionDefinitionPatch)

Patch an existing extension definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.DefinitionsApi();
let definitionId = "definitionId_example"; // String | 
let appId = 56; // Number | 
let publicActionDefinitionPatch = new AutomationActionsV4.PublicActionDefinitionPatch(); // PublicActionDefinitionPatch | 
apiInstance.patchAutomationV4ActionsAppIdDefinitionIdUpdate(definitionId, appId, publicActionDefinitionPatch, (error, data, response) => {
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
 **publicActionDefinitionPatch** | [**PublicActionDefinitionPatch**](PublicActionDefinitionPatch.md)|  | 

### Return type

[**PublicActionDefinition**](PublicActionDefinition.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## postAutomationV4ActionsAppIdCreate

> PublicActionDefinition postAutomationV4ActionsAppIdCreate(appId, publicActionDefinitionEgg)

Create a new extension definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.DefinitionsApi();
let appId = 56; // Number | 
let publicActionDefinitionEgg = new AutomationActionsV4.PublicActionDefinitionEgg(); // PublicActionDefinitionEgg | 
apiInstance.postAutomationV4ActionsAppIdCreate(appId, publicActionDefinitionEgg, (error, data, response) => {
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
 **appId** | **Number**|  | 
 **publicActionDefinitionEgg** | [**PublicActionDefinitionEgg**](PublicActionDefinitionEgg.md)|  | 

### Return type

[**PublicActionDefinition**](PublicActionDefinition.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


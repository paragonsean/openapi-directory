# AutomationActionsV4.RevisionsApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage**](RevisionsApi.md#getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage) | **GET** /automation/v4/actions/{appId}/{definitionId}/revisions | Get all revisions for a given definition
[**getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById**](RevisionsApi.md#getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById) | **GET** /automation/v4/actions/{appId}/{definitionId}/revisions/{revisionId} | Gets a revision for a given definition by revision id



## getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage

> CollectionResponsePublicActionRevisionForwardPaging getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage(definitionId, appId, opts)

Get all revisions for a given definition

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.RevisionsApi();
let definitionId = "definitionId_example"; // String | 
let appId = 56; // Number | 
let opts = {
  'limit': 56, // Number | The maximum number of results to display per page.
  'after': "after_example" // String | The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
};
apiInstance.getAutomationV4ActionsAppIdDefinitionIdRevisionsGetPage(definitionId, appId, opts, (error, data, response) => {
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
 **limit** | **Number**| The maximum number of results to display per page. | [optional] 
 **after** | **String**| The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results. | [optional] 

### Return type

[**CollectionResponsePublicActionRevisionForwardPaging**](CollectionResponsePublicActionRevisionForwardPaging.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById

> PublicActionRevision getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById(definitionId, revisionId, appId)

Gets a revision for a given definition by revision id

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.RevisionsApi();
let definitionId = "definitionId_example"; // String | 
let revisionId = "revisionId_example"; // String | 
let appId = 56; // Number | 
apiInstance.getAutomationV4ActionsAppIdDefinitionIdRevisionsRevisionIdGetById(definitionId, revisionId, appId, (error, data, response) => {
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
 **revisionId** | **String**|  | 
 **appId** | **Number**|  | 

### Return type

[**PublicActionRevision**](PublicActionRevision.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


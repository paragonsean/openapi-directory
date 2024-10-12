# TheJiraCloudPlatformRestApi.ScreenTabFieldsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addScreenTabField**](ScreenTabFieldsApi.md#addScreenTabField) | **POST** /rest/api/3/screens/{screenId}/tabs/{tabId}/fields | Add screen tab field
[**getAllScreenTabFields**](ScreenTabFieldsApi.md#getAllScreenTabFields) | **GET** /rest/api/3/screens/{screenId}/tabs/{tabId}/fields | Get all screen tab fields
[**moveScreenTabField**](ScreenTabFieldsApi.md#moveScreenTabField) | **POST** /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move | Move screen tab field
[**removeScreenTabField**](ScreenTabFieldsApi.md#removeScreenTabField) | **DELETE** /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id} | Remove screen tab field



## addScreenTabField

> ScreenableField addScreenTabField(screenId, tabId, addFieldBean)

Add screen tab field

Adds a field to a screen tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.ScreenTabFieldsApi();
let screenId = 789; // Number | The ID of the screen.
let tabId = 789; // Number | The ID of the screen tab.
let addFieldBean = {"fieldId":"summary"}; // AddFieldBean | 
apiInstance.addScreenTabField(screenId, tabId, addFieldBean, (error, data, response) => {
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
 **screenId** | **Number**| The ID of the screen. | 
 **tabId** | **Number**| The ID of the screen tab. | 
 **addFieldBean** | [**AddFieldBean**](AddFieldBean.md)|  | 

### Return type

[**ScreenableField**](ScreenableField.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAllScreenTabFields

> [ScreenableField] getAllScreenTabFields(screenId, tabId, opts)

Get all screen tab fields

Returns all fields for a screen tab.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.ScreenTabFieldsApi();
let screenId = 789; // Number | The ID of the screen.
let tabId = 789; // Number | The ID of the screen tab.
let opts = {
  'projectKey': "projectKey_example" // String | The key of the project.
};
apiInstance.getAllScreenTabFields(screenId, tabId, opts, (error, data, response) => {
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
 **screenId** | **Number**| The ID of the screen. | 
 **tabId** | **Number**| The ID of the screen tab. | 
 **projectKey** | **String**| The key of the project. | [optional] 

### Return type

[**[ScreenableField]**](ScreenableField.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## moveScreenTabField

> Object moveScreenTabField(screenId, tabId, id, moveFieldBean)

Move screen tab field

Moves a screen tab field.  If &#x60;after&#x60; and &#x60;position&#x60; are provided in the request, &#x60;position&#x60; is ignored.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.ScreenTabFieldsApi();
let screenId = 789; // Number | The ID of the screen.
let tabId = 789; // Number | The ID of the screen tab.
let id = "id_example"; // String | The ID of the field.
let moveFieldBean = new TheJiraCloudPlatformRestApi.MoveFieldBean(); // MoveFieldBean | 
apiInstance.moveScreenTabField(screenId, tabId, id, moveFieldBean, (error, data, response) => {
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
 **screenId** | **Number**| The ID of the screen. | 
 **tabId** | **Number**| The ID of the screen tab. | 
 **id** | **String**| The ID of the field. | 
 **moveFieldBean** | [**MoveFieldBean**](MoveFieldBean.md)|  | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeScreenTabField

> removeScreenTabField(screenId, tabId, id)

Remove screen tab field

Removes a field from a screen tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.ScreenTabFieldsApi();
let screenId = 789; // Number | The ID of the screen.
let tabId = 789; // Number | The ID of the screen tab.
let id = "id_example"; // String | The ID of the field.
apiInstance.removeScreenTabField(screenId, tabId, id, (error, data, response) => {
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
 **screenId** | **Number**| The ID of the screen. | 
 **tabId** | **Number**| The ID of the screen tab. | 
 **id** | **String**| The ID of the field. | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


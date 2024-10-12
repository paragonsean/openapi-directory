# TheJiraCloudPlatformRestApi.ScreenTabsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addScreenTab**](ScreenTabsApi.md#addScreenTab) | **POST** /rest/api/3/screens/{screenId}/tabs | Create screen tab
[**deleteScreenTab**](ScreenTabsApi.md#deleteScreenTab) | **DELETE** /rest/api/3/screens/{screenId}/tabs/{tabId} | Delete screen tab
[**getAllScreenTabs**](ScreenTabsApi.md#getAllScreenTabs) | **GET** /rest/api/3/screens/{screenId}/tabs | Get all screen tabs
[**moveScreenTab**](ScreenTabsApi.md#moveScreenTab) | **POST** /rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos} | Move screen tab
[**renameScreenTab**](ScreenTabsApi.md#renameScreenTab) | **PUT** /rest/api/3/screens/{screenId}/tabs/{tabId} | Update screen tab



## addScreenTab

> ScreenableTab addScreenTab(screenId, screenableTab)

Create screen tab

Creates a tab for a screen.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

let apiInstance = new TheJiraCloudPlatformRestApi.ScreenTabsApi();
let screenId = 789; // Number | The ID of the screen.
let screenableTab = {"name":"Fields Tab"}; // ScreenableTab | 
apiInstance.addScreenTab(screenId, screenableTab, (error, data, response) => {
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
 **screenableTab** | [**ScreenableTab**](ScreenableTab.md)|  | 

### Return type

[**ScreenableTab**](ScreenableTab.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteScreenTab

> deleteScreenTab(screenId, tabId)

Delete screen tab

Deletes a screen tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

let apiInstance = new TheJiraCloudPlatformRestApi.ScreenTabsApi();
let screenId = 789; // Number | The ID of the screen.
let tabId = 789; // Number | The ID of the screen tab.
apiInstance.deleteScreenTab(screenId, tabId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllScreenTabs

> [ScreenableTab] getAllScreenTabs(screenId, opts)

Get all screen tabs

Returns the list of tabs for a screen.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.

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

let apiInstance = new TheJiraCloudPlatformRestApi.ScreenTabsApi();
let screenId = 789; // Number | The ID of the screen.
let opts = {
  'projectKey': "projectKey_example" // String | The key of the project.
};
apiInstance.getAllScreenTabs(screenId, opts, (error, data, response) => {
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
 **projectKey** | **String**| The key of the project. | [optional] 

### Return type

[**[ScreenableTab]**](ScreenableTab.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## moveScreenTab

> Object moveScreenTab(screenId, tabId, pos)

Move screen tab

Moves a screen tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

let apiInstance = new TheJiraCloudPlatformRestApi.ScreenTabsApi();
let screenId = 789; // Number | The ID of the screen.
let tabId = 789; // Number | The ID of the screen tab.
let pos = 56; // Number | The position of tab. The base index is 0.
apiInstance.moveScreenTab(screenId, tabId, pos, (error, data, response) => {
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
 **pos** | **Number**| The position of tab. The base index is 0. | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## renameScreenTab

> ScreenableTab renameScreenTab(screenId, tabId, screenableTab)

Update screen tab

Updates the name of a screen tab.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

let apiInstance = new TheJiraCloudPlatformRestApi.ScreenTabsApi();
let screenId = 789; // Number | The ID of the screen.
let tabId = 789; // Number | The ID of the screen tab.
let screenableTab = new TheJiraCloudPlatformRestApi.ScreenableTab(); // ScreenableTab | 
apiInstance.renameScreenTab(screenId, tabId, screenableTab, (error, data, response) => {
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
 **screenableTab** | [**ScreenableTab**](ScreenableTab.md)|  | 

### Return type

[**ScreenableTab**](ScreenableTab.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


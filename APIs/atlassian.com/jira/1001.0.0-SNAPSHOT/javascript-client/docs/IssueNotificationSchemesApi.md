# TheJiraCloudPlatformRestApi.IssueNotificationSchemesApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addNotifications**](IssueNotificationSchemesApi.md#addNotifications) | **PUT** /rest/api/3/notificationscheme/{id}/notification | Add notifications to notification scheme
[**createNotificationScheme**](IssueNotificationSchemesApi.md#createNotificationScheme) | **POST** /rest/api/3/notificationscheme | Create notification scheme
[**deleteNotificationScheme**](IssueNotificationSchemesApi.md#deleteNotificationScheme) | **DELETE** /rest/api/3/notificationscheme/{notificationSchemeId} | Delete notification scheme
[**getNotificationScheme**](IssueNotificationSchemesApi.md#getNotificationScheme) | **GET** /rest/api/3/notificationscheme/{id} | Get notification scheme
[**getNotificationSchemeToProjectMappings**](IssueNotificationSchemesApi.md#getNotificationSchemeToProjectMappings) | **GET** /rest/api/3/notificationscheme/project | Get projects using notification schemes paginated
[**getNotificationSchemes**](IssueNotificationSchemesApi.md#getNotificationSchemes) | **GET** /rest/api/3/notificationscheme | Get notification schemes paginated
[**removeNotificationFromNotificationScheme**](IssueNotificationSchemesApi.md#removeNotificationFromNotificationScheme) | **DELETE** /rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId} | Remove notification from notification scheme
[**updateNotificationScheme**](IssueNotificationSchemesApi.md#updateNotificationScheme) | **PUT** /rest/api/3/notificationscheme/{id} | Update notification scheme



## addNotifications

> Object addNotifications(id, addNotificationsDetails)

Add notifications to notification scheme

Adds notifications to a notification scheme. You can add up to 1000 notifications per request.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueNotificationSchemesApi();
let id = "id_example"; // String | The ID of the notification scheme.
let addNotificationsDetails = {"notificationSchemeEvents":[{"event":{"id":"1"},"notifications":[{"notificationType":"Group","parameter":"jira-administrators"}]}]}; // AddNotificationsDetails | 
apiInstance.addNotifications(id, addNotificationsDetails, (error, data, response) => {
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
 **id** | **String**| The ID of the notification scheme. | 
 **addNotificationsDetails** | [**AddNotificationsDetails**](AddNotificationsDetails.md)|  | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNotificationScheme

> NotificationSchemeId createNotificationScheme(createNotificationSchemeDetails)

Create notification scheme

Creates a notification scheme with notifications. You can create up to 1000 notifications per request.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueNotificationSchemesApi();
let createNotificationSchemeDetails = {"description":"My new scheme description","name":"My new notification scheme","notificationSchemeEvents":[{"event":{"id":"1"},"notifications":[{"notificationType":"Group","parameter":"jira-administrators"}]}]}; // CreateNotificationSchemeDetails | 
apiInstance.createNotificationScheme(createNotificationSchemeDetails, (error, data, response) => {
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
 **createNotificationSchemeDetails** | [**CreateNotificationSchemeDetails**](CreateNotificationSchemeDetails.md)|  | 

### Return type

[**NotificationSchemeId**](NotificationSchemeId.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNotificationScheme

> Object deleteNotificationScheme(notificationSchemeId)

Delete notification scheme

Deletes a notification scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueNotificationSchemesApi();
let notificationSchemeId = "notificationSchemeId_example"; // String | The ID of the notification scheme.
apiInstance.deleteNotificationScheme(notificationSchemeId, (error, data, response) => {
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
 **notificationSchemeId** | **String**| The ID of the notification scheme. | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotificationScheme

> NotificationScheme getNotificationScheme(id, opts)

Get notification scheme

Returns a [notification scheme](https://confluence.atlassian.com/x/8YdKLg), including the list of events and the recipients who will receive notifications for those events.  **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with the notification scheme.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueNotificationSchemesApi();
let id = 789; // Number | The ID of the notification scheme. Use [Get notification schemes paginated](#api-rest-api-3-notificationscheme-get) to get a list of notification scheme IDs.
let opts = {
  'expand': "expand_example" // String | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `all` Returns all expandable information  *  `field` Returns information about any custom fields assigned to receive an event  *  `group` Returns information about any groups assigned to receive an event  *  `notificationSchemeEvents` Returns a list of event associations. This list is returned for all expandable information  *  `projectRole` Returns information about any project roles assigned to receive an event  *  `user` Returns information about any users assigned to receive an event
};
apiInstance.getNotificationScheme(id, opts, (error, data, response) => {
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
 **id** | **Number**| The ID of the notification scheme. Use [Get notification schemes paginated](#api-rest-api-3-notificationscheme-get) to get a list of notification scheme IDs. | 
 **expand** | **String**| Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;all&#x60; Returns all expandable information  *  &#x60;field&#x60; Returns information about any custom fields assigned to receive an event  *  &#x60;group&#x60; Returns information about any groups assigned to receive an event  *  &#x60;notificationSchemeEvents&#x60; Returns a list of event associations. This list is returned for all expandable information  *  &#x60;projectRole&#x60; Returns information about any project roles assigned to receive an event  *  &#x60;user&#x60; Returns information about any users assigned to receive an event | [optional] 

### Return type

[**NotificationScheme**](NotificationScheme.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotificationSchemeToProjectMappings

> PageBeanNotificationSchemeAndProjectMappingJsonBean getNotificationSchemeToProjectMappings(opts)

Get projects using notification schemes paginated

Returns a [paginated](#pagination) mapping of project that have notification scheme assigned. You can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don&#39;t provide any, this will return a list of all mappings. Note that only company-managed (classic) projects are supported. This is because team-managed projects don&#39;t have a concept of a default notification scheme. The mappings are ordered by projectId.  **[Permissions](#permissions) required:** Permission to access Jira.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueNotificationSchemesApi();
let opts = {
  'startAt': "'0'", // String | The index of the first item to return in a page of results (page offset).
  'maxResults': "'50'", // String | The maximum number of items to return per page.
  'notificationSchemeId': ["null"], // [String] | The list of notifications scheme IDs to be filtered out
  'projectId': ["null"] // [String] | The list of project IDs to be filtered out
};
apiInstance.getNotificationSchemeToProjectMappings(opts, (error, data, response) => {
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
 **startAt** | **String**| The index of the first item to return in a page of results (page offset). | [optional] [default to &#39;0&#39;]
 **maxResults** | **String**| The maximum number of items to return per page. | [optional] [default to &#39;50&#39;]
 **notificationSchemeId** | [**[String]**](String.md)| The list of notifications scheme IDs to be filtered out | [optional] 
 **projectId** | [**[String]**](String.md)| The list of project IDs to be filtered out | [optional] 

### Return type

[**PageBeanNotificationSchemeAndProjectMappingJsonBean**](PageBeanNotificationSchemeAndProjectMappingJsonBean.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotificationSchemes

> PageBeanNotificationScheme getNotificationSchemes(opts)

Get notification schemes paginated

Returns a [paginated](#pagination) list of [notification schemes](https://confluence.atlassian.com/x/8YdKLg) ordered by the display name.  *Note that you should allow for events without recipients to appear in responses.*  **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with a notification scheme for it to be returned.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueNotificationSchemesApi();
let opts = {
  'startAt': "'0'", // String | The index of the first item to return in a page of results (page offset).
  'maxResults': "'50'", // String | The maximum number of items to return per page.
  'id': ["null"], // [String] | The list of notification schemes IDs to be filtered by
  'projectId': ["null"], // [String] | The list of projects IDs to be filtered by
  'onlyDefault': false, // Boolean | When set to true, returns only the default notification scheme. If you provide project IDs not associated with the default, returns an empty page. The default value is false.
  'expand': "expand_example" // String | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  `all` Returns all expandable information  *  `field` Returns information about any custom fields assigned to receive an event  *  `group` Returns information about any groups assigned to receive an event  *  `notificationSchemeEvents` Returns a list of event associations. This list is returned for all expandable information  *  `projectRole` Returns information about any project roles assigned to receive an event  *  `user` Returns information about any users assigned to receive an event
};
apiInstance.getNotificationSchemes(opts, (error, data, response) => {
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
 **startAt** | **String**| The index of the first item to return in a page of results (page offset). | [optional] [default to &#39;0&#39;]
 **maxResults** | **String**| The maximum number of items to return per page. | [optional] [default to &#39;50&#39;]
 **id** | [**[String]**](String.md)| The list of notification schemes IDs to be filtered by | [optional] 
 **projectId** | [**[String]**](String.md)| The list of projects IDs to be filtered by | [optional] 
 **onlyDefault** | **Boolean**| When set to true, returns only the default notification scheme. If you provide project IDs not associated with the default, returns an empty page. The default value is false. | [optional] [default to false]
 **expand** | **String**| Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;all&#x60; Returns all expandable information  *  &#x60;field&#x60; Returns information about any custom fields assigned to receive an event  *  &#x60;group&#x60; Returns information about any groups assigned to receive an event  *  &#x60;notificationSchemeEvents&#x60; Returns a list of event associations. This list is returned for all expandable information  *  &#x60;projectRole&#x60; Returns information about any project roles assigned to receive an event  *  &#x60;user&#x60; Returns information about any users assigned to receive an event | [optional] 

### Return type

[**PageBeanNotificationScheme**](PageBeanNotificationScheme.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeNotificationFromNotificationScheme

> Object removeNotificationFromNotificationScheme(notificationSchemeId, notificationId)

Remove notification from notification scheme

Removes a notification from a notification scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueNotificationSchemesApi();
let notificationSchemeId = "notificationSchemeId_example"; // String | The ID of the notification scheme.
let notificationId = "notificationId_example"; // String | The ID of the notification.
apiInstance.removeNotificationFromNotificationScheme(notificationSchemeId, notificationId, (error, data, response) => {
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
 **notificationSchemeId** | **String**| The ID of the notification scheme. | 
 **notificationId** | **String**| The ID of the notification. | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNotificationScheme

> Object updateNotificationScheme(id, updateNotificationSchemeDetails)

Update notification scheme

Updates a notification scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueNotificationSchemesApi();
let id = "id_example"; // String | The ID of the notification scheme.
let updateNotificationSchemeDetails = {"description":"My updated notification scheme description","name":"My updated notification scheme"}; // UpdateNotificationSchemeDetails | 
apiInstance.updateNotificationScheme(id, updateNotificationSchemeDetails, (error, data, response) => {
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
 **id** | **String**| The ID of the notification scheme. | 
 **updateNotificationSchemeDetails** | [**UpdateNotificationSchemeDetails**](UpdateNotificationSchemeDetails.md)|  | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


# TheJiraCloudPlatformRestApi.DashboardsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addGadget**](DashboardsApi.md#addGadget) | **POST** /rest/api/3/dashboard/{dashboardId}/gadget | Add gadget to dashboard
[**copyDashboard**](DashboardsApi.md#copyDashboard) | **POST** /rest/api/3/dashboard/{id}/copy | Copy dashboard
[**createDashboard**](DashboardsApi.md#createDashboard) | **POST** /rest/api/3/dashboard | Create dashboard
[**deleteDashboard**](DashboardsApi.md#deleteDashboard) | **DELETE** /rest/api/3/dashboard/{id} | Delete dashboard
[**deleteDashboardItemProperty**](DashboardsApi.md#deleteDashboardItemProperty) | **DELETE** /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} | Delete dashboard item property
[**getAllAvailableDashboardGadgets**](DashboardsApi.md#getAllAvailableDashboardGadgets) | **GET** /rest/api/3/dashboard/gadgets | Get available gadgets
[**getAllDashboards**](DashboardsApi.md#getAllDashboards) | **GET** /rest/api/3/dashboard | Get all dashboards
[**getAllGadgets**](DashboardsApi.md#getAllGadgets) | **GET** /rest/api/3/dashboard/{dashboardId}/gadget | Get gadgets
[**getDashboard**](DashboardsApi.md#getDashboard) | **GET** /rest/api/3/dashboard/{id} | Get dashboard
[**getDashboardItemProperty**](DashboardsApi.md#getDashboardItemProperty) | **GET** /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} | Get dashboard item property
[**getDashboardItemPropertyKeys**](DashboardsApi.md#getDashboardItemPropertyKeys) | **GET** /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties | Get dashboard item property keys
[**getDashboardsPaginated**](DashboardsApi.md#getDashboardsPaginated) | **GET** /rest/api/3/dashboard/search | Search for dashboards
[**removeGadget**](DashboardsApi.md#removeGadget) | **DELETE** /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId} | Remove gadget from dashboard
[**setDashboardItemProperty**](DashboardsApi.md#setDashboardItemProperty) | **PUT** /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} | Set dashboard item property
[**updateDashboard**](DashboardsApi.md#updateDashboard) | **PUT** /rest/api/3/dashboard/{id} | Update dashboard
[**updateGadget**](DashboardsApi.md#updateGadget) | **PUT** /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId} | Update gadget on dashboard



## addGadget

> DashboardGadget addGadget(dashboardId, dashboardGadgetSettings)

Add gadget to dashboard

Adds a gadget to a dashboard.  **[Permissions](#permissions) required:** None.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let dashboardId = 789; // Number | The ID of the dashboard.
let dashboardGadgetSettings = {"color":"blue","ignoreUriAndModuleKeyValidation":false,"moduleKey":"com.atlassian.plugins.atlassian-connect-plugin:com.atlassian.connect.node.sample-addon__sample-dashboard-item","position":{"column":1,"row":0},"title":"Issue statistics"}; // DashboardGadgetSettings | 
apiInstance.addGadget(dashboardId, dashboardGadgetSettings, (error, data, response) => {
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
 **dashboardId** | **Number**| The ID of the dashboard. | 
 **dashboardGadgetSettings** | [**DashboardGadgetSettings**](DashboardGadgetSettings.md)|  | 

### Return type

[**DashboardGadget**](DashboardGadget.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## copyDashboard

> Dashboard copyDashboard(id, dashboardDetails)

Copy dashboard

Copies a dashboard. Any values provided in the &#x60;dashboard&#x60; parameter replace those in the copied dashboard.  **[Permissions](#permissions) required:** None  The dashboard to be copied must be owned by or shared with the user.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let id = "id_example"; // String | 
let dashboardDetails = {"description":"A dashboard to help auditors identify sample of issues to check.","editPermissions":[],"name":"Auditors dashboard","sharePermissions":[{"type":"global"}]}; // DashboardDetails | Dashboard details.
apiInstance.copyDashboard(id, dashboardDetails, (error, data, response) => {
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
 **id** | **String**|  | 
 **dashboardDetails** | [**DashboardDetails**](DashboardDetails.md)| Dashboard details. | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDashboard

> Dashboard createDashboard(dashboardDetails)

Create dashboard

Creates a dashboard.  **[Permissions](#permissions) required:** None.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let dashboardDetails = {"description":"A dashboard to help auditors identify sample of issues to check.","editPermissions":[],"name":"Auditors dashboard","sharePermissions":[{"type":"global"}]}; // DashboardDetails | Dashboard details.
apiInstance.createDashboard(dashboardDetails, (error, data, response) => {
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
 **dashboardDetails** | [**DashboardDetails**](DashboardDetails.md)| Dashboard details. | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDashboard

> deleteDashboard(id)

Delete dashboard

Deletes a dashboard.  **[Permissions](#permissions) required:** None  The dashboard to be deleted must be owned by the user.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let id = "id_example"; // String | The ID of the dashboard.
apiInstance.deleteDashboard(id, (error, data, response) => {
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
 **id** | **String**| The ID of the dashboard. | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDashboardItemProperty

> deleteDashboardItemProperty(dashboardId, itemId, propertyKey)

Delete dashboard item property

Deletes a dashboard item property.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The user must be the owner of the dashboard. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let dashboardId = "dashboardId_example"; // String | The ID of the dashboard.
let itemId = "itemId_example"; // String | The ID of the dashboard item.
let propertyKey = "propertyKey_example"; // String | The key of the dashboard item property.
apiInstance.deleteDashboardItemProperty(dashboardId, itemId, propertyKey, (error, data, response) => {
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
 **dashboardId** | **String**| The ID of the dashboard. | 
 **itemId** | **String**| The ID of the dashboard item. | 
 **propertyKey** | **String**| The key of the dashboard item property. | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllAvailableDashboardGadgets

> AvailableDashboardGadgetsResponse getAllAvailableDashboardGadgets()

Get available gadgets

Gets a list of all available gadgets that can be added to all dashboards.  **[Permissions](#permissions) required:** None.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
apiInstance.getAllAvailableDashboardGadgets((error, data, response) => {
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

[**AvailableDashboardGadgetsResponse**](AvailableDashboardGadgetsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllDashboards

> PageOfDashboards getAllDashboards(opts)

Get all dashboards

Returns a list of dashboards owned by or shared with the user. The list may be filtered to include only favorite or owned dashboards.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let opts = {
  'filter': "filter_example", // String | The filter applied to the list of dashboards. Valid values are:   *  `favourite` Returns dashboards the user has marked as favorite.  *  `my` Returns dashboards owned by the user.
  'startAt': 0, // Number | The index of the first item to return in a page of results (page offset).
  'maxResults': 20 // Number | The maximum number of items to return per page.
};
apiInstance.getAllDashboards(opts, (error, data, response) => {
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
 **filter** | **String**| The filter applied to the list of dashboards. Valid values are:   *  &#x60;favourite&#x60; Returns dashboards the user has marked as favorite.  *  &#x60;my&#x60; Returns dashboards owned by the user. | [optional] 
 **startAt** | **Number**| The index of the first item to return in a page of results (page offset). | [optional] [default to 0]
 **maxResults** | **Number**| The maximum number of items to return per page. | [optional] [default to 20]

### Return type

[**PageOfDashboards**](PageOfDashboards.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllGadgets

> DashboardGadgetResponse getAllGadgets(dashboardId, opts)

Get gadgets

Returns a list of dashboard gadgets on a dashboard.  This operation returns:   *  Gadgets from a list of IDs, when &#x60;id&#x60; is set.  *  Gadgets with a module key, when &#x60;moduleKey&#x60; is set.  *  Gadgets from a list of URIs, when &#x60;uri&#x60; is set.  *  All gadgets, when no other parameters are set.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let dashboardId = 789; // Number | The ID of the dashboard.
let opts = {
  'moduleKey': ["null"], // [String] | The list of gadgets module keys. To include multiple module keys, separate module keys with ampersand: `moduleKey=key:one&moduleKey=key:two`.
  'uri': ["null"], // [String] | The list of gadgets URIs. To include multiple URIs, separate URIs with ampersand: `uri=/rest/example/uri/1&uri=/rest/example/uri/2`.
  'gadgetId': [null] // [Number] | The list of gadgets IDs. To include multiple IDs, separate IDs with ampersand: `gadgetId=10000&gadgetId=10001`.
};
apiInstance.getAllGadgets(dashboardId, opts, (error, data, response) => {
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
 **dashboardId** | **Number**| The ID of the dashboard. | 
 **moduleKey** | [**[String]**](String.md)| The list of gadgets module keys. To include multiple module keys, separate module keys with ampersand: &#x60;moduleKey&#x3D;key:one&amp;moduleKey&#x3D;key:two&#x60;. | [optional] 
 **uri** | [**[String]**](String.md)| The list of gadgets URIs. To include multiple URIs, separate URIs with ampersand: &#x60;uri&#x3D;/rest/example/uri/1&amp;uri&#x3D;/rest/example/uri/2&#x60;. | [optional] 
 **gadgetId** | [**[Number]**](Number.md)| The list of gadgets IDs. To include multiple IDs, separate IDs with ampersand: &#x60;gadgetId&#x3D;10000&amp;gadgetId&#x3D;10001&#x60;. | [optional] 

### Return type

[**DashboardGadgetResponse**](DashboardGadgetResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDashboard

> Dashboard getDashboard(id)

Get dashboard

Returns a dashboard.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.  However, to get a dashboard, the dashboard must be shared with the user or the user must own it. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let id = "id_example"; // String | The ID of the dashboard.
apiInstance.getDashboard(id, (error, data, response) => {
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
 **id** | **String**| The ID of the dashboard. | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDashboardItemProperty

> EntityProperty getDashboardItemProperty(dashboardId, itemId, propertyKey)

Get dashboard item property

Returns the key and value of a dashboard item property.  A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. For more information on how users do this, see [Adding and customizing gadgets](https://confluence.atlassian.com/x/7AeiLQ).  When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The callback fires whenever the item is rendered or, where the item is configurable, the user edits the item. The app then uses this resource to store the item&#39;s content or configuration details. For more information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-connect-add-on-33746254/) and the [Dashboard Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.  There is no resource to set or get dashboard items.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the dashboard shared with them. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users, and is accessible to anonymous users when Jira’s anonymous access is permitted.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let dashboardId = "dashboardId_example"; // String | The ID of the dashboard.
let itemId = "itemId_example"; // String | The ID of the dashboard item.
let propertyKey = "propertyKey_example"; // String | The key of the dashboard item property.
apiInstance.getDashboardItemProperty(dashboardId, itemId, propertyKey, (error, data, response) => {
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
 **dashboardId** | **String**| The ID of the dashboard. | 
 **itemId** | **String**| The ID of the dashboard item. | 
 **propertyKey** | **String**| The key of the dashboard item property. | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDashboardItemPropertyKeys

> PropertyKeys getDashboardItemPropertyKeys(dashboardId, itemId)

Get dashboard item property keys

Returns the keys of all properties for a dashboard item.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the dashboard shared with them. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users, and is accessible to anonymous users when Jira’s anonymous access is permitted.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let dashboardId = "dashboardId_example"; // String | The ID of the dashboard.
let itemId = "itemId_example"; // String | The ID of the dashboard item.
apiInstance.getDashboardItemPropertyKeys(dashboardId, itemId, (error, data, response) => {
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
 **dashboardId** | **String**| The ID of the dashboard. | 
 **itemId** | **String**| The ID of the dashboard item. | 

### Return type

[**PropertyKeys**](PropertyKeys.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDashboardsPaginated

> PageBeanDashboard getDashboardsPaginated(opts)

Search for dashboards

Returns a [paginated](#pagination) list of dashboards. This operation is similar to [Get dashboards](#api-rest-api-3-dashboard-get) except that the results can be refined to include dashboards that have specific attributes. For example, dashboards with a particular name. When multiple attributes are specified only filters matching all attributes are returned.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The following dashboards that match the query parameters are returned:   *  Dashboards owned by the user. Not returned for anonymous users.  *  Dashboards shared with a group that the user is a member of. Not returned for anonymous users.  *  Dashboards shared with a private project that the user can browse. Not returned for anonymous users.  *  Dashboards shared with a public project.  *  Dashboards shared with the public.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let opts = {
  'dashboardName': "dashboardName_example", // String | String used to perform a case-insensitive partial match with `name`.
  'accountId': "accountId_example", // String | User account ID used to return dashboards with the matching `owner.accountId`. This parameter cannot be used with the `owner` parameter.
  'owner': "owner_example", // String | This parameter is deprecated because of privacy changes. Use `accountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. User name used to return dashboards with the matching `owner.name`. This parameter cannot be used with the `accountId` parameter.
  'groupname': "groupname_example", // String | As a group's name can change, use of `groupId` is recommended. Group name used to return dashboards that are shared with a group that matches `sharePermissions.group.name`. This parameter cannot be used with the `groupId` parameter.
  'groupId': "groupId_example", // String | Group ID used to return dashboards that are shared with a group that matches `sharePermissions.group.groupId`. This parameter cannot be used with the `groupname` parameter.
  'projectId': 789, // Number | Project ID used to returns dashboards that are shared with a project that matches `sharePermissions.project.id`.
  'orderBy': "'name'", // String | [Order](#ordering) the results by a field:   *  `description` Sorts by dashboard description. Note that this sort works independently of whether the expand to display the description field is in use.  *  `favourite_count` Sorts by dashboard popularity.  *  `id` Sorts by dashboard ID.  *  `is_favourite` Sorts by whether the dashboard is marked as a favorite.  *  `name` Sorts by dashboard name.  *  `owner` Sorts by dashboard owner name.
  'startAt': 0, // Number | The index of the first item to return in a page of results (page offset).
  'maxResults': 50, // Number | The maximum number of items to return per page.
  'status': "'active'", // String | The status to filter by. It may be active, archived or deleted.
  'expand': "expand_example" // String | Use [expand](#expansion) to include additional information about dashboard in the response. This parameter accepts a comma-separated list. Expand options include:   *  `description` Returns the description of the dashboard.  *  `owner` Returns the owner of the dashboard.  *  `viewUrl` Returns the URL that is used to view the dashboard.  *  `favourite` Returns `isFavourite`, an indicator of whether the user has set the dashboard as a favorite.  *  `favouritedCount` Returns `popularity`, a count of how many users have set this dashboard as a favorite.  *  `sharePermissions` Returns details of the share permissions defined for the dashboard.  *  `editPermissions` Returns details of the edit permissions defined for the dashboard.  *  `isWritable` Returns whether the current user has permission to edit the dashboard.
};
apiInstance.getDashboardsPaginated(opts, (error, data, response) => {
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
 **dashboardName** | **String**| String used to perform a case-insensitive partial match with &#x60;name&#x60;. | [optional] 
 **accountId** | **String**| User account ID used to return dashboards with the matching &#x60;owner.accountId&#x60;. This parameter cannot be used with the &#x60;owner&#x60; parameter. | [optional] 
 **owner** | **String**| This parameter is deprecated because of privacy changes. Use &#x60;accountId&#x60; instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. User name used to return dashboards with the matching &#x60;owner.name&#x60;. This parameter cannot be used with the &#x60;accountId&#x60; parameter. | [optional] 
 **groupname** | **String**| As a group&#39;s name can change, use of &#x60;groupId&#x60; is recommended. Group name used to return dashboards that are shared with a group that matches &#x60;sharePermissions.group.name&#x60;. This parameter cannot be used with the &#x60;groupId&#x60; parameter. | [optional] 
 **groupId** | **String**| Group ID used to return dashboards that are shared with a group that matches &#x60;sharePermissions.group.groupId&#x60;. This parameter cannot be used with the &#x60;groupname&#x60; parameter. | [optional] 
 **projectId** | **Number**| Project ID used to returns dashboards that are shared with a project that matches &#x60;sharePermissions.project.id&#x60;. | [optional] 
 **orderBy** | **String**| [Order](#ordering) the results by a field:   *  &#x60;description&#x60; Sorts by dashboard description. Note that this sort works independently of whether the expand to display the description field is in use.  *  &#x60;favourite_count&#x60; Sorts by dashboard popularity.  *  &#x60;id&#x60; Sorts by dashboard ID.  *  &#x60;is_favourite&#x60; Sorts by whether the dashboard is marked as a favorite.  *  &#x60;name&#x60; Sorts by dashboard name.  *  &#x60;owner&#x60; Sorts by dashboard owner name. | [optional] [default to &#39;name&#39;]
 **startAt** | **Number**| The index of the first item to return in a page of results (page offset). | [optional] [default to 0]
 **maxResults** | **Number**| The maximum number of items to return per page. | [optional] [default to 50]
 **status** | **String**| The status to filter by. It may be active, archived or deleted. | [optional] [default to &#39;active&#39;]
 **expand** | **String**| Use [expand](#expansion) to include additional information about dashboard in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;description&#x60; Returns the description of the dashboard.  *  &#x60;owner&#x60; Returns the owner of the dashboard.  *  &#x60;viewUrl&#x60; Returns the URL that is used to view the dashboard.  *  &#x60;favourite&#x60; Returns &#x60;isFavourite&#x60;, an indicator of whether the user has set the dashboard as a favorite.  *  &#x60;favouritedCount&#x60; Returns &#x60;popularity&#x60;, a count of how many users have set this dashboard as a favorite.  *  &#x60;sharePermissions&#x60; Returns details of the share permissions defined for the dashboard.  *  &#x60;editPermissions&#x60; Returns details of the edit permissions defined for the dashboard.  *  &#x60;isWritable&#x60; Returns whether the current user has permission to edit the dashboard. | [optional] 

### Return type

[**PageBeanDashboard**](PageBeanDashboard.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeGadget

> Object removeGadget(dashboardId, gadgetId)

Remove gadget from dashboard

Removes a dashboard gadget from a dashboard.  When a gadget is removed from a dashboard, other gadgets in the same column are moved up to fill the emptied position.  **[Permissions](#permissions) required:** None.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let dashboardId = 789; // Number | The ID of the dashboard.
let gadgetId = 789; // Number | The ID of the gadget.
apiInstance.removeGadget(dashboardId, gadgetId, (error, data, response) => {
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
 **dashboardId** | **Number**| The ID of the dashboard. | 
 **gadgetId** | **Number**| The ID of the gadget. | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setDashboardItemProperty

> Object setDashboardItemProperty(dashboardId, itemId, propertyKey, body)

Set dashboard item property

Sets the value of a dashboard item property. Use this resource in apps to store custom data against a dashboard item.  A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. For more information on how users do this, see [Adding and customizing gadgets](https://confluence.atlassian.com/x/7AeiLQ).  When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The callback fires whenever the item is rendered or, where the item is configurable, the user edits the item. The app then uses this resource to store the item&#39;s content or configuration details. For more information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-connect-add-on-33746254/) and the [Dashboard Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.  There is no resource to set or get dashboard items.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The user must be the owner of the dashboard. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let dashboardId = "dashboardId_example"; // String | The ID of the dashboard.
let itemId = "itemId_example"; // String | The ID of the dashboard item.
let propertyKey = "propertyKey_example"; // String | The key of the dashboard item property. The maximum length is 255 characters. For dashboard items with a spec URI and no complete module key, if the provided propertyKey is equal to \"config\", the request body's JSON must be an object with all keys and values as strings.
let body = {"number":5,"string":"string-value"}; // Object | 
apiInstance.setDashboardItemProperty(dashboardId, itemId, propertyKey, body, (error, data, response) => {
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
 **dashboardId** | **String**| The ID of the dashboard. | 
 **itemId** | **String**| The ID of the dashboard item. | 
 **propertyKey** | **String**| The key of the dashboard item property. The maximum length is 255 characters. For dashboard items with a spec URI and no complete module key, if the provided propertyKey is equal to \&quot;config\&quot;, the request body&#39;s JSON must be an object with all keys and values as strings. | 
 **body** | **Object**|  | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDashboard

> Dashboard updateDashboard(id, dashboardDetails)

Update dashboard

Updates a dashboard, replacing all the dashboard details with those provided.  **[Permissions](#permissions) required:** None  The dashboard to be updated must be owned by the user.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let id = "id_example"; // String | The ID of the dashboard to update.
let dashboardDetails = {"description":"A dashboard to help auditors identify sample of issues to check.","editPermissions":[],"name":"Auditors dashboard","sharePermissions":[{"type":"global"}]}; // DashboardDetails | Replacement dashboard details.
apiInstance.updateDashboard(id, dashboardDetails, (error, data, response) => {
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
 **id** | **String**| The ID of the dashboard to update. | 
 **dashboardDetails** | [**DashboardDetails**](DashboardDetails.md)| Replacement dashboard details. | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGadget

> Object updateGadget(dashboardId, gadgetId, dashboardGadgetUpdateRequest)

Update gadget on dashboard

Changes the title, position, and color of the gadget on a dashboard.  **[Permissions](#permissions) required:** None.

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

let apiInstance = new TheJiraCloudPlatformRestApi.DashboardsApi();
let dashboardId = 789; // Number | The ID of the dashboard.
let gadgetId = 789; // Number | The ID of the gadget.
let dashboardGadgetUpdateRequest = {"color":"red","position":{"column":1,"row":1},"title":"My new gadget title"}; // DashboardGadgetUpdateRequest | 
apiInstance.updateGadget(dashboardId, gadgetId, dashboardGadgetUpdateRequest, (error, data, response) => {
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
 **dashboardId** | **Number**| The ID of the dashboard. | 
 **gadgetId** | **Number**| The ID of the gadget. | 
 **dashboardGadgetUpdateRequest** | [**DashboardGadgetUpdateRequest**](DashboardGadgetUpdateRequest.md)|  | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


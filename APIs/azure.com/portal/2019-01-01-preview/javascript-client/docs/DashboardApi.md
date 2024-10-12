# Portal.DashboardApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboardsCreateOrUpdate**](DashboardApi.md#dashboardsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName} | 
[**dashboardsDelete**](DashboardApi.md#dashboardsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName} | 
[**dashboardsGet**](DashboardApi.md#dashboardsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName} | 
[**dashboardsListByResourceGroup**](DashboardApi.md#dashboardsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards | 
[**dashboardsListBySubscription**](DashboardApi.md#dashboardsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Portal/dashboards | 
[**dashboardsUpdate**](DashboardApi.md#dashboardsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName} | 



## dashboardsCreateOrUpdate

> Dashboard dashboardsCreateOrUpdate(subscriptionId, resourceGroupName, dashboardName, apiVersion, dashboard)



Creates or updates a Dashboard.

### Example

```javascript
import Portal from 'portal';
let defaultClient = Portal.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Portal.DashboardApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let dashboardName = "dashboardName_example"; // String | The name of the dashboard.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let dashboard = new Portal.Dashboard(); // Dashboard | The parameters required to create or update a dashboard.
apiInstance.dashboardsCreateOrUpdate(subscriptionId, resourceGroupName, dashboardName, apiVersion, dashboard, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **dashboardName** | **String**| The name of the dashboard. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **dashboard** | [**Dashboard**](Dashboard.md)| The parameters required to create or update a dashboard. | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dashboardsDelete

> dashboardsDelete(subscriptionId, resourceGroupName, dashboardName, apiVersion)



Deletes the Dashboard.

### Example

```javascript
import Portal from 'portal';
let defaultClient = Portal.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Portal.DashboardApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let dashboardName = "dashboardName_example"; // String | The name of the dashboard.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.dashboardsDelete(subscriptionId, resourceGroupName, dashboardName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **dashboardName** | **String**| The name of the dashboard. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dashboardsGet

> Dashboard dashboardsGet(subscriptionId, resourceGroupName, dashboardName, apiVersion)



Gets the Dashboard.

### Example

```javascript
import Portal from 'portal';
let defaultClient = Portal.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Portal.DashboardApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let dashboardName = "dashboardName_example"; // String | The name of the dashboard.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.dashboardsGet(subscriptionId, resourceGroupName, dashboardName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **dashboardName** | **String**| The name of the dashboard. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dashboardsListByResourceGroup

> DashboardListResult dashboardsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Gets all the Dashboards within a resource group.

### Example

```javascript
import Portal from 'portal';
let defaultClient = Portal.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Portal.DashboardApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.dashboardsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

[**DashboardListResult**](DashboardListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dashboardsListBySubscription

> DashboardListResult dashboardsListBySubscription(subscriptionId, apiVersion)



Gets all the dashboards within a subscription.

### Example

```javascript
import Portal from 'portal';
let defaultClient = Portal.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Portal.DashboardApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.dashboardsListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

[**DashboardListResult**](DashboardListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dashboardsUpdate

> Dashboard dashboardsUpdate(subscriptionId, resourceGroupName, dashboardName, apiVersion, dashboard)



Updates an existing Dashboard.

### Example

```javascript
import Portal from 'portal';
let defaultClient = Portal.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Portal.DashboardApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let dashboardName = "dashboardName_example"; // String | The name of the dashboard.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let dashboard = new Portal.PatchableDashboard(); // PatchableDashboard | The updatable fields of a Dashboard.
apiInstance.dashboardsUpdate(subscriptionId, resourceGroupName, dashboardName, apiVersion, dashboard, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **dashboardName** | **String**| The name of the dashboard. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **dashboard** | [**PatchableDashboard**](PatchableDashboard.md)| The updatable fields of a Dashboard. | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


# AzureActivityLogAlerts.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activityLogAlertsCreateOrUpdate**](DefaultApi.md#activityLogAlertsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts/{activityLogAlertName} | 
[**activityLogAlertsDelete**](DefaultApi.md#activityLogAlertsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts/{activityLogAlertName} | 
[**activityLogAlertsGet**](DefaultApi.md#activityLogAlertsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts/{activityLogAlertName} | 
[**activityLogAlertsListByResourceGroup**](DefaultApi.md#activityLogAlertsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts | 
[**activityLogAlertsListBySubscriptionId**](DefaultApi.md#activityLogAlertsListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/activityLogAlerts | 
[**activityLogAlertsUpdate**](DefaultApi.md#activityLogAlertsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts/{activityLogAlertName} | 



## activityLogAlertsCreateOrUpdate

> ActivityLogAlertResource activityLogAlertsCreateOrUpdate(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion, activityLogAlert)



Create a new activity log alert or update an existing one.

### Example

```javascript
import AzureActivityLogAlerts from 'azure_activity_log_alerts';
let defaultClient = AzureActivityLogAlerts.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActivityLogAlerts.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let activityLogAlertName = "activityLogAlertName_example"; // String | The name of the activity log alert.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let activityLogAlert = new AzureActivityLogAlerts.ActivityLogAlertResource(); // ActivityLogAlertResource | The activity log alert to create or use for the update.
apiInstance.activityLogAlertsCreateOrUpdate(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion, activityLogAlert, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **activityLogAlertName** | **String**| The name of the activity log alert. | 
 **apiVersion** | **String**| Client Api Version. | 
 **activityLogAlert** | [**ActivityLogAlertResource**](ActivityLogAlertResource.md)| The activity log alert to create or use for the update. | 

### Return type

[**ActivityLogAlertResource**](ActivityLogAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## activityLogAlertsDelete

> activityLogAlertsDelete(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion)



Delete an activity log alert.

### Example

```javascript
import AzureActivityLogAlerts from 'azure_activity_log_alerts';
let defaultClient = AzureActivityLogAlerts.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActivityLogAlerts.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let activityLogAlertName = "activityLogAlertName_example"; // String | The name of the activity log alert.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.activityLogAlertsDelete(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **activityLogAlertName** | **String**| The name of the activity log alert. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activityLogAlertsGet

> ActivityLogAlertResource activityLogAlertsGet(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion)



Get an activity log alert.

### Example

```javascript
import AzureActivityLogAlerts from 'azure_activity_log_alerts';
let defaultClient = AzureActivityLogAlerts.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActivityLogAlerts.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let activityLogAlertName = "activityLogAlertName_example"; // String | The name of the activity log alert.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.activityLogAlertsGet(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **activityLogAlertName** | **String**| The name of the activity log alert. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**ActivityLogAlertResource**](ActivityLogAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activityLogAlertsListByResourceGroup

> ActivityLogAlertList activityLogAlertsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Get a list of all activity log alerts in a resource group.

### Example

```javascript
import AzureActivityLogAlerts from 'azure_activity_log_alerts';
let defaultClient = AzureActivityLogAlerts.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActivityLogAlerts.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.activityLogAlertsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**ActivityLogAlertList**](ActivityLogAlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activityLogAlertsListBySubscriptionId

> ActivityLogAlertList activityLogAlertsListBySubscriptionId(subscriptionId, apiVersion)



Get a list of all activity log alerts in a subscription.

### Example

```javascript
import AzureActivityLogAlerts from 'azure_activity_log_alerts';
let defaultClient = AzureActivityLogAlerts.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActivityLogAlerts.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.activityLogAlertsListBySubscriptionId(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**ActivityLogAlertList**](ActivityLogAlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activityLogAlertsUpdate

> ActivityLogAlertResource activityLogAlertsUpdate(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion, activityLogAlertPatch)



Updates an existing ActivityLogAlertResource&#39;s tags. To update other fields use the CreateOrUpdate method.

### Example

```javascript
import AzureActivityLogAlerts from 'azure_activity_log_alerts';
let defaultClient = AzureActivityLogAlerts.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActivityLogAlerts.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let activityLogAlertName = "activityLogAlertName_example"; // String | The name of the activity log alert.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let activityLogAlertPatch = new AzureActivityLogAlerts.ActivityLogAlertPatchBody(); // ActivityLogAlertPatchBody | Parameters supplied to the operation.
apiInstance.activityLogAlertsUpdate(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion, activityLogAlertPatch, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **activityLogAlertName** | **String**| The name of the activity log alert. | 
 **apiVersion** | **String**| Client Api Version. | 
 **activityLogAlertPatch** | [**ActivityLogAlertPatchBody**](ActivityLogAlertPatchBody.md)| Parameters supplied to the operation. | 

### Return type

[**ActivityLogAlertResource**](ActivityLogAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


# StorSimpleManagementClient.AlertsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertsClear**](AlertsApi.md#alertsClear) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/clearAlerts | 
[**alertsListByManager**](AlertsApi.md#alertsListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/alerts | 
[**alertsSendTestEmail**](AlertsApi.md#alertsSendTestEmail) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/sendTestAlertEmail | 



## alertsClear

> alertsClear(subscriptionId, resourceGroupName, managerName, apiVersion, request)



Clear the alerts.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.AlertsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let request = new StorSimpleManagementClient.ClearAlertRequest(); // ClearAlertRequest | The clear alert request.
apiInstance.alertsClear(subscriptionId, resourceGroupName, managerName, apiVersion, request, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **request** | [**ClearAlertRequest**](ClearAlertRequest.md)| The clear alert request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## alertsListByManager

> AlertList alertsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion, opts)



Retrieves all the alerts in a manager.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.AlertsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let opts = {
  'filter': "filter_example" // String | OData Filter options
};
apiInstance.alertsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **filter** | **String**| OData Filter options | [optional] 

### Return type

[**AlertList**](AlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsSendTestEmail

> alertsSendTestEmail(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, request)



Sends a test alert email.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.AlertsApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let request = new StorSimpleManagementClient.SendTestAlertEmailRequest(); // SendTestAlertEmailRequest | The send test alert email request.
apiInstance.alertsSendTestEmail(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, request, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **request** | [**SendTestAlertEmailRequest**](SendTestAlertEmailRequest.md)| The send test alert email request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


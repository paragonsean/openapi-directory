# SecurityCenter.AlertsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertsGetResourceGroupLevelAlerts**](AlertsApi.md#alertsGetResourceGroupLevelAlerts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/alerts/{alertName} | 
[**alertsGetSubscriptionLevelAlert**](AlertsApi.md#alertsGetSubscriptionLevelAlert) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/alerts/{alertName} | 
[**alertsList**](AlertsApi.md#alertsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/alerts | 
[**alertsListByResourceGroup**](AlertsApi.md#alertsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/alerts | 
[**alertsListResourceGroupLevelAlertsByRegion**](AlertsApi.md#alertsListResourceGroupLevelAlertsByRegion) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/alerts | 
[**alertsListSubscriptionLevelAlertsByRegion**](AlertsApi.md#alertsListSubscriptionLevelAlertsByRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/alerts | 
[**alertsUpdateResourceGroupLevelAlertState**](AlertsApi.md#alertsUpdateResourceGroupLevelAlertState) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/alerts/{alertName}/{alertUpdateActionType} | 
[**alertsUpdateSubscriptionLevelAlertState**](AlertsApi.md#alertsUpdateSubscriptionLevelAlertState) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/alerts/{alertName}/{alertUpdateActionType} | 



## alertsGetResourceGroupLevelAlerts

> Alert alertsGetResourceGroupLevelAlerts(apiVersion, subscriptionId, ascLocation, alertName, resourceGroupName)



Get an alert that is associated a resource group or a resource in a resource group

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AlertsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let alertName = "alertName_example"; // String | Name of the alert object
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
apiInstance.alertsGetResourceGroupLevelAlerts(apiVersion, subscriptionId, ascLocation, alertName, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **alertName** | **String**| Name of the alert object | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetSubscriptionLevelAlert

> Alert alertsGetSubscriptionLevelAlert(apiVersion, subscriptionId, ascLocation, alertName)



Get an alert that is associated with a subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AlertsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let alertName = "alertName_example"; // String | Name of the alert object
apiInstance.alertsGetSubscriptionLevelAlert(apiVersion, subscriptionId, ascLocation, alertName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **alertName** | **String**| Name of the alert object | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsList

> AlertList alertsList(apiVersion, subscriptionId, opts)



List all the alerts that are associated with the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AlertsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'select': "select_example", // String | OData select. Optional.
  'expand': "expand_example" // String | OData expand. Optional.
};
apiInstance.alertsList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **select** | **String**| OData select. Optional. | [optional] 
 **expand** | **String**| OData expand. Optional. | [optional] 

### Return type

[**AlertList**](AlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsListByResourceGroup

> AlertList alertsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, opts)



List all the alerts that are associated with the resource group

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AlertsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'select': "select_example", // String | OData select. Optional.
  'expand': "expand_example" // String | OData expand. Optional.
};
apiInstance.alertsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **select** | **String**| OData select. Optional. | [optional] 
 **expand** | **String**| OData expand. Optional. | [optional] 

### Return type

[**AlertList**](AlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsListResourceGroupLevelAlertsByRegion

> AlertList alertsListResourceGroupLevelAlertsByRegion(apiVersion, subscriptionId, ascLocation, resourceGroupName, opts)



List all the alerts that are associated with the resource group that are stored in a specific location

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AlertsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'select': "select_example", // String | OData select. Optional.
  'expand': "expand_example" // String | OData expand. Optional.
};
apiInstance.alertsListResourceGroupLevelAlertsByRegion(apiVersion, subscriptionId, ascLocation, resourceGroupName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **select** | **String**| OData select. Optional. | [optional] 
 **expand** | **String**| OData expand. Optional. | [optional] 

### Return type

[**AlertList**](AlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsListSubscriptionLevelAlertsByRegion

> AlertList alertsListSubscriptionLevelAlertsByRegion(apiVersion, subscriptionId, ascLocation, opts)



List all the alerts that are associated with the subscription that are stored in a specific location

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AlertsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'select': "select_example", // String | OData select. Optional.
  'expand': "expand_example" // String | OData expand. Optional.
};
apiInstance.alertsListSubscriptionLevelAlertsByRegion(apiVersion, subscriptionId, ascLocation, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **select** | **String**| OData select. Optional. | [optional] 
 **expand** | **String**| OData expand. Optional. | [optional] 

### Return type

[**AlertList**](AlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsUpdateResourceGroupLevelAlertState

> alertsUpdateResourceGroupLevelAlertState(apiVersion, subscriptionId, ascLocation, alertName, alertUpdateActionType, resourceGroupName)



Update the alert&#39;s state

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AlertsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let alertName = "alertName_example"; // String | Name of the alert object
let alertUpdateActionType = "alertUpdateActionType_example"; // String | Type of the action to do on the alert
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
apiInstance.alertsUpdateResourceGroupLevelAlertState(apiVersion, subscriptionId, ascLocation, alertName, alertUpdateActionType, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **alertName** | **String**| Name of the alert object | 
 **alertUpdateActionType** | **String**| Type of the action to do on the alert | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsUpdateSubscriptionLevelAlertState

> alertsUpdateSubscriptionLevelAlertState(apiVersion, subscriptionId, ascLocation, alertName, alertUpdateActionType)



Update the alert&#39;s state

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AlertsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let alertName = "alertName_example"; // String | Name of the alert object
let alertUpdateActionType = "alertUpdateActionType_example"; // String | Type of the action to do on the alert
apiInstance.alertsUpdateSubscriptionLevelAlertState(apiVersion, subscriptionId, ascLocation, alertName, alertUpdateActionType, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **alertName** | **String**| Name of the alert object | 
 **alertUpdateActionType** | **String**| Type of the action to do on the alert | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


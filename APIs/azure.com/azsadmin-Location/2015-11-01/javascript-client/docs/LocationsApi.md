# SubscriptionsManagementClient.LocationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationsCreateOrUpdate**](LocationsApi.md#locationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/locations/{location} | 
[**locationsGet**](LocationsApi.md#locationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/locations/{location} | 
[**locationsGetOperationsStatus**](LocationsApi.md#locationsGetOperationsStatus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/locations/{location}/operationsStatus/{operationsStatusName} | 
[**locationsList**](LocationsApi.md#locationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/locations | 



## locationsCreateOrUpdate

> Location locationsCreateOrUpdate(subscriptionId, location, apiVersion, newLocation)



Updates the specified location.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.LocationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The AzureStack location.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
let newLocation = new SubscriptionsManagementClient.Location(); // Location | The new location
apiInstance.locationsCreateOrUpdate(subscriptionId, location, apiVersion, newLocation, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The AzureStack location. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]
 **newLocation** | [**Location**](Location.md)| The new location | 

### Return type

[**Location**](Location.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## locationsGet

> Location locationsGet(subscriptionId, location, apiVersion)



Get the specified location.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.LocationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The AzureStack location.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.locationsGet(subscriptionId, location, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The AzureStack location. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**Location**](Location.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsGetOperationsStatus

> OperationsStatus locationsGetOperationsStatus(subscriptionId, location, operationsStatusName, apiVersion)



Get the operation status.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.LocationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The AzureStack location.
let operationsStatusName = "operationsStatusName_example"; // String | The operation status name.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.locationsGetOperationsStatus(subscriptionId, location, operationsStatusName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The AzureStack location. | 
 **operationsStatusName** | **String**| The operation status name. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**OperationsStatus**](OperationsStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsList

> LocationList locationsList(subscriptionId, apiVersion)



Get a list of all AzureStack location.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.LocationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.locationsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**LocationList**](LocationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


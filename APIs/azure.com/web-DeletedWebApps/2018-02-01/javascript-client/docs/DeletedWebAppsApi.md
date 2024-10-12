# DeletedWebAppsApiClient.DeletedWebAppsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletedWebAppsGetDeletedWebAppByLocation**](DeletedWebAppsApi.md#deletedWebAppsGetDeletedWebAppByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/deletedSites/{deletedSiteId} | Get deleted app for a subscription at location.
[**deletedWebAppsList**](DeletedWebAppsApi.md#deletedWebAppsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/deletedSites | Get all deleted apps for a subscription.
[**deletedWebAppsListByLocation**](DeletedWebAppsApi.md#deletedWebAppsListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/deletedSites | Get all deleted apps for a subscription at location



## deletedWebAppsGetDeletedWebAppByLocation

> DeletedWebAppsGetDeletedWebAppByLocation200Response deletedWebAppsGetDeletedWebAppByLocation(location, deletedSiteId, subscriptionId, apiVersion)

Get deleted app for a subscription at location.

Get deleted app for a subscription at location.

### Example

```javascript
import DeletedWebAppsApiClient from 'deleted_web_apps_api_client';
let defaultClient = DeletedWebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeletedWebAppsApiClient.DeletedWebAppsApi();
let location = "location_example"; // String | 
let deletedSiteId = "deletedSiteId_example"; // String | The numeric ID of the deleted app, e.g. 12345
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.deletedWebAppsGetDeletedWebAppByLocation(location, deletedSiteId, subscriptionId, apiVersion, (error, data, response) => {
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
 **location** | **String**|  | 
 **deletedSiteId** | **String**| The numeric ID of the deleted app, e.g. 12345 | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeletedWebAppsGetDeletedWebAppByLocation200Response**](DeletedWebAppsGetDeletedWebAppByLocation200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletedWebAppsList

> DeletedWebAppCollection deletedWebAppsList(subscriptionId, apiVersion)

Get all deleted apps for a subscription.

Get all deleted apps for a subscription.

### Example

```javascript
import DeletedWebAppsApiClient from 'deleted_web_apps_api_client';
let defaultClient = DeletedWebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeletedWebAppsApiClient.DeletedWebAppsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.deletedWebAppsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeletedWebAppCollection**](DeletedWebAppCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletedWebAppsListByLocation

> DeletedWebAppCollection deletedWebAppsListByLocation(location, subscriptionId, apiVersion)

Get all deleted apps for a subscription at location

Get all deleted apps for a subscription at location

### Example

```javascript
import DeletedWebAppsApiClient from 'deleted_web_apps_api_client';
let defaultClient = DeletedWebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeletedWebAppsApiClient.DeletedWebAppsApi();
let location = "location_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.deletedWebAppsListByLocation(location, subscriptionId, apiVersion, (error, data, response) => {
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
 **location** | **String**|  | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeletedWebAppCollection**](DeletedWebAppCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# WebSiteManagementClient.ClassicMobileServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classicMobileServicesDeleteClassicMobileService**](ClassicMobileServicesApi.md#classicMobileServicesDeleteClassicMobileService) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/classicMobileServices/{name} | Delete a mobile service.
[**classicMobileServicesGetClassicMobileService**](ClassicMobileServicesApi.md#classicMobileServicesGetClassicMobileService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/classicMobileServices/{name} | Get a mobile service.
[**classicMobileServicesGetClassicMobileServices**](ClassicMobileServicesApi.md#classicMobileServicesGetClassicMobileServices) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/classicMobileServices | Get all mobile services in a resource group.



## classicMobileServicesDeleteClassicMobileService

> Object classicMobileServicesDeleteClassicMobileService(resourceGroupName, name, subscriptionId, apiVersion)

Delete a mobile service.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ClassicMobileServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of mobile service
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.classicMobileServicesDeleteClassicMobileService(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of mobile service | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## classicMobileServicesGetClassicMobileService

> ClassicMobileService classicMobileServicesGetClassicMobileService(resourceGroupName, name, subscriptionId, apiVersion)

Get a mobile service.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ClassicMobileServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of mobile service
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.classicMobileServicesGetClassicMobileService(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of mobile service | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ClassicMobileService**](ClassicMobileService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## classicMobileServicesGetClassicMobileServices

> ClassicMobileServiceCollection classicMobileServicesGetClassicMobileServices(resourceGroupName, subscriptionId, apiVersion)

Get all mobile services in a resource group.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ClassicMobileServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.classicMobileServicesGetClassicMobileServices(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ClassicMobileServiceCollection**](ClassicMobileServiceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


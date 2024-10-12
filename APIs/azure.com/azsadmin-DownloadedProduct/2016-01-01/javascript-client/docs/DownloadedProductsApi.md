# AzureBridgeAdminClient.DownloadedProductsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadedProductsCreate**](DownloadedProductsApi.md#downloadedProductsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/downloadedProducts/{productName} | 
[**downloadedProductsDelete**](DownloadedProductsApi.md#downloadedProductsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/downloadedProducts/{productName} | 
[**downloadedProductsGet**](DownloadedProductsApi.md#downloadedProductsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/downloadedProducts/{productName} | 
[**downloadedProductsList**](DownloadedProductsApi.md#downloadedProductsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/downloadedProducts | 



## downloadedProductsCreate

> DownloadedProductsGet200Response downloadedProductsCreate(subscriptionId, resourceGroup, activationName, productName, apiVersion, downloadedProduct)



Creates a downloaded product.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.DownloadedProductsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let activationName = "activationName_example"; // String | Name of the activation.
let productName = "productName_example"; // String | Name of the product.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
let downloadedProduct = new AzureBridgeAdminClient.DownloadedProductsGet200Response(); // DownloadedProductsGet200Response | Downloaded product resource definition.
apiInstance.downloadedProductsCreate(subscriptionId, resourceGroup, activationName, productName, apiVersion, downloadedProduct, (error, data, response) => {
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
 **resourceGroup** | **String**| The resource group the resource is located under. | 
 **activationName** | **String**| Name of the activation. | 
 **productName** | **String**| Name of the product. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-01-01&#39;]
 **downloadedProduct** | [**DownloadedProductsGet200Response**](DownloadedProductsGet200Response.md)| Downloaded product resource definition. | 

### Return type

[**DownloadedProductsGet200Response**](DownloadedProductsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## downloadedProductsDelete

> DownloadedProductsGet200Response downloadedProductsDelete(subscriptionId, resourceGroup, activationName, productName, apiVersion)



Delete a downloaded product.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.DownloadedProductsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let activationName = "activationName_example"; // String | Name of the activation.
let productName = "productName_example"; // String | Name of the product.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
apiInstance.downloadedProductsDelete(subscriptionId, resourceGroup, activationName, productName, apiVersion, (error, data, response) => {
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
 **resourceGroup** | **String**| The resource group the resource is located under. | 
 **activationName** | **String**| Name of the activation. | 
 **productName** | **String**| Name of the product. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-01-01&#39;]

### Return type

[**DownloadedProductsGet200Response**](DownloadedProductsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## downloadedProductsGet

> DownloadedProductsGet200Response downloadedProductsGet(subscriptionId, resourceGroup, activationName, productName, apiVersion)



Get a downloaded product.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.DownloadedProductsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let activationName = "activationName_example"; // String | Name of the activation.
let productName = "productName_example"; // String | Name of the product.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
apiInstance.downloadedProductsGet(subscriptionId, resourceGroup, activationName, productName, apiVersion, (error, data, response) => {
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
 **resourceGroup** | **String**| The resource group the resource is located under. | 
 **activationName** | **String**| Name of the activation. | 
 **productName** | **String**| Name of the product. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-01-01&#39;]

### Return type

[**DownloadedProductsGet200Response**](DownloadedProductsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## downloadedProductsList

> DownloadedProductResourcesPage downloadedProductsList(subscriptionId, resourceGroup, activationName, apiVersion)



Get a list of downloaded products.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.DownloadedProductsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let activationName = "activationName_example"; // String | Name of the activation.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
apiInstance.downloadedProductsList(subscriptionId, resourceGroup, activationName, apiVersion, (error, data, response) => {
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
 **resourceGroup** | **String**| The resource group the resource is located under. | 
 **activationName** | **String**| Name of the activation. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-01-01&#39;]

### Return type

[**DownloadedProductResourcesPage**](DownloadedProductResourcesPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# AzureBridgeAdminClient.ProductsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsDownload**](ProductsApi.md#productsDownload) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/products/{productName}/download | 
[**productsGet**](ProductsApi.md#productsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/products/{productName} | 
[**productsList**](ProductsApi.md#productsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName}/products | 



## productsDownload

> ProductsDownload200Response productsDownload(subscriptionId, resourceGroup, activationName, productName, apiVersion)



Downloads a product from azure marketplace.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.ProductsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let activationName = "activationName_example"; // String | Name of the activation.
let productName = "productName_example"; // String | Name of the product.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
apiInstance.productsDownload(subscriptionId, resourceGroup, activationName, productName, apiVersion, (error, data, response) => {
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

[**ProductsDownload200Response**](ProductsDownload200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsGet

> ProductResource productsGet(subscriptionId, resourceGroup, activationName, productName, apiVersion)



Return product name.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.ProductsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let activationName = "activationName_example"; // String | Name of the activation.
let productName = "productName_example"; // String | Name of the product.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
apiInstance.productsGet(subscriptionId, resourceGroup, activationName, productName, apiVersion, (error, data, response) => {
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

[**ProductResource**](ProductResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsList

> ProductResourcesPage productsList(subscriptionId, resourceGroup, activationName, apiVersion)



Return product name.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.ProductsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let activationName = "activationName_example"; // String | Name of the activation.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
apiInstance.productsList(subscriptionId, resourceGroup, activationName, apiVersion, (error, data, response) => {
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

[**ProductResourcesPage**](ProductResourcesPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


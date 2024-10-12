# AzureStackAzureBridgeClient.ProductApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsGet**](ProductApi.md#productsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products/{productName} | 
[**productsGetProduct**](ProductApi.md#productsGetProduct) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products/{productName}/GetProduct | 
[**productsGetProducts**](ProductApi.md#productsGetProducts) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products/_all/GetProducts | 
[**productsList**](ProductApi.md#productsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products | 
[**productsListDetails**](ProductApi.md#productsListDetails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products/{productName}/listDetails | 
[**productsUploadLog**](ProductApi.md#productsUploadLog) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/products/{productName}/uploadProductLog | 



## productsGet

> Product productsGet(subscriptionId, resourceGroup, registrationName, productName, apiVersion)



Returns the specified product.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.ProductApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let productName = "productName_example"; // String | Name of the product.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
apiInstance.productsGet(subscriptionId, resourceGroup, registrationName, productName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **productName** | **String**| Name of the product. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

[**Product**](Product.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsGetProduct

> Product productsGetProduct(subscriptionId, resourceGroup, registrationName, productName, apiVersion, opts)



Returns the specified product.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.ProductApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let productName = "productName_example"; // String | Name of the product.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
let opts = {
  'deviceConfiguration': new AzureStackAzureBridgeClient.DeviceConfiguration() // DeviceConfiguration | Device configuration.
};
apiInstance.productsGetProduct(subscriptionId, resourceGroup, registrationName, productName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **productName** | **String**| Name of the product. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]
 **deviceConfiguration** | [**DeviceConfiguration**](DeviceConfiguration.md)| Device configuration. | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsGetProducts

> ProductList productsGetProducts(subscriptionId, resourceGroup, registrationName, apiVersion, opts)



Returns a list of products.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.ProductApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
let opts = {
  'deviceConfiguration': new AzureStackAzureBridgeClient.DeviceConfiguration() // DeviceConfiguration | Device configuration.
};
apiInstance.productsGetProducts(subscriptionId, resourceGroup, registrationName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]
 **deviceConfiguration** | [**DeviceConfiguration**](DeviceConfiguration.md)| Device configuration. | [optional] 

### Return type

[**ProductList**](ProductList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsList

> ProductList productsList(subscriptionId, resourceGroup, registrationName, apiVersion)



Returns a list of products.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.ProductApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
apiInstance.productsList(subscriptionId, resourceGroup, registrationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

[**ProductList**](ProductList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsListDetails

> ExtendedProduct productsListDetails(subscriptionId, resourceGroup, registrationName, productName, apiVersion)



Returns the extended properties of a product.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.ProductApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let productName = "productName_example"; // String | Name of the product.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
apiInstance.productsListDetails(subscriptionId, resourceGroup, registrationName, productName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **productName** | **String**| Name of the product. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

[**ExtendedProduct**](ExtendedProduct.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsUploadLog

> ProductLog productsUploadLog(subscriptionId, resourceGroup, registrationName, productName, apiVersion, opts)



Returns the specified product.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.ProductApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let productName = "productName_example"; // String | Name of the product.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
let opts = {
  'marketplaceProductLogUpdate': new AzureStackAzureBridgeClient.MarketplaceProductLogUpdate() // MarketplaceProductLogUpdate | Update details for product log.
};
apiInstance.productsUploadLog(subscriptionId, resourceGroup, registrationName, productName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **productName** | **String**| Name of the product. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]
 **marketplaceProductLogUpdate** | [**MarketplaceProductLogUpdate**](MarketplaceProductLogUpdate.md)| Update details for product log. | [optional] 

### Return type

[**ProductLog**](ProductLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


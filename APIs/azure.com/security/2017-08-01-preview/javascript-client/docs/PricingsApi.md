# SecurityCenter.PricingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pricingsCreateOrUpdateResourceGroupPricing**](PricingsApi.md#pricingsCreateOrUpdateResourceGroupPricing) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/pricings/{pricingName} | 
[**pricingsGetResourceGroupPricing**](PricingsApi.md#pricingsGetResourceGroupPricing) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/pricings/{pricingName} | 
[**pricingsGetSubscriptionPricing**](PricingsApi.md#pricingsGetSubscriptionPricing) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName} | 
[**pricingsList**](PricingsApi.md#pricingsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings | 
[**pricingsListByResourceGroup**](PricingsApi.md#pricingsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/pricings | 
[**pricingsUpdateSubscriptionPricing**](PricingsApi.md#pricingsUpdateSubscriptionPricing) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName} | 



## pricingsCreateOrUpdateResourceGroupPricing

> Pricing pricingsCreateOrUpdateResourceGroupPricing(apiVersion, subscriptionId, resourceGroupName, pricingName, pricing)



Security pricing configuration in the resource group

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.PricingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let pricingName = "pricingName_example"; // String | name of the pricing configuration
let pricing = new SecurityCenter.Pricing(); // Pricing | Pricing object
apiInstance.pricingsCreateOrUpdateResourceGroupPricing(apiVersion, subscriptionId, resourceGroupName, pricingName, pricing, (error, data, response) => {
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
 **pricingName** | **String**| name of the pricing configuration | 
 **pricing** | [**Pricing**](Pricing.md)| Pricing object | 

### Return type

[**Pricing**](Pricing.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pricingsGetResourceGroupPricing

> Pricing pricingsGetResourceGroupPricing(apiVersion, subscriptionId, resourceGroupName, pricingName)



Security pricing configuration in the resource group

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.PricingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let pricingName = "pricingName_example"; // String | name of the pricing configuration
apiInstance.pricingsGetResourceGroupPricing(apiVersion, subscriptionId, resourceGroupName, pricingName, (error, data, response) => {
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
 **pricingName** | **String**| name of the pricing configuration | 

### Return type

[**Pricing**](Pricing.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pricingsGetSubscriptionPricing

> Pricing pricingsGetSubscriptionPricing(apiVersion, subscriptionId, pricingName)



Security pricing configuration in the subscriptionSecurity pricing configuration in the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.PricingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let pricingName = "pricingName_example"; // String | name of the pricing configuration
apiInstance.pricingsGetSubscriptionPricing(apiVersion, subscriptionId, pricingName, (error, data, response) => {
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
 **pricingName** | **String**| name of the pricing configuration | 

### Return type

[**Pricing**](Pricing.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pricingsList

> PricingList pricingsList(apiVersion, subscriptionId)



Security pricing configurations in the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.PricingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.pricingsList(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**PricingList**](PricingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pricingsListByResourceGroup

> PricingList pricingsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Security pricing configurations in the resource group

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.PricingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
apiInstance.pricingsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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

### Return type

[**PricingList**](PricingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pricingsUpdateSubscriptionPricing

> Pricing pricingsUpdateSubscriptionPricing(apiVersion, subscriptionId, pricingName, pricing)



Security pricing configuration in the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.PricingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let pricingName = "pricingName_example"; // String | name of the pricing configuration
let pricing = new SecurityCenter.Pricing(); // Pricing | Pricing object
apiInstance.pricingsUpdateSubscriptionPricing(apiVersion, subscriptionId, pricingName, pricing, (error, data, response) => {
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
 **pricingName** | **String**| name of the pricing configuration | 
 **pricing** | [**Pricing**](Pricing.md)| Pricing object | 

### Return type

[**Pricing**](Pricing.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


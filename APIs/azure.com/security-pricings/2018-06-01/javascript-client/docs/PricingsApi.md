# SecurityCenter.PricingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pricingsGet**](PricingsApi.md#pricingsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName} | 
[**pricingsList**](PricingsApi.md#pricingsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings | 
[**pricingsUpdate**](PricingsApi.md#pricingsUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName} | 



## pricingsGet

> Pricing pricingsGet(apiVersion, subscriptionId, pricingName)



Gets a provided Security Center pricing configuration in the subscription.

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
apiInstance.pricingsGet(apiVersion, subscriptionId, pricingName, (error, data, response) => {
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



Lists Security Center pricing configurations in the subscription.

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


## pricingsUpdate

> Pricing pricingsUpdate(apiVersion, subscriptionId, pricingName, pricing)



Updates a provided Security Center pricing configuration in the subscription.

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
apiInstance.pricingsUpdate(apiVersion, subscriptionId, pricingName, pricing, (error, data, response) => {
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


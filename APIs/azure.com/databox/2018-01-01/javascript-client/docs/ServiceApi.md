# DataBoxManagementClient.ServiceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceListAvailableSkus**](ServiceApi.md#serviceListAvailableSkus) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/availableSkus | 
[**serviceValidateAddress**](ServiceApi.md#serviceValidateAddress) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/validateAddress | 



## serviceListAvailableSkus

> AvailableSkusResult serviceListAvailableSkus(subscriptionId, location, apiVersion, availableSkuRequest)



This method provides the list of available skus for the given subscription and location.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let location = "location_example"; // String | The location of the resource
let apiVersion = "apiVersion_example"; // String | The API Version
let availableSkuRequest = new DataBoxManagementClient.AvailableSkuRequest(); // AvailableSkuRequest | Filters for showing the available skus.
apiInstance.serviceListAvailableSkus(subscriptionId, location, apiVersion, availableSkuRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **location** | **String**| The location of the resource | 
 **apiVersion** | **String**| The API Version | 
 **availableSkuRequest** | [**AvailableSkuRequest**](AvailableSkuRequest.md)| Filters for showing the available skus. | 

### Return type

[**AvailableSkusResult**](AvailableSkusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serviceValidateAddress

> AddressValidationOutput serviceValidateAddress(subscriptionId, location, apiVersion, validateAddress)



This method validates the customer shipping address and provide alternate addresses if any.

### Example

```javascript
import DataBoxManagementClient from 'data_box_management_client';
let defaultClient = DataBoxManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxManagementClient.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let location = "location_example"; // String | The location of the resource
let apiVersion = "apiVersion_example"; // String | The API Version
let validateAddress = new DataBoxManagementClient.ValidateAddress(); // ValidateAddress | Shipping address of the customer.
apiInstance.serviceValidateAddress(subscriptionId, location, apiVersion, validateAddress, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **location** | **String**| The location of the resource | 
 **apiVersion** | **String**| The API Version | 
 **validateAddress** | [**ValidateAddress**](ValidateAddress.md)| Shipping address of the customer. | 

### Return type

[**AddressValidationOutput**](AddressValidationOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


# BillingManagementClient.AddressApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addressValidate**](AddressApi.md#addressValidate) | **POST** /providers/Microsoft.Billing/validateAddress | 



## addressValidate

> ValidateAddressResponse addressValidate(apiVersion, address)



Validates the address.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.AddressApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let address = new BillingManagementClient.AddressDetails(); // AddressDetails | 
apiInstance.addressValidate(apiVersion, address, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **address** | [**AddressDetails**](AddressDetails.md)|  | 

### Return type

[**ValidateAddressResponse**](ValidateAddressResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


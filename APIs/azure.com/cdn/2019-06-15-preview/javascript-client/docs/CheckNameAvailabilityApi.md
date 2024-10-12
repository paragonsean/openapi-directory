# CdnManagementClient.CheckNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkNameAvailability**](CheckNameAvailabilityApi.md#checkNameAvailability) | **POST** /providers/Microsoft.Cdn/checkNameAvailability | 



## checkNameAvailability

> CheckNameAvailabilityOutput checkNameAvailability(apiVersion, checkNameAvailabilityInput)



Check the availability of a resource name. This is needed for resources where name is globally unique, such as a CDN endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.CheckNameAvailabilityApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let checkNameAvailabilityInput = new CdnManagementClient.CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check.
apiInstance.checkNameAvailability(apiVersion, checkNameAvailabilityInput, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **checkNameAvailabilityInput** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Input to check. | 

### Return type

[**CheckNameAvailabilityOutput**](CheckNameAvailabilityOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


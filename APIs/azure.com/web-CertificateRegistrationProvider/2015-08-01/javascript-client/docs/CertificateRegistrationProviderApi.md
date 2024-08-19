# CertificateRegistrationProviderApiClient.CertificateRegistrationProviderApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificateRegistrationProviderListOperations**](CertificateRegistrationProviderApi.md#certificateRegistrationProviderListOperations) | **GET** /providers/Microsoft.CertificateRegistration/operations | Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider



## certificateRegistrationProviderListOperations

> CertificateRegistrationProviderListOperations200Response certificateRegistrationProviderListOperations(apiVersion)

Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider

Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider

### Example

```javascript
import CertificateRegistrationProviderApiClient from 'certificate_registration_provider_api_client';
let defaultClient = CertificateRegistrationProviderApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CertificateRegistrationProviderApiClient.CertificateRegistrationProviderApi();
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateRegistrationProviderListOperations(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| API Version | 

### Return type

[**CertificateRegistrationProviderListOperations200Response**](CertificateRegistrationProviderListOperations200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


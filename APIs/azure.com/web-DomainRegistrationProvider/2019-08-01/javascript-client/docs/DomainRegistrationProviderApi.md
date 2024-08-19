# DomainRegistrationProviderApiClient.DomainRegistrationProviderApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainRegistrationProviderListOperations**](DomainRegistrationProviderApi.md#domainRegistrationProviderListOperations) | **GET** /providers/Microsoft.DomainRegistration/operations | Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider



## domainRegistrationProviderListOperations

> DomainRegistrationProviderListOperations200Response domainRegistrationProviderListOperations(apiVersion)

Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider

Description for Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider

### Example

```javascript
import DomainRegistrationProviderApiClient from 'domain_registration_provider_api_client';
let defaultClient = DomainRegistrationProviderApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DomainRegistrationProviderApiClient.DomainRegistrationProviderApi();
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.domainRegistrationProviderListOperations(apiVersion, (error, data, response) => {
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

[**DomainRegistrationProviderListOperations200Response**](DomainRegistrationProviderListOperations200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# ManagedServicesClient.MarketplaceRegistrationDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketplaceRegistrationDefinitionsGet**](MarketplaceRegistrationDefinitionsApi.md#marketplaceRegistrationDefinitionsGet) | **GET** /{scope}/providers/Microsoft.ManagedServices/marketplaceRegistrationDefinitions/{marketplaceIdentifier} | 
[**marketplaceRegistrationDefinitionsList**](MarketplaceRegistrationDefinitionsApi.md#marketplaceRegistrationDefinitionsList) | **GET** /{scope}/providers/Microsoft.ManagedServices/marketplaceRegistrationDefinitions | 



## marketplaceRegistrationDefinitionsGet

> RegistrationDefinition marketplaceRegistrationDefinitionsGet(scope, marketplaceIdentifier, apiVersion)



Get the marketplace registration definition for the marketplace identifier.

### Example

```javascript
import ManagedServicesClient from 'managed_services_client';
let defaultClient = ManagedServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServicesClient.MarketplaceRegistrationDefinitionsApi();
let scope = "scope_example"; // String | Scope of the resource.
let marketplaceIdentifier = "marketplaceIdentifier_example"; // String | Market place identifer. Expected Formats - {publisher}.{product[-preview]}.{planName}.{version} or {publisher}.{product[-preview]}.{planName} or {publisher}.{product[-preview]} or {publisher}).
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.marketplaceRegistrationDefinitionsGet(scope, marketplaceIdentifier, apiVersion, (error, data, response) => {
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
 **scope** | **String**| Scope of the resource. | 
 **marketplaceIdentifier** | **String**| Market place identifer. Expected Formats - {publisher}.{product[-preview]}.{planName}.{version} or {publisher}.{product[-preview]}.{planName} or {publisher}.{product[-preview]} or {publisher}). | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**RegistrationDefinition**](RegistrationDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketplaceRegistrationDefinitionsList

> MarketplaceRegistrationDefinitionList marketplaceRegistrationDefinitionsList(scope, apiVersion, opts)



Gets a list of the marketplace registration definitions for the marketplace identifier.

### Example

```javascript
import ManagedServicesClient from 'managed_services_client';
let defaultClient = ManagedServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServicesClient.MarketplaceRegistrationDefinitionsApi();
let scope = "scope_example"; // String | Scope of the resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'filter': "filter_example" // String | The filter query parameter. Might be used to filter marketplace registration definition by plan identifier, publisher, version etc.
};
apiInstance.marketplaceRegistrationDefinitionsList(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| Scope of the resource. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **filter** | **String**| The filter query parameter. Might be used to filter marketplace registration definition by plan identifier, publisher, version etc. | [optional] 

### Return type

[**MarketplaceRegistrationDefinitionList**](MarketplaceRegistrationDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


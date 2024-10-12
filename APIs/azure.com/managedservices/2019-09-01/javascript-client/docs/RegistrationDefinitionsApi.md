# ManagedServicesClient.RegistrationDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registrationDefinitionsCreateOrUpdate**](RegistrationDefinitionsApi.md#registrationDefinitionsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.ManagedServices/registrationDefinitions/{registrationDefinitionId} | 
[**registrationDefinitionsDelete**](RegistrationDefinitionsApi.md#registrationDefinitionsDelete) | **DELETE** /{scope}/providers/Microsoft.ManagedServices/registrationDefinitions/{registrationDefinitionId} | 
[**registrationDefinitionsGet**](RegistrationDefinitionsApi.md#registrationDefinitionsGet) | **GET** /{scope}/providers/Microsoft.ManagedServices/registrationDefinitions/{registrationDefinitionId} | 
[**registrationDefinitionsList**](RegistrationDefinitionsApi.md#registrationDefinitionsList) | **GET** /{scope}/providers/Microsoft.ManagedServices/registrationDefinitions | 



## registrationDefinitionsCreateOrUpdate

> RegistrationDefinition registrationDefinitionsCreateOrUpdate(registrationDefinitionId, apiVersion, scope, requestBody)



Creates or updates a registration definition.

### Example

```javascript
import ManagedServicesClient from 'managed_services_client';
let defaultClient = ManagedServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServicesClient.RegistrationDefinitionsApi();
let registrationDefinitionId = "registrationDefinitionId_example"; // String | Guid of the registration definition.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scope = "scope_example"; // String | Scope of the resource.
let requestBody = new ManagedServicesClient.RegistrationDefinition(); // RegistrationDefinition | The parameters required to create new registration definition.
apiInstance.registrationDefinitionsCreateOrUpdate(registrationDefinitionId, apiVersion, scope, requestBody, (error, data, response) => {
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
 **registrationDefinitionId** | **String**| Guid of the registration definition. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **scope** | **String**| Scope of the resource. | 
 **requestBody** | [**RegistrationDefinition**](RegistrationDefinition.md)| The parameters required to create new registration definition. | 

### Return type

[**RegistrationDefinition**](RegistrationDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registrationDefinitionsDelete

> registrationDefinitionsDelete(registrationDefinitionId, apiVersion, scope)



Deletes the registration definition.

### Example

```javascript
import ManagedServicesClient from 'managed_services_client';
let defaultClient = ManagedServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServicesClient.RegistrationDefinitionsApi();
let registrationDefinitionId = "registrationDefinitionId_example"; // String | Guid of the registration definition.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scope = "scope_example"; // String | Scope of the resource.
apiInstance.registrationDefinitionsDelete(registrationDefinitionId, apiVersion, scope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registrationDefinitionId** | **String**| Guid of the registration definition. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **scope** | **String**| Scope of the resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registrationDefinitionsGet

> RegistrationDefinition registrationDefinitionsGet(scope, registrationDefinitionId, apiVersion)



Gets the registration definition details.

### Example

```javascript
import ManagedServicesClient from 'managed_services_client';
let defaultClient = ManagedServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServicesClient.RegistrationDefinitionsApi();
let scope = "scope_example"; // String | Scope of the resource.
let registrationDefinitionId = "registrationDefinitionId_example"; // String | Guid of the registration definition.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.registrationDefinitionsGet(scope, registrationDefinitionId, apiVersion, (error, data, response) => {
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
 **registrationDefinitionId** | **String**| Guid of the registration definition. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**RegistrationDefinition**](RegistrationDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registrationDefinitionsList

> RegistrationDefinitionList registrationDefinitionsList(scope, apiVersion)



Gets a list of the registration definitions.

### Example

```javascript
import ManagedServicesClient from 'managed_services_client';
let defaultClient = ManagedServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServicesClient.RegistrationDefinitionsApi();
let scope = "scope_example"; // String | Scope of the resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.registrationDefinitionsList(scope, apiVersion, (error, data, response) => {
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

### Return type

[**RegistrationDefinitionList**](RegistrationDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


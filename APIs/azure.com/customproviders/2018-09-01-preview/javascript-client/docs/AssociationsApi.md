# Customproviders.AssociationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associationsCreateOrUpdate**](AssociationsApi.md#associationsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.CustomProviders/associations/{associationName} | 
[**associationsDelete**](AssociationsApi.md#associationsDelete) | **DELETE** /{scope}/providers/Microsoft.CustomProviders/associations/{associationName} | 
[**associationsGet**](AssociationsApi.md#associationsGet) | **GET** /{scope}/providers/Microsoft.CustomProviders/associations/{associationName} | 
[**associationsListAll**](AssociationsApi.md#associationsListAll) | **GET** /{scope}/providers/Microsoft.CustomProviders/associations | 



## associationsCreateOrUpdate

> Association associationsCreateOrUpdate(scope, associationName, apiVersion, association)



Create or update an association.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.AssociationsApi();
let scope = "scope_example"; // String | The scope of the association. The scope can be any valid REST resource instance. For example, use '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}' for a virtual machine resource.
let associationName = "associationName_example"; // String | The name of the association.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let association = new Customproviders.Association(); // Association | The parameters required to create or update an association.
apiInstance.associationsCreateOrUpdate(scope, associationName, apiVersion, association, (error, data, response) => {
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
 **scope** | **String**| The scope of the association. The scope can be any valid REST resource instance. For example, use &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}&#39; for a virtual machine resource. | 
 **associationName** | **String**| The name of the association. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **association** | [**Association**](Association.md)| The parameters required to create or update an association. | 

### Return type

[**Association**](Association.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associationsDelete

> associationsDelete(scope, associationName, apiVersion)



Delete an association.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.AssociationsApi();
let scope = "scope_example"; // String | The scope of the association.
let associationName = "associationName_example"; // String | The name of the association.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.associationsDelete(scope, associationName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the association. | 
 **associationName** | **String**| The name of the association. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## associationsGet

> Association associationsGet(scope, associationName, apiVersion)



Get an association.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.AssociationsApi();
let scope = "scope_example"; // String | The scope of the association.
let associationName = "associationName_example"; // String | The name of the association.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.associationsGet(scope, associationName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the association. | 
 **associationName** | **String**| The name of the association. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

[**Association**](Association.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## associationsListAll

> AssociationsList associationsListAll(scope, apiVersion)



Gets all association for the given scope.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.AssociationsApi();
let scope = "scope_example"; // String | The scope of the association.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.associationsListAll(scope, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope of the association. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

[**AssociationsList**](AssociationsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


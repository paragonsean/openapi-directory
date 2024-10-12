# ServiceFabricClientApis.MeshSecretsApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meshSecretCreateOrUpdate**](MeshSecretsApi.md#meshSecretCreateOrUpdate) | **PUT** /Resources/Secrets/{secretResourceName} | Creates or updates a Secret resource.
[**meshSecretDelete**](MeshSecretsApi.md#meshSecretDelete) | **DELETE** /Resources/Secrets/{secretResourceName} | Deletes the Secret resource.
[**meshSecretGet**](MeshSecretsApi.md#meshSecretGet) | **GET** /Resources/Secrets/{secretResourceName} | Gets the Secret resource with the given name.
[**meshSecretList**](MeshSecretsApi.md#meshSecretList) | **GET** /Resources/Secrets | Lists all the secret resources.



## meshSecretCreateOrUpdate

> SecretResourceDescription meshSecretCreateOrUpdate(apiVersion, secretResourceName, secretResourceDescription)

Creates or updates a Secret resource.

Creates a Secret resource with the specified name, description and properties. If Secret resource with the same name exists, then it is updated with the specified description and properties. Once created, the kind and contentType of a secret resource cannot be updated.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshSecretsApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
let secretResourceDescription = new ServiceFabricClientApis.SecretResourceDescription(); // SecretResourceDescription | Description for creating a secret resource.
apiInstance.meshSecretCreateOrUpdate(apiVersion, secretResourceName, secretResourceDescription, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **secretResourceName** | **String**| The name of the secret resource. | 
 **secretResourceDescription** | [**SecretResourceDescription**](SecretResourceDescription.md)| Description for creating a secret resource. | 

### Return type

[**SecretResourceDescription**](SecretResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshSecretDelete

> meshSecretDelete(apiVersion, secretResourceName)

Deletes the Secret resource.

Deletes the specified Secret resource and all of its named values.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshSecretsApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
apiInstance.meshSecretDelete(apiVersion, secretResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **secretResourceName** | **String**| The name of the secret resource. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshSecretGet

> SecretResourceDescription meshSecretGet(apiVersion, secretResourceName)

Gets the Secret resource with the given name.

Gets the information about the Secret resource with the given name. The information include the description and other properties of the Secret.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshSecretsApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
apiInstance.meshSecretGet(apiVersion, secretResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **secretResourceName** | **String**| The name of the secret resource. | 

### Return type

[**SecretResourceDescription**](SecretResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshSecretList

> PagedSecretResourceDescriptionList meshSecretList(apiVersion)

Lists all the secret resources.

Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshSecretsApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
apiInstance.meshSecretList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]

### Return type

[**PagedSecretResourceDescriptionList**](PagedSecretResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


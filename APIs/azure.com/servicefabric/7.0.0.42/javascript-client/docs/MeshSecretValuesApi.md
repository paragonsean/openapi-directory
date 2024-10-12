# ServiceFabricClientApis.MeshSecretValuesApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meshSecretValueAddValue**](MeshSecretValuesApi.md#meshSecretValueAddValue) | **PUT** /Resources/Secrets/{secretResourceName}/values/{secretValueResourceName} | Adds the specified value as a new version of the specified secret resource.
[**meshSecretValueDelete**](MeshSecretValuesApi.md#meshSecretValueDelete) | **DELETE** /Resources/Secrets/{secretResourceName}/values/{secretValueResourceName} | Deletes the specified  value of the named secret resource.
[**meshSecretValueGet**](MeshSecretValuesApi.md#meshSecretValueGet) | **GET** /Resources/Secrets/{secretResourceName}/values/{secretValueResourceName} | Gets the specified secret value resource.
[**meshSecretValueList**](MeshSecretValuesApi.md#meshSecretValueList) | **GET** /Resources/Secrets/{secretResourceName}/values | List names of all values of the specified secret resource.
[**meshSecretValueShow**](MeshSecretValuesApi.md#meshSecretValueShow) | **POST** /Resources/Secrets/{secretResourceName}/values/{secretValueResourceName}/list_value | Lists the specified value of the secret resource.



## meshSecretValueAddValue

> SecretValueResourceDescription meshSecretValueAddValue(apiVersion, secretResourceName, secretValueResourceName, secretValueResourceDescription)

Adds the specified value as a new version of the specified secret resource.

Creates a new value of the specified secret resource. The name of the value is typically the version identifier. Once created the value cannot be changed.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshSecretValuesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
let secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
let secretValueResourceDescription = new ServiceFabricClientApis.SecretValueResourceDescription(); // SecretValueResourceDescription | Description for creating a value of a secret resource.
apiInstance.meshSecretValueAddValue(apiVersion, secretResourceName, secretValueResourceName, secretValueResourceDescription, (error, data, response) => {
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
 **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | 
 **secretValueResourceDescription** | [**SecretValueResourceDescription**](SecretValueResourceDescription.md)| Description for creating a value of a secret resource. | 

### Return type

[**SecretValueResourceDescription**](SecretValueResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshSecretValueDelete

> meshSecretValueDelete(apiVersion, secretResourceName, secretValueResourceName)

Deletes the specified  value of the named secret resource.

Deletes the secret value resource identified by the name. The name of the resource is typically the version associated with that value. Deletion will fail if the specified value is in use.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshSecretValuesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
let secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
apiInstance.meshSecretValueDelete(apiVersion, secretResourceName, secretValueResourceName, (error, data, response) => {
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
 **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshSecretValueGet

> SecretValueResourceDescription meshSecretValueGet(apiVersion, secretResourceName, secretValueResourceName)

Gets the specified secret value resource.

Get the information about the specified named secret value resources. The information does not include the actual value of the secret.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshSecretValuesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
let secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
apiInstance.meshSecretValueGet(apiVersion, secretResourceName, secretValueResourceName, (error, data, response) => {
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
 **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | 

### Return type

[**SecretValueResourceDescription**](SecretValueResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshSecretValueList

> PagedSecretValueResourceDescriptionList meshSecretValueList(apiVersion, secretResourceName)

List names of all values of the specified secret resource.

Gets information about all secret value resources of the specified secret resource. The information includes the names of the secret value resources, but not the actual values.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshSecretValuesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
apiInstance.meshSecretValueList(apiVersion, secretResourceName, (error, data, response) => {
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

[**PagedSecretValueResourceDescriptionList**](PagedSecretValueResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshSecretValueShow

> SecretValue meshSecretValueShow(apiVersion, secretResourceName, secretValueResourceName)

Lists the specified value of the secret resource.

Lists the decrypted value of the specified named value of the secret resource. This is a privileged operation.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshSecretValuesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
let secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
apiInstance.meshSecretValueShow(apiVersion, secretResourceName, secretValueResourceName, (error, data, response) => {
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
 **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | 

### Return type

[**SecretValue**](SecretValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


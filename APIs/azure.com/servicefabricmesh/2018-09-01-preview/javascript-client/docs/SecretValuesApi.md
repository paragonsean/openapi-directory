# SeaBreezeManagementClient.SecretValuesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secretValueCreate**](SecretValuesApi.md#secretValueCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName}/values/{secretValueResourceName} | Adds the specified value as a new version of the specified secret resource.
[**secretValueDelete**](SecretValuesApi.md#secretValueDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName}/values/{secretValueResourceName} | Deletes the specified  value of the named secret resource.
[**secretValueGet**](SecretValuesApi.md#secretValueGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName}/values/{secretValueResourceName} | Gets the specified secret value resource.
[**secretValueList**](SecretValuesApi.md#secretValueList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName}/values | List names of all values of the specified secret resource.
[**secretValueListValue**](SecretValuesApi.md#secretValueListValue) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName}/values/{secretValueResourceName}/list_value | Lists the specified value of the secret resource.



## secretValueCreate

> SecretValueResourceDescription secretValueCreate(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName, secretValueResourceDescription)

Adds the specified value as a new version of the specified secret resource.

Creates a new value of the specified secret resource. The name of the value is typically the version identifier. Once created the value cannot be changed.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.SecretValuesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
let secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
let secretValueResourceDescription = new SeaBreezeManagementClient.SecretValueResourceDescription(); // SecretValueResourceDescription | Description for creating a value of a secret resource.
apiInstance.secretValueCreate(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName, secretValueResourceDescription, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **secretResourceName** | **String**| The name of the secret resource. | 
 **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | 
 **secretValueResourceDescription** | [**SecretValueResourceDescription**](SecretValueResourceDescription.md)| Description for creating a value of a secret resource. | 

### Return type

[**SecretValueResourceDescription**](SecretValueResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## secretValueDelete

> secretValueDelete(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName)

Deletes the specified  value of the named secret resource.

Deletes the secret value resource identified by the name. The name of the resource is typically the version associated with that value. Deletion will fail if the specified value is in use.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.SecretValuesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
let secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
apiInstance.secretValueDelete(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **secretResourceName** | **String**| The name of the secret resource. | 
 **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretValueGet

> SecretValueResourceDescription secretValueGet(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName)

Gets the specified secret value resource.

Get the information about the specified named secret value resources. The information does not include the actual value of the secret.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.SecretValuesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
let secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
apiInstance.secretValueGet(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **secretResourceName** | **String**| The name of the secret resource. | 
 **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | 

### Return type

[**SecretValueResourceDescription**](SecretValueResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretValueList

> SecretValueResourceDescriptionList secretValueList(subscriptionId, apiVersion, resourceGroupName, secretResourceName)

List names of all values of the specified secret resource.

Gets information about all secret value resources of the specified secret resource. The information includes the names of the secret value resources, but not the actual values.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.SecretValuesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
apiInstance.secretValueList(subscriptionId, apiVersion, resourceGroupName, secretResourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **secretResourceName** | **String**| The name of the secret resource. | 

### Return type

[**SecretValueResourceDescriptionList**](SecretValueResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretValueListValue

> SecretValue secretValueListValue(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName)

Lists the specified value of the secret resource.

Lists the decrypted value of the specified named value of the secret resource. This is a privileged operation.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.SecretValuesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
let secretValueResourceName = "secretValueResourceName_example"; // String | The name of the secret resource value which is typically the version identifier for the value.
apiInstance.secretValueListValue(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretValueResourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **secretResourceName** | **String**| The name of the secret resource. | 
 **secretValueResourceName** | **String**| The name of the secret resource value which is typically the version identifier for the value. | 

### Return type

[**SecretValue**](SecretValue.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


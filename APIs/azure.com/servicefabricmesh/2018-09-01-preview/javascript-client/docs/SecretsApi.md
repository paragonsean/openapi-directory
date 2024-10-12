# SeaBreezeManagementClient.SecretsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secretCreate**](SecretsApi.md#secretCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName} | Creates or updates a secret resource.
[**secretDelete**](SecretsApi.md#secretDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName} | Deletes the secret resource.
[**secretGet**](SecretsApi.md#secretGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets/{secretResourceName} | Gets the secret resource with the given name.
[**secretListByResourceGroup**](SecretsApi.md#secretListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/secrets | Gets all the secret resources in a given resource group.
[**secretListBySubscription**](SecretsApi.md#secretListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabricMesh/secrets | Gets all the secret resources in a given subscription.



## secretCreate

> SecretResourceDescription secretCreate(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretResourceDescription)

Creates or updates a secret resource.

Creates a secret resource with the specified name, description and properties. If a secret resource with the same name exists, then it is updated with the specified description and properties.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.SecretsApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
let secretResourceDescription = new SeaBreezeManagementClient.SecretResourceDescription(); // SecretResourceDescription | Description for creating a secret resource.
apiInstance.secretCreate(subscriptionId, apiVersion, resourceGroupName, secretResourceName, secretResourceDescription, (error, data, response) => {
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
 **secretResourceDescription** | [**SecretResourceDescription**](SecretResourceDescription.md)| Description for creating a secret resource. | 

### Return type

[**SecretResourceDescription**](SecretResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## secretDelete

> secretDelete(subscriptionId, apiVersion, resourceGroupName, secretResourceName)

Deletes the secret resource.

Deletes the secret resource identified by the name.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.SecretsApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
apiInstance.secretDelete(subscriptionId, apiVersion, resourceGroupName, secretResourceName, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretGet

> SecretResourceDescription secretGet(subscriptionId, apiVersion, resourceGroupName, secretResourceName)

Gets the secret resource with the given name.

Gets the information about the secret resource with the given name. The information include the description and other properties of the secret.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.SecretsApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let secretResourceName = "secretResourceName_example"; // String | The name of the secret resource.
apiInstance.secretGet(subscriptionId, apiVersion, resourceGroupName, secretResourceName, (error, data, response) => {
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

[**SecretResourceDescription**](SecretResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretListByResourceGroup

> SecretResourceDescriptionList secretListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)

Gets all the secret resources in a given resource group.

Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.SecretsApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
apiInstance.secretListByResourceGroup(subscriptionId, apiVersion, resourceGroupName, (error, data, response) => {
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

### Return type

[**SecretResourceDescriptionList**](SecretResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretListBySubscription

> SecretResourceDescriptionList secretListBySubscription(subscriptionId, apiVersion)

Gets all the secret resources in a given subscription.

Gets the information about all secret resources in a given resource group. The information include the description and other properties of the secret.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.SecretsApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
apiInstance.secretListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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

### Return type

[**SecretResourceDescriptionList**](SecretResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


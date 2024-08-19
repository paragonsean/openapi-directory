# DeploymentAdminClient.ProductSecretsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productSecretsGet**](ProductSecretsApi.md#productSecretsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productSecrets/{productId}/secrets/{secretName} | 
[**productSecretsImport**](ProductSecretsApi.md#productSecretsImport) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productSecrets/{productId}/secrets/{secretName}/import | 
[**productSecretsList**](ProductSecretsApi.md#productSecretsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productPackages/{productId}/secrets | 
[**productSecretsValidate**](ProductSecretsApi.md#productSecretsValidate) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productSecrets/{productId}/secrets/{secretName}/validate | 



## productSecretsGet

> ProductSecret productSecretsGet(subscriptionId, productId, apiVersion, secretName)



Retrieves the specific product secret details.

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductSecretsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | The product identifier.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
let secretName = "secretName_example"; // String | The secret name.
apiInstance.productSecretsGet(subscriptionId, productId, apiVersion, secretName, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **productId** | **String**| The product identifier. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]
 **secretName** | **String**| The secret name. | 

### Return type

[**ProductSecret**](ProductSecret.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productSecretsImport

> productSecretsImport(subscriptionId, productId, secretName, apiVersion, secretParameters)



Imports a product secret.

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductSecretsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | The product identifier.
let secretName = "secretName_example"; // String | The secret name.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
let secretParameters = new DeploymentAdminClient.SecretParameters(); // SecretParameters | The parameters required for creating/updating a product secret.
apiInstance.productSecretsImport(subscriptionId, productId, secretName, apiVersion, secretParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **productId** | **String**| The product identifier. | 
 **secretName** | **String**| The secret name. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]
 **secretParameters** | [**SecretParameters**](SecretParameters.md)| The parameters required for creating/updating a product secret. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productSecretsList

> ProductSecretsList productSecretsList(subscriptionId, apiVersion, productId)



Returns an array of product secrets.

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductSecretsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
let productId = "productId_example"; // String | The product identifier.
apiInstance.productSecretsList(subscriptionId, apiVersion, productId, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]
 **productId** | **String**| The product identifier. | 

### Return type

[**ProductSecretsList**](ProductSecretsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productSecretsValidate

> productSecretsValidate(subscriptionId, productId, secretName, apiVersion, secretParameters)



Validates a product secret.

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductSecretsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | The product identifier.
let secretName = "secretName_example"; // String | The secret name.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
let secretParameters = new DeploymentAdminClient.SecretParameters(); // SecretParameters | The parameters required for creating/updating a product secret.
apiInstance.productSecretsValidate(subscriptionId, productId, secretName, apiVersion, secretParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **productId** | **String**| The product identifier. | 
 **secretName** | **String**| The secret name. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]
 **secretParameters** | [**SecretParameters**](SecretParameters.md)| The parameters required for creating/updating a product secret. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


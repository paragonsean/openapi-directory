# DeploymentAdminClient.ProductDeploymentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productDeploymentsBootStrap**](ProductDeploymentsApi.md#productDeploymentsBootStrap) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/bootstrap | 
[**productDeploymentsDeploy**](ProductDeploymentsApi.md#productDeploymentsDeploy) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/deploy | 
[**productDeploymentsGet**](ProductDeploymentsApi.md#productDeploymentsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId} | 
[**productDeploymentsList**](ProductDeploymentsApi.md#productDeploymentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments | 
[**productDeploymentsLock**](ProductDeploymentsApi.md#productDeploymentsLock) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/lock | 
[**productDeploymentsRemove**](ProductDeploymentsApi.md#productDeploymentsRemove) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/remove | 
[**productDeploymentsRotateSecrets**](ProductDeploymentsApi.md#productDeploymentsRotateSecrets) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/rotateSecrets | 
[**productDeploymentsUnlock**](ProductDeploymentsApi.md#productDeploymentsUnlock) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/unlock | 



## productDeploymentsBootStrap

> productDeploymentsBootStrap(subscriptionId, productId, apiVersion, bootstrapActionParameter)



Invokes bootstrap action on the product deployment

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductDeploymentsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | The product identifier.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
let bootstrapActionParameter = new DeploymentAdminClient.ProductDeploymentsBootStrapRequest(); // ProductDeploymentsBootStrapRequest | Represents bootstrap action parameter
apiInstance.productDeploymentsBootStrap(subscriptionId, productId, apiVersion, bootstrapActionParameter, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]
 **bootstrapActionParameter** | [**ProductDeploymentsBootStrapRequest**](ProductDeploymentsBootStrapRequest.md)| Represents bootstrap action parameter | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productDeploymentsDeploy

> productDeploymentsDeploy(subscriptionId, productId, apiVersion, deployActionParameter)



Invokes deploy action on the product

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductDeploymentsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | The product identifier.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
let deployActionParameter = new DeploymentAdminClient.ProductDeploymentsDeployRequest(); // ProductDeploymentsDeployRequest | Represents bootstrap action parameter
apiInstance.productDeploymentsDeploy(subscriptionId, productId, apiVersion, deployActionParameter, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]
 **deployActionParameter** | [**ProductDeploymentsDeployRequest**](ProductDeploymentsDeployRequest.md)| Represents bootstrap action parameter | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productDeploymentsGet

> ProductDeploymentResourceEntity productDeploymentsGet(subscriptionId, apiVersion, productId)



Invokes bootstrap action on the product deployment

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductDeploymentsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
let productId = "productId_example"; // String | The product identifier.
apiInstance.productDeploymentsGet(subscriptionId, apiVersion, productId, (error, data, response) => {
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

[**ProductDeploymentResourceEntity**](ProductDeploymentResourceEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productDeploymentsList

> ProductDeploymentsList productDeploymentsList(subscriptionId, apiVersion)



Invokes bootstrap action on the product deployment

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductDeploymentsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.productDeploymentsList(subscriptionId, apiVersion, (error, data, response) => {
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

### Return type

[**ProductDeploymentsList**](ProductDeploymentsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productDeploymentsLock

> productDeploymentsLock(subscriptionId, productId, apiVersion)



locks the product subscription

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductDeploymentsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | The product identifier.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.productDeploymentsLock(subscriptionId, productId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productDeploymentsRemove

> productDeploymentsRemove(subscriptionId, productId, apiVersion)



Invokes remove action on the product deployment

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductDeploymentsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | The product identifier.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.productDeploymentsRemove(subscriptionId, productId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productDeploymentsRotateSecrets

> productDeploymentsRotateSecrets(subscriptionId, productId, apiVersion)



Invokes rotate secrets action on the product deployment

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductDeploymentsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | The product identifier.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.productDeploymentsRotateSecrets(subscriptionId, productId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productDeploymentsUnlock

> productDeploymentsUnlock(subscriptionId, productId, apiVersion, unlockActionParameter)



Unlocks the product subscription

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ProductDeploymentsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let productId = "productId_example"; // String | The product identifier.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
let unlockActionParameter = new DeploymentAdminClient.ProductDeploymentsUnlockRequest(); // ProductDeploymentsUnlockRequest | Represents bootstrap action parameter
apiInstance.productDeploymentsUnlock(subscriptionId, productId, apiVersion, unlockActionParameter, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]
 **unlockActionParameter** | [**ProductDeploymentsUnlockRequest**](ProductDeploymentsUnlockRequest.md)| Represents bootstrap action parameter | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


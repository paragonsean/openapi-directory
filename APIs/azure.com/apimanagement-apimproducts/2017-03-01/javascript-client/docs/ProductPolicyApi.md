# ApiManagementClient.ProductPolicyApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productPolicyCreateOrUpdate**](ProductPolicyApi.md#productPolicyCreateOrUpdate) | **PUT** /products/{productId}/policies/{policyId} | 
[**productPolicyDelete**](ProductPolicyApi.md#productPolicyDelete) | **DELETE** /products/{productId}/policies/{policyId} | 
[**productPolicyGet**](ProductPolicyApi.md#productPolicyGet) | **GET** /products/{productId}/policies/{policyId} | 
[**productPolicyListByProduct**](ProductPolicyApi.md#productPolicyListByProduct) | **GET** /products/{productId}/policies | 



## productPolicyCreateOrUpdate

> ProductPolicyListByProduct200ResponseValueInner productPolicyCreateOrUpdate(productId, policyId, apiVersion, parameters)



Creates or updates policy configuration for the Product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.ProductPolicyApi();
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new ApiManagementClient.ProductPolicyListByProduct200ResponseValueInner(); // ProductPolicyListByProduct200ResponseValueInner | The policy contents to apply.
apiInstance.productPolicyCreateOrUpdate(productId, policyId, apiVersion, parameters, (error, data, response) => {
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
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **policyId** | **String**| The identifier of the Policy. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**ProductPolicyListByProduct200ResponseValueInner**](ProductPolicyListByProduct200ResponseValueInner.md)| The policy contents to apply. | 

### Return type

[**ProductPolicyListByProduct200ResponseValueInner**](ProductPolicyListByProduct200ResponseValueInner.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/vnd.ms-azure-apim.policy+xml, application/vnd.ms-azure-apim.policy.raw+xml
- **Accept**: application/json


## productPolicyDelete

> productPolicyDelete(productId, policyId, ifMatch, apiVersion)



Deletes the policy configuration at the Product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.ProductPolicyApi();
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
let ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the product policy to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.productPolicyDelete(productId, policyId, ifMatch, apiVersion, (error, data, response) => {
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
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **policyId** | **String**| The identifier of the Policy. | 
 **ifMatch** | **String**| The entity state (Etag) version of the product policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productPolicyGet

> ProductPolicyListByProduct200ResponseValueInner productPolicyGet(apiVersion, productId, policyId)



Get the policy configuration at the Product level.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.ProductPolicyApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let policyId = "policyId_example"; // String | The identifier of the Policy.
apiInstance.productPolicyGet(apiVersion, productId, policyId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **policyId** | **String**| The identifier of the Policy. | 

### Return type

[**ProductPolicyListByProduct200ResponseValueInner**](ProductPolicyListByProduct200ResponseValueInner.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.ms-azure-apim.policy+xml, application/vnd.ms-azure-apim.policy.raw+xml


## productPolicyListByProduct

> ProductPolicyListByProduct200Response productPolicyListByProduct(apiVersion, productId)



Get the policy configuration at the Product level.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.ProductPolicyApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
apiInstance.productPolicyListByProduct(apiVersion, productId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 

### Return type

[**ProductPolicyListByProduct200Response**](ProductPolicyListByProduct200Response.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


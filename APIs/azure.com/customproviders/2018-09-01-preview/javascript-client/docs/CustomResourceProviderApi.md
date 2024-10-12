# Customproviders.CustomResourceProviderApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customResourceProviderCreateOrUpdate**](CustomResourceProviderApi.md#customResourceProviderCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName} | 
[**customResourceProviderDelete**](CustomResourceProviderApi.md#customResourceProviderDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName} | 
[**customResourceProviderGet**](CustomResourceProviderApi.md#customResourceProviderGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName} | 
[**customResourceProviderListByResourceGroup**](CustomResourceProviderApi.md#customResourceProviderListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders | 
[**customResourceProviderListBySubscription**](CustomResourceProviderApi.md#customResourceProviderListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CustomProviders/resourceProviders | 
[**customResourceProviderUpdate**](CustomResourceProviderApi.md#customResourceProviderUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName} | 



## customResourceProviderCreateOrUpdate

> CustomRPManifest customResourceProviderCreateOrUpdate(subscriptionId, resourceGroupName, resourceProviderName, apiVersion, resourceProvider)



Creates or updates the custom resource provider.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.CustomResourceProviderApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceProviderName = "resourceProviderName_example"; // String | The name of the resource provider.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let resourceProvider = new Customproviders.CustomRPManifest(); // CustomRPManifest | The parameters required to create or update a custom resource provider definition.
apiInstance.customResourceProviderCreateOrUpdate(subscriptionId, resourceGroupName, resourceProviderName, apiVersion, resourceProvider, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceProviderName** | **String**| The name of the resource provider. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **resourceProvider** | [**CustomRPManifest**](CustomRPManifest.md)| The parameters required to create or update a custom resource provider definition. | 

### Return type

[**CustomRPManifest**](CustomRPManifest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customResourceProviderDelete

> customResourceProviderDelete(subscriptionId, resourceGroupName, resourceProviderName, apiVersion)



Deletes the custom resource provider.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.CustomResourceProviderApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceProviderName = "resourceProviderName_example"; // String | The name of the resource provider.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.customResourceProviderDelete(subscriptionId, resourceGroupName, resourceProviderName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceProviderName** | **String**| The name of the resource provider. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customResourceProviderGet

> CustomRPManifest customResourceProviderGet(subscriptionId, resourceGroupName, resourceProviderName, apiVersion)



Gets the custom resource provider manifest.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.CustomResourceProviderApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceProviderName = "resourceProviderName_example"; // String | The name of the resource provider.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.customResourceProviderGet(subscriptionId, resourceGroupName, resourceProviderName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceProviderName** | **String**| The name of the resource provider. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

[**CustomRPManifest**](CustomRPManifest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customResourceProviderListByResourceGroup

> ListByCustomRPManifest customResourceProviderListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Gets all the custom resource providers within a resource group.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.CustomResourceProviderApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.customResourceProviderListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

[**ListByCustomRPManifest**](ListByCustomRPManifest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customResourceProviderListBySubscription

> ListByCustomRPManifest customResourceProviderListBySubscription(subscriptionId, apiVersion)



Gets all the custom resource providers within a subscription.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.CustomResourceProviderApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
apiInstance.customResourceProviderListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

[**ListByCustomRPManifest**](ListByCustomRPManifest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customResourceProviderUpdate

> CustomRPManifest customResourceProviderUpdate(subscriptionId, resourceGroupName, resourceProviderName, apiVersion, patchableResource)



Updates an existing custom resource provider. The only value that can be updated via PATCH currently is the tags.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.CustomResourceProviderApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceProviderName = "resourceProviderName_example"; // String | The name of the resource provider.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let patchableResource = new Customproviders.ResourceProvidersUpdate(); // ResourceProvidersUpdate | The updatable fields of a custom resource provider.
apiInstance.customResourceProviderUpdate(subscriptionId, resourceGroupName, resourceProviderName, apiVersion, patchableResource, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceProviderName** | **String**| The name of the resource provider. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **patchableResource** | [**ResourceProvidersUpdate**](ResourceProvidersUpdate.md)| The updatable fields of a custom resource provider. | 

### Return type

[**CustomRPManifest**](CustomRPManifest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


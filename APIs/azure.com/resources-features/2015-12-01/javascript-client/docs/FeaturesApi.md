# FeatureClient.FeaturesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**featuresGet**](FeaturesApi.md#featuresGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Features/providers/{resourceProviderNamespace}/features/{featureName} | 
[**featuresList**](FeaturesApi.md#featuresList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Features/providers/{resourceProviderNamespace}/features | 
[**featuresListAll**](FeaturesApi.md#featuresListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Features/features | 
[**featuresRegister**](FeaturesApi.md#featuresRegister) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Features/providers/{resourceProviderNamespace}/features/{featureName}/register | 



## featuresGet

> FeatureResult featuresGet(resourceProviderNamespace, featureName, apiVersion, subscriptionId)



Gets the preview feature with the specified name.

### Example

```javascript
import FeatureClient from 'feature_client';
let defaultClient = FeatureClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeatureClient.FeaturesApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The resource provider namespace for the feature.
let featureName = "featureName_example"; // String | The name of the feature to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.featuresGet(resourceProviderNamespace, featureName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| The resource provider namespace for the feature. | 
 **featureName** | **String**| The name of the feature to get. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**FeatureResult**](FeatureResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## featuresList

> FeatureOperationsListResult featuresList(resourceProviderNamespace, apiVersion, subscriptionId)



Gets all the preview features in a provider namespace that are available through AFEC for the subscription.

### Example

```javascript
import FeatureClient from 'feature_client';
let defaultClient = FeatureClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeatureClient.FeaturesApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider for getting features.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.featuresList(resourceProviderNamespace, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| The namespace of the resource provider for getting features. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**FeatureOperationsListResult**](FeatureOperationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## featuresListAll

> FeatureOperationsListResult featuresListAll(apiVersion, subscriptionId)



Gets all the preview features that are available through AFEC for the subscription.

### Example

```javascript
import FeatureClient from 'feature_client';
let defaultClient = FeatureClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeatureClient.FeaturesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.featuresListAll(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**FeatureOperationsListResult**](FeatureOperationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## featuresRegister

> FeatureResult featuresRegister(resourceProviderNamespace, featureName, apiVersion, subscriptionId)



Registers the preview feature for the subscription.

### Example

```javascript
import FeatureClient from 'feature_client';
let defaultClient = FeatureClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeatureClient.FeaturesApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let featureName = "featureName_example"; // String | The name of the feature to register.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.featuresRegister(resourceProviderNamespace, featureName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **featureName** | **String**| The name of the feature to register. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**FeatureResult**](FeatureResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


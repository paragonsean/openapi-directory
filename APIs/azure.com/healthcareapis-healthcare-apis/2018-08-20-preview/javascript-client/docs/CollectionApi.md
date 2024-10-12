# HealthcareApisClient.CollectionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesList**](CollectionApi.md#servicesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HealthcareApis/services | 
[**servicesListByResourceGroup**](CollectionApi.md#servicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HealthcareApis/services | 



## servicesList

> ServicesDescriptionListResult servicesList(apiVersion, subscriptionId)



Get all the service instances in a subscription.

### Example

```javascript
import HealthcareApisClient from 'healthcare_apis_client';
let defaultClient = HealthcareApisClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HealthcareApisClient.CollectionApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
apiInstance.servicesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 

### Return type

[**ServicesDescriptionListResult**](ServicesDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListByResourceGroup

> ServicesDescriptionListResult servicesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all the service instances in a resource group.

### Example

```javascript
import HealthcareApisClient from 'healthcare_apis_client';
let defaultClient = HealthcareApisClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HealthcareApisClient.CollectionApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the service instance.
apiInstance.servicesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the service instance. | 

### Return type

[**ServicesDescriptionListResult**](ServicesDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


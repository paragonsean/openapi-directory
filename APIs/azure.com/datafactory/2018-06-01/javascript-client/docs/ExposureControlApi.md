# DataFactoryManagementClient.ExposureControlApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exposureControlGetFeatureValue**](ExposureControlApi.md#exposureControlGetFeatureValue) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/getFeatureValue | 
[**exposureControlGetFeatureValueByFactory**](ExposureControlApi.md#exposureControlGetFeatureValueByFactory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getFeatureValue | 



## exposureControlGetFeatureValue

> ExposureControlResponse exposureControlGetFeatureValue(subscriptionId, locationId, apiVersion, exposureControlRequest)



Get exposure control feature for specific location.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.ExposureControlApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let locationId = "locationId_example"; // String | The location identifier.
let apiVersion = "apiVersion_example"; // String | The API version.
let exposureControlRequest = new DataFactoryManagementClient.ExposureControlRequest(); // ExposureControlRequest | The exposure control request.
apiInstance.exposureControlGetFeatureValue(subscriptionId, locationId, apiVersion, exposureControlRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **locationId** | **String**| The location identifier. | 
 **apiVersion** | **String**| The API version. | 
 **exposureControlRequest** | [**ExposureControlRequest**](ExposureControlRequest.md)| The exposure control request. | 

### Return type

[**ExposureControlResponse**](ExposureControlResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## exposureControlGetFeatureValueByFactory

> ExposureControlResponse exposureControlGetFeatureValueByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, exposureControlRequest)



Get exposure control feature for specific factory.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.ExposureControlApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let exposureControlRequest = new DataFactoryManagementClient.ExposureControlRequest(); // ExposureControlRequest | The exposure control request.
apiInstance.exposureControlGetFeatureValueByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, exposureControlRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **apiVersion** | **String**| The API version. | 
 **exposureControlRequest** | [**ExposureControlRequest**](ExposureControlRequest.md)| The exposure control request. | 

### Return type

[**ExposureControlResponse**](ExposureControlResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


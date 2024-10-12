# CustomerInsightsManagementClient.ImagesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imagesGetUploadUrlForData**](ImagesApi.md#imagesGetUploadUrlForData) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/images/getDataImageUploadUrl | 
[**imagesGetUploadUrlForEntityType**](ImagesApi.md#imagesGetUploadUrlForEntityType) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/images/getEntityTypeImageUploadUrl | 



## imagesGetUploadUrlForData

> ImageDefinition imagesGetUploadUrlForData(resourceGroupName, hubName, apiVersion, subscriptionId, parameters)



Gets data image upload URL.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.ImagesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new CustomerInsightsManagementClient.GetImageUploadUrlInput(); // GetImageUploadUrlInput | Parameters supplied to the GetUploadUrlForData operation.
apiInstance.imagesGetUploadUrlForData(resourceGroupName, hubName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **hubName** | **String**| The name of the hub. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**GetImageUploadUrlInput**](GetImageUploadUrlInput.md)| Parameters supplied to the GetUploadUrlForData operation. | 

### Return type

[**ImageDefinition**](ImageDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## imagesGetUploadUrlForEntityType

> ImageDefinition imagesGetUploadUrlForEntityType(resourceGroupName, hubName, apiVersion, subscriptionId, parameters)



Gets entity type (profile or interaction) image upload URL.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.ImagesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new CustomerInsightsManagementClient.GetImageUploadUrlInput(); // GetImageUploadUrlInput | Parameters supplied to the GetUploadUrlForEntityType operation.
apiInstance.imagesGetUploadUrlForEntityType(resourceGroupName, hubName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **hubName** | **String**| The name of the hub. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**GetImageUploadUrlInput**](GetImageUploadUrlInput.md)| Parameters supplied to the GetUploadUrlForEntityType operation. | 

### Return type

[**ImageDefinition**](ImageDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


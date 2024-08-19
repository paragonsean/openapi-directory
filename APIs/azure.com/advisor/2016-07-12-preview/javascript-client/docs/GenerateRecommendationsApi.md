# AdvisorManagementClient.GenerateRecommendationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recommendationsGenerate**](GenerateRecommendationsApi.md#recommendationsGenerate) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/generateRecommendations | 
[**recommendationsGetGenerateRecommendationsStatus**](GenerateRecommendationsApi.md#recommendationsGetGenerateRecommendationsStatus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/generateRecommendations/{operationId} | 



## recommendationsGenerate

> recommendationsGenerate(subscriptionId, apiVersion)



Initiates the recommendation generation or computation process for a subscription. This operation is asynchronous. The generated recommendations are stored in a cache in the Advisor service.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.GenerateRecommendationsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.recommendationsGenerate(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## recommendationsGetGenerateRecommendationsStatus

> recommendationsGetGenerateRecommendationsStatus(subscriptionId, operationId, apiVersion)



Retrieves the status of the recommendation computation or generation process. Invoke this API after calling the generation recommendation. The URI of this API is returned in the Location field of the response header.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.GenerateRecommendationsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let operationId = "operationId_example"; // String | The operation ID, which can be found from the Location field in the generate recommendation response header.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.recommendationsGetGenerateRecommendationsStatus(subscriptionId, operationId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **operationId** | **String**| The operation ID, which can be found from the Location field in the generate recommendation response header. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


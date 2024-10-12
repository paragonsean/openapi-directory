# AdvisorManagementClient.GetRecommendationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recommendationsGet**](GetRecommendationsApi.md#recommendationsGet) | **GET** /{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId} | 
[**recommendationsList**](GetRecommendationsApi.md#recommendationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/recommendations | 



## recommendationsGet

> ResourceRecommendationBase recommendationsGet(resourceUri, recommendationId, apiVersion)



Obtains details of a cached recommendation.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.GetRecommendationsApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
let recommendationId = "recommendationId_example"; // String | The recommendation ID.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.recommendationsGet(resourceUri, recommendationId, apiVersion, (error, data, response) => {
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
 **resourceUri** | **String**| The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies. | 
 **recommendationId** | **String**| The recommendation ID. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**ResourceRecommendationBase**](ResourceRecommendationBase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsList

> ResourceRecommendationBaseListResult recommendationsList(subscriptionId, apiVersion, opts)



Obtains cached recommendations for a subscription. The recommendations are generated or computed by invoking generateRecommendations.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.GetRecommendationsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The filter to apply to the recommendations.
  'top': 56, // Number | The number of recommendations per page if a paged version of this API is being used.
  'skipToken': "skipToken_example" // String | The page-continuation token to use with a paged version of this API.
};
apiInstance.recommendationsList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The filter to apply to the recommendations. | [optional] 
 **top** | **Number**| The number of recommendations per page if a paged version of this API is being used. | [optional] 
 **skipToken** | **String**| The page-continuation token to use with a paged version of this API. | [optional] 

### Return type

[**ResourceRecommendationBaseListResult**](ResourceRecommendationBaseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# AdvisorManagementClient.SuppressionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suppressionsCreate**](SuppressionsApi.md#suppressionsCreate) | **PUT** /{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name} | 
[**suppressionsDelete**](SuppressionsApi.md#suppressionsDelete) | **DELETE** /{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name} | 
[**suppressionsGet**](SuppressionsApi.md#suppressionsGet) | **GET** /{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId}/suppressions/{name} | 
[**suppressionsList**](SuppressionsApi.md#suppressionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/suppressions | 



## suppressionsCreate

> SuppressionContract suppressionsCreate(resourceUri, recommendationId, name, apiVersion, suppressionContract)



Enables the snoozed or dismissed attribute of a recommendation. The snoozed or dismissed attribute is referred to as a suppression. Use this API to create or update the snoozed or dismissed status of a recommendation.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.SuppressionsApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
let recommendationId = "recommendationId_example"; // String | The recommendation ID.
let name = "name_example"; // String | The name of the suppression.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let suppressionContract = new AdvisorManagementClient.SuppressionContract(); // SuppressionContract | The snoozed or dismissed attribute; for example, the snooze duration.
apiInstance.suppressionsCreate(resourceUri, recommendationId, name, apiVersion, suppressionContract, (error, data, response) => {
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
 **name** | **String**| The name of the suppression. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **suppressionContract** | [**SuppressionContract**](SuppressionContract.md)| The snoozed or dismissed attribute; for example, the snooze duration. | 

### Return type

[**SuppressionContract**](SuppressionContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## suppressionsDelete

> suppressionsDelete(resourceUri, recommendationId, name, apiVersion)



Enables the activation of a snoozed or dismissed recommendation. The snoozed or dismissed attribute of a recommendation is referred to as a suppression.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.SuppressionsApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
let recommendationId = "recommendationId_example"; // String | The recommendation ID.
let name = "name_example"; // String | The name of the suppression.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.suppressionsDelete(resourceUri, recommendationId, name, apiVersion, (error, data, response) => {
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
 **resourceUri** | **String**| The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies. | 
 **recommendationId** | **String**| The recommendation ID. | 
 **name** | **String**| The name of the suppression. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## suppressionsGet

> SuppressionContract suppressionsGet(resourceUri, recommendationId, name, apiVersion)



Obtains the details of a suppression.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.SuppressionsApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
let recommendationId = "recommendationId_example"; // String | The recommendation ID.
let name = "name_example"; // String | The name of the suppression.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.suppressionsGet(resourceUri, recommendationId, name, apiVersion, (error, data, response) => {
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
 **name** | **String**| The name of the suppression. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**SuppressionContract**](SuppressionContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suppressionsList

> SuppressionContractListResult suppressionsList(subscriptionId, apiVersion, opts)



Retrieves the list of snoozed or dismissed suppressions for a subscription. The snoozed or dismissed attribute of a recommendation is referred to as a suppression.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.SuppressionsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'top': 56, // Number | The number of suppressions per page if a paged version of this API is being used.
  'skipToken': "skipToken_example" // String | The page-continuation token to use with a paged version of this API.
};
apiInstance.suppressionsList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **top** | **Number**| The number of suppressions per page if a paged version of this API is being used. | [optional] 
 **skipToken** | **String**| The page-continuation token to use with a paged version of this API. | [optional] 

### Return type

[**SuppressionContractListResult**](SuppressionContractListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


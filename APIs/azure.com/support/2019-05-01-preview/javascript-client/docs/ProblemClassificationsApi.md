# MicrosoftSupport.ProblemClassificationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**problemClassificationsGet**](ProblemClassificationsApi.md#problemClassificationsGet) | **GET** /providers/Microsoft.Support/services/{serviceName}/problemClassifications/{problemClassificationName} | 
[**problemClassificationsList**](ProblemClassificationsApi.md#problemClassificationsList) | **GET** /providers/Microsoft.Support/services/{serviceName}/problemClassifications | 



## problemClassificationsGet

> ProblemClassification problemClassificationsGet(serviceName, problemClassificationName, apiVersion)



Gets the details of a specific problem classification for a specific Azure service.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.ProblemClassificationsApi();
let serviceName = "serviceName_example"; // String | Name of Azure service available for support.
let problemClassificationName = "problemClassificationName_example"; // String | Name of problem classification.
let apiVersion = "apiVersion_example"; // String | Api version
apiInstance.problemClassificationsGet(serviceName, problemClassificationName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| Name of Azure service available for support. | 
 **problemClassificationName** | **String**| Name of problem classification. | 
 **apiVersion** | **String**| Api version | 

### Return type

[**ProblemClassification**](ProblemClassification.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## problemClassificationsList

> ProblemClassificationsListResult problemClassificationsList(serviceName, apiVersion)



Lists all the problem classifications (categories) available for a specific Azure service.&lt;br/&gt;&lt;br/&gt; Always use the service and problem classifications obtained programmatically. This practice ensures that you always have the most recent set of service and problem classification Ids.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.ProblemClassificationsApi();
let serviceName = "serviceName_example"; // String | Name of Azure service for which the problem classifications need to be retrieved.
let apiVersion = "apiVersion_example"; // String | Api version
apiInstance.problemClassificationsList(serviceName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| Name of Azure service for which the problem classifications need to be retrieved. | 
 **apiVersion** | **String**| Api version | 

### Return type

[**ProblemClassificationsListResult**](ProblemClassificationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


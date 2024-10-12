# InfrastructureInsightsManagementClient.InfrastructureInsightsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](InfrastructureInsightsApi.md#operationsList) | **GET** /providers/Microsoft.InfrastructureInsights.Admin/operations | 



## operationsList

> OperationList operationsList(apiVersion)



Returns a list of support REST operations.

### Example

```javascript
import InfrastructureInsightsManagementClient from 'infrastructure_insights_management_client';
let defaultClient = InfrastructureInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InfrastructureInsightsManagementClient.InfrastructureInsightsApi();
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**OperationList**](OperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


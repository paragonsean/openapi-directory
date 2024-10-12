# AzureResourceGraph.ResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources**](ResourcesApi.md#resources) | **POST** /providers/Microsoft.ResourceGraph/resources | 



## resources

> QueryResponse resources(apiVersion, query)



Queries the resources managed by Azure Resource Manager for all subscriptions specified in the request.

### Example

```javascript
import AzureResourceGraph from 'azure_resource_graph';
let defaultClient = AzureResourceGraph.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureResourceGraph.ResourcesApi();
let apiVersion = "apiVersion_example"; // String | API version.
let query = new AzureResourceGraph.QueryRequest(); // QueryRequest | Request specifying query and its options.
apiInstance.resources(apiVersion, query, (error, data, response) => {
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
 **apiVersion** | **String**| API version. | 
 **query** | [**QueryRequest**](QueryRequest.md)| Request specifying query and its options. | 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


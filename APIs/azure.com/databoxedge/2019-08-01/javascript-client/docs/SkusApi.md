# DataBoxEdgeManagementClient.SkusApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**skusList**](SkusApi.md#skusList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataBoxEdge/skus | List all the available Skus in the region and information related to them



## skusList

> SkuInformationList skusList(subscriptionId, apiVersion, opts)

List all the available Skus in the region and information related to them

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.SkusApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'filter': "filter_example" // String | Specify $filter='location eq <location>' to filter on location.
};
apiInstance.skusList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **apiVersion** | **String**| The API version. | 
 **filter** | **String**| Specify $filter&#x3D;&#39;location eq &lt;location&gt;&#39; to filter on location. | [optional] 

### Return type

[**SkuInformationList**](SkuInformationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


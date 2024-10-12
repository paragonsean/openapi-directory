# ManagementGroups.ManagementGroupsDescendantsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managementGroupsGetDescendants**](ManagementGroupsDescendantsApi.md#managementGroupsGetDescendants) | **GET** /providers/Microsoft.Management/managementGroups/{groupId}/descendants | 



## managementGroupsGetDescendants

> DescendantListResult managementGroupsGetDescendants(groupId, apiVersion, opts)



List all entities that descend from a management group.

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.ManagementGroupsDescendantsApi();
let groupId = "groupId_example"; // String | Management Group ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let opts = {
  'skiptoken': "skiptoken_example", // String | Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | Number of elements to return when retrieving results. Passing this in will override $skipToken.
};
apiInstance.managementGroupsGetDescendants(groupId, apiVersion, opts, (error, data, response) => {
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
 **groupId** | **String**| Management Group ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | 
 **skiptoken** | **String**| Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| Number of elements to return when retrieving results. Passing this in will override $skipToken. | [optional] 

### Return type

[**DescendantListResult**](DescendantListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# ManagementGroups.ManagementGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managementGroupsGet**](ManagementGroupsApi.md#managementGroupsGet) | **GET** /providers/Microsoft.Management/managementGroups/{groupId} | 
[**managementGroupsList**](ManagementGroupsApi.md#managementGroupsList) | **GET** /providers/Microsoft.Management/managementGroups | 



## managementGroupsGet

> ManagementGroupWithHierarchy managementGroupsGet(groupId, apiVersion, opts)



Get the details of the management group. 

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.ManagementGroupsApi();
let groupId = "groupId_example"; // String | Management Group ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-08-31-preview.
let opts = {
  'expand': "expand_example", // String | The $expand=children query string parameter allows clients to request inclusion of children in the response payload.
  'recurse': true // Boolean | The $recurse=true query string parameter allows clients to request inclusion of entire hierarchy in the response payload.
};
apiInstance.managementGroupsGet(groupId, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-08-31-preview. | 
 **expand** | **String**| The $expand&#x3D;children query string parameter allows clients to request inclusion of children in the response payload. | [optional] 
 **recurse** | **Boolean**| The $recurse&#x3D;true query string parameter allows clients to request inclusion of entire hierarchy in the response payload. | [optional] 

### Return type

[**ManagementGroupWithHierarchy**](ManagementGroupWithHierarchy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementGroupsList

> ManagementGroupListResult managementGroupsList(apiVersion, opts)



List management groups for the authenticated user. 

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.ManagementGroupsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-08-31-preview.
let opts = {
  'skiptoken': "skiptoken_example" // String | Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. 
};
apiInstance.managementGroupsList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-08-31-preview. | 
 **skiptoken** | **String**| Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.  | [optional] 

### Return type

[**ManagementGroupListResult**](ManagementGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


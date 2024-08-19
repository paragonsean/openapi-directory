# SeveraPublicRestApiDocumentation.ResourceallocationsDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourceAllocationsDeleteResourceAllocation**](ResourceallocationsDeleteApi.md#resourceAllocationsDeleteResourceAllocation) | **DELETE** /v1/resourceallocations/{guid} | Delete an resource allocation
[**roleAllocationsDeleteRoleAllocation**](ResourceallocationsDeleteApi.md#roleAllocationsDeleteRoleAllocation) | **DELETE** /v1/roleallocations/{guid} | Delete a role allocation.



## resourceAllocationsDeleteResourceAllocation

> resourceAllocationsDeleteResourceAllocation(guid)

Delete an resource allocation

Returns: No Content (204) if succeeded. Not found (404) if resource allocation can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsDeleteApi();
let guid = "guid_example"; // String | ID of the resource allocation to delete
apiInstance.resourceAllocationsDeleteResourceAllocation(guid, (error, data, response) => {
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
 **guid** | **String**| ID of the resource allocation to delete | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## roleAllocationsDeleteRoleAllocation

> roleAllocationsDeleteRoleAllocation(guid)

Delete a role allocation.

Returns: No Content (204) if succeeded. Not found (404) if role can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsDeleteApi();
let guid = "guid_example"; // String | ID for the role allocation to delete.
apiInstance.roleAllocationsDeleteRoleAllocation(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the role allocation to delete. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


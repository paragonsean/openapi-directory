# ManagementGroups.EntitiesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entitiesList**](EntitiesApi.md#entitiesList) | **POST** /providers/Microsoft.Management/getEntities | 



## entitiesList

> EntityListResult entitiesList(apiVersion, opts)



List all entities (Management Groups, Subscriptions, etc.) for the authenticated user. 

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.EntitiesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let opts = {
  'skiptoken': "skiptoken_example", // String | Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. 
  'groupName': "groupName_example", // String | A filter which allows the call to be filtered for a specific group.
  'cacheControl': "'no-cache'" // String | Indicates that the request shouldn't utilize any caches.
};
apiInstance.entitiesList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | 
 **skiptoken** | **String**| Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.  | [optional] 
 **groupName** | **String**| A filter which allows the call to be filtered for a specific group. | [optional] 
 **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to &#39;no-cache&#39;]

### Return type

[**EntityListResult**](EntityListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


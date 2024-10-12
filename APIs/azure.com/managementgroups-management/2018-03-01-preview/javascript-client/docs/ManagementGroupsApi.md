# ManagementGroups.ManagementGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managementGroupSubscriptionsCreate**](ManagementGroupsApi.md#managementGroupSubscriptionsCreate) | **PUT** /providers/Microsoft.Management/managementGroups/{groupId}/subscriptions/{subscriptionId} | 
[**managementGroupSubscriptionsDelete**](ManagementGroupsApi.md#managementGroupSubscriptionsDelete) | **DELETE** /providers/Microsoft.Management/managementGroups/{groupId}/subscriptions/{subscriptionId} | 
[**managementGroupsCreateOrUpdate**](ManagementGroupsApi.md#managementGroupsCreateOrUpdate) | **PUT** /providers/Microsoft.Management/managementGroups/{groupId} | 
[**managementGroupsDelete**](ManagementGroupsApi.md#managementGroupsDelete) | **DELETE** /providers/Microsoft.Management/managementGroups/{groupId} | 
[**managementGroupsGet**](ManagementGroupsApi.md#managementGroupsGet) | **GET** /providers/Microsoft.Management/managementGroups/{groupId} | 
[**managementGroupsList**](ManagementGroupsApi.md#managementGroupsList) | **GET** /providers/Microsoft.Management/managementGroups | 
[**managementGroupsUpdate**](ManagementGroupsApi.md#managementGroupsUpdate) | **PATCH** /providers/Microsoft.Management/managementGroups/{groupId} | 



## managementGroupSubscriptionsCreate

> managementGroupSubscriptionsCreate(groupId, subscriptionId, apiVersion, opts)



Associates existing subscription with the management group.

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.ManagementGroupsApi();
let groupId = "groupId_example"; // String | Management Group ID.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let opts = {
  'cacheControl': "'no-cache'" // String | Indicates that the request shouldn't utilize any caches.
};
apiInstance.managementGroupSubscriptionsCreate(groupId, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **groupId** | **String**| Management Group ID. | 
 **subscriptionId** | **String**| Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | 
 **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to &#39;no-cache&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementGroupSubscriptionsDelete

> managementGroupSubscriptionsDelete(groupId, subscriptionId, apiVersion, opts)



De-associates subscription from the management group.

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.ManagementGroupsApi();
let groupId = "groupId_example"; // String | Management Group ID.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let opts = {
  'cacheControl': "'no-cache'" // String | Indicates that the request shouldn't utilize any caches.
};
apiInstance.managementGroupSubscriptionsDelete(groupId, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **groupId** | **String**| Management Group ID. | 
 **subscriptionId** | **String**| Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | 
 **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to &#39;no-cache&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementGroupsCreateOrUpdate

> ManagementGroup managementGroupsCreateOrUpdate(groupId, apiVersion, createManagementGroupRequest, opts)



Create or update a management group. If a management group is already created and a subsequent create request is issued with different properties, the management group properties will be updated.

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.ManagementGroupsApi();
let groupId = "groupId_example"; // String | Management Group ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let createManagementGroupRequest = new ManagementGroups.CreateManagementGroupRequest(); // CreateManagementGroupRequest | Management group creation parameters.
let opts = {
  'cacheControl': "'no-cache'" // String | Indicates that the request shouldn't utilize any caches.
};
apiInstance.managementGroupsCreateOrUpdate(groupId, apiVersion, createManagementGroupRequest, opts, (error, data, response) => {
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
 **createManagementGroupRequest** | [**CreateManagementGroupRequest**](CreateManagementGroupRequest.md)| Management group creation parameters. | 
 **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to &#39;no-cache&#39;]

### Return type

[**ManagementGroup**](ManagementGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managementGroupsDelete

> OperationResults managementGroupsDelete(groupId, apiVersion, opts)



Delete management group. If a management group contains child resources, the request will fail.

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.ManagementGroupsApi();
let groupId = "groupId_example"; // String | Management Group ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let opts = {
  'cacheControl': "'no-cache'" // String | Indicates that the request shouldn't utilize any caches.
};
apiInstance.managementGroupsDelete(groupId, apiVersion, opts, (error, data, response) => {
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
 **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to &#39;no-cache&#39;]

### Return type

[**OperationResults**](OperationResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementGroupsGet

> ManagementGroup managementGroupsGet(groupId, apiVersion, opts)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let opts = {
  'expand': "expand_example", // String | The $expand=children query string parameter allows clients to request inclusion of children in the response payload.
  'recurse': true, // Boolean | The $recurse=true query string parameter allows clients to request inclusion of entire hierarchy in the response payload. Note that  $expand=children must be passed up if $recurse is set to true.
  'filter': "filter_example", // String | A filter which allows the exclusion of subscriptions from results (i.e. '$filter=children.childType ne Subscription')
  'cacheControl': "'no-cache'" // String | Indicates that the request shouldn't utilize any caches.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | 
 **expand** | **String**| The $expand&#x3D;children query string parameter allows clients to request inclusion of children in the response payload. | [optional] 
 **recurse** | **Boolean**| The $recurse&#x3D;true query string parameter allows clients to request inclusion of entire hierarchy in the response payload. Note that  $expand&#x3D;children must be passed up if $recurse is set to true. | [optional] 
 **filter** | **String**| A filter which allows the exclusion of subscriptions from results (i.e. &#39;$filter&#x3D;children.childType ne Subscription&#39;) | [optional] 
 **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to &#39;no-cache&#39;]

### Return type

[**ManagementGroup**](ManagementGroup.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let opts = {
  'cacheControl': "'no-cache'", // String | Indicates that the request shouldn't utilize any caches.
  'skiptoken': "skiptoken_example" // String | Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | 
 **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to &#39;no-cache&#39;]
 **skiptoken** | **String**| Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. | [optional] 

### Return type

[**ManagementGroupListResult**](ManagementGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementGroupsUpdate

> ManagementGroup managementGroupsUpdate(groupId, apiVersion, patchGroupRequest, opts)



Update a management group.

### Example

```javascript
import ManagementGroups from 'management_groups';
let defaultClient = ManagementGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementGroups.ManagementGroupsApi();
let groupId = "groupId_example"; // String | Management Group ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
let patchGroupRequest = new ManagementGroups.PatchManagementGroupRequest(); // PatchManagementGroupRequest | Management group patch parameters.
let opts = {
  'cacheControl': "'no-cache'" // String | Indicates that the request shouldn't utilize any caches.
};
apiInstance.managementGroupsUpdate(groupId, apiVersion, patchGroupRequest, opts, (error, data, response) => {
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
 **patchGroupRequest** | [**PatchManagementGroupRequest**](PatchManagementGroupRequest.md)| Management group patch parameters. | 
 **cacheControl** | **String**| Indicates that the request shouldn&#39;t utilize any caches. | [optional] [default to &#39;no-cache&#39;]

### Return type

[**ManagementGroup**](ManagementGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


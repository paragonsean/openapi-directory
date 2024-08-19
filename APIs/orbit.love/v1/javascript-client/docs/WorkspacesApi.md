# OrbitApi.WorkspacesApi

All URIs are relative to *https://app.orbit.love/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspacesGet**](WorkspacesApi.md#workspacesGet) | **GET** /workspaces | Get all workspaces for the current user
[**workspacesWorkspaceSlugGet**](WorkspacesApi.md#workspacesWorkspaceSlugGet) | **GET** /workspaces/{workspace_slug} | Get a workspace



## workspacesGet

> workspacesGet()

Get all workspaces for the current user

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.WorkspacesApi();
apiInstance.workspacesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceSlugGet

> workspacesWorkspaceSlugGet(workspaceSlug, opts)

Get a workspace

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.WorkspacesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let opts = {
  'includeOrbitLevelCounts': true // Boolean | Include the number of members by Orbit Level in the attributes
};
apiInstance.workspacesWorkspaceSlugGet(workspaceSlug, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **includeOrbitLevelCounts** | **Boolean**| Include the number of members by Orbit Level in the attributes | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


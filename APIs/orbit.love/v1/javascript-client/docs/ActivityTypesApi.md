# OrbitApi.ActivityTypesApi

All URIs are relative to *https://app.orbit.love/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaceSlugActivityTypesGet**](ActivityTypesApi.md#workspaceSlugActivityTypesGet) | **GET** /{workspace_slug}/activity_types | List all activity types for a workspace



## workspaceSlugActivityTypesGet

> workspaceSlugActivityTypesGet(workspaceSlug)

List all activity types for a workspace

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.ActivityTypesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
apiInstance.workspaceSlugActivityTypesGet(workspaceSlug, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OrbitApi.OrganizationsApi

All URIs are relative to *https://app.orbit.love/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaceSlugOrganizationsGet**](OrganizationsApi.md#workspaceSlugOrganizationsGet) | **GET** /{workspace_slug}/organizations | List organizations in a workspace
[**workspaceSlugOrganizationsOrganizationIdGet**](OrganizationsApi.md#workspaceSlugOrganizationsOrganizationIdGet) | **GET** /{workspace_slug}/organizations/{organization_id} | Get an organization
[**workspaceSlugOrganizationsOrganizationIdPut**](OrganizationsApi.md#workspaceSlugOrganizationsOrganizationIdPut) | **PUT** /{workspace_slug}/organizations/{organization_id} | Update an organization



## workspaceSlugOrganizationsGet

> workspaceSlugOrganizationsGet(workspaceSlug, opts)

List organizations in a workspace

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.OrganizationsApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let opts = {
  'query': "query_example", // String | 
  'page': "page_example", // String | 
  'direction': "direction_example", // String | 
  'items': "items_example", // String | 
  'sort': "sort_example" // String | 
};
apiInstance.workspaceSlugOrganizationsGet(workspaceSlug, opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] 
 **page** | **String**|  | [optional] 
 **direction** | **String**|  | [optional] 
 **items** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugOrganizationsOrganizationIdGet

> workspaceSlugOrganizationsOrganizationIdGet(workspaceSlug, organizationId)

Get an organization

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.OrganizationsApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let organizationId = "organizationId_example"; // String | 
apiInstance.workspaceSlugOrganizationsOrganizationIdGet(workspaceSlug, organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugOrganizationsOrganizationIdPut

> workspaceSlugOrganizationsOrganizationIdPut(workspaceSlug, organizationId, opts)

Update an organization

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.OrganizationsApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let organizationId = "organizationId_example"; // String | 
let opts = {
  'organization': new OrbitApi.Organization() // Organization | 
};
apiInstance.workspaceSlugOrganizationsOrganizationIdPut(workspaceSlug, organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **organization** | [**Organization**](Organization.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


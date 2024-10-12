# SeveraPublicRestApiDocumentation.ResourceallocationsWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourceAllocationsPatchResourceAllocation**](ResourceallocationsWriteApi.md#resourceAllocationsPatchResourceAllocation) | **PATCH** /v1/resourceallocations/{guid} | Update (Patch) a resource allocation or a part of it
[**resourceAllocationsPostResourceAllocation**](ResourceallocationsWriteApi.md#resourceAllocationsPostResourceAllocation) | **POST** /v1/resourceallocations | Insert a resource allocation
[**roleAllocationsPatchRoleAllocation**](ResourceallocationsWriteApi.md#roleAllocationsPatchRoleAllocation) | **PATCH** /v1/roleallocations/{guid} | Update (Patch) a role allocation.
[**roleAllocationsPostRoleAllocation**](ResourceallocationsWriteApi.md#roleAllocationsPostRoleAllocation) | **POST** /v1/roleallocations | Insert a role allocation.



## resourceAllocationsPatchResourceAllocation

> [ResourceAllocationOutputModel] resourceAllocationsPatchResourceAllocation(guid, opts)

Update (Patch) a resource allocation or a part of it

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsWriteApi();
let guid = "guid_example"; // String | ID of the resource allocation
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of ResourceAllocationModel
};
apiInstance.resourceAllocationsPatchResourceAllocation(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the resource allocation | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of ResourceAllocationModel | [optional] 

### Return type

[**[ResourceAllocationOutputModel]**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resourceAllocationsPostResourceAllocation

> ResourceAllocationOutputModel resourceAllocationsPostResourceAllocation(opts)

Insert a resource allocation

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsWriteApi();
let opts = {
  'resourceAllocationInputModel': new SeveraPublicRestApiDocumentation.ResourceAllocationInputModel() // ResourceAllocationInputModel | ResourceAllocationInputModel
};
apiInstance.resourceAllocationsPostResourceAllocation(opts, (error, data, response) => {
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
 **resourceAllocationInputModel** | [**ResourceAllocationInputModel**](ResourceAllocationInputModel.md)| ResourceAllocationInputModel | [optional] 

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## roleAllocationsPatchRoleAllocation

> [RoleAllocationOutputModel] roleAllocationsPatchRoleAllocation(guid, opts)

Update (Patch) a role allocation.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsWriteApi();
let guid = "guid_example"; // String | ID of the role allocation.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of RoleAllocationModel.
};
apiInstance.roleAllocationsPatchRoleAllocation(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the role allocation. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of RoleAllocationModel. | [optional] 

### Return type

[**[RoleAllocationOutputModel]**](RoleAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## roleAllocationsPostRoleAllocation

> RoleAllocationOutputModel roleAllocationsPostRoleAllocation(opts)

Insert a role allocation.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsWriteApi();
let opts = {
  'roleAllocationInputModel': new SeveraPublicRestApiDocumentation.RoleAllocationInputModel() // RoleAllocationInputModel | Role allocation to insert.
};
apiInstance.roleAllocationsPostRoleAllocation(opts, (error, data, response) => {
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
 **roleAllocationInputModel** | [**RoleAllocationInputModel**](RoleAllocationInputModel.md)| Role allocation to insert. | [optional] 

### Return type

[**RoleAllocationOutputModel**](RoleAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


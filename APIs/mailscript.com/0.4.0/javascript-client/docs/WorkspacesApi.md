# Mailscript.WorkspacesApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addWorkspace**](WorkspacesApi.md#addWorkspace) | **POST** /workspaces | Claim a Mailscript workspace
[**getAllWorkspaces**](WorkspacesApi.md#getAllWorkspaces) | **GET** /workspaces | Get all workspaces you have access to



## addWorkspace

> addWorkspace(addWorkspaceRequest)

Claim a Mailscript workspace

An attendant address will be created as well

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.WorkspacesApi();
let addWorkspaceRequest = new Mailscript.AddWorkspaceRequest(); // AddWorkspaceRequest | request body
apiInstance.addWorkspace(addWorkspaceRequest, (error, data, response) => {
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
 **addWorkspaceRequest** | [**AddWorkspaceRequest**](AddWorkspaceRequest.md)| request body | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAllWorkspaces

> GetAllWorkspacesResponse getAllWorkspaces()

Get all workspaces you have access to



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.WorkspacesApi();
apiInstance.getAllWorkspaces((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllWorkspacesResponse**](GetAllWorkspacesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


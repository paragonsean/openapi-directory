# PdfGeneratorApi.WorkspacesApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteWorkspace**](WorkspacesApi.md#deleteWorkspace) | **DELETE** /workspaces/workspaceId | Delete workspace
[**getWorkspace**](WorkspacesApi.md#getWorkspace) | **GET** /workspaces/workspaceId | Get workspace



## deleteWorkspace

> DeleteTemplate200Response deleteWorkspace(workspaceId)

Delete workspace

Deletes the workspace

### Example

```javascript
import PdfGeneratorApi from 'pdf_generator_api';
let defaultClient = PdfGeneratorApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: JSONWebTokenAuth
let JSONWebTokenAuth = defaultClient.authentications['JSONWebTokenAuth'];
JSONWebTokenAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PdfGeneratorApi.WorkspacesApi();
let workspaceId = "demo.example@actualreports.com"; // String | Workspace identifier
apiInstance.deleteWorkspace(workspaceId, (error, data, response) => {
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
 **workspaceId** | **String**| Workspace identifier | 

### Return type

[**DeleteTemplate200Response**](DeleteTemplate200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWorkspace

> GetWorkspace200Response getWorkspace(workspaceId)

Get workspace

Returns workspace information

### Example

```javascript
import PdfGeneratorApi from 'pdf_generator_api';
let defaultClient = PdfGeneratorApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: JSONWebTokenAuth
let JSONWebTokenAuth = defaultClient.authentications['JSONWebTokenAuth'];
JSONWebTokenAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PdfGeneratorApi.WorkspacesApi();
let workspaceId = "demo.example@actualreports.com"; // String | Workspace identifier
apiInstance.getWorkspace(workspaceId, (error, data, response) => {
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
 **workspaceId** | **String**| Workspace identifier | 

### Return type

[**GetWorkspace200Response**](GetWorkspace200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


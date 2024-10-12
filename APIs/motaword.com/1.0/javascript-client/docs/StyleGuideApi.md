# MotaWordApi.StyleGuideApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createStyleGuide**](StyleGuideApi.md#createStyleGuide) | **POST** /projects/{projectId}/styleguides | Upload a new style guide
[**deleteStyleGuide**](StyleGuideApi.md#deleteStyleGuide) | **DELETE** /projects/{projectId}/styleguides/{styleGuideId} | Delete a style guide
[**downloadGlobalStyleGuide**](StyleGuideApi.md#downloadGlobalStyleGuide) | **GET** /styleguide | Download account style guide
[**downloadStyleGuide**](StyleGuideApi.md#downloadStyleGuide) | **GET** /projects/{projectId}/styleguides/{styleGuideId}/download | Download a style guide
[**getStyleGuide**](StyleGuideApi.md#getStyleGuide) | **GET** /projects/{projectId}/styleguides/{styleGuideId} | View a style guide
[**getStyleGuides**](StyleGuideApi.md#getStyleGuides) | **GET** /projects/{projectId}/styleguides | View style guides
[**updateGlobalStyleGuide**](StyleGuideApi.md#updateGlobalStyleGuide) | **POST** /styleguide | Create or update the account style guide
[**updateStyleGuide**](StyleGuideApi.md#updateStyleGuide) | **PUT** /projects/{projectId}/styleguides/{styleGuideId} | Update a style guide



## createStyleGuide

> StyleGuideList createStyleGuide(projectId, opts)

Upload a new style guide

Upload a new style guide

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StyleGuideApi();
let projectId = 74; // Number | Project ID
let opts = {
  'styleGuideUploadRequest': new MotaWordApi.StyleGuideUploadRequest() // StyleGuideUploadRequest | 
};
apiInstance.createStyleGuide(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **styleGuideUploadRequest** | [**StyleGuideUploadRequest**](StyleGuideUploadRequest.md)|  | [optional] 

### Return type

[**StyleGuideList**](StyleGuideList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json


## deleteStyleGuide

> OperationStatus deleteStyleGuide(projectId, styleGuideId)

Delete a style guide

Delete the existing style guide from the project.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StyleGuideApi();
let projectId = 74; // Number | Project ID
let styleGuideId = 13959; // Number | Style Guide ID
apiInstance.deleteStyleGuide(projectId, styleGuideId, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **styleGuideId** | **Number**| Style Guide ID | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## downloadGlobalStyleGuide

> String downloadGlobalStyleGuide()

Download account style guide

Download your account&#39;s global style guide. This endpoint is available only for corporate account customers. This style guide will be automatically attached to each new project under your account.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StyleGuideApi();
apiInstance.downloadGlobalStyleGuide((error, data, response) => {
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

**String**

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## downloadStyleGuide

> String downloadStyleGuide(projectId, styleGuideId)

Download a style guide

Download a previously uploaded style guide file.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StyleGuideApi();
let projectId = 74; // Number | Project ID
let styleGuideId = 13959; // Number | Style Guide ID
apiInstance.downloadStyleGuide(projectId, styleGuideId, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **styleGuideId** | **Number**| Style Guide ID | 

### Return type

**String**

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStyleGuide

> StyleGuide getStyleGuide(projectId, styleGuideId, opts)

View a style guide

View the details of a style guide uploaded to a project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StyleGuideApi();
let projectId = 74; // Number | Project ID
let styleGuideId = 13959; // Number | Style Guide ID
let opts = {
  '_with': ["null"] // [String] | Attach further information. Possible values 'preview' to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]=preview for single document/style guide calls.
};
apiInstance.getStyleGuide(projectId, styleGuideId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **styleGuideId** | **Number**| Style Guide ID | 
 **_with** | [**[String]**](String.md)| Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls. | [optional] 

### Return type

[**StyleGuide**](StyleGuide.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStyleGuides

> StyleGuideList getStyleGuides(projectId, opts)

View style guides

View a list of style guides in your project.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StyleGuideApi();
let projectId = 74; // Number | Project ID
let opts = {
  '_with': ["null"] // [String] | Attach further information. Possible values 'preview' to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]=preview for single document/style guide calls.
};
apiInstance.getStyleGuides(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **_with** | [**[String]**](String.md)| Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls. | [optional] 

### Return type

[**StyleGuideList**](StyleGuideList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateGlobalStyleGuide

> OperationStatus updateGlobalStyleGuide(opts)

Create or update the account style guide

Update your corporate account&#39;s global style guide. This endpoint is available only for corporate account customers. This style guide will be automatically attached to each new project under your account.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StyleGuideApi();
let opts = {
  'accountStyleGuideUploadRequest': new MotaWordApi.AccountStyleGuideUploadRequest() // AccountStyleGuideUploadRequest | 
};
apiInstance.updateGlobalStyleGuide(opts, (error, data, response) => {
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
 **accountStyleGuideUploadRequest** | [**AccountStyleGuideUploadRequest**](AccountStyleGuideUploadRequest.md)|  | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json


## updateStyleGuide

> StyleGuide updateStyleGuide(projectId, styleGuideId, opts)

Update a style guide

Update the existing style guide in the project. Public users are allowed to have only 1 style guide per project and file name and contents will replaced with the new style guide that you are uploading via this endpoint.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StyleGuideApi();
let projectId = 74; // Number | Project ID
let styleGuideId = 13959; // Number | Style guide ID
let opts = {
  'styleGuideUploadRequest': new MotaWordApi.StyleGuideUploadRequest() // StyleGuideUploadRequest | 
};
apiInstance.updateStyleGuide(projectId, styleGuideId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **styleGuideId** | **Number**| Style guide ID | 
 **styleGuideUploadRequest** | [**StyleGuideUploadRequest**](StyleGuideUploadRequest.md)|  | [optional] 

### Return type

[**StyleGuide**](StyleGuide.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json


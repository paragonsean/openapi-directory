# VectaraRestApi.IndexServiceApi

All URIs are relative to *https://api.vectara.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callDelete**](IndexServiceApi.md#callDelete) | **POST** /v1/delete-doc | 
[**fileUpload**](IndexServiceApi.md#fileUpload) | **POST** /v1/upload | 
[**index**](IndexServiceApi.md#index) | **POST** /v1/index | 



## callDelete

> Object callDelete(customerId, vectaraDeleteDocumentRequest)



Delete

### Example

```javascript
import VectaraRestApi from 'vectara_rest_api';
let defaultClient = VectaraRestApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oAuth
let oAuth = defaultClient.authentications['oAuth'];
oAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VectaraRestApi.IndexServiceApi();
let customerId = 56; // Number | The Customer ID to use for the request.
let vectaraDeleteDocumentRequest = new VectaraRestApi.VectaraDeleteDocumentRequest(); // VectaraDeleteDocumentRequest | 
apiInstance.callDelete(customerId, vectaraDeleteDocumentRequest, (error, data, response) => {
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
 **customerId** | **Number**| The Customer ID to use for the request. | 
 **vectaraDeleteDocumentRequest** | [**VectaraDeleteDocumentRequest**](VectaraDeleteDocumentRequest.md)|  | 

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [oAuth](../README.md#oAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fileUpload

> FileUpload200Response fileUpload(c, o, opts)



File Upload

### Example

```javascript
import VectaraRestApi from 'vectara_rest_api';
let defaultClient = VectaraRestApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oAuth
let oAuth = defaultClient.authentications['oAuth'];
oAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VectaraRestApi.IndexServiceApi();
let c = 56; // Number | Customer ID
let o = 56; // Number | Corpus ID
let opts = {
  'd': true, // Boolean | If true, the server returns the extracted document that was indexed
  'docMetadata': "docMetadata_example", // String | A JSON string of any additional metadata you want attached to the file.
  'file': "/path/to/file" // File | The file to be indexed into Vectara.
};
apiInstance.fileUpload(c, o, opts, (error, data, response) => {
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
 **c** | **Number**| Customer ID | 
 **o** | **Number**| Corpus ID | 
 **d** | **Boolean**| If true, the server returns the extracted document that was indexed | [optional] 
 **docMetadata** | **String**| A JSON string of any additional metadata you want attached to the file. | [optional] 
 **file** | **File**| The file to be indexed into Vectara. | [optional] 

### Return type

[**FileUpload200Response**](FileUpload200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [oAuth](../README.md#oAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## index

> VectaraIndexDocumentResponse index(customerId, vectaraIndexDocumentRequest)



Index

### Example

```javascript
import VectaraRestApi from 'vectara_rest_api';
let defaultClient = VectaraRestApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oAuth
let oAuth = defaultClient.authentications['oAuth'];
oAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VectaraRestApi.IndexServiceApi();
let customerId = 56; // Number | The Customer ID to use for the request.
let vectaraIndexDocumentRequest = new VectaraRestApi.VectaraIndexDocumentRequest(); // VectaraIndexDocumentRequest | 
apiInstance.index(customerId, vectaraIndexDocumentRequest, (error, data, response) => {
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
 **customerId** | **Number**| The Customer ID to use for the request. | 
 **vectaraIndexDocumentRequest** | [**VectaraIndexDocumentRequest**](VectaraIndexDocumentRequest.md)|  | 

### Return type

[**VectaraIndexDocumentResponse**](VectaraIndexDocumentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [oAuth](../README.md#oAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


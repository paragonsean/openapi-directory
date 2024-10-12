# ServiceFabricClientApis.ImageStoreApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copyImageStoreContent**](ImageStoreApi.md#copyImageStoreContent) | **POST** /ImageStore/$/Copy | Copies image store content internally
[**deleteImageStoreContent**](ImageStoreApi.md#deleteImageStoreContent) | **DELETE** /ImageStore/{contentPath} | Deletes existing image store content.
[**getImageStoreContent**](ImageStoreApi.md#getImageStoreContent) | **GET** /ImageStore/{contentPath} | Gets the image store content information.
[**getImageStoreRootContent**](ImageStoreApi.md#getImageStoreRootContent) | **GET** /ImageStore | Gets the content information at the root of the image store.
[**uploadFile**](ImageStoreApi.md#uploadFile) | **PUT** /ImageStore/{contentPath} | Uploads contents of the file to the image store.



## copyImageStoreContent

> copyImageStoreContent(apiVersion, imageStoreCopyDescription, opts)

Copies image store content internally

Copies the image store content from the source image store relative path to the destination image store relative path.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ImageStoreApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let imageStoreCopyDescription = new ServiceFabricClientApis.ImageStoreCopyDescription(); // ImageStoreCopyDescription | Describes the copy description for the image store.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.copyImageStoreContent(apiVersion, imageStoreCopyDescription, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **imageStoreCopyDescription** | [**ImageStoreCopyDescription**](ImageStoreCopyDescription.md)| Describes the copy description for the image store. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteImageStoreContent

> deleteImageStoreContent(apiVersion, contentPath, opts)

Deletes existing image store content.

Deletes existing image store content being found within the given image store relative path. This can be used to delete uploaded application packages once they are provisioned.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ImageStoreApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let contentPath = "contentPath_example"; // String | Relative path to file or folder in the image store from its root.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.deleteImageStoreContent(apiVersion, contentPath, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **contentPath** | **String**| Relative path to file or folder in the image store from its root. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageStoreContent

> ImageStoreContent getImageStoreContent(apiVersion, contentPath, opts)

Gets the image store content information.

Returns the information about the image store content at the specified contentPath relative to the root of the image store.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ImageStoreApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let contentPath = "contentPath_example"; // String | Relative path to file or folder in the image store from its root.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getImageStoreContent(apiVersion, contentPath, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **contentPath** | **String**| Relative path to file or folder in the image store from its root. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ImageStoreContent**](ImageStoreContent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageStoreRootContent

> ImageStoreContent getImageStoreRootContent(apiVersion, opts)

Gets the content information at the root of the image store.

Returns the information about the image store content at the root of the image store.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ImageStoreApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getImageStoreRootContent(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ImageStoreContent**](ImageStoreContent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadFile

> uploadFile(apiVersion, contentPath, opts)

Uploads contents of the file to the image store.

Uploads contents of the file to the image store. Use this API if the file is small enough to upload again if the connection fails. The file&#39;s data needs to be added to the request body. The contents will be uploaded to the specified path. Image store service uses a mark file to indicate the availability of the folder. The mark file is an empty file named \&quot;_.dir\&quot;. The mark file is generated by the image store service when all files in a folder are uploaded. When using File-by-File approach to upload application package in REST, the image store service isn&#39;t aware of the file hierarchy of the application package; you need to create a mark file per folder and upload it last, to let the image store service know that the folder is complete. 

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ImageStoreApi();
let apiVersion = "'6.0'"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
let contentPath = "contentPath_example"; // String | Relative path to file or folder in the image store from its root.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.uploadFile(apiVersion, contentPath, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to &#39;6.0&#39;]
 **contentPath** | **String**| Relative path to file or folder in the image store from its root. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


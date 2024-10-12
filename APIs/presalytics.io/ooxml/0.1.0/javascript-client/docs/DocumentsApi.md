# OoxmlAutomation.DocumentsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documentsChildobjectsGetId**](DocumentsApi.md#documentsChildobjectsGetId) | **GET** /Documents/ChildObjects/{id} | DocumentsController: Get Dependent Objects Tree
[**documentsClonePostId**](DocumentsApi.md#documentsClonePostId) | **POST** /Documents/Clone/{id} | Documents: Clone an existing Ooxml Document to new Parent Story
[**documentsDeleteId**](DocumentsApi.md#documentsDeleteId) | **DELETE** /Documents/{id} | Documents: Delete by Id
[**documentsDownloadGetIdOrginal**](DocumentsApi.md#documentsDownloadGetIdOrginal) | **GET** /Documents/Download/{id} | Documents: Download
[**documentsGetId**](DocumentsApi.md#documentsGetId) | **GET** /Documents/{id} | Documents: Get by Id
[**documentsPost**](DocumentsApi.md#documentsPost) | **POST** /Documents | Documents: Upload



## documentsChildobjectsGetId

> [ChildObjects] documentsChildobjectsGetId(id)

DocumentsController: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this DocumentsController and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.DocumentsApi();
let id = "id_example"; // String | 
apiInstance.documentsChildobjectsGetId(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**[ChildObjects]**](ChildObjects.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## documentsClonePostId

> Document documentsClonePostId(id, opts)

Documents: Clone an existing Ooxml Document to new Parent Story

Clone A Document that has already been uploaded to a new Story

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.DocumentsApi();
let id = "id_example"; // String | the Source document Id
let opts = {
  'documentCloneDTO': new OoxmlAutomation.DocumentCloneDTO() // DocumentCloneDTO | A DocumentCloneDto object with containing information required for cloning the document
};
apiInstance.documentsClonePostId(id, opts, (error, data, response) => {
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
 **id** | **String**| the Source document Id | 
 **documentCloneDTO** | [**DocumentCloneDTO**](DocumentCloneDTO.md)| A DocumentCloneDto object with containing information required for cloning the document | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/json, text/plain


## documentsDeleteId

> documentsDeleteId(id)

Documents: Delete by Id

Permantly delete a document from the Ooxml Automation API. Note that is does not make changes to the related Presalytics APIs.  Please use the delete endpoint in the story API to ensure that stories are not left with orphaned references to the Ooxml Automation API.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.DocumentsApi();
let id = "id_example"; // String | 
apiInstance.documentsDeleteId(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## documentsDownloadGetIdOrginal

> File documentsDownloadGetIdOrginal(id, opts)

Documents: Download

Download the into a bytestream for client-side processing.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.DocumentsApi();
let id = "id_example"; // String | 
let opts = {
  'orginal': false // Boolean | 
};
apiInstance.documentsDownloadGetIdOrginal(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **orginal** | **Boolean**|  | [optional] [default to false]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## documentsGetId

> Document documentsGetId(id)

Documents: Get by Id

Get by Id: Use this method to retrieve a Documents object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.DocumentsApi();
let id = "id_example"; // String | 
apiInstance.documentsGetId(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## documentsPost

> [Document] documentsPost(file, storyId)

Documents: Upload

Upload an OpenOfficeXml document (e.g., .xlsx, .pptx) for processing by the API.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.DocumentsApi();
let file = "/path/to/file"; // File | The file to upload.  Must be of type .pptx, ppt
let storyId = "storyId_example"; // String | The story_id of the document being uploaded.
apiInstance.documentsPost(file, storyId, (error, data, response) => {
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
 **file** | **File**| The file to upload.  Must be of type .pptx, ppt | 
 **storyId** | **String**| The story_id of the document being uploaded. | 

### Return type

[**[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, text/json, text/plain


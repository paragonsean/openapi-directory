# Story.StoryApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storyGet**](StoryApi.md#storyGet) | **GET** / | Story: Get List of User Stories
[**storyIdAnalytics**](StoryApi.md#storyIdAnalytics) | **GET** /{id}/analytics | Story: View Analytics
[**storyIdDelete**](StoryApi.md#storyIdDelete) | **DELETE** /{id} | Story: Delete by Id
[**storyIdFileOoxmlautomationidDelete**](StoryApi.md#storyIdFileOoxmlautomationidDelete) | **DELETE** /{id}/file/{ooxml_automation_id} | Story: Delete Subdocument
[**storyIdFileOoxmlautomationidGet**](StoryApi.md#storyIdFileOoxmlautomationidGet) | **GET** /{id}/file/{ooxml_automation_id} | Story: Download Updated File
[**storyIdFilePost**](StoryApi.md#storyIdFilePost) | **POST** /{id}/file | Story: Upload a File To Existing Story
[**storyIdGet**](StoryApi.md#storyIdGet) | **GET** /{id} | Story: Get by Id
[**storyIdOutlineGet**](StoryApi.md#storyIdOutlineGet) | **GET** /{id}/outline | Story: Get Story Outline
[**storyIdOutlinePost**](StoryApi.md#storyIdOutlinePost) | **POST** /{id}/outline | Story: Post Story Outline
[**storyIdPublic**](StoryApi.md#storyIdPublic) | **GET** /{id}/public/ | Story: Public Link to Story Reveal.js Document
[**storyIdPut**](StoryApi.md#storyIdPut) | **PUT** /{id} | Story: Modify
[**storyIdReveal**](StoryApi.md#storyIdReveal) | **GET** /{id}/reveal | Story: Get Story at Reveal.js Document
[**storyIdStatusGet**](StoryApi.md#storyIdStatusGet) | **GET** /{id}/status | Story: Get Story Status
[**storyPost**](StoryApi.md#storyPost) | **POST** / | Story: Upload
[**storyPostFile**](StoryApi.md#storyPostFile) | **POST** /file | Story: Upload a File
[**storyPostFileJson**](StoryApi.md#storyPostFileJson) | **POST** /file/json | Story: Upload a File (base64)



## storyGet

> [Story] storyGet(opts)

Story: Get List of User Stories

Returns a list of stories for this user identifie via the access token presentated to the api

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let opts = {
  'includeRelationships': true, // Boolean | Indicate whether the returned object should include child relationships
  'includeOutline': true // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
};
apiInstance.storyGet(opts, (error, data, response) => {
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
 **includeRelationships** | **Boolean**| Indicate whether the returned object should include child relationships | [optional] 
 **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] 

### Return type

[**[Story]**](Story.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdAnalytics

> String storyIdAnalytics(id)

Story: View Analytics

returns an html document containing session and event metrics for the story

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
apiInstance.storyIdAnalytics(id, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## storyIdDelete

> storyIdDelete(id)

Story: Delete by Id

Remove a story and dependant data.

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
apiInstance.storyIdDelete(id, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdFileOoxmlautomationidDelete

> storyIdFileOoxmlautomationidDelete(id, ooxmlAutomationId)

Story: Delete Subdocument

Deletes a subdcoument of this story (e.g., .pptx, .docx, .xlsx)

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
let ooxmlAutomationId = "ooxmlAutomationId_example"; // String | the id of the ooxml_automation object
apiInstance.storyIdFileOoxmlautomationidDelete(id, ooxmlAutomationId, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **ooxmlAutomationId** | **String**| the id of the ooxml_automation object | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdFileOoxmlautomationidGet

> File storyIdFileOoxmlautomationidGet(id, ooxmlAutomationId)

Story: Download Updated File

Redtreives updated story as open office xml file (e.g., .pptx, .docx, .xlsx)

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
let ooxmlAutomationId = "ooxmlAutomationId_example"; // String | the id of the ooxml_automation object
apiInstance.storyIdFileOoxmlautomationidGet(id, ooxmlAutomationId, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **ooxmlAutomationId** | **String**| the id of the ooxml_automation object | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.openxmlformats-officedocument.presentationml.presentation, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/json


## storyIdFilePost

> Story storyIdFilePost(id, opts)

Story: Upload a File To Existing Story

Upload a file to an existing story

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
let opts = {
  'replaceExisting': true, // Boolean | Indicates whether a put or post method would replace the existing contents
  'obsoleteId': "obsoleteId_example", // String | A primary key pointing to an obsolete item in the story. Item type is context-dependent
  'includeOutline': true, // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
  'file': ["null"] // [File] | 
};
apiInstance.storyIdFilePost(id, opts, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **replaceExisting** | **Boolean**| Indicates whether a put or post method would replace the existing contents | [optional] 
 **obsoleteId** | **String**| A primary key pointing to an obsolete item in the story. Item type is context-dependent | [optional] 
 **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] 
 **file** | **[File]**|  | [optional] 

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## storyIdGet

> Story storyIdGet(id, opts)

Story: Get by Id

Returns story metadata, inlcuding json object with story outline

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
let opts = {
  'includeRelationships': true, // Boolean | Indicate whether the returned object should include child relationships
  'includeOutline': true, // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
  'full': true, // Boolean | Pull a story object with associated collaborator user, permission, and session data(faster if cached from prior api call)
  'refreshCache': true // Boolean | Force the api reload the `Story full` object
};
apiInstance.storyIdGet(id, opts, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **includeRelationships** | **Boolean**| Indicate whether the returned object should include child relationships | [optional] 
 **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] 
 **full** | **Boolean**| Pull a story object with associated collaborator user, permission, and session data(faster if cached from prior api call) | [optional] 
 **refreshCache** | **Boolean**| Force the api reload the &#x60;Story full&#x60; object | [optional] 

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdOutlineGet

> String storyIdOutlineGet(id)

Story: Get Story Outline

Returns Story&#39;s outline

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
apiInstance.storyIdOutlineGet(id, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdOutlinePost

> storyIdOutlinePost(id, body)

Story: Post Story Outline

Update a story outline.

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
let body = "body_example"; // String | A story outline object
apiInstance.storyIdOutlinePost(id, body, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **body** | **String**| A story outline object | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storyIdPublic

> String storyIdPublic(id)

Story: Public Link to Story Reveal.js Document

returns an html document containing a reveal.js epresentation of the story, if the story if set to is_public &#x3D; True

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
apiInstance.storyIdPublic(id, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdPut

> Story storyIdPut(id, story, opts)

Story: Modify

Update story metadata, including story outline

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
let story = new Story.Story(); // Story | The updated story object
let opts = {
  'includeOutline': true // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
};
apiInstance.storyIdPut(id, story, opts, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **story** | [**Story**](Story.md)| The updated story object | 
 **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] 

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storyIdReveal

> String storyIdReveal(id)

Story: Get Story at Reveal.js Document

returns an html document containing a reveal.js epresentation of the story

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
apiInstance.storyIdReveal(id, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## storyIdStatusGet

> Status storyIdStatusGet(id)

Story: Get Story Status

Returns code indicating whether story has active running background and is healthy (e.g., the latest outline is valid)

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let id = "id_example"; // String | the id from the story object
apiInstance.storyIdStatusGet(id, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyPost

> Story storyPost(outline, opts)

Story: Upload

Upload new story to presalytics api

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let outline = new Story.Outline(); // Outline | A story outline json object
let opts = {
  'includeOutline': true // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
};
apiInstance.storyPost(outline, opts, (error, data, response) => {
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
 **outline** | [**Outline**](Outline.md)| A story outline json object | 
 **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] 

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storyPostFile

> Story storyPostFile(opts)

Story: Upload a File

Upload new story to presalytics api via an Open Office Xml file

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let opts = {
  'includeOutline': true, // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
  'file': ["null"] // [File] | 
};
apiInstance.storyPostFile(opts, (error, data, response) => {
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
 **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] 
 **file** | **[File]**|  | [optional] 

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## storyPostFileJson

> Story storyPostFileJson(opts)

Story: Upload a File (base64)

Upload new story to presalytics api via an Open Office Xml file

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryApi();
let opts = {
  'includeOutline': true, // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
  'fileUpload': new Story.FileUpload() // FileUpload | A json-formatted object that includes a base64 encoded file (file encoded utf-8)
};
apiInstance.storyPostFileJson(opts, (error, data, response) => {
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
 **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] 
 **fileUpload** | [**FileUpload**](FileUpload.md)| A json-formatted object that includes a base64 encoded file (file encoded utf-8) | [optional] 

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


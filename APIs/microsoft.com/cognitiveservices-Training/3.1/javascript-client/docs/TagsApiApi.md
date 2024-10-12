# CustomVisionTrainingClient.TagsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.1/training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTag**](TagsApiApi.md#createTag) | **POST** /projects/{projectId}/tags | Create a tag for the project.
[**deleteTag**](TagsApiApi.md#deleteTag) | **DELETE** /projects/{projectId}/tags/{tagId} | Delete a tag from the project.
[**getTag**](TagsApiApi.md#getTag) | **GET** /projects/{projectId}/tags/{tagId} | Get information about a specific tag.
[**getTags**](TagsApiApi.md#getTags) | **GET** /projects/{projectId}/tags | Get the tags for a given project and iteration.
[**updateTag**](TagsApiApi.md#updateTag) | **PATCH** /projects/{projectId}/tags/{tagId} | Update a tag.



## createTag

> Tag createTag(projectId, name, trainingKey, opts)

Create a tag for the project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.TagsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let name = "Tag1"; // String | The tag name.
let trainingKey = "{API Key}"; // String | API key.
let opts = {
  'description': "Description of Tag1", // String | Optional description for the tag.
  'type': "type_example" // String | Optional type for the tag.
};
apiInstance.createTag(projectId, name, trainingKey, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **name** | **String**| The tag name. | 
 **trainingKey** | **String**| API key. | 
 **description** | **String**| Optional description for the tag. | [optional] 
 **type** | **String**| Optional type for the tag. | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## deleteTag

> deleteTag(projectId, tagId, trainingKey)

Delete a tag from the project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.TagsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let tagId = "9e27bc1b-7ae7-4e3b-a4e5-36153479dc01"; // String | Id of the tag to be deleted.
let trainingKey = "{API Key}"; // String | API key.
apiInstance.deleteTag(projectId, tagId, trainingKey, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **tagId** | **String**| Id of the tag to be deleted. | 
 **trainingKey** | **String**| API key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getTag

> Tag getTag(projectId, tagId, trainingKey, opts)

Get information about a specific tag.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.TagsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project this tag belongs to.
let tagId = "9e27bc1b-7ae7-4e3b-a4e5-36153479dc01"; // String | The tag id.
let trainingKey = "{API Key}"; // String | API key.
let opts = {
  'iterationId': "iterationId_example" // String | The iteration to retrieve this tag from. Optional, defaults to current training set.
};
apiInstance.getTag(projectId, tagId, trainingKey, opts, (error, data, response) => {
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
 **projectId** | **String**| The project this tag belongs to. | 
 **tagId** | **String**| The tag id. | 
 **trainingKey** | **String**| API key. | 
 **iterationId** | **String**| The iteration to retrieve this tag from. Optional, defaults to current training set. | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getTags

> [Tag] getTags(projectId, trainingKey, opts)

Get the tags for a given project and iteration.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.TagsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let trainingKey = "{API Key}"; // String | API key.
let opts = {
  'iterationId': "iterationId_example" // String | The iteration id. Defaults to workspace.
};
apiInstance.getTags(projectId, trainingKey, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **trainingKey** | **String**| API key. | 
 **iterationId** | **String**| The iteration id. Defaults to workspace. | [optional] 

### Return type

[**[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## updateTag

> Tag updateTag(projectId, tagId, trainingKey, tag)

Update a tag.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';

let apiInstance = new CustomVisionTrainingClient.TagsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let tagId = "9e27bc1b-7ae7-4e3b-a4e5-36153479dc01"; // String | The id of the target tag.
let trainingKey = "{API Key}"; // String | API key.
let tag = new CustomVisionTrainingClient.Tag(); // Tag | The updated tag model.
apiInstance.updateTag(projectId, tagId, trainingKey, tag, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **tagId** | **String**| The id of the target tag. | 
 **trainingKey** | **String**| API key. | 
 **tag** | [**Tag**](Tag.md)| The updated tag model. | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


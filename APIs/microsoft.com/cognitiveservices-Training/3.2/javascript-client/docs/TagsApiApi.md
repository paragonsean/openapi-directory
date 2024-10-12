# CustomVisionTrainingClient.TagsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTag**](TagsApiApi.md#createTag) | **POST** /projects/{projectId}/tags | Create a tag for the project.
[**deleteTag**](TagsApiApi.md#deleteTag) | **DELETE** /projects/{projectId}/tags/{tagId} | Delete a tag from the project.
[**getTag**](TagsApiApi.md#getTag) | **GET** /projects/{projectId}/tags/{tagId} | Get information about a specific tag.
[**getTags**](TagsApiApi.md#getTags) | **GET** /projects/{projectId}/tags | Get the tags for a given project and iteration.
[**updateTag**](TagsApiApi.md#updateTag) | **PATCH** /projects/{projectId}/tags/{tagId} | Update a tag.



## createTag

> Tag createTag(projectId, name, opts)

Create a tag for the project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.TagsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let name = "Tag1"; // String | The tag name.
let opts = {
  'description': "Description of Tag1", // String | Optional description for the tag.
  'type': "type_example" // String | Optional type for the tag.
};
apiInstance.createTag(projectId, name, opts, (error, data, response) => {
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
 **description** | **String**| Optional description for the tag. | [optional] 
 **type** | **String**| Optional type for the tag. | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## deleteTag

> deleteTag(projectId, tagId)

Delete a tag from the project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.TagsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let tagId = "9e27bc1b-7ae7-4e3b-a4e5-36153479dc01"; // String | Id of the tag to be deleted.
apiInstance.deleteTag(projectId, tagId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getTag

> Tag getTag(projectId, tagId, opts)

Get information about a specific tag.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.TagsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project this tag belongs to.
let tagId = "9e27bc1b-7ae7-4e3b-a4e5-36153479dc01"; // String | The tag id.
let opts = {
  'iterationId': "iterationId_example" // String | The iteration to retrieve this tag from. Optional, defaults to current training set.
};
apiInstance.getTag(projectId, tagId, opts, (error, data, response) => {
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
 **iterationId** | **String**| The iteration to retrieve this tag from. Optional, defaults to current training set. | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getTags

> [Tag] getTags(projectId, opts)

Get the tags for a given project and iteration.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.TagsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let opts = {
  'iterationId': "iterationId_example" // String | The iteration id. Defaults to workspace.
};
apiInstance.getTags(projectId, opts, (error, data, response) => {
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
 **iterationId** | **String**| The iteration id. Defaults to workspace. | [optional] 

### Return type

[**[Tag]**](Tag.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## updateTag

> Tag updateTag(projectId, tagId, tag)

Update a tag.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.TagsApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let tagId = "9e27bc1b-7ae7-4e3b-a4e5-36153479dc01"; // String | The id of the target tag.
let tag = new CustomVisionTrainingClient.Tag(); // Tag | The updated tag model.
apiInstance.updateTag(projectId, tagId, tag, (error, data, response) => {
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
 **tag** | [**Tag**](Tag.md)| The updated tag model. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


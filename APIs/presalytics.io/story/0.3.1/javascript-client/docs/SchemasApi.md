# Story.SchemasApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storyOutlineSchema**](SchemasApi.md#storyOutlineSchema) | **GET** /outline-schema/{schema_version}/story-outline.json | Story Outline Schema



## storyOutlineSchema

> storyOutlineSchema(schemaVersion)

Story Outline Schema

Json Schema for validating Story Outline objects

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.SchemasApi();
let schemaVersion = "schemaVersion_example"; // String | The semanitic version of a schema (e.g. '0.3.1')
apiInstance.storyOutlineSchema(schemaVersion, (error, data, response) => {
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
 **schemaVersion** | **String**| The semanitic version of a schema (e.g. &#39;0.3.1&#39;) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


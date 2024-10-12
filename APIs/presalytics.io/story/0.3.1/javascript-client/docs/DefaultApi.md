# Story.DefaultApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEnvironment**](DefaultApi.md#getEnvironment) | **GET** /environment/ | Environment: Get
[**specNoTags**](DefaultApi.md#specNoTags) | **GET** /no_tags_spec | Specification: No tags



## getEnvironment

> Object getEnvironment()

Environment: Get

pass rendering metadata to the client-side scripts

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.DefaultApi();
apiInstance.getEnvironment((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## specNoTags

> specNoTags()

Specification: No tags

json-formatted version of this spec with the tags removed to help with codegen processes

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.DefaultApi();
apiInstance.specNoTags((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


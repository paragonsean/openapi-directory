# Learnifier.CourseDesignsApi

All URIs are relative to *http://learnifier.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coursedesignsGet**](CourseDesignsApi.md#coursedesignsGet) | **GET** /coursedesigns | Lists all global course design templates



## coursedesignsGet

> [CourseDesign] coursedesignsGet()

Lists all global course design templates

Lists all global course design templates. Only api callers that have full access can call this method.

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.CourseDesignsApi();
apiInstance.coursedesignsGet((error, data, response) => {
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

[**[CourseDesign]**](CourseDesign.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# VsApi.DefaultApi

All URIs are relative to *https://api-vs.herokuapp.com/vs/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesGet**](DefaultApi.md#resourcesGet) | **GET** /resources | Fetch all meanings that contain a specific English string



## resourcesGet

> resourcesGet(description)

Fetch all meanings that contain a specific English string

### Example

```javascript
import VsApi from 'vs_api';

let apiInstance = new VsApi.DefaultApi();
let description = "description_example"; // String | The string you are looking for in the word meaning, for example, chariot. Wildcards are allowed, for example, char\\*.
apiInstance.resourcesGet(description, (error, data, response) => {
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
 **description** | **String**| The string you are looking for in the word meaning, for example, chariot. Wildcards are allowed, for example, char\\*. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


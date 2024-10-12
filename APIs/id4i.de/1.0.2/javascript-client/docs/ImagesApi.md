# Id4iApi.ImagesApi

All URIs are relative to *http://backend.id4i.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolveImageUsingGET**](ImagesApi.md#resolveImageUsingGET) | **GET** /api/v1/public/image/{imageID} | Resolve image



## resolveImageUsingGET

> Blob resolveImageUsingGET(imageID)

Resolve image

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.ImagesApi();
let imageID = "imageID_example"; // String | The id of the image to be resolved.
apiInstance.resolveImageUsingGET(imageID, (error, data, response) => {
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
 **imageID** | **String**| The id of the image to be resolved. | 

### Return type

**Blob**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


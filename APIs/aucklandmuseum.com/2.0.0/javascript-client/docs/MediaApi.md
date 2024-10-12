# AucklandMuseumApi.MediaApi

All URIs are relative to *http://api.aucklandmuseum.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMedia**](MediaApi.md#getMedia) | **GET** /id/media/{path} | Retrieve media associated with Collections and Cenotaph subjects in Auckland Museum



## getMedia

> getMedia(path, opts)

Retrieve media associated with Collections and Cenotaph subjects in Auckland Museum

Gets &#x60;media&#x60; at a given path 

### Example

```javascript
import AucklandMuseumApi from 'auckland_museum_api';

let apiInstance = new AucklandMuseumApi.MediaApi();
let path = "path_example"; // String | The media `identifier` 
let opts = {
  'rendering': "rendering_example" // String | The desired media `rendering`  Possible values: * `original.jpg` * `original.pdf` * `thumbnail.jpg` (fixed with 70px) * `standard.jpg` (fixed width 440px and height 440px) * `preview.jpg` (fixed height 100px) 
};
apiInstance.getMedia(path, opts, (error, data, response) => {
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
 **path** | **String**| The media &#x60;identifier&#x60;  | 
 **rendering** | **String**| The desired media &#x60;rendering&#x60;  Possible values: * &#x60;original.jpg&#x60; * &#x60;original.pdf&#x60; * &#x60;thumbnail.jpg&#x60; (fixed with 70px) * &#x60;standard.jpg&#x60; (fixed width 440px and height 440px) * &#x60;preview.jpg&#x60; (fixed height 100px)  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


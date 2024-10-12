# PaccurateIo.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rootPost**](DefaultApi.md#rootPost) | **POST** / | 



## rootPost

> PackResponse rootPost(opts)



a pure-JSON endpoint for packing requests. 

### Example

```javascript
import PaccurateIo from 'paccurate_io';

let apiInstance = new PaccurateIo.DefaultApi();
let opts = {
  'pack': new PaccurateIo.Pack() // Pack | complete set of items, boxes, and parameters to pack.
};
apiInstance.rootPost(opts, (error, data, response) => {
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
 **pack** | [**Pack**](Pack.md)| complete set of items, boxes, and parameters to pack. | [optional] 

### Return type

[**PackResponse**](PackResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


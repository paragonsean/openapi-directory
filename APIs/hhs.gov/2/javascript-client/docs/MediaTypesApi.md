# HhsMediaServicesApi.MediaTypesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesMediaTypesFormatGet**](MediaTypesApi.md#resourcesMediaTypesFormatGet) | **GET** /resources/mediaTypes.{format} | Get MediaTypes



## resourcesMediaTypesFormatGet

> [MediaTypeHolderWrapped] resourcesMediaTypesFormatGet(format)

Get MediaTypes

Information about media types

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaTypesApi();
let format = "format_example"; // String | Automatically added
apiInstance.resourcesMediaTypesFormatGet(format, (error, data, response) => {
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
 **format** | **String**| Automatically added | 

### Return type

[**[MediaTypeHolderWrapped]**](MediaTypeHolderWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


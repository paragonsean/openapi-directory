# SlideRoomApiV2.ExportApi

All URIs are relative to *https://api.slideroom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exportGetV2**](ExportApi.md#exportGetV2) | **GET** /api/v2/export/{token} | Gets the status/result of a requested export.



## exportGetV2

> ExportResultV2 exportGetV2(token)

Gets the status/result of a requested export.

### Example

```javascript
import SlideRoomApiV2 from 'slide_room_api_v2';

let apiInstance = new SlideRoomApiV2.ExportApi();
let token = 56; // Number | 
apiInstance.exportGetV2(token, (error, data, response) => {
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
 **token** | **Number**|  | 

### Return type

[**ExportResultV2**](ExportResultV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


# OoxmlAutomation.SlidesSlideMastersApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slidesSlidemastersGetId**](SlidesSlideMastersApi.md#slidesSlidemastersGetId) | **GET** /Slides/SlideMasters/{id} | SlideMasters: Get by Id



## slidesSlidemastersGetId

> SlideSlideMasters slidesSlidemastersGetId(id)

SlideMasters: Get by Id

Get by Id: Use this method to retrieve a SlideMasters object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SlidesSlideMastersApi();
let id = "id_example"; // String | 
apiInstance.slidesSlidemastersGetId(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**SlideSlideMasters**](SlideSlideMasters.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


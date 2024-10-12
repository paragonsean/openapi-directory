# OoxmlAutomation.SlidesGraphicsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slidesGraphicsGetId**](SlidesGraphicsApi.md#slidesGraphicsGetId) | **GET** /Slides/Graphics/{id} | Graphics: Get by Id



## slidesGraphicsGetId

> SlideGraphics slidesGraphicsGetId(id)

Graphics: Get by Id

Get by Id: Use this method to retrieve a Graphics object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SlidesGraphicsApi();
let id = "id_example"; // String | 
apiInstance.slidesGraphicsGetId(id, (error, data, response) => {
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

[**SlideGraphics**](SlideGraphics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


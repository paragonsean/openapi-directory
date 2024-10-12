# OoxmlAutomation.SlidesColorMapsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slidesColormapsGetId**](SlidesColorMapsApi.md#slidesColormapsGetId) | **GET** /Slides/ColorMaps/{id} | ColorMaps: Get by Id



## slidesColormapsGetId

> SlideColorMaps slidesColormapsGetId(id)

ColorMaps: Get by Id

Get by Id: Use this method to retrieve a ColorMaps object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SlidesColorMapsApi();
let id = "id_example"; // String | 
apiInstance.slidesColormapsGetId(id, (error, data, response) => {
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

[**SlideColorMaps**](SlideColorMaps.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


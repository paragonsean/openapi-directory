# OoxmlAutomation.SlidesGroupElementsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slidesGroupelementsGetId**](SlidesGroupElementsApi.md#slidesGroupelementsGetId) | **GET** /Slides/GroupElements/{id} | GroupElements: Get by Id



## slidesGroupelementsGetId

> SlideGroupElements slidesGroupelementsGetId(id)

GroupElements: Get by Id

Get by Id: Use this method to retrieve a GroupElements object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SlidesGroupElementsApi();
let id = "id_example"; // String | 
apiInstance.slidesGroupelementsGetId(id, (error, data, response) => {
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

[**SlideGroupElements**](SlideGroupElements.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


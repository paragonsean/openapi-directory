# OoxmlAutomation.SlidesGraphicTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slidesGraphictypesGet**](SlidesGraphicTypesApi.md#slidesGraphictypesGet) | **GET** /Slides/GraphicTypes | GraphicTypes: List All Possible Types
[**slidesGraphictypesGetId**](SlidesGraphicTypesApi.md#slidesGraphictypesGetId) | **GET** /Slides/GraphicTypes/{id} | GraphicTypes: Get by Id
[**slidesGraphictypesTypeidGetTypeId**](SlidesGraphicTypesApi.md#slidesGraphictypesTypeidGetTypeId) | **GET** /Slides/GraphicTypes/TypeId/{type_id} | GraphicTypes: Get By Type Id



## slidesGraphictypesGet

> [SlideGraphicTypes] slidesGraphictypesGet()

GraphicTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the GraphicTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Slides object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SlidesGraphicTypesApi();
apiInstance.slidesGraphictypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[SlideGraphicTypes]**](SlideGraphicTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## slidesGraphictypesGetId

> SlideGraphicTypes slidesGraphictypesGetId(id)

GraphicTypes: Get by Id

Get by Id: Use this method to retrieve a GraphicTypes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SlidesGraphicTypesApi();
let id = "id_example"; // String | 
apiInstance.slidesGraphictypesGetId(id, (error, data, response) => {
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

[**SlideGraphicTypes**](SlideGraphicTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## slidesGraphictypesTypeidGetTypeId

> SlideGraphicTypes slidesGraphictypesTypeidGetTypeId(typeId)

GraphicTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SlidesGraphicTypesApi();
let typeId = 56; // Number | 
apiInstance.slidesGraphictypesTypeidGetTypeId(typeId, (error, data, response) => {
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
 **typeId** | **Number**|  | 

### Return type

[**SlideGraphicTypes**](SlideGraphicTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


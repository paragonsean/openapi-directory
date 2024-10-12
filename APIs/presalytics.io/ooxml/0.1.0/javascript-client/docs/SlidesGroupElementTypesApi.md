# OoxmlAutomation.SlidesGroupElementTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slidesGroupelementtypesGet**](SlidesGroupElementTypesApi.md#slidesGroupelementtypesGet) | **GET** /Slides/GroupElementTypes | GroupElementTypes: List All Possible Types
[**slidesGroupelementtypesGetId**](SlidesGroupElementTypesApi.md#slidesGroupelementtypesGetId) | **GET** /Slides/GroupElementTypes/{id} | GroupElementTypes: Get by Id
[**slidesGroupelementtypesTypeidGetTypeId**](SlidesGroupElementTypesApi.md#slidesGroupelementtypesTypeidGetTypeId) | **GET** /Slides/GroupElementTypes/TypeId/{type_id} | GroupElementTypes: Get By Type Id



## slidesGroupelementtypesGet

> [SlideGroupElementTypes] slidesGroupelementtypesGet()

GroupElementTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the GroupElementTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Slides object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SlidesGroupElementTypesApi();
apiInstance.slidesGroupelementtypesGet((error, data, response) => {
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

[**[SlideGroupElementTypes]**](SlideGroupElementTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## slidesGroupelementtypesGetId

> SlideGroupElementTypes slidesGroupelementtypesGetId(id)

GroupElementTypes: Get by Id

Get by Id: Use this method to retrieve a GroupElementTypes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SlidesGroupElementTypesApi();
let id = "id_example"; // String | 
apiInstance.slidesGroupelementtypesGetId(id, (error, data, response) => {
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

[**SlideGroupElementTypes**](SlideGroupElementTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## slidesGroupelementtypesTypeidGetTypeId

> SlideGroupElementTypes slidesGroupelementtypesTypeidGetTypeId(typeId)

GroupElementTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SlidesGroupElementTypesApi();
let typeId = 56; // Number | 
apiInstance.slidesGroupelementtypesTypeidGetTypeId(typeId, (error, data, response) => {
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

[**SlideGroupElementTypes**](SlideGroupElementTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


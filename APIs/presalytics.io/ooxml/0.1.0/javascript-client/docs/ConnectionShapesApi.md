# OoxmlAutomation.ConnectionShapesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slidesConnectionshapesChildobjectsGetId**](ConnectionShapesApi.md#slidesConnectionshapesChildobjectsGetId) | **GET** /ConnectionShapes/ChildObjects/{id} | Slides: Get Dependent Objects Tree
[**slidesConnectionshapesDetailsGetId**](ConnectionShapesApi.md#slidesConnectionshapesDetailsGetId) | **GET** /ConnectionShapes/Details/{id} | Slides: Get Details
[**slidesConnectionshapesGetId**](ConnectionShapesApi.md#slidesConnectionshapesGetId) | **GET** /ConnectionShapes/{id} | ConnectionShapes: Get by Id
[**slidesConnectionshapesOpenofficexmlGetIdUpdated**](ConnectionShapesApi.md#slidesConnectionshapesOpenofficexmlGetIdUpdated) | **GET** /ConnectionShapes/OpenOfficeXml/{id} | Slides: Get Underlying Xml
[**slidesConnectionshapesOpenofficexmlPutId**](ConnectionShapesApi.md#slidesConnectionshapesOpenofficexmlPutId) | **PUT** /ConnectionShapes/OpenOfficeXml/{id} | Slides: Modify Underlying Xml
[**slidesConnectionshapesSvgGetIdUseCache**](ConnectionShapesApi.md#slidesConnectionshapesSvgGetIdUseCache) | **GET** /ConnectionShapes/Svg/{id} | Slides: Get Svg file



## slidesConnectionshapesChildobjectsGetId

> [ChildObjects] slidesConnectionshapesChildobjectsGetId(id)

Slides: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Slide and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ConnectionShapesApi();
let id = "id_example"; // String | 
apiInstance.slidesConnectionshapesChildobjectsGetId(id, (error, data, response) => {
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

[**[ChildObjects]**](ChildObjects.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## slidesConnectionshapesDetailsGetId

> SlideConnectorDetails slidesConnectionshapesDetailsGetId(id)

Slides: Get Details

Returns object metadata and information about relative dependent objects 

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ConnectionShapesApi();
let id = "id_example"; // String | 
apiInstance.slidesConnectionshapesDetailsGetId(id, (error, data, response) => {
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

[**SlideConnectorDetails**](SlideConnectorDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## slidesConnectionshapesGetId

> SlideConnector slidesConnectionshapesGetId(id)

ConnectionShapes: Get by Id

Get by Id: Use this method to retrieve a ConnectionShapes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ConnectionShapesApi();
let id = "id_example"; // String | An Id of the respository DTO elemennt
apiInstance.slidesConnectionshapesGetId(id, (error, data, response) => {
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
 **id** | **String**| An Id of the respository DTO elemennt | 

### Return type

[**SlideConnector**](SlideConnector.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## slidesConnectionshapesOpenofficexmlGetIdUpdated

> OoxmlDTO slidesConnectionshapesOpenofficexmlGetIdUpdated(id, opts)

Slides: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Slide object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Slide objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ConnectionShapesApi();
let id = "id_example"; // String | 
let opts = {
  'updated': true // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
};
apiInstance.slidesConnectionshapesOpenofficexmlGetIdUpdated(id, opts, (error, data, response) => {
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
 **updated** | **Boolean**| Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default) | [optional] [default to true]

### Return type

[**OoxmlDTO**](OoxmlDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## slidesConnectionshapesOpenofficexmlPutId

> slidesConnectionshapesOpenofficexmlPutId(id, opts)

Slides: Modify Underlying Xml

Directly eidt the underlying xml of a Slide object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Slide objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ConnectionShapesApi();
let id = "id_example"; // String | 
let opts = {
  'ooxmlDTO': new OoxmlAutomation.OoxmlDTO() // OoxmlDTO | 
};
apiInstance.slidesConnectionshapesOpenofficexmlPutId(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **ooxmlDTO** | [**OoxmlDTO**](OoxmlDTO.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## slidesConnectionshapesSvgGetIdUseCache

> File slidesConnectionshapesSvgGetIdUseCache(id, opts)

Slides: Get Svg file

This endpoint is helpful for rending this Slide as an svg or image object that can then be rendered in a story, dashboard or website.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ConnectionShapesApi();
let id = "id_example"; // String | 
let opts = {
  'useCache': false // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
};
apiInstance.slidesConnectionshapesSvgGetIdUseCache(id, opts, (error, data, response) => {
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
 **useCache** | **Boolean**| Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false) | [optional] [default to false]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/svg+xml, application/json


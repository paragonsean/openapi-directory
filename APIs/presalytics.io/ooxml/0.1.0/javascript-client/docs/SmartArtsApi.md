# OoxmlAutomation.SmartArtsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slidesSmartartsChildobjectsGetId**](SmartArtsApi.md#slidesSmartartsChildobjectsGetId) | **GET** /SmartArts/ChildObjects/{id} | Slides: Get Dependent Objects Tree
[**slidesSmartartsDetailsGetId**](SmartArtsApi.md#slidesSmartartsDetailsGetId) | **GET** /SmartArts/Details/{id} | Slides: Get Details
[**slidesSmartartsGetId**](SmartArtsApi.md#slidesSmartartsGetId) | **GET** /SmartArts/{id} | SmartArts: Get by Id
[**slidesSmartartsOpenofficexmlGetIdUpdated**](SmartArtsApi.md#slidesSmartartsOpenofficexmlGetIdUpdated) | **GET** /SmartArts/OpenOfficeXml/{id} | Slides: Get Underlying Xml
[**slidesSmartartsOpenofficexmlPutId**](SmartArtsApi.md#slidesSmartartsOpenofficexmlPutId) | **PUT** /SmartArts/OpenOfficeXml/{id} | Slides: Modify Underlying Xml
[**slidesSmartartsSvgGetIdUseCache**](SmartArtsApi.md#slidesSmartartsSvgGetIdUseCache) | **GET** /SmartArts/Svg/{id} | Slides: Get Svg file



## slidesSmartartsChildobjectsGetId

> [ChildObjects] slidesSmartartsChildobjectsGetId(id)

Slides: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Slide and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SmartArtsApi();
let id = "id_example"; // String | 
apiInstance.slidesSmartartsChildobjectsGetId(id, (error, data, response) => {
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


## slidesSmartartsDetailsGetId

> SlideSmartArtsDetails slidesSmartartsDetailsGetId(id)

Slides: Get Details

Returns object metadata and information about relative dependent objects 

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SmartArtsApi();
let id = "id_example"; // String | 
apiInstance.slidesSmartartsDetailsGetId(id, (error, data, response) => {
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

[**SlideSmartArtsDetails**](SlideSmartArtsDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## slidesSmartartsGetId

> SlideSmartArts slidesSmartartsGetId(id)

SmartArts: Get by Id

Get by Id: Use this method to retrieve a SmartArts object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SmartArtsApi();
let id = "id_example"; // String | An Id of the respository DTO elemennt
apiInstance.slidesSmartartsGetId(id, (error, data, response) => {
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

[**SlideSmartArts**](SlideSmartArts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## slidesSmartartsOpenofficexmlGetIdUpdated

> OoxmlDTO slidesSmartartsOpenofficexmlGetIdUpdated(id, opts)

Slides: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Slide object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Slide objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SmartArtsApi();
let id = "id_example"; // String | 
let opts = {
  'updated': true // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
};
apiInstance.slidesSmartartsOpenofficexmlGetIdUpdated(id, opts, (error, data, response) => {
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


## slidesSmartartsOpenofficexmlPutId

> slidesSmartartsOpenofficexmlPutId(id, opts)

Slides: Modify Underlying Xml

Directly eidt the underlying xml of a Slide object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Slide objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SmartArtsApi();
let id = "id_example"; // String | 
let opts = {
  'ooxmlDTO': new OoxmlAutomation.OoxmlDTO() // OoxmlDTO | 
};
apiInstance.slidesSmartartsOpenofficexmlPutId(id, opts, (error, data, response) => {
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


## slidesSmartartsSvgGetIdUseCache

> File slidesSmartartsSvgGetIdUseCache(id, opts)

Slides: Get Svg file

This endpoint is helpful for rending this Slide as an svg or image object that can then be rendered in a story, dashboard or website.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SmartArtsApi();
let id = "id_example"; // String | 
let opts = {
  'useCache': false // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
};
apiInstance.slidesSmartartsSvgGetIdUseCache(id, opts, (error, data, response) => {
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


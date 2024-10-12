# OoxmlAutomation.ImagesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedImagesChildobjectsGetId**](ImagesApi.md#sharedImagesChildobjectsGetId) | **GET** /Images/ChildObjects/{id} | Shared: Get Dependent Objects Tree
[**sharedImagesDetailsGetId**](ImagesApi.md#sharedImagesDetailsGetId) | **GET** /Images/Details/{id} | Shared: Get Details
[**sharedImagesGetId**](ImagesApi.md#sharedImagesGetId) | **GET** /Images/{id} | Images: Get by Id
[**sharedImagesGetimagePutId**](ImagesApi.md#sharedImagesGetimagePutId) | **PUT** /Images/GetImage/{Id} | Image: Download Image
[**sharedImagesOpenofficexmlGetIdUpdated**](ImagesApi.md#sharedImagesOpenofficexmlGetIdUpdated) | **GET** /Images/OpenOfficeXml/{id} | Shared: Get Underlying Xml
[**sharedImagesOpenofficexmlPutId**](ImagesApi.md#sharedImagesOpenofficexmlPutId) | **PUT** /Images/OpenOfficeXml/{id} | Shared: Modify Underlying Xml
[**sharedImagesSvgGetIdUseCache**](ImagesApi.md#sharedImagesSvgGetIdUseCache) | **GET** /Images/Svg/{id} | Shared: Get Svg file



## sharedImagesChildobjectsGetId

> [ChildObjects] sharedImagesChildobjectsGetId(id)

Shared: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Shared and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ImagesApi();
let id = "id_example"; // String | 
apiInstance.sharedImagesChildobjectsGetId(id, (error, data, response) => {
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


## sharedImagesDetailsGetId

> SharedPicturesDetails sharedImagesDetailsGetId(id)

Shared: Get Details

Returns object metadata and information about relative dependent objects 

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ImagesApi();
let id = "id_example"; // String | 
apiInstance.sharedImagesDetailsGetId(id, (error, data, response) => {
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

[**SharedPicturesDetails**](SharedPicturesDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharedImagesGetId

> SharedPictures sharedImagesGetId(id)

Images: Get by Id

Get by Id: Use this method to retrieve a Images object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ImagesApi();
let id = "id_example"; // String | An Id of the respository DTO elemennt
apiInstance.sharedImagesGetId(id, (error, data, response) => {
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

[**SharedPictures**](SharedPictures.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharedImagesGetimagePutId

> sharedImagesGetimagePutId(id)

Image: Download Image

Download Images extracted from Ooxml Documents

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ImagesApi();
let id = "id_example"; // String | The Image Id
apiInstance.sharedImagesGetimagePutId(id, (error, data, response) => {
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
 **id** | **String**| The Image Id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharedImagesOpenofficexmlGetIdUpdated

> OoxmlDTO sharedImagesOpenofficexmlGetIdUpdated(id, opts)

Shared: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Shared object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Shared objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ImagesApi();
let id = "id_example"; // String | 
let opts = {
  'updated': true // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
};
apiInstance.sharedImagesOpenofficexmlGetIdUpdated(id, opts, (error, data, response) => {
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


## sharedImagesOpenofficexmlPutId

> sharedImagesOpenofficexmlPutId(id, opts)

Shared: Modify Underlying Xml

Directly eidt the underlying xml of a Shared object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Shared objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ImagesApi();
let id = "id_example"; // String | 
let opts = {
  'ooxmlDTO': new OoxmlAutomation.OoxmlDTO() // OoxmlDTO | 
};
apiInstance.sharedImagesOpenofficexmlPutId(id, opts, (error, data, response) => {
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


## sharedImagesSvgGetIdUseCache

> File sharedImagesSvgGetIdUseCache(id, opts)

Shared: Get Svg file

This endpoint is helpful for rending this Shared as an svg or image object that can then be rendered in a story, dashboard or website.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ImagesApi();
let id = "id_example"; // String | 
let opts = {
  'useCache': false // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
};
apiInstance.sharedImagesSvgGetIdUseCache(id, opts, (error, data, response) => {
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


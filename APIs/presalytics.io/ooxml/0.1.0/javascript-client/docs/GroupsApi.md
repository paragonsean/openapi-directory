# OoxmlAutomation.GroupsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slidesGroupsChildobjectsGetId**](GroupsApi.md#slidesGroupsChildobjectsGetId) | **GET** /Groups/ChildObjects/{id} | Slides: Get Dependent Objects Tree
[**slidesGroupsDetailsGetId**](GroupsApi.md#slidesGroupsDetailsGetId) | **GET** /Groups/Details/{id} | Slides: Get Details
[**slidesGroupsGetId**](GroupsApi.md#slidesGroupsGetId) | **GET** /Groups/{id} | Groups: Get by Id
[**slidesGroupsOpenofficexmlGetIdUpdated**](GroupsApi.md#slidesGroupsOpenofficexmlGetIdUpdated) | **GET** /Groups/OpenOfficeXml/{id} | Slides: Get Underlying Xml
[**slidesGroupsOpenofficexmlPutId**](GroupsApi.md#slidesGroupsOpenofficexmlPutId) | **PUT** /Groups/OpenOfficeXml/{id} | Slides: Modify Underlying Xml
[**slidesGroupsSvgGetIdUseCache**](GroupsApi.md#slidesGroupsSvgGetIdUseCache) | **GET** /Groups/Svg/{id} | Slides: Get Svg file



## slidesGroupsChildobjectsGetId

> [ChildObjects] slidesGroupsChildobjectsGetId(id)

Slides: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Slide and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.GroupsApi();
let id = "id_example"; // String | 
apiInstance.slidesGroupsChildobjectsGetId(id, (error, data, response) => {
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


## slidesGroupsDetailsGetId

> SlideGroupsDetails slidesGroupsDetailsGetId(id)

Slides: Get Details

Returns object metadata and information about relative dependent objects 

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.GroupsApi();
let id = "id_example"; // String | 
apiInstance.slidesGroupsDetailsGetId(id, (error, data, response) => {
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

[**SlideGroupsDetails**](SlideGroupsDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## slidesGroupsGetId

> SlideGroups slidesGroupsGetId(id)

Groups: Get by Id

Get by Id: Use this method to retrieve a Groups object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.GroupsApi();
let id = "id_example"; // String | An Id of the respository DTO elemennt
apiInstance.slidesGroupsGetId(id, (error, data, response) => {
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

[**SlideGroups**](SlideGroups.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## slidesGroupsOpenofficexmlGetIdUpdated

> OoxmlDTO slidesGroupsOpenofficexmlGetIdUpdated(id, opts)

Slides: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Slide object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Slide objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.GroupsApi();
let id = "id_example"; // String | 
let opts = {
  'updated': true // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
};
apiInstance.slidesGroupsOpenofficexmlGetIdUpdated(id, opts, (error, data, response) => {
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


## slidesGroupsOpenofficexmlPutId

> slidesGroupsOpenofficexmlPutId(id, opts)

Slides: Modify Underlying Xml

Directly eidt the underlying xml of a Slide object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Slide objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.GroupsApi();
let id = "id_example"; // String | 
let opts = {
  'ooxmlDTO': new OoxmlAutomation.OoxmlDTO() // OoxmlDTO | 
};
apiInstance.slidesGroupsOpenofficexmlPutId(id, opts, (error, data, response) => {
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


## slidesGroupsSvgGetIdUseCache

> File slidesGroupsSvgGetIdUseCache(id, opts)

Slides: Get Svg file

This endpoint is helpful for rending this Slide as an svg or image object that can then be rendered in a story, dashboard or website.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.GroupsApi();
let id = "id_example"; // String | 
let opts = {
  'useCache': false // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
};
apiInstance.slidesGroupsSvgGetIdUseCache(id, opts, (error, data, response) => {
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


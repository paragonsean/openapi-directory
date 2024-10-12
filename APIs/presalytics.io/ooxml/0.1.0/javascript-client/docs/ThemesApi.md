# OoxmlAutomation.ThemesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**themeThemesChildobjectsGetId**](ThemesApi.md#themeThemesChildobjectsGetId) | **GET** /Themes/ChildObjects/{id} | Theme: Get Dependent Objects Tree
[**themeThemesDetailsGetId**](ThemesApi.md#themeThemesDetailsGetId) | **GET** /Themes/Details/{id} | Theme: Get Details
[**themeThemesGetId**](ThemesApi.md#themeThemesGetId) | **GET** /Themes/{id} | Themes: Get by Id
[**themeThemesOpenofficexmlGetIdUpdated**](ThemesApi.md#themeThemesOpenofficexmlGetIdUpdated) | **GET** /Themes/OpenOfficeXml/{id} | Theme: Get Underlying Xml
[**themeThemesOpenofficexmlPutId**](ThemesApi.md#themeThemesOpenofficexmlPutId) | **PUT** /Themes/OpenOfficeXml/{id} | Theme: Modify Underlying Xml
[**themeThemesSvgGetIdUseCache**](ThemesApi.md#themeThemesSvgGetIdUseCache) | **GET** /Themes/Svg/{id} | Theme: Get Svg file



## themeThemesChildobjectsGetId

> [ChildObjects] themeThemesChildobjectsGetId(id)

Theme: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Theme and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesApi();
let id = "id_example"; // String | 
apiInstance.themeThemesChildobjectsGetId(id, (error, data, response) => {
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


## themeThemesDetailsGetId

> ThemeThemesDetails themeThemesDetailsGetId(id)

Theme: Get Details

Returns object metadata and information about relative dependent objects 

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesApi();
let id = "id_example"; // String | 
apiInstance.themeThemesDetailsGetId(id, (error, data, response) => {
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

[**ThemeThemesDetails**](ThemeThemesDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## themeThemesGetId

> ThemeThemes themeThemesGetId(id)

Themes: Get by Id

Get by Id: Use this method to retrieve a Themes object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesApi();
let id = "id_example"; // String | An Id of the respository DTO elemennt
apiInstance.themeThemesGetId(id, (error, data, response) => {
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

[**ThemeThemes**](ThemeThemes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## themeThemesOpenofficexmlGetIdUpdated

> OoxmlDTO themeThemesOpenofficexmlGetIdUpdated(id, opts)

Theme: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Theme object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Theme objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesApi();
let id = "id_example"; // String | 
let opts = {
  'updated': true // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
};
apiInstance.themeThemesOpenofficexmlGetIdUpdated(id, opts, (error, data, response) => {
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


## themeThemesOpenofficexmlPutId

> themeThemesOpenofficexmlPutId(id, opts)

Theme: Modify Underlying Xml

Directly eidt the underlying xml of a Theme object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Theme objects.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesApi();
let id = "id_example"; // String | 
let opts = {
  'ooxmlDTO': new OoxmlAutomation.OoxmlDTO() // OoxmlDTO | 
};
apiInstance.themeThemesOpenofficexmlPutId(id, opts, (error, data, response) => {
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


## themeThemesSvgGetIdUseCache

> File themeThemesSvgGetIdUseCache(id, opts)

Theme: Get Svg file

This endpoint is helpful for rending this Theme as an svg or image object that can then be rendered in a story, dashboard or website.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesApi();
let id = "id_example"; // String | 
let opts = {
  'useCache': false // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
};
apiInstance.themeThemesSvgGetIdUseCache(id, opts, (error, data, response) => {
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


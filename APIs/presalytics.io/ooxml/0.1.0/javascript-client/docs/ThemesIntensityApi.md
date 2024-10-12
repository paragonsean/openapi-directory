# OoxmlAutomation.ThemesIntensityApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**themesIntensityGet**](ThemesIntensityApi.md#themesIntensityGet) | **GET** /Themes/Intensity | Intensity: List All Possible Types
[**themesIntensityGetId**](ThemesIntensityApi.md#themesIntensityGetId) | **GET** /Themes/Intensity/{id} | Intensity: Get by Id
[**themesIntensityTypeidGetTypeId**](ThemesIntensityApi.md#themesIntensityTypeidGetTypeId) | **GET** /Themes/Intensity/TypeId/{type_id} | Intensity: Get By Type Id



## themesIntensityGet

> [ThemeIntensity] themesIntensityGet()

Intensity: List All Possible Types

List Types: Use this method to retreive a list of possible options for the Intensity type. Use the Id from oneof the returned elements on to make changes to elements in the Themes object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesIntensityApi();
apiInstance.themesIntensityGet((error, data, response) => {
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

[**[ThemeIntensity]**](ThemeIntensity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## themesIntensityGetId

> ThemeIntensity themesIntensityGetId(id)

Intensity: Get by Id

Get by Id: Use this method to retrieve a Intensity object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesIntensityApi();
let id = "id_example"; // String | 
apiInstance.themesIntensityGetId(id, (error, data, response) => {
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

[**ThemeIntensity**](ThemeIntensity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## themesIntensityTypeidGetTypeId

> ThemeIntensity themesIntensityTypeidGetTypeId(typeId)

Intensity: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesIntensityApi();
let typeId = 56; // Number | 
apiInstance.themesIntensityTypeidGetTypeId(typeId, (error, data, response) => {
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

[**ThemeIntensity**](ThemeIntensity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


# OoxmlAutomation.ThemesEffectMapApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**themesEffectmapGetId**](ThemesEffectMapApi.md#themesEffectmapGetId) | **GET** /Themes/EffectMap/{id} | EffectMap: Get by Id



## themesEffectmapGetId

> ThemeEffectMap themesEffectmapGetId(id)

EffectMap: Get by Id

Get by Id: Use this method to retrieve a EffectMap object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesEffectMapApi();
let id = "id_example"; // String | 
apiInstance.themesEffectmapGetId(id, (error, data, response) => {
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

[**ThemeEffectMap**](ThemeEffectMap.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


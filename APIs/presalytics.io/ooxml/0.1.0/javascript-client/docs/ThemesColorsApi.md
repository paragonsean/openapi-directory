# OoxmlAutomation.ThemesColorsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**themesColorsGetId**](ThemesColorsApi.md#themesColorsGetId) | **GET** /Themes/Colors/{id} | Colors: Get by Id



## themesColorsGetId

> ThemeColors themesColorsGetId(id)

Colors: Get by Id

Get by Id: Use this method to retrieve a Colors object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesColorsApi();
let id = "id_example"; // String | 
apiInstance.themesColorsGetId(id, (error, data, response) => {
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

[**ThemeColors**](ThemeColors.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


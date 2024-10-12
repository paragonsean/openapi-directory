# OoxmlAutomation.ThemesCustomColorsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**themesCustomcolorsGetId**](ThemesCustomColorsApi.md#themesCustomcolorsGetId) | **GET** /Themes/CustomColors/{id} | CustomColors: Get by Id



## themesCustomcolorsGetId

> ThemeCustomColors themesCustomcolorsGetId(id)

CustomColors: Get by Id

Get by Id: Use this method to retrieve a CustomColors object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesCustomColorsApi();
let id = "id_example"; // String | 
apiInstance.themesCustomcolorsGetId(id, (error, data, response) => {
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

[**ThemeCustomColors**](ThemeCustomColors.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


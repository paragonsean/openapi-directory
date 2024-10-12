# OoxmlAutomation.ThemesLineMapApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**themesLinemapGetId**](ThemesLineMapApi.md#themesLinemapGetId) | **GET** /Themes/LineMap/{id} | LineMap: Get by Id



## themesLinemapGetId

> ThemeLineMap themesLinemapGetId(id)

LineMap: Get by Id

Get by Id: Use this method to retrieve a LineMap object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesLineMapApi();
let id = "id_example"; // String | 
apiInstance.themesLinemapGetId(id, (error, data, response) => {
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

[**ThemeLineMap**](ThemeLineMap.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


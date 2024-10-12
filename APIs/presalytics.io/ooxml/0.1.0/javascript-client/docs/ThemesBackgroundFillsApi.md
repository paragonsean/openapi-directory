# OoxmlAutomation.ThemesBackgroundFillsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**themesBackgroundfillsGetId**](ThemesBackgroundFillsApi.md#themesBackgroundfillsGetId) | **GET** /Themes/BackgroundFills/{id} | BackgroundFills: Get by Id



## themesBackgroundfillsGetId

> ThemeBackgroundFills themesBackgroundfillsGetId(id)

BackgroundFills: Get by Id

Get by Id: Use this method to retrieve a BackgroundFills object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.ThemesBackgroundFillsApi();
let id = "id_example"; // String | 
apiInstance.themesBackgroundfillsGetId(id, (error, data, response) => {
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

[**ThemeBackgroundFills**](ThemeBackgroundFills.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


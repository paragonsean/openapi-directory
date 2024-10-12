# LibreTranslate.FrontendApi

All URIs are relative to *http://libretranslate.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frontendSettingsGet**](FrontendApi.md#frontendSettingsGet) | **GET** /frontend/settings | Retrieve frontend specific settings



## frontendSettingsGet

> FrontendSettings frontendSettingsGet()

Retrieve frontend specific settings



### Example

```javascript
import LibreTranslate from 'libre_translate';

let apiInstance = new LibreTranslate.FrontendApi();
apiInstance.frontendSettingsGet((error, data, response) => {
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

[**FrontendSettings**](FrontendSettings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


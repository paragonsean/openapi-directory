# WireMock.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminResetPost**](SystemApi.md#adminResetPost) | **POST** /__admin/reset | Reset mappings and request journal
[**adminSettingsPost**](SystemApi.md#adminSettingsPost) | **POST** /__admin/settings | Update global settings
[**adminShutdownPost**](SystemApi.md#adminShutdownPost) | **POST** /__admin/shutdown | 



## adminResetPost

> adminResetPost()

Reset mappings and request journal

Reset mappings to the default state and reset the request journal

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.SystemApi();
apiInstance.adminResetPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## adminSettingsPost

> adminSettingsPost(adminSettingsPostRequest)

Update global settings

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.SystemApi();
let adminSettingsPostRequest = new WireMock.AdminSettingsPostRequest(); // AdminSettingsPostRequest | 
apiInstance.adminSettingsPost(adminSettingsPostRequest, (error, data, response) => {
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
 **adminSettingsPostRequest** | [**AdminSettingsPostRequest**](AdminSettingsPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## adminShutdownPost

> adminShutdownPost()



Shutdown the WireMock server

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.SystemApi();
apiInstance.adminShutdownPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


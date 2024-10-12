# WhatsAppBusinessApi.ProfileApi

All URIs are relative to *http://whatsapp.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProfileAbout**](ProfileApi.md#getProfileAbout) | **GET** /settings/profile/about | Get-Profile-About
[**getProfilePhoto**](ProfileApi.md#getProfilePhoto) | **GET** /settings/profile/photo | Get-Profile-Photo
[**updateProfileAbout**](ProfileApi.md#updateProfileAbout) | **PATCH** /settings/profile/about | Update-Profile-About
[**updateProfilePhoto**](ProfileApi.md#updateProfilePhoto) | **POST** /settings/profile/photo | Update-Profile-Photo



## getProfileAbout

> GetProfileAboutResponse getProfileAbout()

Get-Profile-About

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ProfileApi();
apiInstance.getProfileAbout((error, data, response) => {
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

[**GetProfileAboutResponse**](GetProfileAboutResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfilePhoto

> GetProfilePhotoResponse getProfilePhoto(opts)

Get-Profile-Photo

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ProfileApi();
let opts = {
  'format': "link" // String | 
};
apiInstance.getProfilePhoto(opts, (error, data, response) => {
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
 **format** | **String**|  | [optional] 

### Return type

[**GetProfilePhotoResponse**](GetProfilePhotoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, image/jpeg


## updateProfileAbout

> updateProfileAbout(profileAbout)

Update-Profile-About

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ProfileApi();
let profileAbout = {"text":"<About Profile>"}; // ProfileAbout | 
apiInstance.updateProfileAbout(profileAbout, (error, data, response) => {
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
 **profileAbout** | [**ProfileAbout**](ProfileAbout.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateProfilePhoto

> updateProfilePhoto(file)

Update-Profile-Photo

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ProfileApi();
let file = "/path/to/file"; // File | 
apiInstance.updateProfilePhoto(file, (error, data, response) => {
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
 **file** | **File**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


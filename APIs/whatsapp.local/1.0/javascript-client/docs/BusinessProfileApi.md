# WhatsAppBusinessApi.BusinessProfileApi

All URIs are relative to *http://whatsapp.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBusinessProfile**](BusinessProfileApi.md#getBusinessProfile) | **GET** /settings/business/profile | Get-Business-Profile
[**updateBusinessProfile**](BusinessProfileApi.md#updateBusinessProfile) | **POST** /settings/business/profile | Update-Business-Profile



## getBusinessProfile

> GetBusinessProfileResponse getBusinessProfile()

Get-Business-Profile

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.BusinessProfileApi();
apiInstance.getBusinessProfile((error, data, response) => {
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

[**GetBusinessProfileResponse**](GetBusinessProfileResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBusinessProfile

> updateBusinessProfile(businessProfile)

Update-Business-Profile

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.BusinessProfileApi();
let businessProfile = {"address":"<Business Profile Address>","description":"<Business Profile Description>","email":"<Business Profile Email>","vertical":"<Business Profile Vertical>","websites":["https://www.whatsapp.com","https://www.facebook.com"]}; // BusinessProfile | 
apiInstance.updateBusinessProfile(businessProfile, (error, data, response) => {
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
 **businessProfile** | [**BusinessProfile**](BusinessProfile.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


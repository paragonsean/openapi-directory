# TwilioMessaging.MessagingV1BrandVettingApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBrandVetting**](MessagingV1BrandVettingApi.md#createBrandVetting) | **POST** /v1/a2p/BrandRegistrations/{BrandSid}/Vettings | 
[**fetchBrandVetting**](MessagingV1BrandVettingApi.md#fetchBrandVetting) | **GET** /v1/a2p/BrandRegistrations/{BrandSid}/Vettings/{BrandVettingSid} | 
[**listBrandVetting**](MessagingV1BrandVettingApi.md#listBrandVetting) | **GET** /v1/a2p/BrandRegistrations/{BrandSid}/Vettings | 



## createBrandVetting

> MessagingV1BrandRegistrationsBrandVetting createBrandVetting(brandSid, vettingProvider, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1BrandVettingApi();
let brandSid = "brandSid_example"; // String | The SID of the Brand Registration resource of the vettings to create .
let vettingProvider = "vettingProvider_example"; // BrandVettingEnumVettingProvider | 
let opts = {
  'vettingId': "vettingId_example" // String | The unique ID of the vetting
};
apiInstance.createBrandVetting(brandSid, vettingProvider, opts, (error, data, response) => {
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
 **brandSid** | **String**| The SID of the Brand Registration resource of the vettings to create . | 
 **vettingProvider** | **BrandVettingEnumVettingProvider**|  | 
 **vettingId** | **String**| The unique ID of the vetting | [optional] 

### Return type

[**MessagingV1BrandRegistrationsBrandVetting**](MessagingV1BrandRegistrationsBrandVetting.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchBrandVetting

> MessagingV1BrandRegistrationsBrandVetting fetchBrandVetting(brandSid, brandVettingSid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1BrandVettingApi();
let brandSid = "brandSid_example"; // String | The SID of the Brand Registration resource of the vettings to read .
let brandVettingSid = "brandVettingSid_example"; // String | The Twilio SID of the third-party vetting record.
apiInstance.fetchBrandVetting(brandSid, brandVettingSid, (error, data, response) => {
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
 **brandSid** | **String**| The SID of the Brand Registration resource of the vettings to read . | 
 **brandVettingSid** | **String**| The Twilio SID of the third-party vetting record. | 

### Return type

[**MessagingV1BrandRegistrationsBrandVetting**](MessagingV1BrandRegistrationsBrandVetting.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBrandVetting

> ListBrandVettingResponse listBrandVetting(brandSid, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1BrandVettingApi();
let brandSid = "brandSid_example"; // String | The SID of the Brand Registration resource of the vettings to read .
let opts = {
  'vettingProvider': "vettingProvider_example", // BrandVettingEnumVettingProvider | The third-party provider of the vettings to read
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listBrandVetting(brandSid, opts, (error, data, response) => {
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
 **brandSid** | **String**| The SID of the Brand Registration resource of the vettings to read . | 
 **vettingProvider** | **BrandVettingEnumVettingProvider**| The third-party provider of the vettings to read | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListBrandVettingResponse**](ListBrandVettingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


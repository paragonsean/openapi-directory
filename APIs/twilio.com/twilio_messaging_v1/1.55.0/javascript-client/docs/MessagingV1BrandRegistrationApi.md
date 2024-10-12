# TwilioMessaging.MessagingV1BrandRegistrationApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBrandRegistrations**](MessagingV1BrandRegistrationApi.md#createBrandRegistrations) | **POST** /v1/a2p/BrandRegistrations | 
[**fetchBrandRegistrations**](MessagingV1BrandRegistrationApi.md#fetchBrandRegistrations) | **GET** /v1/a2p/BrandRegistrations/{Sid} | 
[**listBrandRegistrations**](MessagingV1BrandRegistrationApi.md#listBrandRegistrations) | **GET** /v1/a2p/BrandRegistrations | 
[**updateBrandRegistrations**](MessagingV1BrandRegistrationApi.md#updateBrandRegistrations) | **POST** /v1/a2p/BrandRegistrations/{Sid} | 



## createBrandRegistrations

> MessagingV1BrandRegistrations createBrandRegistrations(a2PProfileBundleSid, customerProfileBundleSid, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1BrandRegistrationApi();
let a2PProfileBundleSid = "a2PProfileBundleSid_example"; // String | A2P Messaging Profile Bundle Sid.
let customerProfileBundleSid = "customerProfileBundleSid_example"; // String | Customer Profile Bundle Sid.
let opts = {
  'brandType': "brandType_example", // String | Type of brand being created. One of: \\\"STANDARD\\\", \\\"SOLE_PROPRIETOR\\\". SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.
  'mock': true, // Boolean | A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
  'skipAutomaticSecVet': true // Boolean | A flag to disable automatic secondary vetting for brands which it would otherwise be done.
};
apiInstance.createBrandRegistrations(a2PProfileBundleSid, customerProfileBundleSid, opts, (error, data, response) => {
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
 **a2PProfileBundleSid** | **String**| A2P Messaging Profile Bundle Sid. | 
 **customerProfileBundleSid** | **String**| Customer Profile Bundle Sid. | 
 **brandType** | **String**| Type of brand being created. One of: \\\&quot;STANDARD\\\&quot;, \\\&quot;SOLE_PROPRIETOR\\\&quot;. SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases. | [optional] 
 **mock** | **Boolean**| A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided. | [optional] 
 **skipAutomaticSecVet** | **Boolean**| A flag to disable automatic secondary vetting for brands which it would otherwise be done. | [optional] 

### Return type

[**MessagingV1BrandRegistrations**](MessagingV1BrandRegistrations.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchBrandRegistrations

> MessagingV1BrandRegistrations fetchBrandRegistrations(sid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1BrandRegistrationApi();
let sid = "sid_example"; // String | The SID of the Brand Registration resource to fetch.
apiInstance.fetchBrandRegistrations(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Brand Registration resource to fetch. | 

### Return type

[**MessagingV1BrandRegistrations**](MessagingV1BrandRegistrations.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBrandRegistrations

> ListBrandRegistrationsResponse listBrandRegistrations(opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1BrandRegistrationApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listBrandRegistrations(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListBrandRegistrationsResponse**](ListBrandRegistrationsResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBrandRegistrations

> MessagingV1BrandRegistrations updateBrandRegistrations(sid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1BrandRegistrationApi();
let sid = "sid_example"; // String | The SID of the Brand Registration resource to update.
apiInstance.updateBrandRegistrations(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Brand Registration resource to update. | 

### Return type

[**MessagingV1BrandRegistrations**](MessagingV1BrandRegistrations.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


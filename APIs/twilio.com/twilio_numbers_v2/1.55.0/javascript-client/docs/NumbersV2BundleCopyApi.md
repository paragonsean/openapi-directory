# TwilioNumbers.NumbersV2BundleCopyApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBundleCopy**](NumbersV2BundleCopyApi.md#createBundleCopy) | **POST** /v2/RegulatoryCompliance/Bundles/{BundleSid}/Copies | 
[**listBundleCopy**](NumbersV2BundleCopyApi.md#listBundleCopy) | **GET** /v2/RegulatoryCompliance/Bundles/{BundleSid}/Copies | 



## createBundleCopy

> NumbersV2RegulatoryComplianceBundleBundleCopy createBundleCopy(bundleSid, opts)



Creates a new copy of a Bundle. It will internally create copies of all the bundle items (identities and documents) of the original bundle

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2BundleCopyApi();
let bundleSid = "bundleSid_example"; // String | The unique string that identifies the Bundle to be copied.
let opts = {
  'friendlyName': "friendlyName_example" // String | The string that you assigned to describe the copied bundle.
};
apiInstance.createBundleCopy(bundleSid, opts, (error, data, response) => {
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
 **bundleSid** | **String**| The unique string that identifies the Bundle to be copied. | 
 **friendlyName** | **String**| The string that you assigned to describe the copied bundle. | [optional] 

### Return type

[**NumbersV2RegulatoryComplianceBundleBundleCopy**](NumbersV2RegulatoryComplianceBundleBundleCopy.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## listBundleCopy

> ListBundleCopyResponse listBundleCopy(bundleSid, opts)



Retrieve a list of all Bundles Copies for a Bundle.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2BundleCopyApi();
let bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listBundleCopy(bundleSid, opts, (error, data, response) => {
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
 **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListBundleCopyResponse**](ListBundleCopyResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


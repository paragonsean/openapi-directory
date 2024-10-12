# TwilioVideo.VideoV1CompositionSettingsApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCompositionSettings**](VideoV1CompositionSettingsApi.md#createCompositionSettings) | **POST** /v1/CompositionSettings/Default | 
[**fetchCompositionSettings**](VideoV1CompositionSettingsApi.md#fetchCompositionSettings) | **GET** /v1/CompositionSettings/Default | 



## createCompositionSettings

> VideoV1CompositionSettings createCompositionSettings(friendlyName, opts)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1CompositionSettingsApi();
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource and show to the user in the console
let opts = {
  'awsCredentialsSid': "awsCredentialsSid_example", // String | The SID of the stored Credential resource.
  'awsS3Url': "awsS3Url_example", // String | The URL of the AWS S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/compositions`, where `compositions` is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2).
  'awsStorageEnabled': true, // Boolean | Whether all compositions should be written to the `aws_s3_url`. When `false`, all compositions are stored in our cloud.
  'encryptionEnabled': true, // Boolean | Whether all compositions should be stored in an encrypted form. The default is `false`.
  'encryptionKeySid': "encryptionKeySid_example" // String | The SID of the Public Key resource to use for encryption.
};
apiInstance.createCompositionSettings(friendlyName, opts, (error, data, response) => {
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
 **friendlyName** | **String**| A descriptive string that you create to describe the resource and show to the user in the console | 
 **awsCredentialsSid** | **String**| The SID of the stored Credential resource. | [optional] 
 **awsS3Url** | **String**| The URL of the AWS S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like &#x60;https://documentation-example-twilio-bucket/compositions&#x60;, where &#x60;compositions&#x60; is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2). | [optional] 
 **awsStorageEnabled** | **Boolean**| Whether all compositions should be written to the &#x60;aws_s3_url&#x60;. When &#x60;false&#x60;, all compositions are stored in our cloud. | [optional] 
 **encryptionEnabled** | **Boolean**| Whether all compositions should be stored in an encrypted form. The default is &#x60;false&#x60;. | [optional] 
 **encryptionKeySid** | **String**| The SID of the Public Key resource to use for encryption. | [optional] 

### Return type

[**VideoV1CompositionSettings**](VideoV1CompositionSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchCompositionSettings

> VideoV1CompositionSettings fetchCompositionSettings()





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1CompositionSettingsApi();
apiInstance.fetchCompositionSettings((error, data, response) => {
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

[**VideoV1CompositionSettings**](VideoV1CompositionSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


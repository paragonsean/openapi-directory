# TwilioVideo.VideoV1RecordingSettingsApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRecordingSettings**](VideoV1RecordingSettingsApi.md#createRecordingSettings) | **POST** /v1/RecordingSettings/Default | 
[**fetchRecordingSettings**](VideoV1RecordingSettingsApi.md#fetchRecordingSettings) | **GET** /v1/RecordingSettings/Default | 



## createRecordingSettings

> VideoV1RecordingSettings createRecordingSettings(friendlyName, opts)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RecordingSettingsApi();
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource and be shown to users in the console
let opts = {
  'awsCredentialsSid': "awsCredentialsSid_example", // String | The SID of the stored Credential resource.
  'awsS3Url': "awsS3Url_example", // String | The URL of the AWS S3 bucket where the recordings should be stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/recordings`, where `recordings` is the path in which you want the recordings to be stored. This URL accepts only URI-valid characters, as described in the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2).
  'awsStorageEnabled': true, // Boolean | Whether all recordings should be written to the `aws_s3_url`. When `false`, all recordings are stored in our cloud.
  'encryptionEnabled': true, // Boolean | Whether all recordings should be stored in an encrypted form. The default is `false`.
  'encryptionKeySid': "encryptionKeySid_example" // String | The SID of the Public Key resource to use for encryption.
};
apiInstance.createRecordingSettings(friendlyName, opts, (error, data, response) => {
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
 **friendlyName** | **String**| A descriptive string that you create to describe the resource and be shown to users in the console | 
 **awsCredentialsSid** | **String**| The SID of the stored Credential resource. | [optional] 
 **awsS3Url** | **String**| The URL of the AWS S3 bucket where the recordings should be stored. We only support DNS-compliant URLs like &#x60;https://documentation-example-twilio-bucket/recordings&#x60;, where &#x60;recordings&#x60; is the path in which you want the recordings to be stored. This URL accepts only URI-valid characters, as described in the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2). | [optional] 
 **awsStorageEnabled** | **Boolean**| Whether all recordings should be written to the &#x60;aws_s3_url&#x60;. When &#x60;false&#x60;, all recordings are stored in our cloud. | [optional] 
 **encryptionEnabled** | **Boolean**| Whether all recordings should be stored in an encrypted form. The default is &#x60;false&#x60;. | [optional] 
 **encryptionKeySid** | **String**| The SID of the Public Key resource to use for encryption. | [optional] 

### Return type

[**VideoV1RecordingSettings**](VideoV1RecordingSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchRecordingSettings

> VideoV1RecordingSettings fetchRecordingSettings()





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RecordingSettingsApi();
apiInstance.fetchRecordingSettings((error, data, response) => {
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

[**VideoV1RecordingSettings**](VideoV1RecordingSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


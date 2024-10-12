# TwilioNotify.NotifyV1CredentialApi

All URIs are relative to *https://notify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCredential**](NotifyV1CredentialApi.md#createCredential) | **POST** /v1/Credentials | 
[**deleteCredential**](NotifyV1CredentialApi.md#deleteCredential) | **DELETE** /v1/Credentials/{Sid} | 
[**fetchCredential**](NotifyV1CredentialApi.md#fetchCredential) | **GET** /v1/Credentials/{Sid} | 
[**listCredential**](NotifyV1CredentialApi.md#listCredential) | **GET** /v1/Credentials | 
[**updateCredential**](NotifyV1CredentialApi.md#updateCredential) | **POST** /v1/Credentials/{Sid} | 



## createCredential

> NotifyV1Credential createCredential(type, opts)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1CredentialApi();
let type = "type_example"; // CredentialEnumPushService | 
let opts = {
  'apiKey': "apiKey_example", // String | [GCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
  'certificate': "certificate_example", // String | [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. `-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END CERTIFICATE-----`
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'privateKey': "privateKey_example", // String | [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. `-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----`
  'sandbox': true, // Boolean | [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
  'secret': "secret_example" // String | [FCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
};
apiInstance.createCredential(type, opts, (error, data, response) => {
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
 **type** | **CredentialEnumPushService**|  | 
 **apiKey** | **String**| [GCM only] The &#x60;Server key&#x60; of your project from Firebase console under Settings / Cloud messaging. | [optional] 
 **certificate** | **String**| [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. &#x60;-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A&#x3D;&#x3D;-----END CERTIFICATE-----&#x60; | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **privateKey** | **String**| [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. &#x60;-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----&#x60; | [optional] 
 **sandbox** | **Boolean**| [APN only] Whether to send the credential to sandbox APNs. Can be &#x60;true&#x60; to send to sandbox APNs or &#x60;false&#x60; to send to production. | [optional] 
 **secret** | **String**| [FCM only] The &#x60;Server key&#x60; of your project from Firebase console under Settings / Cloud messaging. | [optional] 

### Return type

[**NotifyV1Credential**](NotifyV1Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCredential

> deleteCredential(sid)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1CredentialApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Credential resource to delete.
apiInstance.deleteCredential(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Credential resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchCredential

> NotifyV1Credential fetchCredential(sid)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1CredentialApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Credential resource to fetch.
apiInstance.fetchCredential(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Credential resource to fetch. | 

### Return type

[**NotifyV1Credential**](NotifyV1Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCredential

> ListCredentialResponse listCredential(opts)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1CredentialApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCredential(opts, (error, data, response) => {
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

[**ListCredentialResponse**](ListCredentialResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCredential

> NotifyV1Credential updateCredential(sid, opts)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1CredentialApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Credential resource to update.
let opts = {
  'apiKey': "apiKey_example", // String | [GCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
  'certificate': "certificate_example", // String | [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. `-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END CERTIFICATE-----`
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'privateKey': "privateKey_example", // String | [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. `-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----`
  'sandbox': true, // Boolean | [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
  'secret': "secret_example" // String | [FCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
};
apiInstance.updateCredential(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Credential resource to update. | 
 **apiKey** | **String**| [GCM only] The &#x60;Server key&#x60; of your project from Firebase console under Settings / Cloud messaging. | [optional] 
 **certificate** | **String**| [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. &#x60;-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A&#x3D;&#x3D;-----END CERTIFICATE-----&#x60; | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **privateKey** | **String**| [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. &#x60;-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----&#x60; | [optional] 
 **sandbox** | **Boolean**| [APN only] Whether to send the credential to sandbox APNs. Can be &#x60;true&#x60; to send to sandbox APNs or &#x60;false&#x60; to send to production. | [optional] 
 **secret** | **String**| [FCM only] The &#x60;Server key&#x60; of your project from Firebase console under Settings / Cloud messaging. | [optional] 

### Return type

[**NotifyV1Credential**](NotifyV1Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


# TwilioIpMessaging.IpMessagingV1CredentialApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCredential**](IpMessagingV1CredentialApi.md#createCredential) | **POST** /v1/Credentials | 
[**deleteCredential**](IpMessagingV1CredentialApi.md#deleteCredential) | **DELETE** /v1/Credentials/{Sid} | 
[**fetchCredential**](IpMessagingV1CredentialApi.md#fetchCredential) | **GET** /v1/Credentials/{Sid} | 
[**listCredential**](IpMessagingV1CredentialApi.md#listCredential) | **GET** /v1/Credentials | 
[**updateCredential**](IpMessagingV1CredentialApi.md#updateCredential) | **POST** /v1/Credentials/{Sid} | 



## createCredential

> IpMessagingV1Credential createCredential(type, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1CredentialApi();
let type = "type_example"; // CredentialEnumPushService | 
let opts = {
  'apiKey': "apiKey_example", // String | 
  'certificate': "certificate_example", // String | 
  'friendlyName': "friendlyName_example", // String | 
  'privateKey': "privateKey_example", // String | 
  'sandbox': true, // Boolean | 
  'secret': "secret_example" // String | 
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
 **apiKey** | **String**|  | [optional] 
 **certificate** | **String**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **privateKey** | **String**|  | [optional] 
 **sandbox** | **Boolean**|  | [optional] 
 **secret** | **String**|  | [optional] 

### Return type

[**IpMessagingV1Credential**](IpMessagingV1Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCredential

> deleteCredential(sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1CredentialApi();
let sid = "sid_example"; // String | 
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
 **sid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchCredential

> IpMessagingV1Credential fetchCredential(sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1CredentialApi();
let sid = "sid_example"; // String | 
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
 **sid** | **String**|  | 

### Return type

[**IpMessagingV1Credential**](IpMessagingV1Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCredential

> ListCredentialResponse listCredential(opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1CredentialApi();
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

> IpMessagingV1Credential updateCredential(sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1CredentialApi();
let sid = "sid_example"; // String | 
let opts = {
  'apiKey': "apiKey_example", // String | 
  'certificate': "certificate_example", // String | 
  'friendlyName': "friendlyName_example", // String | 
  'privateKey': "privateKey_example", // String | 
  'sandbox': true, // Boolean | 
  'secret': "secret_example" // String | 
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
 **sid** | **String**|  | 
 **apiKey** | **String**|  | [optional] 
 **certificate** | **String**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **privateKey** | **String**|  | [optional] 
 **sandbox** | **Boolean**|  | [optional] 
 **secret** | **String**|  | [optional] 

### Return type

[**IpMessagingV1Credential**](IpMessagingV1Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


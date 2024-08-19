# AuthentiqApi.DeleteApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyRevokeNosecret_0**](DeleteApi.md#keyRevokeNosecret_0) | **DELETE** /key | 
[**keyRevoke_0**](DeleteApi.md#keyRevoke_0) | **DELETE** /key/{PK} | 
[**signDelete_0**](DeleteApi.md#signDelete_0) | **DELETE** /scope/{job} | 



## keyRevokeNosecret_0

> KeyRevokeNosecret200Response keyRevokeNosecret_0(email, phone, opts)



Revoke an Authentiq ID using email &amp; phone.  If called with &#x60;email&#x60; and &#x60;phone&#x60; only, a verification code  will be sent by email. Do a second call adding &#x60;code&#x60; to  complete the revocation. 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.DeleteApi();
let email = "email_example"; // String | primary email associated to Key (ID)
let phone = "phone_example"; // String | primary phone number, international representation
let opts = {
  'code': "code_example" // String | verification code sent by email
};
apiInstance.keyRevokeNosecret_0(email, phone, opts, (error, data, response) => {
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
 **email** | **String**| primary email associated to Key (ID) | 
 **phone** | **String**| primary phone number, international representation | 
 **code** | **String**| verification code sent by email | [optional] 

### Return type

[**KeyRevokeNosecret200Response**](KeyRevokeNosecret200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## keyRevoke_0

> KeyRevoke200Response keyRevoke_0(PK, secret)



Revoke an Identity (Key) with a revocation secret

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.DeleteApi();
let PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
let secret = "secret_example"; // String | revokation secret
apiInstance.keyRevoke_0(PK, secret, (error, data, response) => {
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
 **PK** | **String**| Public Signing Key - Authentiq ID (43 chars) | 
 **secret** | **String**| revokation secret | 

### Return type

[**KeyRevoke200Response**](KeyRevoke200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## signDelete_0

> KeyRevoke200Response signDelete_0(job)



delete a verification job

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.DeleteApi();
let job = "job_example"; // String | Job ID (20 chars)
apiInstance.signDelete_0(job, (error, data, response) => {
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
 **job** | **String**| Job ID (20 chars) | 

### Return type

[**KeyRevoke200Response**](KeyRevoke200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


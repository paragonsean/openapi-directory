# HttpbinOrg.AuthApi

All URIs are relative to *https://httpbin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**basicAuthUserPasswdGet**](AuthApi.md#basicAuthUserPasswdGet) | **GET** /basic-auth/{user}/{passwd} | Prompts the user for authorization using HTTP Basic Auth.
[**bearerGet**](AuthApi.md#bearerGet) | **GET** /bearer | Prompts the user for authorization using bearer authentication.
[**digestAuthQopUserPasswdAlgorithmGet**](AuthApi.md#digestAuthQopUserPasswdAlgorithmGet) | **GET** /digest-auth/{qop}/{user}/{passwd}/{algorithm} | Prompts the user for authorization using Digest Auth + Algorithm.
[**digestAuthQopUserPasswdAlgorithmStaleAfterGet**](AuthApi.md#digestAuthQopUserPasswdAlgorithmStaleAfterGet) | **GET** /digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after} | Prompts the user for authorization using Digest Auth + Algorithm.
[**digestAuthQopUserPasswdGet**](AuthApi.md#digestAuthQopUserPasswdGet) | **GET** /digest-auth/{qop}/{user}/{passwd} | Prompts the user for authorization using Digest Auth.
[**hiddenBasicAuthUserPasswdGet**](AuthApi.md#hiddenBasicAuthUserPasswdGet) | **GET** /hidden-basic-auth/{user}/{passwd} | Prompts the user for authorization using HTTP Basic Auth.



## basicAuthUserPasswdGet

> basicAuthUserPasswdGet(user, passwd)

Prompts the user for authorization using HTTP Basic Auth.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.AuthApi();
let user = "user_example"; // String | 
let passwd = "passwd_example"; // String | 
apiInstance.basicAuthUserPasswdGet(user, passwd, (error, data, response) => {
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
 **user** | **String**|  | 
 **passwd** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bearerGet

> bearerGet(opts)

Prompts the user for authorization using bearer authentication.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.AuthApi();
let opts = {
  'authorization': "authorization_example" // String | 
};
apiInstance.bearerGet(opts, (error, data, response) => {
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
 **authorization** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## digestAuthQopUserPasswdAlgorithmGet

> digestAuthQopUserPasswdAlgorithmGet(qop, user, passwd, algorithm)

Prompts the user for authorization using Digest Auth + Algorithm.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.AuthApi();
let qop = "qop_example"; // String | auth or auth-int
let user = "user_example"; // String | 
let passwd = "passwd_example"; // String | 
let algorithm = "'MD5'"; // String | MD5, SHA-256, SHA-512
apiInstance.digestAuthQopUserPasswdAlgorithmGet(qop, user, passwd, algorithm, (error, data, response) => {
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
 **qop** | **String**| auth or auth-int | 
 **user** | **String**|  | 
 **passwd** | **String**|  | 
 **algorithm** | **String**| MD5, SHA-256, SHA-512 | [default to &#39;MD5&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## digestAuthQopUserPasswdAlgorithmStaleAfterGet

> digestAuthQopUserPasswdAlgorithmStaleAfterGet(qop, user, passwd, algorithm, staleAfter)

Prompts the user for authorization using Digest Auth + Algorithm.

allow settings the stale_after argument. 

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.AuthApi();
let qop = "qop_example"; // String | auth or auth-int
let user = "user_example"; // String | 
let passwd = "passwd_example"; // String | 
let algorithm = "'MD5'"; // String | MD5, SHA-256, SHA-512
let staleAfter = "'never'"; // String | 
apiInstance.digestAuthQopUserPasswdAlgorithmStaleAfterGet(qop, user, passwd, algorithm, staleAfter, (error, data, response) => {
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
 **qop** | **String**| auth or auth-int | 
 **user** | **String**|  | 
 **passwd** | **String**|  | 
 **algorithm** | **String**| MD5, SHA-256, SHA-512 | [default to &#39;MD5&#39;]
 **staleAfter** | **String**|  | [default to &#39;never&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## digestAuthQopUserPasswdGet

> digestAuthQopUserPasswdGet(qop, user, passwd)

Prompts the user for authorization using Digest Auth.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.AuthApi();
let qop = "qop_example"; // String | auth or auth-int
let user = "user_example"; // String | 
let passwd = "passwd_example"; // String | 
apiInstance.digestAuthQopUserPasswdGet(qop, user, passwd, (error, data, response) => {
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
 **qop** | **String**| auth or auth-int | 
 **user** | **String**|  | 
 **passwd** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## hiddenBasicAuthUserPasswdGet

> hiddenBasicAuthUserPasswdGet(user, passwd)

Prompts the user for authorization using HTTP Basic Auth.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.AuthApi();
let user = "user_example"; // String | 
let passwd = "passwd_example"; // String | 
apiInstance.hiddenBasicAuthUserPasswdGet(user, passwd, (error, data, response) => {
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
 **user** | **String**|  | 
 **passwd** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


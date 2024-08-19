# AuthentiqApi.KeyApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyBind**](KeyApi.md#keyBind) | **PUT** /key/{PK} | 
[**keyPKHead**](KeyApi.md#keyPKHead) | **HEAD** /key/{PK} | 
[**keyRegister**](KeyApi.md#keyRegister) | **POST** /key | 
[**keyRetrieve**](KeyApi.md#keyRetrieve) | **GET** /key/{PK} | 
[**keyRevoke**](KeyApi.md#keyRevoke) | **DELETE** /key/{PK} | 
[**keyRevokeNosecret**](KeyApi.md#keyRevokeNosecret) | **DELETE** /key | 
[**keyUpdate**](KeyApi.md#keyUpdate) | **POST** /key/{PK} | 



## keyBind

> KeyBind200Response keyBind(PK, authentiqID)



Update Authentiq ID by replacing the object.  v4: &#x60;JWT(sub,email,phone)&#x60; to bind email/phone hash;   v5: POST issuer-signed email &amp; phone scopes and PUT to update registration &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.KeyApi();
let PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
let authentiqID = new AuthentiqApi.AuthentiqID(); // AuthentiqID | Authentiq ID to register
apiInstance.keyBind(PK, authentiqID, (error, data, response) => {
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
 **authentiqID** | [**AuthentiqID**](AuthentiqID.md)| Authentiq ID to register | 

### Return type

[**KeyBind200Response**](KeyBind200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/jwt
- **Accept**: application/json, */*


## keyPKHead

> keyPKHead(PK)



HEAD info on Authentiq ID 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.KeyApi();
let PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
apiInstance.keyPKHead(PK, (error, data, response) => {
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
 **PK** | **String**| Public Signing Key - Authentiq ID (43 chars) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## keyRegister

> KeyRegister201Response keyRegister(authentiqID)



Register a new ID &#x60;JWT(sub, devtoken)&#x60;  v5: &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.KeyApi();
let authentiqID = new AuthentiqApi.AuthentiqID(); // AuthentiqID | Authentiq ID to register
apiInstance.keyRegister(authentiqID, (error, data, response) => {
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
 **authentiqID** | [**AuthentiqID**](AuthentiqID.md)| Authentiq ID to register | 

### Return type

[**KeyRegister201Response**](KeyRegister201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/jwt
- **Accept**: application/json, */*


## keyRetrieve

> JWT keyRetrieve(PK)



Get public details of an Authentiq ID. 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.KeyApi();
let PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
apiInstance.keyRetrieve(PK, (error, data, response) => {
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

### Return type

[**JWT**](JWT.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## keyRevoke

> KeyRevoke200Response keyRevoke(PK, secret)



Revoke an Identity (Key) with a revocation secret

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.KeyApi();
let PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
let secret = "secret_example"; // String | revokation secret
apiInstance.keyRevoke(PK, secret, (error, data, response) => {
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


## keyRevokeNosecret

> KeyRevokeNosecret200Response keyRevokeNosecret(email, phone, opts)



Revoke an Authentiq ID using email &amp; phone.  If called with &#x60;email&#x60; and &#x60;phone&#x60; only, a verification code  will be sent by email. Do a second call adding &#x60;code&#x60; to  complete the revocation. 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.KeyApi();
let email = "email_example"; // String | primary email associated to Key (ID)
let phone = "phone_example"; // String | primary phone number, international representation
let opts = {
  'code': "code_example" // String | verification code sent by email
};
apiInstance.keyRevokeNosecret(email, phone, opts, (error, data, response) => {
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


## keyUpdate

> KeyBind200Response keyUpdate(PK, authentiqID)



update properties of an Authentiq ID. (not operational in v4; use PUT for now)  v5: POST issuer-signed email &amp; phone scopes in a self-signed JWT  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.KeyApi();
let PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
let authentiqID = new AuthentiqApi.AuthentiqID(); // AuthentiqID | Authentiq ID to register
apiInstance.keyUpdate(PK, authentiqID, (error, data, response) => {
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
 **authentiqID** | [**AuthentiqID**](AuthentiqID.md)| Authentiq ID to register | 

### Return type

[**KeyBind200Response**](KeyBind200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/jwt
- **Accept**: application/json, */*


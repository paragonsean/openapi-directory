# AuthentiqApi.PostApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyRegister_0**](PostApi.md#keyRegister_0) | **POST** /key | 
[**keyUpdate_0**](PostApi.md#keyUpdate_0) | **POST** /key/{PK} | 
[**pushLoginRequest_0**](PostApi.md#pushLoginRequest_0) | **POST** /login | 
[**signConfirm_0**](PostApi.md#signConfirm_0) | **POST** /scope/{job} | 
[**signRequest_0**](PostApi.md#signRequest_0) | **POST** /scope | 



## keyRegister_0

> KeyRegister201Response keyRegister_0(authentiqID)



Register a new ID &#x60;JWT(sub, devtoken)&#x60;  v5: &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.PostApi();
let authentiqID = new AuthentiqApi.AuthentiqID(); // AuthentiqID | Authentiq ID to register
apiInstance.keyRegister_0(authentiqID, (error, data, response) => {
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


## keyUpdate_0

> KeyBind200Response keyUpdate_0(PK, authentiqID)



update properties of an Authentiq ID. (not operational in v4; use PUT for now)  v5: POST issuer-signed email &amp; phone scopes in a self-signed JWT  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.PostApi();
let PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
let authentiqID = new AuthentiqApi.AuthentiqID(); // AuthentiqID | Authentiq ID to register
apiInstance.keyUpdate_0(PK, authentiqID, (error, data, response) => {
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


## pushLoginRequest_0

> PushLoginRequest200Response pushLoginRequest_0(callback, pushToken)



push sign-in request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.PostApi();
let callback = "callback_example"; // String | URI App will connect to
let pushToken = new AuthentiqApi.PushToken(); // PushToken | Push Token.
apiInstance.pushLoginRequest_0(callback, pushToken, (error, data, response) => {
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
 **callback** | **String**| URI App will connect to | 
 **pushToken** | [**PushToken**](PushToken.md)| Push Token. | 

### Return type

[**PushLoginRequest200Response**](PushLoginRequest200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/jwt
- **Accept**: application/json, */*


## signConfirm_0

> KeyBind200Response signConfirm_0(job)



this is a scope confirmation

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.PostApi();
let job = "job_example"; // String | Job ID (20 chars)
apiInstance.signConfirm_0(job, (error, data, response) => {
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

[**KeyBind200Response**](KeyBind200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## signRequest_0

> SignRequest201Response signRequest_0(claims, opts)



scope verification request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.PostApi();
let claims = new AuthentiqApi.Claims(); // Claims | Claims of scope
let opts = {
  'test': 56 // Number | test only mode, using test issuer
};
apiInstance.signRequest_0(claims, opts, (error, data, response) => {
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
 **claims** | [**Claims**](Claims.md)| Claims of scope | 
 **test** | **Number**| test only mode, using test issuer | [optional] 

### Return type

[**SignRequest201Response**](SignRequest201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/jwt
- **Accept**: application/json, */*


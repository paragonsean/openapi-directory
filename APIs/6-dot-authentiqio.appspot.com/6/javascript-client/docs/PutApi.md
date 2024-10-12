# AuthentiqApi.PutApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyBind_0**](PutApi.md#keyBind_0) | **PUT** /key/{PK} | 
[**signUpdate_0**](PutApi.md#signUpdate_0) | **PUT** /scope/{job} | 



## keyBind_0

> KeyBind200Response keyBind_0(PK, authentiqID)



Update Authentiq ID by replacing the object.  v4: &#x60;JWT(sub,email,phone)&#x60; to bind email/phone hash;   v5: POST issuer-signed email &amp; phone scopes and PUT to update registration &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.PutApi();
let PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
let authentiqID = new AuthentiqApi.AuthentiqID(); // AuthentiqID | Authentiq ID to register
apiInstance.keyBind_0(PK, authentiqID, (error, data, response) => {
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


## signUpdate_0

> SignUpdate200Response signUpdate_0(job)



authority updates a JWT with its signature See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example

```javascript
import AuthentiqApi from 'authentiq_api';

let apiInstance = new AuthentiqApi.PutApi();
let job = "job_example"; // String | Job ID (20 chars)
apiInstance.signUpdate_0(job, (error, data, response) => {
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

[**SignUpdate200Response**](SignUpdate200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/jwt, */*


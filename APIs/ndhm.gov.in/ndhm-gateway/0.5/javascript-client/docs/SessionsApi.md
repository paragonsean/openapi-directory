# Gateway.SessionsApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05CertsGet**](SessionsApi.md#v05CertsGet) | **GET** /v0.5/certs | Get certs for JWT verification
[**v05SessionsPost**](SessionsApi.md#v05SessionsPost) | **POST** /v0.5/sessions | Get access token
[**v05WellKnownOpenidConfigurationGet**](SessionsApi.md#v05WellKnownOpenidConfigurationGet) | **GET** /v0.5/.well-known/openid-configuration | Get openid configuration



## v05CertsGet

> Certs v05CertsGet()

Get certs for JWT verification

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.SessionsApi();
apiInstance.v05CertsGet((error, data, response) => {
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

[**Certs**](Certs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v05SessionsPost

> SessionResponse v05SessionsPost(sessionRequest)

Get access token

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.SessionsApi();
let sessionRequest = new Gateway.SessionRequest(); // SessionRequest | 
apiInstance.v05SessionsPost(sessionRequest, (error, data, response) => {
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
 **sessionRequest** | [**SessionRequest**](SessionRequest.md)|  | 

### Return type

[**SessionResponse**](SessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05WellKnownOpenidConfigurationGet

> OpenIdConfiguration v05WellKnownOpenidConfigurationGet()

Get openid configuration

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.SessionsApi();
apiInstance.v05WellKnownOpenidConfigurationGet((error, data, response) => {
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

[**OpenIdConfiguration**](OpenIdConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


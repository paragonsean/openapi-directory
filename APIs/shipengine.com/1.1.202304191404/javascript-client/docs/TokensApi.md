# ShipEngineApi.TokensApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokensGetEphemeralToken**](TokensApi.md#tokensGetEphemeralToken) | **POST** /v1/tokens/ephemeral | Get Ephemeral Token



## tokensGetEphemeralToken

> TokensGetEphemeralTokenResponseBodyYaml tokensGetEphemeralToken(opts)

Get Ephemeral Token

This endpoint returns a token that can be passed to an application for authorized access.  The lifetime of this token is 10 seconds.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.TokensApi();
let opts = {
  'redirect': new ShipEngineApi.Redirect() // Redirect | Include a redirect url to the application formatted with the ephemeral token.
};
apiInstance.tokensGetEphemeralToken(opts, (error, data, response) => {
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
 **redirect** | [**Redirect**](.md)| Include a redirect url to the application formatted with the ephemeral token. | [optional] 

### Return type

[**TokensGetEphemeralTokenResponseBodyYaml**](TokensGetEphemeralTokenResponseBodyYaml.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


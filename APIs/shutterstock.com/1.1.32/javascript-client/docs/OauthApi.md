# ShutterstockApiExplorer.OauthApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize**](OauthApi.md#authorize) | **GET** /v2/oauth/authorize | Authorize applications
[**createAccessToken**](OauthApi.md#createAccessToken) | **POST** /v2/oauth/access_token | Get access tokens



## authorize

> authorize(clientId, redirectUri, responseType, state, opts)

Authorize applications

This endpoint returns a redirect URI (in the &#39;Location&#39; header) that the customer uses to authorize your application and, together with POST /v2/oauth/access_token, generate an access token that represents that authorization.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';

let apiInstance = new ShutterstockApiExplorer.OauthApi();
let clientId = "6d097450b209c6dcd859"; // String | Client ID (Consumer Key) of your application
let redirectUri = "localhost"; // String | The callback URI to send the request to after authorization; must use a host name that is registered with your application
let responseType = "code"; // String | Type of temporary authorization code that will be used to generate an access code; the only valid value is 'code'
let state = "1540290465000"; // String | Unique value used by the calling app to verify the request
let opts = {
  'realm': "customer", // String | User type to be authorized (usually 'customer')
  'scope': "user.view" // String | Space-separated list of scopes to be authorized
};
apiInstance.authorize(clientId, redirectUri, responseType, state, opts, (error, data, response) => {
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
 **clientId** | **String**| Client ID (Consumer Key) of your application | 
 **redirectUri** | **String**| The callback URI to send the request to after authorization; must use a host name that is registered with your application | 
 **responseType** | **String**| Type of temporary authorization code that will be used to generate an access code; the only valid value is &#39;code&#39; | 
 **state** | **String**| Unique value used by the calling app to verify the request | 
 **realm** | **String**| User type to be authorized (usually &#39;customer&#39;) | [optional] [default to &#39;customer&#39;]
 **scope** | **String**| Space-separated list of scopes to be authorized | [optional] [default to &#39;user.view&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html


## createAccessToken

> OauthAccessTokenResponse createAccessToken(opts)

Get access tokens

This endpoint returns an access token for the specified user and with the specified scopes. The token does not expire until the user changes their password. The body parameters must be encoded as form data.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';

let apiInstance = new ShutterstockApiExplorer.OauthApi();
let opts = {
  'createAccessTokenRequest': {"client_id":"141024g14g28104gff1h"} // CreateAccessTokenRequest | 
};
apiInstance.createAccessToken(opts, (error, data, response) => {
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
 **createAccessTokenRequest** | [**CreateAccessTokenRequest**](CreateAccessTokenRequest.md)|  | [optional] 

### Return type

[**OauthAccessTokenResponse**](OauthAccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json


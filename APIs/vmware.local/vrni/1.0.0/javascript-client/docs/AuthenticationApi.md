# VRealizeNetworkInsightApiReference.AuthenticationApi

All URIs are relative to *http://vmware.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callDelete**](AuthenticationApi.md#callDelete) | **DELETE** /auth/token | Delete an auth token.
[**create**](AuthenticationApi.md#create) | **POST** /auth/token | Create an auth token



## callDelete

> callDelete()

Delete an auth token.

Deletes the auth token provided in Authorization header. Deleting an expired or invalid token will result in 401 Unauthorized error.

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.AuthenticationApi();
apiInstance.callDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## create

> Token create(userCredential)

Create an auth token

&lt;html&gt;&lt;body&gt; vRealize Network Insight supports token based authentication.Tokens are non-modifiable identifiers returned by the system when the user has successfully authenticated using valid credentials. Token expires after expiry time returned in the response. All API requests must provide the auth token in Authorization header in following format.&lt;br&gt; Authorization &amp;#58; NetworkInsight {token} &lt;br&gt; If a token is invalid or expired, 401-Unauthorized error gets returned in the response of the API request. &lt;/body&gt;&lt;/html&gt;

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';

let apiInstance = new VRealizeNetworkInsightApiReference.AuthenticationApi();
let userCredential = new VRealizeNetworkInsightApiReference.UserCredential(); // UserCredential | User Credentials
apiInstance.create(userCredential, (error, data, response) => {
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
 **userCredential** | [**UserCredential**](UserCredential.md)| User Credentials | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, expiry, token


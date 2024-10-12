# AkeneoPimRestApi.AuthenticationApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postToken**](AuthenticationApi.md#postToken) | **POST** /api/oauth/v1/token | Get authentication token



## postToken

> PostToken200Response postToken(contentType, authorization, opts)

Get authentication token

This endpoint allows you to get an authentication token. No need to be authenticated to use this endpoint.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AuthenticationApi();
let contentType = "contentType_example"; // String | Equal to 'application/json' or 'application/x-www-form-urlencoded', no other value allowed
let authorization = "authorization_example"; // String | Equal to 'Basic xx', where 'xx' is the base 64 encoding of the client id and secret. Find out how to generate them in the <a href=\"/documentation/authentication.html#client-idsecret-generation\">Client ID/secret generation</a> section.
let opts = {
  'body': new AkeneoPimRestApi.PostTokenRequest() // PostTokenRequest | 
};
apiInstance.postToken(contentType, authorization, opts, (error, data, response) => {
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
 **contentType** | **String**| Equal to &#39;application/json&#39; or &#39;application/x-www-form-urlencoded&#39;, no other value allowed | 
 **authorization** | **String**| Equal to &#39;Basic xx&#39;, where &#39;xx&#39; is the base 64 encoding of the client id and secret. Find out how to generate them in the &lt;a href&#x3D;\&quot;/documentation/authentication.html#client-idsecret-generation\&quot;&gt;Client ID/secret generation&lt;/a&gt; section. | 
 **body** | [**PostTokenRequest**](PostTokenRequest.md)|  | [optional] 

### Return type

[**PostToken200Response**](PostToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, access_token, expires_in, refresh_token, token_type, code, message, _links


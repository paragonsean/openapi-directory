# AuthorizedPartnerApiSpecification.TokenRevocationAPIApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTokenRevocationId**](TokenRevocationAPIApi.md#getTokenRevocationId) | **POST** /oauth2/1/revoke | Revoke Token.



## getTokenRevocationId

> getTokenRevocationId(opts)

Revoke Token.

Client applications can revoke a previously obtained refresh or access token when it is no longer needed. This is done by making a request to the token revocation endpoint. DigiLocker will invalidate the specified token and, if applicable, other tokens based on the same authorisation grant. This API may be used to sign out a user from DigiLocker. This API will work for server based web applications, mobile application and limited input devices.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthsecurity
let oauthsecurity = defaultClient.authentications['oauthsecurity'];
oauthsecurity.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.TokenRevocationAPIApi();
let opts = {
  'getTokenRevocationIdRequest': new AuthorizedPartnerApiSpecification.GetTokenRevocationIdRequest() // GetTokenRevocationIdRequest | 
};
apiInstance.getTokenRevocationId(opts, (error, data, response) => {
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
 **getTokenRevocationIdRequest** | [**GetTokenRevocationIdRequest**](GetTokenRevocationIdRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


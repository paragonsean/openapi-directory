# AuthorizedPartnerApiSpecification.AuthorizationApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuthorizationCodeId**](AuthorizationApi.md#getAuthorizationCodeId) | **GET** /oauth2/1/authorize | Get Authorization Code
[**getaccesstokenId**](AuthorizationApi.md#getaccesstokenId) | **POST** /oauth2/1/token | Get Access Token



## getAuthorizationCodeId

> Sample getAuthorizationCodeId(responseType, redirectUri, state, opts)

Get Authorization Code

Call to this API starts authorization flow using OAuth 2.0 protocol. This isn&#39;t an API call—it&#39;s a DigiLocker web page that lets the user sign in to DigiLocker and authorize your application to access user’s data. After the user decides whether or not to authorize your app, they will be redirected to the redirect link provided by your application.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthAuthorizeCode
let oauthAuthorizeCode = defaultClient.authentications['oauthAuthorizeCode'];
oauthAuthorizeCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.AuthorizationApi();
let responseType = "responseType_example"; // String | Provide the grant type requested, either token or code.
let redirectUri = "redirectUri_example"; // String | The URI to redirect the user after authorization has completed.
let state = "state_example"; // String | This is your application specific data that will be passed back to your application through redirect_uri.
let opts = {
  'clientId': "clientId_example", // String | Provide the client id that was created during the application registration process on Partners Portal.
  'codeChallenge': base64_url_encode_without_padding(sha256(code_verifier)), // String | A unique random string called code verifier (code_verifier) is created by the client application for every authorization request. The code_challenge sent as this parameter is the Base64URL (with no padding) encoded SHA256 hash of the code verifier.         Code block:         ```        string base64_url_encode_without_padding(string arg)        {            string s = base64encode(arg); //Regular base64encoder with padding           s = s.replace(’=’,’’); //Remove any trailing ’=’           s = s.replace(’+’, ’-’); //Replace ’+’ with ’-’           s = s.replace(’/’, ’_’); //Replace ’/’ with ’_’ return s;         }         ``` 
  'codeChallengeMethod': null, // String | Specifies what method was used to encode a code_verifier to generate code_challenge parameter above. This parameter must be used with the code_challenge parameter. The only supported values for this parameter is S256.
  'dlFlow': "dlFlow_example", // String | If this parameter is provided its value will always be signup. This parameter indicates that the user does not have a DigiLocker account and will be directed to the signup flow directly. After the account is created, the user will be directed to the authorization flow. If this parameter is not sent, the user will be redirected to the sign in flow.
  'verifiedMobile': 56 // Number | Verified mobile number of the user. If this parameter is passed, DigiLocker will skip the mobile OTP verification step during sign up. DigiLocker will treat the mobile number passed in this parameter as a verified mobile number by the trusted client application. This parameter will be used only if dl_flow parameter mentioned above is set to signup and will be ignored otherwise.
};
apiInstance.getAuthorizationCodeId(responseType, redirectUri, state, opts, (error, data, response) => {
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
 **responseType** | **String**| Provide the grant type requested, either token or code. | 
 **redirectUri** | **String**| The URI to redirect the user after authorization has completed. | 
 **state** | **String**| This is your application specific data that will be passed back to your application through redirect_uri. | 
 **clientId** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] 
 **codeChallenge** | [**String**](.md)| A unique random string called code verifier (code_verifier) is created by the client application for every authorization request. The code_challenge sent as this parameter is the Base64URL (with no padding) encoded SHA256 hash of the code verifier.         Code block:         &#x60;&#x60;&#x60;        string base64_url_encode_without_padding(string arg)        {            string s &#x3D; base64encode(arg); //Regular base64encoder with padding           s &#x3D; s.replace(’&#x3D;’,’’); //Remove any trailing ’&#x3D;’           s &#x3D; s.replace(’+’, ’-’); //Replace ’+’ with ’-’           s &#x3D; s.replace(’/’, ’_’); //Replace ’/’ with ’_’ return s;         }         &#x60;&#x60;&#x60;  | [optional] 
 **codeChallengeMethod** | [**String**](.md)| Specifies what method was used to encode a code_verifier to generate code_challenge parameter above. This parameter must be used with the code_challenge parameter. The only supported values for this parameter is S256. | [optional] 
 **dlFlow** | **String**| If this parameter is provided its value will always be signup. This parameter indicates that the user does not have a DigiLocker account and will be directed to the signup flow directly. After the account is created, the user will be directed to the authorization flow. If this parameter is not sent, the user will be redirected to the sign in flow. | [optional] 
 **verifiedMobile** | **Number**| Verified mobile number of the user. If this parameter is passed, DigiLocker will skip the mobile OTP verification step during sign up. DigiLocker will treat the mobile number passed in this parameter as a verified mobile number by the trusted client application. This parameter will be used only if dl_flow parameter mentioned above is set to signup and will be ignored otherwise. | [optional] 

### Return type

[**Sample**](Sample.md)

### Authorization

[oauthAuthorizeCode](../README.md#oauthAuthorizeCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getaccesstokenId

> AccessResponse getaccesstokenId(getaccesstokenIdRequest)

Get Access Token

This endpoint only applies to apps using the authorization code flow. An app calls this endpoint to acquire a bearer token once the user has authorized the app. Calls to /oauth2/1/token need to be authenticated using the app&#39;s key and secret. These can either be passed as application/x-www-form-urlencoded POST parameters (see parameters below) or via HTTP basic authentication. If basic authentication is used, the app key should be provided as the username, and the app secret should be provided as the password.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';

let apiInstance = new AuthorizedPartnerApiSpecification.AuthorizationApi();
let getaccesstokenIdRequest = new AuthorizedPartnerApiSpecification.GetaccesstokenIdRequest(); // GetaccesstokenIdRequest | Details of documents being created.
apiInstance.getaccesstokenId(getaccesstokenIdRequest, (error, data, response) => {
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
 **getaccesstokenIdRequest** | [**GetaccesstokenIdRequest**](GetaccesstokenIdRequest.md)| Details of documents being created. | 

### Return type

[**AccessResponse**](AccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


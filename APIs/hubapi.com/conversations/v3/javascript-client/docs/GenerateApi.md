# VisitorIdentification.GenerateApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postConversationsV3VisitorIdentificationTokensCreateGenerateToken**](GenerateApi.md#postConversationsV3VisitorIdentificationTokensCreateGenerateToken) | **POST** /conversations/v3/visitor-identification/tokens/create | Generate a token



## postConversationsV3VisitorIdentificationTokensCreateGenerateToken

> IdentificationTokenResponse postConversationsV3VisitorIdentificationTokensCreateGenerateToken(identificationTokenGenerationRequest)

Generate a token

Generates a new visitor identification token. This token will be unique every time this endpoint is called, even if called with the same email address. This token is temporary and will expire after 12 hours

### Example

```javascript
import VisitorIdentification from 'visitor_identification';
let defaultClient = VisitorIdentification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new VisitorIdentification.GenerateApi();
let identificationTokenGenerationRequest = new VisitorIdentification.IdentificationTokenGenerationRequest(); // IdentificationTokenGenerationRequest | 
apiInstance.postConversationsV3VisitorIdentificationTokensCreateGenerateToken(identificationTokenGenerationRequest, (error, data, response) => {
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
 **identificationTokenGenerationRequest** | [**IdentificationTokenGenerationRequest**](IdentificationTokenGenerationRequest.md)|  | 

### Return type

[**IdentificationTokenResponse**](IdentificationTokenResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


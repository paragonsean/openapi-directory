# MastodonApiSpecificationHttpsGithubComMastodonMastodon.AppsApi

All URIs are relative to *http://mastodon.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1AppsPost**](AppsApi.md#apiV1AppsPost) | **POST** /api/v1/apps | 
[**apiV1AppsVerifyCredentialsGet**](AppsApi.md#apiV1AppsVerifyCredentialsGet) | **GET** /api/v1/apps/verify_credentials | 



## apiV1AppsPost

> ApiV1AppsPost200Response apiV1AppsPost(opts)



Create a new application to obtain OAuth2 credentials.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AppsApi();
let opts = {
  'apiV1AppsPostRequest': new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1AppsPostRequest() // ApiV1AppsPostRequest | 
};
apiInstance.apiV1AppsPost(opts, (error, data, response) => {
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
 **apiV1AppsPostRequest** | [**ApiV1AppsPostRequest**](ApiV1AppsPostRequest.md)|  | [optional] 

### Return type

[**ApiV1AppsPost200Response**](ApiV1AppsPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/form-data
- **Accept**: application/json


## apiV1AppsVerifyCredentialsGet

> Application apiV1AppsVerifyCredentialsGet()



Confirm that the app&#39;s OAuth2 credentials work.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AppsApi();
apiInstance.apiV1AppsVerifyCredentialsGet((error, data, response) => {
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

[**Application**](Application.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


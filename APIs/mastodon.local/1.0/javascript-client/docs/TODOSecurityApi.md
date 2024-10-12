# MastodonApiSpecificationHttpsGithubComMastodonMastodon.TODOSecurityApi

All URIs are relative to *http://mastodon.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1AccountsPost**](TODOSecurityApi.md#apiV1AccountsPost) | **POST** /api/v1/accounts | 



## apiV1AccountsPost

> apiV1AccountsPost(opts)



Creates a user and account records. Returns an account access token for the app that initiated the request. The app should save this token for later, and should wait for the user to confirm their account by clicking a link in their email inbox.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.TODOSecurityApi();
let opts = {
  'apiV1AccountsPostRequest': new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1AccountsPostRequest() // ApiV1AccountsPostRequest | 
};
apiInstance.apiV1AccountsPost(opts, (error, data, response) => {
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
 **apiV1AccountsPostRequest** | [**ApiV1AccountsPostRequest**](ApiV1AccountsPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/form-data
- **Accept**: Not defined


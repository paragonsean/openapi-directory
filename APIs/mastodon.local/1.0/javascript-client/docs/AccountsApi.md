# MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi

All URIs are relative to *http://mastodon.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1AccountsIdBlockPost**](AccountsApi.md#apiV1AccountsIdBlockPost) | **POST** /api/v1/accounts/{id}/block | 
[**apiV1AccountsIdFeaturedTagsGet**](AccountsApi.md#apiV1AccountsIdFeaturedTagsGet) | **GET** /api/v1/accounts/{id}/featured_tags | 
[**apiV1AccountsIdFollowPost**](AccountsApi.md#apiV1AccountsIdFollowPost) | **POST** /api/v1/accounts/{id}/follow | 
[**apiV1AccountsIdFollowersGet**](AccountsApi.md#apiV1AccountsIdFollowersGet) | **GET** /api/v1/accounts/{id}/followers | 
[**apiV1AccountsIdFollowingGet**](AccountsApi.md#apiV1AccountsIdFollowingGet) | **GET** /api/v1/accounts/{id}/following | 
[**apiV1AccountsIdGet**](AccountsApi.md#apiV1AccountsIdGet) | **GET** /api/v1/accounts/{id} | 
[**apiV1AccountsIdIdentityProofsGet**](AccountsApi.md#apiV1AccountsIdIdentityProofsGet) | **GET** /api/v1/accounts/{id}/identity_proofs | 
[**apiV1AccountsIdListsGet**](AccountsApi.md#apiV1AccountsIdListsGet) | **GET** /api/v1/accounts/{id}/lists | 
[**apiV1AccountsIdMutePost**](AccountsApi.md#apiV1AccountsIdMutePost) | **POST** /api/v1/accounts/{id}/mute | 
[**apiV1AccountsIdNotePost**](AccountsApi.md#apiV1AccountsIdNotePost) | **POST** /api/v1/accounts/{id}/note | 
[**apiV1AccountsIdPinPost**](AccountsApi.md#apiV1AccountsIdPinPost) | **POST** /api/v1/accounts/{id}/pin | 
[**apiV1AccountsIdStatusesGet**](AccountsApi.md#apiV1AccountsIdStatusesGet) | **GET** /api/v1/accounts/{id}/statuses | 
[**apiV1AccountsIdUnblockPost**](AccountsApi.md#apiV1AccountsIdUnblockPost) | **POST** /api/v1/accounts/{id}/unblock | 
[**apiV1AccountsIdUnfollowPost**](AccountsApi.md#apiV1AccountsIdUnfollowPost) | **POST** /api/v1/accounts/{id}/unfollow | 
[**apiV1AccountsIdUnmutePost**](AccountsApi.md#apiV1AccountsIdUnmutePost) | **POST** /api/v1/accounts/{id}/unmute | 
[**apiV1AccountsIdUnpinPost**](AccountsApi.md#apiV1AccountsIdUnpinPost) | **POST** /api/v1/accounts/{id}/unpin | 
[**apiV1AccountsPost_0**](AccountsApi.md#apiV1AccountsPost_0) | **POST** /api/v1/accounts | 
[**apiV1AccountsRelationshipsGet**](AccountsApi.md#apiV1AccountsRelationshipsGet) | **GET** /api/v1/accounts/relationships | 
[**apiV1AccountsSearchGet**](AccountsApi.md#apiV1AccountsSearchGet) | **GET** /api/v1/accounts/search | 
[**apiV1AccountsUpdateCredentialsPatch**](AccountsApi.md#apiV1AccountsUpdateCredentialsPatch) | **PATCH** /api/v1/accounts/update_credentials | 
[**apiV1AccountsVerifyCredentialsGet**](AccountsApi.md#apiV1AccountsVerifyCredentialsGet) | **GET** /api/v1/accounts/verify_credentials | 



## apiV1AccountsIdBlockPost

> Relationship apiV1AccountsIdBlockPost(id)



Block the given account. Clients should filter statuses from this account if received (e.g. due to a boost in the Home timeline).

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdBlockPost(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdFeaturedTagsGet

> [FeaturedTag] apiV1AccountsIdFeaturedTagsGet(id)



Tags featured by this account.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdFeaturedTagsGet(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

[**[FeaturedTag]**](FeaturedTag.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdFollowPost

> Relationship apiV1AccountsIdFollowPost(id, opts)



Follow the given account. Can also be used to update whether to show reblogs or enable notifications.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
let opts = {
  'apiV1AccountsIdFollowPostRequest': new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1AccountsIdFollowPostRequest() // ApiV1AccountsIdFollowPostRequest | 
};
apiInstance.apiV1AccountsIdFollowPost(id, opts, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 
 **apiV1AccountsIdFollowPostRequest** | [**ApiV1AccountsIdFollowPostRequest**](ApiV1AccountsIdFollowPostRequest.md)|  | [optional] 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/form-data
- **Accept**: application/json


## apiV1AccountsIdFollowersGet

> [Account] apiV1AccountsIdFollowersGet(id, opts)



Accounts which follow the given account, if network is not hidden by the account owner.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
let opts = {
  'maxId': "maxId_example", // String | Internal parameter. Use HTTP `Link` header for pagination.
  'sinceId': "sinceId_example", // String | Internal parameter. Use HTTP `Link` header for pagination.
  'limit': 40 // Number | Maximum number of results to return. Defaults to 40.
};
apiInstance.apiV1AccountsIdFollowersGet(id, opts, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 
 **maxId** | **String**| Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination. | [optional] 
 **sinceId** | **String**| Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination. | [optional] 
 **limit** | **Number**| Maximum number of results to return. Defaults to 40. | [optional] [default to 40]

### Return type

[**[Account]**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdFollowingGet

> [Account] apiV1AccountsIdFollowingGet(id, opts)



Accounts which the given account is following, if network is not hidden by the account owner.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
let opts = {
  'maxId': "maxId_example", // String | Internal parameter. Use HTTP `Link` header for pagination.
  'sinceId': "sinceId_example", // String | Internal parameter. Use HTTP `Link` header for pagination.
  'limit': 40 // Number | Maximum number of results to return. Defaults to 40.
};
apiInstance.apiV1AccountsIdFollowingGet(id, opts, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 
 **maxId** | **String**| Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination. | [optional] 
 **sinceId** | **String**| Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination. | [optional] 
 **limit** | **Number**| Maximum number of results to return. Defaults to 40. | [optional] [default to 40]

### Return type

[**[Account]**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdGet

> Account apiV1AccountsIdGet(id)



### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdGet(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdIdentityProofsGet

> [IdentityProof] apiV1AccountsIdIdentityProofsGet(id)



Array of IdentityProof

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdIdentityProofsGet(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

[**[IdentityProof]**](IdentityProof.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdListsGet

> [Array] apiV1AccountsIdListsGet(id)



User lists that you have added this account to.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdListsGet(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

**[Array]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdMutePost

> Relationship apiV1AccountsIdMutePost(id, opts)



Mute the given account. Clients should filter statuses and notifications from this account, if received (e.g. due to a boost in the Home timeline).

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
let opts = {
  'apiV1AccountsIdMutePostRequest': new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1AccountsIdMutePostRequest() // ApiV1AccountsIdMutePostRequest | 
};
apiInstance.apiV1AccountsIdMutePost(id, opts, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 
 **apiV1AccountsIdMutePostRequest** | [**ApiV1AccountsIdMutePostRequest**](ApiV1AccountsIdMutePostRequest.md)|  | [optional] 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/form-data
- **Accept**: application/json


## apiV1AccountsIdNotePost

> Relationship apiV1AccountsIdNotePost(id, opts)



Sets a private note on a user.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
let opts = {
  'apiV1AccountsIdNotePostRequest': new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1AccountsIdNotePostRequest() // ApiV1AccountsIdNotePostRequest | 
};
apiInstance.apiV1AccountsIdNotePost(id, opts, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 
 **apiV1AccountsIdNotePostRequest** | [**ApiV1AccountsIdNotePostRequest**](ApiV1AccountsIdNotePostRequest.md)|  | [optional] 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/form-data
- **Accept**: application/json


## apiV1AccountsIdPinPost

> Relationship apiV1AccountsIdPinPost(id)



Add the given account to the user&#39;s featured profiles. (Featured profiles are currently shown on the user&#39;s own public profile.)

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdPinPost(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdStatusesGet

> [Status] apiV1AccountsIdStatusesGet(id)



Statuses posted to the given account.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdStatusesGet(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

[**[Status]**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdUnblockPost

> Relationship apiV1AccountsIdUnblockPost(id)



Block the given account. Clients should filter statuses from this account if received (e.g. due to a boost in the Home timeline).

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdUnblockPost(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdUnfollowPost

> Relationship apiV1AccountsIdUnfollowPost(id)



Unfollow the given account.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdUnfollowPost(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdUnmutePost

> Relationship apiV1AccountsIdUnmutePost(id)



Unmute the given account.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdUnmutePost(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsIdUnpinPost

> Relationship apiV1AccountsIdUnpinPost(id)



Remove the given account from the user&#39;s featured profiles.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = "id_example"; // String | The id of the account in the database
apiInstance.apiV1AccountsIdUnpinPost(id, (error, data, response) => {
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
 **id** | **String**| The id of the account in the database | 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsPost_0

> apiV1AccountsPost_0(opts)



Creates a user and account records. Returns an account access token for the app that initiated the request. The app should save this token for later, and should wait for the user to confirm their account by clicking a link in their email inbox.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let opts = {
  'apiV1AccountsPostRequest': new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1AccountsPostRequest() // ApiV1AccountsPostRequest | 
};
apiInstance.apiV1AccountsPost_0(opts, (error, data, response) => {
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


## apiV1AccountsRelationshipsGet

> [Relationship] apiV1AccountsRelationshipsGet(id)



Sets a private note on a user.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let id = ["null"]; // [String] | Array of account IDs to check
apiInstance.apiV1AccountsRelationshipsGet(id, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Array of account IDs to check | 

### Return type

[**[Relationship]**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsSearchGet

> [Account] apiV1AccountsSearchGet(q, opts)



Search for matching accounts by username or display name.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let q = "q_example"; // String | What to search for
let opts = {
  'limit': 40, // Number | Maximum number of results. Defaults to 40.
  'resolve': "resolve_example", // String | Attempt WebFinger lookup. Defaults to false. Use this when `q` is an exact address.
  'following': true // Boolean | Only who the user is following. Defaults to false.
};
apiInstance.apiV1AccountsSearchGet(q, opts, (error, data, response) => {
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
 **q** | **String**| What to search for | 
 **limit** | **Number**| Maximum number of results. Defaults to 40. | [optional] [default to 40]
 **resolve** | **String**| Attempt WebFinger lookup. Defaults to false. Use this when &#x60;q&#x60; is an exact address. | [optional] 
 **following** | **Boolean**| Only who the user is following. Defaults to false. | [optional] 

### Return type

[**[Account]**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AccountsUpdateCredentialsPatch

> Account apiV1AccountsUpdateCredentialsPatch(opts)



Update the user&#39;s display and preferences.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
let opts = {
  'apiV1AccountsUpdateCredentialsPatchRequest': new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1AccountsUpdateCredentialsPatchRequest() // ApiV1AccountsUpdateCredentialsPatchRequest | 
};
apiInstance.apiV1AccountsUpdateCredentialsPatch(opts, (error, data, response) => {
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
 **apiV1AccountsUpdateCredentialsPatchRequest** | [**ApiV1AccountsUpdateCredentialsPatchRequest**](ApiV1AccountsUpdateCredentialsPatchRequest.md)|  | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/form-data
- **Accept**: application/json


## apiV1AccountsVerifyCredentialsGet

> Account apiV1AccountsVerifyCredentialsGet()



Test to make sure that the user token works.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';
let defaultClient = MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.AccountsApi();
apiInstance.apiV1AccountsVerifyCredentialsGet((error, data, response) => {
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

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


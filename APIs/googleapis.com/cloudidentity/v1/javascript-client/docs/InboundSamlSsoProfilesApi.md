# CloudIdentityApi.InboundSamlSsoProfilesApi

All URIs are relative to *https://cloudidentity.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudidentityInboundSamlSsoProfilesCreate**](InboundSamlSsoProfilesApi.md#cloudidentityInboundSamlSsoProfilesCreate) | **POST** /v1/inboundSamlSsoProfiles | 
[**cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd**](InboundSamlSsoProfilesApi.md#cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd) | **POST** /v1/{parent}/idpCredentials:add | 
[**cloudidentityInboundSamlSsoProfilesIdpCredentialsList**](InboundSamlSsoProfilesApi.md#cloudidentityInboundSamlSsoProfilesIdpCredentialsList) | **GET** /v1/{parent}/idpCredentials | 
[**cloudidentityInboundSamlSsoProfilesList**](InboundSamlSsoProfilesApi.md#cloudidentityInboundSamlSsoProfilesList) | **GET** /v1/inboundSamlSsoProfiles | 



## cloudidentityInboundSamlSsoProfilesCreate

> Operation cloudidentityInboundSamlSsoProfilesCreate(opts)



Creates an InboundSamlSsoProfile for a customer.

### Example

```javascript
import CloudIdentityApi from 'cloud_identity_api';
let defaultClient = CloudIdentityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudIdentityApi.InboundSamlSsoProfilesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'inboundSamlSsoProfile': new CloudIdentityApi.InboundSamlSsoProfile() // InboundSamlSsoProfile | 
};
apiInstance.cloudidentityInboundSamlSsoProfilesCreate(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **inboundSamlSsoProfile** | [**InboundSamlSsoProfile**](InboundSamlSsoProfile.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd

> Operation cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd(parent, opts)



Adds an IdpCredential. Up to 2 credentials are allowed.

### Example

```javascript
import CloudIdentityApi from 'cloud_identity_api';
let defaultClient = CloudIdentityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudIdentityApi.InboundSamlSsoProfilesApi();
let parent = "parent_example"; // String | Required. The InboundSamlSsoProfile that owns the IdpCredential. Format: `inboundSamlSsoProfiles/{sso_profile_id}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'addIdpCredentialRequest': new CloudIdentityApi.AddIdpCredentialRequest() // AddIdpCredentialRequest | 
};
apiInstance.cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The InboundSamlSsoProfile that owns the IdpCredential. Format: &#x60;inboundSamlSsoProfiles/{sso_profile_id}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **addIdpCredentialRequest** | [**AddIdpCredentialRequest**](AddIdpCredentialRequest.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudidentityInboundSamlSsoProfilesIdpCredentialsList

> ListIdpCredentialsResponse cloudidentityInboundSamlSsoProfilesIdpCredentialsList(parent, opts)



Returns a list of IdpCredentials in an InboundSamlSsoProfile.

### Example

```javascript
import CloudIdentityApi from 'cloud_identity_api';
let defaultClient = CloudIdentityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudIdentityApi.InboundSamlSsoProfilesApi();
let parent = "parent_example"; // String | Required. The parent, which owns this collection of `IdpCredential`s. Format: `inboundSamlSsoProfiles/{sso_profile_id}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of `IdpCredential`s to return. The service may return fewer than this value.
  'pageToken': "pageToken_example" // String | A page token, received from a previous `ListIdpCredentials` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListIdpCredentials` must match the call that provided the page token.
};
apiInstance.cloudidentityInboundSamlSsoProfilesIdpCredentialsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent, which owns this collection of &#x60;IdpCredential&#x60;s. Format: &#x60;inboundSamlSsoProfiles/{sso_profile_id}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of &#x60;IdpCredential&#x60;s to return. The service may return fewer than this value. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListIdpCredentials&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListIdpCredentials&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**ListIdpCredentialsResponse**](ListIdpCredentialsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityInboundSamlSsoProfilesList

> ListInboundSamlSsoProfilesResponse cloudidentityInboundSamlSsoProfilesList(opts)



Lists InboundSamlSsoProfiles for a customer.

### Example

```javascript
import CloudIdentityApi from 'cloud_identity_api';
let defaultClient = CloudIdentityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudIdentityApi.InboundSamlSsoProfilesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | A [Common Expression Language](https://github.com/google/cel-spec) expression to filter the results. The only supported filter is filtering by customer. For example: `customer==\"customers/C0123abc\"`. Omitting the filter or specifying a filter of `customer==\"customers/my_customer\"` will return the profiles for the customer that the caller (authenticated user) belongs to.
  'pageSize': 56, // Number | The maximum number of InboundSamlSsoProfiles to return. The service may return fewer than this value. If omitted (or defaulted to zero) the server will use a sensible default. This default may change over time. The maximum allowed value is 100. Requests with page_size greater than that will be silently interpreted as having this maximum value.
  'pageToken': "pageToken_example" // String | A page token, received from a previous `ListInboundSamlSsoProfiles` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListInboundSamlSsoProfiles` must match the call that provided the page token.
};
apiInstance.cloudidentityInboundSamlSsoProfilesList(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| A [Common Expression Language](https://github.com/google/cel-spec) expression to filter the results. The only supported filter is filtering by customer. For example: &#x60;customer&#x3D;&#x3D;\&quot;customers/C0123abc\&quot;&#x60;. Omitting the filter or specifying a filter of &#x60;customer&#x3D;&#x3D;\&quot;customers/my_customer\&quot;&#x60; will return the profiles for the customer that the caller (authenticated user) belongs to. | [optional] 
 **pageSize** | **Number**| The maximum number of InboundSamlSsoProfiles to return. The service may return fewer than this value. If omitted (or defaulted to zero) the server will use a sensible default. This default may change over time. The maximum allowed value is 100. Requests with page_size greater than that will be silently interpreted as having this maximum value. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListInboundSamlSsoProfiles&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListInboundSamlSsoProfiles&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**ListInboundSamlSsoProfilesResponse**](ListInboundSamlSsoProfilesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


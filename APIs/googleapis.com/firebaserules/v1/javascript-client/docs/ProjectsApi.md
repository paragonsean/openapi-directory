# FirebaseRulesApi.ProjectsApi

All URIs are relative to *https://firebaserules.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firebaserulesProjectsReleasesCreate**](ProjectsApi.md#firebaserulesProjectsReleasesCreate) | **POST** /v1/{name}/releases | 
[**firebaserulesProjectsReleasesGetExecutable**](ProjectsApi.md#firebaserulesProjectsReleasesGetExecutable) | **GET** /v1/{name}:getExecutable | 
[**firebaserulesProjectsReleasesList**](ProjectsApi.md#firebaserulesProjectsReleasesList) | **GET** /v1/{name}/releases | 
[**firebaserulesProjectsReleasesPatch**](ProjectsApi.md#firebaserulesProjectsReleasesPatch) | **PATCH** /v1/{name} | 
[**firebaserulesProjectsRulesetsCreate**](ProjectsApi.md#firebaserulesProjectsRulesetsCreate) | **POST** /v1/{name}/rulesets | 
[**firebaserulesProjectsRulesetsDelete**](ProjectsApi.md#firebaserulesProjectsRulesetsDelete) | **DELETE** /v1/{name} | 
[**firebaserulesProjectsRulesetsGet**](ProjectsApi.md#firebaserulesProjectsRulesetsGet) | **GET** /v1/{name} | 
[**firebaserulesProjectsRulesetsList**](ProjectsApi.md#firebaserulesProjectsRulesetsList) | **GET** /v1/{name}/rulesets | 
[**firebaserulesProjectsTest**](ProjectsApi.md#firebaserulesProjectsTest) | **POST** /v1/{name}:test | 



## firebaserulesProjectsReleasesCreate

> Release firebaserulesProjectsReleasesCreate(name, opts)



Create a &#x60;Release&#x60;. Release names should reflect the developer&#39;s deployment practices. For example, the release name may include the environment name, application name, application version, or any other name meaningful to the developer. Once a &#x60;Release&#x60; refers to a &#x60;Ruleset&#x60;, the rules can be enforced by Firebase Rules-enabled services. More than one &#x60;Release&#x60; may be &#39;live&#39; concurrently. Consider the following three &#x60;Release&#x60; names for &#x60;projects/foo&#x60; and the &#x60;Ruleset&#x60; to which they refer. Release Name -&gt; Ruleset Name * projects/foo/releases/prod -&gt; projects/foo/rulesets/uuid123 * projects/foo/releases/prod/beta -&gt; projects/foo/rulesets/uuid123 * projects/foo/releases/prod/v23 -&gt; projects/foo/rulesets/uuid456 The relationships reflect a &#x60;Ruleset&#x60; rollout in progress. The &#x60;prod&#x60; and &#x60;prod/beta&#x60; releases refer to the same &#x60;Ruleset&#x60;. However, &#x60;prod/v23&#x60; refers to a new &#x60;Ruleset&#x60;. The &#x60;Ruleset&#x60; reference for a &#x60;Release&#x60; may be updated using the UpdateRelease method.

### Example

```javascript
import FirebaseRulesApi from 'firebase_rules_api';
let defaultClient = FirebaseRulesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseRulesApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name for the project which owns this `Release`. Format: `projects/{project_id}`
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
  'release': new FirebaseRulesApi.Release() // Release | 
};
apiInstance.firebaserulesProjectsReleasesCreate(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name for the project which owns this &#x60;Release&#x60;. Format: &#x60;projects/{project_id}&#x60; | 
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
 **release** | [**Release**](Release.md)|  | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaserulesProjectsReleasesGetExecutable

> GetReleaseExecutableResponse firebaserulesProjectsReleasesGetExecutable(name, opts)



Get the &#x60;Release&#x60; executable to use when enforcing rules.

### Example

```javascript
import FirebaseRulesApi from 'firebase_rules_api';
let defaultClient = FirebaseRulesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseRulesApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name of the `Release`. Format: `projects/{project_id}/releases/{release_id}`
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
  'executableVersion': "executableVersion_example" // String | The requested runtime executable version. Defaults to FIREBASE_RULES_EXECUTABLE_V1.
};
apiInstance.firebaserulesProjectsReleasesGetExecutable(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name of the &#x60;Release&#x60;. Format: &#x60;projects/{project_id}/releases/{release_id}&#x60; | 
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
 **executableVersion** | **String**| The requested runtime executable version. Defaults to FIREBASE_RULES_EXECUTABLE_V1. | [optional] 

### Return type

[**GetReleaseExecutableResponse**](GetReleaseExecutableResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaserulesProjectsReleasesList

> ListReleasesResponse firebaserulesProjectsReleasesList(name, opts)



List the &#x60;Release&#x60; values for a project. This list may optionally be filtered by &#x60;Release&#x60; name, &#x60;Ruleset&#x60; name, &#x60;TestSuite&#x60; name, or any combination thereof.

### Example

```javascript
import FirebaseRulesApi from 'firebase_rules_api';
let defaultClient = FirebaseRulesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseRulesApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name for the project. Format: `projects/{project_id}`
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
  'filter': "filter_example", // String | `Release` filter. The list method supports filters with restrictions on the `Release.name`, and `Release.ruleset_name`. Example 1: A filter of 'name=prod*' might return `Release`s with names within 'projects/foo' prefixed with 'prod': Name -> Ruleset Name: * projects/foo/releases/prod -> projects/foo/rulesets/uuid1234 * projects/foo/releases/prod/v1 -> projects/foo/rulesets/uuid1234 * projects/foo/releases/prod/v2 -> projects/foo/rulesets/uuid8888 Example 2: A filter of `name=prod* ruleset_name=uuid1234` would return only `Release` instances for 'projects/foo' with names prefixed with 'prod' referring to the same `Ruleset` name of 'uuid1234': Name -> Ruleset Name: * projects/foo/releases/prod -> projects/foo/rulesets/1234 * projects/foo/releases/prod/v1 -> projects/foo/rulesets/1234 In the examples, the filter parameters refer to the search filters are relative to the project. Fully qualified prefixed may also be used.
  'pageSize': 56, // Number | Page size to load. Maximum of 100. Defaults to 10. Note: `page_size` is just a hint and the service may choose to load fewer than `page_size` results due to the size of the output. To traverse all of the releases, the caller should iterate until the `page_token` on the response is empty.
  'pageToken': "pageToken_example" // String | Next page token for the next batch of `Release` instances.
};
apiInstance.firebaserulesProjectsReleasesList(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name for the project. Format: &#x60;projects/{project_id}&#x60; | 
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
 **filter** | **String**| &#x60;Release&#x60; filter. The list method supports filters with restrictions on the &#x60;Release.name&#x60;, and &#x60;Release.ruleset_name&#x60;. Example 1: A filter of &#39;name&#x3D;prod*&#39; might return &#x60;Release&#x60;s with names within &#39;projects/foo&#39; prefixed with &#39;prod&#39;: Name -&gt; Ruleset Name: * projects/foo/releases/prod -&gt; projects/foo/rulesets/uuid1234 * projects/foo/releases/prod/v1 -&gt; projects/foo/rulesets/uuid1234 * projects/foo/releases/prod/v2 -&gt; projects/foo/rulesets/uuid8888 Example 2: A filter of &#x60;name&#x3D;prod* ruleset_name&#x3D;uuid1234&#x60; would return only &#x60;Release&#x60; instances for &#39;projects/foo&#39; with names prefixed with &#39;prod&#39; referring to the same &#x60;Ruleset&#x60; name of &#39;uuid1234&#39;: Name -&gt; Ruleset Name: * projects/foo/releases/prod -&gt; projects/foo/rulesets/1234 * projects/foo/releases/prod/v1 -&gt; projects/foo/rulesets/1234 In the examples, the filter parameters refer to the search filters are relative to the project. Fully qualified prefixed may also be used. | [optional] 
 **pageSize** | **Number**| Page size to load. Maximum of 100. Defaults to 10. Note: &#x60;page_size&#x60; is just a hint and the service may choose to load fewer than &#x60;page_size&#x60; results due to the size of the output. To traverse all of the releases, the caller should iterate until the &#x60;page_token&#x60; on the response is empty. | [optional] 
 **pageToken** | **String**| Next page token for the next batch of &#x60;Release&#x60; instances. | [optional] 

### Return type

[**ListReleasesResponse**](ListReleasesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaserulesProjectsReleasesPatch

> Release firebaserulesProjectsReleasesPatch(name, opts)



Update a &#x60;Release&#x60; via PATCH. Only updates to &#x60;ruleset_name&#x60; will be honored. &#x60;Release&#x60; rename is not supported. To create a &#x60;Release&#x60; use the CreateRelease method.

### Example

```javascript
import FirebaseRulesApi from 'firebase_rules_api';
let defaultClient = FirebaseRulesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseRulesApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name for the project which owns this `Release`. Format: `projects/{project_id}`
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
  'updateReleaseRequest': new FirebaseRulesApi.UpdateReleaseRequest() // UpdateReleaseRequest | 
};
apiInstance.firebaserulesProjectsReleasesPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name for the project which owns this &#x60;Release&#x60;. Format: &#x60;projects/{project_id}&#x60; | 
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
 **updateReleaseRequest** | [**UpdateReleaseRequest**](UpdateReleaseRequest.md)|  | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaserulesProjectsRulesetsCreate

> Ruleset firebaserulesProjectsRulesetsCreate(name, opts)



Create a &#x60;Ruleset&#x60; from &#x60;Source&#x60;. The &#x60;Ruleset&#x60; is given a unique generated name which is returned to the caller. &#x60;Source&#x60; containing syntactic or semantics errors will result in an error response indicating the first error encountered. For a detailed view of &#x60;Source&#x60; issues, use TestRuleset.

### Example

```javascript
import FirebaseRulesApi from 'firebase_rules_api';
let defaultClient = FirebaseRulesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseRulesApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name for Project which owns this `Ruleset`. Format: `projects/{project_id}`
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
  'ruleset': new FirebaseRulesApi.Ruleset() // Ruleset | 
};
apiInstance.firebaserulesProjectsRulesetsCreate(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name for Project which owns this &#x60;Ruleset&#x60;. Format: &#x60;projects/{project_id}&#x60; | 
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
 **ruleset** | [**Ruleset**](Ruleset.md)|  | [optional] 

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaserulesProjectsRulesetsDelete

> Object firebaserulesProjectsRulesetsDelete(name, opts)



Delete a &#x60;Ruleset&#x60; by resource name. If the &#x60;Ruleset&#x60; is referenced by a &#x60;Release&#x60; the operation will fail.

### Example

```javascript
import FirebaseRulesApi from 'firebase_rules_api';
let defaultClient = FirebaseRulesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseRulesApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name for the ruleset to delete. Format: `projects/{project_id}/rulesets/{ruleset_id}`
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
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.firebaserulesProjectsRulesetsDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name for the ruleset to delete. Format: &#x60;projects/{project_id}/rulesets/{ruleset_id}&#x60; | 
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

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaserulesProjectsRulesetsGet

> Ruleset firebaserulesProjectsRulesetsGet(name, opts)



Get a &#x60;Ruleset&#x60; by name including the full &#x60;Source&#x60; contents.

### Example

```javascript
import FirebaseRulesApi from 'firebase_rules_api';
let defaultClient = FirebaseRulesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseRulesApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name for the ruleset to get. Format: `projects/{project_id}/rulesets/{ruleset_id}`
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
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.firebaserulesProjectsRulesetsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name for the ruleset to get. Format: &#x60;projects/{project_id}/rulesets/{ruleset_id}&#x60; | 
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

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaserulesProjectsRulesetsList

> ListRulesetsResponse firebaserulesProjectsRulesetsList(name, opts)



List &#x60;Ruleset&#x60; metadata only and optionally filter the results by &#x60;Ruleset&#x60; name. The full &#x60;Source&#x60; contents of a &#x60;Ruleset&#x60; may be retrieved with GetRuleset.

### Example

```javascript
import FirebaseRulesApi from 'firebase_rules_api';
let defaultClient = FirebaseRulesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseRulesApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name for the project. Format: `projects/{project_id}`
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
  'filter': "filter_example", // String | `Ruleset` filter. The list method supports filters with restrictions on `Ruleset.name`. Filters on `Ruleset.create_time` should use the `date` function which parses strings that conform to the RFC 3339 date/time specifications. Example: `create_time > date(\"2017-01-01T00:00:00Z\") AND name=UUID-*`
  'pageSize': 56, // Number | Page size to load. Maximum of 100. Defaults to 10. Note: `page_size` is just a hint and the service may choose to load less than `page_size` due to the size of the output. To traverse all of the releases, caller should iterate until the `page_token` is empty.
  'pageToken': "pageToken_example" // String | Next page token for loading the next batch of `Ruleset` instances.
};
apiInstance.firebaserulesProjectsRulesetsList(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name for the project. Format: &#x60;projects/{project_id}&#x60; | 
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
 **filter** | **String**| &#x60;Ruleset&#x60; filter. The list method supports filters with restrictions on &#x60;Ruleset.name&#x60;. Filters on &#x60;Ruleset.create_time&#x60; should use the &#x60;date&#x60; function which parses strings that conform to the RFC 3339 date/time specifications. Example: &#x60;create_time &gt; date(\&quot;2017-01-01T00:00:00Z\&quot;) AND name&#x3D;UUID-*&#x60; | [optional] 
 **pageSize** | **Number**| Page size to load. Maximum of 100. Defaults to 10. Note: &#x60;page_size&#x60; is just a hint and the service may choose to load less than &#x60;page_size&#x60; due to the size of the output. To traverse all of the releases, caller should iterate until the &#x60;page_token&#x60; is empty. | [optional] 
 **pageToken** | **String**| Next page token for loading the next batch of &#x60;Ruleset&#x60; instances. | [optional] 

### Return type

[**ListRulesetsResponse**](ListRulesetsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaserulesProjectsTest

> TestRulesetResponse firebaserulesProjectsTest(name, opts)



Test &#x60;Source&#x60; for syntactic and semantic correctness. Issues present, if any, will be returned to the caller with a description, severity, and source location. The test method may be executed with &#x60;Source&#x60; or a &#x60;Ruleset&#x60; name. Passing &#x60;Source&#x60; is useful for unit testing new rules. Passing a &#x60;Ruleset&#x60; name is useful for regression testing an existing rule. The following is an example of &#x60;Source&#x60; that permits users to upload images to a bucket bearing their user id and matching the correct metadata: _*Example*_ // Users are allowed to subscribe and unsubscribe to the blog. service firebase.storage { match /users/{userId}/images/{imageName} { allow write: if userId &#x3D;&#x3D; request.auth.uid &amp;&amp; (imageName.matches(&#39;*.png$&#39;) || imageName.matches(&#39;*.jpg$&#39;)) &amp;&amp; resource.mimeType.matches(&#39;^image/&#39;) } }

### Example

```javascript
import FirebaseRulesApi from 'firebase_rules_api';
let defaultClient = FirebaseRulesApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseRulesApi.ProjectsApi();
let name = "name_example"; // String | Required. Tests may either provide `source` or a `Ruleset` resource name. For tests against `source`, the resource name must refer to the project: Format: `projects/{project_id}` For tests against a `Ruleset`, this must be the `Ruleset` resource name: Format: `projects/{project_id}/rulesets/{ruleset_id}`
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
  'testRulesetRequest': new FirebaseRulesApi.TestRulesetRequest() // TestRulesetRequest | 
};
apiInstance.firebaserulesProjectsTest(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Tests may either provide &#x60;source&#x60; or a &#x60;Ruleset&#x60; resource name. For tests against &#x60;source&#x60;, the resource name must refer to the project: Format: &#x60;projects/{project_id}&#x60; For tests against a &#x60;Ruleset&#x60;, this must be the &#x60;Ruleset&#x60; resource name: Format: &#x60;projects/{project_id}/rulesets/{ruleset_id}&#x60; | 
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
 **testRulesetRequest** | [**TestRulesetRequest**](TestRulesetRequest.md)|  | [optional] 

### Return type

[**TestRulesetResponse**](TestRulesetResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


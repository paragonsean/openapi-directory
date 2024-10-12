# OrganizationPolicyApi.OrganizationsApi

All URIs are relative to *https://orgpolicy.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgpolicyOrganizationsCustomConstraintsCreate**](OrganizationsApi.md#orgpolicyOrganizationsCustomConstraintsCreate) | **POST** /v2/{parent}/customConstraints | 
[**orgpolicyOrganizationsCustomConstraintsList**](OrganizationsApi.md#orgpolicyOrganizationsCustomConstraintsList) | **GET** /v2/{parent}/customConstraints | 



## orgpolicyOrganizationsCustomConstraintsCreate

> GoogleCloudOrgpolicyV2CustomConstraint orgpolicyOrganizationsCustomConstraintsCreate(parent, opts)



Creates a custom constraint. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.NOT_FOUND&#x60; if the organization does not exist. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.ALREADY_EXISTS&#x60; if the constraint already exists on the given organization.

### Example

```javascript
import OrganizationPolicyApi from 'organization_policy_api';
let defaultClient = OrganizationPolicyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OrganizationPolicyApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. Must be in the following form: * `organizations/{organization_id}`
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
  'googleCloudOrgpolicyV2CustomConstraint': new OrganizationPolicyApi.GoogleCloudOrgpolicyV2CustomConstraint() // GoogleCloudOrgpolicyV2CustomConstraint | 
};
apiInstance.orgpolicyOrganizationsCustomConstraintsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Must be in the following form: * &#x60;organizations/{organization_id}&#x60; | 
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
 **googleCloudOrgpolicyV2CustomConstraint** | [**GoogleCloudOrgpolicyV2CustomConstraint**](GoogleCloudOrgpolicyV2CustomConstraint.md)|  | [optional] 

### Return type

[**GoogleCloudOrgpolicyV2CustomConstraint**](GoogleCloudOrgpolicyV2CustomConstraint.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgpolicyOrganizationsCustomConstraintsList

> GoogleCloudOrgpolicyV2ListCustomConstraintsResponse orgpolicyOrganizationsCustomConstraintsList(parent, opts)



Retrieves all of the custom constraints that exist on a particular organization resource.

### Example

```javascript
import OrganizationPolicyApi from 'organization_policy_api';
let defaultClient = OrganizationPolicyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OrganizationPolicyApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The target Google Cloud resource that parents the set of custom constraints that will be returned from this call. Must be in one of the following forms: * `organizations/{organization_id}`
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
  'pageSize': 56, // Number | Size of the pages to be returned. This is currently unsupported and will be ignored. The server may at any point start using this field to limit page size.
  'pageToken': "pageToken_example" // String | Page token used to retrieve the next page. This is currently unsupported and will be ignored. The server may at any point start using this field.
};
apiInstance.orgpolicyOrganizationsCustomConstraintsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The target Google Cloud resource that parents the set of custom constraints that will be returned from this call. Must be in one of the following forms: * &#x60;organizations/{organization_id}&#x60; | 
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
 **pageSize** | **Number**| Size of the pages to be returned. This is currently unsupported and will be ignored. The server may at any point start using this field to limit page size. | [optional] 
 **pageToken** | **String**| Page token used to retrieve the next page. This is currently unsupported and will be ignored. The server may at any point start using this field. | [optional] 

### Return type

[**GoogleCloudOrgpolicyV2ListCustomConstraintsResponse**](GoogleCloudOrgpolicyV2ListCustomConstraintsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


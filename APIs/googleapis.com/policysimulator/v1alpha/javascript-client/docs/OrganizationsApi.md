# PolicySimulatorApi.OrganizationsApi

All URIs are relative to *https://policysimulator.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsCreate**](OrganizationsApi.md#policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsCreate) | **POST** /v1alpha/{parent}/orgPolicyViolationsPreviews | 
[**policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsGenerate**](OrganizationsApi.md#policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsGenerate) | **POST** /v1alpha/{parent}/orgPolicyViolationsPreviews:generate | 
[**policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsList**](OrganizationsApi.md#policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsList) | **GET** /v1alpha/{parent}/orgPolicyViolationsPreviews | 
[**policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsOrgPolicyViolationsList**](OrganizationsApi.md#policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsOrgPolicyViolationsList) | **GET** /v1alpha/{parent}/orgPolicyViolations | 



## policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsCreate

> GoogleLongrunningOperation policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsCreate(parent, opts)



CreateOrgPolicyViolationsPreview creates an OrgPolicyViolationsPreview for the proposed changes in the provided OrgPolicyViolationsPreview.OrgPolicyOverlay. The changes to OrgPolicy are specified by this &#x60;OrgPolicyOverlay&#x60;. The resources to scan are inferred from these specified changes.

### Example

```javascript
import PolicySimulatorApi from 'policy_simulator_api';
let defaultClient = PolicySimulatorApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicySimulatorApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The organization under which this OrgPolicyViolationsPreview will be created. Example: `organizations/my-example-org/locations/global`
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
  'orgPolicyViolationsPreviewId': "orgPolicyViolationsPreviewId_example", // String | Optional. An optional user-specified ID for the OrgPolicyViolationsPreview. If not provided, a random ID will be generated.
  'googleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview': new PolicySimulatorApi.GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview() // GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview | 
};
apiInstance.policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The organization under which this OrgPolicyViolationsPreview will be created. Example: &#x60;organizations/my-example-org/locations/global&#x60; | 
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
 **orgPolicyViolationsPreviewId** | **String**| Optional. An optional user-specified ID for the OrgPolicyViolationsPreview. If not provided, a random ID will be generated. | [optional] 
 **googleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview** | [**GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview**](GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsGenerate

> GoogleLongrunningOperation policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsGenerate(parent, opts)



GenerateOrgPolicyViolationsPreview generates an OrgPolicyViolationsPreview for the proposed changes in the provided OrgPolicyViolationsPreview.OrgPolicyOverlay. The changes to OrgPolicy are specified by this &#x60;OrgPolicyOverlay&#x60;. The resources to scan are inferred from these specified changes.

### Example

```javascript
import PolicySimulatorApi from 'policy_simulator_api';
let defaultClient = PolicySimulatorApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicySimulatorApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The organization under which this OrgPolicyViolationsPreview will be created. Example: `organizations/my-example-org/locations/global`
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
  'googleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview': new PolicySimulatorApi.GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview() // GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview | 
};
apiInstance.policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsGenerate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The organization under which this OrgPolicyViolationsPreview will be created. Example: &#x60;organizations/my-example-org/locations/global&#x60; | 
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
 **googleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview** | [**GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview**](GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsList

> GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponse policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsList(parent, opts)



ListOrgPolicyViolationsPreviews lists each OrgPolicyViolationsPreview in an organization. Each OrgPolicyViolationsPreview is available for at least 7 days.

### Example

```javascript
import PolicySimulatorApi from 'policy_simulator_api';
let defaultClient = PolicySimulatorApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicySimulatorApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The parent the violations are scoped to. Format: `organizations/{organization}/locations/{location}` Example: `organizations/my-example-org/locations/global`
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
  'pageSize': 56, // Number | Optional. The maximum number of items to return. The service may return fewer than this value. If unspecified, at most 5 items will be returned. The maximum value is 10; values above 10 will be coerced to 10.
  'pageToken': "pageToken_example" // String | Optional. A page token, received from a previous call. Provide this to retrieve the subsequent page. When paginating, all other parameters must match the call that provided the page token.
};
apiInstance.policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent the violations are scoped to. Format: &#x60;organizations/{organization}/locations/{location}&#x60; Example: &#x60;organizations/my-example-org/locations/global&#x60; | 
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
 **pageSize** | **Number**| Optional. The maximum number of items to return. The service may return fewer than this value. If unspecified, at most 5 items will be returned. The maximum value is 10; values above 10 will be coerced to 10. | [optional] 
 **pageToken** | **String**| Optional. A page token, received from a previous call. Provide this to retrieve the subsequent page. When paginating, all other parameters must match the call that provided the page token. | [optional] 

### Return type

[**GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponse**](GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsOrgPolicyViolationsList

> GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponse policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsOrgPolicyViolationsList(parent, opts)



ListOrgPolicyViolations lists the OrgPolicyViolations that are present in an OrgPolicyViolationsPreview.

### Example

```javascript
import PolicySimulatorApi from 'policy_simulator_api';
let defaultClient = PolicySimulatorApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicySimulatorApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The OrgPolicyViolationsPreview to get OrgPolicyViolations from. Format: organizations/{organization}/locations/{location}/orgPolicyViolationsPreviews/{orgPolicyViolationsPreview}
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
  'pageSize': 56, // Number | Optional. The maximum number of items to return. The service may return fewer than this value. If unspecified, at most 50 items will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
  'pageToken': "pageToken_example" // String | Optional. A page token, received from a previous call. Provide this to retrieve the subsequent page. When paginating, all other parameters must match the call that provided the page token.
};
apiInstance.policysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsOrgPolicyViolationsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The OrgPolicyViolationsPreview to get OrgPolicyViolations from. Format: organizations/{organization}/locations/{location}/orgPolicyViolationsPreviews/{orgPolicyViolationsPreview} | 
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
 **pageSize** | **Number**| Optional. The maximum number of items to return. The service may return fewer than this value. If unspecified, at most 50 items will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| Optional. A page token, received from a previous call. Provide this to retrieve the subsequent page. When paginating, all other parameters must match the call that provided the page token. | [optional] 

### Return type

[**GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponse**](GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


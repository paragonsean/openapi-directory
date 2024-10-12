# BeyondCorpApi.OrganizationsApi

All URIs are relative to *https://beyondcorp.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate) | **POST** /v1alpha/{parent}/browserDlpRules | 
[**beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList) | **GET** /v1alpha/{parent}/browserDlpRules | 
[**beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate) | **POST** /v1alpha/{parent}/partnerTenants | 
[**beyondcorpOrganizationsLocationsGlobalPartnerTenantsList**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsList) | **GET** /v1alpha/{parent}/partnerTenants | 
[**beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate) | **POST** /v1alpha/{parent}/proxyConfigs | 
[**beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList) | **GET** /v1alpha/{parent}/proxyConfigs | 
[**beyondcorpOrganizationsLocationsSubscriptionsCreate**](OrganizationsApi.md#beyondcorpOrganizationsLocationsSubscriptionsCreate) | **POST** /v1alpha/{parent}/subscriptions | 
[**beyondcorpOrganizationsLocationsSubscriptionsList**](OrganizationsApi.md#beyondcorpOrganizationsLocationsSubscriptionsList) | **GET** /v1alpha/{parent}/subscriptions | 



## beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate

> GoogleLongrunningOperation beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate(parent, opts)



Creates a new BrowserDlpRule in a given organization and PartnerTenant.

### Example

```javascript
import BeyondCorpApi from 'beyond_corp_api';
let defaultClient = BeyondCorpApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BeyondCorpApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The resource name of the BrowserDlpRule parent using the form: `organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}`
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
  'requestId': "requestId_example", // String | Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
  'googleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule': new BeyondCorpApi.GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule() // GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule | 
};
apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the BrowserDlpRule parent using the form: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60; | 
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
 **requestId** | **String**| Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). | [optional] 
 **googleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule** | [**GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule**](GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList

> GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponse beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList(parent, opts)



Lists BrowserDlpRules for PartnerTenant in a given organization.

### Example

```javascript
import BeyondCorpApi from 'beyond_corp_api';
let defaultClient = BeyondCorpApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BeyondCorpApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The parent partnerTenant to which the BrowserDlpRules belong. Format: `organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}`
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
apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent partnerTenant to which the BrowserDlpRules belong. Format: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60; | 
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

[**GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponse**](GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate

> GoogleLongrunningOperation beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate(parent, opts)



Creates a new BeyondCorp Enterprise partnerTenant in a given organization and can only be called by onboarded BeyondCorp Enterprise partner.

### Example

```javascript
import BeyondCorpApi from 'beyond_corp_api';
let defaultClient = BeyondCorpApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BeyondCorpApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The resource name of the parent organization using the form: `organizations/{organization_id}/locations/global`
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
  'requestId': "requestId_example", // String | Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
  'googleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant': new BeyondCorpApi.GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant() // GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant | 
};
apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the parent organization using the form: &#x60;organizations/{organization_id}/locations/global&#x60; | 
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
 **requestId** | **String**| Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). | [optional] 
 **googleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant** | [**GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant**](GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## beyondcorpOrganizationsLocationsGlobalPartnerTenantsList

> GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse beyondcorpOrganizationsLocationsGlobalPartnerTenantsList(parent, opts)



Lists PartnerTenants in a given organization.

### Example

```javascript
import BeyondCorpApi from 'beyond_corp_api';
let defaultClient = BeyondCorpApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BeyondCorpApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The parent organization to which the PartnerTenants belong. Format: `organizations/{organization_id}/locations/global`
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
  'filter': "filter_example", // String | Optional. A filter specifying constraints of a list operation. All fields in the PartnerTenant message are supported. For example, the following query will return the PartnerTenants with displayName \"test-tenant\" organizations/${ORG_ID}/locations/${LOCATION}/partnerTenants?filter=displayName=\"test-tenant\" Nested fields are also supported. The follow query will return PartnerTenants with internal_tenant_id \"1234\" organizations/${ORG_ID}/locations/${LOCATION}/partnerTenants?filter=partnerMetadata.internalTenantId=\"1234\" For more information, please refer to https://google.aip.dev/160.
  'orderBy': "orderBy_example", // String | Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
  'pageSize': 56, // Number | Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.
  'pageToken': "pageToken_example" // String | Optional. The next_page_token value returned from a previous ListPartnerTenantsResponse, if any.
};
apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent organization to which the PartnerTenants belong. Format: &#x60;organizations/{organization_id}/locations/global&#x60; | 
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
 **filter** | **String**| Optional. A filter specifying constraints of a list operation. All fields in the PartnerTenant message are supported. For example, the following query will return the PartnerTenants with displayName \&quot;test-tenant\&quot; organizations/${ORG_ID}/locations/${LOCATION}/partnerTenants?filter&#x3D;displayName&#x3D;\&quot;test-tenant\&quot; Nested fields are also supported. The follow query will return PartnerTenants with internal_tenant_id \&quot;1234\&quot; organizations/${ORG_ID}/locations/${LOCATION}/partnerTenants?filter&#x3D;partnerMetadata.internalTenantId&#x3D;\&quot;1234\&quot; For more information, please refer to https://google.aip.dev/160. | [optional] 
 **orderBy** | **String**| Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information. | [optional] 
 **pageSize** | **Number**| Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried. | [optional] 
 **pageToken** | **String**| Optional. The next_page_token value returned from a previous ListPartnerTenantsResponse, if any. | [optional] 

### Return type

[**GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse**](GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate

> GoogleLongrunningOperation beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate(parent, opts)



Creates a new BeyondCorp Enterprise ProxyConfig in a given organization and PartnerTenant. Can only be called by on onboarded Beyondcorp Enterprise partner.

### Example

```javascript
import BeyondCorpApi from 'beyond_corp_api';
let defaultClient = BeyondCorpApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BeyondCorpApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The resource name of the parent PartnerTenant using the form: `organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}`
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
  'requestId': "requestId_example", // String | Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
  'googleCloudBeyondcorpPartnerservicesV1alphaProxyConfig': new BeyondCorpApi.GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig() // GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig | 
};
apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the parent PartnerTenant using the form: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60; | 
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
 **requestId** | **String**| Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). | [optional] 
 **googleCloudBeyondcorpPartnerservicesV1alphaProxyConfig** | [**GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig**](GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList

> GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList(parent, opts)



Lists ProxyConfigs for PartnerTenant in a given organization.

### Example

```javascript
import BeyondCorpApi from 'beyond_corp_api';
let defaultClient = BeyondCorpApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BeyondCorpApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The parent organization to which the ProxyConfigs belong. Format: `organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}`
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
  'filter': "filter_example", // String | Optional. A filter specifying constraints of a list operation. All fields in the ProxyConfig message are supported. For example, the following query will return the ProxyConfigs with displayName \"test-config\" organizations/${ORG_ID}/locations/global/partnerTenants/${PARTNER_TENANT_ID}/proxyConfigs?filter=displayName=\"test-config\" Nested fields are also supported. The follow query will return ProxyConfigs with pacUri \"example.com/pac.pac\" organizations/${ORG_ID}/locations/global/partnerTenants/${PARTNER_TENANT_ID}/proxyConfigs?filter=routingInfo.pacUri=\"example.com/pac.pac\" For more information, please refer to https://google.aip.dev/160.
  'orderBy': "orderBy_example", // String | Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
  'pageSize': 56, // Number | Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.
  'pageToken': "pageToken_example" // String | Optional. The next_page_token value returned from a previous ListProxyConfigsRequest, if any.
};
apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent organization to which the ProxyConfigs belong. Format: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60; | 
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
 **filter** | **String**| Optional. A filter specifying constraints of a list operation. All fields in the ProxyConfig message are supported. For example, the following query will return the ProxyConfigs with displayName \&quot;test-config\&quot; organizations/${ORG_ID}/locations/global/partnerTenants/${PARTNER_TENANT_ID}/proxyConfigs?filter&#x3D;displayName&#x3D;\&quot;test-config\&quot; Nested fields are also supported. The follow query will return ProxyConfigs with pacUri \&quot;example.com/pac.pac\&quot; organizations/${ORG_ID}/locations/global/partnerTenants/${PARTNER_TENANT_ID}/proxyConfigs?filter&#x3D;routingInfo.pacUri&#x3D;\&quot;example.com/pac.pac\&quot; For more information, please refer to https://google.aip.dev/160. | [optional] 
 **orderBy** | **String**| Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information. | [optional] 
 **pageSize** | **Number**| Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried. | [optional] 
 **pageToken** | **String**| Optional. The next_page_token value returned from a previous ListProxyConfigsRequest, if any. | [optional] 

### Return type

[**GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse**](GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## beyondcorpOrganizationsLocationsSubscriptionsCreate

> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription beyondcorpOrganizationsLocationsSubscriptionsCreate(parent, opts)



Creates a new BeyondCorp Enterprise Subscription in a given organization. Location will always be global as BeyondCorp subscriptions are per organization.

### Example

```javascript
import BeyondCorpApi from 'beyond_corp_api';

let apiInstance = new BeyondCorpApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The resource name of the subscription location using the form: `organizations/{organization_id}/locations/{location}`
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
  'googleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription': new BeyondCorpApi.GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription() // GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription | 
};
apiInstance.beyondcorpOrganizationsLocationsSubscriptionsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the subscription location using the form: &#x60;organizations/{organization_id}/locations/{location}&#x60; | 
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
 **googleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription** | [**GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription**](GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription.md)|  | [optional] 

### Return type

[**GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription**](GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## beyondcorpOrganizationsLocationsSubscriptionsList

> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse beyondcorpOrganizationsLocationsSubscriptionsList(parent, opts)



Lists Subscriptions in a given organization and location.

### Example

```javascript
import BeyondCorpApi from 'beyond_corp_api';

let apiInstance = new BeyondCorpApi.OrganizationsApi();
let parent = "parent_example"; // String | Required. The resource name of Subscription using the form: `organizations/{organization_id}/locations/{location}`
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
  'pageSize': 56, // Number | Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.
  'pageToken': "pageToken_example" // String | Optional. The next_page_token value returned from a previous ListSubscriptionsRequest, if any.
};
apiInstance.beyondcorpOrganizationsLocationsSubscriptionsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of Subscription using the form: &#x60;organizations/{organization_id}/locations/{location}&#x60; | 
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
 **pageSize** | **Number**| Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried. | [optional] 
 **pageToken** | **String**| Optional. The next_page_token value returned from a previous ListSubscriptionsRequest, if any. | [optional] 

### Return type

[**GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse**](GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# AnalyticsHubApi.OrganizationsApi

All URIs are relative to *https://analyticshub.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyticshubOrganizationsLocationsDataExchangesList**](OrganizationsApi.md#analyticshubOrganizationsLocationsDataExchangesList) | **GET** /v1/{organization}/dataExchanges | 



## analyticshubOrganizationsLocationsDataExchangesList

> ListOrgDataExchangesResponse analyticshubOrganizationsLocationsDataExchangesList(organization, opts)



Lists all data exchanges from projects in a given organization and location.

### Example

```javascript
import AnalyticsHubApi from 'analytics_hub_api';
let defaultClient = AnalyticsHubApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AnalyticsHubApi.OrganizationsApi();
let organization = "organization_example"; // String | Required. The organization resource path of the projects containing DataExchanges. e.g. `organizations/myorg/locations/US`.
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
  'pageSize': 56, // Number | The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection.
  'pageToken': "pageToken_example" // String | Page token, returned by a previous call, to request the next page of results.
};
apiInstance.analyticshubOrganizationsLocationsDataExchangesList(organization, opts, (error, data, response) => {
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
 **organization** | **String**| Required. The organization resource path of the projects containing DataExchanges. e.g. &#x60;organizations/myorg/locations/US&#x60;. | 
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
 **pageSize** | **Number**| The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection. | [optional] 
 **pageToken** | **String**| Page token, returned by a previous call, to request the next page of results. | [optional] 

### Return type

[**ListOrgDataExchangesResponse**](ListOrgDataExchangesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# CloudResourceManagerApi.OrganizationsApi

All URIs are relative to *https://cloudresourcemanager.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudresourcemanagerOrganizationsSearch**](OrganizationsApi.md#cloudresourcemanagerOrganizationsSearch) | **GET** /v3/organizations:search | 



## cloudresourcemanagerOrganizationsSearch

> SearchOrganizationsResponse cloudresourcemanagerOrganizationsSearch(opts)



Searches organization resources that are visible to the user and satisfy the specified filter. This method returns organizations in an unspecified order. New organizations do not necessarily appear at the end of the results, and may take a small amount of time to appear. Search will only return organizations on which the user has the permission &#x60;resourcemanager.organizations.get&#x60; or has super admin privileges.

### Example

```javascript
import CloudResourceManagerApi from 'cloud_resource_manager_api';
let defaultClient = CloudResourceManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudResourceManagerApi.OrganizationsApi();
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
  'pageSize': 56, // Number | Optional. The maximum number of organizations to return in the response. The server can return fewer organizations than requested. If unspecified, server picks an appropriate default.
  'pageToken': "pageToken_example", // String | Optional. A pagination token returned from a previous call to `SearchOrganizations` that indicates from where listing should continue.
  'query': "query_example" // String | Optional. An optional query string used to filter the Organizations to return in the response. Query rules are case-insensitive. ``` | Field | Description | |------------------|--------------------------------------------| | directoryCustomerId, owner.directoryCustomerId | Filters by directory customer id. | | domain | Filters by domain. | ``` Organizations may be queried by `directoryCustomerId` or by `domain`, where the domain is a G Suite domain, for example: * Query `directorycustomerid:123456789` returns Organization resources with `owner.directory_customer_id` equal to `123456789`. * Query `domain:google.com` returns Organization resources corresponding to the domain `google.com`.
};
apiInstance.cloudresourcemanagerOrganizationsSearch(opts, (error, data, response) => {
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
 **pageSize** | **Number**| Optional. The maximum number of organizations to return in the response. The server can return fewer organizations than requested. If unspecified, server picks an appropriate default. | [optional] 
 **pageToken** | **String**| Optional. A pagination token returned from a previous call to &#x60;SearchOrganizations&#x60; that indicates from where listing should continue. | [optional] 
 **query** | **String**| Optional. An optional query string used to filter the Organizations to return in the response. Query rules are case-insensitive. &#x60;&#x60;&#x60; | Field | Description | |------------------|--------------------------------------------| | directoryCustomerId, owner.directoryCustomerId | Filters by directory customer id. | | domain | Filters by domain. | &#x60;&#x60;&#x60; Organizations may be queried by &#x60;directoryCustomerId&#x60; or by &#x60;domain&#x60;, where the domain is a G Suite domain, for example: * Query &#x60;directorycustomerid:123456789&#x60; returns Organization resources with &#x60;owner.directory_customer_id&#x60; equal to &#x60;123456789&#x60;. * Query &#x60;domain:google.com&#x60; returns Organization resources corresponding to the domain &#x60;google.com&#x60;. | [optional] 

### Return type

[**SearchOrganizationsResponse**](SearchOrganizationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


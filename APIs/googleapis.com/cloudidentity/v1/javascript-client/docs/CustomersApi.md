# CloudIdentityApi.CustomersApi

All URIs are relative to *https://cloudidentity.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudidentityCustomersUserinvitationsCancel**](CustomersApi.md#cloudidentityCustomersUserinvitationsCancel) | **POST** /v1/{name}:cancel | 
[**cloudidentityCustomersUserinvitationsIsInvitableUser**](CustomersApi.md#cloudidentityCustomersUserinvitationsIsInvitableUser) | **GET** /v1/{name}:isInvitableUser | 
[**cloudidentityCustomersUserinvitationsList**](CustomersApi.md#cloudidentityCustomersUserinvitationsList) | **GET** /v1/{parent}/userinvitations | 
[**cloudidentityCustomersUserinvitationsSend**](CustomersApi.md#cloudidentityCustomersUserinvitationsSend) | **POST** /v1/{name}:send | 



## cloudidentityCustomersUserinvitationsCancel

> Operation cloudidentityCustomersUserinvitationsCancel(name, opts)



Cancels a UserInvitation that was already sent.

### Example

```javascript
import CloudIdentityApi from 'cloud_identity_api';

let apiInstance = new CloudIdentityApi.CustomersApi();
let name = "name_example"; // String | Required. `UserInvitation` name in the format `customers/{customer}/userinvitations/{user_email_address}`
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
  'body': {key: null} // Object | 
};
apiInstance.cloudidentityCustomersUserinvitationsCancel(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. &#x60;UserInvitation&#x60; name in the format &#x60;customers/{customer}/userinvitations/{user_email_address}&#x60; | 
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
 **body** | **Object**|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudidentityCustomersUserinvitationsIsInvitableUser

> IsInvitableUserResponse cloudidentityCustomersUserinvitationsIsInvitableUser(name, opts)



Verifies whether a user account is eligible to receive a UserInvitation (is an unmanaged account). Eligibility is based on the following criteria: * the email address is a consumer account and it&#39;s the primary email address of the account, and * the domain of the email address matches an existing verified Google Workspace or Cloud Identity domain If both conditions are met, the user is eligible. **Note:** This method is not supported for Workspace Essentials customers.

### Example

```javascript
import CloudIdentityApi from 'cloud_identity_api';

let apiInstance = new CloudIdentityApi.CustomersApi();
let name = "name_example"; // String | Required. `UserInvitation` name in the format `customers/{customer}/userinvitations/{user_email_address}`
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
apiInstance.cloudidentityCustomersUserinvitationsIsInvitableUser(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. &#x60;UserInvitation&#x60; name in the format &#x60;customers/{customer}/userinvitations/{user_email_address}&#x60; | 
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

[**IsInvitableUserResponse**](IsInvitableUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityCustomersUserinvitationsList

> ListUserInvitationsResponse cloudidentityCustomersUserinvitationsList(parent, opts)



Retrieves a list of UserInvitation resources. **Note:** New consumer accounts with the customer&#39;s verified domain created within the previous 48 hours will not appear in the result. This delay also applies to newly-verified domains.

### Example

```javascript
import CloudIdentityApi from 'cloud_identity_api';

let apiInstance = new CloudIdentityApi.CustomersApi();
let parent = "parent_example"; // String | Required. The customer ID of the Google Workspace or Cloud Identity account the UserInvitation resources are associated with.
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
  'filter': "filter_example", // String | Optional. A query string for filtering `UserInvitation` results by their current state, in the format: `\"state=='invited'\"`.
  'orderBy': "orderBy_example", // String | Optional. The sort order of the list results. You can sort the results in descending order based on either email or last update timestamp but not both, using `order_by=\"email desc\"`. Currently, sorting is supported for `update_time asc`, `update_time desc`, `email asc`, and `email desc`. If not specified, results will be returned based on `email asc` order.
  'pageSize': 56, // Number | Optional. The maximum number of UserInvitation resources to return. If unspecified, at most 100 resources will be returned. The maximum value is 200; values above 200 will be set to 200.
  'pageToken': "pageToken_example" // String | Optional. A page token, received from a previous `ListUserInvitations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListBooks` must match the call that provided the page token.
};
apiInstance.cloudidentityCustomersUserinvitationsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The customer ID of the Google Workspace or Cloud Identity account the UserInvitation resources are associated with. | 
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
 **filter** | **String**| Optional. A query string for filtering &#x60;UserInvitation&#x60; results by their current state, in the format: &#x60;\&quot;state&#x3D;&#x3D;&#39;invited&#39;\&quot;&#x60;. | [optional] 
 **orderBy** | **String**| Optional. The sort order of the list results. You can sort the results in descending order based on either email or last update timestamp but not both, using &#x60;order_by&#x3D;\&quot;email desc\&quot;&#x60;. Currently, sorting is supported for &#x60;update_time asc&#x60;, &#x60;update_time desc&#x60;, &#x60;email asc&#x60;, and &#x60;email desc&#x60;. If not specified, results will be returned based on &#x60;email asc&#x60; order. | [optional] 
 **pageSize** | **Number**| Optional. The maximum number of UserInvitation resources to return. If unspecified, at most 100 resources will be returned. The maximum value is 200; values above 200 will be set to 200. | [optional] 
 **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListUserInvitations&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListBooks&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**ListUserInvitationsResponse**](ListUserInvitationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityCustomersUserinvitationsSend

> Operation cloudidentityCustomersUserinvitationsSend(name, opts)



Sends a UserInvitation to email. If the &#x60;UserInvitation&#x60; does not exist for this request and it is a valid request, the request creates a &#x60;UserInvitation&#x60;. **Note:** The &#x60;get&#x60; and &#x60;list&#x60; methods have a 48-hour delay where newly-created consumer accounts will not appear in the results. You can still send a &#x60;UserInvitation&#x60; to those accounts if you know the unmanaged email address and IsInvitableUser&#x3D;&#x3D;True.

### Example

```javascript
import CloudIdentityApi from 'cloud_identity_api';

let apiInstance = new CloudIdentityApi.CustomersApi();
let name = "name_example"; // String | Required. `UserInvitation` name in the format `customers/{customer}/userinvitations/{user_email_address}`
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
  'body': {key: null} // Object | 
};
apiInstance.cloudidentityCustomersUserinvitationsSend(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. &#x60;UserInvitation&#x60; name in the format &#x60;customers/{customer}/userinvitations/{user_email_address}&#x60; | 
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
 **body** | **Object**|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


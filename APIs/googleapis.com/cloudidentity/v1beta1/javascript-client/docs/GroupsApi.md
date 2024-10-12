# CloudIdentityApi.GroupsApi

All URIs are relative to *https://cloudidentity.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudidentityGroupsCreate**](GroupsApi.md#cloudidentityGroupsCreate) | **POST** /v1beta1/groups | 
[**cloudidentityGroupsList**](GroupsApi.md#cloudidentityGroupsList) | **GET** /v1beta1/groups | 
[**cloudidentityGroupsLookup**](GroupsApi.md#cloudidentityGroupsLookup) | **GET** /v1beta1/groups:lookup | 
[**cloudidentityGroupsMembershipsCheckTransitiveMembership**](GroupsApi.md#cloudidentityGroupsMembershipsCheckTransitiveMembership) | **GET** /v1beta1/{parent}/memberships:checkTransitiveMembership | 
[**cloudidentityGroupsMembershipsCreate**](GroupsApi.md#cloudidentityGroupsMembershipsCreate) | **POST** /v1beta1/{parent}/memberships | 
[**cloudidentityGroupsMembershipsGetMembershipGraph**](GroupsApi.md#cloudidentityGroupsMembershipsGetMembershipGraph) | **GET** /v1beta1/{parent}/memberships:getMembershipGraph | 
[**cloudidentityGroupsMembershipsLookup**](GroupsApi.md#cloudidentityGroupsMembershipsLookup) | **GET** /v1beta1/{parent}/memberships:lookup | 
[**cloudidentityGroupsMembershipsModifyMembershipRoles**](GroupsApi.md#cloudidentityGroupsMembershipsModifyMembershipRoles) | **POST** /v1beta1/{name}:modifyMembershipRoles | 
[**cloudidentityGroupsMembershipsSearchDirectGroups**](GroupsApi.md#cloudidentityGroupsMembershipsSearchDirectGroups) | **GET** /v1beta1/{parent}/memberships:searchDirectGroups | 
[**cloudidentityGroupsMembershipsSearchTransitiveGroups**](GroupsApi.md#cloudidentityGroupsMembershipsSearchTransitiveGroups) | **GET** /v1beta1/{parent}/memberships:searchTransitiveGroups | 
[**cloudidentityGroupsMembershipsSearchTransitiveMemberships**](GroupsApi.md#cloudidentityGroupsMembershipsSearchTransitiveMemberships) | **GET** /v1beta1/{parent}/memberships:searchTransitiveMemberships | 
[**cloudidentityGroupsSearch**](GroupsApi.md#cloudidentityGroupsSearch) | **GET** /v1beta1/groups:search | 



## cloudidentityGroupsCreate

> Operation cloudidentityGroupsCreate(opts)



Creates a &#x60;Group&#x60;.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
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
  'initialGroupConfig': "initialGroupConfig_example", // String | Required. The initial configuration option for the `Group`.
  'group': new CloudIdentityApi.Group() // Group | 
};
apiInstance.cloudidentityGroupsCreate(opts, (error, data, response) => {
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
 **initialGroupConfig** | **String**| Required. The initial configuration option for the &#x60;Group&#x60;. | [optional] 
 **group** | [**Group**](Group.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudidentityGroupsList

> ListGroupsResponse cloudidentityGroupsList(opts)



Lists the &#x60;Group&#x60; resources under a customer or namespace.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
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
  'pageSize': 56, // Number | The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a `next_page_token`. If unspecified, defaults to 200 for `View.BASIC` and to 50 for `View.FULL`. Must not be greater than 1000 for `View.BASIC` or 500 for `View.FULL`.
  'pageToken': "pageToken_example", // String | The `next_page_token` value returned from a previous list request, if any.
  'parent': "parent_example", // String | Required. The parent resource under which to list all `Group` resources. Must be of the form `identitysources/{identity_source_id}` for external- identity-mapped groups or `customers/{customer_id}` for Google Groups. The `customer_id` must begin with \"C\" (for example, 'C046psxkn'). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793)
  'view': "view_example" // String | The level of detail to be returned. If unspecified, defaults to `View.BASIC`.
};
apiInstance.cloudidentityGroupsList(opts, (error, data, response) => {
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
 **pageSize** | **Number**| The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a &#x60;next_page_token&#x60;. If unspecified, defaults to 200 for &#x60;View.BASIC&#x60; and to 50 for &#x60;View.FULL&#x60;. Must not be greater than 1000 for &#x60;View.BASIC&#x60; or 500 for &#x60;View.FULL&#x60;. | [optional] 
 **pageToken** | **String**| The &#x60;next_page_token&#x60; value returned from a previous list request, if any. | [optional] 
 **parent** | **String**| Required. The parent resource under which to list all &#x60;Group&#x60; resources. Must be of the form &#x60;identitysources/{identity_source_id}&#x60; for external- identity-mapped groups or &#x60;customers/{customer_id}&#x60; for Google Groups. The &#x60;customer_id&#x60; must begin with \&quot;C\&quot; (for example, &#39;C046psxkn&#39;). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793) | [optional] 
 **view** | **String**| The level of detail to be returned. If unspecified, defaults to &#x60;View.BASIC&#x60;. | [optional] 

### Return type

[**ListGroupsResponse**](ListGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityGroupsLookup

> LookupGroupNameResponse cloudidentityGroupsLookup(opts)



Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a &#x60;Group&#x60; by its &#x60;EntityKey&#x60;.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
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
  'groupKeyId': "groupKeyId_example", // String | The ID of the entity. For Google-managed entities, the `id` must be the email address of an existing group or user. For external-identity-mapped entities, the `id` must be a string conforming to the Identity Source's requirements. Must be unique within a `namespace`.
  'groupKeyNamespace': "groupKeyNamespace_example" // String | The namespace in which the entity exists. If not specified, the `EntityKey` represents a Google-managed entity such as a Google user or a Google Group. If specified, the `EntityKey` represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of `identitysources/{identity_source_id}`.
};
apiInstance.cloudidentityGroupsLookup(opts, (error, data, response) => {
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
 **groupKeyId** | **String**| The ID of the entity. For Google-managed entities, the &#x60;id&#x60; must be the email address of an existing group or user. For external-identity-mapped entities, the &#x60;id&#x60; must be a string conforming to the Identity Source&#39;s requirements. Must be unique within a &#x60;namespace&#x60;. | [optional] 
 **groupKeyNamespace** | **String**| The namespace in which the entity exists. If not specified, the &#x60;EntityKey&#x60; represents a Google-managed entity such as a Google user or a Google Group. If specified, the &#x60;EntityKey&#x60; represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of &#x60;identitysources/{identity_source_id}&#x60;. | [optional] 

### Return type

[**LookupGroupNameResponse**](LookupGroupNameResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityGroupsMembershipsCheckTransitiveMembership

> CheckTransitiveMembershipResponse cloudidentityGroupsMembershipsCheckTransitiveMembership(parent, opts)



Check a potential member for membership in a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. A member has membership to a group as long as there is a single viewable transitive membership between the group and the member. The actor must have view permissions to at least one transitive membership between the member and group.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
let parent = "parent_example"; // String | [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to check the transitive membership in. Format: `groups/{group_id}`, where `group_id` is the unique id assigned to the Group to which the Membership belongs to.
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
  'query': "query_example" // String | Required. A CEL expression that MUST include member specification. This is a `required` field. Certain groups are uniquely identified by both a 'member_key_id' and a 'member_key_namespace', which requires an additional query input: 'member_key_namespace'. Example query: `member_key_id == 'member_key_id_value'`
};
apiInstance.cloudidentityGroupsMembershipsCheckTransitiveMembership(parent, opts, (error, data, response) => {
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
 **parent** | **String**| [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to check the transitive membership in. Format: &#x60;groups/{group_id}&#x60;, where &#x60;group_id&#x60; is the unique id assigned to the Group to which the Membership belongs to. | 
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
 **query** | **String**| Required. A CEL expression that MUST include member specification. This is a &#x60;required&#x60; field. Certain groups are uniquely identified by both a &#39;member_key_id&#39; and a &#39;member_key_namespace&#39;, which requires an additional query input: &#39;member_key_namespace&#39;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39;&#x60; | [optional] 

### Return type

[**CheckTransitiveMembershipResponse**](CheckTransitiveMembershipResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityGroupsMembershipsCreate

> Operation cloudidentityGroupsMembershipsCreate(parent, opts)



Creates a &#x60;Membership&#x60;.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
let parent = "parent_example"; // String | Required. The parent `Group` resource under which to create the `Membership`. Must be of the form `groups/{group_id}`.
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
  'membership': new CloudIdentityApi.Membership() // Membership | 
};
apiInstance.cloudidentityGroupsMembershipsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent &#x60;Group&#x60; resource under which to create the &#x60;Membership&#x60;. Must be of the form &#x60;groups/{group_id}&#x60;. | 
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
 **membership** | [**Membership**](Membership.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudidentityGroupsMembershipsGetMembershipGraph

> Operation cloudidentityGroupsMembershipsGetMembershipGraph(parent, opts)



Get a membership graph of just a member or both a member and a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. Given a member, the response will contain all membership paths from the member. Given both a group and a member, the response will contain all membership paths between the group and the member.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
let parent = "parent_example"; // String | Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: `groups/{group_id}`, where `group_id` is the unique ID assigned to the Group to which the Membership belongs to. group_id can be a wildcard collection id \"-\". When a group_id is specified, the membership graph will be constrained to paths between the member (defined in the query) and the parent. If a wildcard collection is provided, all membership paths connected to the member will be returned.
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
  'query': "query_example" // String | Required. A CEL expression that MUST include member specification AND label(s). Certain groups are uniquely identified by both a 'member_key_id' and a 'member_key_namespace', which requires an additional query input: 'member_key_namespace'. Example query: `member_key_id == 'member_key_id_value' && in labels`
};
apiInstance.cloudidentityGroupsMembershipsGetMembershipGraph(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: &#x60;groups/{group_id}&#x60;, where &#x60;group_id&#x60; is the unique ID assigned to the Group to which the Membership belongs to. group_id can be a wildcard collection id \&quot;-\&quot;. When a group_id is specified, the membership graph will be constrained to paths between the member (defined in the query) and the parent. If a wildcard collection is provided, all membership paths connected to the member will be returned. | 
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
 **query** | **String**| Required. A CEL expression that MUST include member specification AND label(s). Certain groups are uniquely identified by both a &#39;member_key_id&#39; and a &#39;member_key_namespace&#39;, which requires an additional query input: &#39;member_key_namespace&#39;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; in labels&#x60; | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityGroupsMembershipsLookup

> LookupMembershipNameResponse cloudidentityGroupsMembershipsLookup(parent, opts)



Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a &#x60;Membership&#x60; by its &#x60;EntityKey&#x60;.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
let parent = "parent_example"; // String | Required. The parent `Group` resource under which to lookup the `Membership` name. Must be of the form `groups/{group_id}`.
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
  'memberKeyId': "memberKeyId_example", // String | The ID of the entity. For Google-managed entities, the `id` must be the email address of an existing group or user. For external-identity-mapped entities, the `id` must be a string conforming to the Identity Source's requirements. Must be unique within a `namespace`.
  'memberKeyNamespace': "memberKeyNamespace_example" // String | The namespace in which the entity exists. If not specified, the `EntityKey` represents a Google-managed entity such as a Google user or a Google Group. If specified, the `EntityKey` represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of `identitysources/{identity_source_id}`.
};
apiInstance.cloudidentityGroupsMembershipsLookup(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent &#x60;Group&#x60; resource under which to lookup the &#x60;Membership&#x60; name. Must be of the form &#x60;groups/{group_id}&#x60;. | 
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
 **memberKeyId** | **String**| The ID of the entity. For Google-managed entities, the &#x60;id&#x60; must be the email address of an existing group or user. For external-identity-mapped entities, the &#x60;id&#x60; must be a string conforming to the Identity Source&#39;s requirements. Must be unique within a &#x60;namespace&#x60;. | [optional] 
 **memberKeyNamespace** | **String**| The namespace in which the entity exists. If not specified, the &#x60;EntityKey&#x60; represents a Google-managed entity such as a Google user or a Google Group. If specified, the &#x60;EntityKey&#x60; represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of &#x60;identitysources/{identity_source_id}&#x60;. | [optional] 

### Return type

[**LookupMembershipNameResponse**](LookupMembershipNameResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityGroupsMembershipsModifyMembershipRoles

> ModifyMembershipRolesResponse cloudidentityGroupsMembershipsModifyMembershipRoles(name, opts)



Modifies the &#x60;MembershipRole&#x60;s of a &#x60;Membership&#x60;.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
let name = "name_example"; // String | Required. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Membership` whose roles are to be modified. Must be of the form `groups/{group_id}/memberships/{membership_id}`.
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
  'modifyMembershipRolesRequest': new CloudIdentityApi.ModifyMembershipRolesRequest() // ModifyMembershipRolesRequest | 
};
apiInstance.cloudidentityGroupsMembershipsModifyMembershipRoles(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The [resource name](https://cloud.google.com/apis/design/resource_names) of the &#x60;Membership&#x60; whose roles are to be modified. Must be of the form &#x60;groups/{group_id}/memberships/{membership_id}&#x60;. | 
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
 **modifyMembershipRolesRequest** | [**ModifyMembershipRolesRequest**](ModifyMembershipRolesRequest.md)|  | [optional] 

### Return type

[**ModifyMembershipRolesResponse**](ModifyMembershipRolesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudidentityGroupsMembershipsSearchDirectGroups

> SearchDirectGroupsResponse cloudidentityGroupsMembershipsSearchDirectGroups(parent, opts)



Searches direct groups of a member.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
let parent = "parent_example"; // String | [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: groups/{group_id}, where group_id is always '-' as this API will search across all groups for a given member.
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
  'orderBy': "orderBy_example", // String | The ordering of membership relation for the display name or email in the response. The syntax for this field can be found at https://cloud.google.com/apis/design/design_patterns#sorting_order. Example: Sort by the ascending display name: order_by=\"group_name\" or order_by=\"group_name asc\". Sort by the descending display name: order_by=\"group_name desc\". Sort by the ascending group key: order_by=\"group_key\" or order_by=\"group_key asc\". Sort by the descending group key: order_by=\"group_key desc\".
  'pageSize': 56, // Number | The default page size is 200 (max 1000).
  'pageToken': "pageToken_example", // String | The next_page_token value returned from a previous list request, if any
  'query': "query_example" // String | Required. A CEL expression that MUST include member specification AND label(s). Users can search on label attributes of groups. CONTAINS match ('in') is supported on labels. Identity-mapped groups are uniquely identified by both a `member_key_id` and a `member_key_namespace`, which requires an additional query input: `member_key_namespace`. Example query: `member_key_id == 'member_key_id_value' && 'label_value' in labels`
};
apiInstance.cloudidentityGroupsMembershipsSearchDirectGroups(parent, opts, (error, data, response) => {
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
 **parent** | **String**| [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: groups/{group_id}, where group_id is always &#39;-&#39; as this API will search across all groups for a given member. | 
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
 **orderBy** | **String**| The ordering of membership relation for the display name or email in the response. The syntax for this field can be found at https://cloud.google.com/apis/design/design_patterns#sorting_order. Example: Sort by the ascending display name: order_by&#x3D;\&quot;group_name\&quot; or order_by&#x3D;\&quot;group_name asc\&quot;. Sort by the descending display name: order_by&#x3D;\&quot;group_name desc\&quot;. Sort by the ascending group key: order_by&#x3D;\&quot;group_key\&quot; or order_by&#x3D;\&quot;group_key asc\&quot;. Sort by the descending group key: order_by&#x3D;\&quot;group_key desc\&quot;. | [optional] 
 **pageSize** | **Number**| The default page size is 200 (max 1000). | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request, if any | [optional] 
 **query** | **String**| Required. A CEL expression that MUST include member specification AND label(s). Users can search on label attributes of groups. CONTAINS match (&#39;in&#39;) is supported on labels. Identity-mapped groups are uniquely identified by both a &#x60;member_key_id&#x60; and a &#x60;member_key_namespace&#x60;, which requires an additional query input: &#x60;member_key_namespace&#x60;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; &#39;label_value&#39; in labels&#x60; | [optional] 

### Return type

[**SearchDirectGroupsResponse**](SearchDirectGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityGroupsMembershipsSearchTransitiveGroups

> SearchTransitiveGroupsResponse cloudidentityGroupsMembershipsSearchTransitiveGroups(parent, opts)



Search transitive groups of a member. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. A transitive group is any group that has a direct or indirect membership to the member. Actor must have view permissions all transitive groups.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
let parent = "parent_example"; // String | [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: `groups/{group_id}`, where `group_id` is always '-' as this API will search across all groups for a given member.
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
  'pageSize': 56, // Number | The default page size is 200 (max 1000).
  'pageToken': "pageToken_example", // String | The next_page_token value returned from a previous list request, if any.
  'query': "query_example" // String | Required. A CEL expression that MUST include member specification AND label(s). This is a `required` field. Users can search on label attributes of groups. CONTAINS match ('in') is supported on labels. Identity-mapped groups are uniquely identified by both a `member_key_id` and a `member_key_namespace`, which requires an additional query input: `member_key_namespace`. Example query: `member_key_id == 'member_key_id_value' && in labels` Query may optionally contain equality operators on the parent of the group restricting the search within a particular customer, e.g. `parent == 'customers/{customer_id}'`. The `customer_id` must begin with \"C\" (for example, 'C046psxkn'). This filtering is only supported for Admins with groups read permissons on the input customer. Example query: `member_key_id == 'member_key_id_value' && in labels && parent == 'customers/C046psxkn'`
};
apiInstance.cloudidentityGroupsMembershipsSearchTransitiveGroups(parent, opts, (error, data, response) => {
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
 **parent** | **String**| [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: &#x60;groups/{group_id}&#x60;, where &#x60;group_id&#x60; is always &#39;-&#39; as this API will search across all groups for a given member. | 
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
 **pageSize** | **Number**| The default page size is 200 (max 1000). | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request, if any. | [optional] 
 **query** | **String**| Required. A CEL expression that MUST include member specification AND label(s). This is a &#x60;required&#x60; field. Users can search on label attributes of groups. CONTAINS match (&#39;in&#39;) is supported on labels. Identity-mapped groups are uniquely identified by both a &#x60;member_key_id&#x60; and a &#x60;member_key_namespace&#x60;, which requires an additional query input: &#x60;member_key_namespace&#x60;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; in labels&#x60; Query may optionally contain equality operators on the parent of the group restricting the search within a particular customer, e.g. &#x60;parent &#x3D;&#x3D; &#39;customers/{customer_id}&#39;&#x60;. The &#x60;customer_id&#x60; must begin with \&quot;C\&quot; (for example, &#39;C046psxkn&#39;). This filtering is only supported for Admins with groups read permissons on the input customer. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; in labels &amp;&amp; parent &#x3D;&#x3D; &#39;customers/C046psxkn&#39;&#x60; | [optional] 

### Return type

[**SearchTransitiveGroupsResponse**](SearchTransitiveGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityGroupsMembershipsSearchTransitiveMemberships

> SearchTransitiveMembershipsResponse cloudidentityGroupsMembershipsSearchTransitiveMemberships(parent, opts)



Search transitive memberships of a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. A transitive membership is any direct or indirect membership of a group. Actor must have view permissions to all transitive memberships.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
let parent = "parent_example"; // String | [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: `groups/{group_id}`, where `group_id` is the unique ID assigned to the Group.
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
  'pageSize': 56, // Number | The default page size is 200 (max 1000).
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request, if any.
};
apiInstance.cloudidentityGroupsMembershipsSearchTransitiveMemberships(parent, opts, (error, data, response) => {
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
 **parent** | **String**| [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: &#x60;groups/{group_id}&#x60;, where &#x60;group_id&#x60; is the unique ID assigned to the Group. | 
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
 **pageSize** | **Number**| The default page size is 200 (max 1000). | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request, if any. | [optional] 

### Return type

[**SearchTransitiveMembershipsResponse**](SearchTransitiveMembershipsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudidentityGroupsSearch

> SearchGroupsResponse cloudidentityGroupsSearch(opts)



Searches for &#x60;Group&#x60; resources matching a specified query.

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

let apiInstance = new CloudIdentityApi.GroupsApi();
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
  'orderBy': "orderBy_example", // String | The ordering of groups for the display name or email in the search groups response. The syntax for this field can be found at https://cloud.google.com/apis/design/design_patterns#sorting_order. Example: Sort by the ascending name: order_by=\"display_name\" Sort by the descending group key email: order_by=\"group_key desc\"
  'pageSize': 56, // Number | The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a `next_page_token`. If unspecified, defaults to 200 for `GroupView.BASIC` and to 50 for `GroupView.FULL`. Must not be greater than 1000 for `GroupView.BASIC` or 500 for `GroupView.FULL`.
  'pageToken': "pageToken_example", // String | The `next_page_token` value returned from a previous search request, if any.
  'query': "query_example", // String | Required. The search query. * Must be specified in [Common Expression Language](https://opensource.google/projects/cel). * Must contain equality operators on the parent, e.g. `parent == 'customers/{customer_id}'`. The `customer_id` must begin with \"C\" (for example, 'C046psxkn'). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793) * Can contain optional inclusion operators on `labels` such as `'cloudidentity.googleapis.com/groups.discussion_forum' in labels`). * Can contain an optional equality operator on `domain_name`. e.g. `domain_name == 'examplepetstore.com'` * Can contain optional `startsWith/contains/equality` operators on `group_key`, e.g. `group_key.startsWith('dev')`, `group_key.contains('dev'), group_key == 'dev@examplepetstore.com'` * Can contain optional `startsWith/contains/equality` operators on `display_name`, such as `display_name.startsWith('dev')` , `display_name.contains('dev')`, `display_name == 'dev'`
  'view': "view_example" // String | The level of detail to be returned. If unspecified, defaults to `View.BASIC`.
};
apiInstance.cloudidentityGroupsSearch(opts, (error, data, response) => {
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
 **orderBy** | **String**| The ordering of groups for the display name or email in the search groups response. The syntax for this field can be found at https://cloud.google.com/apis/design/design_patterns#sorting_order. Example: Sort by the ascending name: order_by&#x3D;\&quot;display_name\&quot; Sort by the descending group key email: order_by&#x3D;\&quot;group_key desc\&quot; | [optional] 
 **pageSize** | **Number**| The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a &#x60;next_page_token&#x60;. If unspecified, defaults to 200 for &#x60;GroupView.BASIC&#x60; and to 50 for &#x60;GroupView.FULL&#x60;. Must not be greater than 1000 for &#x60;GroupView.BASIC&#x60; or 500 for &#x60;GroupView.FULL&#x60;. | [optional] 
 **pageToken** | **String**| The &#x60;next_page_token&#x60; value returned from a previous search request, if any. | [optional] 
 **query** | **String**| Required. The search query. * Must be specified in [Common Expression Language](https://opensource.google/projects/cel). * Must contain equality operators on the parent, e.g. &#x60;parent &#x3D;&#x3D; &#39;customers/{customer_id}&#39;&#x60;. The &#x60;customer_id&#x60; must begin with \&quot;C\&quot; (for example, &#39;C046psxkn&#39;). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793) * Can contain optional inclusion operators on &#x60;labels&#x60; such as &#x60;&#39;cloudidentity.googleapis.com/groups.discussion_forum&#39; in labels&#x60;). * Can contain an optional equality operator on &#x60;domain_name&#x60;. e.g. &#x60;domain_name &#x3D;&#x3D; &#39;examplepetstore.com&#39;&#x60; * Can contain optional &#x60;startsWith/contains/equality&#x60; operators on &#x60;group_key&#x60;, e.g. &#x60;group_key.startsWith(&#39;dev&#39;)&#x60;, &#x60;group_key.contains(&#39;dev&#39;), group_key &#x3D;&#x3D; &#39;dev@examplepetstore.com&#39;&#x60; * Can contain optional &#x60;startsWith/contains/equality&#x60; operators on &#x60;display_name&#x60;, such as &#x60;display_name.startsWith(&#39;dev&#39;)&#x60; , &#x60;display_name.contains(&#39;dev&#39;)&#x60;, &#x60;display_name &#x3D;&#x3D; &#39;dev&#39;&#x60; | [optional] 
 **view** | **String**| The level of detail to be returned. If unspecified, defaults to &#x60;View.BASIC&#x60;. | [optional] 

### Return type

[**SearchGroupsResponse**](SearchGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


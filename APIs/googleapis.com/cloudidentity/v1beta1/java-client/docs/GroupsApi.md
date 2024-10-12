# GroupsApi

All URIs are relative to *https://cloudidentity.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudidentityGroupsCreate**](GroupsApi.md#cloudidentityGroupsCreate) | **POST** /v1beta1/groups |  |
| [**cloudidentityGroupsList**](GroupsApi.md#cloudidentityGroupsList) | **GET** /v1beta1/groups |  |
| [**cloudidentityGroupsLookup**](GroupsApi.md#cloudidentityGroupsLookup) | **GET** /v1beta1/groups:lookup |  |
| [**cloudidentityGroupsMembershipsCheckTransitiveMembership**](GroupsApi.md#cloudidentityGroupsMembershipsCheckTransitiveMembership) | **GET** /v1beta1/{parent}/memberships:checkTransitiveMembership |  |
| [**cloudidentityGroupsMembershipsCreate**](GroupsApi.md#cloudidentityGroupsMembershipsCreate) | **POST** /v1beta1/{parent}/memberships |  |
| [**cloudidentityGroupsMembershipsGetMembershipGraph**](GroupsApi.md#cloudidentityGroupsMembershipsGetMembershipGraph) | **GET** /v1beta1/{parent}/memberships:getMembershipGraph |  |
| [**cloudidentityGroupsMembershipsLookup**](GroupsApi.md#cloudidentityGroupsMembershipsLookup) | **GET** /v1beta1/{parent}/memberships:lookup |  |
| [**cloudidentityGroupsMembershipsModifyMembershipRoles**](GroupsApi.md#cloudidentityGroupsMembershipsModifyMembershipRoles) | **POST** /v1beta1/{name}:modifyMembershipRoles |  |
| [**cloudidentityGroupsMembershipsSearchDirectGroups**](GroupsApi.md#cloudidentityGroupsMembershipsSearchDirectGroups) | **GET** /v1beta1/{parent}/memberships:searchDirectGroups |  |
| [**cloudidentityGroupsMembershipsSearchTransitiveGroups**](GroupsApi.md#cloudidentityGroupsMembershipsSearchTransitiveGroups) | **GET** /v1beta1/{parent}/memberships:searchTransitiveGroups |  |
| [**cloudidentityGroupsMembershipsSearchTransitiveMemberships**](GroupsApi.md#cloudidentityGroupsMembershipsSearchTransitiveMemberships) | **GET** /v1beta1/{parent}/memberships:searchTransitiveMemberships |  |
| [**cloudidentityGroupsSearch**](GroupsApi.md#cloudidentityGroupsSearch) | **GET** /v1beta1/groups:search |  |


<a id="cloudidentityGroupsCreate"></a>
# **cloudidentityGroupsCreate**
> Operation cloudidentityGroupsCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, initialGroupConfig, group)



Creates a &#x60;Group&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String initialGroupConfig = "INITIAL_GROUP_CONFIG_UNSPECIFIED"; // String | Required. The initial configuration option for the `Group`.
    Group group = new Group(); // Group | 
    try {
      Operation result = apiInstance.cloudidentityGroupsCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, initialGroupConfig, group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **initialGroupConfig** | **String**| Required. The initial configuration option for the &#x60;Group&#x60;. | [optional] [enum: INITIAL_GROUP_CONFIG_UNSPECIFIED, WITH_INITIAL_OWNER, EMPTY] |
| **group** | [**Group**](Group.md)|  | [optional] |

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsList"></a>
# **cloudidentityGroupsList**
> ListGroupsResponse cloudidentityGroupsList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, parent, view)



Lists the &#x60;Group&#x60; resources under a customer or namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a `next_page_token`. If unspecified, defaults to 200 for `View.BASIC` and to 50 for `View.FULL`. Must not be greater than 1000 for `View.BASIC` or 500 for `View.FULL`.
    String pageToken = "pageToken_example"; // String | The `next_page_token` value returned from a previous list request, if any.
    String parent = "parent_example"; // String | Required. The parent resource under which to list all `Group` resources. Must be of the form `identitysources/{identity_source_id}` for external- identity-mapped groups or `customers/{customer_id}` for Google Groups. The `customer_id` must begin with \"C\" (for example, 'C046psxkn'). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793)
    String view = "VIEW_UNSPECIFIED"; // String | The level of detail to be returned. If unspecified, defaults to `View.BASIC`.
    try {
      ListGroupsResponse result = apiInstance.cloudidentityGroupsList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, parent, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a &#x60;next_page_token&#x60;. If unspecified, defaults to 200 for &#x60;View.BASIC&#x60; and to 50 for &#x60;View.FULL&#x60;. Must not be greater than 1000 for &#x60;View.BASIC&#x60; or 500 for &#x60;View.FULL&#x60;. | [optional] |
| **pageToken** | **String**| The &#x60;next_page_token&#x60; value returned from a previous list request, if any. | [optional] |
| **parent** | **String**| Required. The parent resource under which to list all &#x60;Group&#x60; resources. Must be of the form &#x60;identitysources/{identity_source_id}&#x60; for external- identity-mapped groups or &#x60;customers/{customer_id}&#x60; for Google Groups. The &#x60;customer_id&#x60; must begin with \&quot;C\&quot; (for example, &#39;C046psxkn&#39;). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793) | [optional] |
| **view** | **String**| The level of detail to be returned. If unspecified, defaults to &#x60;View.BASIC&#x60;. | [optional] [enum: VIEW_UNSPECIFIED, BASIC, FULL] |

### Return type

[**ListGroupsResponse**](ListGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsLookup"></a>
# **cloudidentityGroupsLookup**
> LookupGroupNameResponse cloudidentityGroupsLookup($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, groupKeyId, groupKeyNamespace)



Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a &#x60;Group&#x60; by its &#x60;EntityKey&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String groupKeyId = "groupKeyId_example"; // String | The ID of the entity. For Google-managed entities, the `id` must be the email address of an existing group or user. For external-identity-mapped entities, the `id` must be a string conforming to the Identity Source's requirements. Must be unique within a `namespace`.
    String groupKeyNamespace = "groupKeyNamespace_example"; // String | The namespace in which the entity exists. If not specified, the `EntityKey` represents a Google-managed entity such as a Google user or a Google Group. If specified, the `EntityKey` represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of `identitysources/{identity_source_id}`.
    try {
      LookupGroupNameResponse result = apiInstance.cloudidentityGroupsLookup($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, groupKeyId, groupKeyNamespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsLookup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **groupKeyId** | **String**| The ID of the entity. For Google-managed entities, the &#x60;id&#x60; must be the email address of an existing group or user. For external-identity-mapped entities, the &#x60;id&#x60; must be a string conforming to the Identity Source&#39;s requirements. Must be unique within a &#x60;namespace&#x60;. | [optional] |
| **groupKeyNamespace** | **String**| The namespace in which the entity exists. If not specified, the &#x60;EntityKey&#x60; represents a Google-managed entity such as a Google user or a Google Group. If specified, the &#x60;EntityKey&#x60; represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of &#x60;identitysources/{identity_source_id}&#x60;. | [optional] |

### Return type

[**LookupGroupNameResponse**](LookupGroupNameResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsMembershipsCheckTransitiveMembership"></a>
# **cloudidentityGroupsMembershipsCheckTransitiveMembership**
> CheckTransitiveMembershipResponse cloudidentityGroupsMembershipsCheckTransitiveMembership(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, query)



Check a potential member for membership in a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. A member has membership to a group as long as there is a single viewable transitive membership between the group and the member. The actor must have view permissions to at least one transitive membership between the member and group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String parent = "parent_example"; // String | [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to check the transitive membership in. Format: `groups/{group_id}`, where `group_id` is the unique id assigned to the Group to which the Membership belongs to.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String query = "query_example"; // String | Required. A CEL expression that MUST include member specification. This is a `required` field. Certain groups are uniquely identified by both a 'member_key_id' and a 'member_key_namespace', which requires an additional query input: 'member_key_namespace'. Example query: `member_key_id == 'member_key_id_value'`
    try {
      CheckTransitiveMembershipResponse result = apiInstance.cloudidentityGroupsMembershipsCheckTransitiveMembership(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsMembershipsCheckTransitiveMembership");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to check the transitive membership in. Format: &#x60;groups/{group_id}&#x60;, where &#x60;group_id&#x60; is the unique id assigned to the Group to which the Membership belongs to. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **query** | **String**| Required. A CEL expression that MUST include member specification. This is a &#x60;required&#x60; field. Certain groups are uniquely identified by both a &#39;member_key_id&#39; and a &#39;member_key_namespace&#39;, which requires an additional query input: &#39;member_key_namespace&#39;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39;&#x60; | [optional] |

### Return type

[**CheckTransitiveMembershipResponse**](CheckTransitiveMembershipResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsMembershipsCreate"></a>
# **cloudidentityGroupsMembershipsCreate**
> Operation cloudidentityGroupsMembershipsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, membership)



Creates a &#x60;Membership&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent `Group` resource under which to create the `Membership`. Must be of the form `groups/{group_id}`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Membership membership = new Membership(); // Membership | 
    try {
      Operation result = apiInstance.cloudidentityGroupsMembershipsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, membership);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsMembershipsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The parent &#x60;Group&#x60; resource under which to create the &#x60;Membership&#x60;. Must be of the form &#x60;groups/{group_id}&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **membership** | [**Membership**](Membership.md)|  | [optional] |

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsMembershipsGetMembershipGraph"></a>
# **cloudidentityGroupsMembershipsGetMembershipGraph**
> Operation cloudidentityGroupsMembershipsGetMembershipGraph(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, query)



Get a membership graph of just a member or both a member and a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. Given a member, the response will contain all membership paths from the member. Given both a group and a member, the response will contain all membership paths between the group and the member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String parent = "parent_example"; // String | Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: `groups/{group_id}`, where `group_id` is the unique ID assigned to the Group to which the Membership belongs to. group_id can be a wildcard collection id \"-\". When a group_id is specified, the membership graph will be constrained to paths between the member (defined in the query) and the parent. If a wildcard collection is provided, all membership paths connected to the member will be returned.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String query = "query_example"; // String | Required. A CEL expression that MUST include member specification AND label(s). Certain groups are uniquely identified by both a 'member_key_id' and a 'member_key_namespace', which requires an additional query input: 'member_key_namespace'. Example query: `member_key_id == 'member_key_id_value' && in labels`
    try {
      Operation result = apiInstance.cloudidentityGroupsMembershipsGetMembershipGraph(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsMembershipsGetMembershipGraph");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: &#x60;groups/{group_id}&#x60;, where &#x60;group_id&#x60; is the unique ID assigned to the Group to which the Membership belongs to. group_id can be a wildcard collection id \&quot;-\&quot;. When a group_id is specified, the membership graph will be constrained to paths between the member (defined in the query) and the parent. If a wildcard collection is provided, all membership paths connected to the member will be returned. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **query** | **String**| Required. A CEL expression that MUST include member specification AND label(s). Certain groups are uniquely identified by both a &#39;member_key_id&#39; and a &#39;member_key_namespace&#39;, which requires an additional query input: &#39;member_key_namespace&#39;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; in labels&#x60; | [optional] |

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsMembershipsLookup"></a>
# **cloudidentityGroupsMembershipsLookup**
> LookupMembershipNameResponse cloudidentityGroupsMembershipsLookup(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, memberKeyId, memberKeyNamespace)



Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a &#x60;Membership&#x60; by its &#x60;EntityKey&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent `Group` resource under which to lookup the `Membership` name. Must be of the form `groups/{group_id}`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String memberKeyId = "memberKeyId_example"; // String | The ID of the entity. For Google-managed entities, the `id` must be the email address of an existing group or user. For external-identity-mapped entities, the `id` must be a string conforming to the Identity Source's requirements. Must be unique within a `namespace`.
    String memberKeyNamespace = "memberKeyNamespace_example"; // String | The namespace in which the entity exists. If not specified, the `EntityKey` represents a Google-managed entity such as a Google user or a Google Group. If specified, the `EntityKey` represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of `identitysources/{identity_source_id}`.
    try {
      LookupMembershipNameResponse result = apiInstance.cloudidentityGroupsMembershipsLookup(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, memberKeyId, memberKeyNamespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsMembershipsLookup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The parent &#x60;Group&#x60; resource under which to lookup the &#x60;Membership&#x60; name. Must be of the form &#x60;groups/{group_id}&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **memberKeyId** | **String**| The ID of the entity. For Google-managed entities, the &#x60;id&#x60; must be the email address of an existing group or user. For external-identity-mapped entities, the &#x60;id&#x60; must be a string conforming to the Identity Source&#39;s requirements. Must be unique within a &#x60;namespace&#x60;. | [optional] |
| **memberKeyNamespace** | **String**| The namespace in which the entity exists. If not specified, the &#x60;EntityKey&#x60; represents a Google-managed entity such as a Google user or a Google Group. If specified, the &#x60;EntityKey&#x60; represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of &#x60;identitysources/{identity_source_id}&#x60;. | [optional] |

### Return type

[**LookupMembershipNameResponse**](LookupMembershipNameResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsMembershipsModifyMembershipRoles"></a>
# **cloudidentityGroupsMembershipsModifyMembershipRoles**
> ModifyMembershipRolesResponse cloudidentityGroupsMembershipsModifyMembershipRoles(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, modifyMembershipRolesRequest)



Modifies the &#x60;MembershipRole&#x60;s of a &#x60;Membership&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String name = "name_example"; // String | Required. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Membership` whose roles are to be modified. Must be of the form `groups/{group_id}/memberships/{membership_id}`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    ModifyMembershipRolesRequest modifyMembershipRolesRequest = new ModifyMembershipRolesRequest(); // ModifyMembershipRolesRequest | 
    try {
      ModifyMembershipRolesResponse result = apiInstance.cloudidentityGroupsMembershipsModifyMembershipRoles(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, modifyMembershipRolesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsMembershipsModifyMembershipRoles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. The [resource name](https://cloud.google.com/apis/design/resource_names) of the &#x60;Membership&#x60; whose roles are to be modified. Must be of the form &#x60;groups/{group_id}/memberships/{membership_id}&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **modifyMembershipRolesRequest** | [**ModifyMembershipRolesRequest**](ModifyMembershipRolesRequest.md)|  | [optional] |

### Return type

[**ModifyMembershipRolesResponse**](ModifyMembershipRolesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsMembershipsSearchDirectGroups"></a>
# **cloudidentityGroupsMembershipsSearchDirectGroups**
> SearchDirectGroupsResponse cloudidentityGroupsMembershipsSearchDirectGroups(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, orderBy, pageSize, pageToken, query)



Searches direct groups of a member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String parent = "parent_example"; // String | [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: groups/{group_id}, where group_id is always '-' as this API will search across all groups for a given member.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String orderBy = "orderBy_example"; // String | The ordering of membership relation for the display name or email in the response. The syntax for this field can be found at https://cloud.google.com/apis/design/design_patterns#sorting_order. Example: Sort by the ascending display name: order_by=\"group_name\" or order_by=\"group_name asc\". Sort by the descending display name: order_by=\"group_name desc\". Sort by the ascending group key: order_by=\"group_key\" or order_by=\"group_key asc\". Sort by the descending group key: order_by=\"group_key desc\".
    Integer pageSize = 56; // Integer | The default page size is 200 (max 1000).
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request, if any
    String query = "query_example"; // String | Required. A CEL expression that MUST include member specification AND label(s). Users can search on label attributes of groups. CONTAINS match ('in') is supported on labels. Identity-mapped groups are uniquely identified by both a `member_key_id` and a `member_key_namespace`, which requires an additional query input: `member_key_namespace`. Example query: `member_key_id == 'member_key_id_value' && 'label_value' in labels`
    try {
      SearchDirectGroupsResponse result = apiInstance.cloudidentityGroupsMembershipsSearchDirectGroups(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, orderBy, pageSize, pageToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsMembershipsSearchDirectGroups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: groups/{group_id}, where group_id is always &#39;-&#39; as this API will search across all groups for a given member. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **orderBy** | **String**| The ordering of membership relation for the display name or email in the response. The syntax for this field can be found at https://cloud.google.com/apis/design/design_patterns#sorting_order. Example: Sort by the ascending display name: order_by&#x3D;\&quot;group_name\&quot; or order_by&#x3D;\&quot;group_name asc\&quot;. Sort by the descending display name: order_by&#x3D;\&quot;group_name desc\&quot;. Sort by the ascending group key: order_by&#x3D;\&quot;group_key\&quot; or order_by&#x3D;\&quot;group_key asc\&quot;. Sort by the descending group key: order_by&#x3D;\&quot;group_key desc\&quot;. | [optional] |
| **pageSize** | **Integer**| The default page size is 200 (max 1000). | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request, if any | [optional] |
| **query** | **String**| Required. A CEL expression that MUST include member specification AND label(s). Users can search on label attributes of groups. CONTAINS match (&#39;in&#39;) is supported on labels. Identity-mapped groups are uniquely identified by both a &#x60;member_key_id&#x60; and a &#x60;member_key_namespace&#x60;, which requires an additional query input: &#x60;member_key_namespace&#x60;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; &#39;label_value&#39; in labels&#x60; | [optional] |

### Return type

[**SearchDirectGroupsResponse**](SearchDirectGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsMembershipsSearchTransitiveGroups"></a>
# **cloudidentityGroupsMembershipsSearchTransitiveGroups**
> SearchTransitiveGroupsResponse cloudidentityGroupsMembershipsSearchTransitiveGroups(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, query)



Search transitive groups of a member. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. A transitive group is any group that has a direct or indirect membership to the member. Actor must have view permissions all transitive groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String parent = "parent_example"; // String | [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: `groups/{group_id}`, where `group_id` is always '-' as this API will search across all groups for a given member.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The default page size is 200 (max 1000).
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request, if any.
    String query = "query_example"; // String | Required. A CEL expression that MUST include member specification AND label(s). This is a `required` field. Users can search on label attributes of groups. CONTAINS match ('in') is supported on labels. Identity-mapped groups are uniquely identified by both a `member_key_id` and a `member_key_namespace`, which requires an additional query input: `member_key_namespace`. Example query: `member_key_id == 'member_key_id_value' && in labels` Query may optionally contain equality operators on the parent of the group restricting the search within a particular customer, e.g. `parent == 'customers/{customer_id}'`. The `customer_id` must begin with \"C\" (for example, 'C046psxkn'). This filtering is only supported for Admins with groups read permissons on the input customer. Example query: `member_key_id == 'member_key_id_value' && in labels && parent == 'customers/C046psxkn'`
    try {
      SearchTransitiveGroupsResponse result = apiInstance.cloudidentityGroupsMembershipsSearchTransitiveGroups(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsMembershipsSearchTransitiveGroups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: &#x60;groups/{group_id}&#x60;, where &#x60;group_id&#x60; is always &#39;-&#39; as this API will search across all groups for a given member. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The default page size is 200 (max 1000). | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request, if any. | [optional] |
| **query** | **String**| Required. A CEL expression that MUST include member specification AND label(s). This is a &#x60;required&#x60; field. Users can search on label attributes of groups. CONTAINS match (&#39;in&#39;) is supported on labels. Identity-mapped groups are uniquely identified by both a &#x60;member_key_id&#x60; and a &#x60;member_key_namespace&#x60;, which requires an additional query input: &#x60;member_key_namespace&#x60;. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; in labels&#x60; Query may optionally contain equality operators on the parent of the group restricting the search within a particular customer, e.g. &#x60;parent &#x3D;&#x3D; &#39;customers/{customer_id}&#39;&#x60;. The &#x60;customer_id&#x60; must begin with \&quot;C\&quot; (for example, &#39;C046psxkn&#39;). This filtering is only supported for Admins with groups read permissons on the input customer. Example query: &#x60;member_key_id &#x3D;&#x3D; &#39;member_key_id_value&#39; &amp;&amp; in labels &amp;&amp; parent &#x3D;&#x3D; &#39;customers/C046psxkn&#39;&#x60; | [optional] |

### Return type

[**SearchTransitiveGroupsResponse**](SearchTransitiveGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsMembershipsSearchTransitiveMemberships"></a>
# **cloudidentityGroupsMembershipsSearchTransitiveMemberships**
> SearchTransitiveMembershipsResponse cloudidentityGroupsMembershipsSearchTransitiveMemberships(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Search transitive memberships of a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. A transitive membership is any direct or indirect membership of a group. Actor must have view permissions to all transitive memberships.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String parent = "parent_example"; // String | [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: `groups/{group_id}`, where `group_id` is the unique ID assigned to the Group.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The default page size is 200 (max 1000).
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request, if any.
    try {
      SearchTransitiveMembershipsResponse result = apiInstance.cloudidentityGroupsMembershipsSearchTransitiveMemberships(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsMembershipsSearchTransitiveMemberships");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| [Resource name](https://cloud.google.com/apis/design/resource_names) of the group to search transitive memberships in. Format: &#x60;groups/{group_id}&#x60;, where &#x60;group_id&#x60; is the unique ID assigned to the Group. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The default page size is 200 (max 1000). | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request, if any. | [optional] |

### Return type

[**SearchTransitiveMembershipsResponse**](SearchTransitiveMembershipsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityGroupsSearch"></a>
# **cloudidentityGroupsSearch**
> SearchGroupsResponse cloudidentityGroupsSearch($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, orderBy, pageSize, pageToken, query, view)



Searches for &#x60;Group&#x60; resources matching a specified query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String orderBy = "orderBy_example"; // String | The ordering of groups for the display name or email in the search groups response. The syntax for this field can be found at https://cloud.google.com/apis/design/design_patterns#sorting_order. Example: Sort by the ascending name: order_by=\"display_name\" Sort by the descending group key email: order_by=\"group_key desc\"
    Integer pageSize = 56; // Integer | The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a `next_page_token`. If unspecified, defaults to 200 for `GroupView.BASIC` and to 50 for `GroupView.FULL`. Must not be greater than 1000 for `GroupView.BASIC` or 500 for `GroupView.FULL`.
    String pageToken = "pageToken_example"; // String | The `next_page_token` value returned from a previous search request, if any.
    String query = "query_example"; // String | Required. The search query. * Must be specified in [Common Expression Language](https://opensource.google/projects/cel). * Must contain equality operators on the parent, e.g. `parent == 'customers/{customer_id}'`. The `customer_id` must begin with \"C\" (for example, 'C046psxkn'). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793) * Can contain optional inclusion operators on `labels` such as `'cloudidentity.googleapis.com/groups.discussion_forum' in labels`). * Can contain an optional equality operator on `domain_name`. e.g. `domain_name == 'examplepetstore.com'` * Can contain optional `startsWith/contains/equality` operators on `group_key`, e.g. `group_key.startsWith('dev')`, `group_key.contains('dev'), group_key == 'dev@examplepetstore.com'` * Can contain optional `startsWith/contains/equality` operators on `display_name`, such as `display_name.startsWith('dev')` , `display_name.contains('dev')`, `display_name == 'dev'`
    String view = "BASIC"; // String | The level of detail to be returned. If unspecified, defaults to `View.BASIC`.
    try {
      SearchGroupsResponse result = apiInstance.cloudidentityGroupsSearch($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, orderBy, pageSize, pageToken, query, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#cloudidentityGroupsSearch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **orderBy** | **String**| The ordering of groups for the display name or email in the search groups response. The syntax for this field can be found at https://cloud.google.com/apis/design/design_patterns#sorting_order. Example: Sort by the ascending name: order_by&#x3D;\&quot;display_name\&quot; Sort by the descending group key email: order_by&#x3D;\&quot;group_key desc\&quot; | [optional] |
| **pageSize** | **Integer**| The maximum number of results to return. Note that the number of results returned may be less than this value even if there are more available results. To fetch all results, clients must continue calling this method repeatedly until the response no longer contains a &#x60;next_page_token&#x60;. If unspecified, defaults to 200 for &#x60;GroupView.BASIC&#x60; and to 50 for &#x60;GroupView.FULL&#x60;. Must not be greater than 1000 for &#x60;GroupView.BASIC&#x60; or 500 for &#x60;GroupView.FULL&#x60;. | [optional] |
| **pageToken** | **String**| The &#x60;next_page_token&#x60; value returned from a previous search request, if any. | [optional] |
| **query** | **String**| Required. The search query. * Must be specified in [Common Expression Language](https://opensource.google/projects/cel). * Must contain equality operators on the parent, e.g. &#x60;parent &#x3D;&#x3D; &#39;customers/{customer_id}&#39;&#x60;. The &#x60;customer_id&#x60; must begin with \&quot;C\&quot; (for example, &#39;C046psxkn&#39;). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793) * Can contain optional inclusion operators on &#x60;labels&#x60; such as &#x60;&#39;cloudidentity.googleapis.com/groups.discussion_forum&#39; in labels&#x60;). * Can contain an optional equality operator on &#x60;domain_name&#x60;. e.g. &#x60;domain_name &#x3D;&#x3D; &#39;examplepetstore.com&#39;&#x60; * Can contain optional &#x60;startsWith/contains/equality&#x60; operators on &#x60;group_key&#x60;, e.g. &#x60;group_key.startsWith(&#39;dev&#39;)&#x60;, &#x60;group_key.contains(&#39;dev&#39;), group_key &#x3D;&#x3D; &#39;dev@examplepetstore.com&#39;&#x60; * Can contain optional &#x60;startsWith/contains/equality&#x60; operators on &#x60;display_name&#x60;, such as &#x60;display_name.startsWith(&#39;dev&#39;)&#x60; , &#x60;display_name.contains(&#39;dev&#39;)&#x60;, &#x60;display_name &#x3D;&#x3D; &#39;dev&#39;&#x60; | [optional] |
| **view** | **String**| The level of detail to be returned. If unspecified, defaults to &#x60;View.BASIC&#x60;. | [optional] [enum: BASIC, FULL] |

### Return type

[**SearchGroupsResponse**](SearchGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |


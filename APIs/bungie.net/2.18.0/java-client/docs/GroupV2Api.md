# GroupV2Api

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**groupV2AbdicateFoundership**](GroupV2Api.md#groupV2AbdicateFoundership) | **POST** /GroupV2/{groupId}/Admin/AbdicateFoundership/{membershipType}/{founderIdNew}/ |  |
| [**groupV2AddOptionalConversation**](GroupV2Api.md#groupV2AddOptionalConversation) | **POST** /GroupV2/{groupId}/OptionalConversations/Add/ |  |
| [**groupV2ApproveAllPending**](GroupV2Api.md#groupV2ApproveAllPending) | **POST** /GroupV2/{groupId}/Members/ApproveAll/ |  |
| [**groupV2ApprovePending**](GroupV2Api.md#groupV2ApprovePending) | **POST** /GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/ |  |
| [**groupV2ApprovePendingForList**](GroupV2Api.md#groupV2ApprovePendingForList) | **POST** /GroupV2/{groupId}/Members/ApproveList/ |  |
| [**groupV2BanMember**](GroupV2Api.md#groupV2BanMember) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Ban/ |  |
| [**groupV2DenyAllPending**](GroupV2Api.md#groupV2DenyAllPending) | **POST** /GroupV2/{groupId}/Members/DenyAll/ |  |
| [**groupV2DenyPendingForList**](GroupV2Api.md#groupV2DenyPendingForList) | **POST** /GroupV2/{groupId}/Members/DenyList/ |  |
| [**groupV2EditClanBanner**](GroupV2Api.md#groupV2EditClanBanner) | **POST** /GroupV2/{groupId}/EditClanBanner/ |  |
| [**groupV2EditFounderOptions**](GroupV2Api.md#groupV2EditFounderOptions) | **POST** /GroupV2/{groupId}/EditFounderOptions/ |  |
| [**groupV2EditGroup**](GroupV2Api.md#groupV2EditGroup) | **POST** /GroupV2/{groupId}/Edit/ |  |
| [**groupV2EditGroupMembership**](GroupV2Api.md#groupV2EditGroupMembership) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/SetMembershipType/{memberType}/ |  |
| [**groupV2EditOptionalConversation**](GroupV2Api.md#groupV2EditOptionalConversation) | **POST** /GroupV2/{groupId}/OptionalConversations/Edit/{conversationId}/ |  |
| [**groupV2GetAdminsAndFounderOfGroup**](GroupV2Api.md#groupV2GetAdminsAndFounderOfGroup) | **GET** /GroupV2/{groupId}/AdminsAndFounder/ |  |
| [**groupV2GetAvailableAvatars**](GroupV2Api.md#groupV2GetAvailableAvatars) | **GET** /GroupV2/GetAvailableAvatars/ |  |
| [**groupV2GetAvailableThemes**](GroupV2Api.md#groupV2GetAvailableThemes) | **GET** /GroupV2/GetAvailableThemes/ |  |
| [**groupV2GetBannedMembersOfGroup**](GroupV2Api.md#groupV2GetBannedMembersOfGroup) | **GET** /GroupV2/{groupId}/Banned/ |  |
| [**groupV2GetGroup**](GroupV2Api.md#groupV2GetGroup) | **GET** /GroupV2/{groupId}/ |  |
| [**groupV2GetGroupByName**](GroupV2Api.md#groupV2GetGroupByName) | **GET** /GroupV2/Name/{groupName}/{groupType}/ |  |
| [**groupV2GetGroupByNameV2**](GroupV2Api.md#groupV2GetGroupByNameV2) | **POST** /GroupV2/NameV2/ |  |
| [**groupV2GetGroupOptionalConversations**](GroupV2Api.md#groupV2GetGroupOptionalConversations) | **GET** /GroupV2/{groupId}/OptionalConversations/ |  |
| [**groupV2GetGroupsForMember**](GroupV2Api.md#groupV2GetGroupsForMember) | **GET** /GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/ |  |
| [**groupV2GetInvitedIndividuals**](GroupV2Api.md#groupV2GetInvitedIndividuals) | **GET** /GroupV2/{groupId}/Members/InvitedIndividuals/ |  |
| [**groupV2GetMembersOfGroup**](GroupV2Api.md#groupV2GetMembersOfGroup) | **GET** /GroupV2/{groupId}/Members/ |  |
| [**groupV2GetPendingMemberships**](GroupV2Api.md#groupV2GetPendingMemberships) | **GET** /GroupV2/{groupId}/Members/Pending/ |  |
| [**groupV2GetPotentialGroupsForMember**](GroupV2Api.md#groupV2GetPotentialGroupsForMember) | **GET** /GroupV2/User/Potential/{membershipType}/{membershipId}/{filter}/{groupType}/ |  |
| [**groupV2GetRecommendedGroups**](GroupV2Api.md#groupV2GetRecommendedGroups) | **POST** /GroupV2/Recommended/{groupType}/{createDateRange}/ |  |
| [**groupV2GetUserClanInviteSetting**](GroupV2Api.md#groupV2GetUserClanInviteSetting) | **GET** /GroupV2/GetUserClanInviteSetting/{mType}/ |  |
| [**groupV2GroupSearch**](GroupV2Api.md#groupV2GroupSearch) | **POST** /GroupV2/Search/ |  |
| [**groupV2IndividualGroupInvite**](GroupV2Api.md#groupV2IndividualGroupInvite) | **POST** /GroupV2/{groupId}/Members/IndividualInvite/{membershipType}/{membershipId}/ |  |
| [**groupV2IndividualGroupInviteCancel**](GroupV2Api.md#groupV2IndividualGroupInviteCancel) | **POST** /GroupV2/{groupId}/Members/IndividualInviteCancel/{membershipType}/{membershipId}/ |  |
| [**groupV2KickMember**](GroupV2Api.md#groupV2KickMember) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Kick/ |  |
| [**groupV2RecoverGroupForFounder**](GroupV2Api.md#groupV2RecoverGroupForFounder) | **GET** /GroupV2/Recover/{membershipType}/{membershipId}/{groupType}/ |  |
| [**groupV2UnbanMember**](GroupV2Api.md#groupV2UnbanMember) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Unban/ |  |


<a id="groupV2AbdicateFoundership"></a>
# **groupV2AbdicateFoundership**
> GroupV2GetUserClanInviteSetting200Response groupV2AbdicateFoundership(founderIdNew, groupId, membershipType)



An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long founderIdNew = 56L; // Long | The new founder for this group. Must already be a group admin.
    Long groupId = 56L; // Long | The target group id.
    Integer membershipType = 56; // Integer | Membership type of the provided founderIdNew.
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.groupV2AbdicateFoundership(founderIdNew, groupId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2AbdicateFoundership");
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
| **founderIdNew** | **Long**| The new founder for this group. Must already be a group admin. | |
| **groupId** | **Long**| The target group id. | |
| **membershipType** | **Integer**| Membership type of the provided founderIdNew. | |

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2AddOptionalConversation"></a>
# **groupV2AddOptionalConversation**
> ForumGetTopicForContent200Response groupV2AddOptionalConversation(groupId)



Add a new optional conversation/chat channel. Requires admin permissions to the group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | Group ID of the group to edit.
    try {
      ForumGetTopicForContent200Response result = apiInstance.groupV2AddOptionalConversation(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2AddOptionalConversation");
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
| **groupId** | **Long**| Group ID of the group to edit. | |

### Return type

[**ForumGetTopicForContent200Response**](ForumGetTopicForContent200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2ApproveAllPending"></a>
# **groupV2ApproveAllPending**
> GroupV2ApproveAllPending200Response groupV2ApproveAllPending(groupId)



Approve all of the pending users for the given group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | ID of the group.
    try {
      GroupV2ApproveAllPending200Response result = apiInstance.groupV2ApproveAllPending(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2ApproveAllPending");
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
| **groupId** | **Long**| ID of the group. | |

### Return type

[**GroupV2ApproveAllPending200Response**](GroupV2ApproveAllPending200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2ApprovePending"></a>
# **groupV2ApprovePending**
> GroupV2GetUserClanInviteSetting200Response groupV2ApprovePending(groupId, membershipId, membershipType)



Approve the given membershipId to join the group/clan as long as they have applied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | ID of the group.
    Long membershipId = 56L; // Long | The membership id being approved.
    Integer membershipType = 56; // Integer | Membership type of the supplied membership ID.
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.groupV2ApprovePending(groupId, membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2ApprovePending");
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
| **groupId** | **Long**| ID of the group. | |
| **membershipId** | **Long**| The membership id being approved. | |
| **membershipType** | **Integer**| Membership type of the supplied membership ID. | |

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2ApprovePendingForList"></a>
# **groupV2ApprovePendingForList**
> GroupV2ApproveAllPending200Response groupV2ApprovePendingForList(groupId)



Approve all of the pending users for the given group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | ID of the group.
    try {
      GroupV2ApproveAllPending200Response result = apiInstance.groupV2ApprovePendingForList(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2ApprovePendingForList");
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
| **groupId** | **Long**| ID of the group. | |

### Return type

[**GroupV2ApproveAllPending200Response**](GroupV2ApproveAllPending200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2BanMember"></a>
# **groupV2BanMember**
> Destiny2EquipItem200Response groupV2BanMember(groupId, membershipId, membershipType)



Bans the requested member from the requested group for the specified period of time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | Group ID that has the member to ban.
    Long membershipId = 56L; // Long | Membership ID of the member to ban from the group.
    Integer membershipType = 56; // Integer | Membership type of the provided membership ID.
    try {
      Destiny2EquipItem200Response result = apiInstance.groupV2BanMember(groupId, membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2BanMember");
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
| **groupId** | **Long**| Group ID that has the member to ban. | |
| **membershipId** | **Long**| Membership ID of the member to ban from the group. | |
| **membershipType** | **Integer**| Membership type of the provided membership ID. | |

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2DenyAllPending"></a>
# **groupV2DenyAllPending**
> GroupV2ApproveAllPending200Response groupV2DenyAllPending(groupId)



Deny all of the pending users for the given group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | ID of the group.
    try {
      GroupV2ApproveAllPending200Response result = apiInstance.groupV2DenyAllPending(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2DenyAllPending");
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
| **groupId** | **Long**| ID of the group. | |

### Return type

[**GroupV2ApproveAllPending200Response**](GroupV2ApproveAllPending200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2DenyPendingForList"></a>
# **groupV2DenyPendingForList**
> GroupV2ApproveAllPending200Response groupV2DenyPendingForList(groupId)



Deny all of the pending users for the given group that match the passed-in .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | ID of the group.
    try {
      GroupV2ApproveAllPending200Response result = apiInstance.groupV2DenyPendingForList(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2DenyPendingForList");
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
| **groupId** | **Long**| ID of the group. | |

### Return type

[**GroupV2ApproveAllPending200Response**](GroupV2ApproveAllPending200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2EditClanBanner"></a>
# **groupV2EditClanBanner**
> Destiny2EquipItem200Response groupV2EditClanBanner(groupId)



Edit an existing group&#39;s clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | Group ID of the group to edit.
    try {
      Destiny2EquipItem200Response result = apiInstance.groupV2EditClanBanner(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2EditClanBanner");
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
| **groupId** | **Long**| Group ID of the group to edit. | |

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2EditFounderOptions"></a>
# **groupV2EditFounderOptions**
> Destiny2EquipItem200Response groupV2EditFounderOptions(groupId)



Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | Group ID of the group to edit.
    try {
      Destiny2EquipItem200Response result = apiInstance.groupV2EditFounderOptions(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2EditFounderOptions");
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
| **groupId** | **Long**| Group ID of the group to edit. | |

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2EditGroup"></a>
# **groupV2EditGroup**
> Destiny2EquipItem200Response groupV2EditGroup(groupId)



Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | Group ID of the group to edit.
    try {
      Destiny2EquipItem200Response result = apiInstance.groupV2EditGroup(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2EditGroup");
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
| **groupId** | **Long**| Group ID of the group to edit. | |

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2EditGroupMembership"></a>
# **groupV2EditGroupMembership**
> Destiny2EquipItem200Response groupV2EditGroupMembership(groupId, membershipId, membershipType, memberType)



Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | ID of the group to which the member belongs.
    Long membershipId = 56L; // Long | Membership ID to modify.
    Integer membershipType = 56; // Integer | Membership type of the provide membership ID.
    Integer memberType = 56; // Integer | New membertype for the specified member.
    try {
      Destiny2EquipItem200Response result = apiInstance.groupV2EditGroupMembership(groupId, membershipId, membershipType, memberType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2EditGroupMembership");
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
| **groupId** | **Long**| ID of the group to which the member belongs. | |
| **membershipId** | **Long**| Membership ID to modify. | |
| **membershipType** | **Integer**| Membership type of the provide membership ID. | |
| **memberType** | **Integer**| New membertype for the specified member. | |

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2EditOptionalConversation"></a>
# **groupV2EditOptionalConversation**
> ForumGetTopicForContent200Response groupV2EditOptionalConversation(conversationId, groupId)



Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long conversationId = 56L; // Long | Conversation Id of the channel being edited.
    Long groupId = 56L; // Long | Group ID of the group to edit.
    try {
      ForumGetTopicForContent200Response result = apiInstance.groupV2EditOptionalConversation(conversationId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2EditOptionalConversation");
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
| **conversationId** | **Long**| Conversation Id of the channel being edited. | |
| **groupId** | **Long**| Group ID of the group to edit. | |

### Return type

[**ForumGetTopicForContent200Response**](ForumGetTopicForContent200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetAdminsAndFounderOfGroup"></a>
# **groupV2GetAdminsAndFounderOfGroup**
> GroupV2GetAdminsAndFounderOfGroup200Response groupV2GetAdminsAndFounderOfGroup(currentpage, groupId)



Get the list of members in a given group who are of admin level or higher.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Integer currentpage = 56; // Integer | Page number (starting with 1). Each page has a fixed size of 50 items per page.
    Long groupId = 56L; // Long | The ID of the group.
    try {
      GroupV2GetAdminsAndFounderOfGroup200Response result = apiInstance.groupV2GetAdminsAndFounderOfGroup(currentpage, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetAdminsAndFounderOfGroup");
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
| **currentpage** | **Integer**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | |
| **groupId** | **Long**| The ID of the group. | |

### Return type

[**GroupV2GetAdminsAndFounderOfGroup200Response**](GroupV2GetAdminsAndFounderOfGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetAvailableAvatars"></a>
# **groupV2GetAvailableAvatars**
> GetAvailableLocales200Response groupV2GetAvailableAvatars()



Returns a list of all available group avatars for the signed-in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    try {
      GetAvailableLocales200Response result = apiInstance.groupV2GetAvailableAvatars();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetAvailableAvatars");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAvailableLocales200Response**](GetAvailableLocales200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetAvailableThemes"></a>
# **groupV2GetAvailableThemes**
> GroupV2GetAvailableThemes200Response groupV2GetAvailableThemes()



Returns a list of all available group themes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    try {
      GroupV2GetAvailableThemes200Response result = apiInstance.groupV2GetAvailableThemes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetAvailableThemes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupV2GetAvailableThemes200Response**](GroupV2GetAvailableThemes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetBannedMembersOfGroup"></a>
# **groupV2GetBannedMembersOfGroup**
> GroupV2GetBannedMembersOfGroup200Response groupV2GetBannedMembersOfGroup(currentpage, groupId)



Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Integer currentpage = 56; // Integer | Page number (starting with 1). Each page has a fixed size of 50 entries.
    Long groupId = 56L; // Long | Group ID whose banned members you are fetching
    try {
      GroupV2GetBannedMembersOfGroup200Response result = apiInstance.groupV2GetBannedMembersOfGroup(currentpage, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetBannedMembersOfGroup");
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
| **currentpage** | **Integer**| Page number (starting with 1). Each page has a fixed size of 50 entries. | |
| **groupId** | **Long**| Group ID whose banned members you are fetching | |

### Return type

[**GroupV2GetBannedMembersOfGroup200Response**](GroupV2GetBannedMembersOfGroup200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetGroup"></a>
# **groupV2GetGroup**
> GroupV2GetGroupByName200Response groupV2GetGroup(groupId)



Get information about a specific group of the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | Requested group's id.
    try {
      GroupV2GetGroupByName200Response result = apiInstance.groupV2GetGroup(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetGroup");
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
| **groupId** | **Long**| Requested group&#39;s id. | |

### Return type

[**GroupV2GetGroupByName200Response**](GroupV2GetGroupByName200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetGroupByName"></a>
# **groupV2GetGroupByName**
> GroupV2GetGroupByName200Response groupV2GetGroupByName(groupName, groupType)



Get information about a specific group with the given name and type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    String groupName = "groupName_example"; // String | Exact name of the group to find.
    Integer groupType = 56; // Integer | Type of group to find.
    try {
      GroupV2GetGroupByName200Response result = apiInstance.groupV2GetGroupByName(groupName, groupType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetGroupByName");
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
| **groupName** | **String**| Exact name of the group to find. | |
| **groupType** | **Integer**| Type of group to find. | |

### Return type

[**GroupV2GetGroupByName200Response**](GroupV2GetGroupByName200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetGroupByNameV2"></a>
# **groupV2GetGroupByNameV2**
> GroupV2GetGroupByName200Response groupV2GetGroupByNameV2()



Get information about a specific group with the given name and type. The POST version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    try {
      GroupV2GetGroupByName200Response result = apiInstance.groupV2GetGroupByNameV2();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetGroupByNameV2");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupV2GetGroupByName200Response**](GroupV2GetGroupByName200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetGroupOptionalConversations"></a>
# **groupV2GetGroupOptionalConversations**
> GroupV2GetGroupOptionalConversations200Response groupV2GetGroupOptionalConversations(groupId)



Gets a list of available optional conversation channels and their settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | Requested group's id.
    try {
      GroupV2GetGroupOptionalConversations200Response result = apiInstance.groupV2GetGroupOptionalConversations(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetGroupOptionalConversations");
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
| **groupId** | **Long**| Requested group&#39;s id. | |

### Return type

[**GroupV2GetGroupOptionalConversations200Response**](GroupV2GetGroupOptionalConversations200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetGroupsForMember"></a>
# **groupV2GetGroupsForMember**
> GroupV2GetGroupsForMember200Response groupV2GetGroupsForMember(filter, groupType, membershipId, membershipType)



Get information about the groups that a given member has joined.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Integer filter = 56; // Integer | Filter apply to list of joined groups.
    Integer groupType = 56; // Integer | Type of group the supplied member founded.
    Long membershipId = 56L; // Long | Membership ID to for which to find founded groups.
    Integer membershipType = 56; // Integer | Membership type of the supplied membership ID.
    try {
      GroupV2GetGroupsForMember200Response result = apiInstance.groupV2GetGroupsForMember(filter, groupType, membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetGroupsForMember");
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
| **filter** | **Integer**| Filter apply to list of joined groups. | |
| **groupType** | **Integer**| Type of group the supplied member founded. | |
| **membershipId** | **Long**| Membership ID to for which to find founded groups. | |
| **membershipType** | **Integer**| Membership type of the supplied membership ID. | |

### Return type

[**GroupV2GetGroupsForMember200Response**](GroupV2GetGroupsForMember200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetInvitedIndividuals"></a>
# **groupV2GetInvitedIndividuals**
> GroupV2GetInvitedIndividuals200Response groupV2GetInvitedIndividuals(currentpage, groupId)



Get the list of users who have been invited into the group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Integer currentpage = 56; // Integer | Page number (starting with 1). Each page has a fixed size of 50 items per page.
    Long groupId = 56L; // Long | ID of the group.
    try {
      GroupV2GetInvitedIndividuals200Response result = apiInstance.groupV2GetInvitedIndividuals(currentpage, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetInvitedIndividuals");
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
| **currentpage** | **Integer**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | |
| **groupId** | **Long**| ID of the group. | |

### Return type

[**GroupV2GetInvitedIndividuals200Response**](GroupV2GetInvitedIndividuals200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetMembersOfGroup"></a>
# **groupV2GetMembersOfGroup**
> GroupV2GetAdminsAndFounderOfGroup200Response groupV2GetMembersOfGroup(currentpage, groupId, memberType, nameSearch)



Get the list of members in a given group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Integer currentpage = 56; // Integer | Page number (starting with 1). Each page has a fixed size of 50 items per page.
    Long groupId = 56L; // Long | The ID of the group.
    Integer memberType = 56; // Integer | Filter out other member types. Use None for all members.
    String nameSearch = "nameSearch_example"; // String | The name fragment upon which a search should be executed for members with matching display or unique names.
    try {
      GroupV2GetAdminsAndFounderOfGroup200Response result = apiInstance.groupV2GetMembersOfGroup(currentpage, groupId, memberType, nameSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetMembersOfGroup");
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
| **currentpage** | **Integer**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | |
| **groupId** | **Long**| The ID of the group. | |
| **memberType** | **Integer**| Filter out other member types. Use None for all members. | [optional] |
| **nameSearch** | **String**| The name fragment upon which a search should be executed for members with matching display or unique names. | [optional] |

### Return type

[**GroupV2GetAdminsAndFounderOfGroup200Response**](GroupV2GetAdminsAndFounderOfGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetPendingMemberships"></a>
# **groupV2GetPendingMemberships**
> GroupV2GetInvitedIndividuals200Response groupV2GetPendingMemberships(currentpage, groupId)



Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Integer currentpage = 56; // Integer | Page number (starting with 1). Each page has a fixed size of 50 items per page.
    Long groupId = 56L; // Long | ID of the group.
    try {
      GroupV2GetInvitedIndividuals200Response result = apiInstance.groupV2GetPendingMemberships(currentpage, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetPendingMemberships");
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
| **currentpage** | **Integer**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | |
| **groupId** | **Long**| ID of the group. | |

### Return type

[**GroupV2GetInvitedIndividuals200Response**](GroupV2GetInvitedIndividuals200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetPotentialGroupsForMember"></a>
# **groupV2GetPotentialGroupsForMember**
> GroupV2GetPotentialGroupsForMember200Response groupV2GetPotentialGroupsForMember(filter, groupType, membershipId, membershipType)



Get information about the groups that a given member has applied to or been invited to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Integer filter = 56; // Integer | Filter apply to list of potential joined groups.
    Integer groupType = 56; // Integer | Type of group the supplied member applied.
    Long membershipId = 56L; // Long | Membership ID to for which to find applied groups.
    Integer membershipType = 56; // Integer | Membership type of the supplied membership ID.
    try {
      GroupV2GetPotentialGroupsForMember200Response result = apiInstance.groupV2GetPotentialGroupsForMember(filter, groupType, membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetPotentialGroupsForMember");
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
| **filter** | **Integer**| Filter apply to list of potential joined groups. | |
| **groupType** | **Integer**| Type of group the supplied member applied. | |
| **membershipId** | **Long**| Membership ID to for which to find applied groups. | |
| **membershipType** | **Integer**| Membership type of the supplied membership ID. | |

### Return type

[**GroupV2GetPotentialGroupsForMember200Response**](GroupV2GetPotentialGroupsForMember200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetRecommendedGroups"></a>
# **groupV2GetRecommendedGroups**
> GroupV2GetRecommendedGroups200Response groupV2GetRecommendedGroups(createDateRange, groupType)



Gets groups recommended for you based on the groups to whom those you follow belong.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Integer createDateRange = 56; // Integer | Requested range in which to pull recommended groups
    Integer groupType = 56; // Integer | Type of groups requested
    try {
      GroupV2GetRecommendedGroups200Response result = apiInstance.groupV2GetRecommendedGroups(createDateRange, groupType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetRecommendedGroups");
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
| **createDateRange** | **Integer**| Requested range in which to pull recommended groups | |
| **groupType** | **Integer**| Type of groups requested | |

### Return type

[**GroupV2GetRecommendedGroups200Response**](GroupV2GetRecommendedGroups200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GetUserClanInviteSetting"></a>
# **groupV2GetUserClanInviteSetting**
> GroupV2GetUserClanInviteSetting200Response groupV2GetUserClanInviteSetting(mType)



Gets the state of the user&#39;s clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Integer mType = 56; // Integer | The Destiny membership type of the account we wish to access settings.
    try {
      GroupV2GetUserClanInviteSetting200Response result = apiInstance.groupV2GetUserClanInviteSetting(mType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GetUserClanInviteSetting");
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
| **mType** | **Integer**| The Destiny membership type of the account we wish to access settings. | |

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2GroupSearch"></a>
# **groupV2GroupSearch**
> GroupV2GroupSearch200Response groupV2GroupSearch()



Search for Groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    try {
      GroupV2GroupSearch200Response result = apiInstance.groupV2GroupSearch();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2GroupSearch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupV2GroupSearch200Response**](GroupV2GroupSearch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2IndividualGroupInvite"></a>
# **groupV2IndividualGroupInvite**
> GroupV2IndividualGroupInvite200Response groupV2IndividualGroupInvite(groupId, membershipId, membershipType)



Invite a user to join this group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | ID of the group you would like to join.
    Long membershipId = 56L; // Long | Membership id of the account being invited.
    Integer membershipType = 56; // Integer | MembershipType of the account being invited.
    try {
      GroupV2IndividualGroupInvite200Response result = apiInstance.groupV2IndividualGroupInvite(groupId, membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2IndividualGroupInvite");
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
| **groupId** | **Long**| ID of the group you would like to join. | |
| **membershipId** | **Long**| Membership id of the account being invited. | |
| **membershipType** | **Integer**| MembershipType of the account being invited. | |

### Return type

[**GroupV2IndividualGroupInvite200Response**](GroupV2IndividualGroupInvite200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2IndividualGroupInviteCancel"></a>
# **groupV2IndividualGroupInviteCancel**
> GroupV2IndividualGroupInvite200Response groupV2IndividualGroupInviteCancel(groupId, membershipId, membershipType)



Cancels a pending invitation to join a group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | ID of the group you would like to join.
    Long membershipId = 56L; // Long | Membership id of the account being cancelled.
    Integer membershipType = 56; // Integer | MembershipType of the account being cancelled.
    try {
      GroupV2IndividualGroupInvite200Response result = apiInstance.groupV2IndividualGroupInviteCancel(groupId, membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2IndividualGroupInviteCancel");
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
| **groupId** | **Long**| ID of the group you would like to join. | |
| **membershipId** | **Long**| Membership id of the account being cancelled. | |
| **membershipType** | **Integer**| MembershipType of the account being cancelled. | |

### Return type

[**GroupV2IndividualGroupInvite200Response**](GroupV2IndividualGroupInvite200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2KickMember"></a>
# **groupV2KickMember**
> GroupV2KickMember200Response groupV2KickMember(groupId, membershipId, membershipType)



Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | Group ID to kick the user from.
    Long membershipId = 56L; // Long | Membership ID to kick.
    Integer membershipType = 56; // Integer | Membership type of the provided membership ID.
    try {
      GroupV2KickMember200Response result = apiInstance.groupV2KickMember(groupId, membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2KickMember");
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
| **groupId** | **Long**| Group ID to kick the user from. | |
| **membershipId** | **Long**| Membership ID to kick. | |
| **membershipType** | **Integer**| Membership type of the provided membership ID. | |

### Return type

[**GroupV2KickMember200Response**](GroupV2KickMember200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2RecoverGroupForFounder"></a>
# **groupV2RecoverGroupForFounder**
> GroupV2RecoverGroupForFounder200Response groupV2RecoverGroupForFounder(groupType, membershipId, membershipType)



Allows a founder to manually recover a group they can see in game but not on bungie.net

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Integer groupType = 56; // Integer | Type of group the supplied member founded.
    Long membershipId = 56L; // Long | Membership ID to for which to find founded groups.
    Integer membershipType = 56; // Integer | Membership type of the supplied membership ID.
    try {
      GroupV2RecoverGroupForFounder200Response result = apiInstance.groupV2RecoverGroupForFounder(groupType, membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2RecoverGroupForFounder");
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
| **groupType** | **Integer**| Type of group the supplied member founded. | |
| **membershipId** | **Long**| Membership ID to for which to find founded groups. | |
| **membershipType** | **Integer**| Membership type of the supplied membership ID. | |

### Return type

[**GroupV2RecoverGroupForFounder200Response**](GroupV2RecoverGroupForFounder200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="groupV2UnbanMember"></a>
# **groupV2UnbanMember**
> Destiny2EquipItem200Response groupV2UnbanMember(groupId, membershipId, membershipType)



Unbans the requested member, allowing them to re-apply for membership.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupV2Api apiInstance = new GroupV2Api(defaultClient);
    Long groupId = 56L; // Long | 
    Long membershipId = 56L; // Long | Membership ID of the member to unban from the group
    Integer membershipType = 56; // Integer | Membership type of the provided membership ID.
    try {
      Destiny2EquipItem200Response result = apiInstance.groupV2UnbanMember(groupId, membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupV2Api#groupV2UnbanMember");
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
| **groupId** | **Long**|  | |
| **membershipId** | **Long**| Membership ID of the member to unban from the group | |
| **membershipType** | **Integer**| Membership type of the provided membership ID. | |

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |


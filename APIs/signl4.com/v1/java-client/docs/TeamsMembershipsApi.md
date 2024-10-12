# TeamsMembershipsApi

All URIs are relative to *https://connect.signl4.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**teamsTeamIdMembershipsGet**](TeamsMembershipsApi.md#teamsTeamIdMembershipsGet) | **GET** /teams/{teamId}/memberships | Get all invites of a team. |
| [**teamsTeamIdMembershipsPost**](TeamsMembershipsApi.md#teamsTeamIdMembershipsPost) | **POST** /teams/{teamId}/memberships | Invite users to a team |
| [**teamsTeamIdMembershipsResendInviteMailPost**](TeamsMembershipsApi.md#teamsTeamIdMembershipsResendInviteMailPost) | **POST** /teams/{teamId}/memberships/resendInviteMail | Sends invite email again if an invite exists |
| [**teamsTeamIdMembershipsUserIdDelete**](TeamsMembershipsApi.md#teamsTeamIdMembershipsUserIdDelete) | **DELETE** /teams/{teamId}/memberships/{userId} | Removes a user or invitation from a team, and may delete the user if he is not in any team. |
| [**teamsTeamIdMembershipsUserIdPut**](TeamsMembershipsApi.md#teamsTeamIdMembershipsUserIdPut) | **PUT** /teams/{teamId}/memberships/{userId} | Update user&#39;s team membership. |


<a id="teamsTeamIdMembershipsGet"></a>
# **teamsTeamIdMembershipsGet**
> List&lt;InvitedUserInfo&gt; teamsTeamIdMembershipsGet(teamId)

Get all invites of a team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsMembershipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsMembershipsApi apiInstance = new TeamsMembershipsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team ID of team you want to request.
    try {
      List<InvitedUserInfo> result = apiInstance.teamsTeamIdMembershipsGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsMembershipsApi#teamsTeamIdMembershipsGet");
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
| **teamId** | **String**| Team ID of team you want to request. | |

### Return type

[**List&lt;InvitedUserInfo&gt;**](InvitedUserInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User invitations are returned. |  -  |
| **204** | Request was canceled. |  -  |
| **400** | Required parameters or authentifaction info could not be found in the request/claims. |  -  |
| **403** | You&#39;re not allowed to request the access all required entities. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdMembershipsPost"></a>
# **teamsTeamIdMembershipsPost**
> List&lt;UserInvitationResult&gt; teamsTeamIdMembershipsPost(teamId, usersInvitation)

Invite users to a team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsMembershipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsMembershipsApi apiInstance = new TeamsMembershipsApi(defaultClient);
    String teamId = "teamId_example"; // String | Id of team the user should be invited to.
    UsersInvitation usersInvitation = new UsersInvitation(); // UsersInvitation | Information about user to invite and inviter id.
    try {
      List<UserInvitationResult> result = apiInstance.teamsTeamIdMembershipsPost(teamId, usersInvitation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsMembershipsApi#teamsTeamIdMembershipsPost");
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
| **teamId** | **String**| Id of team the user should be invited to. | |
| **usersInvitation** | [**UsersInvitation**](UsersInvitation.md)| Information about user to invite and inviter id. | [optional] |

### Return type

[**List&lt;UserInvitationResult&gt;**](UserInvitationResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User invitation results are returned. |  -  |
| **204** | Request was canceled. |  -  |
| **400** | Required parameters or authentifaction info could not be found in the request/claims. |  -  |
| **403** | You&#39;re not allowed to request the access all required entities. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdMembershipsResendInviteMailPost"></a>
# **teamsTeamIdMembershipsResendInviteMailPost**
> String teamsTeamIdMembershipsResendInviteMailPost(teamId, userInvitationInfo)

Sends invite email again if an invite exists

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsMembershipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsMembershipsApi apiInstance = new TeamsMembershipsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team ID of team with invited user.
    UserInvitationInfo userInvitationInfo = new UserInvitationInfo(); // UserInvitationInfo | Information which user should be invited again.
    try {
      String result = apiInstance.teamsTeamIdMembershipsResendInviteMailPost(teamId, userInvitationInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsMembershipsApi#teamsTeamIdMembershipsResendInviteMailPost");
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
| **teamId** | **String**| Team ID of team with invited user. | |
| **userInvitationInfo** | [**UserInvitationInfo**](UserInvitationInfo.md)| Information which user should be invited again. | [optional] |

### Return type

**String**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdMembershipsUserIdDelete"></a>
# **teamsTeamIdMembershipsUserIdDelete**
> String teamsTeamIdMembershipsUserIdDelete(teamId, userId, requesterUserId)

Removes a user or invitation from a team, and may delete the user if he is not in any team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsMembershipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsMembershipsApi apiInstance = new TeamsMembershipsApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the user should be deleted from
    String userId = "userId_example"; // String | ID of the user that should be deleted
    String requesterUserId = "requesterUserId_example"; // String | User ID of user which will remove the other user.
    try {
      String result = apiInstance.teamsTeamIdMembershipsUserIdDelete(teamId, userId, requesterUserId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsMembershipsApi#teamsTeamIdMembershipsUserIdDelete");
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
| **teamId** | **String**| ID of the team the user should be deleted from | |
| **userId** | **String**| ID of the user that should be deleted | |
| **requesterUserId** | **String**| User ID of user which will remove the other user. | [optional] |

### Return type

**String**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success message |  -  |
| **204** | Request was canceled. |  -  |
| **400** | Required parameters or authentifaction info could not be found in the request/claims. |  -  |
| **403** | You&#39;re not allowed to request the access all required entities. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdMembershipsUserIdPut"></a>
# **teamsTeamIdMembershipsUserIdPut**
> UserInfo teamsTeamIdMembershipsUserIdPut(teamId, userId, requesterUserId, userMembership)

Update user&#39;s team membership.

Updates the user&#39;s team membership. You can move the user to another team within the subscription  and/or change the user&#39;s role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsMembershipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamsMembershipsApi apiInstance = new TeamsMembershipsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team the user you want to update belongs to at the moment.
    String userId = "userId_example"; // String | User ID of user you want to update.
    String requesterUserId = "requesterUserId_example"; // String | User ID of user which you want to change role with. This must be provided when using an api key. This user must have role administrator (for setting administrator role) or team administrator (for setting  rights.
    UserMembership userMembership = new UserMembership(); // UserMembership | Information about role id and target team id.
    try {
      UserInfo result = apiInstance.teamsTeamIdMembershipsUserIdPut(teamId, userId, requesterUserId, userMembership);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsMembershipsApi#teamsTeamIdMembershipsUserIdPut");
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
| **teamId** | **String**| Team the user you want to update belongs to at the moment. | |
| **userId** | **String**| User ID of user you want to update. | |
| **requesterUserId** | **String**| User ID of user which you want to change role with. This must be provided when using an api key. This user must have role administrator (for setting administrator role) or team administrator (for setting  rights. | [optional] |
| **userMembership** | [**UserMembership**](UserMembership.md)| Information about role id and target team id. | [optional] |

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User was successfully updated. |  -  |
| **204** | Request was canceled. |  -  |
| **400** | Required parameters or authentifaction info could not be found in the request/claims. |  -  |
| **403** | You&#39;re not allowed to request the access all required entities. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Server Error |  -  |


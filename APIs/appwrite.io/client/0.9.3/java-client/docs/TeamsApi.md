# TeamsApi

All URIs are relative to *https://appwrite.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**teamsCreate**](TeamsApi.md#teamsCreate) | **POST** /teams | Create Team |
| [**teamsCreateMembership**](TeamsApi.md#teamsCreateMembership) | **POST** /teams/{teamId}/memberships | Create Team Membership |
| [**teamsDelete**](TeamsApi.md#teamsDelete) | **DELETE** /teams/{teamId} | Delete Team |
| [**teamsDeleteMembership**](TeamsApi.md#teamsDeleteMembership) | **DELETE** /teams/{teamId}/memberships/{membershipId} | Delete Team Membership |
| [**teamsGet**](TeamsApi.md#teamsGet) | **GET** /teams/{teamId} | Get Team |
| [**teamsGetMemberships**](TeamsApi.md#teamsGetMemberships) | **GET** /teams/{teamId}/memberships | Get Team Memberships |
| [**teamsList**](TeamsApi.md#teamsList) | **GET** /teams | List Teams |
| [**teamsUpdate**](TeamsApi.md#teamsUpdate) | **PUT** /teams/{teamId} | Update Team |
| [**teamsUpdateMembershipRoles**](TeamsApi.md#teamsUpdateMembershipRoles) | **PATCH** /teams/{teamId}/memberships/{membershipId} | Update Membership Roles |
| [**teamsUpdateMembershipStatus**](TeamsApi.md#teamsUpdateMembershipStatus) | **PATCH** /teams/{teamId}/memberships/{membershipId}/status | Update Team Membership Status |


<a id="teamsCreate"></a>
# **teamsCreate**
> Team teamsCreate(teamsCreateRequest)

Create Team

Create a new team. The user who creates the team will automatically be assigned as the owner of the team. The team owner can invite new members, who will be able add new owners and update or delete the team from your project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    TeamsCreateRequest teamsCreateRequest = new TeamsCreateRequest(); // TeamsCreateRequest | 
    try {
      Team result = apiInstance.teamsCreate(teamsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsCreate");
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
| **teamsCreateRequest** | [**TeamsCreateRequest**](TeamsCreateRequest.md)|  | [optional] |

### Return type

[**Team**](Team.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Team |  -  |

<a id="teamsCreateMembership"></a>
# **teamsCreateMembership**
> Membership teamsCreateMembership(teamId, teamsCreateMembershipRequest)

Create Team Membership

Use this endpoint to invite a new member to join your team. If initiated from Client SDK, an email with a link to join the team will be sent to the new member&#39;s email address if the member doesn&#39;t exist in the project it will be created automatically. If initiated from server side SDKs, new member will automatically be added to the team.  Use the &#39;URL&#39; parameter to redirect the user from the invitation email back to your app. When the user is redirected, use the [Update Team Membership Status](/docs/client/teams#teamsUpdateMembershipStatus) endpoint to allow the user to accept the invitation to the team.  While calling from side SDKs the redirect url can be empty string.  Please note that in order to avoid a [Redirect Attacks](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URL&#39;s are the once from domains you have set when added your platforms in the console interface.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team unique ID.
    TeamsCreateMembershipRequest teamsCreateMembershipRequest = new TeamsCreateMembershipRequest(); // TeamsCreateMembershipRequest | 
    try {
      Membership result = apiInstance.teamsCreateMembership(teamId, teamsCreateMembershipRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsCreateMembership");
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
| **teamId** | **String**| Team unique ID. | |
| **teamsCreateMembershipRequest** | [**TeamsCreateMembershipRequest**](TeamsCreateMembershipRequest.md)|  | [optional] |

### Return type

[**Membership**](Membership.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Membership |  -  |

<a id="teamsDelete"></a>
# **teamsDelete**
> teamsDelete(teamId)

Delete Team

Delete a team by its unique ID. Only team owners have write access for this resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team unique ID.
    try {
      apiInstance.teamsDelete(teamId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsDelete");
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
| **teamId** | **String**| Team unique ID. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="teamsDeleteMembership"></a>
# **teamsDeleteMembership**
> teamsDeleteMembership(teamId, membershipId)

Delete Team Membership

This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team unique ID.
    String membershipId = "membershipId_example"; // String | Membership ID.
    try {
      apiInstance.teamsDeleteMembership(teamId, membershipId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsDeleteMembership");
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
| **teamId** | **String**| Team unique ID. | |
| **membershipId** | **String**| Membership ID. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="teamsGet"></a>
# **teamsGet**
> Team teamsGet(teamId)

Get Team

Get a team by its unique ID. All team members have read access for this resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team unique ID.
    try {
      Team result = apiInstance.teamsGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGet");
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
| **teamId** | **String**| Team unique ID. | |

### Return type

[**Team**](Team.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team |  -  |

<a id="teamsGetMemberships"></a>
# **teamsGetMemberships**
> MembershipList teamsGetMemberships(teamId, search, limit, offset, orderType)

Get Team Memberships

Get a team members by the team unique ID. All team members have read access for this list of resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team unique ID.
    String search = ""; // String | Search term to filter your list results. Max length: 256 chars.
    Integer limit = 25; // Integer | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    Integer offset = 0; // Integer | Results offset. The default value is 0. Use this param to manage pagination.
    String orderType = "ASC"; // String | Order result by ASC or DESC order.
    try {
      MembershipList result = apiInstance.teamsGetMemberships(teamId, search, limit, offset, orderType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGetMemberships");
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
| **teamId** | **String**| Team unique ID. | |
| **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to ] |
| **limit** | **Integer**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25] |
| **offset** | **Integer**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0] |
| **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to ASC] |

### Return type

[**MembershipList**](MembershipList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Memberships List |  -  |

<a id="teamsList"></a>
# **teamsList**
> TeamList teamsList(search, limit, offset, orderType)

List Teams

Get a list of all the current user teams. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s teams. [Learn more about different API modes](/docs/admin).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String search = ""; // String | Search term to filter your list results. Max length: 256 chars.
    Integer limit = 25; // Integer | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    Integer offset = 0; // Integer | Results offset. The default value is 0. Use this param to manage pagination.
    String orderType = "ASC"; // String | Order result by ASC or DESC order.
    try {
      TeamList result = apiInstance.teamsList(search, limit, offset, orderType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsList");
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
| **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to ] |
| **limit** | **Integer**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25] |
| **offset** | **Integer**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0] |
| **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to ASC] |

### Return type

[**TeamList**](TeamList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Teams List |  -  |

<a id="teamsUpdate"></a>
# **teamsUpdate**
> Team teamsUpdate(teamId, teamsUpdateRequest)

Update Team

Update a team by its unique ID. Only team owners have write access for this resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team unique ID.
    TeamsUpdateRequest teamsUpdateRequest = new TeamsUpdateRequest(); // TeamsUpdateRequest | 
    try {
      Team result = apiInstance.teamsUpdate(teamId, teamsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsUpdate");
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
| **teamId** | **String**| Team unique ID. | |
| **teamsUpdateRequest** | [**TeamsUpdateRequest**](TeamsUpdateRequest.md)|  | [optional] |

### Return type

[**Team**](Team.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team |  -  |

<a id="teamsUpdateMembershipRoles"></a>
# **teamsUpdateMembershipRoles**
> Membership teamsUpdateMembershipRoles(teamId, membershipId, teamsUpdateMembershipRolesRequest)

Update Membership Roles



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team unique ID.
    String membershipId = "membershipId_example"; // String | Membership ID.
    TeamsUpdateMembershipRolesRequest teamsUpdateMembershipRolesRequest = new TeamsUpdateMembershipRolesRequest(); // TeamsUpdateMembershipRolesRequest | 
    try {
      Membership result = apiInstance.teamsUpdateMembershipRoles(teamId, membershipId, teamsUpdateMembershipRolesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsUpdateMembershipRoles");
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
| **teamId** | **String**| Team unique ID. | |
| **membershipId** | **String**| Membership ID. | |
| **teamsUpdateMembershipRolesRequest** | [**TeamsUpdateMembershipRolesRequest**](TeamsUpdateMembershipRolesRequest.md)|  | [optional] |

### Return type

[**Membership**](Membership.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Membership |  -  |

<a id="teamsUpdateMembershipStatus"></a>
# **teamsUpdateMembershipStatus**
> Membership teamsUpdateMembershipStatus(teamId, membershipId, teamsUpdateMembershipStatusRequest)

Update Team Membership Status

Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email recieved by the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String teamId = "teamId_example"; // String | Team unique ID.
    String membershipId = "membershipId_example"; // String | Membership ID.
    TeamsUpdateMembershipStatusRequest teamsUpdateMembershipStatusRequest = new TeamsUpdateMembershipStatusRequest(); // TeamsUpdateMembershipStatusRequest | 
    try {
      Membership result = apiInstance.teamsUpdateMembershipStatus(teamId, membershipId, teamsUpdateMembershipStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsUpdateMembershipStatus");
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
| **teamId** | **String**| Team unique ID. | |
| **membershipId** | **String**| Membership ID. | |
| **teamsUpdateMembershipStatusRequest** | [**TeamsUpdateMembershipStatusRequest**](TeamsUpdateMembershipStatusRequest.md)|  | [optional] |

### Return type

[**Membership**](Membership.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Membership |  -  |


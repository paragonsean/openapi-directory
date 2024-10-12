# GroupsApi

All URIs are relative to *https://gitlab.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteV3GroupsId**](GroupsApi.md#deleteV3GroupsId) | **DELETE** /v3/groups/{id} | Remove a group. |
| [**deleteV3GroupsIdAccessRequestsUserId**](GroupsApi.md#deleteV3GroupsIdAccessRequestsUserId) | **DELETE** /v3/groups/{id}/access_requests/{user_id} | Denies an access request for the given user. |
| [**deleteV3GroupsIdMembersUserId**](GroupsApi.md#deleteV3GroupsIdMembersUserId) | **DELETE** /v3/groups/{id}/members/{user_id} | Removes a user from a group or project. |
| [**getV3Groups**](GroupsApi.md#getV3Groups) | **GET** /v3/groups | Get a groups list |
| [**getV3GroupsId**](GroupsApi.md#getV3GroupsId) | **GET** /v3/groups/{id} | Get a single group, with containing projects. |
| [**getV3GroupsIdAccessRequests**](GroupsApi.md#getV3GroupsIdAccessRequests) | **GET** /v3/groups/{id}/access_requests | Gets a list of access requests for a group. |
| [**getV3GroupsIdIssues**](GroupsApi.md#getV3GroupsIdIssues) | **GET** /v3/groups/{id}/issues | Get a list of group issues |
| [**getV3GroupsIdMembers**](GroupsApi.md#getV3GroupsIdMembers) | **GET** /v3/groups/{id}/members | Gets a list of group or project members viewable by the authenticated user. |
| [**getV3GroupsIdMembersUserId**](GroupsApi.md#getV3GroupsIdMembersUserId) | **GET** /v3/groups/{id}/members/{user_id} | Gets a member of a group or project. |
| [**getV3GroupsIdNotificationSettings**](GroupsApi.md#getV3GroupsIdNotificationSettings) | **GET** /v3/groups/{id}/notification_settings | Get group level notification level settings, defaults to Global |
| [**getV3GroupsIdProjects**](GroupsApi.md#getV3GroupsIdProjects) | **GET** /v3/groups/{id}/projects | Get a list of projects in this group. |
| [**getV3GroupsOwned**](GroupsApi.md#getV3GroupsOwned) | **GET** /v3/groups/owned | Get list of owned groups for authenticated user |
| [**postV3Groups**](GroupsApi.md#postV3Groups) | **POST** /v3/groups | Create a group. Available only for users who can create groups. |
| [**postV3GroupsIdAccessRequests**](GroupsApi.md#postV3GroupsIdAccessRequests) | **POST** /v3/groups/{id}/access_requests | Requests access for the authenticated user to a group. |
| [**postV3GroupsIdMembers**](GroupsApi.md#postV3GroupsIdMembers) | **POST** /v3/groups/{id}/members | Adds a member to a group or project. |
| [**postV3GroupsIdProjectsProjectId**](GroupsApi.md#postV3GroupsIdProjectsProjectId) | **POST** /v3/groups/{id}/projects/{project_id} | Transfer a project to the group namespace. Available only for admin. |
| [**putV3GroupsId**](GroupsApi.md#putV3GroupsId) | **PUT** /v3/groups/{id} | Update a group. Available only for users who can administrate groups. |
| [**putV3GroupsIdAccessRequestsUserIdApprove**](GroupsApi.md#putV3GroupsIdAccessRequestsUserIdApprove) | **PUT** /v3/groups/{id}/access_requests/{user_id}/approve | Approves an access request for the given user. |
| [**putV3GroupsIdMembersUserId**](GroupsApi.md#putV3GroupsIdMembersUserId) | **PUT** /v3/groups/{id}/members/{user_id} | Updates a member of a group or project. |
| [**putV3GroupsIdNotificationSettings**](GroupsApi.md#putV3GroupsIdNotificationSettings) | **PUT** /v3/groups/{id}/notification_settings | Update group level notification level settings, defaults to Global |


<a id="deleteV3GroupsId"></a>
# **deleteV3GroupsId**
> deleteV3GroupsId(id)

Remove a group.

Remove a group.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The ID of a group
    try {
      apiInstance.deleteV3GroupsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#deleteV3GroupsId");
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
| **id** | **String**| The ID of a group | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Remove a group. |  -  |

<a id="deleteV3GroupsIdAccessRequestsUserId"></a>
# **deleteV3GroupsIdAccessRequestsUserId**
> deleteV3GroupsIdAccessRequestsUserId(id, userId)

Denies an access request for the given user.

This feature was introduced in GitLab 8.11.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID
    Integer userId = 56; // Integer | The user ID of the access requester
    try {
      apiInstance.deleteV3GroupsIdAccessRequestsUserId(id, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#deleteV3GroupsIdAccessRequestsUserId");
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
| **id** | **String**| The group ID | |
| **userId** | **Integer**| The user ID of the access requester | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Denies an access request for the given user. |  -  |

<a id="deleteV3GroupsIdMembersUserId"></a>
# **deleteV3GroupsIdMembersUserId**
> deleteV3GroupsIdMembersUserId(id, userId)

Removes a user from a group or project.

Removes a user from a group or project.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID
    Integer userId = 56; // Integer | The user ID of the member
    try {
      apiInstance.deleteV3GroupsIdMembersUserId(id, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#deleteV3GroupsIdMembersUserId");
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
| **id** | **String**| The group ID | |
| **userId** | **Integer**| The user ID of the member | |

### Return type

null (empty response body)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Removes a user from a group or project. |  -  |

<a id="getV3Groups"></a>
# **getV3Groups**
> Group getV3Groups(statistics, allAvailable, search, orderBy, sort, page, perPage, skipGroups)

Get a groups list

Get a groups list

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Boolean statistics = true; // Boolean | Include project statistics
    Boolean allAvailable = true; // Boolean | Show all group that you have access to
    String search = "search_example"; // String | Search for a specific group
    String orderBy = "name"; // String | Order by name or path
    String sort = "asc"; // String | Sort by asc (ascending) or desc (descending)
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    List<Integer> skipGroups = Arrays.asList(); // List<Integer> | Array of group ids to exclude from list
    try {
      Group result = apiInstance.getV3Groups(statistics, allAvailable, search, orderBy, sort, page, perPage, skipGroups);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getV3Groups");
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
| **statistics** | **Boolean**| Include project statistics | [optional] |
| **allAvailable** | **Boolean**| Show all group that you have access to | [optional] |
| **search** | **String**| Search for a specific group | [optional] |
| **orderBy** | **String**| Order by name or path | [optional] [default to name] [enum: name, path] |
| **sort** | **String**| Sort by asc (ascending) or desc (descending) | [optional] [default to asc] [enum: asc, desc] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |
| **skipGroups** | [**List&lt;Integer&gt;**](Integer.md)| Array of group ids to exclude from list | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a groups list |  -  |

<a id="getV3GroupsId"></a>
# **getV3GroupsId**
> GroupDetail getV3GroupsId(id)

Get a single group, with containing projects.

Get a single group, with containing projects.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The ID of a group
    try {
      GroupDetail result = apiInstance.getV3GroupsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getV3GroupsId");
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
| **id** | **String**| The ID of a group | |

### Return type

[**GroupDetail**](GroupDetail.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a single group, with containing projects. |  -  |

<a id="getV3GroupsIdAccessRequests"></a>
# **getV3GroupsIdAccessRequests**
> AccessRequester getV3GroupsIdAccessRequests(id, page, perPage)

Gets a list of access requests for a group.

This feature was introduced in GitLab 8.11.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      AccessRequester result = apiInstance.getV3GroupsIdAccessRequests(id, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getV3GroupsIdAccessRequests");
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
| **id** | **String**| The group ID | |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**AccessRequester**](AccessRequester.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets a list of access requests for a group. |  -  |

<a id="getV3GroupsIdIssues"></a>
# **getV3GroupsIdIssues**
> Issue getV3GroupsIdIssues(id, state, labels, milestone, orderBy, sort, page, perPage)

Get a list of group issues

Get a list of group issues

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The ID of a group
    String state = "opened"; // String | Return opened, closed, or all issues
    String labels = "labels_example"; // String | Comma-separated list of label names
    String milestone = "milestone_example"; // String | Return issues for a specific milestone
    String orderBy = "created_at"; // String | Return issues ordered by `created_at` or `updated_at` fields.
    String sort = "asc"; // String | Return issues sorted in `asc` or `desc` order.
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Issue result = apiInstance.getV3GroupsIdIssues(id, state, labels, milestone, orderBy, sort, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getV3GroupsIdIssues");
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
| **id** | **String**| The ID of a group | |
| **state** | **String**| Return opened, closed, or all issues | [optional] [default to opened] [enum: opened, closed, all] |
| **labels** | **String**| Comma-separated list of label names | [optional] |
| **milestone** | **String**| Return issues for a specific milestone | [optional] |
| **orderBy** | **String**| Return issues ordered by &#x60;created_at&#x60; or &#x60;updated_at&#x60; fields. | [optional] [default to created_at] [enum: created_at, updated_at] |
| **sort** | **String**| Return issues sorted in &#x60;asc&#x60; or &#x60;desc&#x60; order. | [optional] [default to desc] [enum: asc, desc] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Issue**](Issue.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of group issues |  -  |

<a id="getV3GroupsIdMembers"></a>
# **getV3GroupsIdMembers**
> Member getV3GroupsIdMembers(id, query, page, perPage)

Gets a list of group or project members viewable by the authenticated user.

Gets a list of group or project members viewable by the authenticated user.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID
    String query = "query_example"; // String | A query string to search for members
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Member result = apiInstance.getV3GroupsIdMembers(id, query, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getV3GroupsIdMembers");
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
| **id** | **String**| The group ID | |
| **query** | **String**| A query string to search for members | [optional] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Member**](Member.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets a list of group or project members viewable by the authenticated user. |  -  |

<a id="getV3GroupsIdMembersUserId"></a>
# **getV3GroupsIdMembersUserId**
> Member getV3GroupsIdMembersUserId(id, userId)

Gets a member of a group or project.

Gets a member of a group or project.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID
    Integer userId = 56; // Integer | The user ID of the member
    try {
      Member result = apiInstance.getV3GroupsIdMembersUserId(id, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getV3GroupsIdMembersUserId");
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
| **id** | **String**| The group ID | |
| **userId** | **Integer**| The user ID of the member | |

### Return type

[**Member**](Member.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets a member of a group or project. |  -  |

<a id="getV3GroupsIdNotificationSettings"></a>
# **getV3GroupsIdNotificationSettings**
> NotificationSetting getV3GroupsIdNotificationSettings(id)

Get group level notification level settings, defaults to Global

This feature was introduced in GitLab 8.12

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID or project ID or project NAMESPACE/PROJECT_NAME
    try {
      NotificationSetting result = apiInstance.getV3GroupsIdNotificationSettings(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getV3GroupsIdNotificationSettings");
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
| **id** | **String**| The group ID or project ID or project NAMESPACE/PROJECT_NAME | |

### Return type

[**NotificationSetting**](NotificationSetting.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get group level notification level settings, defaults to Global |  -  |

<a id="getV3GroupsIdProjects"></a>
# **getV3GroupsIdProjects**
> Project getV3GroupsIdProjects(id, archived, visibility, search, orderBy, sort, simple, page, perPage)

Get a list of projects in this group.

Get a list of projects in this group.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The ID of a group
    Boolean archived = true; // Boolean | Limit by archived status
    String visibility = "public"; // String | Limit by visibility
    String search = "search_example"; // String | Return list of authorized projects matching the search criteria
    String orderBy = "id"; // String | Return projects ordered by field
    String sort = "asc"; // String | Return projects sorted in ascending and descending order
    Boolean simple = true; // Boolean | Return only the ID, URL, name, and path of each project
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Project result = apiInstance.getV3GroupsIdProjects(id, archived, visibility, search, orderBy, sort, simple, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getV3GroupsIdProjects");
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
| **id** | **String**| The ID of a group | |
| **archived** | **Boolean**| Limit by archived status | [optional] |
| **visibility** | **String**| Limit by visibility | [optional] [enum: public, internal, private] |
| **search** | **String**| Return list of authorized projects matching the search criteria | [optional] |
| **orderBy** | **String**| Return projects ordered by field | [optional] [default to created_at] [enum: id, name, path, created_at, updated_at, last_activity_at] |
| **sort** | **String**| Return projects sorted in ascending and descending order | [optional] [default to desc] [enum: asc, desc] |
| **simple** | **Boolean**| Return only the ID, URL, name, and path of each project | [optional] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a list of projects in this group. |  -  |

<a id="getV3GroupsOwned"></a>
# **getV3GroupsOwned**
> Group getV3GroupsOwned(page, perPage, statistics)

Get list of owned groups for authenticated user

Get list of owned groups for authenticated user

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    Boolean statistics = true; // Boolean | Include project statistics
    try {
      Group result = apiInstance.getV3GroupsOwned(page, perPage, statistics);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getV3GroupsOwned");
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
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |
| **statistics** | **Boolean**| Include project statistics | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get list of owned groups for authenticated user |  -  |

<a id="postV3Groups"></a>
# **postV3Groups**
> Group postV3Groups(postV3GroupsRequest)

Create a group. Available only for users who can create groups.

Create a group. Available only for users who can create groups.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    PostV3GroupsRequest postV3GroupsRequest = new PostV3GroupsRequest(); // PostV3GroupsRequest | 
    try {
      Group result = apiInstance.postV3Groups(postV3GroupsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#postV3Groups");
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
| **postV3GroupsRequest** | [**PostV3GroupsRequest**](PostV3GroupsRequest.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create a group. Available only for users who can create groups. |  -  |

<a id="postV3GroupsIdAccessRequests"></a>
# **postV3GroupsIdAccessRequests**
> AccessRequester postV3GroupsIdAccessRequests(id)

Requests access for the authenticated user to a group.

This feature was introduced in GitLab 8.11.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID
    try {
      AccessRequester result = apiInstance.postV3GroupsIdAccessRequests(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#postV3GroupsIdAccessRequests");
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
| **id** | **String**| The group ID | |

### Return type

[**AccessRequester**](AccessRequester.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Requests access for the authenticated user to a group. |  -  |

<a id="postV3GroupsIdMembers"></a>
# **postV3GroupsIdMembers**
> Member postV3GroupsIdMembers(id, postV3GroupsIdMembersRequest)

Adds a member to a group or project.

Adds a member to a group or project.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID
    PostV3GroupsIdMembersRequest postV3GroupsIdMembersRequest = new PostV3GroupsIdMembersRequest(); // PostV3GroupsIdMembersRequest | 
    try {
      Member result = apiInstance.postV3GroupsIdMembers(id, postV3GroupsIdMembersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#postV3GroupsIdMembers");
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
| **id** | **String**| The group ID | |
| **postV3GroupsIdMembersRequest** | [**PostV3GroupsIdMembersRequest**](PostV3GroupsIdMembersRequest.md)|  | |

### Return type

[**Member**](Member.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Adds a member to a group or project. |  -  |

<a id="postV3GroupsIdProjectsProjectId"></a>
# **postV3GroupsIdProjectsProjectId**
> GroupDetail postV3GroupsIdProjectsProjectId(id, projectId)

Transfer a project to the group namespace. Available only for admin.

Transfer a project to the group namespace. Available only for admin.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The ID of a group
    String projectId = "projectId_example"; // String | The ID or path of the project
    try {
      GroupDetail result = apiInstance.postV3GroupsIdProjectsProjectId(id, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#postV3GroupsIdProjectsProjectId");
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
| **id** | **String**| The ID of a group | |
| **projectId** | **String**| The ID or path of the project | |

### Return type

[**GroupDetail**](GroupDetail.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transfer a project to the group namespace. Available only for admin. |  -  |

<a id="putV3GroupsId"></a>
# **putV3GroupsId**
> Group putV3GroupsId(id, putV3GroupsIdRequest)

Update a group. Available only for users who can administrate groups.

Update a group. Available only for users who can administrate groups.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The ID of a group
    PutV3GroupsIdRequest putV3GroupsIdRequest = new PutV3GroupsIdRequest(); // PutV3GroupsIdRequest | 
    try {
      Group result = apiInstance.putV3GroupsId(id, putV3GroupsIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#putV3GroupsId");
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
| **id** | **String**| The ID of a group | |
| **putV3GroupsIdRequest** | [**PutV3GroupsIdRequest**](PutV3GroupsIdRequest.md)|  | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update a group. Available only for users who can administrate groups. |  -  |

<a id="putV3GroupsIdAccessRequestsUserIdApprove"></a>
# **putV3GroupsIdAccessRequestsUserIdApprove**
> Member putV3GroupsIdAccessRequestsUserIdApprove(id, userId, putV3GroupsIdAccessRequestsUserIdApproveRequest)

Approves an access request for the given user.

This feature was introduced in GitLab 8.11.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID
    Integer userId = 56; // Integer | The user ID of the access requester
    PutV3GroupsIdAccessRequestsUserIdApproveRequest putV3GroupsIdAccessRequestsUserIdApproveRequest = new PutV3GroupsIdAccessRequestsUserIdApproveRequest(); // PutV3GroupsIdAccessRequestsUserIdApproveRequest | 
    try {
      Member result = apiInstance.putV3GroupsIdAccessRequestsUserIdApprove(id, userId, putV3GroupsIdAccessRequestsUserIdApproveRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#putV3GroupsIdAccessRequestsUserIdApprove");
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
| **id** | **String**| The group ID | |
| **userId** | **Integer**| The user ID of the access requester | |
| **putV3GroupsIdAccessRequestsUserIdApproveRequest** | [**PutV3GroupsIdAccessRequestsUserIdApproveRequest**](PutV3GroupsIdAccessRequestsUserIdApproveRequest.md)|  | [optional] |

### Return type

[**Member**](Member.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Approves an access request for the given user. |  -  |

<a id="putV3GroupsIdMembersUserId"></a>
# **putV3GroupsIdMembersUserId**
> Member putV3GroupsIdMembersUserId(id, userId, putV3GroupsIdMembersUserIdRequest)

Updates a member of a group or project.

Updates a member of a group or project.

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID
    Integer userId = 56; // Integer | The user ID of the new member
    PutV3GroupsIdMembersUserIdRequest putV3GroupsIdMembersUserIdRequest = new PutV3GroupsIdMembersUserIdRequest(); // PutV3GroupsIdMembersUserIdRequest | 
    try {
      Member result = apiInstance.putV3GroupsIdMembersUserId(id, userId, putV3GroupsIdMembersUserIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#putV3GroupsIdMembersUserId");
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
| **id** | **String**| The group ID | |
| **userId** | **Integer**| The user ID of the new member | |
| **putV3GroupsIdMembersUserIdRequest** | [**PutV3GroupsIdMembersUserIdRequest**](PutV3GroupsIdMembersUserIdRequest.md)|  | |

### Return type

[**Member**](Member.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updates a member of a group or project. |  -  |

<a id="putV3GroupsIdNotificationSettings"></a>
# **putV3GroupsIdNotificationSettings**
> NotificationSetting putV3GroupsIdNotificationSettings(id, putV3GroupsIdNotificationSettingsRequest)

Update group level notification level settings, defaults to Global

This feature was introduced in GitLab 8.12

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
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String id = "id_example"; // String | The group ID or project ID or project NAMESPACE/PROJECT_NAME
    PutV3GroupsIdNotificationSettingsRequest putV3GroupsIdNotificationSettingsRequest = new PutV3GroupsIdNotificationSettingsRequest(); // PutV3GroupsIdNotificationSettingsRequest | 
    try {
      NotificationSetting result = apiInstance.putV3GroupsIdNotificationSettings(id, putV3GroupsIdNotificationSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#putV3GroupsIdNotificationSettings");
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
| **id** | **String**| The group ID or project ID or project NAMESPACE/PROJECT_NAME | |
| **putV3GroupsIdNotificationSettingsRequest** | [**PutV3GroupsIdNotificationSettingsRequest**](PutV3GroupsIdNotificationSettingsRequest.md)|  | [optional] |

### Return type

[**NotificationSetting**](NotificationSetting.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update group level notification level settings, defaults to Global |  -  |


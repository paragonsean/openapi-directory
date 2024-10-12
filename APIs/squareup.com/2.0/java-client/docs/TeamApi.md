# TeamApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkCreateTeamMembers**](TeamApi.md#bulkCreateTeamMembers) | **POST** /v2/team-members/bulk-create | BulkCreateTeamMembers |
| [**bulkUpdateTeamMembers**](TeamApi.md#bulkUpdateTeamMembers) | **POST** /v2/team-members/bulk-update | BulkUpdateTeamMembers |
| [**createTeamMember**](TeamApi.md#createTeamMember) | **POST** /v2/team-members | CreateTeamMember |
| [**retrieveTeamMember**](TeamApi.md#retrieveTeamMember) | **GET** /v2/team-members/{team_member_id} | RetrieveTeamMember |
| [**retrieveWageSetting**](TeamApi.md#retrieveWageSetting) | **GET** /v2/team-members/{team_member_id}/wage-setting | RetrieveWageSetting |
| [**searchTeamMembers**](TeamApi.md#searchTeamMembers) | **POST** /v2/team-members/search | SearchTeamMembers |
| [**updateTeamMember**](TeamApi.md#updateTeamMember) | **PUT** /v2/team-members/{team_member_id} | UpdateTeamMember |
| [**updateWageSetting**](TeamApi.md#updateWageSetting) | **PUT** /v2/team-members/{team_member_id}/wage-setting | UpdateWageSetting |


<a id="bulkCreateTeamMembers"></a>
# **bulkCreateTeamMembers**
> BulkCreateTeamMembersResponse bulkCreateTeamMembers(bulkCreateTeamMembersRequest)

BulkCreateTeamMembers

Creates multiple &#x60;TeamMember&#x60; objects. The created &#x60;TeamMember&#x60; objects are returned on successful creates. This process is non-transactional and processes as much of the request as possible. If one of the creates in the request cannot be successfully processed, the request is not marked as failed, but the body of the response contains explicit error information for the failed create.  Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    BulkCreateTeamMembersRequest bulkCreateTeamMembersRequest = new BulkCreateTeamMembersRequest(); // BulkCreateTeamMembersRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      BulkCreateTeamMembersResponse result = apiInstance.bulkCreateTeamMembers(bulkCreateTeamMembersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#bulkCreateTeamMembers");
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
| **bulkCreateTeamMembersRequest** | [**BulkCreateTeamMembersRequest**](BulkCreateTeamMembersRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**BulkCreateTeamMembersResponse**](BulkCreateTeamMembersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bulkUpdateTeamMembers"></a>
# **bulkUpdateTeamMembers**
> BulkUpdateTeamMembersResponse bulkUpdateTeamMembers(bulkUpdateTeamMembersRequest)

BulkUpdateTeamMembers

Updates multiple &#x60;TeamMember&#x60; objects. The updated &#x60;TeamMember&#x60; objects are returned on successful updates. This process is non-transactional and processes as much of the request as possible. If one of the updates in the request cannot be successfully processed, the request is not marked as failed, but the body of the response contains explicit error information for the failed update. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    BulkUpdateTeamMembersRequest bulkUpdateTeamMembersRequest = new BulkUpdateTeamMembersRequest(); // BulkUpdateTeamMembersRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      BulkUpdateTeamMembersResponse result = apiInstance.bulkUpdateTeamMembers(bulkUpdateTeamMembersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#bulkUpdateTeamMembers");
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
| **bulkUpdateTeamMembersRequest** | [**BulkUpdateTeamMembersRequest**](BulkUpdateTeamMembersRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**BulkUpdateTeamMembersResponse**](BulkUpdateTeamMembersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="createTeamMember"></a>
# **createTeamMember**
> CreateTeamMemberResponse createTeamMember(createTeamMemberRequest)

CreateTeamMember

Creates a single &#x60;TeamMember&#x60; object. The &#x60;TeamMember&#x60; object is returned on successful creates. You must provide the following values in your request to this endpoint: - &#x60;given_name&#x60; - &#x60;family_name&#x60;  Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#createteammember).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    CreateTeamMemberRequest createTeamMemberRequest = new CreateTeamMemberRequest(); // CreateTeamMemberRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateTeamMemberResponse result = apiInstance.createTeamMember(createTeamMemberRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#createTeamMember");
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
| **createTeamMemberRequest** | [**CreateTeamMemberRequest**](CreateTeamMemberRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateTeamMemberResponse**](CreateTeamMemberResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveTeamMember"></a>
# **retrieveTeamMember**
> RetrieveTeamMemberResponse retrieveTeamMember(teamMemberId)

RetrieveTeamMember

Retrieves a &#x60;TeamMember&#x60; object for the given &#x60;TeamMember.id&#x60;. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    String teamMemberId = "teamMemberId_example"; // String | The ID of the team member to retrieve.
    try {
      RetrieveTeamMemberResponse result = apiInstance.retrieveTeamMember(teamMemberId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#retrieveTeamMember");
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
| **teamMemberId** | **String**| The ID of the team member to retrieve. | |

### Return type

[**RetrieveTeamMemberResponse**](RetrieveTeamMemberResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveWageSetting"></a>
# **retrieveWageSetting**
> RetrieveWageSettingResponse retrieveWageSetting(teamMemberId)

RetrieveWageSetting

Retrieves a &#x60;WageSetting&#x60; object for a team member specified by &#x60;TeamMember.id&#x60;. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    String teamMemberId = "teamMemberId_example"; // String | The ID of the team member for which to retrieve the wage setting.
    try {
      RetrieveWageSettingResponse result = apiInstance.retrieveWageSetting(teamMemberId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#retrieveWageSetting");
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
| **teamMemberId** | **String**| The ID of the team member for which to retrieve the wage setting. | |

### Return type

[**RetrieveWageSettingResponse**](RetrieveWageSettingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="searchTeamMembers"></a>
# **searchTeamMembers**
> SearchTeamMembersResponse searchTeamMembers(searchTeamMembersRequest)

SearchTeamMembers

Returns a paginated list of &#x60;TeamMember&#x60; objects for a business. The list can be filtered by the following: - location IDs - &#x60;status&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    SearchTeamMembersRequest searchTeamMembersRequest = new SearchTeamMembersRequest(); // SearchTeamMembersRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      SearchTeamMembersResponse result = apiInstance.searchTeamMembers(searchTeamMembersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#searchTeamMembers");
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
| **searchTeamMembersRequest** | [**SearchTeamMembersRequest**](SearchTeamMembersRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**SearchTeamMembersResponse**](SearchTeamMembersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateTeamMember"></a>
# **updateTeamMember**
> UpdateTeamMemberResponse updateTeamMember(teamMemberId, updateTeamMemberRequest)

UpdateTeamMember

Updates a single &#x60;TeamMember&#x60; object. The &#x60;TeamMember&#x60; object is returned on successful updates. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    String teamMemberId = "teamMemberId_example"; // String | The ID of the team member to update.
    UpdateTeamMemberRequest updateTeamMemberRequest = new UpdateTeamMemberRequest(); // UpdateTeamMemberRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      UpdateTeamMemberResponse result = apiInstance.updateTeamMember(teamMemberId, updateTeamMemberRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#updateTeamMember");
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
| **teamMemberId** | **String**| The ID of the team member to update. | |
| **updateTeamMemberRequest** | [**UpdateTeamMemberRequest**](UpdateTeamMemberRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**UpdateTeamMemberResponse**](UpdateTeamMemberResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateWageSetting"></a>
# **updateWageSetting**
> UpdateWageSettingResponse updateWageSetting(teamMemberId, updateWageSettingRequest)

UpdateWageSetting

Creates or updates a &#x60;WageSetting&#x60; object. The object is created if a &#x60;WageSetting&#x60; with the specified &#x60;team_member_id&#x60; does not exist. Otherwise, it fully replaces the &#x60;WageSetting&#x60; object for the team member. The &#x60;WageSetting&#x60; is returned on a successful update. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TeamApi apiInstance = new TeamApi(defaultClient);
    String teamMemberId = "teamMemberId_example"; // String | The ID of the team member for which to update the `WageSetting` object.
    UpdateWageSettingRequest updateWageSettingRequest = new UpdateWageSettingRequest(); // UpdateWageSettingRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      UpdateWageSettingResponse result = apiInstance.updateWageSetting(teamMemberId, updateWageSettingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#updateWageSetting");
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
| **teamMemberId** | **String**| The ID of the team member for which to update the &#x60;WageSetting&#x60; object. | |
| **updateWageSettingRequest** | [**UpdateWageSettingRequest**](UpdateWageSettingRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**UpdateWageSettingResponse**](UpdateWageSettingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


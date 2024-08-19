# TeamsApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1TeamGet**](TeamsApi.md#apiPublicV1TeamGet) | **GET** /api-public/v1/team | List teams |
| [**apiPublicV1TeamPost**](TeamsApi.md#apiPublicV1TeamPost) | **POST** /api-public/v1/team | Add a team |
| [**apiPublicV1TeamTeamAdminsGet**](TeamsApi.md#apiPublicV1TeamTeamAdminsGet) | **GET** /api-public/v1/team/{team}/admins | Retrieve a list of team admins for a team |
| [**apiPublicV1TeamTeamDelete**](TeamsApi.md#apiPublicV1TeamTeamDelete) | **DELETE** /api-public/v1/team/{team} | Remove a team |
| [**apiPublicV1TeamTeamGet**](TeamsApi.md#apiPublicV1TeamTeamGet) | **GET** /api-public/v1/team/{team} | Retrieve information for a team |
| [**apiPublicV1TeamTeamMembersGet**](TeamsApi.md#apiPublicV1TeamTeamMembersGet) | **GET** /api-public/v1/team/{team}/members | Retrieve a list of members for a team |
| [**apiPublicV1TeamTeamMembersPost**](TeamsApi.md#apiPublicV1TeamTeamMembersPost) | **POST** /api-public/v1/team/{team}/members | Add a team member |
| [**apiPublicV1TeamTeamMembersUserDelete**](TeamsApi.md#apiPublicV1TeamTeamMembersUserDelete) | **DELETE** /api-public/v1/team/{team}/members/{user} | Remove a team member |
| [**apiPublicV1TeamTeamPoliciesGet_0**](TeamsApi.md#apiPublicV1TeamTeamPoliciesGet_0) | **GET** /api-public/v1/team/{team}/policies | Retrieve a list of escalation policies for a team |
| [**apiPublicV1TeamTeamPut**](TeamsApi.md#apiPublicV1TeamTeamPut) | **PUT** /api-public/v1/team/{team} | Update a team |


<a id="apiPublicV1TeamGet"></a>
# **apiPublicV1TeamGet**
> List&lt;TeamDetail&gt; apiPublicV1TeamGet(xVOApiId, xVOApiKey)

List teams

Get a list of teams for your organization.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      List<TeamDetail> result = apiInstance.apiPublicV1TeamGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#apiPublicV1TeamGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**List&lt;TeamDetail&gt;**](TeamDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of teams for your organization |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **422** | You have reached your team limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamPost"></a>
# **apiPublicV1TeamPost**
> TeamDetail apiPublicV1TeamPost(xVOApiId, xVOApiKey, body)

Add a team

Add a team to your organization.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    AddTeamPayload body = new AddTeamPayload(); // AddTeamPayload | The team information
    try {
      TeamDetail result = apiInstance.apiPublicV1TeamPost(xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#apiPublicV1TeamPost");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **body** | [**AddTeamPayload**](AddTeamPayload.md)| The team information | |

### Return type

[**TeamDetail**](TeamDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Some details about the team that was added |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **422** | Team name or email is unavailable, or you have reached your team limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamAdminsGet"></a>
# **apiPublicV1TeamTeamAdminsGet**
> TeamAdminsResponse apiPublicV1TeamTeamAdminsGet(xVOApiId, xVOApiKey, team)

Retrieve a list of team admins for a team

Get the team admins for the specified team.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team
    try {
      TeamAdminsResponse result = apiInstance.apiPublicV1TeamTeamAdminsGet(xVOApiId, xVOApiKey, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#apiPublicV1TeamTeamAdminsGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **team** | **String**| The VictorOps team | |

### Return type

[**TeamAdminsResponse**](TeamAdminsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Some details about the team that was added |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamDelete"></a>
# **apiPublicV1TeamTeamDelete**
> apiPublicV1TeamTeamDelete(xVOApiId, xVOApiKey, team)

Remove a team

Remove a team from your organization.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team to be deleted
    try {
      apiInstance.apiPublicV1TeamTeamDelete(xVOApiId, xVOApiKey, team);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#apiPublicV1TeamTeamDelete");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **team** | **String**| The VictorOps team to be deleted | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team was deleted |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **422** | There was a problem with the delete such as the replacement team was not found.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamGet"></a>
# **apiPublicV1TeamTeamGet**
> TeamDetail apiPublicV1TeamTeamGet(xVOApiId, xVOApiKey, team)

Retrieve information for a team

Get the information for the specified team.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team to fetch
    try {
      TeamDetail result = apiInstance.apiPublicV1TeamTeamGet(xVOApiId, xVOApiKey, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#apiPublicV1TeamTeamGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **team** | **String**| The VictorOps team to fetch | |

### Return type

[**TeamDetail**](TeamDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Some details about the team that was added |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **422** | Team name or email is unavailable, or you have reached your team limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamMembersGet"></a>
# **apiPublicV1TeamTeamMembersGet**
> ListTeamMembersResponse apiPublicV1TeamTeamMembersGet(xVOApiId, xVOApiKey, team)

Retrieve a list of members for a team

Get the members for the specified team.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team to fetch
    try {
      ListTeamMembersResponse result = apiInstance.apiPublicV1TeamTeamMembersGet(xVOApiId, xVOApiKey, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#apiPublicV1TeamTeamMembersGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **team** | **String**| The VictorOps team to fetch | |

### Return type

[**ListTeamMembersResponse**](ListTeamMembersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Some details about the team that was added |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **422** | Team name or email is unavailable, or you have reached your team limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamMembersPost"></a>
# **apiPublicV1TeamTeamMembersPost**
> ListTeamMembersResponse apiPublicV1TeamTeamMembersPost(xVOApiId, xVOApiKey, team, body)

Add a team member

Add a team member to your team.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team to fetch
    AddTeamMemberPayload body = new AddTeamMemberPayload(); // AddTeamMemberPayload | 
    try {
      ListTeamMembersResponse result = apiInstance.apiPublicV1TeamTeamMembersPost(xVOApiId, xVOApiKey, team, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#apiPublicV1TeamTeamMembersPost");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **team** | **String**| The VictorOps team to fetch | |
| **body** | [**AddTeamMemberPayload**](AddTeamMemberPayload.md)|  | |

### Return type

[**ListTeamMembersResponse**](ListTeamMembersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Some details about the team that was added |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **422** | Team name or email is unavailable, or you have reached your team limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamMembersUserDelete"></a>
# **apiPublicV1TeamTeamMembersUserDelete**
> apiPublicV1TeamTeamMembersUserDelete(xVOApiId, xVOApiKey, team, user, body)

Remove a team member

Remove a team from your organization.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team to be deleted
    String user = "user_example"; // String | The team member username
    RemoveTeamMemberPayload body = new RemoveTeamMemberPayload(); // RemoveTeamMemberPayload | The user information
    try {
      apiInstance.apiPublicV1TeamTeamMembersUserDelete(xVOApiId, xVOApiKey, team, user, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#apiPublicV1TeamTeamMembersUserDelete");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **team** | **String**| The VictorOps team to be deleted | |
| **user** | **String**| The team member username | |
| **body** | [**RemoveTeamMemberPayload**](RemoveTeamMemberPayload.md)| The user information | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team was deleted |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **422** | There was a problem with the delete such as the replacement team member was not found.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamPoliciesGet_0"></a>
# **apiPublicV1TeamTeamPoliciesGet_0**
> EscalationPolicyList apiPublicV1TeamTeamPoliciesGet_0(xVOApiId, xVOApiKey, team)

Retrieve a list of escalation policies for a team

Get the escalation policies for the specified team.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team to fetch
    try {
      EscalationPolicyList result = apiInstance.apiPublicV1TeamTeamPoliciesGet_0(xVOApiId, xVOApiKey, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#apiPublicV1TeamTeamPoliciesGet_0");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **team** | **String**| The VictorOps team to fetch | |

### Return type

[**EscalationPolicyList**](EscalationPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The escalation policy list. This does not include details about the actual notification steps of the policy. |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **422** | Team name or email is unavailable, or you have reached your team limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1TeamTeamPut"></a>
# **apiPublicV1TeamTeamPut**
> TeamDetail apiPublicV1TeamTeamPut(xVOApiId, xVOApiKey, team, body)

Update a team

Update the designated team  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team to be updated
    AddTeamPayload body = new AddTeamPayload(); // AddTeamPayload | The team information
    try {
      TeamDetail result = apiInstance.apiPublicV1TeamTeamPut(xVOApiId, xVOApiKey, team, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#apiPublicV1TeamTeamPut");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **team** | **String**| The VictorOps team to be updated | |
| **body** | [**AddTeamPayload**](AddTeamPayload.md)| The team information | |

### Return type

[**TeamDetail**](TeamDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Some details about the team that was added |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team not found |  -  |
| **422** | Team name or email is unavailable, or you have reached your team limit.  |  -  |
| **500** | Internal Server Error |  -  |


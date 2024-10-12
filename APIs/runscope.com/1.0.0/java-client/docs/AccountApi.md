# AccountApi

All URIs are relative to *https://api.runscope.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountGet**](AccountApi.md#accountGet) | **GET** /account | Account Resource |
| [**teamsTeamIdAgentsGet**](AccountApi.md#teamsTeamIdAgentsGet) | **GET** /teams/{teamId}/agents | Team agents list |
| [**teamsTeamIdIntegrationsGet**](AccountApi.md#teamsTeamIdIntegrationsGet) | **GET** /teams/{teamId}/integrations | Team integrations list |
| [**teamsTeamIdPeopleGet**](AccountApi.md#teamsTeamIdPeopleGet) | **GET** /teams/{teamId}/people | Teams Resource |


<a id="accountGet"></a>
# **accountGet**
> AccountGet200Response accountGet()

Account Resource

Information about the authorized account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      AccountGet200Response result = apiInstance.accountGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountGet");
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

[**AccountGet200Response**](AccountGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account owner and team information. |  -  |
| **0** | Unexpected error |  -  |

<a id="teamsTeamIdAgentsGet"></a>
# **teamsTeamIdAgentsGet**
> List&lt;Agent&gt; teamsTeamIdAgentsGet(teamId)

Team agents list

List currently connected agents associated with a given team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String teamId = "teamId_example"; // String | Unique identifier for team
    try {
      List<Agent> result = apiInstance.teamsTeamIdAgentsGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsTeamIdAgentsGet");
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
| **teamId** | **String**| Unique identifier for team | |

### Return type

[**List&lt;Agent&gt;**](Agent.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of the team’s currently connected agents. |  -  |
| **0** | Unexpected error |  -  |

<a id="teamsTeamIdIntegrationsGet"></a>
# **teamsTeamIdIntegrationsGet**
> TeamsTeamIdIntegrationsGet200Response teamsTeamIdIntegrationsGet(teamId)

Team integrations list

Returns a list of integrations configured for the team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String teamId = "teamId_example"; // String | Unique identifier for team
    try {
      TeamsTeamIdIntegrationsGet200Response result = apiInstance.teamsTeamIdIntegrationsGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsTeamIdIntegrationsGet");
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
| **teamId** | **String**| Unique identifier for team | |

### Return type

[**TeamsTeamIdIntegrationsGet200Response**](TeamsTeamIdIntegrationsGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of integrations associated with the team. |  -  |
| **0** | Unexpected error |  -  |

<a id="teamsTeamIdPeopleGet"></a>
# **teamsTeamIdPeopleGet**
> List&lt;Account&gt; teamsTeamIdPeopleGet(teamId)

Teams Resource

List people and integrations associated with a given team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String teamId = "teamId_example"; // String | Unique identifier for team
    try {
      List<Account> result = apiInstance.teamsTeamIdPeopleGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsTeamIdPeopleGet");
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
| **teamId** | **String**| Unique identifier for team | |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of people associated with the team. |  -  |
| **0** | Unexpected error |  -  |


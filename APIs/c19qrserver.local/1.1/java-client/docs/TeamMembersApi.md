# TeamMembersApi

All URIs are relative to *http://c19qrserver.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userPost**](TeamMembersApi.md#userPost) | **POST** /user | Create a user |
| [**userUserIdDelete**](TeamMembersApi.md#userUserIdDelete) | **DELETE** /user/{userId} | Delete a team member&#39;s user record |
| [**userUserIdGet**](TeamMembersApi.md#userUserIdGet) | **GET** /user/{userId} | Retrieve the information associated with a team member&#39;s user record |
| [**usersGet**](TeamMembersApi.md#usersGet) | **GET** /users | Retrieve the information associated with all team members&#39; user records |


<a id="userPost"></a>
# **userPost**
> CreateUserResponse userPost(sample3)

Create a user

Use this endpoint to create a team member (user) record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    TeamMembersApi apiInstance = new TeamMembersApi(defaultClient);
    Sample3 sample3 = new Sample3(); // Sample3 | Create User Payload
    try {
      CreateUserResponse result = apiInstance.userPost(sample3);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMembersApi#userPost");
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
| **sample3** | [**Sample3**](Sample3.md)| Create User Payload | |

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="userUserIdDelete"></a>
# **userUserIdDelete**
> userUserIdDelete(userId)

Delete a team member&#39;s user record

To preserve referential integrity in the database, the user account  will not be deleted from the database. Rather, the password will be set to the empty string, effectively preventing that user from logging in. Furthermore, all active sessions for that user will be deleted, as will any password reset tokens.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    TeamMembersApi apiInstance = new TeamMembersApi(defaultClient);
    Integer userId = 1; // Integer | The ID of the user record to be deleted.
    try {
      apiInstance.userUserIdDelete(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMembersApi#userUserIdDelete");
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
| **userId** | **Integer**| The ID of the user record to be deleted. | |

### Return type

null (empty response body)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="userUserIdGet"></a>
# **userUserIdGet**
> UserRecord userUserIdGet(userId)

Retrieve the information associated with a team member&#39;s user record

Retrieve the information associated with a user&#39;s account 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    TeamMembersApi apiInstance = new TeamMembersApi(defaultClient);
    Integer userId = 1; // Integer | The ID of the user record to be retrieved.
    try {
      UserRecord result = apiInstance.userUserIdGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMembersApi#userUserIdGet");
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
| **userId** | **Integer**| The ID of the user record to be retrieved. | |

### Return type

[**UserRecord**](UserRecord.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="usersGet"></a>
# **usersGet**
> List&lt;UserRecord&gt; usersGet()

Retrieve the information associated with all team members&#39; user records

Retrieve the information associated with all team members&#39; user records 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    TeamMembersApi apiInstance = new TeamMembersApi(defaultClient);
    try {
      List<UserRecord> result = apiInstance.usersGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamMembersApi#usersGet");
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

[**List&lt;UserRecord&gt;**](UserRecord.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |


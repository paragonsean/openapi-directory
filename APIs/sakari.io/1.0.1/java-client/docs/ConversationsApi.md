# ConversationsApi

All URIs are relative to *https://api.sakari.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**conversationsClose**](ConversationsApi.md#conversationsClose) | **PUT** /v1/accounts/{accountId}/conversations/{conversationId}/close | Closes a conversation |
| [**conversationsFetch**](ConversationsApi.md#conversationsFetch) | **GET** /v1/accounts/{accountId}/conversations/{conversationId} | Fetch conversation by ID |
| [**conversationsFetchAll**](ConversationsApi.md#conversationsFetchAll) | **GET** /v1/accounts/{accountId}/conversations | Fetch conversations |


<a id="conversationsClose"></a>
# **conversationsClose**
> ConversationResponse conversationsClose(accountId, conversationId)

Closes a conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String conversationId = "conversationId_example"; // String | ID of conversation
    try {
      ConversationResponse result = apiInstance.conversationsClose(accountId, conversationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsClose");
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
| **accountId** | **String**| Account to apply operations to | |
| **conversationId** | **String**| ID of conversation | |

### Return type

[**ConversationResponse**](ConversationResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="conversationsFetch"></a>
# **conversationsFetch**
> ConversationResponse conversationsFetch(accountId, conversationId)

Fetch conversation by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String conversationId = "conversationId_example"; // String | ID of template to return
    try {
      ConversationResponse result = apiInstance.conversationsFetch(accountId, conversationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsFetch");
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
| **accountId** | **String**| Account to apply operations to | |
| **conversationId** | **String**| ID of template to return | |

### Return type

[**ConversationResponse**](ConversationResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="conversationsFetchAll"></a>
# **conversationsFetchAll**
> ConversationsResponse conversationsFetchAll(accountId, offset, limit)

Fetch conversations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    Long offset = 56L; // Long | Results to skip when paginating through a result set
    Long limit = 56L; // Long | Maximum number of results to return
    try {
      ConversationsResponse result = apiInstance.conversationsFetchAll(accountId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsFetchAll");
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
| **accountId** | **String**| Account to apply operations to | |
| **offset** | **Long**| Results to skip when paginating through a result set | [optional] |
| **limit** | **Long**| Maximum number of results to return | [optional] |

### Return type

[**ConversationsResponse**](ConversationsResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **4XX** | invalid request |  -  |
| **5XX** | invalid request |  -  |


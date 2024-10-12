# MessagesApi

All URIs are relative to *https://api.sakari.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**messagesFetch**](MessagesApi.md#messagesFetch) | **GET** /v1/accounts/{accountId}/messages/{messageId} | Fetch message by id |
| [**messagesFetchAll**](MessagesApi.md#messagesFetchAll) | **GET** /v1/accounts/{accountId}/messages | Fetch messages |
| [**messagesSend**](MessagesApi.md#messagesSend) | **POST** /v1/accounts/{accountId}/messages | Send Messages |


<a id="messagesFetch"></a>
# **messagesFetch**
> MessageResponse messagesFetch(accountId, messageId)

Fetch message by id

Returns a single messag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String messageId = "messageId_example"; // String | ID of message to return
    try {
      MessageResponse result = apiInstance.messagesFetch(accountId, messageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesFetch");
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
| **messageId** | **String**| ID of message to return | |

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="messagesFetchAll"></a>
# **messagesFetchAll**
> MessagesResponse messagesFetchAll(accountId, offset, limit, contactId, conversationId)

Fetch messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    Long offset = 56L; // Long | Results to skip when paginating through a result set
    Long limit = 56L; // Long | Maximum number of results to return
    String contactId = "contactId_example"; // String | ID of contact
    String conversationId = "conversationId_example"; // String | ID of conversation
    try {
      MessagesResponse result = apiInstance.messagesFetchAll(accountId, offset, limit, contactId, conversationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesFetchAll");
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
| **contactId** | **String**| ID of contact | [optional] |
| **conversationId** | **String**| ID of conversation | [optional] |

### Return type

[**MessagesResponse**](MessagesResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="messagesSend"></a>
# **messagesSend**
> SendMessagesResponse messagesSend(accountId, sendMessagesRequest)

Send Messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    SendMessagesRequest sendMessagesRequest = new SendMessagesRequest(); // SendMessagesRequest | 
    try {
      SendMessagesResponse result = apiInstance.messagesSend(accountId, sendMessagesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesSend");
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
| **sendMessagesRequest** | [**SendMessagesRequest**](SendMessagesRequest.md)|  | [optional] |

### Return type

[**SendMessagesResponse**](SendMessagesResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


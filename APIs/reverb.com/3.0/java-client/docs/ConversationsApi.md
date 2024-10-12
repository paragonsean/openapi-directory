# ConversationsApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**conversationsConversationIdOfferPost**](ConversationsApi.md#conversationsConversationIdOfferPost) | **POST** /conversations/{conversation_id}/offer | Make an offer to the other participant in the conversation |
| [**conversationsIdOfferPost**](ConversationsApi.md#conversationsIdOfferPost) | **POST** /conversations/{id}/offer | Make an offer to the other participant in the conversation |


<a id="conversationsConversationIdOfferPost"></a>
# **conversationsConversationIdOfferPost**
> conversationsConversationIdOfferPost(conversationId, conversationsConversationIdOfferPostRequest)

Make an offer to the other participant in the conversation

Make an offer to the other participant in the conversation

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
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String conversationId = "conversationId_example"; // String | 
    ConversationsConversationIdOfferPostRequest conversationsConversationIdOfferPostRequest = new ConversationsConversationIdOfferPostRequest(); // ConversationsConversationIdOfferPostRequest | the content of the request
    try {
      apiInstance.conversationsConversationIdOfferPost(conversationId, conversationsConversationIdOfferPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsConversationIdOfferPost");
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
| **conversationId** | **String**|  | |
| **conversationsConversationIdOfferPostRequest** | [**ConversationsConversationIdOfferPostRequest**](ConversationsConversationIdOfferPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="conversationsIdOfferPost"></a>
# **conversationsIdOfferPost**
> conversationsIdOfferPost(id, conversationsIdOfferPostRequest)

Make an offer to the other participant in the conversation

Make an offer to the other participant in the conversation

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
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String id = "id_example"; // String | 
    ConversationsIdOfferPostRequest conversationsIdOfferPostRequest = new ConversationsIdOfferPostRequest(); // ConversationsIdOfferPostRequest | the content of the request
    try {
      apiInstance.conversationsIdOfferPost(id, conversationsIdOfferPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsIdOfferPost");
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
| **id** | **String**|  | |
| **conversationsIdOfferPostRequest** | [**ConversationsIdOfferPostRequest**](ConversationsIdOfferPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |


# ConversationApi

All URIs are relative to *https://api.nexmo.com/v0.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createConversation**](ConversationApi.md#createConversation) | **POST** /conversations | Create a conversation |
| [**deleteConversation**](ConversationApi.md#deleteConversation) | **DELETE** /conversations/{conversation_id} | Delete a conversation |
| [**listConversations**](ConversationApi.md#listConversations) | **GET** /conversations | List conversations |
| [**recordConversation**](ConversationApi.md#recordConversation) | **PUT** /conversations/{conversation_id}/record | Record a conversation |
| [**replaceConversation**](ConversationApi.md#replaceConversation) | **PUT** /conversations/{conversation_id} | Update a conversation |
| [**retrieveConversation**](ConversationApi.md#retrieveConversation) | **GET** /conversations/{conversation_id} | Retrieve a conversation |


<a id="createConversation"></a>
# **createConversation**
> CreateConversation200Response createConversation(createConversationRequest)

Create a conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ConversationApi apiInstance = new ConversationApi(defaultClient);
    CreateConversationRequest createConversationRequest = new CreateConversationRequest(); // CreateConversationRequest | Conversation Request Payload Object
    try {
      CreateConversation200Response result = apiInstance.createConversation(createConversationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationApi#createConversation");
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
| **createConversationRequest** | [**CreateConversationRequest**](CreateConversationRequest.md)| Conversation Request Payload Object | [optional] |

### Return type

[**CreateConversation200Response**](CreateConversation200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Create / Update Conversation Response Payload Object |  -  |

<a id="deleteConversation"></a>
# **deleteConversation**
> Object deleteConversation(conversationId)

Delete a conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ConversationApi apiInstance = new ConversationApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    try {
      Object result = apiInstance.deleteConversation(conversationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationApi#deleteConversation");
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
| **conversationId** | **String**| Conversation ID | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response with empty JSON |  -  |

<a id="listConversations"></a>
# **listConversations**
> ListConversations200Response listConversations(dateStart, dateEnd, pageSize, recordIndex, order)

List conversations

This endpoint is **DEPRECATED**. Please use [/v0.2/conversations](/api/conversation.v2#get-conversations).  List all conversations associated with your application. This endpoint required an admin JWT. To find all conversations for the currently logged in user, see [GET /users/:id/conversations](#getuserConversations)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ConversationApi apiInstance = new ConversationApi(defaultClient);
    String dateStart = "2018-01-01 10:00:00"; // String | Return the records that occurred after this point in time.
    String dateEnd = "2018-01-01 12:00:00"; // String | Return the records that occurred before this point in time.
    BigDecimal pageSize = new BigDecimal("10"); // BigDecimal | Return this amount of records in the response
    BigDecimal recordIndex = new BigDecimal("0"); // BigDecimal | Return calls from this index in the response
    String order = "asc"; // String | Return the records in ascending or descending order.
    try {
      ListConversations200Response result = apiInstance.listConversations(dateStart, dateEnd, pageSize, recordIndex, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationApi#listConversations");
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
| **dateStart** | **String**| Return the records that occurred after this point in time. | [optional] |
| **dateEnd** | **String**| Return the records that occurred before this point in time. | [optional] |
| **pageSize** | **BigDecimal**| Return this amount of records in the response | [optional] [default to 10] |
| **recordIndex** | **BigDecimal**| Return calls from this index in the response | [optional] [default to 0] |
| **order** | **String**| Return the records in ascending or descending order. | [optional] [default to asc] [enum: asc, desc, ASC, DESC] |

### Return type

[**ListConversations200Response**](ListConversations200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List Conversations Response Payload Object. |  -  |

<a id="recordConversation"></a>
# **recordConversation**
> recordConversation(conversationId, recordConversationRequest)

Record a conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ConversationApi apiInstance = new ConversationApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    RecordConversationRequest recordConversationRequest = new RecordConversationRequest(); // RecordConversationRequest | Record Conversation Request Payload Object
    try {
      apiInstance.recordConversation(conversationId, recordConversationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationApi#recordConversation");
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
| **conversationId** | **String**| Conversation ID | |
| **recordConversationRequest** | [**RecordConversationRequest**](RecordConversationRequest.md)| Record Conversation Request Payload Object | [optional] |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="replaceConversation"></a>
# **replaceConversation**
> CreateConversation200Response replaceConversation(conversationId, createConversationRequest)

Update a conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ConversationApi apiInstance = new ConversationApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    CreateConversationRequest createConversationRequest = new CreateConversationRequest(); // CreateConversationRequest | Conversation Request Payload Object
    try {
      CreateConversation200Response result = apiInstance.replaceConversation(conversationId, createConversationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationApi#replaceConversation");
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
| **conversationId** | **String**| Conversation ID | |
| **createConversationRequest** | [**CreateConversationRequest**](CreateConversationRequest.md)| Conversation Request Payload Object | [optional] |

### Return type

[**CreateConversation200Response**](CreateConversation200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Create / Update Conversation Response Payload Object |  -  |

<a id="retrieveConversation"></a>
# **retrieveConversation**
> RetrieveConversation200Response retrieveConversation(conversationId)

Retrieve a conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ConversationApi apiInstance = new ConversationApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    try {
      RetrieveConversation200Response result = apiInstance.retrieveConversation(conversationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationApi#retrieveConversation");
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
| **conversationId** | **String**| Conversation ID | |

### Return type

[**RetrieveConversation200Response**](RetrieveConversation200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve a conversation |  -  |


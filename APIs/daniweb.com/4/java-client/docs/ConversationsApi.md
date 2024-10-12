# ConversationsApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**conversationsIDGet**](ConversationsApi.md#conversationsIDGet) | **GET** /conversations/{ID} |  |
| [**conversationsIDMessagesGet**](ConversationsApi.md#conversationsIDMessagesGet) | **GET** /conversations/{ID}/messages |  |
| [**conversationsIDMessagesPost**](ConversationsApi.md#conversationsIDMessagesPost) | **POST** /conversations/{ID}/messages |  |
| [**conversationsIDSchedulesPost**](ConversationsApi.md#conversationsIDSchedulesPost) | **POST** /conversations/{ID}/schedules |  |
| [**conversationsIDSearchesPost**](ConversationsApi.md#conversationsIDSearchesPost) | **POST** /conversations/{ID}/searches |  |
| [**conversationsIDStatusesGet**](ConversationsApi.md#conversationsIDStatusesGet) | **GET** /conversations/{ID}/statuses |  |
| [**conversationsIDStatusesPatch**](ConversationsApi.md#conversationsIDStatusesPatch) | **PATCH** /conversations/{ID}/statuses |  |
| [**conversationsSchedulesPost**](ConversationsApi.md#conversationsSchedulesPost) | **POST** /conversations/schedules |  |
| [**conversationsSearchesPost**](ConversationsApi.md#conversationsSearchesPost) | **POST** /conversations/searches |  |
| [**conversationsStatusesGet**](ConversationsApi.md#conversationsStatusesGet) | **GET** /conversations/statuses |  |


<a id="conversationsIDGet"></a>
# **conversationsIDGet**
> EndpointGetConversationsID conversationsIDGet(ID)



Fetch an array of conversations. You can only retrieve conversations with users who exist within the current access token&#39;s bubble.

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
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointGetConversationsID result = apiInstance.conversationsIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsIDGet");
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
| **ID** | [**List&lt;Integer&gt;**](Integer.md)|  | |

### Return type

[**EndpointGetConversationsID**](EndpointGetConversationsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="conversationsIDMessagesGet"></a>
# **conversationsIDMessagesGet**
> EndpointGetConversationsIDMessages conversationsIDMessagesGet(ID, gtMessageId, excludeSelf, date, bubbled, recordSeen, timeout, offset, limit)



Retrieve the last {limit} messages in the conversation, provided the conversations exist within the current access token&#39;s bubble. If a timeout is 0 or greater, the batch is sorted oldest first. Otherwise, if timeout is a negative number, the transcript is paginated and sorted newest first. Specify a timeout for long polling (which delays the server sending back results for up to n seconds or until results are available, whichever comes first), or default to 0 for immediate results. Optionally record your status as online along with sharing the latest message you&#39;ve seen with the other conversation participant. Optionally specify a gt_message_id to retrieve only messages with an ID greater than that specified (such as greater than the latest message ID received in the last poll). Optionally only poll for messages authored by the other person in the conversation, and echo messages authored by you when sending, for a perceived increase in performance. Optionally only retrieve messages that were posted from within the current access token&#39;s bubble. Optionally specify a date formatted as YYYY-MM-DD to retrieve a transcript of messages from a single day. When record_seen is set to true, the new message count for the conversation is reset to zero.

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
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    Integer ID = 56; // Integer | 
    Integer gtMessageId = 56; // Integer | 
    Boolean excludeSelf = false; // Boolean | 
    String date = "date_example"; // String | 
    Boolean bubbled = false; // Boolean | 
    Boolean recordSeen = false; // Boolean | 
    Integer timeout = 0; // Integer | 
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetConversationsIDMessages result = apiInstance.conversationsIDMessagesGet(ID, gtMessageId, excludeSelf, date, bubbled, recordSeen, timeout, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsIDMessagesGet");
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
| **ID** | **Integer**|  | |
| **gtMessageId** | **Integer**|  | [optional] |
| **excludeSelf** | **Boolean**|  | [optional] [default to false] |
| **date** | **String**|  | [optional] |
| **bubbled** | **Boolean**|  | [optional] [default to false] |
| **recordSeen** | **Boolean**|  | [optional] [default to false] |
| **timeout** | **Integer**|  | [optional] [default to 0] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetConversationsIDMessages**](EndpointGetConversationsIDMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="conversationsIDMessagesPost"></a>
# **conversationsIDMessagesPost**
> EndpointPostConversationsIDMessages conversationsIDMessagesPost(ID, textRaw, bubbled, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values, textEmoticons)



Post a message to a conversation that is with a user who exists within the current access token&#39;s bubble. Optionally specify whether emoticons should be parsed into smiley images. Optionally specify whether the message should be bubbled within the app. Additionally, optionally attach a single metadata key/value pair to the message upon submission.

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
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    Integer ID = 56; // Integer | 
    String textRaw = "textRaw_example"; // String | 
    Boolean bubbled = false; // Boolean | 
    String metadata0Key = "metadata0Key_example"; // String | 
    String metadata0Privacy = "Public"; // String | 
    List<String> metadata0Values = Arrays.asList(); // List<String> | 
    String metadata1Key = "metadata1Key_example"; // String | 
    String metadata1Privacy = "Public"; // String | 
    List<String> metadata1Values = Arrays.asList(); // List<String> | 
    String metadata2Key = "metadata2Key_example"; // String | 
    String metadata2Privacy = "Public"; // String | 
    List<String> metadata2Values = Arrays.asList(); // List<String> | 
    Boolean textEmoticons = false; // Boolean | 
    try {
      EndpointPostConversationsIDMessages result = apiInstance.conversationsIDMessagesPost(ID, textRaw, bubbled, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values, textEmoticons);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsIDMessagesPost");
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
| **ID** | **Integer**|  | |
| **textRaw** | **String**|  | |
| **bubbled** | **Boolean**|  | [optional] [default to false] |
| **metadata0Key** | **String**|  | [optional] |
| **metadata0Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata0Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata1Key** | **String**|  | [optional] |
| **metadata1Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata1Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata2Key** | **String**|  | [optional] |
| **metadata2Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata2Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **textEmoticons** | **Boolean**|  | [optional] [default to false] |

### Return type

[**EndpointPostConversationsIDMessages**](EndpointPostConversationsIDMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="conversationsIDSchedulesPost"></a>
# **conversationsIDSchedulesPost**
> EndpointPostConversationsIDSchedules conversationsIDSchedulesPost(ID, date, limit, offset, rollUp, sort)



Paginated report of information about messages contributed by conversation and date. Only conversations that exist within the current access token&#39;s bubble are considered in the calculations. Optionally roll up all conversations to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages within the conversation(s).

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
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    String date = "date_example"; // String | 
    Integer limit = 50; // Integer | 
    Integer offset = 0; // Integer | 
    Boolean rollUp = false; // Boolean | 
    String sort = "asc"; // String | 
    try {
      EndpointPostConversationsIDSchedules result = apiInstance.conversationsIDSchedulesPost(ID, date, limit, offset, rollUp, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsIDSchedulesPost");
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
| **ID** | [**List&lt;Integer&gt;**](Integer.md)|  | |
| **date** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **rollUp** | **Boolean**|  | [optional] [default to false] |
| **sort** | **String**|  | [optional] [default to desc] [enum: asc, desc] |

### Return type

[**EndpointPostConversationsIDSchedules**](EndpointPostConversationsIDSchedules.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="conversationsIDSearchesPost"></a>
# **conversationsIDSearchesPost**
> EndpointPostConversationsIDSearches conversationsIDSearchesPost(ID, query, date, gtMessageId, limit, offset)



Fetch messages authored from within specified conversations that match a query string passed in as a search parameter along with their relevancy score.

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
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    String query = "query_example"; // String | 
    String date = "date_example"; // String | 
    Integer gtMessageId = 56; // Integer | 
    Integer limit = 50; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      EndpointPostConversationsIDSearches result = apiInstance.conversationsIDSearchesPost(ID, query, date, gtMessageId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsIDSearchesPost");
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
| **ID** | [**List&lt;Integer&gt;**](Integer.md)|  | |
| **query** | **String**|  | |
| **date** | **String**|  | [optional] |
| **gtMessageId** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**EndpointPostConversationsIDSearches**](EndpointPostConversationsIDSearches.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="conversationsIDStatusesGet"></a>
# **conversationsIDStatusesGet**
> EndpointGetConversationsIDStatuses conversationsIDStatusesGet(ID)



Status information about your current relationship with one or more conversations you participating in, provided the conversations exist within the current access token&#39;s bubble.

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
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointGetConversationsIDStatuses result = apiInstance.conversationsIDStatusesGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsIDStatusesGet");
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
| **ID** | [**List&lt;Integer&gt;**](Integer.md)|  | |

### Return type

[**EndpointGetConversationsIDStatuses**](EndpointGetConversationsIDStatuses.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="conversationsIDStatusesPatch"></a>
# **conversationsIDStatusesPatch**
> EndpointPatchConversationsIDStatuses conversationsIDStatusesPatch(ID, archivedStatus)



Archive or unarchive a conversation that is with a user who exists within the same bubble.

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
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    Integer ID = 56; // Integer | 
    Boolean archivedStatus = true; // Boolean | 
    try {
      EndpointPatchConversationsIDStatuses result = apiInstance.conversationsIDStatusesPatch(ID, archivedStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsIDStatusesPatch");
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
| **ID** | **Integer**|  | |
| **archivedStatus** | **Boolean**|  | |

### Return type

[**EndpointPatchConversationsIDStatuses**](EndpointPatchConversationsIDStatuses.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="conversationsSchedulesPost"></a>
# **conversationsSchedulesPost**
> EndpointPostConversationsSchedules conversationsSchedulesPost(date, limit, offset, rollUp, sort)



Paginated report of information about messages contributed by conversation and date. Only conversations that exist within the current access token&#39;s bubble are considered in the calculations. Optionally roll up all conversations to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages.

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
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String date = "date_example"; // String | 
    Integer limit = 50; // Integer | 
    Integer offset = 0; // Integer | 
    Boolean rollUp = false; // Boolean | 
    String sort = "asc"; // String | 
    try {
      EndpointPostConversationsSchedules result = apiInstance.conversationsSchedulesPost(date, limit, offset, rollUp, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsSchedulesPost");
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
| **date** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **rollUp** | **Boolean**|  | [optional] [default to false] |
| **sort** | **String**|  | [optional] [default to desc] [enum: asc, desc] |

### Return type

[**EndpointPostConversationsSchedules**](EndpointPostConversationsSchedules.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="conversationsSearchesPost"></a>
# **conversationsSearchesPost**
> EndpointPostConversationsSearches conversationsSearchesPost(query, date, gtMessageId, limit, offset)



Fetch messages authored from within the current bubble that match a query string passed in as a search parameter along with their relevancy score.

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
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String query = "query_example"; // String | 
    String date = "date_example"; // String | 
    Integer gtMessageId = 56; // Integer | 
    Integer limit = 50; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      EndpointPostConversationsSearches result = apiInstance.conversationsSearchesPost(query, date, gtMessageId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsSearchesPost");
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
| **query** | **String**|  | |
| **date** | **String**|  | [optional] |
| **gtMessageId** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**EndpointPostConversationsSearches**](EndpointPostConversationsSearches.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="conversationsStatusesGet"></a>
# **conversationsStatusesGet**
> EndpointGetConversationsStatuses conversationsStatusesGet(filter, includeArchived, bubbled, offset, limit)



Retrieve conversations that you are participating in with users who exists within the same bubble, along with your current relationship with the conversations. The user_a / user_b properties of the conversation are populated with as much data as is available if the user is not you. If the user is you, only the id field is populated. There is a separate status endpoint to retrieve relationship information for individual conversations. Optionally filter: &#39;new&#39; to only show conversations with messages you haven&#39;t yet seen; &#39;introductions&#39; to only show conversations where users have introduced themselves to you but nothing more; &#39;unreplied&#39; to only show conversations where you have introduced yourself to other users but nothing more; &#39;notifications&#39; to show all conversations where the other user was the last person to message. Optionally only show conversations engaging within the existing access token&#39;s bubble. This report is limited to your ~500-1000 most recently active conversations you&#39;ve engaged in within current the access token&#39;s bubble.

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
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String filter = "new"; // String | 
    Boolean includeArchived = false; // Boolean | 
    Boolean bubbled = false; // Boolean | 
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetConversationsStatuses result = apiInstance.conversationsStatusesGet(filter, includeArchived, bubbled, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsStatusesGet");
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
| **filter** | **String**|  | [optional] [enum: new, introductions, unreplied, notifications] |
| **includeArchived** | **Boolean**|  | [optional] [default to false] |
| **bubbled** | **Boolean**|  | [optional] [default to false] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetConversationsStatuses**](EndpointGetConversationsStatuses.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |


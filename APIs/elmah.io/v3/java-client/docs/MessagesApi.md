# MessagesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**messagesCreate**](MessagesApi.md#messagesCreate) | **POST** /v3/messages/{logId} | Create a new message. |
| [**messagesCreateBulk**](MessagesApi.md#messagesCreateBulk) | **POST** /v3/messages/{logId}/_bulk | Create one or more new messages. |
| [**messagesDelete**](MessagesApi.md#messagesDelete) | **DELETE** /v3/messages/{logId}/{id} | Delete a message by its ID. |
| [**messagesDeleteAll**](MessagesApi.md#messagesDeleteAll) | **DELETE** /v3/messages/{logId} | Deletes a list of messages by logid and query. |
| [**messagesFix**](MessagesApi.md#messagesFix) | **POST** /v3/messages/{logId}/{id}/_fix | Fix a message by its ID. |
| [**messagesFixAll**](MessagesApi.md#messagesFixAll) | **POST** /v3/messages/{logId}/_fix | Mark a list of messages as fixed by logid and query. |
| [**messagesGet**](MessagesApi.md#messagesGet) | **GET** /v3/messages/{logId}/{id} | Fetch a message by its ID. |
| [**messagesGetAll**](MessagesApi.md#messagesGetAll) | **GET** /v3/messages/{logId} | Fetch messages from a log. |
| [**messagesHide**](MessagesApi.md#messagesHide) | **POST** /v3/messages/{logId}/{id}/_hide | Hide a message by its ID. |


<a id="messagesCreate"></a>
# **messagesCreate**
> CreateMessageResult messagesCreate(logId, createMessage)

Create a new message.

Required permission: &#x60;messages_write&#x60;

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String logId = "logId_example"; // String | The ID of the log which should contain the new message.
    CreateMessage createMessage = new CreateMessage(); // CreateMessage | The message object to create.
    try {
      CreateMessageResult result = apiInstance.messagesCreate(logId, createMessage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesCreate");
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
| **logId** | **String**| The ID of the log which should contain the new message. | |
| **createMessage** | [**CreateMessage**](CreateMessage.md)| The message object to create. | [optional] |

### Return type

[**CreateMessageResult**](CreateMessageResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message was not created. |  -  |
| **201** | Message was successfully created. |  -  |
| **400** | Something wrong with the query parameters. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Log not found. |  -  |
| **413** | Message too large. Messages must not exceed 256 kb. As additional information, some fields are trimmed down when processed on the backend. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="messagesCreateBulk"></a>
# **messagesCreateBulk**
> List&lt;CreateBulkMessageResult&gt; messagesCreateBulk(logId, createMessage)

Create one or more new messages.

Required permission: &#x60;messages_write&#x60;

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String logId = "logId_example"; // String | The ID of the log which should contain the new messages.
    List<CreateMessage> createMessage = Arrays.asList(); // List<CreateMessage> | The messages to create.
    try {
      List<CreateBulkMessageResult> result = apiInstance.messagesCreateBulk(logId, createMessage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesCreateBulk");
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
| **logId** | **String**| The ID of the log which should contain the new messages. | |
| **createMessage** | [**List&lt;CreateMessage&gt;**](CreateMessage.md)| The messages to create. | [optional] |

### Return type

[**List&lt;CreateBulkMessageResult&gt;**](CreateBulkMessageResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Zero or more messages where successfully created. Check the response body for details. |  -  |
| **400** | Something wrong with the query parameters. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Log not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="messagesDelete"></a>
# **messagesDelete**
> messagesDelete(id, logId)

Delete a message by its ID.

Required permission: &#x60;messages_delete&#x60;

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String id = "id_example"; // String | The ID of the message to delete.
    String logId = "logId_example"; // String | The ID of the log containing the message.
    try {
      apiInstance.messagesDelete(id, logId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesDelete");
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
| **id** | **String**| The ID of the message to delete. | |
| **logId** | **String**| The ID of the log containing the message. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message where deleted. |  -  |
| **400** | Something wrong with the query parameters. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Log or message not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="messagesDeleteAll"></a>
# **messagesDeleteAll**
> messagesDeleteAll(logId, search)

Deletes a list of messages by logid and query.

Required permission: &#x60;messages_delete&#x60;

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String logId = "logId_example"; // String | The ID of the log containing the message.
    Search search = new Search(); // Search | A search object containing query, time filters etc.
    try {
      apiInstance.messagesDeleteAll(logId, search);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesDeleteAll");
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
| **logId** | **String**| The ID of the log containing the message. | |
| **search** | [**Search**](Search.md)| A search object containing query, time filters etc. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Messages where deleted. |  -  |
| **400** | Something wrong with the query parameters. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Log not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="messagesFix"></a>
# **messagesFix**
> messagesFix(id, logId, markAllAsFixed)

Fix a message by its ID.

Required permission: &#x60;messages_write&#x60;

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String id = "id_example"; // String | The ID of the message to fix.
    String logId = "logId_example"; // String | The ID of the log containing the message.
    Boolean markAllAsFixed = false; // Boolean | If set to true, all instances of the log message are set to fixed.
    try {
      apiInstance.messagesFix(id, logId, markAllAsFixed);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesFix");
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
| **id** | **String**| The ID of the message to fix. | |
| **logId** | **String**| The ID of the log containing the message. | |
| **markAllAsFixed** | **Boolean**| If set to true, all instances of the log message are set to fixed. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message was fixed. |  -  |
| **400** | Something wrong with the query parameters. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Message not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="messagesFixAll"></a>
# **messagesFixAll**
> messagesFixAll(logId, search)

Mark a list of messages as fixed by logid and query.

Required permission: &#x60;messages_write&#x60;

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String logId = "logId_example"; // String | The ID of the log containing the messages.
    Search search = new Search(); // Search | A search object containing query, time filters etc.
    try {
      apiInstance.messagesFixAll(logId, search);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesFixAll");
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
| **logId** | **String**| The ID of the log containing the messages. | |
| **search** | [**Search**](Search.md)| A search object containing query, time filters etc. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Messages where marked as fixed. |  -  |
| **400** | Something wrong with the query parameters. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Log not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="messagesGet"></a>
# **messagesGet**
> Message messagesGet(id, logId)

Fetch a message by its ID.

Required permission: &#x60;messages_read&#x60;

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String id = "id_example"; // String | The ID of the message to fetch.
    String logId = "logId_example"; // String | The ID of the log containing the message.
    try {
      Message result = apiInstance.messagesGet(id, logId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesGet");
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
| **id** | **String**| The ID of the message to fetch. | |
| **logId** | **String**| The ID of the log containing the message. | |

### Return type

[**Message**](Message.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message found. |  -  |
| **400** | Something wrong with the query parameters. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Message not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="messagesGetAll"></a>
# **messagesGetAll**
> MessagesResult messagesGetAll(logId, pageIndex, pageSize, query, from, to, includeHeaders)

Fetch messages from a log.

Required permission: &#x60;messages_read&#x60;

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String logId = "logId_example"; // String | The ID of the log containing the messages.
    Integer pageIndex = 0; // Integer | The page number of the result.
    Integer pageSize = 15; // Integer | The number of messages to load (max 100) or 15 if not set.
    String query = "query_example"; // String | A full-text or Lucene query to limit the messages by.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | A start date and time to search from (not included).
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | An end date and time to search to (not included).
    Boolean includeHeaders = false; // Boolean | Include headers like server variables and cookies in the result (slower).
    try {
      MessagesResult result = apiInstance.messagesGetAll(logId, pageIndex, pageSize, query, from, to, includeHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesGetAll");
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
| **logId** | **String**| The ID of the log containing the messages. | |
| **pageIndex** | **Integer**| The page number of the result. | [optional] [default to 0] |
| **pageSize** | **Integer**| The number of messages to load (max 100) or 15 if not set. | [optional] [default to 15] |
| **query** | **String**| A full-text or Lucene query to limit the messages by. | [optional] |
| **from** | **OffsetDateTime**| A start date and time to search from (not included). | [optional] |
| **to** | **OffsetDateTime**| An end date and time to search to (not included). | [optional] |
| **includeHeaders** | **Boolean**| Include headers like server variables and cookies in the result (slower). | [optional] [default to false] |

### Return type

[**MessagesResult**](MessagesResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Log found and may contain messages. |  -  |
| **400** | Something wrong with the query parameters. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="messagesHide"></a>
# **messagesHide**
> messagesHide(id, logId)

Hide a message by its ID.

Required permission: &#x60;messages_write&#x60;

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String id = "id_example"; // String | The ID of the message to hide.
    String logId = "logId_example"; // String | The ID of the log containing the message.
    try {
      apiInstance.messagesHide(id, logId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesHide");
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
| **id** | **String**| The ID of the message to hide. | |
| **logId** | **String**| The ID of the log containing the message. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message was hidden. |  -  |
| **400** | Something wrong with the query parameters. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the logs API but the trial expired. |  -  |
| **404** | Message not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |


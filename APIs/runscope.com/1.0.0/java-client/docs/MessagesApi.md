# MessagesApi

All URIs are relative to *https://api.runscope.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bucketsBucketKeyErrorsGet**](MessagesApi.md#bucketsBucketKeyErrorsGet) | **GET** /buckets/{bucketKey}/errors | Retrieve a list of error messages in a bucket |
| [**bucketsBucketKeyMessagesDelete**](MessagesApi.md#bucketsBucketKeyMessagesDelete) | **DELETE** /buckets/{bucketKey}/messages | Clear a bucket (remove all messages). |
| [**bucketsBucketKeyMessagesGet**](MessagesApi.md#bucketsBucketKeyMessagesGet) | **GET** /buckets/{bucketKey}/messages | Retrieve a list of messages in a bucket |
| [**bucketsBucketKeyMessagesMessageIdGet**](MessagesApi.md#bucketsBucketKeyMessagesMessageIdGet) | **GET** /buckets/{bucketKey}/messages/{messageId} | Retrieve the details for a single message. |
| [**bucketsBucketKeyMessagesPost**](MessagesApi.md#bucketsBucketKeyMessagesPost) | **POST** /buckets/{bucketKey}/messages | Create a message |


<a id="bucketsBucketKeyErrorsGet"></a>
# **bucketsBucketKeyErrorsGet**
> bucketsBucketKeyErrorsGet(bucketKey, count, since, before)

Retrieve a list of error messages in a bucket

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
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    Integer count = 56; // Integer | Maxiumum number of messages to return. Default 50, max 1000.
    Integer since = 56; // Integer | Only return messages after the given Unix timestamp
    Integer before = 56; // Integer | Only return messages before the given Unix timestamp
    try {
      apiInstance.bucketsBucketKeyErrorsGet(bucketKey, count, since, before);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#bucketsBucketKeyErrorsGet");
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
| **bucketKey** | **String**| Unique identifier for a bucket | |
| **count** | **Integer**| Maxiumum number of messages to return. Default 50, max 1000. | [optional] |
| **since** | **Integer**| Only return messages after the given Unix timestamp | [optional] |
| **before** | **Integer**| Only return messages before the given Unix timestamp | [optional] |

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of error messages in a bucket |  -  |
| **0** | Unexpected error |  -  |

<a id="bucketsBucketKeyMessagesDelete"></a>
# **bucketsBucketKeyMessagesDelete**
> bucketsBucketKeyMessagesDelete(bucketKey)

Clear a bucket (remove all messages).

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
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    try {
      apiInstance.bucketsBucketKeyMessagesDelete(bucketKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#bucketsBucketKeyMessagesDelete");
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
| **bucketKey** | **String**| Unique identifier for a bucket | |

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content with no body. |  -  |
| **0** | Unexpected error |  -  |

<a id="bucketsBucketKeyMessagesGet"></a>
# **bucketsBucketKeyMessagesGet**
> bucketsBucketKeyMessagesGet(bucketKey, count, since, before)

Retrieve a list of messages in a bucket

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
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    Integer count = 56; // Integer | Maxiumum number of messages to return. Default 50, max 1000.
    Integer since = 56; // Integer | Only return messages after the given Unix timestamp
    Integer before = 56; // Integer | Only return messages before the given Unix timestamp
    try {
      apiInstance.bucketsBucketKeyMessagesGet(bucketKey, count, since, before);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#bucketsBucketKeyMessagesGet");
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
| **bucketKey** | **String**| Unique identifier for a bucket | |
| **count** | **Integer**| Maxiumum number of messages to return. Default 50, max 1000. | [optional] |
| **since** | **Integer**| Only return messages after the given Unix timestamp | [optional] |
| **before** | **Integer**| Only return messages before the given Unix timestamp | [optional] |

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of messages in a bucket |  -  |
| **0** | Unexpected error |  -  |

<a id="bucketsBucketKeyMessagesMessageIdGet"></a>
# **bucketsBucketKeyMessagesMessageIdGet**
> bucketsBucketKeyMessagesMessageIdGet(bucketKey, messageId)

Retrieve the details for a single message.

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
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String messageId = "messageId_example"; // String | The unique identifier for this message
    try {
      apiInstance.bucketsBucketKeyMessagesMessageIdGet(bucketKey, messageId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#bucketsBucketKeyMessagesMessageIdGet");
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
| **bucketKey** | **String**| Unique identifier for a bucket | |
| **messageId** | **String**| The unique identifier for this message | |

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of messages in a bucket |  -  |
| **0** | Unexpected error |  -  |

<a id="bucketsBucketKeyMessagesPost"></a>
# **bucketsBucketKeyMessagesPost**
> BucketsBucketKeyMessagesPost200Response bucketsBucketKeyMessagesPost(bucketKey, newMessage)

Create a message

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
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    NewMessage newMessage = new NewMessage(); // NewMessage | 
    try {
      BucketsBucketKeyMessagesPost200Response result = apiInstance.bucketsBucketKeyMessagesPost(bucketKey, newMessage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#bucketsBucketKeyMessagesPost");
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
| **bucketKey** | **String**| Unique identifier for a bucket | |
| **newMessage** | [**NewMessage**](NewMessage.md)|  | |

### Return type

[**BucketsBucketKeyMessagesPost200Response**](BucketsBucketKeyMessagesPost200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response includes a list of result objects for the message(s) submitted. It will always return an array, even if only one message was created. The order of the result objects corresponds to the order of messages submitted. |  -  |
| **0** | Unexpected error |  -  |


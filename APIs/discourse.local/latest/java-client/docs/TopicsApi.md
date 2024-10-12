# TopicsApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bookmarkTopic**](TopicsApi.md#bookmarkTopic) | **PUT** /t/{id}/bookmark.json | Bookmark topic |
| [**createTopicPostPM_0**](TopicsApi.md#createTopicPostPM_0) | **POST** /posts.json | Creates a new topic, a new post, or a private message |
| [**createTopicTimer**](TopicsApi.md#createTopicTimer) | **POST** /t/{id}/timer.json | Create topic timer |
| [**getSpecificPostsFromTopic**](TopicsApi.md#getSpecificPostsFromTopic) | **GET** /t/{id}/posts.json | Get specific posts from a topic |
| [**getTopic**](TopicsApi.md#getTopic) | **GET** /t/{id}.json | Get a single topic |
| [**getTopicByExternalId**](TopicsApi.md#getTopicByExternalId) | **GET** /t/external_id/{external_id}.json | Get topic by external_id |
| [**inviteToTopic**](TopicsApi.md#inviteToTopic) | **POST** /t/{id}/invite.json | Invite to topic |
| [**listLatestTopics**](TopicsApi.md#listLatestTopics) | **GET** /latest.json | Get the latest topics |
| [**listTopTopics**](TopicsApi.md#listTopTopics) | **GET** /top.json | Get the top topics filtered by period |
| [**removeTopic**](TopicsApi.md#removeTopic) | **DELETE** /t/{id}.json | Remove a topic |
| [**setNotificationLevel**](TopicsApi.md#setNotificationLevel) | **POST** /t/{id}/notifications.json | Set notification level |
| [**updateTopic**](TopicsApi.md#updateTopic) | **PUT** /t/-/{id}.json | Update a topic |
| [**updateTopicStatus**](TopicsApi.md#updateTopicStatus) | **PUT** /t/{id}/status.json | Update the status of a topic |
| [**updateTopicTimestamp**](TopicsApi.md#updateTopicTimestamp) | **PUT** /t/{id}/change-timestamp.json | Update topic timestamp |


<a id="bookmarkTopic"></a>
# **bookmarkTopic**
> bookmarkTopic(apiKey, apiUsername, id)

Bookmark topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.bookmarkTopic(apiKey, apiUsername, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#bookmarkTopic");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |

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
| **200** | topic updated |  -  |

<a id="createTopicPostPM_0"></a>
# **createTopicPostPM_0**
> CreateTopicPostPM200Response createTopicPostPM_0(createTopicPostPMRequest)

Creates a new topic, a new post, or a private message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    CreateTopicPostPMRequest createTopicPostPMRequest = new CreateTopicPostPMRequest(); // CreateTopicPostPMRequest | 
    try {
      CreateTopicPostPM200Response result = apiInstance.createTopicPostPM_0(createTopicPostPMRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#createTopicPostPM_0");
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
| **createTopicPostPMRequest** | [**CreateTopicPostPMRequest**](CreateTopicPostPMRequest.md)|  | [optional] |

### Return type

[**CreateTopicPostPM200Response**](CreateTopicPostPM200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | post created |  -  |

<a id="createTopicTimer"></a>
# **createTopicTimer**
> CreateTopicTimer200Response createTopicTimer(apiKey, apiUsername, id, createTopicTimerRequest)

Create topic timer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    CreateTopicTimerRequest createTopicTimerRequest = new CreateTopicTimerRequest(); // CreateTopicTimerRequest | 
    try {
      CreateTopicTimer200Response result = apiInstance.createTopicTimer(apiKey, apiUsername, id, createTopicTimerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#createTopicTimer");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |
| **createTopicTimerRequest** | [**CreateTopicTimerRequest**](CreateTopicTimerRequest.md)|  | [optional] |

### Return type

[**CreateTopicTimer200Response**](CreateTopicTimer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | topic updated |  -  |

<a id="getSpecificPostsFromTopic"></a>
# **getSpecificPostsFromTopic**
> GetSpecificPostsFromTopic200Response getSpecificPostsFromTopic(apiKey, apiUsername, id, getSpecificPostsFromTopicRequest)

Get specific posts from a topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    GetSpecificPostsFromTopicRequest getSpecificPostsFromTopicRequest = new GetSpecificPostsFromTopicRequest(); // GetSpecificPostsFromTopicRequest | 
    try {
      GetSpecificPostsFromTopic200Response result = apiInstance.getSpecificPostsFromTopic(apiKey, apiUsername, id, getSpecificPostsFromTopicRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#getSpecificPostsFromTopic");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |
| **getSpecificPostsFromTopicRequest** | [**GetSpecificPostsFromTopicRequest**](GetSpecificPostsFromTopicRequest.md)|  | [optional] |

### Return type

[**GetSpecificPostsFromTopic200Response**](GetSpecificPostsFromTopic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | specific posts |  -  |

<a id="getTopic"></a>
# **getTopic**
> GetTopic200Response getTopic(apiKey, apiUsername, id)

Get a single topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    try {
      GetTopic200Response result = apiInstance.getTopic(apiKey, apiUsername, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#getTopic");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |

### Return type

[**GetTopic200Response**](GetTopic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | specific posts |  -  |

<a id="getTopicByExternalId"></a>
# **getTopicByExternalId**
> getTopicByExternalId(externalId)

Get topic by external_id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String externalId = "externalId_example"; // String | 
    try {
      apiInstance.getTopicByExternalId(externalId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#getTopicByExternalId");
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
| **externalId** | **String**|  | |

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
| **301** | redirects to /t/{topic_id}.json |  -  |

<a id="inviteToTopic"></a>
# **inviteToTopic**
> InviteToTopic200Response inviteToTopic(apiKey, apiUsername, id, inviteToTopicRequest)

Invite to topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    InviteToTopicRequest inviteToTopicRequest = new InviteToTopicRequest(); // InviteToTopicRequest | 
    try {
      InviteToTopic200Response result = apiInstance.inviteToTopic(apiKey, apiUsername, id, inviteToTopicRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#inviteToTopic");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |
| **inviteToTopicRequest** | [**InviteToTopicRequest**](InviteToTopicRequest.md)|  | [optional] |

### Return type

[**InviteToTopic200Response**](InviteToTopic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | topic updated |  -  |

<a id="listLatestTopics"></a>
# **listLatestTopics**
> ListLatestTopics200Response listLatestTopics(apiKey, apiUsername, order, ascending)

Get the latest topics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String order = "order_example"; // String | Enum: `default`, `created`, `activity`, `views`, `posts`, `category`, `likes`, `op_likes`, `posters`
    String ascending = "ascending_example"; // String | Defaults to `desc`, add `ascending=true` to sort asc
    try {
      ListLatestTopics200Response result = apiInstance.listLatestTopics(apiKey, apiUsername, order, ascending);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#listLatestTopics");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **order** | **String**| Enum: &#x60;default&#x60;, &#x60;created&#x60;, &#x60;activity&#x60;, &#x60;views&#x60;, &#x60;posts&#x60;, &#x60;category&#x60;, &#x60;likes&#x60;, &#x60;op_likes&#x60;, &#x60;posters&#x60; | [optional] |
| **ascending** | **String**| Defaults to &#x60;desc&#x60;, add &#x60;ascending&#x3D;true&#x60; to sort asc | [optional] |

### Return type

[**ListLatestTopics200Response**](ListLatestTopics200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | topic updated |  -  |

<a id="listTopTopics"></a>
# **listTopTopics**
> ListTopTopics200Response listTopTopics(apiKey, apiUsername, period)

Get the top topics filtered by period

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String period = "period_example"; // String | Enum: `all`, `yearly`, `quarterly`, `monthly`, `weekly`, `daily`
    try {
      ListTopTopics200Response result = apiInstance.listTopTopics(apiKey, apiUsername, period);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#listTopTopics");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **period** | **String**| Enum: &#x60;all&#x60;, &#x60;yearly&#x60;, &#x60;quarterly&#x60;, &#x60;monthly&#x60;, &#x60;weekly&#x60;, &#x60;daily&#x60; | [optional] |

### Return type

[**ListTopTopics200Response**](ListTopTopics200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="removeTopic"></a>
# **removeTopic**
> removeTopic(apiKey, apiUsername, id)

Remove a topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.removeTopic(apiKey, apiUsername, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#removeTopic");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |

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
| **200** | specific posts |  -  |

<a id="setNotificationLevel"></a>
# **setNotificationLevel**
> UpdateGroup200Response setNotificationLevel(apiKey, apiUsername, id, setNotificationLevelRequest)

Set notification level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    SetNotificationLevelRequest setNotificationLevelRequest = new SetNotificationLevelRequest(); // SetNotificationLevelRequest | 
    try {
      UpdateGroup200Response result = apiInstance.setNotificationLevel(apiKey, apiUsername, id, setNotificationLevelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#setNotificationLevel");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |
| **setNotificationLevelRequest** | [**SetNotificationLevelRequest**](SetNotificationLevelRequest.md)|  | [optional] |

### Return type

[**UpdateGroup200Response**](UpdateGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | topic updated |  -  |

<a id="updateTopic"></a>
# **updateTopic**
> UpdateTopic200Response updateTopic(apiKey, apiUsername, id, updateTopicRequest)

Update a topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    UpdateTopicRequest updateTopicRequest = new UpdateTopicRequest(); // UpdateTopicRequest | 
    try {
      UpdateTopic200Response result = apiInstance.updateTopic(apiKey, apiUsername, id, updateTopicRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#updateTopic");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |
| **updateTopicRequest** | [**UpdateTopicRequest**](UpdateTopicRequest.md)|  | [optional] |

### Return type

[**UpdateTopic200Response**](UpdateTopic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | topic updated |  -  |

<a id="updateTopicStatus"></a>
# **updateTopicStatus**
> UpdateTopicStatus200Response updateTopicStatus(apiKey, apiUsername, id, updateTopicStatusRequest)

Update the status of a topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    UpdateTopicStatusRequest updateTopicStatusRequest = new UpdateTopicStatusRequest(); // UpdateTopicStatusRequest | 
    try {
      UpdateTopicStatus200Response result = apiInstance.updateTopicStatus(apiKey, apiUsername, id, updateTopicStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#updateTopicStatus");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |
| **updateTopicStatusRequest** | [**UpdateTopicStatusRequest**](UpdateTopicStatusRequest.md)|  | [optional] |

### Return type

[**UpdateTopicStatus200Response**](UpdateTopicStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | topic updated |  -  |

<a id="updateTopicTimestamp"></a>
# **updateTopicTimestamp**
> UpdateGroup200Response updateTopicTimestamp(apiKey, apiUsername, id, updateTopicTimestampRequest)

Update topic timestamp

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String apiUsername = "apiUsername_example"; // String | 
    String id = "id_example"; // String | 
    UpdateTopicTimestampRequest updateTopicTimestampRequest = new UpdateTopicTimestampRequest(); // UpdateTopicTimestampRequest | 
    try {
      UpdateGroup200Response result = apiInstance.updateTopicTimestamp(apiKey, apiUsername, id, updateTopicTimestampRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#updateTopicTimestamp");
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
| **apiKey** | **String**|  | |
| **apiUsername** | **String**|  | |
| **id** | **String**|  | |
| **updateTopicTimestampRequest** | [**UpdateTopicTimestampRequest**](UpdateTopicTimestampRequest.md)|  | [optional] |

### Return type

[**UpdateGroup200Response**](UpdateGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | topic updated |  -  |


# QueuesApi

All URIs are relative to *https://apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ackMessage**](QueuesApi.md#ackMessage) | **DELETE** /queues/{queueName}/messages/{queueMessageId} | Acknowledge that Queue Message has been processed. |
| [**createQueue**](QueuesApi.md#createQueue) | **POST** /queues | Create new queue. |
| [**deleteQueue**](QueuesApi.md#deleteQueue) | **DELETE** /queues/{queueName} | Delete Queue. |
| [**getListOfQueues**](QueuesApi.md#getListOfQueues) | **GET** /queues | Get list of all Queues. |
| [**getMessageData**](QueuesApi.md#getMessageData) | **GET** /queues/{queueName}/data/{queueMessageId} | Get data associated with a Queue Message. |
| [**getNextMessages**](QueuesApi.md#getNextMessages) | **GET** /queues/{queueName}/messages | Get next Queue Messages from a Queue |
| [**getQueueConfig**](QueuesApi.md#getQueueConfig) | **GET** /queues/{queueName}/config | Get Queue config. |
| [**sendMessageBinary**](QueuesApi.md#sendMessageBinary) | **POST** /queues/{queueName}/messages | Send Queue Message with a binary data (blob) payload. |
| [**updateQueueConfig**](QueuesApi.md#updateQueueConfig) | **PUT** /queues/{queueName}/config | Update Queue configuration. |


<a id="ackMessage"></a>
# **ackMessage**
> ModelApiResponse ackMessage(queueName, queueMessageId)

Acknowledge that Queue Message has been processed.



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apache.local");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String queueName = "queueName_example"; // String | Name of Queue
    String queueMessageId = "queueMessageId_example"; // String | ID of Queue Message to be acknowledged
    try {
      ModelApiResponse result = apiInstance.ackMessage(queueName, queueMessageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#ackMessage");
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
| **queueName** | **String**| Name of Queue | |
| **queueMessageId** | **String**| ID of Queue Message to be acknowledged | |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Queue Message ID invalid, or message not in-flight |  -  |

<a id="createQueue"></a>
# **createQueue**
> ModelApiResponse createQueue()

Create new queue.



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apache.local");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    try {
      ModelApiResponse result = apiInstance.createQueue();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#createQueue");
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

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | No Queue object posted, or name field is missing |  -  |

<a id="deleteQueue"></a>
# **deleteQueue**
> ModelApiResponse deleteQueue(queueName, confirm)

Delete Queue.



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apache.local");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String queueName = "queueName_example"; // String | 
    Boolean confirm = false; // Boolean | 
    try {
      ModelApiResponse result = apiInstance.deleteQueue(queueName, confirm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#deleteQueue");
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
| **queueName** | **String**|  | |
| **confirm** | **Boolean**|  | [optional] [default to false] |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Queue name or confirm flag missing. |  -  |

<a id="getListOfQueues"></a>
# **getListOfQueues**
> ModelApiResponse getListOfQueues()

Get list of all Queues.



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apache.local");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    try {
      ModelApiResponse result = apiInstance.getListOfQueues();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#getListOfQueues");
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

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getMessageData"></a>
# **getMessageData**
> ModelApiResponse getMessageData(queueName, queueMessageId)

Get data associated with a Queue Message.



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apache.local");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String queueName = "queueName_example"; // String | Name of Queue
    String queueMessageId = "queueMessageId_example"; // String | ID of Queue Message for which data is to be returned
    try {
      ModelApiResponse result = apiInstance.getMessageData(queueName, queueMessageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#getMessageData");
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
| **queueName** | **String**| Name of Queue | |
| **queueMessageId** | **String**| ID of Queue Message for which data is to be returned | |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Message ID invalid |  -  |
| **404** | Queue Message or data not found |  -  |

<a id="getNextMessages"></a>
# **getNextMessages**
> ModelApiResponse getNextMessages(queueName, count)

Get next Queue Messages from a Queue



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apache.local");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String queueName = "queueName_example"; // String | Name of Queue
    String count = "1"; // String | Number of messages to get
    try {
      ModelApiResponse result = apiInstance.getNextMessages(queueName, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#getNextMessages");
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
| **queueName** | **String**| Name of Queue | |
| **count** | **String**| Number of messages to get | [optional] [default to 1] |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid count parameter |  -  |

<a id="getQueueConfig"></a>
# **getQueueConfig**
> ModelApiResponse getQueueConfig(queueName)

Get Queue config.



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apache.local");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String queueName = "queueName_example"; // String | Name of Queue
    try {
      ModelApiResponse result = apiInstance.getQueueConfig(queueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#getQueueConfig");
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
| **queueName** | **String**| Name of Queue | |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Queue name or confirm flag missing. |  -  |

<a id="sendMessageBinary"></a>
# **sendMessageBinary**
> ModelApiResponse sendMessageBinary(queueName, contentType, requestBody, regions, delay, expiration)

Send Queue Message with a binary data (blob) payload.



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apache.local");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String queueName = "queueName_example"; // String | Name of Queue
    String contentType = "contentType_example"; // String | Content type of the data to be sent with Queue Message
    List<byte[]> requestBody = null; // List<byte[]> | Data to be send with Queue Message
    String regions = "regions_example"; // String | Regions to which message is to be sent
    String delay = "delay_example"; // String | 
    String expiration = "expiration_example"; // String | 
    try {
      ModelApiResponse result = apiInstance.sendMessageBinary(queueName, contentType, requestBody, regions, delay, expiration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#sendMessageBinary");
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
| **queueName** | **String**| Name of Queue | |
| **contentType** | **String**| Content type of the data to be sent with Queue Message | |
| **requestBody** | [**List&lt;byte[]&gt;**](byte[].md)| Data to be send with Queue Message | |
| **regions** | **String**| Regions to which message is to be sent | [optional] |
| **delay** | **String**|  | [optional] |
| **expiration** | **String**|  | [optional] |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="updateQueueConfig"></a>
# **updateQueueConfig**
> ModelApiResponse updateQueueConfig(queueName)

Update Queue configuration.



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apache.local");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String queueName = "queueName_example"; // String | 
    try {
      ModelApiResponse result = apiInstance.updateQueueConfig(queueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#updateQueueConfig");
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
| **queueName** | **String**|  | |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | No Queue object posted, or name field is missing |  -  |


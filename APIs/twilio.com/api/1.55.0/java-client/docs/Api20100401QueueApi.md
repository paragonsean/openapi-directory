# Api20100401QueueApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createQueue**](Api20100401QueueApi.md#createQueue) | **POST** /2010-04-01/Accounts/{AccountSid}/Queues.json |  |
| [**deleteQueue**](Api20100401QueueApi.md#deleteQueue) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json |  |
| [**fetchQueue**](Api20100401QueueApi.md#fetchQueue) | **GET** /2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json |  |
| [**listQueue**](Api20100401QueueApi.md#listQueue) | **GET** /2010-04-01/Accounts/{AccountSid}/Queues.json |  |
| [**updateQueue**](Api20100401QueueApi.md#updateQueue) | **POST** /2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json |  |


<a id="createQueue"></a>
# **createQueue**
> ApiV2010AccountQueue createQueue(accountSid, friendlyName, maxSize)



Create a queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401QueueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401QueueApi apiInstance = new Api20100401QueueApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you created to describe this resource. It can be up to 64 characters long.
    Integer maxSize = 56; // Integer | The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
    try {
      ApiV2010AccountQueue result = apiInstance.createQueue(accountSid, friendlyName, maxSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401QueueApi#createQueue");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | |
| **friendlyName** | **String**| A descriptive string that you created to describe this resource. It can be up to 64 characters long. | |
| **maxSize** | **Integer**| The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000. | [optional] |

### Return type

[**ApiV2010AccountQueue**](ApiV2010AccountQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteQueue"></a>
# **deleteQueue**
> deleteQueue(accountSid, sid)



Remove an empty queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401QueueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401QueueApi apiInstance = new Api20100401QueueApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Queue resource to delete
    try {
      apiInstance.deleteQueue(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401QueueApi#deleteQueue");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Queue resource to delete | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchQueue"></a>
# **fetchQueue**
> ApiV2010AccountQueue fetchQueue(accountSid, sid)



Fetch an instance of a queue identified by the QueueSid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401QueueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401QueueApi apiInstance = new Api20100401QueueApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Queue resource to fetch
    try {
      ApiV2010AccountQueue result = apiInstance.fetchQueue(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401QueueApi#fetchQueue");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Queue resource to fetch | |

### Return type

[**ApiV2010AccountQueue**](ApiV2010AccountQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listQueue"></a>
# **listQueue**
> ListQueueResponse listQueue(accountSid, pageSize, page, pageToken)



Retrieve a list of queues belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401QueueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401QueueApi apiInstance = new Api20100401QueueApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListQueueResponse result = apiInstance.listQueue(accountSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401QueueApi#listQueue");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListQueueResponse**](ListQueueResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateQueue"></a>
# **updateQueue**
> ApiV2010AccountQueue updateQueue(accountSid, sid, friendlyName, maxSize)



Update the queue with the new parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401QueueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401QueueApi apiInstance = new Api20100401QueueApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Queue resource to update
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you created to describe this resource. It can be up to 64 characters long.
    Integer maxSize = 56; // Integer | The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
    try {
      ApiV2010AccountQueue result = apiInstance.updateQueue(accountSid, sid, friendlyName, maxSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401QueueApi#updateQueue");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Queue resource to update | |
| **friendlyName** | **String**| A descriptive string that you created to describe this resource. It can be up to 64 characters long. | [optional] |
| **maxSize** | **Integer**| The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000. | [optional] |

### Return type

[**ApiV2010AccountQueue**](ApiV2010AccountQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


# ChannelsApi

All URIs are relative to *https://demo.pims.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAllChannels**](ChannelsApi.md#fetchAllChannels) | **GET** /channels | Find all channels |
| [**fetchAllEventsChannels**](ChannelsApi.md#fetchAllEventsChannels) | **GET** /events/{event_id}/channels | Find all channels for one event |
| [**fetchOneChannel**](ChannelsApi.md#fetchOneChannel) | **GET** /channels/{channel_id} | Get one channel by ID |
| [**fetchOneEventChannel**](ChannelsApi.md#fetchOneEventChannel) | **GET** /events/{event_id}/channels/{channel_id} | Get one event channel by ID |


<a id="fetchAllChannels"></a>
# **fetchAllChannels**
> List&lt;ChannelsEntity&gt; fetchAllChannels(label, showIgnored, sort, pageSize, acceptLanguage)

Find all channels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String label = "label_example"; // String | Find only the channels whose label contains this value.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the channels which are not ignored. If set to `true`, show all channels.
    String sort = "label"; // String | Sort the channels in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<ChannelsEntity> result = apiInstance.fetchAllChannels(label, showIgnored, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#fetchAllChannels");
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
| **label** | **String**| Find only the channels whose label contains this value. | [optional] |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the channels which are not ignored. If set to &#x60;true&#x60;, show all channels. | [optional] [default to false] |
| **sort** | **String**| Sort the channels in the corresponding order. | [optional] [default to label] [enum: label, -label, order, -order] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;ChannelsEntity&gt;**](ChannelsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of channels |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchAllEventsChannels"></a>
# **fetchAllEventsChannels**
> List&lt;EventsChannelsEntity&gt; fetchAllEventsChannels(eventId, showIgnored, pageSize)

Find all channels for one event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the [event-]channels which are not ignored. If set to `true`, show everything.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    try {
      List<EventsChannelsEntity> result = apiInstance.fetchAllEventsChannels(eventId, showIgnored, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#fetchAllEventsChannels");
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
| **eventId** | **Integer**| ID of the targeted event. | |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]channels which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |

### Return type

[**List&lt;EventsChannelsEntity&gt;**](EventsChannelsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of events channels |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOneChannel"></a>
# **fetchOneChannel**
> ChannelsEntity fetchOneChannel(channelId, acceptLanguage)

Get one channel by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    Integer channelId = 56; // Integer | ID of the targeted channel.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      ChannelsEntity result = apiInstance.fetchOneChannel(channelId, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#fetchOneChannel");
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
| **channelId** | **Integer**| ID of the targeted channel. | |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**ChannelsEntity**](ChannelsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one channel |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOneEventChannel"></a>
# **fetchOneEventChannel**
> EventsChannelsEntity fetchOneEventChannel(eventId, channelId)

Get one event channel by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    Integer channelId = 56; // Integer | ID of the targeted event channel.
    try {
      EventsChannelsEntity result = apiInstance.fetchOneEventChannel(eventId, channelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#fetchOneEventChannel");
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
| **eventId** | **Integer**| ID of the targeted event. | |
| **channelId** | **Integer**| ID of the targeted event channel. | |

### Return type

[**EventsChannelsEntity**](EventsChannelsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one event channel |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |


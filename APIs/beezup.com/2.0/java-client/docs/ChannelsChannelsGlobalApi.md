# ChannelsChannelsGlobalApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAvailableChannels**](ChannelsChannelsGlobalApi.md#getAvailableChannels) | **GET** /v2/user/channels/ | List all available channel for this store |
| [**getChannelCategories**](ChannelsChannelsGlobalApi.md#getChannelCategories) | **GET** /v2/user/channels/{channelId}/categories | Get channel categories |
| [**getChannelColumns**](ChannelsChannelsGlobalApi.md#getChannelColumns) | **POST** /v2/user/channels/{channelId}/columns | Get channel columns |
| [**getChannelInfo**](ChannelsChannelsGlobalApi.md#getChannelInfo) | **GET** /v2/user/channels/{channelId} | Get channel information |


<a id="getAvailableChannels"></a>
# **getAvailableChannels**
> List&lt;ChannelHeader&gt; getAvailableChannels(storeId)

List all available channel for this store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsChannelsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelsChannelsGlobalApi apiInstance = new ChannelsChannelsGlobalApi(defaultClient);
    String storeId = "04730364-9826-4ff3-92e4-51fccd02bf10"; // String | The store identifier
    try {
      List<ChannelHeader> result = apiInstance.getAvailableChannels(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsChannelsGlobalApi#getAvailableChannels");
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
| **storeId** | **String**| The store identifier | |

### Return type

[**List&lt;ChannelHeader&gt;**](ChannelHeader.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Available channel list for this store |  -  |

<a id="getChannelCategories"></a>
# **getChannelCategories**
> ChannelRootCategory getChannelCategories(channelId, acceptEncoding)

Get channel categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsChannelsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelsChannelsGlobalApi apiInstance = new ChannelsChannelsGlobalApi(defaultClient);
    String channelId = "2dc136a7-0d3d-4cc9-a825-a28a42c53e28"; // String | The channel identifier
    List<String> acceptEncoding = Arrays.asList(); // List<String> | Indicates that the client accepts that the response will be compressed to reduce traffic size.
    try {
      ChannelRootCategory result = apiInstance.getChannelCategories(channelId, acceptEncoding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsChannelsGlobalApi#getChannelCategories");
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
| **channelId** | **String**| The channel identifier | |
| **acceptEncoding** | [**List&lt;String&gt;**](String.md)| Indicates that the client accepts that the response will be compressed to reduce traffic size. | |

### Return type

[**ChannelRootCategory**](ChannelRootCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel categories |  * Content-Encoding - Indicates the compression use in the response <br>  |

<a id="getChannelColumns"></a>
# **getChannelColumns**
> List&lt;ChannelColumn&gt; getChannelColumns(channelId, acceptEncoding, requestBody)

Get channel columns

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsChannelsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelsChannelsGlobalApi apiInstance = new ChannelsChannelsGlobalApi(defaultClient);
    String channelId = "2dc136a7-0d3d-4cc9-a825-a28a42c53e28"; // String | The channel identifier
    List<String> acceptEncoding = Arrays.asList(); // List<String> | Indicates that the client accepts that the response will be compressed to reduce traffic size.
    List<String> requestBody = Arrays.asList(); // List<String> | Allow you to filter the channel column identifier list your want to get
    try {
      List<ChannelColumn> result = apiInstance.getChannelColumns(channelId, acceptEncoding, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsChannelsGlobalApi#getChannelColumns");
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
| **channelId** | **String**| The channel identifier | |
| **acceptEncoding** | [**List&lt;String&gt;**](String.md)| Indicates that the client accepts that the response will be compressed to reduce traffic size. | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| Allow you to filter the channel column identifier list your want to get | [optional] |

### Return type

[**List&lt;ChannelColumn&gt;**](ChannelColumn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel columns |  * Content-Encoding - Indicates the compression use in the response <br>  |

<a id="getChannelInfo"></a>
# **getChannelInfo**
> ChannelInfo getChannelInfo(channelId)

Get channel information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsChannelsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelsChannelsGlobalApi apiInstance = new ChannelsChannelsGlobalApi(defaultClient);
    String channelId = "2dc136a7-0d3d-4cc9-a825-a28a42c53e28"; // String | The channel identifier
    try {
      ChannelInfo result = apiInstance.getChannelInfo(channelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsChannelsGlobalApi#getChannelInfo");
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
| **channelId** | **String**| The channel identifier | |

### Return type

[**ChannelInfo**](ChannelInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel information |  -  |


# StatusApi

All URIs are relative to *https://rest.ably.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMetadataOfAllChannels**](StatusApi.md#getMetadataOfAllChannels) | **GET** /channels | Enumerate all active channels of the application |
| [**getMetadataOfChannel**](StatusApi.md#getMetadataOfChannel) | **GET** /channels/{channel_id} | Get metadata of a channel |
| [**getPresenceOfChannel**](StatusApi.md#getPresenceOfChannel) | **GET** /channels/{channel_id}/presence | Get presence of a channel |


<a id="getMetadataOfAllChannels"></a>
# **getMetadataOfAllChannels**
> GetMetadataOfAllChannels2XXResponse getMetadataOfAllChannels(xAblyVersion, format, limit, prefix, by)

Enumerate all active channels of the application

Enumerate all active channels of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    Integer limit = 100; // Integer | 
    String prefix = "prefix_example"; // String | Optionally limits the query to only those channels whose name starts with the given prefix
    String by = "value"; // String | optionally specifies whether to return just channel names (by=id) or ChannelDetails (by=value)
    try {
      GetMetadataOfAllChannels2XXResponse result = apiInstance.getMetadataOfAllChannels(xAblyVersion, format, limit, prefix, by);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getMetadataOfAllChannels");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **limit** | **Integer**|  | [optional] [default to 100] |
| **prefix** | **String**| Optionally limits the query to only those channels whose name starts with the given prefix | [optional] |
| **by** | **String**| optionally specifies whether to return just channel names (by&#x3D;id) or ChannelDetails (by&#x3D;value) | [optional] [enum: value, id] |

### Return type

[**GetMetadataOfAllChannels2XXResponse**](GetMetadataOfAllChannels2XXResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  * link -  <br>  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="getMetadataOfChannel"></a>
# **getMetadataOfChannel**
> ChannelDetails getMetadataOfChannel(channelId, xAblyVersion, format)

Get metadata of a channel

Get metadata of a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String channelId = "channelId_example"; // String | The [Channel's ID](https://www.ably.io/documentation/rest/channels).
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    try {
      ChannelDetails result = apiInstance.getMetadataOfChannel(channelId, xAblyVersion, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getMetadataOfChannel");
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
| **channelId** | **String**| The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels). | |
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |

### Return type

[**ChannelDetails**](ChannelDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * x-ably-serverid -  <br>  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="getPresenceOfChannel"></a>
# **getPresenceOfChannel**
> List&lt;PresenceMessage&gt; getPresenceOfChannel(channelId, xAblyVersion, format, clientId, connectionId, limit)

Get presence of a channel

Get presence on a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String channelId = "channelId_example"; // String | The [Channel's ID](https://www.ably.io/documentation/rest/channels).
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    String clientId = "clientId_example"; // String | 
    String connectionId = "connectionId_example"; // String | 
    Integer limit = 100; // Integer | 
    try {
      List<PresenceMessage> result = apiInstance.getPresenceOfChannel(channelId, xAblyVersion, format, clientId, connectionId, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getPresenceOfChannel");
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
| **channelId** | **String**| The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels). | |
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **clientId** | **String**|  | [optional] |
| **connectionId** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 100] |

### Return type

[**List&lt;PresenceMessage&gt;**](PresenceMessage.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * link -  <br>  * x-ably-serverid -  <br>  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |


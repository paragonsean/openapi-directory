# PublishingApi

All URIs are relative to *https://rest.ably.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publishMessagesToChannel**](PublishingApi.md#publishMessagesToChannel) | **POST** /channels/{channel_id}/messages | Publish a message to a channel |


<a id="publishMessagesToChannel"></a>
# **publishMessagesToChannel**
> PublishMessagesToChannel2XXResponse publishMessagesToChannel(channelId, xAblyVersion, format, message)

Publish a message to a channel

Publish a message to the specified channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishingApi;

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

    PublishingApi apiInstance = new PublishingApi(defaultClient);
    String channelId = "channelId_example"; // String | The [Channel's ID](https://www.ably.io/documentation/rest/channels).
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    Message message = new Message(); // Message | 
    try {
      PublishMessagesToChannel2XXResponse result = apiInstance.publishMessagesToChannel(channelId, xAblyVersion, format, message);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishingApi#publishMessagesToChannel");
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
| **message** | [**Message**](Message.md)|  | [optional] |

### Return type

[**PublishMessagesToChannel2XXResponse**](PublishMessagesToChannel2XXResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-msgpack, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  * x-ably-serverid -  <br>  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |


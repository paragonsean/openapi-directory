# PinsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pinsAdd**](PinsApi.md#pinsAdd) | **POST** /pins.add |  |
| [**pinsList**](PinsApi.md#pinsList) | **GET** /pins.list |  |
| [**pinsRemove**](PinsApi.md#pinsRemove) | **POST** /pins.remove |  |


<a id="pinsAdd"></a>
# **pinsAdd**
> PinsAddSchema pinsAdd(token, channel, timestamp)



Pins an item to a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PinsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    PinsApi apiInstance = new PinsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `pins:write`
    String channel = "channel_example"; // String | Channel to pin the item in.
    String timestamp = "timestamp_example"; // String | Timestamp of the message to pin.
    try {
      PinsAddSchema result = apiInstance.pinsAdd(token, channel, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PinsApi#pinsAdd");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;pins:write&#x60; | |
| **channel** | **String**| Channel to pin the item in. | |
| **timestamp** | **String**| Timestamp of the message to pin. | [optional] |

### Return type

[**PinsAddSchema**](PinsAddSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="pinsList"></a>
# **pinsList**
> List&lt;PinsListSuccessSchemaInner&gt; pinsList(token, channel)



Lists items pinned to a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PinsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    PinsApi apiInstance = new PinsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `pins:read`
    String channel = "channel_example"; // String | Channel to get pinned items for.
    try {
      List<PinsListSuccessSchemaInner> result = apiInstance.pinsList(token, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PinsApi#pinsList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;pins:read&#x60; | |
| **channel** | **String**| Channel to get pinned items for. | |

### Return type

[**List&lt;PinsListSuccessSchemaInner&gt;**](PinsListSuccessSchemaInner.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="pinsRemove"></a>
# **pinsRemove**
> PinsRemoveSchema pinsRemove(token, channel, timestamp)



Un-pins an item from a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PinsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    PinsApi apiInstance = new PinsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `pins:write`
    String channel = "channel_example"; // String | Channel where the item is pinned to.
    String timestamp = "timestamp_example"; // String | Timestamp of the message to un-pin.
    try {
      PinsRemoveSchema result = apiInstance.pinsRemove(token, channel, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PinsApi#pinsRemove");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;pins:write&#x60; | |
| **channel** | **String**| Channel where the item is pinned to. | |
| **timestamp** | **String**| Timestamp of the message to un-pin. | [optional] |

### Return type

[**PinsRemoveSchema**](PinsRemoveSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |


# ChannelsApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getChannels**](ChannelsApi.md#getChannels) | **GET** /channels | List all the channels. |
| [**getHighlightsByChannel**](ChannelsApi.md#getHighlightsByChannel) | **GET** /channels/{channel}/highlights | List the highlights for a channel. |
| [**getScheduleByChannel**](ChannelsApi.md#getScheduleByChannel) | **GET** /channels/{channel}/schedule/{date} | Get schedule by channel |


<a id="getChannels"></a>
# **getChannels**
> Object getChannels(lang, region)

List all the channels.

Get the list of all the channels TV &amp; iPlayer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String lang = "en"; // String | The language for any applicable localised strings.
    String region = "region_example"; // String | The region to get the channels for.
    try {
      Object result = apiInstance.getChannels(lang, region);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#getChannels");
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
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **region** | **String**| The region to get the channels for. | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getHighlightsByChannel"></a>
# **getHighlightsByChannel**
> Object getHighlightsByChannel(channel, lang, rights, availability, live, mixin)

List the highlights for a channel.

Get the editorial highlights of a given channel in TV &amp; iPlayer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String channel = "channel_example"; // String | The channel identifier to limit results to.
    String lang = "en"; // String | The language for any applicable localised strings.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    Boolean live = true; // Boolean | Whether to include live programmes
    List<String> mixin = Arrays.asList(); // List<String> | Request additional data in the output
    try {
      Object result = apiInstance.getHighlightsByChannel(channel, lang, rights, availability, live, mixin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#getHighlightsByChannel");
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
| **channel** | **String**| The channel identifier to limit results to. | |
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |
| **live** | **Boolean**| Whether to include live programmes | [optional] |
| **mixin** | [**List&lt;String&gt;**](String.md)| Request additional data in the output | [optional] [enum: live, promotions] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getScheduleByChannel"></a>
# **getScheduleByChannel**
> Object getScheduleByChannel(channel, date, lang, rights, availability)

Get schedule by channel

Get schedule by channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String channel = "channel_example"; // String | The channel identifier to limit results to.
    String date = "date_example"; // String | The date to return the schedule for, yyyy-mm-dd format
    String lang = "en"; // String | The language for any applicable localised strings.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    try {
      Object result = apiInstance.getScheduleByChannel(channel, date, lang, rights, availability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#getScheduleByChannel");
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
| **channel** | **String**| The channel identifier to limit results to. | |
| **date** | **String**| The date to return the schedule for, yyyy-mm-dd format | |
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |


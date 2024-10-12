# ChannelApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getChannel**](ChannelApi.md#getChannel) | **GET** /channel/{channelId} | Channel Detail |
| [**listChannels**](ChannelApi.md#listChannels) | **GET** /channel | Channel Collection |


<a id="getChannel"></a>
# **getChannel**
> Object getChannel(channelId, aliases)

Channel Detail

Return the content of the selected channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ChannelApi apiInstance = new ChannelApi(defaultClient);
    String channelId = "channelId_example"; // String | The identifier for the selected channel.
    Boolean aliases = true; // Boolean | Flag to display Legacy and Provider Ids.
    try {
      Object result = apiInstance.getChannel(channelId, aliases);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelApi#getChannel");
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
| **channelId** | **String**| The identifier for the selected channel. | |
| **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true] |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listChannels"></a>
# **listChannels**
> Object listChannels(platformId, regionId, aliases, date, scheduleStart, scheduleEnd, scheduleUpdatedSince)

Channel Collection

If you are interested in a list of channels that have had there schedule updated you can filter by the following query params.  - scheduleStart  - scheduleEnd  - scheduleUpdatedSince  adding these query params will filter the channel collection to only return channels that have been updated within the given range, updatedSince stores the state of your previous call.  Example Usage: Every 10 minutes get me the channels that have updated schedules for the next 2 weeks.  /channel?platform&#x3D;{uuid}&amp;scheduleStart&#x3D;{today}&amp;scheduleEnd&#x3D;{today + 2 weeks}&amp;updatedSince&#x3D;{10 minutes ago}  Also please note epg numbers are only exposed when a platform and region are passed to the query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ChannelApi apiInstance = new ChannelApi(defaultClient);
    String platformId = "d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3"; // String | The identifier for the selected platform. Multiple platforms can be passed to the API without a region Id. Passing multiple platforms without a region will not return epg numbers as these are linked to a platform and region.
    String regionId = "afa4f624-da9b-54ce-b514-570345dbbdce"; // String | The platform region ID for the channel selection.
    Boolean aliases = true; // Boolean | Flag to display Legacy and Provider Ids.
    String date = "2018-09-15"; // String | Date of the Channel State to select, this will display channel names and attributes in the future or past.
    String scheduleStart = "2015-05-05T00:00:00"; // String | The Start Date for the schedule.
    String scheduleEnd = "2015-05-06T00:00:00"; // String | The End Date for the schedule.
    String scheduleUpdatedSince = "2015-05-05T00:00:00"; // String | Schedule Updated Since
    try {
      Object result = apiInstance.listChannels(platformId, regionId, aliases, date, scheduleStart, scheduleEnd, scheduleUpdatedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelApi#listChannels");
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
| **platformId** | **String**| The identifier for the selected platform. Multiple platforms can be passed to the API without a region Id. Passing multiple platforms without a region will not return epg numbers as these are linked to a platform and region. | [optional] [default to d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3] |
| **regionId** | **String**| The platform region ID for the channel selection. | [optional] [default to afa4f624-da9b-54ce-b514-570345dbbdce] |
| **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true] |
| **date** | **String**| Date of the Channel State to select, this will display channel names and attributes in the future or past. | [optional] [default to 2018-09-15] |
| **scheduleStart** | **String**| The Start Date for the schedule. | [optional] [default to 2015-05-05T00:00:00] |
| **scheduleEnd** | **String**| The End Date for the schedule. | [optional] [default to 2015-05-06T00:00:00] |
| **scheduleUpdatedSince** | **String**| Schedule Updated Since | [optional] [default to 2015-05-05T00:00:00] |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |


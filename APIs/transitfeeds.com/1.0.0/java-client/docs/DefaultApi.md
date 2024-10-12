# DefaultApi

All URIs are relative to *https://api.transitfeeds.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFeedVersions**](DefaultApi.md#getFeedVersions) | **GET** /getFeedVersions | Retrieve a list of versions of specified (or all) feeds. |
| [**getFeeds**](DefaultApi.md#getFeeds) | **GET** /getFeeds | Retrieve a list of feeds. |
| [**getLatestFeedVersion**](DefaultApi.md#getLatestFeedVersion) | **GET** /getLatestFeedVersion | Retrieve the download URL for the latest version of a feed. |
| [**getLocations**](DefaultApi.md#getLocations) | **GET** /getLocations | Retrieve a list of locations. |


<a id="getFeedVersions"></a>
# **getFeedVersions**
> GetFeedVersionsResponse getFeedVersions(key, feed, page, limit, err, warn)

Retrieve a list of versions of specified (or all) feeds.

This API call allows you to easily see every single feed update in the TranstiFeeds.com system. Since this can be quite long, it&#39;s also possible to filter this list by a single feed ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.transitfeeds.com/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "YOUR_API_KEY"; // String | Your personal API key, used for authentication.
    String feed = "feed_example"; // String | If you only want to retrieve feed versions for a particular feed, include its ID here. You can use the `/getFeeds` call to discover feed IDs.
    Integer page = 1; // Integer | The page number of results to return. For example, if you specify a `page` of `2` with a `limit` of 10, then results 11-20 are returned. The number of pages available is included in the response. 
    Integer limit = 10; // Integer | The maximum number of results to return..
    Integer err = 0; // Integer | To include any errors detected when importing this feed in the response, specify a valud of `1`.
    Integer warn = 0; // Integer | To include any warnings detected when importing this feed in the response, specify a valud of `1`.
    try {
      GetFeedVersionsResponse result = apiInstance.getFeedVersions(key, feed, page, limit, err, warn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFeedVersions");
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
| **key** | **String**| Your personal API key, used for authentication. | [default to YOUR_API_KEY] |
| **feed** | **String**| If you only want to retrieve feed versions for a particular feed, include its ID here. You can use the &#x60;/getFeeds&#x60; call to discover feed IDs. | [optional] |
| **page** | **Integer**| The page number of results to return. For example, if you specify a &#x60;page&#x60; of &#x60;2&#x60; with a &#x60;limit&#x60; of 10, then results 11-20 are returned. The number of pages available is included in the response.  | [optional] [default to 1] |
| **limit** | **Integer**| The maximum number of results to return.. | [optional] [default to 10] |
| **err** | **Integer**| To include any errors detected when importing this feed in the response, specify a valud of &#x60;1&#x60;. | [optional] [default to 1] [enum: 0, 1] |
| **warn** | **Integer**| To include any warnings detected when importing this feed in the response, specify a valud of &#x60;1&#x60;. | [optional] [default to 1] [enum: 0, 1] |

### Return type

[**GetFeedVersionsResponse**](GetFeedVersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response for a valid &#x60;/getFeedVersions&#x60; API call. |  -  |

<a id="getFeeds"></a>
# **getFeeds**
> GetFeedsResponse getFeeds(key, location, descendants, page, limit, type)

Retrieve a list of feeds.

Used this API to retrieve a list of feeds in the system. Doing so can be usedful to discover feed IDs that can be used in other API calls. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.transitfeeds.com/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "YOUR_API_KEY"; // String | Your personal API key, used for authentication.
    Integer location = 56; // Integer | This is the unique ID of a location. If specified, feeds will only be returned that belong to this location (and perhaps sub-locations too, depending on the `descendants` value). You can use the `/getLocations` API endpoint to determine location IDs. 
    Integer descendants = 0; // Integer | If a location is specified in `location`, this flag can be used to control if returned feeds must be assigned directly to the location, or if feeds belonging to sub-locations can also be returned. If `0`, then feeds must be assigned directly to the specified location.
    Integer page = 1; // Integer | The page number of results to return. For example, if you specify a `page` of `2` with a `limit` of 10, then results 11-20 are returned. The number of pages available is included in the response. 
    Integer limit = 10; // Integer | The maximum number of results to return..
    String type = "gtfs"; // String | The type of feeds to return. If unspecified, feeds of all types are returned.
    try {
      GetFeedsResponse result = apiInstance.getFeeds(key, location, descendants, page, limit, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFeeds");
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
| **key** | **String**| Your personal API key, used for authentication. | [default to YOUR_API_KEY] |
| **location** | **Integer**| This is the unique ID of a location. If specified, feeds will only be returned that belong to this location (and perhaps sub-locations too, depending on the &#x60;descendants&#x60; value). You can use the &#x60;/getLocations&#x60; API endpoint to determine location IDs.  | [optional] |
| **descendants** | **Integer**| If a location is specified in &#x60;location&#x60;, this flag can be used to control if returned feeds must be assigned directly to the location, or if feeds belonging to sub-locations can also be returned. If &#x60;0&#x60;, then feeds must be assigned directly to the specified location. | [optional] [default to 1] [enum: 0, 1] |
| **page** | **Integer**| The page number of results to return. For example, if you specify a &#x60;page&#x60; of &#x60;2&#x60; with a &#x60;limit&#x60; of 10, then results 11-20 are returned. The number of pages available is included in the response.  | [optional] [default to 1] |
| **limit** | **Integer**| The maximum number of results to return.. | [optional] [default to 10] |
| **type** | **String**| The type of feeds to return. If unspecified, feeds of all types are returned. | [optional] [enum: gtfs, gtfsrealtime] |

### Return type

[**GetFeedsResponse**](GetFeedsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response for a valid &#x60;/getFeeds&#x60; API call. |  -  |

<a id="getLatestFeedVersion"></a>
# **getLatestFeedVersion**
> GetLatestFeedVersionResponse getLatestFeedVersion(key, feed)

Retrieve the download URL for the latest version of a feed.

Once you have used &#x60;/getFeeds&#x60; to discover a feed&#39;s URL, you can use this endpoint to download its latest version from TranstiFeeds. It will be unmodified in the original format from the provider. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.transitfeeds.com/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "YOUR_API_KEY"; // String | Your personal API key, used for authentication.
    String feed = "feed_example"; // String | The ID of the feed to retrieve the latest feed version for. You can use the `/getFeeds` call to discover feed IDs.
    try {
      GetLatestFeedVersionResponse result = apiInstance.getLatestFeedVersion(key, feed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLatestFeedVersion");
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
| **key** | **String**| Your personal API key, used for authentication. | [default to YOUR_API_KEY] |
| **feed** | **String**| The ID of the feed to retrieve the latest feed version for. You can use the &#x60;/getFeeds&#x60; call to discover feed IDs. | |

### Return type

[**GetLatestFeedVersionResponse**](GetLatestFeedVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response for a &#x60;/getLatestFeedVersion&#x60; API call that includes invalid request parameters. |  -  |
| **302** | If a &#x60;/getLatestFeedVersion&#x60; request is valid, then a HTTP 302 Temporary Redirect is issued to the download location. For example, if the requested feed is a GTFS feed, then this will redirect to the URL of the latest zip file for this feed.  |  * Location -  <br>  |

<a id="getLocations"></a>
# **getLocations**
> GetLocationsResponse getLocations(key)

Retrieve a list of locations.

Retrieve a list of locations. Each location (except for the root) has a parent location, and each location has zero or more child locations. This hierarchy is generally structured so countries contain states, states contain cities (although this typically depends on the country). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.transitfeeds.com/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "YOUR_API_KEY"; // String | Your personal API key, used for authentication.
    try {
      GetLocationsResponse result = apiInstance.getLocations(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLocations");
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
| **key** | **String**| Your personal API key, used for authentication. | [default to YOUR_API_KEY] |

### Return type

[**GetLocationsResponse**](GetLocationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response for a valid &#x60;getLocations&#x60; API call. |  -  |
| **401** | The response for invalid key or permission denied. |  -  |
| **404** | The response for invalid API method. |  -  |


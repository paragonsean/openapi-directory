# ListsApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllListComments**](ListsApi.md#getAllListComments) | **GET** /lists/{id}/comments/{sort} | Get all list comments |
| [**getAllUsersWhoLikedAList**](ListsApi.md#getAllUsersWhoLikedAList) | **GET** /lists/{id}/likes | Get all users who liked a list |
| [**getItemsOnAList**](ListsApi.md#getItemsOnAList) | **GET** /lists/{id}/items/{type} | Get items on a list |
| [**getList**](ListsApi.md#getList) | **GET** /lists/{id} | Get list |
| [**getPopularLists**](ListsApi.md#getPopularLists) | **GET** /lists/popular | Get popular lists |
| [**getTrendingLists**](ListsApi.md#getTrendingLists) | **GET** /lists/trending | Get trending lists |


<a id="getAllListComments"></a>
# **getAllListComments**
> getAllListComments(id, sort, traktApiVersion, traktApiKey)

Get all list comments

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a list. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, and most &#x60;replies&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    ListsApi apiInstance = new ListsApi(defaultClient);
    Integer id = 55; // Integer | Trakt ID
    String sort = "newest"; // String | how to sort
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllListComments(id, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListsApi#getAllListComments");
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
| **id** | **Integer**| Trakt ID | |
| **sort** | **String**| how to sort | [enum: newest, oldest, likes, replies] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getAllUsersWhoLikedAList"></a>
# **getAllUsersWhoLikedAList**
> getAllUsersWhoLikedAList(id, traktApiVersion, traktApiKey)

Get all users who liked a list

#### &amp;#128196; Pagination  Returns all users who liked a list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    ListsApi apiInstance = new ListsApi(defaultClient);
    String id = "55"; // String | Trakt ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllUsersWhoLikedAList(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListsApi#getAllUsersWhoLikedAList");
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
| **id** | **String**| Trakt ID | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getItemsOnAList"></a>
# **getItemsOnAList**
> getItemsOnAList(id, type, traktApiVersion, traktApiKey)

Get items on a list

#### &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Get all items on a personal list. Items can be a &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;person&#x60;. You can optionally specify the &#x60;type&#x60; parameter with a single value or comma delimited string for multiple item types.  #### Notes  Each list item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  All list items are sorted by ascending &#x60;rank&#x60;. We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which can be used to custom sort the list _**in your app**_ based on the user&#39;s preference. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, and &#x60;collected&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    ListsApi apiInstance = new ListsApi(defaultClient);
    String id = "55"; // String | Trakt ID
    String type = "movie"; // String | Filter for a specific item type
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getItemsOnAList(id, type, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListsApi#getItemsOnAList");
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
| **id** | **String**| Trakt ID | |
| **type** | **String**| Filter for a specific item type | [enum: movie, show, season, episode, person] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Private-User -  <br>  * X-Sort-By -  <br>  * X-Sort-How -  <br>  |

<a id="getList"></a>
# **getList**
> getList(id, traktApiVersion, traktApiKey)

Get list

#### &amp;#128513; Emojis  Returns a single list. Use the [**_/lists/:id/items**](#reference/lists/list-items) method to get the actual items this list contains.  **Note:** You must use an integer &#x60;id&#x60;, and only public lists will return data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    ListsApi apiInstance = new ListsApi(defaultClient);
    Integer id = 55; // Integer | Trakt ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getList(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListsApi#getList");
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
| **id** | **Integer**| Trakt ID | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Sort-By -  <br>  * X-Sort-How -  <br>  |

<a id="getPopularLists"></a>
# **getPopularLists**
> getPopularLists(traktApiVersion, traktApiKey)

Get popular lists

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns the most popular lists. Popularity is calculated using total number of likes and comments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    ListsApi apiInstance = new ListsApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getPopularLists(traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListsApi#getPopularLists");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getTrendingLists"></a>
# **getTrendingLists**
> getTrendingLists(traktApiVersion, traktApiKey)

Get trending lists

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists with the most likes and comments over the last 7 days.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    ListsApi apiInstance = new ListsApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getTrendingLists(traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListsApi#getTrendingLists");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |


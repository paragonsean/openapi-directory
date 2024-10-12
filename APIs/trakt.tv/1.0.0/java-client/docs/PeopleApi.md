# PeopleApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getASinglePerson**](PeopleApi.md#getASinglePerson) | **GET** /people/{id} | Get a single person |
| [**getListsContainingThisPerson**](PeopleApi.md#getListsContainingThisPerson) | **GET** /people/{id}/lists/{type}/{sort} | Get lists containing this person |
| [**getMovieCredits**](PeopleApi.md#getMovieCredits) | **GET** /people/{id}/movies | Get movie credits |
| [**getRecentlyUpdatedPeople**](PeopleApi.md#getRecentlyUpdatedPeople) | **GET** /people/updates/{start_date} | Get recently updated people |
| [**getRecentlyUpdatedPeopleTraktIDs**](PeopleApi.md#getRecentlyUpdatedPeopleTraktIDs) | **GET** /people/updates/id/{start_date} | Get recently updated people Trakt IDs |
| [**getShowCredits**](PeopleApi.md#getShowCredits) | **GET** /people/{id}/shows | Get show credits |


<a id="getASinglePerson"></a>
# **getASinglePerson**
> getASinglePerson(id, traktApiVersion, traktApiKey)

Get a single person

#### &amp;#10024; Extended Info  Returns a single person&#39;s details.  #### Gender  If available, the &#x60;gender&#x60; property will be set to &#x60;male&#x60;, &#x60;female&#x60;, or &#x60;non_binary&#x60;.  #### Known For Department  If available, the &#x60;known_for_department&#x60; property will be set to &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, or &#x60;editing&#x60;. Many people have credits across departments, &#x60;known_for&#x60; allows you to select their default credits more accurately.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String id = "bryan-cranston"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getASinglePerson(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#getASinglePerson");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
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
| **200** | &#x60;&#x60;&#x60; /people/bryan-cranston?extended&#x3D;full &#x60;&#x60;&#x60; |  -  |

<a id="getListsContainingThisPerson"></a>
# **getListsContainingThisPerson**
> getListsContainingThisPerson(id, type, sort, traktApiVersion, traktApiKey)

Get lists containing this person

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this person. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String id = "bryan-cranston"; // String | Trakt ID, Trakt slug, or IMDB ID
    String type = "all"; // String | Filter for a specific list type
    String sort = "popular"; // String | How to sort
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getListsContainingThisPerson(id, type, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#getListsContainingThisPerson");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **type** | **String**| Filter for a specific list type | [enum: all, personal, official] |
| **sort** | **String**| How to sort | [enum: popular, likes, comments, items, added, updated] |
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

<a id="getMovieCredits"></a>
# **getMovieCredits**
> getMovieCredits(id, traktApiVersion, traktApiKey)

Get movie credits

#### &amp;#10024; Extended Info  Returns all movies where this person is in the &#x60;cast&#x60; or &#x60;crew&#x60;. Each &#x60;cast&#x60; object will have a &#x60;characters&#x60; array and a standard &#x60;movie&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;movie&#x60; object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String id = "bryan-cranston"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getMovieCredits(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#getMovieCredits");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
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
| **200** | OK |  -  |

<a id="getRecentlyUpdatedPeople"></a>
# **getRecentlyUpdatedPeople**
> getRecentlyUpdatedPeople(startDate, traktApiVersion, traktApiKey)

Get recently updated people

#### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns all people updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String startDate = "2020-11-27T00:00:00Z"; // String | Updated since this date and time.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getRecentlyUpdatedPeople(startDate, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#getRecentlyUpdatedPeople");
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
| **startDate** | **String**| Updated since this date and time. | |
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
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  * X-Start-Date -  <br>  |

<a id="getRecentlyUpdatedPeopleTraktIDs"></a>
# **getRecentlyUpdatedPeopleTraktIDs**
> getRecentlyUpdatedPeopleTraktIDs(startDate, traktApiVersion, traktApiKey)

Get recently updated people Trakt IDs

#### &amp;#128196; Pagination  Returns all people Trakt IDs updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String startDate = "2020-11-27T00:00:00Z"; // String | Updated since this date and time.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getRecentlyUpdatedPeopleTraktIDs(startDate, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#getRecentlyUpdatedPeopleTraktIDs");
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
| **startDate** | **String**| Updated since this date and time. | |
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
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  * X-Start-Date -  <br>  |

<a id="getShowCredits"></a>
# **getShowCredits**
> getShowCredits(id, traktApiVersion, traktApiKey)

Get show credits

#### &amp;#10024; Extended Info  Returns all shows where this person is in the &#x60;cast&#x60; or &#x60;crew&#x60;, including the &#x60;episode_count&#x60; for which they appear. Each &#x60;cast&#x60; object will have a &#x60;characters&#x60; array and a standard &#x60;show&#x60; object. If &#x60;series_regular&#x60; is &#x60;true&#x60;, this person is a series regular and not simply a guest star.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, &#x60;editing&#x60;, and &#x60;created  by&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;show&#x60; object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String id = "bryan-cranston"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getShowCredits(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#getShowCredits");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
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
| **200** | OK |  -  |


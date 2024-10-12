# SeasonsApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllPeopleForASeason**](SeasonsApi.md#getAllPeopleForASeason) | **GET** /shows/{id}/seasons/{season}/people | Get all people for a season |
| [**getAllSeasonComments**](SeasonsApi.md#getAllSeasonComments) | **GET** /shows/{id}/seasons/{season}/comments/{sort} | Get all season comments |
| [**getAllSeasonTranslations**](SeasonsApi.md#getAllSeasonTranslations) | **GET** /shows/{id}/seasons/{season}/translations/{language} | Get all season translations |
| [**getAllSeasonsForAShow**](SeasonsApi.md#getAllSeasonsForAShow) | **GET** /shows/{id}/seasons | Get all seasons for a show |
| [**getListsContainingThisSeason**](SeasonsApi.md#getListsContainingThisSeason) | **GET** /shows/{id}/seasons/{season}/lists/{type}/{sort} | Get lists containing this season |
| [**getSeasonRatings**](SeasonsApi.md#getSeasonRatings) | **GET** /shows/{id}/seasons/{season}/ratings | Get season ratings |
| [**getSeasonStats**](SeasonsApi.md#getSeasonStats) | **GET** /shows/{id}/seasons/{season}/stats | Get season stats |
| [**getSingleSeasonForAShow**](SeasonsApi.md#getSingleSeasonForAShow) | **GET** /shows/{id}/seasons/{season} | Get single season for a show |
| [**showsIdSeasonsSeasonWatchingGet**](SeasonsApi.md#showsIdSeasonsSeasonWatchingGet) | **GET** /shows/{id}/seasons/{season}/watching | Get users watching right now |


<a id="getAllPeopleForASeason"></a>
# **getAllPeopleForASeason**
> getAllPeopleForASeason(id, season, traktApiVersion, traktApiKey)

Get all people for a season

#### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for a season, including the &#x60;episode_count&#x60; for which they appear. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions).. Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in at least 1 episode of the season.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    SeasonsApi apiInstance = new SeasonsApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllPeopleForASeason(id, season, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeasonsApi#getAllPeopleForASeason");
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
| **season** | **Integer**| season number | |
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
| **200** | &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/people?extended&#x3D;guest_stars &#x60;&#x60;&#x60; |  -  |

<a id="getAllSeasonComments"></a>
# **getAllSeasonComments**
> getAllSeasonComments(id, season, sort, traktApiVersion, traktApiKey)

Get all season comments

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a season. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, most &#x60;plays&#x60;, and highest &#x60;watched&#x60; percentage.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    SeasonsApi apiInstance = new SeasonsApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    String sort = "newest"; // String | how to sort
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllSeasonComments(id, season, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeasonsApi#getAllSeasonComments");
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
| **season** | **Integer**| season number | |
| **sort** | **String**| how to sort | [enum: newest, oldest, likes, replies, highest, lowest, plays, watched] |
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

<a id="getAllSeasonTranslations"></a>
# **getAllSeasonTranslations**
> getAllSeasonTranslations(id, season, language, traktApiVersion, traktApiKey)

Get all season translations

Returns all translations for an season, including language and translated values for title and overview.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    SeasonsApi apiInstance = new SeasonsApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    String language = "es"; // String | 2 character language code
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllSeasonTranslations(id, season, language, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeasonsApi#getAllSeasonTranslations");
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
| **season** | **Integer**| season number | |
| **language** | **String**| 2 character language code | |
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

<a id="getAllSeasonsForAShow"></a>
# **getAllSeasonsForAShow**
> getAllSeasonsForAShow(id, traktApiVersion, traktApiKey)

Get all seasons for a show

#### &amp;#10024; Extended Info  Returns all seasons for a show including the number of episodes in each season.  #### Episodes  If you add &#x60;?extended&#x3D;episodes&#x60; to the URL, it will return all episodes for all seasons.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    SeasonsApi apiInstance = new SeasonsApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllSeasonsForAShow(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeasonsApi#getAllSeasonsForAShow");
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
| **200** | &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons?extended&#x3D;episodes &#x60;&#x60;&#x60; |  -  |

<a id="getListsContainingThisSeason"></a>
# **getListsContainingThisSeason**
> getListsContainingThisSeason(id, season, type, sort, traktApiVersion, traktApiKey)

Get lists containing this season

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this season. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    SeasonsApi apiInstance = new SeasonsApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    String type = "all"; // String | Filter for a specific list type
    String sort = "popular"; // String | How to sort
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getListsContainingThisSeason(id, season, type, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeasonsApi#getListsContainingThisSeason");
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
| **season** | **Integer**| season number | |
| **type** | **String**| Filter for a specific list type | [enum: all, personal, official, watchlists] |
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

<a id="getSeasonRatings"></a>
# **getSeasonRatings**
> getSeasonRatings(id, season, traktApiVersion, traktApiKey)

Get season ratings

Returns rating (between 0 and 10) and distribution for a season.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    SeasonsApi apiInstance = new SeasonsApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getSeasonRatings(id, season, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeasonsApi#getSeasonRatings");
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
| **season** | **Integer**| season number | |
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

<a id="getSeasonStats"></a>
# **getSeasonStats**
> getSeasonStats(id, season, traktApiVersion, traktApiKey)

Get season stats

Returns lots of season stats.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    SeasonsApi apiInstance = new SeasonsApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getSeasonStats(id, season, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeasonsApi#getSeasonStats");
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
| **season** | **Integer**| season number | |
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

<a id="getSingleSeasonForAShow"></a>
# **getSingleSeasonForAShow**
> getSingleSeasonForAShow(id, season, translations, traktApiVersion, traktApiKey)

Get single season for a show

#### &amp;#10024; Extended Info  Returns all episodes for a specific season of a show.  #### Translations  If you&#39;d like to included translated episode titles and overviews in the response, include the &#x60;translations&#x60; parameter in the URL. Include all languages by setting the parameter to &#x60;all&#x60; or use a specific 2 digit country language code to further limit it.  **Note:** This returns a lot of data, so please only use this parameter if you actually need it!

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    SeasonsApi apiInstance = new SeasonsApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    String translations = "es"; // String | include episode translations
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getSingleSeasonForAShow(id, season, translations, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeasonsApi#getSingleSeasonForAShow");
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
| **season** | **Integer**| season number | |
| **translations** | **String**| include episode translations | [optional] |
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

<a id="showsIdSeasonsSeasonWatchingGet"></a>
# **showsIdSeasonsSeasonWatchingGet**
> showsIdSeasonsSeasonWatchingGet(id, season, traktApiVersion, traktApiKey)

Get users watching right now

#### &amp;#10024; Extended Info  Returns all users watching this season right now.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    SeasonsApi apiInstance = new SeasonsApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.showsIdSeasonsSeasonWatchingGet(id, season, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeasonsApi#showsIdSeasonsSeasonWatchingGet");
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
| **season** | **Integer**| season number | |
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


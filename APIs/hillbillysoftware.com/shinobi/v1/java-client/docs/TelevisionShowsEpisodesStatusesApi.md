# TelevisionShowsEpisodesStatusesApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTVShowPost**](TelevisionShowsEpisodesStatusesApi.md#addTVShowPost) | **POST** /AddTVShow | Add new show to database |
| [**episodesByIDGet**](TelevisionShowsEpisodesStatusesApi.md#episodesByIDGet) | **GET** /Episodes/ByID/{AccessToken}/{ID} | Gets all episodes for selected ID |
| [**episodesBySeasonGet**](TelevisionShowsEpisodesStatusesApi.md#episodesBySeasonGet) | **GET** /Episodes/BySeason/{AccessToken}/{ID}/{Season} | Gets list of episodes for specified imdbID and Season number |
| [**episodesGet**](TelevisionShowsEpisodesStatusesApi.md#episodesGet) | **GET** /Episodes/ByShowName/{AccessToken}/{Showname} | Gets all episodes for selected show |
| [**episodesLastAvailableSeasonGet**](TelevisionShowsEpisodesStatusesApi.md#episodesLastAvailableSeasonGet) | **GET** /Episodes/LatestSeason/{AccessToken}/{ID} | Returns last available season number in database, based on passed imdbID |
| [**episodesLastAvailableSeasonbyNameGet**](TelevisionShowsEpisodesStatusesApi.md#episodesLastAvailableSeasonbyNameGet) | **GET** /Episodes/LatestSeason/Show/{AccessToken}/{Name} | Gets latest season number based on show name |
| [**episodesSeasonCountGet**](TelevisionShowsEpisodesStatusesApi.md#episodesSeasonCountGet) | **GET** /Episodes/SeasonCount/{AccessToken}/{ID} | Returns number of available seasons and episodes |
| [**showStatusGet**](TelevisionShowsEpisodesStatusesApi.md#showStatusGet) | **GET** /Status/{AccessToken}/{Query} | Returns status of queried show (query can be IMDB, TVDB, or showname) |
| [**tVShowByNameGet**](TelevisionShowsEpisodesStatusesApi.md#tVShowByNameGet) | **GET** /TV/ByName/{AccessToken}/{Query} | Returns results based on query, result set limited to 5 records |
| [**tVShowIDGet**](TelevisionShowsEpisodesStatusesApi.md#tVShowIDGet) | **GET** /TV/ByID/{accesstoken}/{imdbID} | Returns TVShow information based on IMDBid |


<a id="addTVShowPost"></a>
# **addTVShowPost**
> PostResult addTVShowPost(value)

Add new show to database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelevisionShowsEpisodesStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TelevisionShowsEpisodesStatusesApi apiInstance = new TelevisionShowsEpisodesStatusesApi(defaultClient);
    TVInformationPost value = new TVInformationPost(); // TVInformationPost | 
    try {
      PostResult result = apiInstance.addTVShowPost(value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelevisionShowsEpisodesStatusesApi#addTVShowPost");
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
| **value** | [**TVInformationPost**](TVInformationPost.md)|  | |

### Return type

[**PostResult**](PostResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result |  -  |
| **204** | Result |  -  |

<a id="episodesByIDGet"></a>
# **episodesByIDGet**
> List&lt;Episode&gt; episodesByIDGet(accessToken, ID)

Gets all episodes for selected ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelevisionShowsEpisodesStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TelevisionShowsEpisodesStatusesApi apiInstance = new TelevisionShowsEpisodesStatusesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String ID = "ID_example"; // String | imdbID
    try {
      List<Episode> result = apiInstance.episodesByIDGet(accessToken, ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelevisionShowsEpisodesStatusesApi#episodesByIDGet");
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
| **accessToken** | **String**|  | |
| **ID** | **String**| imdbID | |

### Return type

[**List&lt;Episode&gt;**](Episode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of episodes |  -  |

<a id="episodesBySeasonGet"></a>
# **episodesBySeasonGet**
> List&lt;Episode&gt; episodesBySeasonGet(accessToken, ID, season)

Gets list of episodes for specified imdbID and Season number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelevisionShowsEpisodesStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TelevisionShowsEpisodesStatusesApi apiInstance = new TelevisionShowsEpisodesStatusesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String ID = "ID_example"; // String | imdbID
    String season = "season_example"; // String | Season number
    try {
      List<Episode> result = apiInstance.episodesBySeasonGet(accessToken, ID, season);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelevisionShowsEpisodesStatusesApi#episodesBySeasonGet");
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
| **accessToken** | **String**|  | |
| **ID** | **String**| imdbID | |
| **season** | **String**| Season number | |

### Return type

[**List&lt;Episode&gt;**](Episode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of episodes for specified season |  -  |

<a id="episodesGet"></a>
# **episodesGet**
> List&lt;Episode&gt; episodesGet(accessToken, showname)

Gets all episodes for selected show

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelevisionShowsEpisodesStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TelevisionShowsEpisodesStatusesApi apiInstance = new TelevisionShowsEpisodesStatusesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String showname = "showname_example"; // String | 
    try {
      List<Episode> result = apiInstance.episodesGet(accessToken, showname);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelevisionShowsEpisodesStatusesApi#episodesGet");
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
| **accessToken** | **String**|  | |
| **showname** | **String**|  | |

### Return type

[**List&lt;Episode&gt;**](Episode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of episodes |  -  |

<a id="episodesLastAvailableSeasonGet"></a>
# **episodesLastAvailableSeasonGet**
> LastAvailableSeason episodesLastAvailableSeasonGet(accessToken, ID)

Returns last available season number in database, based on passed imdbID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelevisionShowsEpisodesStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TelevisionShowsEpisodesStatusesApi apiInstance = new TelevisionShowsEpisodesStatusesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String ID = "ID_example"; // String | imdbID
    try {
      LastAvailableSeason result = apiInstance.episodesLastAvailableSeasonGet(accessToken, ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelevisionShowsEpisodesStatusesApi#episodesLastAvailableSeasonGet");
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
| **accessToken** | **String**|  | |
| **ID** | **String**| imdbID | |

### Return type

[**LastAvailableSeason**](LastAvailableSeason.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns last available Season Number for passed imdbID |  -  |

<a id="episodesLastAvailableSeasonbyNameGet"></a>
# **episodesLastAvailableSeasonbyNameGet**
> LastAvailableSeason episodesLastAvailableSeasonbyNameGet(accessToken, name)

Gets latest season number based on show name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelevisionShowsEpisodesStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TelevisionShowsEpisodesStatusesApi apiInstance = new TelevisionShowsEpisodesStatusesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String name = "name_example"; // String | 
    try {
      LastAvailableSeason result = apiInstance.episodesLastAvailableSeasonbyNameGet(accessToken, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelevisionShowsEpisodesStatusesApi#episodesLastAvailableSeasonbyNameGet");
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
| **accessToken** | **String**|  | |
| **name** | **String**|  | |

### Return type

[**LastAvailableSeason**](LastAvailableSeason.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns last available Season Number for passed showname |  -  |

<a id="episodesSeasonCountGet"></a>
# **episodesSeasonCountGet**
> TVShowSeasons episodesSeasonCountGet(accessToken, ID)

Returns number of available seasons and episodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelevisionShowsEpisodesStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TelevisionShowsEpisodesStatusesApi apiInstance = new TelevisionShowsEpisodesStatusesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String ID = "ID_example"; // String | imdbID
    try {
      TVShowSeasons result = apiInstance.episodesSeasonCountGet(accessToken, ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelevisionShowsEpisodesStatusesApi#episodesSeasonCountGet");
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
| **accessToken** | **String**|  | |
| **ID** | **String**| imdbID | |

### Return type

[**TVShowSeasons**](TVShowSeasons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns number of seasons available |  -  |

<a id="showStatusGet"></a>
# **showStatusGet**
> List&lt;ShowStatus&gt; showStatusGet(accessToken, query)

Returns status of queried show (query can be IMDB, TVDB, or showname)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelevisionShowsEpisodesStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TelevisionShowsEpisodesStatusesApi apiInstance = new TelevisionShowsEpisodesStatusesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String query = "query_example"; // String | Query can be IMDB, TVDB, or Show name
    try {
      List<ShowStatus> result = apiInstance.showStatusGet(accessToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelevisionShowsEpisodesStatusesApi#showStatusGet");
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
| **accessToken** | **String**|  | |
| **query** | **String**| Query can be IMDB, TVDB, or Show name | |

### Return type

[**List&lt;ShowStatus&gt;**](ShowStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of statuses |  -  |

<a id="tVShowByNameGet"></a>
# **tVShowByNameGet**
> List&lt;TVInformation&gt; tVShowByNameGet(accessToken, query)

Returns results based on query, result set limited to 5 records

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelevisionShowsEpisodesStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TelevisionShowsEpisodesStatusesApi apiInstance = new TelevisionShowsEpisodesStatusesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String query = "query_example"; // String | 
    try {
      List<TVInformation> result = apiInstance.tVShowByNameGet(accessToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelevisionShowsEpisodesStatusesApi#tVShowByNameGet");
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
| **accessToken** | **String**|  | |
| **query** | **String**|  | |

### Return type

[**List&lt;TVInformation&gt;**](TVInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of television show information |  -  |

<a id="tVShowIDGet"></a>
# **tVShowIDGet**
> TVInformation tVShowIDGet(accesstoken, id, imdbID)

Returns TVShow information based on IMDBid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelevisionShowsEpisodesStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    TelevisionShowsEpisodesStatusesApi apiInstance = new TelevisionShowsEpisodesStatusesApi(defaultClient);
    String accesstoken = "accesstoken_example"; // String | 
    String id = "id_example"; // String | imdbID of show you want info on
    String imdbID = "imdbID_example"; // String | 
    try {
      TVInformation result = apiInstance.tVShowIDGet(accesstoken, id, imdbID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelevisionShowsEpisodesStatusesApi#tVShowIDGet");
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
| **accesstoken** | **String**|  | |
| **id** | **String**| imdbID of show you want info on | |
| **imdbID** | **String**|  | |

### Return type

[**TVInformation**](TVInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Television show information |  -  |


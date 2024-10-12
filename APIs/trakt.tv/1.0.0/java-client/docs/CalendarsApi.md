# CalendarsApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calendarsAllDvdStartDateDaysGet**](CalendarsApi.md#calendarsAllDvdStartDateDaysGet) | **GET** /calendars/all/dvd/{start_date}/{days} | Get DVD releases |
| [**calendarsAllMoviesStartDateDaysGet**](CalendarsApi.md#calendarsAllMoviesStartDateDaysGet) | **GET** /calendars/all/movies/{start_date}/{days} | Get movies |
| [**calendarsAllShowsNewStartDateDaysGet**](CalendarsApi.md#calendarsAllShowsNewStartDateDaysGet) | **GET** /calendars/all/shows/new/{start_date}/{days} | Get new shows |
| [**calendarsAllShowsPremieresStartDateDaysGet**](CalendarsApi.md#calendarsAllShowsPremieresStartDateDaysGet) | **GET** /calendars/all/shows/premieres/{start_date}/{days} | Get season premieres |
| [**calendarsAllShowsStartDateDaysGet**](CalendarsApi.md#calendarsAllShowsStartDateDaysGet) | **GET** /calendars/all/shows/{start_date}/{days} | Get shows |
| [**getDVDReleases**](CalendarsApi.md#getDVDReleases) | **GET** /calendars/my/dvd/{start_date}/{days} | Get DVD releases |
| [**getMovies**](CalendarsApi.md#getMovies) | **GET** /calendars/my/movies/{start_date}/{days} | Get movies |
| [**getNewShows**](CalendarsApi.md#getNewShows) | **GET** /calendars/my/shows/new/{start_date}/{days} | Get new shows |
| [**getSeasonPremieres**](CalendarsApi.md#getSeasonPremieres) | **GET** /calendars/my/shows/premieres/{start_date}/{days} | Get season premieres |
| [**getShows**](CalendarsApi.md#getShows) | **GET** /calendars/my/shows/{start_date}/{days} | Get shows |


<a id="calendarsAllDvdStartDateDaysGet"></a>
# **calendarsAllDvdStartDateDaysGet**
> calendarsAllDvdStartDateDaysGet(startDate, days, traktApiVersion, traktApiKey)

Get DVD releases

#### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a DVD release date during the time period specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String startDate = "2014-09-01"; // String | Start the calendar on this date.
    Integer days = 7; // Integer | Number of days to display.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.calendarsAllDvdStartDateDaysGet(startDate, days, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#calendarsAllDvdStartDateDaysGet");
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
| **startDate** | **String**| Start the calendar on this date. | |
| **days** | **Integer**| Number of days to display. | |
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
| **200** | OK |  * X-End-Date -  <br>  * X-Start-Date -  <br>  |

<a id="calendarsAllMoviesStartDateDaysGet"></a>
# **calendarsAllMoviesStartDateDaysGet**
> calendarsAllMoviesStartDateDaysGet(startDate, days, traktApiVersion, traktApiKey)

Get movies

#### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a release date during the time period specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String startDate = "2014-09-01"; // String | Start the calendar on this date.
    Integer days = 7; // Integer | Number of days to display.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.calendarsAllMoviesStartDateDaysGet(startDate, days, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#calendarsAllMoviesStartDateDaysGet");
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
| **startDate** | **String**| Start the calendar on this date. | |
| **days** | **Integer**| Number of days to display. | |
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
| **200** | OK |  * X-End-Date -  <br>  * X-Start-Date -  <br>  |

<a id="calendarsAllShowsNewStartDateDaysGet"></a>
# **calendarsAllShowsNewStartDateDaysGet**
> calendarsAllShowsNewStartDateDaysGet(startDate, days, traktApiVersion, traktApiKey)

Get new shows

#### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all new show premieres (season 1, episode 1) airing during the time period specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String startDate = "2014-09-01"; // String | Start the calendar on this date.
    Integer days = 7; // Integer | Number of days to display.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.calendarsAllShowsNewStartDateDaysGet(startDate, days, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#calendarsAllShowsNewStartDateDaysGet");
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
| **startDate** | **String**| Start the calendar on this date. | |
| **days** | **Integer**| Number of days to display. | |
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
| **200** | OK |  * X-End-Date -  <br>  * X-Start-Date -  <br>  |

<a id="calendarsAllShowsPremieresStartDateDaysGet"></a>
# **calendarsAllShowsPremieresStartDateDaysGet**
> calendarsAllShowsPremieresStartDateDaysGet(startDate, days, traktApiVersion, traktApiKey)

Get season premieres

#### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all show premieres (any season, episode 1) airing during the time period specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String startDate = "2014-09-01"; // String | Start the calendar on this date.
    Integer days = 7; // Integer | Number of days to display.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.calendarsAllShowsPremieresStartDateDaysGet(startDate, days, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#calendarsAllShowsPremieresStartDateDaysGet");
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
| **startDate** | **String**| Start the calendar on this date. | |
| **days** | **Integer**| Number of days to display. | |
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
| **200** | OK |  * X-End-Date -  <br>  * X-Start-Date -  <br>  |

<a id="calendarsAllShowsStartDateDaysGet"></a>
# **calendarsAllShowsStartDateDaysGet**
> calendarsAllShowsStartDateDaysGet(startDate, days, traktApiVersion, traktApiKey)

Get shows

#### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all shows airing during the time period specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String startDate = "2014-09-01"; // String | Start the calendar on this date.
    Integer days = 7; // Integer | Number of days to display.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.calendarsAllShowsStartDateDaysGet(startDate, days, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#calendarsAllShowsStartDateDaysGet");
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
| **startDate** | **String**| Start the calendar on this date. | |
| **days** | **Integer**| Number of days to display. | |
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
| **200** | OK |  * X-End-Date -  <br>  * X-Start-Date -  <br>  |

<a id="getDVDReleases"></a>
# **getDVDReleases**
> getDVDReleases(startDate, days, traktApiVersion, traktApiKey)

Get DVD releases

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a DVD release date during the time period specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String startDate = "2014-09-01"; // String | Start the calendar on this date.
    Integer days = 7; // Integer | Number of days to display.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getDVDReleases(startDate, days, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#getDVDReleases");
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
| **startDate** | **String**| Start the calendar on this date. | |
| **days** | **Integer**| Number of days to display. | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-End-Date -  <br>  * X-Start-Date -  <br>  |

<a id="getMovies"></a>
# **getMovies**
> getMovies(startDate, days, traktApiVersion, traktApiKey)

Get movies

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a release date during the time period specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String startDate = "2014-09-01"; // String | Start the calendar on this date.
    Integer days = 7; // Integer | Number of days to display.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getMovies(startDate, days, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#getMovies");
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
| **startDate** | **String**| Start the calendar on this date. | |
| **days** | **Integer**| Number of days to display. | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-End-Date -  <br>  * X-Start-Date -  <br>  |

<a id="getNewShows"></a>
# **getNewShows**
> getNewShows(startDate, days, traktApiVersion, traktApiKey)

Get new shows

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all new show premieres (season 1, episode 1) airing during the time period specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String startDate = "2014-09-01"; // String | Start the calendar on this date.
    Integer days = 7; // Integer | Number of days to display.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getNewShows(startDate, days, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#getNewShows");
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
| **startDate** | **String**| Start the calendar on this date. | |
| **days** | **Integer**| Number of days to display. | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-End-Date -  <br>  * X-Start-Date -  <br>  |

<a id="getSeasonPremieres"></a>
# **getSeasonPremieres**
> getSeasonPremieres(startDate, days, traktApiVersion, traktApiKey)

Get season premieres

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all show premieres (any season, episode 1) airing during the time period specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String startDate = "2014-09-01"; // String | Start the calendar on this date.
    Integer days = 7; // Integer | Number of days to display.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getSeasonPremieres(startDate, days, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#getSeasonPremieres");
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
| **startDate** | **String**| Start the calendar on this date. | |
| **days** | **Integer**| Number of days to display. | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-End-Date -  <br>  * X-Start-Date -  <br>  |

<a id="getShows"></a>
# **getShows**
> getShows(startDate, days, traktApiVersion, traktApiKey)

Get shows

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all shows airing during the time period specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String startDate = "2014-09-01"; // String | Start the calendar on this date.
    Integer days = 7; // Integer | Number of days to display.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getShows(startDate, days, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#getShows");
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
| **startDate** | **String**| Start the calendar on this date. | |
| **days** | **Integer**| Number of days to display. | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-End-Date -  <br>  * X-Start-Date -  <br>  |


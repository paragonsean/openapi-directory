# CalendarTelevisionShowSchedulesApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calendarByShowNameGet**](CalendarTelevisionShowSchedulesApi.md#calendarByShowNameGet) | **GET** /Calendar/Show/{AccessToken}/{Name}/{Year} | Will return show schedule for queried showname and year |
| [**calendarCountriesGet**](CalendarTelevisionShowSchedulesApi.md#calendarCountriesGet) | **GET** /Calendar/Countries/{AccessToken} | Returns list of available countries in calendar database |
| [**calendarNetworksGet**](CalendarTelevisionShowSchedulesApi.md#calendarNetworksGet) | **GET** /Calendar/Networks/{AccessToken} | Gets a list of available networks |
| [**calendarShowSeasonsGet**](CalendarTelevisionShowSchedulesApi.md#calendarShowSeasonsGet) | **GET** /Calendar/Seasons/{AccessToken}/{Name} | Returns list of seasons available in the calendar for show |
| [**calendarTodayGet**](CalendarTelevisionShowSchedulesApi.md#calendarTodayGet) | **GET** /Calendar/Today/{AccessToken} | Will return show schedule for today for all countries in database |
| [**calendarbyShownameSeasonGet**](CalendarTelevisionShowSchedulesApi.md#calendarbyShownameSeasonGet) | **GET** /Calendar/Show/Season/{AccessToken}/{Name}/{Season} | Get Calendar by showname and season |
| [**scheduleByDateGet**](CalendarTelevisionShowSchedulesApi.md#scheduleByDateGet) | **GET** /Calendar/ByDate/{AccessToken}/{Date}/{Country} | Gets TV Schedule for selected data |


<a id="calendarByShowNameGet"></a>
# **calendarByShowNameGet**
> List&lt;Schedule&gt; calendarByShowNameGet(accessToken, name, year)

Will return show schedule for queried showname and year

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarTelevisionShowSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CalendarTelevisionShowSchedulesApi apiInstance = new CalendarTelevisionShowSchedulesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String name = "name_example"; // String | 
    String year = "year_example"; // String | 
    try {
      List<Schedule> result = apiInstance.calendarByShowNameGet(accessToken, name, year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarTelevisionShowSchedulesApi#calendarByShowNameGet");
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
| **year** | **String**|  | |

### Return type

[**List&lt;Schedule&gt;**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of schedules/calendar entries |  -  |

<a id="calendarCountriesGet"></a>
# **calendarCountriesGet**
> List&lt;Country&gt; calendarCountriesGet(accessToken)

Returns list of available countries in calendar database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarTelevisionShowSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CalendarTelevisionShowSchedulesApi apiInstance = new CalendarTelevisionShowSchedulesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    try {
      List<Country> result = apiInstance.calendarCountriesGet(accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarTelevisionShowSchedulesApi#calendarCountriesGet");
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

### Return type

[**List&lt;Country&gt;**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of countries |  -  |

<a id="calendarNetworksGet"></a>
# **calendarNetworksGet**
> List&lt;Networks&gt; calendarNetworksGet(accessToken)

Gets a list of available networks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarTelevisionShowSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CalendarTelevisionShowSchedulesApi apiInstance = new CalendarTelevisionShowSchedulesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    try {
      List<Networks> result = apiInstance.calendarNetworksGet(accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarTelevisionShowSchedulesApi#calendarNetworksGet");
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

### Return type

[**List&lt;Networks&gt;**](Networks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of networks |  -  |

<a id="calendarShowSeasonsGet"></a>
# **calendarShowSeasonsGet**
> List&lt;ShowSeasons&gt; calendarShowSeasonsGet(accessToken, name)

Returns list of seasons available in the calendar for show

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarTelevisionShowSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CalendarTelevisionShowSchedulesApi apiInstance = new CalendarTelevisionShowSchedulesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String name = "name_example"; // String | 
    try {
      List<ShowSeasons> result = apiInstance.calendarShowSeasonsGet(accessToken, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarTelevisionShowSchedulesApi#calendarShowSeasonsGet");
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

[**List&lt;ShowSeasons&gt;**](ShowSeasons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of years |  -  |

<a id="calendarTodayGet"></a>
# **calendarTodayGet**
> List&lt;Schedule&gt; calendarTodayGet(accessToken)

Will return show schedule for today for all countries in database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarTelevisionShowSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CalendarTelevisionShowSchedulesApi apiInstance = new CalendarTelevisionShowSchedulesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    try {
      List<Schedule> result = apiInstance.calendarTodayGet(accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarTelevisionShowSchedulesApi#calendarTodayGet");
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

### Return type

[**List&lt;Schedule&gt;**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of schedules/calendar entries |  -  |

<a id="calendarbyShownameSeasonGet"></a>
# **calendarbyShownameSeasonGet**
> List&lt;Schedule&gt; calendarbyShownameSeasonGet(accessToken, name, season)

Get Calendar by showname and season

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarTelevisionShowSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CalendarTelevisionShowSchedulesApi apiInstance = new CalendarTelevisionShowSchedulesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String name = "name_example"; // String | 
    String season = "season_example"; // String | 
    try {
      List<Schedule> result = apiInstance.calendarbyShownameSeasonGet(accessToken, name, season);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarTelevisionShowSchedulesApi#calendarbyShownameSeasonGet");
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
| **season** | **String**|  | |

### Return type

[**List&lt;Schedule&gt;**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of schedules/calendar entries |  -  |

<a id="scheduleByDateGet"></a>
# **scheduleByDateGet**
> List&lt;Schedule&gt; scheduleByDateGet(accessToken, date, country)

Gets TV Schedule for selected data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarTelevisionShowSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    CalendarTelevisionShowSchedulesApi apiInstance = new CalendarTelevisionShowSchedulesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String date = "date_example"; // String | date format year-month-day
    String country = "country_example"; // String | US / CA / NL / BE / DE / GB or FR
    try {
      List<Schedule> result = apiInstance.scheduleByDateGet(accessToken, date, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarTelevisionShowSchedulesApi#scheduleByDateGet");
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
| **date** | **String**| date format year-month-day | |
| **country** | **String**| US / CA / NL / BE / DE / GB or FR | |

### Return type

[**List&lt;Schedule&gt;**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of schedules/calendar entries |  -  |


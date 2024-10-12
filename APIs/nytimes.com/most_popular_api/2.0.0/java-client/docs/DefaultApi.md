# DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/mostpopular/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETMostemailedSectionTimePeriodJson**](DefaultApi.md#gETMostemailedSectionTimePeriodJson) | **GET** /mostemailed/{section}/{time-period}.json | Most Emailed by Section &amp; Time Period |
| [**gETMostsharedSectionTimePeriodJson**](DefaultApi.md#gETMostsharedSectionTimePeriodJson) | **GET** /mostshared/{section}/{time-period}.json | Most Shared by Section &amp; Time Period |
| [**gETMostviewedSectionTimePeriodJson**](DefaultApi.md#gETMostviewedSectionTimePeriodJson) | **GET** /mostviewed/{section}/{time-period}.json | Most Viewed by Section &amp; Time Period |


<a id="gETMostemailedSectionTimePeriodJson"></a>
# **gETMostemailedSectionTimePeriodJson**
> GETMostemailedSectionTimePeriodJson200Response gETMostemailedSectionTimePeriodJson(section, timePeriod)

Most Emailed by Section &amp; Time Period



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/mostpopular/v2");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String section = "Arts"; // String | Limits the results by one or more sections. You can use `all-sections` or one or more section names seperated by semicolons. See `viewed/sections.json` call to get a list of sections.  
    String timePeriod = "1"; // String | Number of days `1 | 7 | 30 ` corresponds to a day, a week, or a month of content.
    try {
      GETMostemailedSectionTimePeriodJson200Response result = apiInstance.gETMostemailedSectionTimePeriodJson(section, timePeriod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETMostemailedSectionTimePeriodJson");
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
| **section** | **String**| Limits the results by one or more sections. You can use &#x60;all-sections&#x60; or one or more section names seperated by semicolons. See &#x60;viewed/sections.json&#x60; call to get a list of sections.   | [enum: Arts, Automobiles, Blogs, Books, Business Day, Education, Fashion & Style, Food, Health, Job Market, Magazine, membercenter, Movies, Multimedia, N.Y.%20%2F%20Region, NYT Now, Obituaries, Open, Opinion, Public Editor, Real Estate, Science, Sports, Style, Sunday Review, T Magazine, Technology, The Upshot, Theater, Times Insider, Today’s Paper, Travel, U.S., World, Your Money, all-sections] |
| **timePeriod** | **String**| Number of days &#x60;1 | 7 | 30 &#x60; corresponds to a day, a week, or a month of content. | [enum: 1, 7, 30] |

### Return type

[**GETMostemailedSectionTimePeriodJson200Response**](GETMostemailedSectionTimePeriodJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Articles |  -  |
| **400** |  |  -  |
| **403** |  |  -  |

<a id="gETMostsharedSectionTimePeriodJson"></a>
# **gETMostsharedSectionTimePeriodJson**
> GETMostsharedSectionTimePeriodJson200Response gETMostsharedSectionTimePeriodJson(section, timePeriod)

Most Shared by Section &amp; Time Period



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/mostpopular/v2");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String section = "Arts"; // String | Limits the results by one or more sections. You can use `all-sections` or one or more section names seperated by semicolons. See `viewed/sections.json` call to get a list of sections.  
    String timePeriod = "1"; // String | Number of days `1 | 7 | 30 ` corresponds to a day, a week, or a month of content.
    try {
      GETMostsharedSectionTimePeriodJson200Response result = apiInstance.gETMostsharedSectionTimePeriodJson(section, timePeriod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETMostsharedSectionTimePeriodJson");
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
| **section** | **String**| Limits the results by one or more sections. You can use &#x60;all-sections&#x60; or one or more section names seperated by semicolons. See &#x60;viewed/sections.json&#x60; call to get a list of sections.   | [enum: Arts, Automobiles, Blogs, Books, Business Day, Education, Fashion & Style, Food, Health, Job Market, Magazine, membercenter, Movies, Multimedia, N.Y.%20%2F%20Region, NYT Now, Obituaries, Open, Opinion, Public Editor, Real Estate, Science, Sports, Style, Sunday Review, T Magazine, Technology, The Upshot, Theater, Times Insider, Today’s Paper, Travel, U.S., World, Your Money, all-sections] |
| **timePeriod** | **String**| Number of days &#x60;1 | 7 | 30 &#x60; corresponds to a day, a week, or a month of content. | [enum: 1, 7, 30] |

### Return type

[**GETMostsharedSectionTimePeriodJson200Response**](GETMostsharedSectionTimePeriodJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Articles |  -  |
| **400** |  |  -  |

<a id="gETMostviewedSectionTimePeriodJson"></a>
# **gETMostviewedSectionTimePeriodJson**
> GETMostsharedSectionTimePeriodJson200Response gETMostviewedSectionTimePeriodJson(section, timePeriod)

Most Viewed by Section &amp; Time Period



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/mostpopular/v2");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String section = "Arts"; // String | Limits the results by one or more sections. You can use `all-sections` or one or more section names seperated by semicolons. See `viewed/sections.json` call to get a list of sections.  
    String timePeriod = "1"; // String | Number of days `1 | 7 | 30 ` corresponds to a day, a week, or a month of content.
    try {
      GETMostsharedSectionTimePeriodJson200Response result = apiInstance.gETMostviewedSectionTimePeriodJson(section, timePeriod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETMostviewedSectionTimePeriodJson");
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
| **section** | **String**| Limits the results by one or more sections. You can use &#x60;all-sections&#x60; or one or more section names seperated by semicolons. See &#x60;viewed/sections.json&#x60; call to get a list of sections.   | [enum: Arts, Automobiles, Blogs, Books, Business Day, Education, Fashion & Style, Food, Health, Job Market, Magazine, membercenter, Movies, Multimedia, N.Y.%20%2F%20Region, NYT Now, Obituaries, Open, Opinion, Public Editor, Real Estate, Science, Sports, Style, Sunday Review, T Magazine, Technology, The Upshot, Theater, Times Insider, Today’s Paper, Travel, U.S., World, Your Money, all-sections] |
| **timePeriod** | **String**| Number of days &#x60;1 | 7 | 30 &#x60; corresponds to a day, a week, or a month of content. | [enum: 1, 7, 30] |

### Return type

[**GETMostsharedSectionTimePeriodJson200Response**](GETMostsharedSectionTimePeriodJson200Response.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Articles |  -  |


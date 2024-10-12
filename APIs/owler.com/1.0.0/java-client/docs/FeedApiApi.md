# FeedApiApi

All URIs are relative to *https://api.owler.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1FeedGet**](FeedApiApi.md#v1FeedGet) | **GET** /v1/feed | Get Feeds for given Company Ids |
| [**v1FeedUrlGet**](FeedApiApi.md#v1FeedUrlGet) | **GET** /v1/feed/url | Get Feeds for given Company Websites |


<a id="v1FeedGet"></a>
# **v1FeedGet**
> Results v1FeedGet(companyId, format, limit, paginationId, category)

Get Feeds for given Company Ids

The Feeds API provides a list of feeds and individual feed information for the given Company Ids and Category. By default the API returns the latest 10 feeds available unless the limit is specified. The maximum result is restricted to 100 feeds per API request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    FeedApiApi apiInstance = new FeedApiApi(defaultClient);
    List<String> companyId = Arrays.asList(); // List<String> | Company Ids separated by comma (Maximum of 150 Company Ids)
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    String limit = "10"; // String | Number of results to be displayed - 10 (by default, if not specified) to 100
    String paginationId = "*"; // String | Pass pagination_id as blank in the first API request. The API response will return the latest feeds along with the next pagination_id which can be passed in the subsequent API request to get the next set of feeds. Repeat this process until needed or till the pagination_id returned is blank
    List<String> category = Arrays.asList(); // List<String> | Categories separated by comma. If not specified, will search against all categories
    try {
      Results result = apiInstance.v1FeedGet(companyId, format, limit, paginationId, category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedApiApi#v1FeedGet");
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
| **companyId** | [**List&lt;String&gt;**](String.md)| Company Ids separated by comma (Maximum of 150 Company Ids) | |
| **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to json] [enum: xml, json] |
| **limit** | **String**| Number of results to be displayed - 10 (by default, if not specified) to 100 | [optional] [default to 10] |
| **paginationId** | **String**| Pass pagination_id as blank in the first API request. The API response will return the latest feeds along with the next pagination_id which can be passed in the subsequent API request to get the next set of feeds. Repeat this process until needed or till the pagination_id returned is blank | [optional] [default to *] |
| **category** | [**List&lt;String&gt;**](String.md)| Categories separated by comma. If not specified, will search against all categories | [optional] [enum: NEWS, PRESS, FUNDING, ACQUISITION, PEOPLE, BLOG, VIDEOS] |

### Return type

[**Results**](Results.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feeds Data |  -  |
| **400** | Invalid Parameters |  -  |
| **403** | Authentication Failed |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

<a id="v1FeedUrlGet"></a>
# **v1FeedUrlGet**
> Results v1FeedUrlGet(domain, format, limit, paginationId, category)

Get Feeds for given Company Websites

The Feeds API provides a list of feeds and individual feed information for the given Company Websites and Category. By default the API returns the latest 10 feeds available unless the limit is specified. The maximum result is restricted to 100 feeds per API request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.owler.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    FeedApiApi apiInstance = new FeedApiApi(defaultClient);
    List<String> domain = Arrays.asList(); // List<String> | Company Websites separated by comma (Maximum of 10 Company Websites)
    String format = "xml"; // String | Format of the response content - json (by default if not specified), xml
    String limit = "10"; // String | Number of results to be displayed - 10 (by default, if not specified) to 100
    String paginationId = "*"; // String | Pass pagination_id as blank in the first API request. The API response will return the latest feeds along with the next pagination_id which can be passed in the subsequent API request to get the next set of feeds. Repeat this process until needed or till the pagination_id returned is blank
    List<String> category = Arrays.asList(); // List<String> | Categories separated by comma. If not specified, will search against all categories
    try {
      Results result = apiInstance.v1FeedUrlGet(domain, format, limit, paginationId, category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedApiApi#v1FeedUrlGet");
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
| **domain** | [**List&lt;String&gt;**](String.md)| Company Websites separated by comma (Maximum of 10 Company Websites) | |
| **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to json] [enum: xml, json] |
| **limit** | **String**| Number of results to be displayed - 10 (by default, if not specified) to 100 | [optional] [default to 10] |
| **paginationId** | **String**| Pass pagination_id as blank in the first API request. The API response will return the latest feeds along with the next pagination_id which can be passed in the subsequent API request to get the next set of feeds. Repeat this process until needed or till the pagination_id returned is blank | [optional] [default to *] |
| **category** | [**List&lt;String&gt;**](String.md)| Categories separated by comma. If not specified, will search against all categories | [optional] [enum: NEWS, PRESS, FUNDING, ACQUISITION, PEOPLE, BLOG, VIDEOS] |

### Return type

[**Results**](Results.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feeds Data |  -  |
| **400** | Invalid Parameters |  -  |
| **403** | Authentication Failed |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |


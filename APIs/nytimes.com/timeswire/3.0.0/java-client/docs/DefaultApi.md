# DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/news/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentJsonGet**](DefaultApi.md#contentJsonGet) | **GET** /content.json |  |
| [**contentSourceSectionJsonGet**](DefaultApi.md#contentSourceSectionJsonGet) | **GET** /content/{source}/{section}.json |  |
| [**contentSourceSectionTimePeriodJsonGet**](DefaultApi.md#contentSourceSectionTimePeriodJsonGet) | **GET** /content/{source}/{section}/{time-period}.json |  |


<a id="contentJsonGet"></a>
# **contentJsonGet**
> ContentJsonGet200Response contentJsonGet(url)



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
    defaultClient.setBasePath("http://api.nytimes.com/svc/news/v3");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String url = "url_example"; // String | The complete URL of a specific news item, URL-encoded or backslash-escaped
    try {
      ContentJsonGet200Response result = apiInstance.contentJsonGet(url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#contentJsonGet");
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
| **url** | **String**| The complete URL of a specific news item, URL-encoded or backslash-escaped | |

### Return type

[**ContentJsonGet200Response**](ContentJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Articles |  -  |

<a id="contentSourceSectionJsonGet"></a>
# **contentSourceSectionJsonGet**
> ContentJsonGet200Response contentSourceSectionJsonGet(source, section, limit, offset)



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
    defaultClient.setBasePath("http://api.nytimes.com/svc/news/v3");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String source = "all"; // String | Limits the set of items by originating source  all = items from both The New York Times and The International New York Times nyt = New York Times items only iht = International New York Times items only 
    String section = "section_example"; // String | Limits the set of items by one or more sections all | One or more section names, separated by semicolons   To get all sections, specify all. To get a particular section or sections, use the section names returned by this request:  http://api.nytimes.com/svc/news/v3/content/section-list.json 
    Integer limit = 20; // Integer | Limits the number of results, between 1 and 20
    Integer offset = 0; // Integer | Sets the starting point of the result set
    try {
      ContentJsonGet200Response result = apiInstance.contentSourceSectionJsonGet(source, section, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#contentSourceSectionJsonGet");
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
| **source** | **String**| Limits the set of items by originating source  all &#x3D; items from both The New York Times and The International New York Times nyt &#x3D; New York Times items only iht &#x3D; International New York Times items only  | [enum: all, nyt, iht] |
| **section** | **String**| Limits the set of items by one or more sections all | One or more section names, separated by semicolons   To get all sections, specify all. To get a particular section or sections, use the section names returned by this request:  http://api.nytimes.com/svc/news/v3/content/section-list.json  | |
| **limit** | **Integer**| Limits the number of results, between 1 and 20 | [optional] [default to 20] |
| **offset** | **Integer**| Sets the starting point of the result set | [optional] [default to 0] |

### Return type

[**ContentJsonGet200Response**](ContentJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Articles |  -  |

<a id="contentSourceSectionTimePeriodJsonGet"></a>
# **contentSourceSectionTimePeriodJsonGet**
> ContentJsonGet200Response contentSourceSectionTimePeriodJsonGet(source, section, timePeriod, limit, offset)



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
    defaultClient.setBasePath("http://api.nytimes.com/svc/news/v3");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String source = "all"; // String | Limits the set of items by originating source  all = items from both The New York Times and The International New York Times nyt = New York Times items only iht = International New York Times items only 
    String section = "section_example"; // String | Limits the set of items by one or more sections all | One or more section names, separated by semicolons   To get all sections, specify all. To get a particular section or sections, use the section names returned by this request:  http://api.nytimes.com/svc/news/v3/content/section-list.json 
    Integer timePeriod = 56; // Integer | Limits the set of items by time published, integer in number of hours
    Integer limit = 20; // Integer | Limits the number of results, between 1 and 20
    Integer offset = 0; // Integer | Sets the starting point of the result set
    try {
      ContentJsonGet200Response result = apiInstance.contentSourceSectionTimePeriodJsonGet(source, section, timePeriod, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#contentSourceSectionTimePeriodJsonGet");
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
| **source** | **String**| Limits the set of items by originating source  all &#x3D; items from both The New York Times and The International New York Times nyt &#x3D; New York Times items only iht &#x3D; International New York Times items only  | [enum: all, nyt, iht] |
| **section** | **String**| Limits the set of items by one or more sections all | One or more section names, separated by semicolons   To get all sections, specify all. To get a particular section or sections, use the section names returned by this request:  http://api.nytimes.com/svc/news/v3/content/section-list.json  | |
| **timePeriod** | **Integer**| Limits the set of items by time published, integer in number of hours | |
| **limit** | **Integer**| Limits the number of results, between 1 and 20 | [optional] [default to 20] |
| **offset** | **Integer**| Sets the starting point of the result set | [optional] [default to 0] |

### Return type

[**ContentJsonGet200Response**](ContentJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Articles |  -  |


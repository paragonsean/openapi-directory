# MiscellaneousConversionOtherUtilitiesApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getIMDBidGetAsync**](MiscellaneousConversionOtherUtilitiesApi.md#getIMDBidGetAsync) | **GET** /GetIMDBid/ByID/{AccessToken}/{Query} | Gets list of avaiable IMDB ids from Movies and TV Show databases, you can use those to query other end points that need ID&#39;s |


<a id="getIMDBidGetAsync"></a>
# **getIMDBidGetAsync**
> List&lt;ImdbID&gt; getIMDBidGetAsync(accessToken, query)

Gets list of avaiable IMDB ids from Movies and TV Show databases, you can use those to query other end points that need ID&#39;s

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MiscellaneousConversionOtherUtilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MiscellaneousConversionOtherUtilitiesApi apiInstance = new MiscellaneousConversionOtherUtilitiesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String query = "query_example"; // String | 
    try {
      List<ImdbID> result = apiInstance.getIMDBidGetAsync(accessToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MiscellaneousConversionOtherUtilitiesApi#getIMDBidGetAsync");
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

[**List&lt;ImdbID&gt;**](ImdbID.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of imdb ID&#39;s |  -  |


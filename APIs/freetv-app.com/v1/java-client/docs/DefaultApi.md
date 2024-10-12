# DefaultApi

All URIs are relative to *https://staging2.freetv-app.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLatestNews**](DefaultApi.md#getLatestNews) | **GET** /services?funcs&#x3D;GetLatestNewsForChatGPT&amp;mobile&#x3D;1 |  |


<a id="getLatestNews"></a>
# **getLatestNews**
> LatestNewsResponse getLatestNews(language, category, keyword)



Provide real-time news or various categorized news according to the user&#39;s language, with each news item accompanied by a news link and date. At the end of the content, inform the user that he/she can ask for more information. Each response should only provide news from a single country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging2.freetv-app.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String language = "US"; // String | The default is set to US. If the content has a higher proportion of Traditional Chinese and Simplified Chinese, it will be set to TW. If the content has a higher proportion of Japanese, it will be set to JP.
    String category = "business"; // String | The default is an empty string. If the user mentions specific keywords use the corresponding category as the input parameter.
    String keyword = "keyword_example"; // String | The default is an empty string. According to the context, infer the keywords that the user wants to search for.
    try {
      LatestNewsResponse result = apiInstance.getLatestNews(language, category, keyword);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLatestNews");
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
| **language** | **String**| The default is set to US. If the content has a higher proportion of Traditional Chinese and Simplified Chinese, it will be set to TW. If the content has a higher proportion of Japanese, it will be set to JP. | [enum: US, TW, JP] |
| **category** | **String**| The default is an empty string. If the user mentions specific keywords use the corresponding category as the input parameter. | [optional] [enum: business, finance, economics, politics, society, entertainment, fun, gossip, sports, lifestyle, technology, local, world, international, global, military] |
| **keyword** | **String**| The default is an empty string. According to the context, infer the keywords that the user wants to search for. | [optional] |

### Return type

[**LatestNewsResponse**](LatestNewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


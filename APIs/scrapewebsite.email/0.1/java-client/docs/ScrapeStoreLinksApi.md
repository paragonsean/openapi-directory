# ScrapeStoreLinksApi

All URIs are relative to *http://scrapewebsite.email*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETV1ScrapeStoreLinksFormat**](ScrapeStoreLinksApi.md#gETV1ScrapeStoreLinksFormat) | **GET** /v1/scrape_store_links.json | Attempts to grab the google store url or the ios store url for a site, after searching through the site. |


<a id="gETV1ScrapeStoreLinksFormat"></a>
# **gETV1ScrapeStoreLinksFormat**
> gETV1ScrapeStoreLinksFormat(website)

Attempts to grab the google store url or the ios store url for a site, after searching through the site.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScrapeStoreLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://scrapewebsite.email");

    ScrapeStoreLinksApi apiInstance = new ScrapeStoreLinksApi(defaultClient);
    String website = "website_example"; // String | <p>The website (ie. www.soundflair.com)</p> 
    try {
      apiInstance.gETV1ScrapeStoreLinksFormat(website);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScrapeStoreLinksApi#gETV1ScrapeStoreLinksFormat");
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
| **website** | **String**| &lt;p&gt;The website (ie. www.soundflair.com)&lt;/p&gt;  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |


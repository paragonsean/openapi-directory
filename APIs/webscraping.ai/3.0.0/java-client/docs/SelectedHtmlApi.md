# SelectedHtmlApi

All URIs are relative to *https://api.webscraping.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSelected**](SelectedHtmlApi.md#getSelected) | **GET** /selected | HTML of a selected page area by URL and CSS selector |
| [**getSelectedMultiple**](SelectedHtmlApi.md#getSelectedMultiple) | **GET** /selected-multiple | HTML of multiple page areas by URL and CSS selectors |


<a id="getSelected"></a>
# **getSelected**
> String getSelected(url, selector, headers, timeout, js, jsTimeout, proxy, country, device, errorOn404, errorOnRedirect)

HTML of a selected page area by URL and CSS selector

Returns just HTML on success, JSON on error

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SelectedHtmlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.webscraping.ai");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SelectedHtmlApi apiInstance = new SelectedHtmlApi(defaultClient);
    String url = "https://example.com"; // String | URL of the target page
    String selector = "h1"; // String | CSS selector (null by default, returns whole page HTML)
    Map<String, String> headers = new HashMap(); // Map<String, String> | HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"})
    Integer timeout = 10000; // Integer | Maximum processing time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000)
    Boolean js = true; // Boolean | Execute on-page JavaScript using a headless browser (true by default)
    Integer jsTimeout = 2000; // Integer | Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.
    String proxy = "datacenter"; // String | Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.
    String country = "us"; // String | Country of the proxy to use (US by default). Only available on Startup and Custom plans.
    String device = "desktop"; // String | Type of device emulation.
    Boolean errorOn404 = false; // Boolean | Return error on 404 HTTP status on the target page (false by default).
    Boolean errorOnRedirect = false; // Boolean | Return error on redirect on the target page (false by default).
    try {
      String result = apiInstance.getSelected(url, selector, headers, timeout, js, jsTimeout, proxy, country, device, errorOn404, errorOnRedirect);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SelectedHtmlApi#getSelected");
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
| **url** | **String**| URL of the target page | |
| **selector** | **String**| CSS selector (null by default, returns whole page HTML) | [optional] |
| **headers** | [**Map&lt;String, String&gt;**](String.md)| HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&amp;headers[One]&#x3D;value1&amp;headers&#x3D;[Another]&#x3D;value2) or as a JSON encoded object (...&amp;headers&#x3D;{\&quot;One\&quot;: \&quot;value1\&quot;, \&quot;Another\&quot;: \&quot;value2\&quot;}) | [optional] |
| **timeout** | **Integer**| Maximum processing time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000) | [optional] [default to 10000] |
| **js** | **Boolean**| Execute on-page JavaScript using a headless browser (true by default) | [optional] [default to true] |
| **jsTimeout** | **Integer**| Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page. | [optional] [default to 2000] |
| **proxy** | **String**| Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details. | [optional] [default to datacenter] [enum: datacenter, residential] |
| **country** | **String**| Country of the proxy to use (US by default). Only available on Startup and Custom plans. | [optional] [default to us] [enum: us, gb, de, it, fr, ca, es, ru, jp, kr] |
| **device** | **String**| Type of device emulation. | [optional] [default to desktop] [enum: desktop, mobile, tablet] |
| **errorOn404** | **Boolean**| Return error on 404 HTTP status on the target page (false by default). | [optional] [default to false] |
| **errorOnRedirect** | **Boolean**| Return error on redirect on the target page (false by default). | [optional] [default to false] |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** |  |  -  |
| **402** |  |  -  |
| **403** |  |  -  |
| **429** |  |  -  |
| **500** |  |  -  |
| **502** |  |  -  |
| **503** |  |  -  |
| **504** |  |  -  |

<a id="getSelectedMultiple"></a>
# **getSelectedMultiple**
> List&lt;String&gt; getSelectedMultiple(url, selectors, headers, timeout, js, jsTimeout, proxy, country, device, errorOn404, errorOnRedirect)

HTML of multiple page areas by URL and CSS selectors

Always returns JSON

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SelectedHtmlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.webscraping.ai");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SelectedHtmlApi apiInstance = new SelectedHtmlApi(defaultClient);
    String url = "https://example.com"; // String | URL of the target page
    List<String> selectors = Arrays.asList(); // List<String> | Multiple CSS selectors (null by default, returns whole page HTML)
    Map<String, String> headers = new HashMap(); // Map<String, String> | HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"})
    Integer timeout = 10000; // Integer | Maximum processing time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000)
    Boolean js = true; // Boolean | Execute on-page JavaScript using a headless browser (true by default)
    Integer jsTimeout = 2000; // Integer | Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.
    String proxy = "datacenter"; // String | Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.
    String country = "us"; // String | Country of the proxy to use (US by default). Only available on Startup and Custom plans.
    String device = "desktop"; // String | Type of device emulation.
    Boolean errorOn404 = false; // Boolean | Return error on 404 HTTP status on the target page (false by default).
    Boolean errorOnRedirect = false; // Boolean | Return error on redirect on the target page (false by default).
    try {
      List<String> result = apiInstance.getSelectedMultiple(url, selectors, headers, timeout, js, jsTimeout, proxy, country, device, errorOn404, errorOnRedirect);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SelectedHtmlApi#getSelectedMultiple");
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
| **url** | **String**| URL of the target page | |
| **selectors** | [**List&lt;String&gt;**](String.md)| Multiple CSS selectors (null by default, returns whole page HTML) | [optional] |
| **headers** | [**Map&lt;String, String&gt;**](String.md)| HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&amp;headers[One]&#x3D;value1&amp;headers&#x3D;[Another]&#x3D;value2) or as a JSON encoded object (...&amp;headers&#x3D;{\&quot;One\&quot;: \&quot;value1\&quot;, \&quot;Another\&quot;: \&quot;value2\&quot;}) | [optional] |
| **timeout** | **Integer**| Maximum processing time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000) | [optional] [default to 10000] |
| **js** | **Boolean**| Execute on-page JavaScript using a headless browser (true by default) | [optional] [default to true] |
| **jsTimeout** | **Integer**| Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page. | [optional] [default to 2000] |
| **proxy** | **String**| Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details. | [optional] [default to datacenter] [enum: datacenter, residential] |
| **country** | **String**| Country of the proxy to use (US by default). Only available on Startup and Custom plans. | [optional] [default to us] [enum: us, gb, de, it, fr, ca, es, ru, jp, kr] |
| **device** | **String**| Type of device emulation. | [optional] [default to desktop] [enum: desktop, mobile, tablet] |
| **errorOn404** | **Boolean**| Return error on 404 HTTP status on the target page (false by default). | [optional] [default to false] |
| **errorOnRedirect** | **Boolean**| Return error on redirect on the target page (false by default). | [optional] [default to false] |

### Return type

**List&lt;String&gt;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** |  |  -  |
| **402** |  |  -  |
| **403** |  |  -  |
| **429** |  |  -  |
| **500** |  |  -  |
| **502** |  |  -  |
| **503** |  |  -  |
| **504** |  |  -  |


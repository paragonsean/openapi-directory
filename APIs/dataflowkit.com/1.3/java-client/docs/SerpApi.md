# SerpApi

All URIs are relative to *https://api.dataflowkit.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serp**](SerpApi.md#serp) | **POST** /serp | Collect search results from search engines |


<a id="serp"></a>
# **serp**
> Object serp(serprequest)

Collect search results from search engines

To crawl search engine result pages, you can use &#x60;/serp&#x60; endpoint. SERP collection service extracts a list of organic results, news, images, and more.  Specify configuration parameters, such as country or languages, to customize output SERP data. The following search engines are supported  - google - google-image - google-news - google-shopping - bing - duckduckgo - baidu - yandex   Generate ready-to-run code for your favorite language at [https://dataflowkit.com/serp](https://dataflowkit.com/serp)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SerpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dataflowkit.com/v1");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SerpApi apiInstance = new SerpApi(defaultClient);
    Serprequest serprequest = new Serprequest(); // Serprequest | <h2>Search parameters</h2>  > In most cases, you don't need to customize parameters by hand. Use <a href=\"https://dataflowkit.com/serp\" target=\"_blank\">SERP extraction Code generator</a>. It is the easiest way to generate a payload for launching in the Dataflow kit cloud.  <h3>URL GET parameters</h3>  |||| |-|-|-| |q| Parameter defines encoded search term. You can use anything that you would use in a regular Search engines search. (e.g. for Google, <ul> <li><code>link:dataflowkit.com</code>,</li> <li><code>site:twitter.com Bratislava</code>,</li><li><code>inurl:view/view.shtml</code>, etc.)</li></ul> See The Complete List of 42 Advanced <a href=\"https://ahrefs.com/blog/google-advanced-search-operators/\" target=\"_blank\">Google Search Operators</a>|<ul> <li><code>q</code> parameter is used by google, Bing, DuckDuckGo.</li><li> <code>text</code> is used as query holder by Yandex SE.</li><li> Chineese Baidu uses <code>wd</code> for this purpose.</li></ul>| |tbm| <code>tbm</code> is a special Google parameter used to differentiate between search types|  <ul> <li><code>tbm=isch</code> - Google Images,</li> <li> <code>tbm=nws</code> - Google News</li> <li><code>tbm=shop</code> - Google Shopping</li> </ul>| |lr|Restricts the search to documents written in a particular languages.|<ul><li>Google uses <code>lang_{two-letter lang code}</code> to specify languages and <code>&#124;</code> as a delimiter. (e.g., <code>lang_sk&#124;lang_de</code> will only search Slovak and German pages). See the <a href=\"https://developers.google.com/custom-search/v1/cse/list\">full list</a> of possible values for Google. </li><li>For Bing specify <code>setLang=en</code> parameter.</li><li> In Yandex use <code>lang=ca</code> parameter</li></ul>| |gl|Specify the country to search from. It's a two-letter country code. (e.g., <code>sk</code> for Slovakia, or <code>us</code> for the United States).| For Google see the <a href=\"https://developers.google.com/custom-search/docs/xml_results_appendices#countryCodes\">Country Codes</a> page for a list of valid values. For Bing <code>cc=at</code> parameter is used.| 
    try {
      Object result = apiInstance.serp(serprequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SerpApi#serp");
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
| **serprequest** | [**Serprequest**](Serprequest.md)| &lt;h2&gt;Search parameters&lt;/h2&gt;  &gt; In most cases, you don&#39;t need to customize parameters by hand. Use &lt;a href&#x3D;\&quot;https://dataflowkit.com/serp\&quot; target&#x3D;\&quot;_blank\&quot;&gt;SERP extraction Code generator&lt;/a&gt;. It is the easiest way to generate a payload for launching in the Dataflow kit cloud.  &lt;h3&gt;URL GET parameters&lt;/h3&gt;  |||| |-|-|-| |q| Parameter defines encoded search term. You can use anything that you would use in a regular Search engines search. (e.g. for Google, &lt;ul&gt; &lt;li&gt;&lt;code&gt;link:dataflowkit.com&lt;/code&gt;,&lt;/li&gt; &lt;li&gt;&lt;code&gt;site:twitter.com Bratislava&lt;/code&gt;,&lt;/li&gt;&lt;li&gt;&lt;code&gt;inurl:view/view.shtml&lt;/code&gt;, etc.)&lt;/li&gt;&lt;/ul&gt; See The Complete List of 42 Advanced &lt;a href&#x3D;\&quot;https://ahrefs.com/blog/google-advanced-search-operators/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Google Search Operators&lt;/a&gt;|&lt;ul&gt; &lt;li&gt;&lt;code&gt;q&lt;/code&gt; parameter is used by google, Bing, DuckDuckGo.&lt;/li&gt;&lt;li&gt; &lt;code&gt;text&lt;/code&gt; is used as query holder by Yandex SE.&lt;/li&gt;&lt;li&gt; Chineese Baidu uses &lt;code&gt;wd&lt;/code&gt; for this purpose.&lt;/li&gt;&lt;/ul&gt;| |tbm| &lt;code&gt;tbm&lt;/code&gt; is a special Google parameter used to differentiate between search types|  &lt;ul&gt; &lt;li&gt;&lt;code&gt;tbm&#x3D;isch&lt;/code&gt; - Google Images,&lt;/li&gt; &lt;li&gt; &lt;code&gt;tbm&#x3D;nws&lt;/code&gt; - Google News&lt;/li&gt; &lt;li&gt;&lt;code&gt;tbm&#x3D;shop&lt;/code&gt; - Google Shopping&lt;/li&gt; &lt;/ul&gt;| |lr|Restricts the search to documents written in a particular languages.|&lt;ul&gt;&lt;li&gt;Google uses &lt;code&gt;lang_{two-letter lang code}&lt;/code&gt; to specify languages and &lt;code&gt;&amp;#124;&lt;/code&gt; as a delimiter. (e.g., &lt;code&gt;lang_sk&amp;#124;lang_de&lt;/code&gt; will only search Slovak and German pages). See the &lt;a href&#x3D;\&quot;https://developers.google.com/custom-search/v1/cse/list\&quot;&gt;full list&lt;/a&gt; of possible values for Google. &lt;/li&gt;&lt;li&gt;For Bing specify &lt;code&gt;setLang&#x3D;en&lt;/code&gt; parameter.&lt;/li&gt;&lt;li&gt; In Yandex use &lt;code&gt;lang&#x3D;ca&lt;/code&gt; parameter&lt;/li&gt;&lt;/ul&gt;| |gl|Specify the country to search from. It&#39;s a two-letter country code. (e.g., &lt;code&gt;sk&lt;/code&gt; for Slovakia, or &lt;code&gt;us&lt;/code&gt; for the United States).| For Google see the &lt;a href&#x3D;\&quot;https://developers.google.com/custom-search/docs/xml_results_appendices#countryCodes\&quot;&gt;Country Codes&lt;/a&gt; page for a list of valid values. For Bing &lt;code&gt;cc&#x3D;at&lt;/code&gt; parameter is used.|  | |

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/x-ndjson, text/csv, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns data in the one of the follwing formats - JSON, JSON Lines, CSV, MS Excel, XML |  -  |
| **400** | Bad Request. Invalid payload specified. |  -  |
| **401** | Unauthorized. &#x60;api_key&#x60; parameter is missed or incorrect |  -  |
| **500** | Internal Server Error is a very general HTTP status code that means something has gone wrong on the web site&#39;s server. |  -  |


# ScrapeEmailsApi

All URIs are relative to *http://scrapewebsite.email*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETV1ScrapeEmailsFormat**](ScrapeEmailsApi.md#gETV1ScrapeEmailsFormat) | **GET** /v1/scrape_emails.json | Returns a list of emails scraped by priority (ie. e-mails appear on top level pages are first). Please note that subsequent calls to the same url will be fetched from the &lt;b&gt;cache&lt;/b&gt; (14 day flush). &lt;br/&gt;&lt;br/&gt;Will also parse patterns such as hello[at]site.com, hello[at]site[dot]com, hello(at)site.com, hello(at)site(dot)com, hello @ site.com, hello @ site . com. &lt;br/&gt;&lt;br/&gt;Please do note we cannot parse sites that require a login (for now), so for some Facebook pages it is not possible at the moment to fetch the e-mail.&lt;br/&gt;&lt;br/&gt;Finally, please note that the api will fetch links for up to 2 minutes. After that time it will start analysing the pages which have been scraped. &lt;b&gt;Therefore&lt;/b&gt; please ensure that your client has a timeout of at least &lt;b&gt;150 seconds&lt;/b&gt; (2 mins to fetch and the rest to parse). &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Please note&lt;/b&gt; that due to the fact that the api goes out to fetch the pages, the server allows only 1 concurrent request/ip. Requests which are made while the 1 request is still processing will result in a 429 code.&lt;br/&gt;&lt;br/&gt;&lt;b&gt;Please note&lt;/b&gt; that as of May 25, 2014, the main mechanism of tracking usage will be done via Mashape. You can get the free calls by signing up with the FREE plan.&lt;br/&gt;&lt;br/&gt;Please visit &lt;a href&#x3D;&#39;https://www.mashape.com/tommytcchan/scrape-website-email&#39;&gt;https://www.mashape.com/tommytcchan/scrape-website-email&lt;/a&gt;.&lt;br/&gt;&lt;br/&gt;&lt;b&gt;There is now a limit of 5 requests per day using this sample interface.&lt;/b&gt;&lt;br/&gt;&lt;br/&gt; |


<a id="gETV1ScrapeEmailsFormat"></a>
# **gETV1ScrapeEmailsFormat**
> gETV1ScrapeEmailsFormat(website, mustInclude)

Returns a list of emails scraped by priority (ie. e-mails appear on top level pages are first). Please note that subsequent calls to the same url will be fetched from the &lt;b&gt;cache&lt;/b&gt; (14 day flush). &lt;br/&gt;&lt;br/&gt;Will also parse patterns such as hello[at]site.com, hello[at]site[dot]com, hello(at)site.com, hello(at)site(dot)com, hello @ site.com, hello @ site . com. &lt;br/&gt;&lt;br/&gt;Please do note we cannot parse sites that require a login (for now), so for some Facebook pages it is not possible at the moment to fetch the e-mail.&lt;br/&gt;&lt;br/&gt;Finally, please note that the api will fetch links for up to 2 minutes. After that time it will start analysing the pages which have been scraped. &lt;b&gt;Therefore&lt;/b&gt; please ensure that your client has a timeout of at least &lt;b&gt;150 seconds&lt;/b&gt; (2 mins to fetch and the rest to parse). &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Please note&lt;/b&gt; that due to the fact that the api goes out to fetch the pages, the server allows only 1 concurrent request/ip. Requests which are made while the 1 request is still processing will result in a 429 code.&lt;br/&gt;&lt;br/&gt;&lt;b&gt;Please note&lt;/b&gt; that as of May 25, 2014, the main mechanism of tracking usage will be done via Mashape. You can get the free calls by signing up with the FREE plan.&lt;br/&gt;&lt;br/&gt;Please visit &lt;a href&#x3D;&#39;https://www.mashape.com/tommytcchan/scrape-website-email&#39;&gt;https://www.mashape.com/tommytcchan/scrape-website-email&lt;/a&gt;.&lt;br/&gt;&lt;br/&gt;&lt;b&gt;There is now a limit of 5 requests per day using this sample interface.&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScrapeEmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://scrapewebsite.email");

    ScrapeEmailsApi apiInstance = new ScrapeEmailsApi(defaultClient);
    String website = "website_example"; // String | <p>The website (ie. www.soundflair.com)</p> 
    String mustInclude = "mustInclude_example"; // String | <table>   <tbody>     <tr>       <td>Optional. The word(s) that the webpage must include (otherwise it will skip scraping that page). Good if you want to scrape only contact pages. Takes regex (ie. about</td>       <td>contact).</td>     </tr>   </tbody> </table> 
    try {
      apiInstance.gETV1ScrapeEmailsFormat(website, mustInclude);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScrapeEmailsApi#gETV1ScrapeEmailsFormat");
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
| **mustInclude** | **String**| &lt;table&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;Optional. The word(s) that the webpage must include (otherwise it will skip scraping that page). Good if you want to scrape only contact pages. Takes regex (ie. about&lt;/td&gt;       &lt;td&gt;contact).&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt;  | [optional] |

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


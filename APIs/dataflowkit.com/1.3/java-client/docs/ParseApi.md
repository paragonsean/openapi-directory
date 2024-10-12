# ParseApi

All URIs are relative to *https://api.dataflowkit.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**parse**](ParseApi.md#parse) | **POST** /parse | Extract structured data from web pages |


<a id="parse"></a>
# **parse**
> Object parse(parserequest)

Extract structured data from web pages

Dataflow kit uses CSS selectors to find HTML elements in web pages for later data extraction.  Open [visual point-and-click toolkit](https://dataflowkit.com/dfk) and click desired elements on a page to specify extracting data.     Then you can send generated payload to &#x60;/parse&#x60; endpoint. We crawl web pages and extract data like text, links, or images for you following the specified rules.    Extracted data is returned in CSV, MS Excel, JSON, JSON(Lines) or XML format. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dataflowkit.com/v1");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ParseApi apiInstance = new ParseApi(defaultClient);
    Parserequest parserequest = new Parserequest(); // Parserequest | ### Field types and attributes    - **Text**. Extract human-readable text from the selected element and all its child elements. HTML tags are stripped, and only text returned.      - **Link**. Capture link `href` attribute and link text. Or specify a special _Path_ option for website navigation. When Path option is true, all other selectors ignored, and no results from the current page returned.      - **Image**. Image type extracts `src` (URL) and `alt` attributes of an image   *** ### Filters Filters are used to manipulate text data when extracting.  Here is the list of available filters   - **Trim** removes leading and trailing white spaces from the _field text or attribute_  - **Normal** leaves the case and capitalization of text/ attribute exactly as is.  - **UPPERCASE** makes all of the letters in the Field's text/ attribute uppercase.  - **lowercase** makes all of the letters in the Field's text/ attribute lowercase.  - **Capitalize** capitalizes the first letter of each word in the Field's text/ attribute  - **Concatinate** joins text array element into a single string  *** ### Regular Expressions  For more advanced text formatting regular expression can be used. Some useful examples are listed below   | Input text | Regex | Result | | ---------- | ----- | ------ | | price- 10.99€ | <code>[0-9]+\\.[0-9]+</code> | 10.99 | | phone- 0 (944) 244-18-22 | <code>\\w+</code> | 09442441822 |   *** ### Details. Chaining. The Link field type serves as a navigation link to a details page containing more data. A special _Path_ option is used for navigation only. When the Path option specified, no results from the current page returned. But grouped results from details pages will be pulled instead. You can use chaining functionality of Dataflow Kit scraper to retrieve all the detail page data at the same time. 
    try {
      Object result = apiInstance.parse(parserequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParseApi#parse");
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
| **parserequest** | [**Parserequest**](Parserequest.md)| ### Field types and attributes    - **Text**. Extract human-readable text from the selected element and all its child elements. HTML tags are stripped, and only text returned.      - **Link**. Capture link &#x60;href&#x60; attribute and link text. Or specify a special _Path_ option for website navigation. When Path option is true, all other selectors ignored, and no results from the current page returned.      - **Image**. Image type extracts &#x60;src&#x60; (URL) and &#x60;alt&#x60; attributes of an image   *** ### Filters Filters are used to manipulate text data when extracting.  Here is the list of available filters   - **Trim** removes leading and trailing white spaces from the _field text or attribute_  - **Normal** leaves the case and capitalization of text/ attribute exactly as is.  - **UPPERCASE** makes all of the letters in the Field&#39;s text/ attribute uppercase.  - **lowercase** makes all of the letters in the Field&#39;s text/ attribute lowercase.  - **Capitalize** capitalizes the first letter of each word in the Field&#39;s text/ attribute  - **Concatinate** joins text array element into a single string  *** ### Regular Expressions  For more advanced text formatting regular expression can be used. Some useful examples are listed below   | Input text | Regex | Result | | ---------- | ----- | ------ | | price- 10.99€ | &lt;code&gt;[0-9]+\\.[0-9]+&lt;/code&gt; | 10.99 | | phone- 0 (944) 244-18-22 | &lt;code&gt;\\w+&lt;/code&gt; | 09442441822 |   *** ### Details. Chaining. The Link field type serves as a navigation link to a details page containing more data. A special _Path_ option is used for navigation only. When the Path option specified, no results from the current page returned. But grouped results from details pages will be pulled instead. You can use chaining functionality of Dataflow Kit scraper to retrieve all the detail page data at the same time.  | |

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns data in the one of the follwing formats - JSON, JSON Lines, CSV, MS Excel, XML |  -  |
| **400** | Bad Request. Invalid payload specified. |  -  |
| **401** | Unauthorized. &#x60;api_key&#x60; parameter is missed or incorrect |  -  |
| **500** | Internal Server Error is a very general HTTP status code that means something has gone wrong on the web site&#39;s server. |  -  |


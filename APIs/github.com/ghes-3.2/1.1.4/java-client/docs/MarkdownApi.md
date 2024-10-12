# MarkdownApi

All URIs are relative to *https://github.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**markdownRender**](MarkdownApi.md#markdownRender) | **POST** /markdown | Render a Markdown document |
| [**markdownRenderRaw**](MarkdownApi.md#markdownRenderRaw) | **POST** /markdown/raw | Render a Markdown document in raw mode |


<a id="markdownRender"></a>
# **markdownRender**
> String markdownRender(markdownRenderRequest)

Render a Markdown document



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarkdownApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    MarkdownApi apiInstance = new MarkdownApi(defaultClient);
    MarkdownRenderRequest markdownRenderRequest = new MarkdownRenderRequest(); // MarkdownRenderRequest | 
    try {
      String result = apiInstance.markdownRender(markdownRenderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarkdownApi#markdownRender");
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
| **markdownRenderRequest** | [**MarkdownRenderRequest**](MarkdownRenderRequest.md)|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Content-Length -  <br>  * Content-Type -  <br>  * X-CommonMarker-Version -  <br>  |
| **304** | Not modified |  -  |

<a id="markdownRenderRaw"></a>
# **markdownRenderRaw**
> String markdownRenderRaw(body)

Render a Markdown document in raw mode

You must send Markdown as plain text (using a &#x60;Content-Type&#x60; header of &#x60;text/plain&#x60; or &#x60;text/x-markdown&#x60;) to this endpoint, rather than using JSON format. In raw mode, [GitHub Flavored Markdown](https://github.github.com/gfm/) is not supported and Markdown will be rendered in plain format like a README.md file. Markdown content must be 400 KB or less.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarkdownApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    MarkdownApi apiInstance = new MarkdownApi(defaultClient);
    String body = "body_example"; // String | 
    try {
      String result = apiInstance.markdownRenderRaw(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarkdownApi#markdownRenderRaw");
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
| **body** | **String**|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, text/x-markdown
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * X-CommonMarker-Version -  <br>  |
| **304** | Not modified |  -  |


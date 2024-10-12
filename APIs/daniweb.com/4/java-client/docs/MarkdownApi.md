# MarkdownApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**markdownEmoticonsGet**](MarkdownApi.md#markdownEmoticonsGet) | **GET** /markdown/emoticons |  |
| [**markdownPost**](MarkdownApi.md#markdownPost) | **POST** /markdown |  |


<a id="markdownEmoticonsGet"></a>
# **markdownEmoticonsGet**
> EndpointGetMarkdownEmoticons markdownEmoticonsGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarkdownApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    MarkdownApi apiInstance = new MarkdownApi(defaultClient);
    try {
      EndpointGetMarkdownEmoticons result = apiInstance.markdownEmoticonsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarkdownApi#markdownEmoticonsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EndpointGetMarkdownEmoticons**](EndpointGetMarkdownEmoticons.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="markdownPost"></a>
# **markdownPost**
> EndpointPostMarkdown markdownPost(textRaw, textEmoticons)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarkdownApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    MarkdownApi apiInstance = new MarkdownApi(defaultClient);
    String textRaw = "textRaw_example"; // String | 
    Boolean textEmoticons = false; // Boolean | 
    try {
      EndpointPostMarkdown result = apiInstance.markdownPost(textRaw, textEmoticons);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarkdownApi#markdownPost");
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
| **textRaw** | **String**|  | |
| **textEmoticons** | **Boolean**|  | [optional] [default to false] |

### Return type

[**EndpointPostMarkdown**](EndpointPostMarkdown.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |


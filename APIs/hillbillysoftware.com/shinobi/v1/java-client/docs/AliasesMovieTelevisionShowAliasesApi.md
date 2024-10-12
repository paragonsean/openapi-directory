# AliasesMovieTelevisionShowAliasesApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aliasesByIDGet**](AliasesMovieTelevisionShowAliasesApi.md#aliasesByIDGet) | **GET** /Aliases/ByID/{AccessToken}/{imdbID} | Get known aliases for Movies or Television shows from passed imdbID |
| [**aliasesGet**](AliasesMovieTelevisionShowAliasesApi.md#aliasesGet) | **GET** /Aliases/ByName/{AccessToken}/{Title} | Get known aliases for Movies or Television shows |


<a id="aliasesByIDGet"></a>
# **aliasesByIDGet**
> List&lt;Aliases&gt; aliasesByIDGet(accessToken, imdbID)

Get known aliases for Movies or Television shows from passed imdbID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AliasesMovieTelevisionShowAliasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    AliasesMovieTelevisionShowAliasesApi apiInstance = new AliasesMovieTelevisionShowAliasesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String imdbID = "imdbID_example"; // String | 
    try {
      List<Aliases> result = apiInstance.aliasesByIDGet(accessToken, imdbID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AliasesMovieTelevisionShowAliasesApi#aliasesByIDGet");
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
| **imdbID** | **String**|  | |

### Return type

[**List&lt;Aliases&gt;**](Aliases.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of known Aliases |  -  |

<a id="aliasesGet"></a>
# **aliasesGet**
> List&lt;Aliases&gt; aliasesGet(accessToken, title)

Get known aliases for Movies or Television shows

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AliasesMovieTelevisionShowAliasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    AliasesMovieTelevisionShowAliasesApi apiInstance = new AliasesMovieTelevisionShowAliasesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String title = "title_example"; // String | Title of movie or television show
    try {
      List<Aliases> result = apiInstance.aliasesGet(accessToken, title);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AliasesMovieTelevisionShowAliasesApi#aliasesGet");
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
| **title** | **String**| Title of movie or television show | |

### Return type

[**List&lt;Aliases&gt;**](Aliases.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of known Aliases |  -  |


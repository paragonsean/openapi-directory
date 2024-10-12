# ForexApi

All URIs are relative to *https://1forge.com/forex-quotes*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quotesGet**](ForexApi.md#quotesGet) | **GET** /quotes | Get quotes for all symbols |
| [**symbolsGet**](ForexApi.md#symbolsGet) | **GET** /symbols | Get a list of symbols for which we provide real-time quotes |


<a id="quotesGet"></a>
# **quotesGet**
> quotesGet()

Get quotes for all symbols

Get quotes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForexApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://1forge.com/forex-quotes");

    ForexApi apiInstance = new ForexApi(defaultClient);
    try {
      apiInstance.quotesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ForexApi#quotesGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of quotes |  -  |

<a id="symbolsGet"></a>
# **symbolsGet**
> List&lt;String&gt; symbolsGet()

Get a list of symbols for which we provide real-time quotes

Symbol List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForexApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://1forge.com/forex-quotes");

    ForexApi apiInstance = new ForexApi(defaultClient);
    try {
      List<String> result = apiInstance.symbolsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForexApi#symbolsGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of symbols |  -  |


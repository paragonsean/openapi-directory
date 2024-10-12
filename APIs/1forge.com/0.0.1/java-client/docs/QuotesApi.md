# QuotesApi

All URIs are relative to *https://1forge.com/forex-quotes*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quotesGet_1**](QuotesApi.md#quotesGet_1) | **GET** /quotes | Get quotes for all symbols |
| [**symbolsGet_1**](QuotesApi.md#symbolsGet_1) | **GET** /symbols | Get a list of symbols for which we provide real-time quotes |


<a id="quotesGet_1"></a>
# **quotesGet_1**
> quotesGet_1()

Get quotes for all symbols

Get quotes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://1forge.com/forex-quotes");

    QuotesApi apiInstance = new QuotesApi(defaultClient);
    try {
      apiInstance.quotesGet_1();
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesApi#quotesGet_1");
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

<a id="symbolsGet_1"></a>
# **symbolsGet_1**
> List&lt;String&gt; symbolsGet_1()

Get a list of symbols for which we provide real-time quotes

Symbol List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://1forge.com/forex-quotes");

    QuotesApi apiInstance = new QuotesApi(defaultClient);
    try {
      List<String> result = apiInstance.symbolsGet_1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesApi#symbolsGet_1");
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


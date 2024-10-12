# QueryApi

All URIs are relative to *https://api.parliament.uk/search*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryExtensionGet**](QueryApi.md#queryExtensionGet) | **GET** /query.{extension} | Search results |
| [**queryGet**](QueryApi.md#queryGet) | **GET** /query | Search results |


<a id="queryExtensionGet"></a>
# **queryExtensionGet**
> queryExtensionGet(extension, q, start, count, subdomains, inUrlPrefixes)

Search results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.parliament.uk/search");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String extension = "atom"; // String | extension
    String q = "q_example"; // String | 
    BigDecimal start = new BigDecimal(78); // BigDecimal | 
    BigDecimal count = new BigDecimal(78); // BigDecimal | 
    String subdomains = "subdomains_example"; // String | 
    String inUrlPrefixes = "inUrlPrefixes_example"; // String | 
    try {
      apiInstance.queryExtensionGet(extension, q, start, count, subdomains, inUrlPrefixes);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryExtensionGet");
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
| **extension** | **String**| extension | [enum: atom, rss, html, json] |
| **q** | **String**|  | |
| **start** | **BigDecimal**|  | [optional] |
| **count** | **BigDecimal**|  | [optional] |
| **subdomains** | **String**|  | [optional] |
| **inUrlPrefixes** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/atom+xml, application/json, application/rss+xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search results |  -  |

<a id="queryGet"></a>
# **queryGet**
> queryGet(q, start, count, subdomains, inUrlPrefixes)

Search results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.parliament.uk/search");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String q = "q_example"; // String | 
    BigDecimal start = new BigDecimal(78); // BigDecimal | 
    BigDecimal count = new BigDecimal(78); // BigDecimal | 
    String subdomains = "subdomains_example"; // String | 
    String inUrlPrefixes = "inUrlPrefixes_example"; // String | 
    try {
      apiInstance.queryGet(q, start, count, subdomains, inUrlPrefixes);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryGet");
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
| **q** | **String**|  | |
| **start** | **BigDecimal**|  | [optional] |
| **count** | **BigDecimal**|  | [optional] |
| **subdomains** | **String**|  | [optional] |
| **inUrlPrefixes** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/atom+xml, application/json, application/rss+xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search results |  -  |


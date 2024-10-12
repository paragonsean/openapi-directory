# SslpApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMappedSSLPByPositionUsingGET**](SslpApi.md#getMappedSSLPByPositionUsingGET) | **GET** /sslps/mapped/{chr}/{start}/{stop}/{mapKey} | Returns a list SSLP for given position and assembly map |


<a id="getMappedSSLPByPositionUsingGET"></a>
# **getMappedSSLPByPositionUsingGET**
> List&lt;MappedSSLP&gt; getMappedSSLPByPositionUsingGET(chr, start, stop, mapKey)

Returns a list SSLP for given position and assembly map

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SslpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    SslpApi apiInstance = new SslpApi(defaultClient);
    String chr = "chr_example"; // String | Chromosome
    Long start = 56L; // Long | Start Position
    Long stop = 56L; // Long | Stop Position
    Integer mapKey = 56; // Integer | A list of assembly map keys can be found using the lookup service
    try {
      List<MappedSSLP> result = apiInstance.getMappedSSLPByPositionUsingGET(chr, start, stop, mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SslpApi#getMappedSSLPByPositionUsingGET");
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
| **chr** | **String**| Chromosome | |
| **start** | **Long**| Start Position | |
| **stop** | **Long**| Stop Position | |
| **mapKey** | **Integer**| A list of assembly map keys can be found using the lookup service | |

### Return type

[**List&lt;MappedSSLP&gt;**](MappedSSLP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |


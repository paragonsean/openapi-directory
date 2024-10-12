# NaicsApi

All URIs are relative to *https://discovery.gsa.gov*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listNaicsGET**](NaicsApi.md#listNaicsGET) | **GET** /api/naics/ | This endpoint lists all of the NAICS codes that are relevant to the OASIS family of vehicles |


<a id="listNaicsGET"></a>
# **listNaicsGET**
> Object listNaicsGET()

This endpoint lists all of the NAICS codes that are relevant to the OASIS family of vehicles

&lt;p&gt;This endpoint lists all of the NAICS codes that are relevant to the OASIS family of vehicles. It takes no parameters.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NaicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://discovery.gsa.gov");

    NaicsApi apiInstance = new NaicsApi(defaultClient);
    try {
      Object result = apiInstance.listNaicsGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NaicsApi#listNaicsGET");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |


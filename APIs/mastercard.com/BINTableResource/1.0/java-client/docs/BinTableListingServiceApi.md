# BinTableListingServiceApi

All URIs are relative to *https://api.mastercard.com/fraud/mtf/bintable/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**binlistingGet**](BinTableListingServiceApi.md#binlistingGet) | **GET** /binlisting | BIN Table Listing file |


<a id="binlistingGet"></a>
# **binlistingGet**
> BinTableResponse binlistingGet()

BIN Table Listing file

REST service will retrieve and return the BIN Table file to Merchants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BinTableListingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/fraud/mtf/bintable/v1");

    BinTableListingServiceApi apiInstance = new BinTableListingServiceApi(defaultClient);
    try {
      BinTableResponse result = apiInstance.binlistingGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BinTableListingServiceApi#binlistingGet");
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

[**BinTableResponse**](BinTableResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the BIN Table Listing file and available to Merchants |  -  |
| **404** | Resource Not Found |  -  |


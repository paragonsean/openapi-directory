# MerchantCategoriesApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**merchantsV1CategoryGet**](MerchantCategoriesApi.md#merchantsV1CategoryGet) | **GET** /merchants/v1/category | Returns a list of all merchant categories for contactless and cash back merchants (example:  Airline, Retail, etc.).  |


<a id="merchantsV1CategoryGet"></a>
# **merchantsV1CategoryGet**
> CategoriesResponse merchantsV1CategoryGet()

Returns a list of all merchant categories for contactless and cash back merchants (example:  Airline, Retail, etc.). 

Returns a list of all merchant categories for contactless and cash back merchants (example:  Airline, Retail, etc.). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    MerchantCategoriesApi apiInstance = new MerchantCategoriesApi(defaultClient);
    try {
      CategoriesResponse result = apiInstance.merchantsV1CategoryGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantCategoriesApi#merchantsV1CategoryGet");
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

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all the categories supported |  -  |
| **0** | Unexpected error |  -  |


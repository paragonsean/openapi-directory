# CurrencyApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**currencyGet**](CurrencyApi.md#currencyGet) | **GET** /api/Currency | Gets list of Currencies |


<a id="currencyGet"></a>
# **currencyGet**
> CurrencyList currencyGet()

Gets list of Currencies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrencyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");

    CurrencyApi apiInstance = new CurrencyApi(defaultClient);
    try {
      CurrencyList result = apiInstance.currencyGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrencyApi#currencyGet");
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

[**CurrencyList**](CurrencyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


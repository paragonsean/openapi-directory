# CurrenciesApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listSupportedCurrenciesV2**](CurrenciesApi.md#listSupportedCurrenciesV2) | **GET** /v2/currencies | List Supported Currencies |


<a id="listSupportedCurrenciesV2"></a>
# **listSupportedCurrenciesV2**
> SupportedCurrencyResponseV2 listSupportedCurrenciesV2()

List Supported Currencies

List the supported currencies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    try {
      SupportedCurrencyResponseV2 result = apiInstance.listSupportedCurrenciesV2();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#listSupportedCurrenciesV2");
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

[**SupportedCurrencyResponseV2**](SupportedCurrencyResponseV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List Supported Currencies |  -  |


# CurrencyRatesApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getcurrencyrate**](CurrencyRatesApi.md#getcurrencyrate) | **GET** /getcurrencyrate | Gets a foreign currency rate for one US Dollar |


<a id="getcurrencyrate"></a>
# **getcurrencyrate**
> Getcurrencyrate200Response getcurrencyrate(license, symbol)

Gets a foreign currency rate for one US Dollar

Use a currency symbol (EUR, GBP, CNY, JPY, AUD, etc.) to obtain a live currency foreign exchange rate for one US Dollar. See the API home page for list of all supported currencies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrencyRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    CurrencyRatesApi apiInstance = new CurrencyRatesApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String symbol = "symbol_example"; // String | Currency symbol to retrieve current rate for
    try {
      Getcurrencyrate200Response result = apiInstance.getcurrencyrate(license, symbol);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrencyRatesApi#getcurrencyrate");
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
| **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | |
| **symbol** | **String**| Currency symbol to retrieve current rate for | |

### Return type

[**Getcurrencyrate200Response**](Getcurrencyrate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Currency rate data to one US Dollar |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **404** | currency symbol not found |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |


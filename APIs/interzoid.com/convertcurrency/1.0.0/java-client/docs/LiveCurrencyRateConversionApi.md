# LiveCurrencyRateConversionApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**convertcurrency**](LiveCurrencyRateConversionApi.md#convertcurrency) | **GET** /convertcurrency | Converts amount in one currency to that of another |


<a id="convertcurrency"></a>
# **convertcurrency**
> Convertcurrency200Response convertcurrency(license, from, to, amount)

Converts amount in one currency to that of another

Provide an amount in one currency (EUR, GBP, CNY, JPY, AUD, etc.), and also a second currency to convert it to. The API will return the result using current foreign exchange rates. See the API home page for a list of all supported currencies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveCurrencyRateConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    LiveCurrencyRateConversionApi apiInstance = new LiveCurrencyRateConversionApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String from = "from_example"; // String | Currency symbol for the converted from amount
    String to = "to_example"; // String | Currency symbol for the converted to amount
    String amount = "amount_example"; // String | The amount of currency to be converted
    try {
      Convertcurrency200Response result = apiInstance.convertcurrency(license, from, to, amount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveCurrencyRateConversionApi#convertcurrency");
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
| **from** | **String**| Currency symbol for the converted from amount | |
| **to** | **String**| Currency symbol for the converted to amount | |
| **amount** | **String**| The amount of currency to be converted | |

### Return type

[**Convertcurrency200Response**](Convertcurrency200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Currency rate data to one US DOllar |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **404** | currency symbol not found |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |


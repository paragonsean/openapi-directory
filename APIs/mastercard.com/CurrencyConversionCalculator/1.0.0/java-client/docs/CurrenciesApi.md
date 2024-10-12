# CurrenciesApi

All URIs are relative to *http://api.mastercard.com/mcapi/settlement/currencyrate*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCurrencyRateDataUsingGET**](CurrenciesApi.md#getCurrencyRateDataUsingGET) | **GET** /settlement-currencies | getCurrencyRateData |


<a id="getCurrencyRateDataUsingGET"></a>
# **getCurrencyRateDataUsingGET**
> SettlementCurrencyRequest getCurrencyRateDataUsingGET()

getCurrencyRateData

List of supported currencies.

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
    defaultClient.setBasePath("http://api.mastercard.com/mcapi/settlement/currencyrate");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    try {
      SettlementCurrencyRequest result = apiInstance.getCurrencyRateDataUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#getCurrencyRateDataUsingGET");
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

[**SettlementCurrencyRequest**](SettlementCurrencyRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |


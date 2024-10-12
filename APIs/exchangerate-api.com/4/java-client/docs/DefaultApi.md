# DefaultApi

All URIs are relative to *https://api.exchangerate-api.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**latestBaseCurrencyGet**](DefaultApi.md#latestBaseCurrencyGet) | **GET** /latest/{base_currency} | Returns latest exchange rates in parameter-supplied base currency. |


<a id="latestBaseCurrencyGet"></a>
# **latestBaseCurrencyGet**
> LatestBaseCurrencyGet200Response latestBaseCurrencyGet(baseCurrency)

Returns latest exchange rates in parameter-supplied base currency.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exchangerate-api.com/v4");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String baseCurrency = "baseCurrency_example"; // String | **Base Currency**. *Example: USD*. You an use any of the ISO 4217 currency codes we support. See https://www.exchangerate-api.com/docs/supported-currencies
    try {
      LatestBaseCurrencyGet200Response result = apiInstance.latestBaseCurrencyGet(baseCurrency);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#latestBaseCurrencyGet");
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
| **baseCurrency** | **String**| **Base Currency**. *Example: USD*. You an use any of the ISO 4217 currency codes we support. See https://www.exchangerate-api.com/docs/supported-currencies | |

### Return type

[**LatestBaseCurrencyGet200Response**](LatestBaseCurrencyGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **404** | Currency code not supported |  -  |


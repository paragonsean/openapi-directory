# CurrencyApi

All URIs are relative to *https://api.billingo.hu/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConversionRate**](CurrencyApi.md#getConversionRate) | **GET** /currencies | Get currencies exchange rate. |


<a id="getConversionRate"></a>
# **getConversionRate**
> ConversationRate getConversionRate(from, to)

Get currencies exchange rate.

Return with the exchange value of given currencies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrencyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.billingo.hu/v3");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CurrencyApi apiInstance = new CurrencyApi(defaultClient);
    Currency from = Currency.fromValue("AUD"); // Currency | 
    Currency to = Currency.fromValue("AUD"); // Currency | 
    try {
      ConversationRate result = apiInstance.getConversionRate(from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrencyApi#getConversionRate");
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
| **from** | [**Currency**](.md)|  | [enum: AUD, BGN, BRL, CAD, CHF, CNY, CZK, DKK, EUR, GBP, HKD, HRK, HUF, IDR, ILS, INR, ISK, JPY, KRW, LTL, LVL, MXN, MYR, NOK, NZD, PHP, PLN, RON, RSD, RUB, SEK, SGD, THB, TRY, UAH, USD, ZAR] |
| **to** | [**Currency**](.md)|  | [enum: AUD, BGN, BRL, CAD, CHF, CNY, CZK, DKK, EUR, GBP, HKD, HRK, HUF, IDR, ILS, INR, ISK, JPY, KRW, LTL, LVL, MXN, MYR, NOK, NZD, PHP, PLN, RON, RSD, RUB, SEK, SGD, THB, TRY, UAH, USD, ZAR] |

### Return type

[**ConversationRate**](ConversationRate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Currencies exchange rate returned. |  * Retry-After - How many seconds you have to wait before making new request. <br>  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  |
| **400** | The request is malformed. |  * Retry-After - How many seconds you have to wait before making new request. <br>  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  |
| **401** | Authorization information is missing or invalid. |  * Retry-After - How many seconds you have to wait before making new request. <br>  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  |
| **422** | Validation errors occured. |  * Retry-After - How many seconds you have to wait before making new request. <br>  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  |
| **500** | Internal server error. |  * Retry-After - How many seconds you have to wait before making new request. <br>  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  * X-RateLimit-Reset - The timestamp at which the current rate limit window resets. <br>  |


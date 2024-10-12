# EndpointsApi

All URIs are relative to *https://api.currencytick.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**healthcheck**](EndpointsApi.md#healthcheck) | **GET** /healthcheck | Healthcheck |
| [**historicalExchangeRate**](EndpointsApi.md#historicalExchangeRate) | **GET** /historical | Historical Exchange Rate |
| [**listOfSupportedCurrencies**](EndpointsApi.md#listOfSupportedCurrencies) | **GET** /supported_currencies | List of supported currencies |
| [**liveCurrencyExchangeRate**](EndpointsApi.md#liveCurrencyExchangeRate) | **GET** /live | Live currency exchange rate |


<a id="healthcheck"></a>
# **healthcheck**
> Healthcheck200Response healthcheck()

Healthcheck

Check that the service is up. If everything is okay, you&#39;ll get a 200 OK response.  Otherwise, the request will fail with a 400 error, and a response listing the failed services.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.currencytick.com");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    try {
      Healthcheck200Response result = apiInstance.healthcheck();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#healthcheck");
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

[**Healthcheck200Response**](Healthcheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Service is unhealthy |  -  |

<a id="historicalExchangeRate"></a>
# **historicalExchangeRate**
> HistoricalExchangeRate200Response historicalExchangeRate(apikey, base, target, date)

Historical Exchange Rate

Get the exchange rate on a specific date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.currencytick.com");
    
    // Configure API key authorization: default
    ApiKeyAuth default = (ApiKeyAuth) defaultClient.getAuthentication("default");
    default.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //default.setApiKeyPrefix("Token");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String apikey = "YOUR_API_KEY"; // String | Authentication key.
    String base = "USD"; // String | The source currency.
    String target = "EUR"; // String | The target currency.
    String date = "2023-04-18"; // String | The date to get the exchange rate.
    try {
      HistoricalExchangeRate200Response result = apiInstance.historicalExchangeRate(apikey, base, target, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#historicalExchangeRate");
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
| **apikey** | **String**| Authentication key. | |
| **base** | **String**| The source currency. | |
| **target** | **String**| The target currency. | |
| **date** | **String**| The date to get the exchange rate. | |

### Return type

[**HistoricalExchangeRate200Response**](HistoricalExchangeRate200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listOfSupportedCurrencies"></a>
# **listOfSupportedCurrencies**
> String listOfSupportedCurrencies(apikey)

List of supported currencies

Get the list of supported currencies, currently 220 currencies are supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.currencytick.com");
    
    // Configure API key authorization: default
    ApiKeyAuth default = (ApiKeyAuth) defaultClient.getAuthentication("default");
    default.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //default.setApiKeyPrefix("Token");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String apikey = "YOUR_API_KEY"; // String | Authentication key.
    try {
      String result = apiInstance.listOfSupportedCurrencies(apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#listOfSupportedCurrencies");
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
| **apikey** | **String**| Authentication key. | |

### Return type

**String**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="liveCurrencyExchangeRate"></a>
# **liveCurrencyExchangeRate**
> HistoricalExchangeRate200Response liveCurrencyExchangeRate(apikey, base, target, amount)

Live currency exchange rate

Get the exchange rate between two currencies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.currencytick.com");
    
    // Configure API key authorization: default
    ApiKeyAuth default = (ApiKeyAuth) defaultClient.getAuthentication("default");
    default.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //default.setApiKeyPrefix("Token");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String apikey = "YOUR_API_KEY"; // String | Authentication key.
    String base = "USD"; // String | The source currency.
    String target = "EUR"; // String | The target currency.
    BigDecimal amount = new BigDecimal("1"); // BigDecimal | optional The amount to convert.
    try {
      HistoricalExchangeRate200Response result = apiInstance.liveCurrencyExchangeRate(apikey, base, target, amount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#liveCurrencyExchangeRate");
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
| **apikey** | **String**| Authentication key. | |
| **base** | **String**| The source currency. | |
| **target** | **String**| The target currency. | |
| **amount** | **BigDecimal**| optional The amount to convert. | [optional] |

### Return type

[**HistoricalExchangeRate200Response**](HistoricalExchangeRate200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


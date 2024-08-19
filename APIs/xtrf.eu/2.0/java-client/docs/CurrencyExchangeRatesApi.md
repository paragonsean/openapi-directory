# CurrencyExchangeRatesApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createExchangeRate**](CurrencyExchangeRatesApi.md#createExchangeRate) | **POST** /dictionaries/currency/{isoCode}/exchangeRate | Adding currency exchange rates. |
| [**getByIsoCode**](CurrencyExchangeRatesApi.md#getByIsoCode) | **GET** /dictionaries/currency/{isoCode}/exchangeRate | Returns currency exchange rates. |


<a id="createExchangeRate"></a>
# **createExchangeRate**
> createExchangeRate(isoCode, currencyHistoryDTO)

Adding currency exchange rates.

Adding currency exchange rates via API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrencyExchangeRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    CurrencyExchangeRatesApi apiInstance = new CurrencyExchangeRatesApi(defaultClient);
    String isoCode = "isoCode_example"; // String | iso code, https://www.xe.com/iso4217.php
    CurrencyHistoryDTO currencyHistoryDTO = new CurrencyHistoryDTO(); // CurrencyHistoryDTO | Adding new currency exchange rates
    try {
      apiInstance.createExchangeRate(isoCode, currencyHistoryDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrencyExchangeRatesApi#createExchangeRate");
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
| **isoCode** | **String**| iso code, https://www.xe.com/iso4217.php | |
| **currencyHistoryDTO** | [**CurrencyHistoryDTO**](CurrencyHistoryDTO.md)| Adding new currency exchange rates | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="getByIsoCode"></a>
# **getByIsoCode**
> CurrencyHistoryDTO getByIsoCode(isoCode)

Returns currency exchange rates.

Returns currency exchange rates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrencyExchangeRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    CurrencyExchangeRatesApi apiInstance = new CurrencyExchangeRatesApi(defaultClient);
    String isoCode = "isoCode_example"; // String | iso code, https://www.xe.com/iso4217.php
    try {
      CurrencyHistoryDTO result = apiInstance.getByIsoCode(isoCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrencyExchangeRatesApi#getByIsoCode");
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
| **isoCode** | **String**| iso code, https://www.xe.com/iso4217.php | |

### Return type

[**CurrencyHistoryDTO**](CurrencyHistoryDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |


# TickersApi

All URIs are relative to *https://api.chain49.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTickersListV2**](TickersApi.md#getTickersListV2) | **GET** /{blockchain}/v2/tickers-list/ | Get Tickers list V2 |
| [**getTickersV2**](TickersApi.md#getTickersV2) | **GET** /{blockchain}/v2/tickers/ | Get Tickers V2 |


<a id="getTickersListV2"></a>
# **getTickersListV2**
> GetTickersListV2200Response getTickersListV2(blockchain, timestamp)

Get Tickers list V2

Returns a list of available currency rate tickers (secondary currencies) for the specified date, along with an actual data timestamp.  Trailing slash &#39;/&#39; is mandatory

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TickersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.chain49.com");
    
    // Configure API key authorization: X-RapidAPI-Host
    ApiKeyAuth X-RapidAPI-Host = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Host");
    X-RapidAPI-Host.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Host.setApiKeyPrefix("Token");

    // Configure API key authorization: X-API-Key
    ApiKeyAuth X-API-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-API-Key");
    X-API-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    TickersApi apiInstance = new TickersApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    String timestamp = "1519053802"; // String | specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned.
    try {
      GetTickersListV2200Response result = apiInstance.getTickersListV2(blockchain, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TickersApi#getTickersListV2");
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
| **blockchain** | **String**| Blockchain name | |
| **timestamp** | **String**| specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. | [optional] |

### Return type

[**GetTickersListV2200Response**](GetTickersListV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getTickersV2"></a>
# **getTickersV2**
> GetTickersV2200Response getTickersV2(blockchain, timestamp, currency)

Get Tickers V2

Returns currency rate for the specified currency and date. If the currency is not available for that specific timestamp, the next closest rate will be returned. All responses contain an actual rate timestamp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TickersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.chain49.com");
    
    // Configure API key authorization: X-RapidAPI-Host
    ApiKeyAuth X-RapidAPI-Host = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Host");
    X-RapidAPI-Host.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Host.setApiKeyPrefix("Token");

    // Configure API key authorization: X-API-Key
    ApiKeyAuth X-API-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-API-Key");
    X-API-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    TickersApi apiInstance = new TickersApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    String timestamp = "1519053802"; // String | specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned.
    String currency = "usd"; // String | specifies a currency of returned rate (\"usd\", \"eur\", \"eth\"...). If not specified, all available currencies will be returned
    try {
      GetTickersV2200Response result = apiInstance.getTickersV2(blockchain, timestamp, currency);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TickersApi#getTickersV2");
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
| **blockchain** | **String**| Blockchain name | |
| **timestamp** | **String**| specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. | [optional] |
| **currency** | **String**| specifies a currency of returned rate (\&quot;usd\&quot;, \&quot;eur\&quot;, \&quot;eth\&quot;...). If not specified, all available currencies will be returned | [optional] |

### Return type

[**GetTickersV2200Response**](GetTickersV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


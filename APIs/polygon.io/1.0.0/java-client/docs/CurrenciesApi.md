# CurrenciesApi

All URIs are relative to *https://api.polygon.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CurrenciesGet**](CurrenciesApi.md#v1CurrenciesGet) | **GET** /v1/currencies | Available Currencies |
| [**v1HistoricForexFromToDateGet**](CurrenciesApi.md#v1HistoricForexFromToDateGet) | **GET** /v1/historic/forex/{from}/{to}/{date} | Historic Forex Ticks |
| [**v1LastCurrenciesFromToGet**](CurrenciesApi.md#v1LastCurrenciesFromToGet) | **GET** /v1/last/currencies/{from}/{to} | Last Trade for a Currency Pair |
| [**v1LastQuoteCurrenciesFromToGet**](CurrenciesApi.md#v1LastQuoteCurrenciesFromToGet) | **GET** /v1/last_quote/currencies/{from}/{to} | Last Quote for a Currency Pair |


<a id="v1CurrenciesGet"></a>
# **v1CurrenciesGet**
> List&lt;String&gt; v1CurrenciesGet()

Available Currencies

Get a list of the currencies that polygon.io streams. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.polygon.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    try {
      List<String> result = apiInstance.v1CurrenciesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#v1CurrenciesGet");
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

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of currencies |  -  |
| **0** | Unexpected error |  -  |

<a id="v1HistoricForexFromToDateGet"></a>
# **v1HistoricForexFromToDateGet**
> V1HistoricForexFromToDateGet200Response v1HistoricForexFromToDateGet(from, to, date, offset, limit)

Historic Forex Ticks

Get historic ticks for a currency pair. Example for **USD/JPY** the from would be **USD** and to would be **JPY**. The date formatted like **2017-6-22** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.polygon.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String from = "from_example"; // String | From Symbol of the currency pair
    String to = "to_example"; // String | To Symbol of the currency pair
    LocalDate date = LocalDate.now(); // LocalDate | Date/Day of the historic ticks to retreive
    Integer offset = 56; // Integer | Timestamp offset, used for pagination
    Integer limit = 100; // Integer | Limit the size of response, max: 10000
    try {
      V1HistoricForexFromToDateGet200Response result = apiInstance.v1HistoricForexFromToDateGet(from, to, date, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#v1HistoricForexFromToDateGet");
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
| **from** | **String**| From Symbol of the currency pair | |
| **to** | **String**| To Symbol of the currency pair | |
| **date** | **LocalDate**| Date/Day of the historic ticks to retreive | |
| **offset** | **Integer**| Timestamp offset, used for pagination | [optional] |
| **limit** | **Integer**| Limit the size of response, max: 10000 | [optional] [default to 100] |

### Return type

[**V1HistoricForexFromToDateGet200Response**](V1HistoricForexFromToDateGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of forex ticks |  -  |
| **0** | Unexpected error |  -  |

<a id="v1LastCurrenciesFromToGet"></a>
# **v1LastCurrenciesFromToGet**
> V1LastCurrenciesFromToGet200Response v1LastCurrenciesFromToGet(from, to)

Last Trade for a Currency Pair

Get Last Trade Tick for a Currency Pair. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.polygon.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String from = "from_example"; // String | From Symbol of the pair
    String to = "to_example"; // String | To Symbol of the pair
    try {
      V1LastCurrenciesFromToGet200Response result = apiInstance.v1LastCurrenciesFromToGet(from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#v1LastCurrenciesFromToGet");
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
| **from** | **String**| From Symbol of the pair | |
| **to** | **String**| To Symbol of the pair | |

### Return type

[**V1LastCurrenciesFromToGet200Response**](V1LastCurrenciesFromToGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Last tick for this currency pair |  -  |
| **0** | Unexpected error |  -  |

<a id="v1LastQuoteCurrenciesFromToGet"></a>
# **v1LastQuoteCurrenciesFromToGet**
> V1LastQuoteCurrenciesFromToGet200Response v1LastQuoteCurrenciesFromToGet(from, to)

Last Quote for a Currency Pair

Get Last Quote Tick for a Currency Pair. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.polygon.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String from = "from_example"; // String | From Symbol of the pair
    String to = "to_example"; // String | To Symbol of the pair
    try {
      V1LastQuoteCurrenciesFromToGet200Response result = apiInstance.v1LastQuoteCurrenciesFromToGet(from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#v1LastQuoteCurrenciesFromToGet");
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
| **from** | **String**| From Symbol of the pair | |
| **to** | **String**| To Symbol of the pair | |

### Return type

[**V1LastQuoteCurrenciesFromToGet200Response**](V1LastQuoteCurrenciesFromToGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Last quote tick for this currency pair |  -  |
| **0** | Unexpected error |  -  |


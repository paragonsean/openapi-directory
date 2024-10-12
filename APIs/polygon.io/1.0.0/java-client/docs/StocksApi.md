# StocksApi

All URIs are relative to *https://api.polygon.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CompaniesGet**](StocksApi.md#v1CompaniesGet) | **GET** /v1/companies | Available Companies |
| [**v1HistoricAggSizeSymbolDateGet**](StocksApi.md#v1HistoricAggSizeSymbolDateGet) | **GET** /v1/historic/agg/{size}/{symbol}/{date} | Historic Aggregates |
| [**v1HistoricQuotesSymbolDateGet**](StocksApi.md#v1HistoricQuotesSymbolDateGet) | **GET** /v1/historic/quotes/{symbol}/{date} | Historic Quotes |
| [**v1HistoricTradesSymbolDateGet**](StocksApi.md#v1HistoricTradesSymbolDateGet) | **GET** /v1/historic/trades/{symbol}/{date} | Historic Trades |
| [**v1LastQuoteStocksSymbolGet**](StocksApi.md#v1LastQuoteStocksSymbolGet) | **GET** /v1/last_quote/stocks/{symbol} | Last Quote for a Symbol |
| [**v1LastStocksSymbolGet**](StocksApi.md#v1LastStocksSymbolGet) | **GET** /v1/last/stocks/{symbol} | Last Trade for a Symbol |


<a id="v1CompaniesGet"></a>
# **v1CompaniesGet**
> List&lt;Company&gt; v1CompaniesGet(sort, perpage, page)

Available Companies

Get a list of the traded companies that polygon.io streams. Company includes some details about the company which we hope to add more to soon. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.polygon.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    StocksApi apiInstance = new StocksApi(defaultClient);
    String sort = "sort_example"; // String | Which field to sort by. For desc place a `-` in front of the field name. eg `?sort=-marketcap`
    BigDecimal perpage = new BigDecimal(78); // BigDecimal | How many items to be on each page during pagination
    BigDecimal page = new BigDecimal("1.0"); // BigDecimal | Which page of results to return
    try {
      List<Company> result = apiInstance.v1CompaniesGet(sort, perpage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StocksApi#v1CompaniesGet");
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
| **sort** | **String**| Which field to sort by. For desc place a &#x60;-&#x60; in front of the field name. eg &#x60;?sort&#x3D;-marketcap&#x60; | [optional] |
| **perpage** | **BigDecimal**| How many items to be on each page during pagination | [optional] |
| **page** | **BigDecimal**| Which page of results to return | [optional] [default to 1.0] |

### Return type

[**List&lt;Company&gt;**](Company.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of companies |  -  |
| **0** | Unexpected error |  -  |

<a id="v1HistoricAggSizeSymbolDateGet"></a>
# **v1HistoricAggSizeSymbolDateGet**
> V1HistoricAggSizeSymbolDateGet200Response v1HistoricAggSizeSymbolDateGet(size, symbol, date, offset, limit)

Historic Aggregates

Get historic aggregations for a symbol. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.polygon.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    StocksApi apiInstance = new StocksApi(defaultClient);
    String size = "second"; // String | Size of the aggregation. `second` or `minute`
    String symbol = "symbol_example"; // String | Symbol of the company to retrieve
    LocalDate date = LocalDate.now(); // LocalDate | Date/Day of the historic ticks to retreive
    Integer offset = 56; // Integer | Timestamp offset, used for pagination
    Integer limit = 100; // Integer | Limit the size of response, max: 10000
    try {
      V1HistoricAggSizeSymbolDateGet200Response result = apiInstance.v1HistoricAggSizeSymbolDateGet(size, symbol, date, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StocksApi#v1HistoricAggSizeSymbolDateGet");
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
| **size** | **String**| Size of the aggregation. &#x60;second&#x60; or &#x60;minute&#x60; | [enum: second, minute] |
| **symbol** | **String**| Symbol of the company to retrieve | |
| **date** | **LocalDate**| Date/Day of the historic ticks to retreive | |
| **offset** | **Integer**| Timestamp offset, used for pagination | [optional] |
| **limit** | **Integer**| Limit the size of response, max: 10000 | [optional] [default to 100] |

### Return type

[**V1HistoricAggSizeSymbolDateGet200Response**](V1HistoricAggSizeSymbolDateGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of aggregates |  -  |
| **0** | Unexpected error |  -  |

<a id="v1HistoricQuotesSymbolDateGet"></a>
# **v1HistoricQuotesSymbolDateGet**
> V1HistoricQuotesSymbolDateGet200Response v1HistoricQuotesSymbolDateGet(symbol, date, offset, limit)

Historic Quotes

Get historic quotes for a symbol. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.polygon.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    StocksApi apiInstance = new StocksApi(defaultClient);
    String symbol = "symbol_example"; // String | Symbol of the company to retrieve
    LocalDate date = LocalDate.now(); // LocalDate | Date/Day of the historic ticks to retreive
    Integer offset = 56; // Integer | Timestamp offset, used for pagination
    Integer limit = 100; // Integer | Limit the size of response, max: 10000
    try {
      V1HistoricQuotesSymbolDateGet200Response result = apiInstance.v1HistoricQuotesSymbolDateGet(symbol, date, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StocksApi#v1HistoricQuotesSymbolDateGet");
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
| **symbol** | **String**| Symbol of the company to retrieve | |
| **date** | **LocalDate**| Date/Day of the historic ticks to retreive | |
| **offset** | **Integer**| Timestamp offset, used for pagination | [optional] |
| **limit** | **Integer**| Limit the size of response, max: 10000 | [optional] [default to 100] |

### Return type

[**V1HistoricQuotesSymbolDateGet200Response**](V1HistoricQuotesSymbolDateGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of quotes |  -  |
| **0** | Unexpected error |  -  |

<a id="v1HistoricTradesSymbolDateGet"></a>
# **v1HistoricTradesSymbolDateGet**
> V1HistoricTradesSymbolDateGet200Response v1HistoricTradesSymbolDateGet(symbol, date, offset, limit)

Historic Trades

Get historic trades for a symbol. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.polygon.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    StocksApi apiInstance = new StocksApi(defaultClient);
    String symbol = "symbol_example"; // String | Symbol of the company to retrieve
    LocalDate date = LocalDate.now(); // LocalDate | Date/Day of the historic ticks to retreive
    Integer offset = 56; // Integer | Timestamp offset, used for pagination
    Integer limit = 100; // Integer | Limit the size of response, max: 10000
    try {
      V1HistoricTradesSymbolDateGet200Response result = apiInstance.v1HistoricTradesSymbolDateGet(symbol, date, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StocksApi#v1HistoricTradesSymbolDateGet");
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
| **symbol** | **String**| Symbol of the company to retrieve | |
| **date** | **LocalDate**| Date/Day of the historic ticks to retreive | |
| **offset** | **Integer**| Timestamp offset, used for pagination | [optional] |
| **limit** | **Integer**| Limit the size of response, max: 10000 | [optional] [default to 100] |

### Return type

[**V1HistoricTradesSymbolDateGet200Response**](V1HistoricTradesSymbolDateGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of trades |  -  |
| **0** | Unexpected error |  -  |

<a id="v1LastQuoteStocksSymbolGet"></a>
# **v1LastQuoteStocksSymbolGet**
> V1LastQuoteStocksSymbolGet200Response v1LastQuoteStocksSymbolGet(symbol)

Last Quote for a Symbol

Get the last quote tick for a given stock. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.polygon.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    StocksApi apiInstance = new StocksApi(defaultClient);
    String symbol = "symbol_example"; // String | Symbol of the stock to get
    try {
      V1LastQuoteStocksSymbolGet200Response result = apiInstance.v1LastQuoteStocksSymbolGet(symbol);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StocksApi#v1LastQuoteStocksSymbolGet");
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
| **symbol** | **String**| Symbol of the stock to get | |

### Return type

[**V1LastQuoteStocksSymbolGet200Response**](V1LastQuoteStocksSymbolGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Last quote tick for this stock |  -  |
| **0** | Unexpected error |  -  |

<a id="v1LastStocksSymbolGet"></a>
# **v1LastStocksSymbolGet**
> V1LastStocksSymbolGet200Response v1LastStocksSymbolGet(symbol)

Last Trade for a Symbol

Get the last trade for a given stock. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.polygon.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    StocksApi apiInstance = new StocksApi(defaultClient);
    String symbol = "symbol_example"; // String | Symbol of the stock to get
    try {
      V1LastStocksSymbolGet200Response result = apiInstance.v1LastStocksSymbolGet(symbol);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StocksApi#v1LastStocksSymbolGet");
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
| **symbol** | **String**| Symbol of the stock to get | |

### Return type

[**V1LastStocksSymbolGet200Response**](V1LastStocksSymbolGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Last trade for this stock |  -  |
| **0** | Unexpected error |  -  |


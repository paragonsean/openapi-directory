# CurrenciesApi

All URIs are relative to *https://api.nfusionsolutions.biz*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**currenciesHistoryGET**](CurrenciesApi.md#currenciesHistoryGET) | **GET** /api/v1/Currencies/history | Get historical prices for requested currency pairs |
| [**currenciesRateGET**](CurrenciesApi.md#currenciesRateGET) | **GET** /api/v1/Currencies/rate | Get latest mid rate for requested currency pairs |
| [**currenciesSummaryGET**](CurrenciesApi.md#currenciesSummaryGET) | **GET** /api/v1/Currencies/summary | Get latest Summary for requested currency pairs |
| [**currenciesSupportedCurrenciesHistoryGET**](CurrenciesApi.md#currenciesSupportedCurrenciesHistoryGET) | **GET** /api/v1/Currencies/history/supported | Get list of currency pairs supported by the history endpoint |
| [**currenciesSupportedCurrenciesRateGET**](CurrenciesApi.md#currenciesSupportedCurrenciesRateGET) | **GET** /api/v1/Currencies/rate/supported | Get list of currencies supported by the rate endpoint |
| [**currenciesSupportedCurrenciesSummaryGET**](CurrenciesApi.md#currenciesSupportedCurrenciesSummaryGET) | **GET** /api/v1/Currencies/summary/supported | Get list of currency pairs supported by the Summary endpoint |


<a id="currenciesHistoryGET"></a>
# **currenciesHistoryGET**
> List&lt;IntervalCollectionResponse&gt; currenciesHistoryGET(pairs, start, end, interval, format)

Get historical prices for requested currency pairs

Historical OHLC data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.

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
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String pairs = "pairs_example"; // String | comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | start date of time period. format is <i>yyyy-mm-dd</i>
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | end date of time period. format is <i>yyyy-mm-dd</i>. Default is current date.
    String interval = "interval_example"; // String | aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y=year,  m=month,  w=week,  d=day,  h=hour,  mi=minute    For example, a yearly interval can be specified as \"y\" and 6 month interval as \"6m\".     If not specified the interval parameter default is 1 Day.
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<IntervalCollectionResponse> result = apiInstance.currenciesHistoryGET(pairs, start, end, interval, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesHistoryGET");
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
| **pairs** | **String**| comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD | |
| **start** | **OffsetDateTime**| start date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt; | |
| **end** | **OffsetDateTime**| end date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;. Default is current date. | [optional] |
| **interval** | **String**| aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y&#x3D;year,  m&#x3D;month,  w&#x3D;week,  d&#x3D;day,  h&#x3D;hour,  mi&#x3D;minute    For example, a yearly interval can be specified as \&quot;y\&quot; and 6 month interval as \&quot;6m\&quot;.     If not specified the interval parameter default is 1 Day. | [optional] |
| **format** | **String**| to override content negotiation specify a value of json or xml | [optional] [enum: json, xml] |

### Return type

[**List&lt;IntervalCollectionResponse&gt;**](IntervalCollectionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="currenciesRateGET"></a>
# **currenciesRateGET**
> List&lt;RateResponse&gt; currenciesRateGET(pairs, format)

Get latest mid rate for requested currency pairs

Current Mid Rate

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
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String pairs = "pairs_example"; // String | comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<RateResponse> result = apiInstance.currenciesRateGET(pairs, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesRateGET");
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
| **pairs** | **String**| comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD | |
| **format** | **String**| to override content negotiation specify a value of json or xml | [optional] [enum: json, xml] |

### Return type

[**List&lt;RateResponse&gt;**](RateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="currenciesSummaryGET"></a>
# **currenciesSummaryGET**
> List&lt;SummaryResponse&gt; currenciesSummaryGET(pairs, format)

Get latest Summary for requested currency pairs

Current and daily summary information combined into a single quote

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
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String pairs = "pairs_example"; // String | comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<SummaryResponse> result = apiInstance.currenciesSummaryGET(pairs, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesSummaryGET");
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
| **pairs** | **String**| comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD | |
| **format** | **String**| to override content negotiation specify a value of json or xml | [optional] [enum: json, xml] |

### Return type

[**List&lt;SummaryResponse&gt;**](SummaryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="currenciesSupportedCurrenciesHistoryGET"></a>
# **currenciesSupportedCurrenciesHistoryGET**
> List&lt;String&gt; currenciesSupportedCurrenciesHistoryGET(format)

Get list of currency pairs supported by the history endpoint

Only the currency pairs in the direction noted can be used with the history endpoint.  For example: USD/CAD is not the same as CAD/USD

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
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<String> result = apiInstance.currenciesSupportedCurrenciesHistoryGET(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesSupportedCurrenciesHistoryGET");
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
| **format** | **String**| to override content negotiation specify a value of json or xml | [optional] [enum: json, xml] |

### Return type

**List&lt;String&gt;**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="currenciesSupportedCurrenciesRateGET"></a>
# **currenciesSupportedCurrenciesRateGET**
> List&lt;String&gt; currenciesSupportedCurrenciesRateGET(format)

Get list of currencies supported by the rate endpoint

Any of the currencies in this list can be paired with any other currency in this list when supplied to the Rate endpoint.  For example: USD/CAD,CAD/USD,USD/EUR,EUR/CAD

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
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<String> result = apiInstance.currenciesSupportedCurrenciesRateGET(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesSupportedCurrenciesRateGET");
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
| **format** | **String**| to override content negotiation specify a value of json or xml | [optional] [enum: json, xml] |

### Return type

**List&lt;String&gt;**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="currenciesSupportedCurrenciesSummaryGET"></a>
# **currenciesSupportedCurrenciesSummaryGET**
> List&lt;String&gt; currenciesSupportedCurrenciesSummaryGET(format)

Get list of currency pairs supported by the Summary endpoint

Only the currency pairs in the direction noted can be used with the Summary endpoint.  For example: USD/CAD is not the same as CAD/USD

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
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<String> result = apiInstance.currenciesSupportedCurrenciesSummaryGET(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesSupportedCurrenciesSummaryGET");
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
| **format** | **String**| to override content negotiation specify a value of json or xml | [optional] [enum: json, xml] |

### Return type

**List&lt;String&gt;**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |


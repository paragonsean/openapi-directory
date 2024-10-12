# MetalsApi

All URIs are relative to *https://api.nfusionsolutions.biz*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metalsBenchmarkHistoryGET**](MetalsApi.md#metalsBenchmarkHistoryGET) | **GET** /api/v1/Metals/benchmark/history | Get historical benchmark prices for requested metals |
| [**metalsBenchmarkSummaryGET**](MetalsApi.md#metalsBenchmarkSummaryGET) | **GET** /api/v1/Metals/benchmark/summary | Get latest Benchmark prices for requested metals |
| [**metalsBenchmarkSupportedMetalsGET**](MetalsApi.md#metalsBenchmarkSupportedMetalsGET) | **GET** /api/v1/Metals/benchmark/supported | Get list of symbols supported by the benchmark endpoints |
| [**metalsSpotAnnualHistoricalPerformanceGET**](MetalsApi.md#metalsSpotAnnualHistoricalPerformanceGET) | **GET** /api/v1/Metals/spot/performance/annual | Get Historical Annual Performance for requested metals |
| [**metalsSpotHistoricalPerformanceGET**](MetalsApi.md#metalsSpotHistoricalPerformanceGET) | **GET** /api/v1/Metals/spot/performance | Get Historical Performance for requested metals |
| [**metalsSpotHistoryGET**](MetalsApi.md#metalsSpotHistoryGET) | **GET** /api/v1/Metals/spot/history | Get historical Spot prices for requested metals |
| [**metalsSpotRatioHistoryGET**](MetalsApi.md#metalsSpotRatioHistoryGET) | **GET** /api/v1/Metals/spot/ratio/history | Get historical Spot Ratio prices for requested metals |
| [**metalsSpotRatioSummaryGET**](MetalsApi.md#metalsSpotRatioSummaryGET) | **GET** /api/v1/Metals/spot/ratio/summary | Get latest Spot Summary for requested metal ratios |
| [**metalsSpotSummaryGET**](MetalsApi.md#metalsSpotSummaryGET) | **GET** /api/v1/Metals/spot/summary | Get latest Spot Summary for requested metals |
| [**metalsSpotSupportedMetalsGET**](MetalsApi.md#metalsSpotSupportedMetalsGET) | **GET** /api/v1/Metals/spot/supported | Get list of symbols supported by the spot endpoints |
| [**metalsSupportedCurrenciesMetalsGET**](MetalsApi.md#metalsSupportedCurrenciesMetalsGET) | **GET** /api/v1/Metals/supported/currency | Get list of currencies supported by metals endpoints for currency conversion |


<a id="metalsBenchmarkHistoryGET"></a>
# **metalsBenchmarkHistoryGET**
> List&lt;IntervalCollectionResponse&gt; metalsBenchmarkHistoryGET(metals, start, end, interval, historicalfx, currency, unitofmeasure, format)

Get historical benchmark prices for requested metals

Historical OHLC data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.    The historicalfx flag is used to determine whether to apply today&#39;s fx rates to a historical period, or to apply the historical rates from that same time frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String metals = "metals_example"; // String | comma separated list of metals
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | start date of time period. format is <i>yyyy-mm-dd</i>
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | end date of time period. format is <i>yyyy-mm-dd</i>. Default is current date.
    String interval = "interval_example"; // String | aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y=year,  m=month,  w=week,  d=day,  h=hour,  mi=minute    For example, a yearly interval can be specified as \"y\" and 6 month interval as \"6m\".     If not specified the interval parameter default is 1 Day.
    Boolean historicalfx = true; // Boolean | if true use historical currency rates otherwise current currency rates. Defaults to true.
    String currency = "currency_example"; // String | comma separated list of conversion currencies, defaults to USD
    String unitofmeasure = "mg"; // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<IntervalCollectionResponse> result = apiInstance.metalsBenchmarkHistoryGET(metals, start, end, interval, historicalfx, currency, unitofmeasure, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsBenchmarkHistoryGET");
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
| **metals** | **String**| comma separated list of metals | |
| **start** | **OffsetDateTime**| start date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt; | |
| **end** | **OffsetDateTime**| end date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;. Default is current date. | [optional] |
| **interval** | **String**| aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y&#x3D;year,  m&#x3D;month,  w&#x3D;week,  d&#x3D;day,  h&#x3D;hour,  mi&#x3D;minute    For example, a yearly interval can be specified as \&quot;y\&quot; and 6 month interval as \&quot;6m\&quot;.     If not specified the interval parameter default is 1 Day. | [optional] |
| **historicalfx** | **Boolean**| if true use historical currency rates otherwise current currency rates. Defaults to true. | [optional] |
| **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] |
| **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] [enum: mg, g, kg, gr, oz, toz, ct, dwt] |
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

<a id="metalsBenchmarkSummaryGET"></a>
# **metalsBenchmarkSummaryGET**
> List&lt;SummaryResponse&gt; metalsBenchmarkSummaryGET(metals, currency, unitofmeasure, format)

Get latest Benchmark prices for requested metals

Benchmark price information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String metals = "metals_example"; // String | comma separated list of metals
    String currency = "currency_example"; // String | comma separated list of conversion currencies, defaults to USD
    String unitofmeasure = "mg"; // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<SummaryResponse> result = apiInstance.metalsBenchmarkSummaryGET(metals, currency, unitofmeasure, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsBenchmarkSummaryGET");
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
| **metals** | **String**| comma separated list of metals | |
| **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] |
| **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] [enum: mg, g, kg, gr, oz, toz, ct, dwt] |
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

<a id="metalsBenchmarkSupportedMetalsGET"></a>
# **metalsBenchmarkSupportedMetalsGET**
> List&lt;String&gt; metalsBenchmarkSupportedMetalsGET(format)

Get list of symbols supported by the benchmark endpoints



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<String> result = apiInstance.metalsBenchmarkSupportedMetalsGET(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsBenchmarkSupportedMetalsGET");
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

<a id="metalsSpotAnnualHistoricalPerformanceGET"></a>
# **metalsSpotAnnualHistoricalPerformanceGET**
> List&lt;IntervalCollectionResponse&gt; metalsSpotAnnualHistoricalPerformanceGET(metals, currency, unitofmeasure, format, years)

Get Historical Annual Performance for requested metals

Annual Historical Performance information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String metals = "metals_example"; // String | comma separated list of metals
    String currency = "currency_example"; // String | comma separated list of conversion currencies, defaults to USD
    String unitofmeasure = "mg"; // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    Integer years = 56; // Integer | Number of years of history to return. Defaults to 10.
    try {
      List<IntervalCollectionResponse> result = apiInstance.metalsSpotAnnualHistoricalPerformanceGET(metals, currency, unitofmeasure, format, years);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsSpotAnnualHistoricalPerformanceGET");
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
| **metals** | **String**| comma separated list of metals | |
| **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] |
| **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] [enum: mg, g, kg, gr, oz, toz, ct, dwt] |
| **format** | **String**| to override content negotiation specify a value of json or xml | [optional] [enum: json, xml] |
| **years** | **Integer**| Number of years of history to return. Defaults to 10. | [optional] |

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

<a id="metalsSpotHistoricalPerformanceGET"></a>
# **metalsSpotHistoricalPerformanceGET**
> List&lt;IntervalCollectionResponse&gt; metalsSpotHistoricalPerformanceGET(metals, currency, unitofmeasure, format)

Get Historical Performance for requested metals

Historical Performance information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String metals = "metals_example"; // String | comma separated list of metals
    String currency = "currency_example"; // String | comma separated list of conversion currencies, defaults to USD
    String unitofmeasure = "mg"; // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<IntervalCollectionResponse> result = apiInstance.metalsSpotHistoricalPerformanceGET(metals, currency, unitofmeasure, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsSpotHistoricalPerformanceGET");
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
| **metals** | **String**| comma separated list of metals | |
| **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] |
| **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] [enum: mg, g, kg, gr, oz, toz, ct, dwt] |
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

<a id="metalsSpotHistoryGET"></a>
# **metalsSpotHistoryGET**
> List&lt;IntervalCollectionResponse&gt; metalsSpotHistoryGET(metals, start, end, interval, historicalfx, currency, unitofmeasure, format)

Get historical Spot prices for requested metals

Historical OHLC data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.    The historicalfx flag is used to determine whether to apply today&#39;s fx rates to a historical period, or to apply the historical rates from that same time frame.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String metals = "metals_example"; // String | comma separated list of metals
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | start date of time period. format is <i>yyyy-mm-dd</i>
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | end date of time period. format is <i>yyyy-mm-dd</i>. Default is current date.
    String interval = "interval_example"; // String | aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y=year,  m=month,  w=week,  d=day,  h=hour,  mi=minute    For example, a yearly interval can be specified as \"y\" and 6 month interval as \"6m\".     If not specified the interval parameter default is 1 Day.
    Boolean historicalfx = true; // Boolean | if true use historical currency rates otherwise current currency rates. Defaults to true.
    String currency = "currency_example"; // String | comma separated list of conversion currencies, defaults to USD
    String unitofmeasure = "mg"; // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<IntervalCollectionResponse> result = apiInstance.metalsSpotHistoryGET(metals, start, end, interval, historicalfx, currency, unitofmeasure, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsSpotHistoryGET");
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
| **metals** | **String**| comma separated list of metals | |
| **start** | **OffsetDateTime**| start date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt; | |
| **end** | **OffsetDateTime**| end date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;. Default is current date. | [optional] |
| **interval** | **String**| aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y&#x3D;year,  m&#x3D;month,  w&#x3D;week,  d&#x3D;day,  h&#x3D;hour,  mi&#x3D;minute    For example, a yearly interval can be specified as \&quot;y\&quot; and 6 month interval as \&quot;6m\&quot;.     If not specified the interval parameter default is 1 Day. | [optional] |
| **historicalfx** | **Boolean**| if true use historical currency rates otherwise current currency rates. Defaults to true. | [optional] |
| **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] |
| **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] [enum: mg, g, kg, gr, oz, toz, ct, dwt] |
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

<a id="metalsSpotRatioHistoryGET"></a>
# **metalsSpotRatioHistoryGET**
> List&lt;IntervalCollectionResponse&gt; metalsSpotRatioHistoryGET(pairs, start, end, interval, format)

Get historical Spot Ratio prices for requested metals

Historical data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String pairs = "pairs_example"; // String | comma separated list of metals
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | start date of time period. format is <i>yyyy-mm-dd</i>
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | end date of time period. format is <i>yyyy-mm-dd</i>. Default is current date.
    String interval = "interval_example"; // String | aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y=year,  m=month,  w=week,  d=day,  h=hour,  mi=minute    For example, a yearly interval can be specified as \"y\" and 6 month interval as \"6m\".     If not specified the interval parameter default is 1 Day.
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<IntervalCollectionResponse> result = apiInstance.metalsSpotRatioHistoryGET(pairs, start, end, interval, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsSpotRatioHistoryGET");
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
| **pairs** | **String**| comma separated list of metals | |
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

<a id="metalsSpotRatioSummaryGET"></a>
# **metalsSpotRatioSummaryGET**
> List&lt;SummaryResponse&gt; metalsSpotRatioSummaryGET(pairs, format)

Get latest Spot Summary for requested metal ratios

Ratios between prices of two metals

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String pairs = "pairs_example"; // String | comma separated list of metal pairs. For example: gold/silver,gold/platinum,silver/palladium
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<SummaryResponse> result = apiInstance.metalsSpotRatioSummaryGET(pairs, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsSpotRatioSummaryGET");
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
| **pairs** | **String**| comma separated list of metal pairs. For example: gold/silver,gold/platinum,silver/palladium | |
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

<a id="metalsSpotSummaryGET"></a>
# **metalsSpotSummaryGET**
> List&lt;SummaryResponse&gt; metalsSpotSummaryGET(metals, currency, unitofmeasure, format)

Get latest Spot Summary for requested metals

Current and daily summary information combined into a single quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String metals = "metals_example"; // String | comma separated list of metals
    String currency = "currency_example"; // String | comma separated list of conversion currencies, defaults to USD
    String unitofmeasure = "mg"; // String | unit of meaure, defaults to troy ounces. allowed values are:  mg=milligram  g=gram  kg=kilogram  gr=grain  oz=ounce  toz=troy ounce  ct=carat  dwt=pennyweight
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<SummaryResponse> result = apiInstance.metalsSpotSummaryGET(metals, currency, unitofmeasure, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsSpotSummaryGET");
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
| **metals** | **String**| comma separated list of metals | |
| **currency** | **String**| comma separated list of conversion currencies, defaults to USD | [optional] |
| **unitofmeasure** | **String**| unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight | [optional] [enum: mg, g, kg, gr, oz, toz, ct, dwt] |
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

<a id="metalsSpotSupportedMetalsGET"></a>
# **metalsSpotSupportedMetalsGET**
> List&lt;String&gt; metalsSpotSupportedMetalsGET(format)

Get list of symbols supported by the spot endpoints



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<String> result = apiInstance.metalsSpotSupportedMetalsGET(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsSpotSupportedMetalsGET");
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

<a id="metalsSupportedCurrenciesMetalsGET"></a>
# **metalsSupportedCurrenciesMetalsGET**
> List&lt;String&gt; metalsSupportedCurrenciesMetalsGET(format)

Get list of currencies supported by metals endpoints for currency conversion



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nfusionsolutions.biz");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    MetalsApi apiInstance = new MetalsApi(defaultClient);
    String format = "json"; // String | to override content negotiation specify a value of json or xml
    try {
      List<String> result = apiInstance.metalsSupportedCurrenciesMetalsGET(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetalsApi#metalsSupportedCurrenciesMetalsGET");
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


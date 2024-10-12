# StatisticsApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDailySettlementStats**](StatisticsApi.md#getDailySettlementStats) | **GET** /api/v1/stats/settlement/daily | Settlement stats over time |
| [**getSettlementStatsByCountry**](StatisticsApi.md#getSettlementStatsByCountry) | **GET** /api/v1/stats/settlement/by_country | Settlement by country |
| [**getSettlementStatsByTaxationType**](StatisticsApi.md#getSettlementStatsByTaxationType) | **GET** /api/v1/stats/settlement/by_taxation_type | Settlement by tax type |
| [**getTransactionsStats**](StatisticsApi.md#getTransactionsStats) | **GET** /api/v1/stats/transactions | Transaction stats |
| [**getTransactionsStatsByCountry**](StatisticsApi.md#getTransactionsStatsByCountry) | **GET** /api/v1/stats/transactions/by_country | Settlement by country |


<a id="getDailySettlementStats"></a>
# **getDailySettlementStats**
> GetDailySettlementStatsOut getDailySettlementStats(interval, dateFrom, dateTo)

Settlement stats over time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    String interval = "interval_example"; // String | Interval type - day, week, month.
    String dateFrom = "dateFrom_example"; // String | Date from in yyyy-MM format.
    String dateTo = "dateTo_example"; // String | Date to in yyyy-MM format.
    try {
      GetDailySettlementStatsOut result = apiInstance.getDailySettlementStats(interval, dateFrom, dateTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getDailySettlementStats");
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
| **interval** | **String**| Interval type - day, week, month. | |
| **dateFrom** | **String**| Date from in yyyy-MM format. | |
| **dateTo** | **String**| Date to in yyyy-MM format. | |

### Return type

[**GetDailySettlementStatsOut**](GetDailySettlementStatsOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="getSettlementStatsByCountry"></a>
# **getSettlementStatsByCountry**
> GetSettlementStatsByCountryOut getSettlementStatsByCountry(dateFrom, dateTo)

Settlement by country

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    String dateFrom = "dateFrom_example"; // String | Date from in yyyy-MM format.
    String dateTo = "dateTo_example"; // String | Date to in yyyy-MM format.
    try {
      GetSettlementStatsByCountryOut result = apiInstance.getSettlementStatsByCountry(dateFrom, dateTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getSettlementStatsByCountry");
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
| **dateFrom** | **String**| Date from in yyyy-MM format. | |
| **dateTo** | **String**| Date to in yyyy-MM format. | |

### Return type

[**GetSettlementStatsByCountryOut**](GetSettlementStatsByCountryOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="getSettlementStatsByTaxationType"></a>
# **getSettlementStatsByTaxationType**
> GetSettlementStatsByTaxationTypeOut getSettlementStatsByTaxationType(dateFrom, dateTo)

Settlement by tax type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    String dateFrom = "dateFrom_example"; // String | Date from in yyyy-MM format.
    String dateTo = "dateTo_example"; // String | Date to in yyyy-MM format.
    try {
      GetSettlementStatsByTaxationTypeOut result = apiInstance.getSettlementStatsByTaxationType(dateFrom, dateTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getSettlementStatsByTaxationType");
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
| **dateFrom** | **String**| Date from in yyyy-MM format. | |
| **dateTo** | **String**| Date to in yyyy-MM format. | |

### Return type

[**GetSettlementStatsByTaxationTypeOut**](GetSettlementStatsByTaxationTypeOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="getTransactionsStats"></a>
# **getTransactionsStats**
> GetTransactionsStatsOut getTransactionsStats(dateFrom, dateTo, interval)

Transaction stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    String dateFrom = "dateFrom_example"; // String | Date from in yyyy-MM format.
    String dateTo = "dateTo_example"; // String | Date to in yyyy-MM format.
    String interval = "interval_example"; // String | Interval. Accepted values are 'day', 'week' and 'month'.
    try {
      GetTransactionsStatsOut result = apiInstance.getTransactionsStats(dateFrom, dateTo, interval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getTransactionsStats");
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
| **dateFrom** | **String**| Date from in yyyy-MM format. | |
| **dateTo** | **String**| Date to in yyyy-MM format. | |
| **interval** | **String**| Interval. Accepted values are &#39;day&#39;, &#39;week&#39; and &#39;month&#39;. | [optional] |

### Return type

[**GetTransactionsStatsOut**](GetTransactionsStatsOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="getTransactionsStatsByCountry"></a>
# **getTransactionsStatsByCountry**
> GetTransactionsStatsByCountryOut getTransactionsStatsByCountry(dateFrom, dateTo, globalCurrencyCode)

Settlement by country

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    String dateFrom = "dateFrom_example"; // String | Date from in yyyy-MM format.
    String dateTo = "dateTo_example"; // String | Date to in yyyy-MM format.
    String globalCurrencyCode = "globalCurrencyCode_example"; // String | Global currency code to use for conversion - in addition to country's currency if rate is available. Conversion is indicative and based on most-recent rate from ECB.
    try {
      GetTransactionsStatsByCountryOut result = apiInstance.getTransactionsStatsByCountry(dateFrom, dateTo, globalCurrencyCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getTransactionsStatsByCountry");
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
| **dateFrom** | **String**| Date from in yyyy-MM format. | |
| **dateTo** | **String**| Date to in yyyy-MM format. | |
| **globalCurrencyCode** | **String**| Global currency code to use for conversion - in addition to country&#39;s currency if rate is available. Conversion is indicative and based on most-recent rate from ECB. | [optional] |

### Return type

[**GetTransactionsStatsByCountryOut**](GetTransactionsStatsByCountryOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |


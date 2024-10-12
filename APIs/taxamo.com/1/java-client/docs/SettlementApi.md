# SettlementApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDetailedRefunds**](SettlementApi.md#getDetailedRefunds) | **GET** /api/v1/settlement/detailed_refunds | Detailed refunds |
| [**getRefunds**](SettlementApi.md#getRefunds) | **GET** /api/v1/settlement/refunds | Fetch refunds |
| [**getSettlement**](SettlementApi.md#getSettlement) | **GET** /api/v1/settlement/{quarter} | Fetch settlement |
| [**getSettlementSummary**](SettlementApi.md#getSettlementSummary) | **GET** /api/v1/settlement/summary/{quarter} | Fetch summary |


<a id="getDetailedRefunds"></a>
# **getDetailedRefunds**
> GetDetailedRefundsOut getDetailedRefunds(format, countryCodes, dateFrom, dateTo, limit, offset)

Detailed refunds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettlementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    SettlementApi apiInstance = new SettlementApi(defaultClient);
    String format = "format_example"; // String | Output format. 'json' or 'csv'. Default value is 'json'
    String countryCodes = "countryCodes_example"; // String | Comma separated list of 2-letter country codes
    String dateFrom = "dateFrom_example"; // String | Take only refunds issued at or after the date. Format: yyyy-MM-dd
    String dateTo = "dateTo_example"; // String | Take only refunds issued at or before the date. Format: yyyy-MM-dd
    BigDecimal limit = new BigDecimal(78); // BigDecimal | Limit (no more than 1000, defaults to 100).
    BigDecimal offset = new BigDecimal(78); // BigDecimal | Offset. Defaults to 0
    try {
      GetDetailedRefundsOut result = apiInstance.getDetailedRefunds(format, countryCodes, dateFrom, dateTo, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettlementApi#getDetailedRefunds");
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
| **format** | **String**| Output format. &#39;json&#39; or &#39;csv&#39;. Default value is &#39;json&#39; | [optional] |
| **countryCodes** | **String**| Comma separated list of 2-letter country codes | [optional] |
| **dateFrom** | **String**| Take only refunds issued at or after the date. Format: yyyy-MM-dd | [optional] |
| **dateTo** | **String**| Take only refunds issued at or before the date. Format: yyyy-MM-dd | [optional] |
| **limit** | **BigDecimal**| Limit (no more than 1000, defaults to 100). | [optional] |
| **offset** | **BigDecimal**| Offset. Defaults to 0 | [optional] |

### Return type

[**GetDetailedRefundsOut**](GetDetailedRefundsOut.md)

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

<a id="getRefunds"></a>
# **getRefunds**
> GetRefundsOut getRefunds(dateFrom, format, mossCountryCode, taxRegion)

Fetch refunds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettlementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    SettlementApi apiInstance = new SettlementApi(defaultClient);
    String dateFrom = "dateFrom_example"; // String | Take only refunds issued at or after the date. Format: yyyy-MM-dd
    String format = "format_example"; // String | Output format. 'csv' value is accepted as well
    String mossCountryCode = "mossCountryCode_example"; // String | MOSS country code, used to determine currency. If ommited, merchant default setting is used.
    String taxRegion = "taxRegion_example"; // String | Tax region key, defaults to EU for backwards compatibility.
    try {
      GetRefundsOut result = apiInstance.getRefunds(dateFrom, format, mossCountryCode, taxRegion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettlementApi#getRefunds");
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
| **dateFrom** | **String**| Take only refunds issued at or after the date. Format: yyyy-MM-dd | |
| **format** | **String**| Output format. &#39;csv&#39; value is accepted as well | [optional] |
| **mossCountryCode** | **String**| MOSS country code, used to determine currency. If ommited, merchant default setting is used. | [optional] |
| **taxRegion** | **String**| Tax region key, defaults to EU for backwards compatibility. | [optional] |

### Return type

[**GetRefundsOut**](GetRefundsOut.md)

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

<a id="getSettlement"></a>
# **getSettlement**
> GetSettlementOut getSettlement(quarter, mossTaxId, currencyCode, endMonth, taxId, refundDateKindOverride, startMonth, mossCountryCode, format, taxCountryCode)

Fetch settlement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettlementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    SettlementApi apiInstance = new SettlementApi(defaultClient);
    String quarter = "quarter_example"; // String | Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to 'range'.
    String mossTaxId = "mossTaxId_example"; // String | MOSS-assigned tax ID - if not provided, merchant's national tax number will be used. Deprecated, please use tax-id.
    String currencyCode = "currencyCode_example"; // String | ISO 3-letter currency code, e.g. EUR or USD. If provided, all amounts will be coerced for this currency. Defaults to region's currency code.
    String endMonth = "endMonth_example"; // String | Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
    String taxId = "taxId_example"; // String | MOSS-assigned tax ID - if not provided, merchant's national tax number will be used. Deprecated, please use tax-id.
    String refundDateKindOverride = "refundDateKindOverride_example"; // String | Set to 'order_date' to show only refunds for the transactions in the selected reporting period. Set to 'refund_timestamp' to show refunds that were created in the selected reporting period. Do not set to use the default region's setting.
    String startMonth = "startMonth_example"; // String | Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
    String mossCountryCode = "mossCountryCode_example"; // String | MOSS country code, used to determine currency/region. If ommited, merchant default setting is used. Deprecated: please use tax-country-code.
    String format = "format_example"; // String | Output format. 'csv' value is accepted as well
    String taxCountryCode = "taxCountryCode_example"; // String | Tax entity country code, used to determine currency/region. 
    try {
      GetSettlementOut result = apiInstance.getSettlement(quarter, mossTaxId, currencyCode, endMonth, taxId, refundDateKindOverride, startMonth, mossCountryCode, format, taxCountryCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettlementApi#getSettlement");
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
| **quarter** | **String**| Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to &#39;range&#39;. | |
| **mossTaxId** | **String**| MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. Deprecated, please use tax-id. | [optional] |
| **currencyCode** | **String**| ISO 3-letter currency code, e.g. EUR or USD. If provided, all amounts will be coerced for this currency. Defaults to region&#39;s currency code. | [optional] |
| **endMonth** | **String**| Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided. | [optional] |
| **taxId** | **String**| MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. Deprecated, please use tax-id. | [optional] |
| **refundDateKindOverride** | **String**| Set to &#39;order_date&#39; to show only refunds for the transactions in the selected reporting period. Set to &#39;refund_timestamp&#39; to show refunds that were created in the selected reporting period. Do not set to use the default region&#39;s setting. | [optional] |
| **startMonth** | **String**| Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided. | [optional] |
| **mossCountryCode** | **String**| MOSS country code, used to determine currency/region. If ommited, merchant default setting is used. Deprecated: please use tax-country-code. | [optional] |
| **format** | **String**| Output format. &#39;csv&#39; value is accepted as well | [optional] |
| **taxCountryCode** | **String**| Tax entity country code, used to determine currency/region.  | [optional] |

### Return type

[**GetSettlementOut**](GetSettlementOut.md)

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

<a id="getSettlementSummary"></a>
# **getSettlementSummary**
> GetSettlementSummaryOut getSettlementSummary(quarter, mossCountryCode, taxRegion, startMonth, endMonth)

Fetch summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettlementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    SettlementApi apiInstance = new SettlementApi(defaultClient);
    String quarter = "quarter_example"; // String | Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to 'range'.
    String mossCountryCode = "mossCountryCode_example"; // String | MOSS country code, used to determine currency. If ommited, merchant default setting is used.
    String taxRegion = "taxRegion_example"; // String | Tax region key
    String startMonth = "startMonth_example"; // String | Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
    String endMonth = "endMonth_example"; // String | Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
    try {
      GetSettlementSummaryOut result = apiInstance.getSettlementSummary(quarter, mossCountryCode, taxRegion, startMonth, endMonth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettlementApi#getSettlementSummary");
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
| **quarter** | **String**| Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to &#39;range&#39;. | |
| **mossCountryCode** | **String**| MOSS country code, used to determine currency. If ommited, merchant default setting is used. | [optional] |
| **taxRegion** | **String**| Tax region key | [optional] |
| **startMonth** | **String**| Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided. | [optional] |
| **endMonth** | **String**| Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided. | [optional] |

### Return type

[**GetSettlementSummaryOut**](GetSettlementSummaryOut.md)

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


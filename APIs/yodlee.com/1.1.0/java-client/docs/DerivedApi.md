# DerivedApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHoldingSummary**](DerivedApi.md#getHoldingSummary) | **GET** /derived/holdingSummary | Get Holding Summary |
| [**getNetworth**](DerivedApi.md#getNetworth) | **GET** /derived/networth | Get Networth Summary |
| [**getTransactionSummary**](DerivedApi.md#getTransactionSummary) | **GET** /derived/transactionSummary | Get Transaction Summary |


<a id="getHoldingSummary"></a>
# **getHoldingSummary**
> DerivedHoldingSummaryResponse getHoldingSummary(accountIds, classificationType, include)

Get Holding Summary

The get holding summary service is used to get the summary of asset classifications for the user.&lt;br&gt;By default, accounts with status as ACTIVE and TO BE CLOSED will be considered.&lt;br&gt;If the include parameter value is passed as details then a summary with holdings and account information is returned.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DerivedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DerivedApi apiInstance = new DerivedApi(defaultClient);
    String accountIds = "accountIds_example"; // String | Comma separated accountIds
    String classificationType = "classificationType_example"; // String | e.g. Country, Sector, etc.
    String include = "include_example"; // String | details
    try {
      DerivedHoldingSummaryResponse result = apiInstance.getHoldingSummary(accountIds, classificationType, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DerivedApi#getHoldingSummary");
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
| **accountIds** | **String**| Comma separated accountIds | [optional] |
| **classificationType** | **String**| e.g. Country, Sector, etc. | [optional] |
| **include** | **String**| details | [optional] |

### Return type

[**DerivedHoldingSummaryResponse**](DerivedHoldingSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for classificationType&lt;br&gt;Y814 : Exchange rate not available for currency&lt;br&gt;Y824 : The maximum number of accountIds permitted is 100&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getNetworth"></a>
# **getNetworth**
> DerivedNetworthResponse getNetworth(accountIds, container, fromDate, include, interval, skip, toDate, top)

Get Networth Summary

The get networth service is used to get the networth for the user.&lt;br&gt;If the include parameter value is passed as details then networth with historical balances is returned. &lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DerivedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DerivedApi apiInstance = new DerivedApi(defaultClient);
    String accountIds = "accountIds_example"; // String | comma separated accountIds
    String container = "container_example"; // String | bank/creditCard/investment/insurance/loan/realEstate/otherAssets/otherLiabilities
    String fromDate = "fromDate_example"; // String | from date for balance retrieval (YYYY-MM-DD)
    String include = "include_example"; // String | details
    String interval = "interval_example"; // String | D-daily, W-weekly or M-monthly
    Integer skip = 56; // Integer | skip (Min 0)
    String toDate = "toDate_example"; // String | toDate for balance retrieval (YYYY-MM-DD)
    Integer top = 56; // Integer | top (Max 500)
    try {
      DerivedNetworthResponse result = apiInstance.getNetworth(accountIds, container, fromDate, include, interval, skip, toDate, top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DerivedApi#getNetworth");
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
| **accountIds** | **String**| comma separated accountIds | [optional] |
| **container** | **String**| bank/creditCard/investment/insurance/loan/realEstate/otherAssets/otherLiabilities | [optional] |
| **fromDate** | **String**| from date for balance retrieval (YYYY-MM-DD) | [optional] |
| **include** | **String**| details | [optional] |
| **interval** | **String**| D-daily, W-weekly or M-monthly | [optional] |
| **skip** | **Integer**| skip (Min 0) | [optional] |
| **toDate** | **String**| toDate for balance retrieval (YYYY-MM-DD) | [optional] |
| **top** | **Integer**| top (Max 500) | [optional] |

### Return type

[**DerivedNetworthResponse**](DerivedNetworthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for accountIds&lt;br&gt;Y800 : Invalid value for fromDate&lt;br&gt;Y800 : Invalid value for toDate&lt;br&gt;Y809 : Invalid date range&lt;br&gt;Y800 : Invalid value for interval&lt;br&gt;Y802 : Future date not allowed&lt;br&gt;Y814 : Exchange rate not available for currency&lt;br&gt;Y800 : Invalid value for container |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getTransactionSummary"></a>
# **getTransactionSummary**
> DerivedTransactionSummaryResponse getTransactionSummary(groupBy, accountId, categoryId, categoryType, fromDate, include, includeUserCategory, interval, toDate)

Get Transaction Summary

The transaction summary service provides the summary values of transactions for the given date range by category type, high-level categories, or system-defined categories.&lt;br&gt;&lt;br&gt;Yodlee has the transaction data stored for a day, month, year and week per category as per the availability of user&#39;s data. If the include parameter value is passed as details, then summary details will be returned depending on the interval passed-monthly is the default.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;ol&gt; &lt;li&gt; Details can be requested for only one system-defined category&lt;li&gt;Passing categoryType is mandatory except when the groupBy value is CATEGORY_TYPE&lt;li&gt;Dates will not be respected for monthly, yearly, and weekly details&lt;li&gt;When monthly details are requested, only the fromDate and toDate month will be respected&lt;li&gt;When yearly details are requested, only the fromDate and toDate year will be respected&lt;li&gt;For weekly data points, details will be provided for every Sunday date available within the fromDate and toDate&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter&lt;/li&gt;&lt;/ol&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DerivedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DerivedApi apiInstance = new DerivedApi(defaultClient);
    String groupBy = "groupBy_example"; // String | CATEGORY_TYPE, HIGH_LEVEL_CATEGORY or CATEGORY
    String accountId = "accountId_example"; // String | comma separated account Ids
    String categoryId = "categoryId_example"; // String | comma separated categoryIds
    String categoryType = "categoryType_example"; // String | INCOME, EXPENSE, TRANSFER, UNCATEGORIZE or DEFERRED_COMPENSATION
    String fromDate = "fromDate_example"; // String | YYYY-MM-DD format
    String include = "include_example"; // String | details
    Boolean includeUserCategory = true; // Boolean | TRUE/FALSE
    String interval = "interval_example"; // String | D-daily, W-weekly, M-mothly or Y-yearly
    String toDate = "toDate_example"; // String | YYYY-MM-DD format
    try {
      DerivedTransactionSummaryResponse result = apiInstance.getTransactionSummary(groupBy, accountId, categoryId, categoryType, fromDate, include, includeUserCategory, interval, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DerivedApi#getTransactionSummary");
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
| **groupBy** | **String**| CATEGORY_TYPE, HIGH_LEVEL_CATEGORY or CATEGORY | |
| **accountId** | **String**| comma separated account Ids | [optional] |
| **categoryId** | **String**| comma separated categoryIds | [optional] |
| **categoryType** | **String**| INCOME, EXPENSE, TRANSFER, UNCATEGORIZE or DEFERRED_COMPENSATION | [optional] |
| **fromDate** | **String**| YYYY-MM-DD format | [optional] |
| **include** | **String**| details | [optional] |
| **includeUserCategory** | **Boolean**| TRUE/FALSE | [optional] |
| **interval** | **String**| D-daily, W-weekly, M-mothly or Y-yearly | [optional] |
| **toDate** | **String**| YYYY-MM-DD format | [optional] |

### Return type

[**DerivedTransactionSummaryResponse**](DerivedTransactionSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y010 : Invalid session&lt;br&gt;Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for groupBy&lt;br&gt;Y803 : groupBy required&lt;br&gt;Y803 : categoryType required&lt;br&gt;Y800 : Invalid value for categoryId&lt;br&gt;Y800 : Invalid value for fromDate&lt;br&gt;Y800 : Invalid value for toDate&lt;br&gt;Y800 : Invalid value for fromDate or toDate&lt;br&gt;Y814 : Exchange rate not available for currency&lt;br&gt;Y815 : Cannot apply filter on categoryId if groupBy value is CATEGORY_TYPE&lt;br&gt;Y816 : User-defined category details can only be requested for one system categoryId with groupBy&#x3D;&#39;CATEGORY&#39;&lt;br&gt;Y824 : The maximum number of accountIds permitted is 100&lt;br&gt;Y824 : The maximum number of categoryIds permitted is 100&lt;br&gt;Y824 : The maximum number of categoryTypes permitted is 100 |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |


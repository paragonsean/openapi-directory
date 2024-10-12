# BudgetingApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersIdBudgetGet**](BudgetingApi.md#usersIdBudgetGet) | **GET** /users/{id}/budget | List budget for user |
| [**usersIdBudgetSummaryGet**](BudgetingApi.md#usersIdBudgetSummaryGet) | **GET** /users/{id}/budget_summary | Get budget summary for user |
| [**usersIdForecastCacheDelete**](BudgetingApi.md#usersIdForecastCacheDelete) | **DELETE** /users/{id}/forecast_cache | Delete forecast cache for user |
| [**usersIdTrendAnalysisGet**](BudgetingApi.md#usersIdTrendAnalysisGet) | **GET** /users/{id}/trend_analysis | Get trend analysis for user |


<a id="usersIdBudgetGet"></a>
# **usersIdBudgetGet**
> List&lt;BudgetAnalysisPackage&gt; usersIdBudgetGet(id, rollUp)

List budget for user

Lists the user&#39;s budget, consisting of one or more budget analysis packages, one per category. Akin to the list on the Budget page in PocketSmith.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    BudgetingApi apiInstance = new BudgetingApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the account.
    Boolean rollUp = true; // Boolean | Whether parent categories should have their children rolled up into them. When used, the children will still appear in the collection on their own, but their actual and forecast figures will be rolled up to the root parent.
    try {
      List<BudgetAnalysisPackage> result = apiInstance.usersIdBudgetGet(id, rollUp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetingApi#usersIdBudgetGet");
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
| **id** | **Integer**| The unique identifier of the account. | |
| **rollUp** | **Boolean**| Whether parent categories should have their children rolled up into them. When used, the children will still appear in the collection on their own, but their actual and forecast figures will be rolled up to the root parent. | [optional] |

### Return type

[**List&lt;BudgetAnalysisPackage&gt;**](BudgetAnalysisPackage.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="usersIdBudgetSummaryGet"></a>
# **usersIdBudgetSummaryGet**
> List&lt;BudgetAnalysisPackage&gt; usersIdBudgetSummaryGet(id, period, interval, startDate, endDate)

Get budget summary for user

Get the user&#39;s budget summary, containing an expense and income analysis for all categories (excluding transfer categories) for the given period and date range. Akin to the overall budget shown on the Budget page in PocketSmith.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    BudgetingApi apiInstance = new BudgetingApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    String period = "weeks"; // String | The period to analyse in, one of `weeks`, `months` or `years`. Also supported is `event`, although event period analysis is only possible when the budget events gathered align, so in this case where all categories are analysed together, it's highly unlikely that event period analysis will be possible.
    Integer interval = 2; // Integer | The period interval, e.g. if the interval is 2 and the period is weeks, the budget will be analysed fortnightly.
    String startDate = "2016-11-01"; // String | The date to start analysing the budget from. This will be bumped out to make full periods as necessary.
    String endDate = "2016-11-30"; // String | The date to stop analysing the budget from. This will be bumped out to make full periods as necessary.
    try {
      List<BudgetAnalysisPackage> result = apiInstance.usersIdBudgetSummaryGet(id, period, interval, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetingApi#usersIdBudgetSummaryGet");
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
| **id** | **Integer**| The unique identifier of the user. | |
| **period** | **String**| The period to analyse in, one of &#x60;weeks&#x60;, &#x60;months&#x60; or &#x60;years&#x60;. Also supported is &#x60;event&#x60;, although event period analysis is only possible when the budget events gathered align, so in this case where all categories are analysed together, it&#39;s highly unlikely that event period analysis will be possible. | [enum: weeks, months, years, event] |
| **interval** | **Integer**| The period interval, e.g. if the interval is 2 and the period is weeks, the budget will be analysed fortnightly. | |
| **startDate** | **String**| The date to start analysing the budget from. This will be bumped out to make full periods as necessary. | |
| **endDate** | **String**| The date to stop analysing the budget from. This will be bumped out to make full periods as necessary. | |

### Return type

[**List&lt;BudgetAnalysisPackage&gt;**](BudgetAnalysisPackage.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="usersIdForecastCacheDelete"></a>
# **usersIdForecastCacheDelete**
> usersIdForecastCacheDelete(id)

Delete forecast cache for user

Delete the user&#39;s cached forecast by recalculating the forecast.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    BudgetingApi apiInstance = new BudgetingApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    try {
      apiInstance.usersIdForecastCacheDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetingApi#usersIdForecastCacheDelete");
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
| **id** | **Integer**| The unique identifier of the user. | |

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="usersIdTrendAnalysisGet"></a>
# **usersIdTrendAnalysisGet**
> List&lt;BudgetAnalysisPackage&gt; usersIdTrendAnalysisGet(id, period, interval, startDate, endDate, categories, scenarios)

Get trend analysis for user

Get an income and/or expense budget analysis for the given date range and period across any number of categories and scenarios. Akin to the Trends page in PocketSmith.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BudgetingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    BudgetingApi apiInstance = new BudgetingApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    String period = "weeks"; // String | The period to analyse in, one of `weeks`, `months` or `years`. Also supported is `event`, although event period analysis is only possible when the budget events gathered align, so in this case where all categories are analysed together, it's highly unlikely that event period analysis will be possible.
    Integer interval = true; // Integer | The period interval, e.g. if the interval is 2 and the period is weeks, the budget will be analysed fortnightly.
    String startDate = "2016-11-01"; // String | The date to start analysing the budget from. This will be bumped out to make full periods as necessary.
    String endDate = "2016-11-30"; // String | The date to stop analysing the budget from. This will be bumped out to make full periods as necessary.
    String categories = "42,49"; // String | A comma-separated list of category IDs to analyse.
    String scenarios = "11,29"; // String | A comma-separated list of scenario IDs to analyse. You're likely going to want to include all a user's scenarios here, unless you have reason to only analyse for a subset of scenarios. Regardless of what scenarios are analysed, all actuals (transactions) across all accounts will be included.
    try {
      List<BudgetAnalysisPackage> result = apiInstance.usersIdTrendAnalysisGet(id, period, interval, startDate, endDate, categories, scenarios);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BudgetingApi#usersIdTrendAnalysisGet");
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
| **id** | **Integer**| The unique identifier of the user. | |
| **period** | **String**| The period to analyse in, one of &#x60;weeks&#x60;, &#x60;months&#x60; or &#x60;years&#x60;. Also supported is &#x60;event&#x60;, although event period analysis is only possible when the budget events gathered align, so in this case where all categories are analysed together, it&#39;s highly unlikely that event period analysis will be possible. | [enum: weeks, months, years, event] |
| **interval** | **Integer**| The period interval, e.g. if the interval is 2 and the period is weeks, the budget will be analysed fortnightly. | |
| **startDate** | **String**| The date to start analysing the budget from. This will be bumped out to make full periods as necessary. | |
| **endDate** | **String**| The date to stop analysing the budget from. This will be bumped out to make full periods as necessary. | |
| **categories** | **String**| A comma-separated list of category IDs to analyse. | |
| **scenarios** | **String**| A comma-separated list of scenario IDs to analyse. You&#39;re likely going to want to include all a user&#39;s scenarios here, unless you have reason to only analyse for a subset of scenarios. Regardless of what scenarios are analysed, all actuals (transactions) across all accounts will be included. | |

### Return type

[**List&lt;BudgetAnalysisPackage&gt;**](BudgetAnalysisPackage.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |


# FinancialsApi

All URIs are relative to *https://api.exhibitday.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**financialsEventCosts0Get**](FinancialsApi.md#financialsEventCosts0Get) | **GET** /v1/financials/event_costs |  |
| [**financialsMiscAnnualExpenseCosts0Get**](FinancialsApi.md#financialsMiscAnnualExpenseCosts0Get) | **GET** /v1/financials/misc_annual_expense_costs |  |


<a id="financialsEventCosts0Get"></a>
# **financialsEventCosts0Get**
> String financialsEventCosts0Get(apiKey, filterByEventId, filterByEventStartDateGreaterThanOrEqualTo, filterByEventStartDateSmallerThanOrEqualTo, filterByEventEndDateGreaterThanOrEqualTo, filterByEventEndDateSmallerThanOrEqualTo)



Retrieve event costs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    FinancialsApi apiInstance = new FinancialsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal filterByEventId = new BigDecimal(78); // BigDecimal | Id of a specific event that you would like to retrieve costs for.
    LocalDate filterByEventStartDateGreaterThanOrEqualTo = LocalDate.now(); // LocalDate | Only include costs for events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    LocalDate filterByEventStartDateSmallerThanOrEqualTo = LocalDate.now(); // LocalDate | Only include costs for events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    LocalDate filterByEventEndDateGreaterThanOrEqualTo = LocalDate.now(); // LocalDate | Only include costs for events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    LocalDate filterByEventEndDateSmallerThanOrEqualTo = LocalDate.now(); // LocalDate | Only include costs for events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
    try {
      String result = apiInstance.financialsEventCosts0Get(apiKey, filterByEventId, filterByEventStartDateGreaterThanOrEqualTo, filterByEventStartDateSmallerThanOrEqualTo, filterByEventEndDateGreaterThanOrEqualTo, filterByEventEndDateSmallerThanOrEqualTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialsApi#financialsEventCosts0Get");
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
| **apiKey** | **String**|  | |
| **filterByEventId** | **BigDecimal**| Id of a specific event that you would like to retrieve costs for. | [optional] |
| **filterByEventStartDateGreaterThanOrEqualTo** | **LocalDate**| Only include costs for events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] |
| **filterByEventStartDateSmallerThanOrEqualTo** | **LocalDate**| Only include costs for events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] |
| **filterByEventEndDateGreaterThanOrEqualTo** | **LocalDate**| Only include costs for events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] |
| **filterByEventEndDateSmallerThanOrEqualTo** | **LocalDate**| Only include costs for events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="financialsMiscAnnualExpenseCosts0Get"></a>
# **financialsMiscAnnualExpenseCosts0Get**
> String financialsMiscAnnualExpenseCosts0Get(apiKey, budgetYear)



Retrieve Miscellaneous Annual Expense Costs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exhibitday.com");

    FinancialsApi apiInstance = new FinancialsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    BigDecimal budgetYear = new BigDecimal(78); // BigDecimal | The specific budget year that you would like to retrieve miscellaneous annual expense costs for (e.g., 2023).
    try {
      String result = apiInstance.financialsMiscAnnualExpenseCosts0Get(apiKey, budgetYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialsApi#financialsMiscAnnualExpenseCosts0Get");
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
| **apiKey** | **String**|  | |
| **budgetYear** | **BigDecimal**| The specific budget year that you would like to retrieve miscellaneous annual expense costs for (e.g., 2023). | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


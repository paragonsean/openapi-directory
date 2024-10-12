# SalesRulesSearchApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRuleRuleRepositoryV1GetListGet**](SalesRulesSearchApi.md#salesRuleRuleRepositoryV1GetListGet) | **GET** /V1/salesRules/search | salesRules/search |


<a id="salesRuleRuleRepositoryV1GetListGet"></a>
# **salesRuleRuleRepositoryV1GetListGet**
> SalesRuleDataRuleSearchResultInterface salesRuleRuleRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage)

salesRules/search

Retrieve sales rules that match te specified criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#RuleRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRulesSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SalesRulesSearchApi apiInstance = new SalesRulesSearchApi(defaultClient);
    String searchCriteriaFilterGroups0Filters0Field = "searchCriteriaFilterGroups0Filters0Field_example"; // String | Field
    String searchCriteriaFilterGroups0Filters0Value = "searchCriteriaFilterGroups0Filters0Value_example"; // String | Value
    String searchCriteriaFilterGroups0Filters0ConditionType = "searchCriteriaFilterGroups0Filters0ConditionType_example"; // String | Condition type
    String searchCriteriaSortOrders0Field = "searchCriteriaSortOrders0Field_example"; // String | Sorting field.
    String searchCriteriaSortOrders0Direction = "searchCriteriaSortOrders0Direction_example"; // String | Sorting direction.
    Integer searchCriteriaPageSize = 56; // Integer | Page size.
    Integer searchCriteriaCurrentPage = 56; // Integer | Current page.
    try {
      SalesRuleDataRuleSearchResultInterface result = apiInstance.salesRuleRuleRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRulesSearchApi#salesRuleRuleRepositoryV1GetListGet");
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
| **searchCriteriaFilterGroups0Filters0Field** | **String**| Field | [optional] |
| **searchCriteriaFilterGroups0Filters0Value** | **String**| Value | [optional] |
| **searchCriteriaFilterGroups0Filters0ConditionType** | **String**| Condition type | [optional] |
| **searchCriteriaSortOrders0Field** | **String**| Sorting field. | [optional] |
| **searchCriteriaSortOrders0Direction** | **String**| Sorting direction. | [optional] |
| **searchCriteriaPageSize** | **Integer**| Page size. | [optional] |
| **searchCriteriaCurrentPage** | **Integer**| Current page. | [optional] |

### Return type

[**SalesRuleDataRuleSearchResultInterface**](SalesRuleDataRuleSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |


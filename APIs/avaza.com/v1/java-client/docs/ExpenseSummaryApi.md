# ExpenseSummaryApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expenseSummaryGet**](ExpenseSummaryApi.md#expenseSummaryGet) | **GET** /api/ExpenseSummary | Gets Basic Summary of Expense Statistics |


<a id="expenseSummaryGet"></a>
# **expenseSummaryGet**
> ExpenseSummaryResult expenseSummaryGet(modelGroupBy, modelExpenseDateFrom, modelExpenseDateTo, modelUserID, modelProjectID)

Gets Basic Summary of Expense Statistics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseSummaryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpenseSummaryApi apiInstance = new ExpenseSummaryApi(defaultClient);
    List<String> modelGroupBy = Arrays.asList(); // List<String> | (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \"Category\", \"ChargeableStatus\", \"Merchant\", \"ApprovalStatus\", \"ReimbursementStatus\", \"Customer\", \"Project\", \"User\", \"Task\", \"Year\", \"Month\", \"Day\", \"Week\".
    OffsetDateTime modelExpenseDateFrom = OffsetDateTime.now(); // OffsetDateTime | (Required) Filter for expenses with expense dates greater or equal to the specified date. e.g. 2019-01-25.
    OffsetDateTime modelExpenseDateTo = OffsetDateTime.now(); // OffsetDateTime | (Required) Filter for expenses with an expense date smaller or equal to the specified  date. e.g. 2019-01-25.
    List<Integer> modelUserID = Arrays.asList(); // List<Integer> | (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose expenses should be retrieved. If the current user doesn't have impersonation rights, then they will only see their own data.
    Integer modelProjectID = 56; // Integer | (Optional) Filter by Project
    try {
      ExpenseSummaryResult result = apiInstance.expenseSummaryGet(modelGroupBy, modelExpenseDateFrom, modelExpenseDateTo, modelUserID, modelProjectID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseSummaryApi#expenseSummaryGet");
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
| **modelGroupBy** | [**List&lt;String&gt;**](String.md)| (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \&quot;Category\&quot;, \&quot;ChargeableStatus\&quot;, \&quot;Merchant\&quot;, \&quot;ApprovalStatus\&quot;, \&quot;ReimbursementStatus\&quot;, \&quot;Customer\&quot;, \&quot;Project\&quot;, \&quot;User\&quot;, \&quot;Task\&quot;, \&quot;Year\&quot;, \&quot;Month\&quot;, \&quot;Day\&quot;, \&quot;Week\&quot;. | [optional] |
| **modelExpenseDateFrom** | **OffsetDateTime**| (Required) Filter for expenses with expense dates greater or equal to the specified date. e.g. 2019-01-25. | [optional] |
| **modelExpenseDateTo** | **OffsetDateTime**| (Required) Filter for expenses with an expense date smaller or equal to the specified  date. e.g. 2019-01-25. | [optional] |
| **modelUserID** | [**List&lt;Integer&gt;**](Integer.md)| (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose expenses should be retrieved. If the current user doesn&#39;t have impersonation rights, then they will only see their own data. | [optional] |
| **modelProjectID** | **Integer**| (Optional) Filter by Project | [optional] |

### Return type

[**ExpenseSummaryResult**](ExpenseSummaryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


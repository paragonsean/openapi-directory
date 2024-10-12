# StatementsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStatements**](StatementsApi.md#getStatements) | **GET** /statements | Get Statements |


<a id="getStatements"></a>
# **getStatements**
> StatementResponse getStatements(accountId, container, fromDate, isLatest, status)

Get Statements

The statements service is used to get the list of statement related information. &lt;br&gt;By default, all the latest statements of active and to be closed accounts are retrieved for the user. &lt;br&gt;Certain sites do not have both a statement date and a due date. When a fromDate is passed as an input, all the statements that have the due date on or after the passed date are retrieved. &lt;br&gt;For sites that do not have the due date, statements that have the statement date on or after the passed date are retrieved. &lt;br&gt;The default value of \&quot;isLatest\&quot; is true. To retrieve historical statements isLatest needs to be set to false.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StatementsApi apiInstance = new StatementsApi(defaultClient);
    String accountId = "accountId_example"; // String | accountId
    String container = "container_example"; // String | creditCard/loan/insurance
    String fromDate = "fromDate_example"; // String | from date for statement retrieval (YYYY-MM-DD)
    String isLatest = "isLatest_example"; // String | isLatest (true/false)
    String status = "status_example"; // String | ACTIVE,TO_BE_CLOSED,CLOSED
    try {
      StatementResponse result = apiInstance.getStatements(accountId, container, fromDate, isLatest, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatementsApi#getStatements");
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
| **accountId** | **String**| accountId | [optional] |
| **container** | **String**| creditCard/loan/insurance | [optional] |
| **fromDate** | **String**| from date for statement retrieval (YYYY-MM-DD) | [optional] |
| **isLatest** | **String**| isLatest (true/false) | [optional] |
| **status** | **String**| ACTIVE,TO_BE_CLOSED,CLOSED | [optional] |

### Return type

[**StatementResponse**](StatementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for status&lt;br&gt;Y805 : Multiple containers not supported&lt;br&gt;Y800 : Invalid value for container&lt;br&gt;Y800 : Invalid value for isLatest&lt;br&gt;Y800 : Invalid value for fromDate&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |


# AmendmentsApi

All URIs are relative to *https://bills-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAmendment**](AmendmentsApi.md#getAmendment) | **GET** /api/v1/Bills/{billId}/Stages/{billStageId}/Amendments/{amendmentId} | Returns an amendment. |
| [**getAmendments**](AmendmentsApi.md#getAmendments) | **GET** /api/v1/Bills/{billId}/Stages/{billStageId}/Amendments | Returns a list of amendments. |


<a id="getAmendment"></a>
# **getAmendment**
> AmendmentDetail getAmendment(billId, billStageId, amendmentId)

Returns an amendment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AmendmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    AmendmentsApi apiInstance = new AmendmentsApi(defaultClient);
    Integer billId = 56; // Integer | Amendment relating to a bill with bill ID specified
    Integer billStageId = 56; // Integer | Amendment relating to a bill stage with bill stage ID specified
    Integer amendmentId = 56; // Integer | Amendment with amendment ID specified
    try {
      AmendmentDetail result = apiInstance.getAmendment(billId, billStageId, amendmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AmendmentsApi#getAmendment");
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
| **billId** | **Integer**| Amendment relating to a bill with bill ID specified | |
| **billStageId** | **Integer**| Amendment relating to a bill stage with bill stage ID specified | |
| **amendmentId** | **Integer**| Amendment with amendment ID specified | |

### Return type

[**AmendmentDetail**](AmendmentDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="getAmendments"></a>
# **getAmendments**
> AmendmentSearchItemSearchResult getAmendments(billId, billStageId, searchTerm, decision, memberId, skip, take)

Returns a list of amendments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AmendmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    AmendmentsApi apiInstance = new AmendmentsApi(defaultClient);
    Integer billId = 56; // Integer | Amendments relating to a Bill with Bill ID specified
    Integer billStageId = 56; // Integer | Amendments relating to a Bill stage with Bill stage ID specified
    String searchTerm = "searchTerm_example"; // String | 
    Decision decision = Decision.fromValue("All"); // Decision | 
    Integer memberId = 56; // Integer | 
    Integer skip = 56; // Integer | 
    Integer take = 56; // Integer | 
    try {
      AmendmentSearchItemSearchResult result = apiInstance.getAmendments(billId, billStageId, searchTerm, decision, memberId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AmendmentsApi#getAmendments");
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
| **billId** | **Integer**| Amendments relating to a Bill with Bill ID specified | |
| **billStageId** | **Integer**| Amendments relating to a Bill stage with Bill stage ID specified | |
| **searchTerm** | **String**|  | [optional] |
| **decision** | [**Decision**](.md)|  | [optional] [enum: All, NoDecision, Withdrawn, Disagreed, NotMoved, Agreed] |
| **memberId** | **Integer**|  | [optional] |
| **skip** | **Integer**|  | [optional] |
| **take** | **Integer**|  | [optional] |

### Return type

[**AmendmentSearchItemSearchResult**](AmendmentSearchItemSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |


# BillsApi

All URIs are relative to *https://bills-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1BillsBillIdStagesGet**](BillsApi.md#apiV1BillsBillIdStagesGet) | **GET** /api/v1/Bills/{billId}/Stages | Returns all Bill stages. |
| [**getBill**](BillsApi.md#getBill) | **GET** /api/v1/Bills/{billId} | Return a Bill. |
| [**getBillStageDetails**](BillsApi.md#getBillStageDetails) | **GET** /api/v1/Bills/{billId}/Stages/{billStageId} | Returns a Bill stage. |
| [**getBills**](BillsApi.md#getBills) | **GET** /api/v1/Bills | Returns a list of Bills. |


<a id="apiV1BillsBillIdStagesGet"></a>
# **apiV1BillsBillIdStagesGet**
> StageSummarySearchResult apiV1BillsBillIdStagesGet(billId, skip, take)

Returns all Bill stages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    BillsApi apiInstance = new BillsApi(defaultClient);
    Integer billId = 56; // Integer | Stages relating to a Bill with Bill ID specified
    Integer skip = 56; // Integer | 
    Integer take = 56; // Integer | 
    try {
      StageSummarySearchResult result = apiInstance.apiV1BillsBillIdStagesGet(billId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillsApi#apiV1BillsBillIdStagesGet");
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
| **billId** | **Integer**| Stages relating to a Bill with Bill ID specified | |
| **skip** | **Integer**|  | [optional] |
| **take** | **Integer**|  | [optional] |

### Return type

[**StageSummarySearchResult**](StageSummarySearchResult.md)

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

<a id="getBill"></a>
# **getBill**
> Bill getBill(billId)

Return a Bill.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    BillsApi apiInstance = new BillsApi(defaultClient);
    Integer billId = 56; // Integer | Bill with ID specified
    try {
      Bill result = apiInstance.getBill(billId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillsApi#getBill");
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
| **billId** | **Integer**| Bill with ID specified | |

### Return type

[**Bill**](Bill.md)

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

<a id="getBillStageDetails"></a>
# **getBillStageDetails**
> BillStageDetails getBillStageDetails(billId, billStageId)

Returns a Bill stage.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    BillsApi apiInstance = new BillsApi(defaultClient);
    Integer billId = 56; // Integer | Bill stage relating to Bill with Bill ID specified
    Integer billStageId = 56; // Integer | Bill stage with ID specified
    try {
      BillStageDetails result = apiInstance.getBillStageDetails(billId, billStageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillsApi#getBillStageDetails");
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
| **billId** | **Integer**| Bill stage relating to Bill with Bill ID specified | |
| **billStageId** | **Integer**| Bill stage with ID specified | |

### Return type

[**BillStageDetails**](BillStageDetails.md)

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

<a id="getBills"></a>
# **getBills**
> BillSummarySearchResult getBills(searchTerm, session, currentHouse, originatingHouse, memberId, departmentId, billStage, billStagesExcluded, isDefeated, isWithdrawn, billType, sortOrder, billIds, skip, take)

Returns a list of Bills.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    BillsApi apiInstance = new BillsApi(defaultClient);
    String searchTerm = "searchTerm_example"; // String | 
    Integer session = 56; // Integer | 
    House currentHouse = House.fromValue("All"); // House | 
    OriginatingHouse originatingHouse = OriginatingHouse.fromValue("All"); // OriginatingHouse | 
    Integer memberId = 56; // Integer | 
    Integer departmentId = 56; // Integer | 
    List<Integer> billStage = Arrays.asList(); // List<Integer> | 
    List<Integer> billStagesExcluded = Arrays.asList(); // List<Integer> | 
    Boolean isDefeated = true; // Boolean | 
    Boolean isWithdrawn = true; // Boolean | 
    List<Integer> billType = Arrays.asList(); // List<Integer> | 
    BillSortOrder sortOrder = BillSortOrder.fromValue("TitleAscending"); // BillSortOrder | 
    List<Integer> billIds = Arrays.asList(); // List<Integer> | 
    Integer skip = 56; // Integer | 
    Integer take = 56; // Integer | 
    try {
      BillSummarySearchResult result = apiInstance.getBills(searchTerm, session, currentHouse, originatingHouse, memberId, departmentId, billStage, billStagesExcluded, isDefeated, isWithdrawn, billType, sortOrder, billIds, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillsApi#getBills");
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
| **searchTerm** | **String**|  | [optional] |
| **session** | **Integer**|  | [optional] |
| **currentHouse** | [**House**](.md)|  | [optional] [enum: All, Commons, Lords, Unassigned] |
| **originatingHouse** | [**OriginatingHouse**](.md)|  | [optional] [enum: All, Commons, Lords] |
| **memberId** | **Integer**|  | [optional] |
| **departmentId** | **Integer**|  | [optional] |
| **billStage** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **billStagesExcluded** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **isDefeated** | **Boolean**|  | [optional] |
| **isWithdrawn** | **Boolean**|  | [optional] |
| **billType** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **sortOrder** | [**BillSortOrder**](.md)|  | [optional] [enum: TitleAscending, TitleDescending, DateUpdatedAscending, DateUpdatedDescending] |
| **billIds** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **skip** | **Integer**|  | [optional] |
| **take** | **Integer**|  | [optional] |

### Return type

[**BillSummarySearchResult**](BillSummarySearchResult.md)

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


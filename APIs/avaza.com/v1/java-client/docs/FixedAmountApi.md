# FixedAmountApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fixedAmountGet**](FixedAmountApi.md#fixedAmountGet) | **GET** /api/FixedAmount | Gets list of Fixed Amounts |


<a id="fixedAmountGet"></a>
# **fixedAmountGet**
> FixedAmountList fixedAmountGet(updatedAfter, entryDateFrom, entryDateTo, projectID, taskID, isInvoiced, pageSize, pageNumber, sort)

Gets list of Fixed Amounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FixedAmountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    FixedAmountApi apiInstance = new FixedAmountApi(defaultClient);
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime entryDateFrom = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime entryDateTo = OffsetDateTime.now(); // OffsetDateTime | 
    Integer projectID = 56; // Integer | (Optional) The ProjectID of a Project to filter Fixed Amounts for
    Integer taskID = 56; // Integer | (Optional) The TaskID of a Task to filter Fixed Amounts for
    Boolean isInvoiced = true; // Boolean | 
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    String sort = "sort_example"; // String | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\",\"EntryDate\", \"EntryDate desc\", \"StartTimeLocal\",\"StartTimeLocal desc\", \"TimeSheetEntryID\", \"TimeSheetEntryID desc\"
    try {
      FixedAmountList result = apiInstance.fixedAmountGet(updatedAfter, entryDateFrom, entryDateTo, projectID, taskID, isInvoiced, pageSize, pageNumber, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FixedAmountApi#fixedAmountGet");
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
| **updatedAfter** | **OffsetDateTime**|  | [optional] |
| **entryDateFrom** | **OffsetDateTime**|  | [optional] |
| **entryDateTo** | **OffsetDateTime**|  | [optional] |
| **projectID** | **Integer**| (Optional) The ProjectID of a Project to filter Fixed Amounts for | [optional] |
| **taskID** | **Integer**| (Optional) The TaskID of a Task to filter Fixed Amounts for | [optional] |
| **isInvoiced** | **Boolean**|  | [optional] |
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |
| **sort** | **String**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;,\&quot;EntryDate\&quot;, \&quot;EntryDate desc\&quot;, \&quot;StartTimeLocal\&quot;,\&quot;StartTimeLocal desc\&quot;, \&quot;TimeSheetEntryID\&quot;, \&quot;TimeSheetEntryID desc\&quot; | [optional] |

### Return type

[**FixedAmountList**](FixedAmountList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |


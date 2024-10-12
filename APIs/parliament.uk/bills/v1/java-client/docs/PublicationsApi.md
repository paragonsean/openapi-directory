# PublicationsApi

All URIs are relative to *https://bills-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1BillsBillIdStagesStageIdPublicationsGet**](PublicationsApi.md#apiV1BillsBillIdStagesStageIdPublicationsGet) | **GET** /api/v1/Bills/{billId}/Stages/{stageId}/Publications | Return a list of Bill stage publications. |
| [**getBillPublication**](PublicationsApi.md#getBillPublication) | **GET** /api/v1/Bills/{billId}/Publications | Return a list of Bill publications. |


<a id="apiV1BillsBillIdStagesStageIdPublicationsGet"></a>
# **apiV1BillsBillIdStagesStageIdPublicationsGet**
> BillStagePublicationList apiV1BillsBillIdStagesStageIdPublicationsGet(billId, stageId)

Return a list of Bill stage publications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    PublicationsApi apiInstance = new PublicationsApi(defaultClient);
    Integer billId = 56; // Integer | 
    Integer stageId = 56; // Integer | 
    try {
      BillStagePublicationList result = apiInstance.apiV1BillsBillIdStagesStageIdPublicationsGet(billId, stageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicationsApi#apiV1BillsBillIdStagesStageIdPublicationsGet");
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
| **billId** | **Integer**|  | |
| **stageId** | **Integer**|  | |

### Return type

[**BillStagePublicationList**](BillStagePublicationList.md)

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

<a id="getBillPublication"></a>
# **getBillPublication**
> BillPublicationList getBillPublication(billId)

Return a list of Bill publications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    PublicationsApi apiInstance = new PublicationsApi(defaultClient);
    Integer billId = 56; // Integer | Publications relating to Bill with Bill ID specified
    try {
      BillPublicationList result = apiInstance.getBillPublication(billId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicationsApi#getBillPublication");
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
| **billId** | **Integer**| Publications relating to Bill with Bill ID specified | |

### Return type

[**BillPublicationList**](BillPublicationList.md)

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


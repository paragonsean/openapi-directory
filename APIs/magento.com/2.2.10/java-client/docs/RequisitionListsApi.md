# RequisitionListsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**requisitionListRequisitionListRepositoryV1SavePost**](RequisitionListsApi.md#requisitionListRequisitionListRepositoryV1SavePost) | **POST** /V1/requisition_lists | requisition_lists |


<a id="requisitionListRequisitionListRepositoryV1SavePost"></a>
# **requisitionListRequisitionListRepositoryV1SavePost**
> RequisitionListDataRequisitionListInterface requisitionListRequisitionListRepositoryV1SavePost(requisitionListRequisitionListRepositoryV1SavePostRequest)

requisition_lists

Save Requisition List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequisitionListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    RequisitionListsApi apiInstance = new RequisitionListsApi(defaultClient);
    RequisitionListRequisitionListRepositoryV1SavePostRequest requisitionListRequisitionListRepositoryV1SavePostRequest = new RequisitionListRequisitionListRepositoryV1SavePostRequest(); // RequisitionListRequisitionListRepositoryV1SavePostRequest | 
    try {
      RequisitionListDataRequisitionListInterface result = apiInstance.requisitionListRequisitionListRepositoryV1SavePost(requisitionListRequisitionListRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequisitionListsApi#requisitionListRequisitionListRepositoryV1SavePost");
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
| **requisitionListRequisitionListRepositoryV1SavePostRequest** | [**RequisitionListRequisitionListRepositoryV1SavePostRequest**](RequisitionListRequisitionListRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**RequisitionListDataRequisitionListInterface**](RequisitionListDataRequisitionListInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |


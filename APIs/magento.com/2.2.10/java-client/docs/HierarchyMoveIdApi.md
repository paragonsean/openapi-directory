# HierarchyMoveIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyCompanyHierarchyV1MoveNodePut**](HierarchyMoveIdApi.md#companyCompanyHierarchyV1MoveNodePut) | **PUT** /V1/hierarchy/move/{id} | hierarchy/move/{id} |


<a id="companyCompanyHierarchyV1MoveNodePut"></a>
# **companyCompanyHierarchyV1MoveNodePut**
> ErrorResponse companyCompanyHierarchyV1MoveNodePut(id, companyCompanyHierarchyV1MoveNodePutRequest)

hierarchy/move/{id}

Moves teams and users within the company structure.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HierarchyMoveIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    HierarchyMoveIdApi apiInstance = new HierarchyMoveIdApi(defaultClient);
    Integer id = 56; // Integer | 
    CompanyCompanyHierarchyV1MoveNodePutRequest companyCompanyHierarchyV1MoveNodePutRequest = new CompanyCompanyHierarchyV1MoveNodePutRequest(); // CompanyCompanyHierarchyV1MoveNodePutRequest | 
    try {
      ErrorResponse result = apiInstance.companyCompanyHierarchyV1MoveNodePut(id, companyCompanyHierarchyV1MoveNodePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HierarchyMoveIdApi#companyCompanyHierarchyV1MoveNodePut");
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
| **id** | **Integer**|  | |
| **companyCompanyHierarchyV1MoveNodePutRequest** | [**CompanyCompanyHierarchyV1MoveNodePutRequest**](CompanyCompanyHierarchyV1MoveNodePutRequest.md)|  | [optional] |

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |


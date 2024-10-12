# HierarchyIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyCompanyHierarchyV1GetCompanyHierarchyGet**](HierarchyIdApi.md#companyCompanyHierarchyV1GetCompanyHierarchyGet) | **GET** /V1/hierarchy/{id} | hierarchy/{id} |


<a id="companyCompanyHierarchyV1GetCompanyHierarchyGet"></a>
# **companyCompanyHierarchyV1GetCompanyHierarchyGet**
> List&lt;CompanyDataHierarchyInterface&gt; companyCompanyHierarchyV1GetCompanyHierarchyGet(id)

hierarchy/{id}

Returns the list of teams and company users in the company structure.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HierarchyIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    HierarchyIdApi apiInstance = new HierarchyIdApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      List<CompanyDataHierarchyInterface> result = apiInstance.companyCompanyHierarchyV1GetCompanyHierarchyGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HierarchyIdApi#companyCompanyHierarchyV1GetCompanyHierarchyGet");
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

### Return type

[**List&lt;CompanyDataHierarchyInterface&gt;**](CompanyDataHierarchyInterface.md)

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
| **0** | Unexpected error |  -  |


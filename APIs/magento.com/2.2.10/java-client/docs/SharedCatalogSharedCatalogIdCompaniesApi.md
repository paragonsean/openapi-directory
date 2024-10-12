# SharedCatalogSharedCatalogIdCompaniesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedCatalogCompanyManagementV1GetCompaniesGet**](SharedCatalogSharedCatalogIdCompaniesApi.md#sharedCatalogCompanyManagementV1GetCompaniesGet) | **GET** /V1/sharedCatalog/{sharedCatalogId}/companies | sharedCatalog/{sharedCatalogId}/companies |


<a id="sharedCatalogCompanyManagementV1GetCompaniesGet"></a>
# **sharedCatalogCompanyManagementV1GetCompaniesGet**
> String sharedCatalogCompanyManagementV1GetCompaniesGet(sharedCatalogId)

sharedCatalog/{sharedCatalogId}/companies

Return the list of company IDs for the companies assigned to the selected catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogSharedCatalogIdCompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogSharedCatalogIdCompaniesApi apiInstance = new SharedCatalogSharedCatalogIdCompaniesApi(defaultClient);
    Integer sharedCatalogId = 56; // Integer | 
    try {
      String result = apiInstance.sharedCatalogCompanyManagementV1GetCompaniesGet(sharedCatalogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogSharedCatalogIdCompaniesApi#sharedCatalogCompanyManagementV1GetCompaniesGet");
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
| **sharedCatalogId** | **Integer**|  | |

### Return type

**String**

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


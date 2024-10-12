# SharedCatalogSharedCatalogIdAssignCompaniesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedCatalogCompanyManagementV1AssignCompaniesPost**](SharedCatalogSharedCatalogIdAssignCompaniesApi.md#sharedCatalogCompanyManagementV1AssignCompaniesPost) | **POST** /V1/sharedCatalog/{sharedCatalogId}/assignCompanies | sharedCatalog/{sharedCatalogId}/assignCompanies |


<a id="sharedCatalogCompanyManagementV1AssignCompaniesPost"></a>
# **sharedCatalogCompanyManagementV1AssignCompaniesPost**
> Boolean sharedCatalogCompanyManagementV1AssignCompaniesPost(sharedCatalogId, sharedCatalogCompanyManagementV1AssignCompaniesPostRequest)

sharedCatalog/{sharedCatalogId}/assignCompanies

Assign companies to a shared catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogSharedCatalogIdAssignCompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogSharedCatalogIdAssignCompaniesApi apiInstance = new SharedCatalogSharedCatalogIdAssignCompaniesApi(defaultClient);
    Integer sharedCatalogId = 56; // Integer | 
    SharedCatalogCompanyManagementV1AssignCompaniesPostRequest sharedCatalogCompanyManagementV1AssignCompaniesPostRequest = new SharedCatalogCompanyManagementV1AssignCompaniesPostRequest(); // SharedCatalogCompanyManagementV1AssignCompaniesPostRequest | 
    try {
      Boolean result = apiInstance.sharedCatalogCompanyManagementV1AssignCompaniesPost(sharedCatalogId, sharedCatalogCompanyManagementV1AssignCompaniesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogSharedCatalogIdAssignCompaniesApi#sharedCatalogCompanyManagementV1AssignCompaniesPost");
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
| **sharedCatalogCompanyManagementV1AssignCompaniesPostRequest** | [**SharedCatalogCompanyManagementV1AssignCompaniesPostRequest**](SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |


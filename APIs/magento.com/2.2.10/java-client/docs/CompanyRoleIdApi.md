# CompanyRoleIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyRoleRepositoryV1SavePut**](CompanyRoleIdApi.md#companyRoleRepositoryV1SavePut) | **PUT** /V1/company/role/{id} | company/role/{id} |


<a id="companyRoleRepositoryV1SavePut"></a>
# **companyRoleRepositoryV1SavePut**
> CompanyDataRoleInterface companyRoleRepositoryV1SavePut(id, companyRoleRepositoryV1SavePostRequest)

company/role/{id}

Create or update a role for a selected company.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyRoleIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyRoleIdApi apiInstance = new CompanyRoleIdApi(defaultClient);
    String id = "id_example"; // String | 
    CompanyRoleRepositoryV1SavePostRequest companyRoleRepositoryV1SavePostRequest = new CompanyRoleRepositoryV1SavePostRequest(); // CompanyRoleRepositoryV1SavePostRequest | 
    try {
      CompanyDataRoleInterface result = apiInstance.companyRoleRepositoryV1SavePut(id, companyRoleRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyRoleIdApi#companyRoleRepositoryV1SavePut");
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
| **id** | **String**|  | |
| **companyRoleRepositoryV1SavePostRequest** | [**CompanyRoleRepositoryV1SavePostRequest**](CompanyRoleRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**CompanyDataRoleInterface**](CompanyDataRoleInterface.md)

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


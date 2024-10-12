# CompanyRoleRoleIdUsersApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyAclV1GetUsersByRoleIdGet**](CompanyRoleRoleIdUsersApi.md#companyAclV1GetUsersByRoleIdGet) | **GET** /V1/company/role/{roleId}/users | company/role/{roleId}/users |


<a id="companyAclV1GetUsersByRoleIdGet"></a>
# **companyAclV1GetUsersByRoleIdGet**
> List&lt;CustomerDataCustomerInterface&gt; companyAclV1GetUsersByRoleIdGet(roleId)

company/role/{roleId}/users

View the list of company users assigned to a specified role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyRoleRoleIdUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyRoleRoleIdUsersApi apiInstance = new CompanyRoleRoleIdUsersApi(defaultClient);
    Integer roleId = 56; // Integer | 
    try {
      List<CustomerDataCustomerInterface> result = apiInstance.companyAclV1GetUsersByRoleIdGet(roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyRoleRoleIdUsersApi#companyAclV1GetUsersByRoleIdGet");
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
| **roleId** | **Integer**|  | |

### Return type

[**List&lt;CustomerDataCustomerInterface&gt;**](CustomerDataCustomerInterface.md)

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


# CompanyAssignRolesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyAclV1AssignRolesPut**](CompanyAssignRolesApi.md#companyAclV1AssignRolesPut) | **PUT** /V1/company/assignRoles | company/assignRoles |


<a id="companyAclV1AssignRolesPut"></a>
# **companyAclV1AssignRolesPut**
> Boolean companyAclV1AssignRolesPut(companyAclV1AssignRolesPutRequest)

company/assignRoles

Change a role for a company user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyAssignRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyAssignRolesApi apiInstance = new CompanyAssignRolesApi(defaultClient);
    CompanyAclV1AssignRolesPutRequest companyAclV1AssignRolesPutRequest = new CompanyAclV1AssignRolesPutRequest(); // CompanyAclV1AssignRolesPutRequest | 
    try {
      Boolean result = apiInstance.companyAclV1AssignRolesPut(companyAclV1AssignRolesPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyAssignRolesApi#companyAclV1AssignRolesPut");
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
| **companyAclV1AssignRolesPutRequest** | [**CompanyAclV1AssignRolesPutRequest**](CompanyAclV1AssignRolesPutRequest.md)|  | [optional] |

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
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |


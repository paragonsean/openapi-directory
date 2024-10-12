# ServicePrincipalAppRoleAssignmentsApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicePrincipalsListAppRoleAssignments**](ServicePrincipalAppRoleAssignmentsApi.md#servicePrincipalsListAppRoleAssignments) | **GET** /{tenantID}/servicePrincipals/{objectId}/appRoleAssignments | Applications that the service principal is assigned to. |


<a id="servicePrincipalsListAppRoleAssignments"></a>
# **servicePrincipalsListAppRoleAssignments**
> AppRoleAssignmentListResult servicePrincipalsListAppRoleAssignments(objectId, apiVersion, tenantID)

Applications that the service principal is assigned to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePrincipalAppRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicePrincipalAppRoleAssignmentsApi apiInstance = new ServicePrincipalAppRoleAssignmentsApi(defaultClient);
    String objectId = "objectId_example"; // String | The object ID of the service principal for which to get owners.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      AppRoleAssignmentListResult result = apiInstance.servicePrincipalsListAppRoleAssignments(objectId, apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePrincipalAppRoleAssignmentsApi#servicePrincipalsListAppRoleAssignments");
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
| **objectId** | **String**| The object ID of the service principal for which to get owners. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

[**AppRoleAssignmentListResult**](AppRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


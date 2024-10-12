# InfraRoleApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**infraRolesRestart**](InfraRoleApi.md#infraRolesRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoles/{infraRole}/Restart |  |


<a id="infraRolesRestart"></a>
# **infraRolesRestart**
> infraRolesRestart(subscriptionId, resourceGroupName, location, infraRole, apiVersion)



Restarts the requested infrastructure role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfraRoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InfraRoleApi apiInstance = new InfraRoleApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String infraRole = "infraRole_example"; // String | Infrastructure role name.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      apiInstance.infraRolesRestart(subscriptionId, resourceGroupName, location, infraRole, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfraRoleApi#infraRolesRestart");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **infraRole** | **String**| Infrastructure role name. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | ACCEPTED |  -  |


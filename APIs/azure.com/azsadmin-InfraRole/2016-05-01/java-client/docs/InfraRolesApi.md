# InfraRolesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**infraRolesGet**](InfraRolesApi.md#infraRolesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoles/{infraRole} |  |
| [**infraRolesList**](InfraRolesApi.md#infraRolesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoles |  |


<a id="infraRolesGet"></a>
# **infraRolesGet**
> InfraRole infraRolesGet(subscriptionId, resourceGroupName, location, infraRole, apiVersion)



Returns the requested infrastructure role description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfraRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InfraRolesApi apiInstance = new InfraRolesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String infraRole = "infraRole_example"; // String | Infrastructure role name.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      InfraRole result = apiInstance.infraRolesGet(subscriptionId, resourceGroupName, location, infraRole, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfraRolesApi#infraRolesGet");
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

[**InfraRole**](InfraRole.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="infraRolesList"></a>
# **infraRolesList**
> InfraRoleList infraRolesList(subscriptionId, resourceGroupName, location, apiVersion, $filter)



Returns a list of all infrastructure roles at a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfraRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InfraRolesApi apiInstance = new InfraRolesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    String $filter = "$filter_example"; // String | OData filter parameter.
    try {
      InfraRoleList result = apiInstance.infraRolesList(subscriptionId, resourceGroupName, location, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfraRolesApi#infraRolesList");
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
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |
| **$filter** | **String**| OData filter parameter. | [optional] |

### Return type

[**InfraRoleList**](InfraRoleList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |


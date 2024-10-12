# ContainerHostMappingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**containerHostMappingsGetContainerHostMapping**](ContainerHostMappingsApi.md#containerHostMappingsGetContainerHostMapping) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/locations/{location}/checkContainerHostMapping | Returns container host mapping object for a container host resource ID if an associated controller exists. |


<a id="containerHostMappingsGetContainerHostMapping"></a>
# **containerHostMappingsGetContainerHostMapping**
> ContainerHostMapping containerHostMappingsGetContainerHostMapping(apiVersion, subscriptionId, resourceGroupName, location, containerHostMapping)

Returns container host mapping object for a container host resource ID if an associated controller exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerHostMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ContainerHostMappingsApi apiInstance = new ContainerHostMappingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
    String location = "location_example"; // String | Location of the container host.
    ContainerHostMapping containerHostMapping = new ContainerHostMapping(); // ContainerHostMapping | 
    try {
      ContainerHostMapping result = apiInstance.containerHostMappingsGetContainerHostMapping(apiVersion, subscriptionId, resourceGroupName, location, containerHostMapping);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerHostMappingsApi#containerHostMappingsGetContainerHostMapping");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group to which the resource belongs. | |
| **location** | **String**| Location of the container host. | |
| **containerHostMapping** | [**ContainerHostMapping**](ContainerHostMapping.md)|  | |

### Return type

[**ContainerHostMapping**](ContainerHostMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; response contains the container host mapping. |  -  |
| **204** | The request was successful; container host mapping does not exist. |  -  |
| **0** | Error response describing the reason for operation failure. 400 - BadRequest(Invalid container host resource ID.) |  -  |


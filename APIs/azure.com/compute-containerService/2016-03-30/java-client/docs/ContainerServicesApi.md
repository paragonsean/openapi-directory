# ContainerServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**containerServicesCreateOrUpdate**](ContainerServicesApi.md#containerServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/containerServices/{containerServiceName} |  |
| [**containerServicesList**](ContainerServicesApi.md#containerServicesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ContainerService/containerServices |  |


<a id="containerServicesCreateOrUpdate"></a>
# **containerServicesCreateOrUpdate**
> ContainerService containerServicesCreateOrUpdate(resourceGroupName, containerServiceName, apiVersion, subscriptionId, parameters)



Creates or updates a container service with the specified configuration of orchestrator, masters, and agents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ContainerServicesApi apiInstance = new ContainerServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String containerServiceName = "containerServiceName_example"; // String | The name of the container service in the specified subscription and resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ContainerService parameters = new ContainerService(); // ContainerService | Parameters supplied to the Create or Update a Container Service operation.
    try {
      ContainerService result = apiInstance.containerServicesCreateOrUpdate(resourceGroupName, containerServiceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerServicesApi#containerServicesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **containerServiceName** | **String**| The name of the container service in the specified subscription and resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ContainerService**](ContainerService.md)| Parameters supplied to the Create or Update a Container Service operation. | |

### Return type

[**ContainerService**](ContainerService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **202** | Accepted |  -  |

<a id="containerServicesList"></a>
# **containerServicesList**
> ContainerServiceListResult containerServicesList(apiVersion, subscriptionId)



Gets a list of container services in the specified subscription. The operation returns properties of each container service including state, orchestrator, number of masters and agents, and FQDNs of masters and agents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContainerServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ContainerServicesApi apiInstance = new ContainerServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ContainerServiceListResult result = apiInstance.containerServicesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContainerServicesApi#containerServicesList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ContainerServiceListResult**](ContainerServiceListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


# CodePackagesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**codePackageGetContainerLogs**](CodePackagesApi.md#codePackageGetContainerLogs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationResourceName}/services/{serviceResourceName}/replicas/{replicaName}/codePackages/{codePackageName}/logs | Gets the logs from the container. |


<a id="codePackageGetContainerLogs"></a>
# **codePackageGetContainerLogs**
> ContainerLogs codePackageGetContainerLogs(subscriptionId, resourceGroupName, apiVersion, applicationResourceName, serviceResourceName, replicaName, codePackageName, tail)

Gets the logs from the container.

Gets the logs for the container of the specified code package of the service replica.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodePackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CodePackagesApi apiInstance = new CodePackagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    String serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
    String replicaName = "replicaName_example"; // String | Service Fabric replica name.
    String codePackageName = "codePackageName_example"; // String | The name of code package of the service.
    Integer tail = 56; // Integer | Number of lines to show from the end of the logs. Default is 100.
    try {
      ContainerLogs result = apiInstance.codePackageGetContainerLogs(subscriptionId, resourceGroupName, apiVersion, applicationResourceName, serviceResourceName, replicaName, codePackageName, tail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodePackagesApi#codePackageGetContainerLogs");
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
| **subscriptionId** | **String**| The customer subscription identifier | |
| **resourceGroupName** | **String**| Azure resource group name | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **applicationResourceName** | **String**| The identity of the application. | |
| **serviceResourceName** | **String**| The identity of the service. | |
| **replicaName** | **String**| Service Fabric replica name. | |
| **codePackageName** | **String**| The name of code package of the service. | |
| **tail** | **Integer**| Number of lines to show from the end of the logs. Default is 100. | [optional] |

### Return type

[**ContainerLogs**](ContainerLogs.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **0** | Error |  -  |


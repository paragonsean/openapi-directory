# MeshCodePackagesApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meshCodePackageGetContainerLogs**](MeshCodePackagesApi.md#meshCodePackageGetContainerLogs) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName}/Replicas/{replicaName}/CodePackages/{codePackageName}/Logs | Gets the logs from the container. |


<a id="meshCodePackageGetContainerLogs"></a>
# **meshCodePackageGetContainerLogs**
> ContainerLogs meshCodePackageGetContainerLogs(apiVersion, applicationResourceName, serviceResourceName, replicaName, codePackageName, tail)

Gets the logs from the container.

Gets the logs for the container of the specified code package of the service replica.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshCodePackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshCodePackagesApi apiInstance = new MeshCodePackagesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    String serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
    String replicaName = "replicaName_example"; // String | Service Fabric replica name.
    String codePackageName = "codePackageName_example"; // String | The name of code package of the service.
    String tail = "tail_example"; // String | Number of lines to show from the end of the logs. Default is 100. 'all' to show the complete logs.
    try {
      ContainerLogs result = apiInstance.meshCodePackageGetContainerLogs(apiVersion, applicationResourceName, serviceResourceName, replicaName, codePackageName, tail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshCodePackagesApi#meshCodePackageGetContainerLogs");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **applicationResourceName** | **String**| The identity of the application. | |
| **serviceResourceName** | **String**| The identity of the service. | |
| **replicaName** | **String**| Service Fabric replica name. | |
| **codePackageName** | **String**| The name of code package of the service. | |
| **tail** | **String**| Number of lines to show from the end of the logs. Default is 100. &#39;all&#39; to show the complete logs. | [optional] |

### Return type

[**ContainerLogs**](ContainerLogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |


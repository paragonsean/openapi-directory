# ServiceReplicasApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceReplicaGet**](ServiceReplicasApi.md#serviceReplicaGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationResourceName}/services/{serviceResourceName}/replicas/{replicaName} | Gets the given replica of the service of an application. |
| [**serviceReplicaList**](ServiceReplicasApi.md#serviceReplicaList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationResourceName}/services/{serviceResourceName}/replicas | Gets replicas of a given service. |


<a id="serviceReplicaGet"></a>
# **serviceReplicaGet**
> ServiceReplicaDescription serviceReplicaGet(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, serviceResourceName, replicaName)

Gets the given replica of the service of an application.

Gets the information about the service replica with the given name. The information include the description and other properties of the service replica.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceReplicasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceReplicasApi apiInstance = new ServiceReplicasApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    String serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
    String replicaName = "replicaName_example"; // String | Service Fabric replica name.
    try {
      ServiceReplicaDescription result = apiInstance.serviceReplicaGet(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, serviceResourceName, replicaName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceReplicasApi#serviceReplicaGet");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **applicationResourceName** | **String**| The identity of the application. | |
| **serviceResourceName** | **String**| The identity of the service. | |
| **replicaName** | **String**| Service Fabric replica name. | |

### Return type

[**ServiceReplicaDescription**](ServiceReplicaDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="serviceReplicaList"></a>
# **serviceReplicaList**
> ServiceReplicaDescriptionList serviceReplicaList(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, serviceResourceName)

Gets replicas of a given service.

Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceReplicasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceReplicasApi apiInstance = new ServiceReplicasApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    String serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
    try {
      ServiceReplicaDescriptionList result = apiInstance.serviceReplicaList(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, serviceResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceReplicasApi#serviceReplicaList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **applicationResourceName** | **String**| The identity of the application. | |
| **serviceResourceName** | **String**| The identity of the service. | |

### Return type

[**ServiceReplicaDescriptionList**](ServiceReplicaDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |


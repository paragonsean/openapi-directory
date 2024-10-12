# ReplicasApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicaGet**](ReplicasApi.md#replicaGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationName}/services/{serviceName}/replicas/{replicaName} | Gets a specific replica of a given service. |
| [**replicaListByServiceName**](ReplicasApi.md#replicaListByServiceName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationName}/services/{serviceName}/replicas | Gets replicas of a given service. |


<a id="replicaGet"></a>
# **replicaGet**
> ServiceReplicaDescription replicaGet(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName, replicaName)

Gets a specific replica of a given service.

Gets the information about the specified replica of a given service of an application. The information includes the runtime properties of the replica instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicasApi apiInstance = new ReplicasApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-07-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String applicationName = "applicationName_example"; // String | The identity of the application.
    String serviceName = "serviceName_example"; // String | The identity of the service.
    String replicaName = "replicaName_example"; // String | The identity of the service replica.
    try {
      ServiceReplicaDescription result = apiInstance.replicaGet(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName, replicaName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicasApi#replicaGet");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to 2018-07-01-preview] [enum: 2018-07-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **applicationName** | **String**| The identity of the application. | |
| **serviceName** | **String**| The identity of the service. | |
| **replicaName** | **String**| The identity of the service replica. | |

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

<a id="replicaListByServiceName"></a>
# **replicaListByServiceName**
> ServiceReplicaList replicaListByServiceName(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName)

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
import org.openapitools.client.api.ReplicasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicasApi apiInstance = new ReplicasApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-07-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String applicationName = "applicationName_example"; // String | The identity of the application.
    String serviceName = "serviceName_example"; // String | The identity of the service.
    try {
      ServiceReplicaList result = apiInstance.replicaListByServiceName(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicasApi#replicaListByServiceName");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to 2018-07-01-preview] [enum: 2018-07-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **applicationName** | **String**| The identity of the application. | |
| **serviceName** | **String**| The identity of the service. | |

### Return type

[**ServiceReplicaList**](ServiceReplicaList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


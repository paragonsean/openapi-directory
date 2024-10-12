# MeshServiceReplicasApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meshServiceReplicaGet**](MeshServiceReplicasApi.md#meshServiceReplicaGet) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName}/Replicas/{replicaName} | Gets the given replica of the service of an application. |
| [**meshServiceReplicaList**](MeshServiceReplicasApi.md#meshServiceReplicaList) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName}/Replicas | Lists all the replicas of a service. |


<a id="meshServiceReplicaGet"></a>
# **meshServiceReplicaGet**
> ServiceReplicaDescription meshServiceReplicaGet(apiVersion, applicationResourceName, serviceResourceName, replicaName)

Gets the given replica of the service of an application.

Gets the information about the service replica with the given name. The information include the description and other properties of the service replica.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshServiceReplicasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshServiceReplicasApi apiInstance = new MeshServiceReplicasApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    String serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
    String replicaName = "replicaName_example"; // String | Service Fabric replica name.
    try {
      ServiceReplicaDescription result = apiInstance.meshServiceReplicaGet(apiVersion, applicationResourceName, serviceResourceName, replicaName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshServiceReplicasApi#meshServiceReplicaGet");
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

### Return type

[**ServiceReplicaDescription**](ServiceReplicaDescription.md)

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

<a id="meshServiceReplicaList"></a>
# **meshServiceReplicaList**
> PagedServiceReplicaDescriptionList meshServiceReplicaList(apiVersion, applicationResourceName, serviceResourceName)

Lists all the replicas of a service.

Gets the information about all replicas of a service. The information include the description and other properties of the service replica.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshServiceReplicasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshServiceReplicasApi apiInstance = new MeshServiceReplicasApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    String serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
    try {
      PagedServiceReplicaDescriptionList result = apiInstance.meshServiceReplicaList(apiVersion, applicationResourceName, serviceResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshServiceReplicasApi#meshServiceReplicaList");
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

### Return type

[**PagedServiceReplicaDescriptionList**](PagedServiceReplicaDescriptionList.md)

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


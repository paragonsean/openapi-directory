# ClusterVersionsListOperationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clusterVersionsListByVersion**](ClusterVersionsListOperationApi.md#clusterVersionsListByVersion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions/{clusterVersion} |  |


<a id="clusterVersionsListByVersion"></a>
# **clusterVersionsListByVersion**
> ClusterCodeVersionsListResult clusterVersionsListByVersion(location, apiVersion, subscriptionId, clusterVersion)



List cluster code versions by version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterVersionsListOperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClusterVersionsListOperationApi apiInstance = new ClusterVersionsListOperationApi(defaultClient);
    String location = "location_example"; // String | The location for the cluster code versions, this is different from cluster location
    String apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String clusterVersion = "clusterVersion_example"; // String | The cluster code version
    try {
      ClusterCodeVersionsListResult result = apiInstance.clusterVersionsListByVersion(location, apiVersion, subscriptionId, clusterVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterVersionsListOperationApi#clusterVersionsListByVersion");
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
| **location** | **String**| The location for the cluster code versions, this is different from cluster location | |
| **apiVersion** | **String**| The version of the ServiceFabric resource provider api | |
| **subscriptionId** | **String**| The customer subscription identifier | |
| **clusterVersion** | **String**| The cluster code version | |

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Get cluster code versions successfully |  -  |


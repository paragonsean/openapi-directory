# ClusterListOperationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clustersList**](ClusterListOperationApi.md#clustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/clusters |  |


<a id="clustersList"></a>
# **clustersList**
> ClusterListResult clustersList(apiVersion, subscriptionId)



List cluster resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterListOperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClusterListOperationApi apiInstance = new ClusterListOperationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    try {
      ClusterListResult result = apiInstance.clustersList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterListOperationApi#clustersList");
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
| **apiVersion** | **String**| The version of the ServiceFabric resource provider api | |
| **subscriptionId** | **String**| The customer subscription identifier | |

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Get cluster  successfully |  -  |


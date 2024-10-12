# TopologyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**topologyGet**](TopologyApi.md#topologyGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/topologies/{topologyResourceName} |  |
| [**topologyList**](TopologyApi.md#topologyList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/topologies |  |
| [**topologyListByHomeRegion**](TopologyApi.md#topologyListByHomeRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/topologies |  |


<a id="topologyGet"></a>
# **topologyGet**
> TopologyResource topologyGet(subscriptionId, resourceGroupName, ascLocation, topologyResourceName, apiVersion)



Gets a specific topology component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopologyApi apiInstance = new TopologyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String topologyResourceName = "topologyResourceName_example"; // String | Name of a topology resources collection.
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      TopologyResource result = apiInstance.topologyGet(subscriptionId, resourceGroupName, ascLocation, topologyResourceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopologyApi#topologyGet");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **topologyResourceName** | **String**| Name of a topology resources collection. | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**TopologyResource**](TopologyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="topologyList"></a>
# **topologyList**
> TopologyList topologyList(subscriptionId, apiVersion)



Gets a list that allows to build a topology view of a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopologyApi apiInstance = new TopologyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      TopologyList result = apiInstance.topologyList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopologyApi#topologyList");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**TopologyList**](TopologyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="topologyListByHomeRegion"></a>
# **topologyListByHomeRegion**
> TopologyList topologyListByHomeRegion(subscriptionId, ascLocation, apiVersion)



Gets a list that allows to build a topology view of a subscription and location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopologyApi apiInstance = new TopologyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      TopologyList result = apiInstance.topologyListByHomeRegion(subscriptionId, ascLocation, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopologyApi#topologyListByHomeRegion");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**TopologyList**](TopologyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |


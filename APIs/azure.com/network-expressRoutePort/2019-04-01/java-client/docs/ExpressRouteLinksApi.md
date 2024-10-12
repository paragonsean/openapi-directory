# ExpressRouteLinksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRouteLinksGet**](ExpressRouteLinksApi.md#expressRouteLinksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}/links/{linkName} |  |
| [**expressRouteLinksList**](ExpressRouteLinksApi.md#expressRouteLinksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}/links |  |


<a id="expressRouteLinksGet"></a>
# **expressRouteLinksGet**
> ExpressRouteLink expressRouteLinksGet(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, linkName)



Retrieves the specified ExpressRouteLink resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteLinksApi apiInstance = new ExpressRouteLinksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String expressRoutePortName = "expressRoutePortName_example"; // String | The name of the ExpressRoutePort resource.
    String linkName = "linkName_example"; // String | The name of the ExpressRouteLink resource.
    try {
      ExpressRouteLink result = apiInstance.expressRouteLinksGet(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, linkName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteLinksApi#expressRouteLinksGet");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **expressRoutePortName** | **String**| The name of the ExpressRoutePort resource. | |
| **linkName** | **String**| The name of the ExpressRouteLink resource. | |

### Return type

[**ExpressRouteLink**](ExpressRouteLink.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the requested ExpressRouteLink resource. |  -  |

<a id="expressRouteLinksList"></a>
# **expressRouteLinksList**
> ExpressRouteLinkListResult expressRouteLinksList(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName)



Retrieve the ExpressRouteLink sub-resources of the specified ExpressRoutePort resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRouteLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRouteLinksApi apiInstance = new ExpressRouteLinksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String expressRoutePortName = "expressRoutePortName_example"; // String | The name of the ExpressRoutePort resource.
    try {
      ExpressRouteLinkListResult result = apiInstance.expressRouteLinksList(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRouteLinksApi#expressRouteLinksList");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **expressRoutePortName** | **String**| The name of the ExpressRoutePort resource. | |

### Return type

[**ExpressRouteLinkListResult**](ExpressRouteLinkListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of ExpressRouteLink resources. If there are no ExpressRouteLink resources then an empty list is returned. |  -  |


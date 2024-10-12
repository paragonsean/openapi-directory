# ConfigurationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurationsGet**](ConfigurationsApi.md#configurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/configurations/{configurationName} |  |
| [**configurationsList**](ConfigurationsApi.md#configurationsList) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/configurations |  |
| [**configurationsUpdate**](ConfigurationsApi.md#configurationsUpdate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/configurations/{configurationName} |  |


<a id="configurationsGet"></a>
# **configurationsGet**
> Map&lt;String, String&gt; configurationsGet(subscriptionId, resourceGroupName, clusterName, configurationName, apiVersion)



The configuration object for the specified cluster. This API is not recommended and might be removed in the future. Please consider using List configurations API instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationsApi apiInstance = new ConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    String configurationName = "configurationName_example"; // String | The name of the cluster configuration.
    String apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
    try {
      Map<String, String> result = apiInstance.configurationsGet(subscriptionId, resourceGroupName, clusterName, configurationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationsApi#configurationsGet");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **clusterName** | **String**| The name of the cluster. | |
| **configurationName** | **String**| The name of the cluster configuration. | |
| **apiVersion** | **String**| The HDInsight client API Version. | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="configurationsList"></a>
# **configurationsList**
> ClusterConfigurations configurationsList(subscriptionId, resourceGroupName, clusterName, apiVersion)



Gets all configuration information for an HDI cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationsApi apiInstance = new ConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    String apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
    try {
      ClusterConfigurations result = apiInstance.configurationsList(subscriptionId, resourceGroupName, clusterName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationsApi#configurationsList");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **clusterName** | **String**| The name of the cluster. | |
| **apiVersion** | **String**| The HDInsight client API Version. | |

### Return type

[**ClusterConfigurations**](ClusterConfigurations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="configurationsUpdate"></a>
# **configurationsUpdate**
> configurationsUpdate(subscriptionId, resourceGroupName, clusterName, configurationName, apiVersion, parameters)



Configures the HTTP settings on the specified cluster. This API is deprecated, please use UpdateGatewaySettings in cluster endpoint instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationsApi apiInstance = new ConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    String configurationName = "configurationName_example"; // String | The name of the cluster configuration.
    String apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
    Map<String, String> parameters = new HashMap(); // Map<String, String> | The cluster configurations.
    try {
      apiInstance.configurationsUpdate(subscriptionId, resourceGroupName, clusterName, configurationName, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationsApi#configurationsUpdate");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **clusterName** | **String**| The name of the cluster. | |
| **configurationName** | **String**| The name of the cluster configuration. | |
| **apiVersion** | **String**| The HDInsight client API Version. | |
| **parameters** | [**Map&lt;String, String&gt;**](String.md)| The cluster configurations. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok response definition |  -  |
| **202** | Accepted response definition |  -  |
| **204** | No content response definition |  -  |
| **0** | Error response describing why the operation failed. |  -  |


# IntegrationRuntimeNodesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationRuntimeNodesDelete**](IntegrationRuntimeNodesApi.md#integrationRuntimeNodesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName} |  |
| [**integrationRuntimeNodesGet**](IntegrationRuntimeNodesApi.md#integrationRuntimeNodesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName} |  |
| [**integrationRuntimeNodesGetIpAddress**](IntegrationRuntimeNodesApi.md#integrationRuntimeNodesGetIpAddress) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName}/ipAddress |  |
| [**integrationRuntimeNodesUpdate**](IntegrationRuntimeNodesApi.md#integrationRuntimeNodesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/nodes/{nodeName} |  |


<a id="integrationRuntimeNodesDelete"></a>
# **integrationRuntimeNodesDelete**
> integrationRuntimeNodesDelete(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion)



Deletes a self-hosted integration runtime node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimeNodesApi apiInstance = new IntegrationRuntimeNodesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String nodeName = "nodeName_example"; // String | The integration runtime node name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationRuntimeNodesDelete(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimeNodesApi#integrationRuntimeNodesDelete");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **nodeName** | **String**| The integration runtime node name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **204** | No Content. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimeNodesGet"></a>
# **integrationRuntimeNodesGet**
> IntegrationRuntimeNodesGet200Response integrationRuntimeNodesGet(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion)



Gets a self-hosted integration runtime node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimeNodesApi apiInstance = new IntegrationRuntimeNodesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String nodeName = "nodeName_example"; // String | The integration runtime node name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationRuntimeNodesGet200Response result = apiInstance.integrationRuntimeNodesGet(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimeNodesApi#integrationRuntimeNodesGet");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **nodeName** | **String**| The integration runtime node name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationRuntimeNodesGet200Response**](IntegrationRuntimeNodesGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimeNodesGetIpAddress"></a>
# **integrationRuntimeNodesGetIpAddress**
> IntegrationRuntimeNodesGetIpAddress200Response integrationRuntimeNodesGetIpAddress(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion)



Get the IP address of self-hosted integration runtime node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimeNodesApi apiInstance = new IntegrationRuntimeNodesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String nodeName = "nodeName_example"; // String | The integration runtime node name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationRuntimeNodesGetIpAddress200Response result = apiInstance.integrationRuntimeNodesGetIpAddress(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimeNodesApi#integrationRuntimeNodesGetIpAddress");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **nodeName** | **String**| The integration runtime node name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationRuntimeNodesGetIpAddress200Response**](IntegrationRuntimeNodesGetIpAddress200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="integrationRuntimeNodesUpdate"></a>
# **integrationRuntimeNodesUpdate**
> IntegrationRuntimeNodesGet200Response integrationRuntimeNodesUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion, updateIntegrationRuntimeNodeRequest)



Updates a self-hosted integration runtime node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimeNodesApi apiInstance = new IntegrationRuntimeNodesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String nodeName = "nodeName_example"; // String | The integration runtime node name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    UpdateIntegrationRuntimeNodeRequest updateIntegrationRuntimeNodeRequest = new UpdateIntegrationRuntimeNodeRequest(); // UpdateIntegrationRuntimeNodeRequest | The parameters for updating an integration runtime node.
    try {
      IntegrationRuntimeNodesGet200Response result = apiInstance.integrationRuntimeNodesUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, nodeName, apiVersion, updateIntegrationRuntimeNodeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimeNodesApi#integrationRuntimeNodesUpdate");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **integrationRuntimeName** | **String**| The integration runtime name. | |
| **nodeName** | **String**| The integration runtime node name. | |
| **apiVersion** | **String**| The API version. | |
| **updateIntegrationRuntimeNodeRequest** | [**UpdateIntegrationRuntimeNodeRequest**](UpdateIntegrationRuntimeNodeRequest.md)| The parameters for updating an integration runtime node. | |

### Return type

[**IntegrationRuntimeNodesGet200Response**](IntegrationRuntimeNodesGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |


# IntegrationRuntimeObjectMetadataApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationRuntimeObjectMetadataGet**](IntegrationRuntimeObjectMetadataApi.md#integrationRuntimeObjectMetadataGet) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/getObjectMetadata |  |
| [**integrationRuntimeObjectMetadataRefresh**](IntegrationRuntimeObjectMetadataApi.md#integrationRuntimeObjectMetadataRefresh) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/refreshObjectMetadata |  |


<a id="integrationRuntimeObjectMetadataGet"></a>
# **integrationRuntimeObjectMetadataGet**
> IntegrationRuntimeObjectMetadataGet200Response integrationRuntimeObjectMetadataGet(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, getMetadataRequest)



Get a SSIS integration runtime object metadata by specified path. The return is pageable metadata list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimeObjectMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimeObjectMetadataApi apiInstance = new IntegrationRuntimeObjectMetadataApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    GetSsisObjectMetadataRequest getMetadataRequest = new GetSsisObjectMetadataRequest(); // GetSsisObjectMetadataRequest | The parameters for getting a SSIS object metadata.
    try {
      IntegrationRuntimeObjectMetadataGet200Response result = apiInstance.integrationRuntimeObjectMetadataGet(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, getMetadataRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimeObjectMetadataApi#integrationRuntimeObjectMetadataGet");
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
| **apiVersion** | **String**| The API version. | |
| **getMetadataRequest** | [**GetSsisObjectMetadataRequest**](GetSsisObjectMetadataRequest.md)| The parameters for getting a SSIS object metadata. | [optional] |

### Return type

[**IntegrationRuntimeObjectMetadataGet200Response**](IntegrationRuntimeObjectMetadataGet200Response.md)

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

<a id="integrationRuntimeObjectMetadataRefresh"></a>
# **integrationRuntimeObjectMetadataRefresh**
> SsisObjectMetadataStatusResponse integrationRuntimeObjectMetadataRefresh(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Refresh a SSIS integration runtime object metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationRuntimeObjectMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationRuntimeObjectMetadataApi apiInstance = new IntegrationRuntimeObjectMetadataApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      SsisObjectMetadataStatusResponse result = apiInstance.integrationRuntimeObjectMetadataRefresh(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationRuntimeObjectMetadataApi#integrationRuntimeObjectMetadataRefresh");
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
| **apiVersion** | **String**| The API version. | |

### Return type

[**SsisObjectMetadataStatusResponse**](SsisObjectMetadataStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Accepted. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |


# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**proactiveDetectionConfigurationsGet**](DefaultApi.md#proactiveDetectionConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs/{ConfigurationId} |  |
| [**proactiveDetectionConfigurationsList**](DefaultApi.md#proactiveDetectionConfigurationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs |  |
| [**proactiveDetectionConfigurationsUpdate**](DefaultApi.md#proactiveDetectionConfigurationsUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs/{ConfigurationId} |  |


<a id="proactiveDetectionConfigurationsGet"></a>
# **proactiveDetectionConfigurationsGet**
> ApplicationInsightsComponentProactiveDetectionConfiguration proactiveDetectionConfigurationsGet(resourceGroupName, apiVersion, subscriptionId, resourceName, configurationId)



Get the ProactiveDetection configuration for this configuration id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String configurationId = "configurationId_example"; // String | The ProactiveDetection configuration ID. This is unique within a Application Insights component.
    try {
      ApplicationInsightsComponentProactiveDetectionConfiguration result = apiInstance.proactiveDetectionConfigurationsGet(resourceGroupName, apiVersion, subscriptionId, resourceName, configurationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#proactiveDetectionConfigurationsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **configurationId** | **String**| The ProactiveDetection configuration ID. This is unique within a Application Insights component. | |

### Return type

[**ApplicationInsightsComponentProactiveDetectionConfiguration**](ApplicationInsightsComponentProactiveDetectionConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ProactiveDetection configuration for this configuration id. |  -  |

<a id="proactiveDetectionConfigurationsList"></a>
# **proactiveDetectionConfigurationsList**
> List&lt;ApplicationInsightsComponentProactiveDetectionConfiguration&gt; proactiveDetectionConfigurationsList(resourceGroupName, apiVersion, subscriptionId, resourceName)



Gets a list of ProactiveDetection configurations of an Application Insights component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    try {
      List<ApplicationInsightsComponentProactiveDetectionConfiguration> result = apiInstance.proactiveDetectionConfigurationsList(resourceGroupName, apiVersion, subscriptionId, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#proactiveDetectionConfigurationsList");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |

### Return type

[**List&lt;ApplicationInsightsComponentProactiveDetectionConfiguration&gt;**](ApplicationInsightsComponentProactiveDetectionConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more ProactiveDetection configurations of an Application Insights component. |  -  |

<a id="proactiveDetectionConfigurationsUpdate"></a>
# **proactiveDetectionConfigurationsUpdate**
> ApplicationInsightsComponentProactiveDetectionConfiguration proactiveDetectionConfigurationsUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, configurationId, proactiveDetectionProperties)



Update the ProactiveDetection configuration for this configuration id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String configurationId = "configurationId_example"; // String | The ProactiveDetection configuration ID. This is unique within a Application Insights component.
    ApplicationInsightsComponentProactiveDetectionConfiguration proactiveDetectionProperties = new ApplicationInsightsComponentProactiveDetectionConfiguration(); // ApplicationInsightsComponentProactiveDetectionConfiguration | Properties that need to be specified to update the ProactiveDetection configuration.
    try {
      ApplicationInsightsComponentProactiveDetectionConfiguration result = apiInstance.proactiveDetectionConfigurationsUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, configurationId, proactiveDetectionProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#proactiveDetectionConfigurationsUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **configurationId** | **String**| The ProactiveDetection configuration ID. This is unique within a Application Insights component. | |
| **proactiveDetectionProperties** | [**ApplicationInsightsComponentProactiveDetectionConfiguration**](ApplicationInsightsComponentProactiveDetectionConfiguration.md)| Properties that need to be specified to update the ProactiveDetection configuration. | |

### Return type

[**ApplicationInsightsComponentProactiveDetectionConfiguration**](ApplicationInsightsComponentProactiveDetectionConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ProactiveDetection configuration that was successfully updated. |  -  |


# ConfigurationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurationsCreateInResourceGroup**](ConfigurationsApi.md#configurationsCreateInResourceGroup) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Advisor/configurations/{configurationName} | Create/Overwrite Azure Advisor configuration. |
| [**configurationsCreateInSubscription**](ConfigurationsApi.md#configurationsCreateInSubscription) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/configurations/{configurationName} | Create/Overwrite Azure Advisor configuration. |
| [**configurationsListByResourceGroup**](ConfigurationsApi.md#configurationsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Advisor/configurations | Retrieve Azure Advisor configurations. |
| [**configurationsListBySubscription**](ConfigurationsApi.md#configurationsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/configurations | Retrieve Azure Advisor configurations. |


<a id="configurationsCreateInResourceGroup"></a>
# **configurationsCreateInResourceGroup**
> ConfigData configurationsCreateInResourceGroup(apiVersion, subscriptionId, configurationName, resourceGroup, configContract)

Create/Overwrite Azure Advisor configuration.

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
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String configurationName = "default"; // String | Advisor configuration name. Value must be 'default'
    String resourceGroup = "resourceGroup_example"; // String | The name of the Azure resource group.
    ConfigData configContract = new ConfigData(); // ConfigData | The Azure Advisor configuration data structure.
    try {
      ConfigData result = apiInstance.configurationsCreateInResourceGroup(apiVersion, subscriptionId, configurationName, resourceGroup, configContract);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationsApi#configurationsCreateInResourceGroup");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **configurationName** | **String**| Advisor configuration name. Value must be &#39;default&#39; | [enum: default] |
| **resourceGroup** | **String**| The name of the Azure resource group. | |
| **configContract** | [**ConfigData**](ConfigData.md)| The Azure Advisor configuration data structure. | |

### Return type

[**ConfigData**](ConfigData.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created/overwrote configuration. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="configurationsCreateInSubscription"></a>
# **configurationsCreateInSubscription**
> ConfigData configurationsCreateInSubscription(apiVersion, subscriptionId, configurationName, configContract)

Create/Overwrite Azure Advisor configuration.

Create/Overwrite Azure Advisor configuration and also delete all configurations of contained resource groups.

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
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String configurationName = "default"; // String | Advisor configuration name. Value must be 'default'
    ConfigData configContract = new ConfigData(); // ConfigData | The Azure Advisor configuration data structure.
    try {
      ConfigData result = apiInstance.configurationsCreateInSubscription(apiVersion, subscriptionId, configurationName, configContract);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationsApi#configurationsCreateInSubscription");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **configurationName** | **String**| Advisor configuration name. Value must be &#39;default&#39; | [enum: default] |
| **configContract** | [**ConfigData**](ConfigData.md)| The Azure Advisor configuration data structure. | |

### Return type

[**ConfigData**](ConfigData.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created/overwrote configuration. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="configurationsListByResourceGroup"></a>
# **configurationsListByResourceGroup**
> ConfigurationListResult configurationsListByResourceGroup(apiVersion, subscriptionId, resourceGroup)

Retrieve Azure Advisor configurations.

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
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The name of the Azure resource group.
    try {
      ConfigurationListResult result = apiInstance.configurationsListByResourceGroup(apiVersion, subscriptionId, resourceGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationsApi#configurationsListByResourceGroup");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **resourceGroup** | **String**| The name of the Azure resource group. | |

### Return type

[**ConfigurationListResult**](ConfigurationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Successfully retrieved zero or more configurations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="configurationsListBySubscription"></a>
# **configurationsListBySubscription**
> ConfigurationListResult configurationsListBySubscription(apiVersion, subscriptionId)

Retrieve Azure Advisor configurations.

Retrieve Azure Advisor configurations and also retrieve configurations of contained resource groups.

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
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    try {
      ConfigurationListResult result = apiInstance.configurationsListBySubscription(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationsApi#configurationsListBySubscription");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |

### Return type

[**ConfigurationListResult**](ConfigurationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Successfully retrieved zero or more configurations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


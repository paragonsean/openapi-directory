# IntegrationAccountRosettaNetProcessConfigurationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rosettaNetProcessConfigurationsCreateOrUpdate**](IntegrationAccountRosettaNetProcessConfigurationsApi.md#rosettaNetProcessConfigurationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/rosettanetprocessconfigurations/{rosettaNetProcessConfigurationName} |  |
| [**rosettaNetProcessConfigurationsDelete**](IntegrationAccountRosettaNetProcessConfigurationsApi.md#rosettaNetProcessConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/rosettanetprocessconfigurations/{rosettaNetProcessConfigurationName} |  |
| [**rosettaNetProcessConfigurationsGet**](IntegrationAccountRosettaNetProcessConfigurationsApi.md#rosettaNetProcessConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/rosettanetprocessconfigurations/{rosettaNetProcessConfigurationName} |  |
| [**rosettaNetProcessConfigurationsListByIntegrationAccounts**](IntegrationAccountRosettaNetProcessConfigurationsApi.md#rosettaNetProcessConfigurationsListByIntegrationAccounts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/rosettanetprocessconfigurations |  |


<a id="rosettaNetProcessConfigurationsCreateOrUpdate"></a>
# **rosettaNetProcessConfigurationsCreateOrUpdate**
> IntegrationAccountRosettaNetProcessConfiguration rosettaNetProcessConfigurationsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion, rosettaNetProcessConfiguration)



Creates or updates an integration account RosettaNetProcessConfiguration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountRosettaNetProcessConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountRosettaNetProcessConfigurationsApi apiInstance = new IntegrationAccountRosettaNetProcessConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String rosettaNetProcessConfigurationName = "rosettaNetProcessConfigurationName_example"; // String | The integration account RosettaNet ProcessConfiguration name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationAccountRosettaNetProcessConfiguration rosettaNetProcessConfiguration = new IntegrationAccountRosettaNetProcessConfiguration(); // IntegrationAccountRosettaNetProcessConfiguration | The integration account RosettaNet ProcessConfiguration.
    try {
      IntegrationAccountRosettaNetProcessConfiguration result = apiInstance.rosettaNetProcessConfigurationsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion, rosettaNetProcessConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountRosettaNetProcessConfigurationsApi#rosettaNetProcessConfigurationsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **rosettaNetProcessConfigurationName** | **String**| The integration account RosettaNet ProcessConfiguration name. | |
| **apiVersion** | **String**| The API version. | |
| **rosettaNetProcessConfiguration** | [**IntegrationAccountRosettaNetProcessConfiguration**](IntegrationAccountRosettaNetProcessConfiguration.md)| The integration account RosettaNet ProcessConfiguration. | |

### Return type

[**IntegrationAccountRosettaNetProcessConfiguration**](IntegrationAccountRosettaNetProcessConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="rosettaNetProcessConfigurationsDelete"></a>
# **rosettaNetProcessConfigurationsDelete**
> rosettaNetProcessConfigurationsDelete(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion)



Deletes an integration account RosettaNet ProcessConfiguration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountRosettaNetProcessConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountRosettaNetProcessConfigurationsApi apiInstance = new IntegrationAccountRosettaNetProcessConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String rosettaNetProcessConfigurationName = "rosettaNetProcessConfigurationName_example"; // String | The integration account RosettaNetProcessConfiguration name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.rosettaNetProcessConfigurationsDelete(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountRosettaNetProcessConfigurationsApi#rosettaNetProcessConfigurationsDelete");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **rosettaNetProcessConfigurationName** | **String**| The integration account RosettaNetProcessConfiguration name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |

<a id="rosettaNetProcessConfigurationsGet"></a>
# **rosettaNetProcessConfigurationsGet**
> IntegrationAccountRosettaNetProcessConfiguration rosettaNetProcessConfigurationsGet(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion)



Gets an integration account RosettaNetProcessConfiguration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountRosettaNetProcessConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountRosettaNetProcessConfigurationsApi apiInstance = new IntegrationAccountRosettaNetProcessConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String rosettaNetProcessConfigurationName = "rosettaNetProcessConfigurationName_example"; // String | The integration account RosettaNetProcessConfiguration name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationAccountRosettaNetProcessConfiguration result = apiInstance.rosettaNetProcessConfigurationsGet(subscriptionId, resourceGroupName, integrationAccountName, rosettaNetProcessConfigurationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountRosettaNetProcessConfigurationsApi#rosettaNetProcessConfigurationsGet");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **rosettaNetProcessConfigurationName** | **String**| The integration account RosettaNetProcessConfiguration name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationAccountRosettaNetProcessConfiguration**](IntegrationAccountRosettaNetProcessConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="rosettaNetProcessConfigurationsListByIntegrationAccounts"></a>
# **rosettaNetProcessConfigurationsListByIntegrationAccounts**
> IntegrationAccountRosettaNetProcessConfigurationListResult rosettaNetProcessConfigurationsListByIntegrationAccounts(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top, $filter)



Gets a list of integration account RosettaNet process configurations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountRosettaNetProcessConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountRosettaNetProcessConfigurationsApi apiInstance = new IntegrationAccountRosettaNetProcessConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      IntegrationAccountRosettaNetProcessConfigurationListResult result = apiInstance.rosettaNetProcessConfigurationsListByIntegrationAccounts(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountRosettaNetProcessConfigurationsApi#rosettaNetProcessConfigurationsListByIntegrationAccounts");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**IntegrationAccountRosettaNetProcessConfigurationListResult**](IntegrationAccountRosettaNetProcessConfigurationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


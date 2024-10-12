# IntegrationAccountBatchConfigurationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationAccountBatchConfigurationsCreateOrUpdate**](IntegrationAccountBatchConfigurationsApi.md#integrationAccountBatchConfigurationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/batchConfigurations/{batchConfigurationName} |  |
| [**integrationAccountBatchConfigurationsDelete**](IntegrationAccountBatchConfigurationsApi.md#integrationAccountBatchConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/batchConfigurations/{batchConfigurationName} |  |
| [**integrationAccountBatchConfigurationsGet**](IntegrationAccountBatchConfigurationsApi.md#integrationAccountBatchConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/batchConfigurations/{batchConfigurationName} |  |
| [**integrationAccountBatchConfigurationsList**](IntegrationAccountBatchConfigurationsApi.md#integrationAccountBatchConfigurationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/batchConfigurations |  |


<a id="integrationAccountBatchConfigurationsCreateOrUpdate"></a>
# **integrationAccountBatchConfigurationsCreateOrUpdate**
> BatchConfiguration integrationAccountBatchConfigurationsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion, batchConfiguration)



Create or update a batch configuration for an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountBatchConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountBatchConfigurationsApi apiInstance = new IntegrationAccountBatchConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String batchConfigurationName = "batchConfigurationName_example"; // String | The batch configuration name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    BatchConfiguration batchConfiguration = new BatchConfiguration(); // BatchConfiguration | The batch configuration.
    try {
      BatchConfiguration result = apiInstance.integrationAccountBatchConfigurationsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion, batchConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountBatchConfigurationsApi#integrationAccountBatchConfigurationsCreateOrUpdate");
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
| **batchConfigurationName** | **String**| The batch configuration name. | |
| **apiVersion** | **String**| The API version. | |
| **batchConfiguration** | [**BatchConfiguration**](BatchConfiguration.md)| The batch configuration. | |

### Return type

[**BatchConfiguration**](BatchConfiguration.md)

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
| **0** | Error response describing why the operation failed. |  -  |

<a id="integrationAccountBatchConfigurationsDelete"></a>
# **integrationAccountBatchConfigurationsDelete**
> integrationAccountBatchConfigurationsDelete(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion)



Delete a batch configuration for an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountBatchConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountBatchConfigurationsApi apiInstance = new IntegrationAccountBatchConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String batchConfigurationName = "batchConfigurationName_example"; // String | The batch configuration name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationAccountBatchConfigurationsDelete(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountBatchConfigurationsApi#integrationAccountBatchConfigurationsDelete");
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
| **batchConfigurationName** | **String**| The batch configuration name. | |
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
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="integrationAccountBatchConfigurationsGet"></a>
# **integrationAccountBatchConfigurationsGet**
> BatchConfiguration integrationAccountBatchConfigurationsGet(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion)



Get a batch configuration for an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountBatchConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountBatchConfigurationsApi apiInstance = new IntegrationAccountBatchConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String batchConfigurationName = "batchConfigurationName_example"; // String | The batch configuration name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      BatchConfiguration result = apiInstance.integrationAccountBatchConfigurationsGet(subscriptionId, resourceGroupName, integrationAccountName, batchConfigurationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountBatchConfigurationsApi#integrationAccountBatchConfigurationsGet");
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
| **batchConfigurationName** | **String**| The batch configuration name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**BatchConfiguration**](BatchConfiguration.md)

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

<a id="integrationAccountBatchConfigurationsList"></a>
# **integrationAccountBatchConfigurationsList**
> BatchConfigurationCollection integrationAccountBatchConfigurationsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion)



List the batch configurations for an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountBatchConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountBatchConfigurationsApi apiInstance = new IntegrationAccountBatchConfigurationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      BatchConfigurationCollection result = apiInstance.integrationAccountBatchConfigurationsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountBatchConfigurationsApi#integrationAccountBatchConfigurationsList");
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

### Return type

[**BatchConfigurationCollection**](BatchConfigurationCollection.md)

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


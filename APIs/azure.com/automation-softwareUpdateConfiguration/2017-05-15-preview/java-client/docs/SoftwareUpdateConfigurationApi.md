# SoftwareUpdateConfigurationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**softwareUpdateConfigurationsCreate**](SoftwareUpdateConfigurationApi.md#softwareUpdateConfigurationsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurations/{softwareUpdateConfigurationName} |  |
| [**softwareUpdateConfigurationsDelete**](SoftwareUpdateConfigurationApi.md#softwareUpdateConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurations/{softwareUpdateConfigurationName} |  |
| [**softwareUpdateConfigurationsGetByName**](SoftwareUpdateConfigurationApi.md#softwareUpdateConfigurationsGetByName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurations/{softwareUpdateConfigurationName} |  |
| [**softwareUpdateConfigurationsList**](SoftwareUpdateConfigurationApi.md#softwareUpdateConfigurationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurations |  |


<a id="softwareUpdateConfigurationsCreate"></a>
# **softwareUpdateConfigurationsCreate**
> SoftwareUpdateConfiguration softwareUpdateConfigurationsCreate(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, parameters, clientRequestId)



Create a new software update configuration with the name given in the URI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoftwareUpdateConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SoftwareUpdateConfigurationApi apiInstance = new SoftwareUpdateConfigurationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String softwareUpdateConfigurationName = "softwareUpdateConfigurationName_example"; // String | The name of the software update configuration to be created.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    SoftwareUpdateConfiguration parameters = new SoftwareUpdateConfiguration(); // SoftwareUpdateConfiguration | Request body.
    String clientRequestId = "clientRequestId_example"; // String | Identifies this specific client request.
    try {
      SoftwareUpdateConfiguration result = apiInstance.softwareUpdateConfigurationsCreate(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, parameters, clientRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareUpdateConfigurationApi#softwareUpdateConfigurationsCreate");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **softwareUpdateConfigurationName** | **String**| The name of the software update configuration to be created. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**SoftwareUpdateConfiguration**](SoftwareUpdateConfiguration.md)| Request body. | |
| **clientRequestId** | **String**| Identifies this specific client request. | [optional] |

### Return type

[**SoftwareUpdateConfiguration**](SoftwareUpdateConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Software update configuration with the same name and properties already exists. |  -  |
| **201** | Software update configuration is created. |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

<a id="softwareUpdateConfigurationsDelete"></a>
# **softwareUpdateConfigurationsDelete**
> softwareUpdateConfigurationsDelete(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, clientRequestId)



delete a specific software update configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoftwareUpdateConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SoftwareUpdateConfigurationApi apiInstance = new SoftwareUpdateConfigurationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String softwareUpdateConfigurationName = "softwareUpdateConfigurationName_example"; // String | The name of the software update configuration to be created.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String clientRequestId = "clientRequestId_example"; // String | Identifies this specific client request.
    try {
      apiInstance.softwareUpdateConfigurationsDelete(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, clientRequestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareUpdateConfigurationApi#softwareUpdateConfigurationsDelete");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **softwareUpdateConfigurationName** | **String**| The name of the software update configuration to be created. | |
| **apiVersion** | **String**| Client Api Version. | |
| **clientRequestId** | **String**| Identifies this specific client request. | [optional] |

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
| **200** | The software update configuration has been deleted. |  -  |
| **204** | The software update configuration does not exist. |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

<a id="softwareUpdateConfigurationsGetByName"></a>
# **softwareUpdateConfigurationsGetByName**
> SoftwareUpdateConfiguration softwareUpdateConfigurationsGetByName(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, clientRequestId)



Get a single software update configuration by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoftwareUpdateConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SoftwareUpdateConfigurationApi apiInstance = new SoftwareUpdateConfigurationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String softwareUpdateConfigurationName = "softwareUpdateConfigurationName_example"; // String | The name of the software update configuration to be created.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String clientRequestId = "clientRequestId_example"; // String | Identifies this specific client request.
    try {
      SoftwareUpdateConfiguration result = apiInstance.softwareUpdateConfigurationsGetByName(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, clientRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareUpdateConfigurationApi#softwareUpdateConfigurationsGetByName");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **softwareUpdateConfigurationName** | **String**| The name of the software update configuration to be created. | |
| **apiVersion** | **String**| Client Api Version. | |
| **clientRequestId** | **String**| Identifies this specific client request. | [optional] |

### Return type

[**SoftwareUpdateConfiguration**](SoftwareUpdateConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single software update configuration. |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

<a id="softwareUpdateConfigurationsList"></a>
# **softwareUpdateConfigurationsList**
> SoftwareUpdateConfigurationListResult softwareUpdateConfigurationsList(subscriptionId, resourceGroupName, automationAccountName, apiVersion, clientRequestId, $filter)



Get all software update configurations for the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoftwareUpdateConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SoftwareUpdateConfigurationApi apiInstance = new SoftwareUpdateConfigurationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String clientRequestId = "clientRequestId_example"; // String | Identifies this specific client request.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      SoftwareUpdateConfigurationListResult result = apiInstance.softwareUpdateConfigurationsList(subscriptionId, resourceGroupName, automationAccountName, apiVersion, clientRequestId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareUpdateConfigurationApi#softwareUpdateConfigurationsList");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **apiVersion** | **String**| Client Api Version. | |
| **clientRequestId** | **String**| Identifies this specific client request. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**SoftwareUpdateConfigurationListResult**](SoftwareUpdateConfigurationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return list of software update configurations. |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |


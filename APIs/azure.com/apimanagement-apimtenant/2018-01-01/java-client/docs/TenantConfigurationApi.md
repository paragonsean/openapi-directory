# TenantConfigurationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tenantConfigurationDeploy**](TenantConfigurationApi.md#tenantConfigurationDeploy) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{configurationName}/deploy |  |
| [**tenantConfigurationSave**](TenantConfigurationApi.md#tenantConfigurationSave) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{configurationName}/save |  |
| [**tenantConfigurationValidate**](TenantConfigurationApi.md#tenantConfigurationValidate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/tenant/{configurationName}/validate |  |


<a id="tenantConfigurationDeploy"></a>
# **tenantConfigurationDeploy**
> OperationResultContract tenantConfigurationDeploy(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters)



This operation applies changes from the specified Git branch to the configuration database. This is a long running operation and could take several minutes to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TenantConfigurationApi apiInstance = new TenantConfigurationApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String configurationName = "configuration"; // String | The identifier of the Git Configuration Operation.
    DeployConfigurationParameters parameters = new DeployConfigurationParameters(); // DeployConfigurationParameters | Deploy Configuration parameters.
    try {
      OperationResultContract result = apiInstance.tenantConfigurationDeploy(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantConfigurationApi#tenantConfigurationDeploy");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **configurationName** | **String**| The identifier of the Git Configuration Operation. | [enum: configuration] |
| **parameters** | [**DeployConfigurationParameters**](DeployConfigurationParameters.md)| Deploy Configuration parameters. | |

### Return type

[**OperationResultContract**](OperationResultContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of applying changes from Git branch to database. |  -  |
| **202** | Accepted: Location header contains the URL where the status of the long running operation can be checked. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tenantConfigurationSave"></a>
# **tenantConfigurationSave**
> OperationResultContract tenantConfigurationSave(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters)



This operation creates a commit with the current configuration snapshot to the specified branch in the repository. This is a long running operation and could take several minutes to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TenantConfigurationApi apiInstance = new TenantConfigurationApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String configurationName = "configuration"; // String | The identifier of the Git Configuration Operation.
    SaveConfigurationParameter parameters = new SaveConfigurationParameter(); // SaveConfigurationParameter | Save Configuration parameters.
    try {
      OperationResultContract result = apiInstance.tenantConfigurationSave(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantConfigurationApi#tenantConfigurationSave");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **configurationName** | **String**| The identifier of the Git Configuration Operation. | [enum: configuration] |
| **parameters** | [**SaveConfigurationParameter**](SaveConfigurationParameter.md)| Save Configuration parameters. | |

### Return type

[**OperationResultContract**](OperationResultContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of creating a commit in the repository. |  -  |
| **202** | Accepted: Location header contains the URL where the status of the long running operation can be checked. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tenantConfigurationValidate"></a>
# **tenantConfigurationValidate**
> OperationResultContract tenantConfigurationValidate(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters)



This operation validates the changes in the specified Git branch. This is a long running operation and could take several minutes to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TenantConfigurationApi apiInstance = new TenantConfigurationApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String configurationName = "configuration"; // String | The identifier of the Git Configuration Operation.
    DeployConfigurationParameters parameters = new DeployConfigurationParameters(); // DeployConfigurationParameters | Validate Configuration parameters.
    try {
      OperationResultContract result = apiInstance.tenantConfigurationValidate(resourceGroupName, serviceName, apiVersion, subscriptionId, configurationName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantConfigurationApi#tenantConfigurationValidate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **configurationName** | **String**| The identifier of the Git Configuration Operation. | [enum: configuration] |
| **parameters** | [**DeployConfigurationParameters**](DeployConfigurationParameters.md)| Validate Configuration parameters. | |

### Return type

[**OperationResultContract**](OperationResultContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of validating the changes in the specified Git branch. |  -  |
| **202** | Accepted: Location header contains the URL where the status of the long running operation can be checked. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


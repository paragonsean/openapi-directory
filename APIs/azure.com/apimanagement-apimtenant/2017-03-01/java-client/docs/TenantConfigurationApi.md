# TenantConfigurationApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tenantConfigurationDeploy**](TenantConfigurationApi.md#tenantConfigurationDeploy) | **POST** /tenant/{configurationName}/deploy |  |
| [**tenantConfigurationSave**](TenantConfigurationApi.md#tenantConfigurationSave) | **POST** /tenant/{configurationName}/save |  |
| [**tenantConfigurationValidate**](TenantConfigurationApi.md#tenantConfigurationValidate) | **POST** /tenant/{configurationName}/validate |  |


<a id="tenantConfigurationDeploy"></a>
# **tenantConfigurationDeploy**
> OperationResultContract tenantConfigurationDeploy(apiVersion, configurationName, parameters)



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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantConfigurationApi apiInstance = new TenantConfigurationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String configurationName = "configuration"; // String | The identifier of the Git Configuration Operation.
    DeployConfigurationParameters parameters = new DeployConfigurationParameters(); // DeployConfigurationParameters | Deploy Configuration parameters.
    try {
      OperationResultContract result = apiInstance.tenantConfigurationDeploy(apiVersion, configurationName, parameters);
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **configurationName** | **String**| The identifier of the Git Configuration Operation. | [enum: configuration] |
| **parameters** | [**DeployConfigurationParameters**](DeployConfigurationParameters.md)| Deploy Configuration parameters. | |

### Return type

[**OperationResultContract**](OperationResultContract.md)

### Authorization

[apim_key](../README.md#apim_key)

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
> OperationResultContract tenantConfigurationSave(apiVersion, configurationName, parameters)



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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantConfigurationApi apiInstance = new TenantConfigurationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String configurationName = "configuration"; // String | The identifier of the Git Configuration Operation.
    SaveConfigurationParameter parameters = new SaveConfigurationParameter(); // SaveConfigurationParameter | Save Configuration parameters.
    try {
      OperationResultContract result = apiInstance.tenantConfigurationSave(apiVersion, configurationName, parameters);
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **configurationName** | **String**| The identifier of the Git Configuration Operation. | [enum: configuration] |
| **parameters** | [**SaveConfigurationParameter**](SaveConfigurationParameter.md)| Save Configuration parameters. | |

### Return type

[**OperationResultContract**](OperationResultContract.md)

### Authorization

[apim_key](../README.md#apim_key)

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
> OperationResultContract tenantConfigurationValidate(apiVersion, configurationName, parameters)



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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantConfigurationApi apiInstance = new TenantConfigurationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String configurationName = "configuration"; // String | The identifier of the Git Configuration Operation.
    DeployConfigurationParameters parameters = new DeployConfigurationParameters(); // DeployConfigurationParameters | Validate Configuration parameters.
    try {
      OperationResultContract result = apiInstance.tenantConfigurationValidate(apiVersion, configurationName, parameters);
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **configurationName** | **String**| The identifier of the Git Configuration Operation. | [enum: configuration] |
| **parameters** | [**DeployConfigurationParameters**](DeployConfigurationParameters.md)| Validate Configuration parameters. | |

### Return type

[**OperationResultContract**](OperationResultContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of validating the changes in the specified Git branch. |  -  |
| **202** | Accepted: Location header contains the URL where the status of the long running operation can be checked. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


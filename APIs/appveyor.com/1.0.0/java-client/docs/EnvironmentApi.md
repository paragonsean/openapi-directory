# EnvironmentApi

All URIs are relative to *https://ci.appveyor.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addEnvironment**](EnvironmentApi.md#addEnvironment) | **POST** /environments | Add environment |
| [**deleteEnvironment**](EnvironmentApi.md#deleteEnvironment) | **DELETE** /environments/{deploymentEnvironmentId} | Delete environment |
| [**getEnvironmentDeployments**](EnvironmentApi.md#getEnvironmentDeployments) | **GET** /environments/{deploymentEnvironmentId}/deployments | Get environment deployments |
| [**getEnvironmentSettings**](EnvironmentApi.md#getEnvironmentSettings) | **GET** /environments/{deploymentEnvironmentId}/settings | Get environment settings |
| [**getEnvironments**](EnvironmentApi.md#getEnvironments) | **GET** /environments | Get environments |
| [**updateEnvironment**](EnvironmentApi.md#updateEnvironment) | **PUT** /environments | Update environment |


<a id="addEnvironment"></a>
# **addEnvironment**
> DeploymentEnvironmentWithSettings addEnvironment(body)

Add environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    EnvironmentApi apiInstance = new EnvironmentApi(defaultClient);
    DeploymentEnvironmentAddition body = new DeploymentEnvironmentAddition(); // DeploymentEnvironmentAddition | 
    try {
      DeploymentEnvironmentWithSettings result = apiInstance.addEnvironment(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentApi#addEnvironment");
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
| **body** | [**DeploymentEnvironmentAddition**](DeploymentEnvironmentAddition.md)|  | |

### Return type

[**DeploymentEnvironmentWithSettings**](DeploymentEnvironmentWithSettings.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="deleteEnvironment"></a>
# **deleteEnvironment**
> deleteEnvironment(deploymentEnvironmentId)

Delete environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    EnvironmentApi apiInstance = new EnvironmentApi(defaultClient);
    Integer deploymentEnvironmentId = 56; // Integer | Deployment Environment ID (`deploymentEnvironmentId` property of `DeploymentEnvironment`) 
    try {
      apiInstance.deleteEnvironment(deploymentEnvironmentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentApi#deleteEnvironment");
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
| **deploymentEnvironmentId** | **Integer**| Deployment Environment ID (&#x60;deploymentEnvironmentId&#x60; property of &#x60;DeploymentEnvironment&#x60;)  | |

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="getEnvironmentDeployments"></a>
# **getEnvironmentDeployments**
> DeploymentEnvironmentDeploymentsResults getEnvironmentDeployments(deploymentEnvironmentId)

Get environment deployments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    EnvironmentApi apiInstance = new EnvironmentApi(defaultClient);
    Integer deploymentEnvironmentId = 56; // Integer | Deployment Environment ID (`deploymentEnvironmentId` property of `DeploymentEnvironment`) 
    try {
      DeploymentEnvironmentDeploymentsResults result = apiInstance.getEnvironmentDeployments(deploymentEnvironmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentApi#getEnvironmentDeployments");
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
| **deploymentEnvironmentId** | **Integer**| Deployment Environment ID (&#x60;deploymentEnvironmentId&#x60; property of &#x60;DeploymentEnvironment&#x60;)  | |

### Return type

[**DeploymentEnvironmentDeploymentsResults**](DeploymentEnvironmentDeploymentsResults.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getEnvironmentSettings"></a>
# **getEnvironmentSettings**
> DeploymentEnvironmentSettingsResults getEnvironmentSettings(deploymentEnvironmentId)

Get environment settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    EnvironmentApi apiInstance = new EnvironmentApi(defaultClient);
    Integer deploymentEnvironmentId = 56; // Integer | Deployment Environment ID (`deploymentEnvironmentId` property of `DeploymentEnvironment`) 
    try {
      DeploymentEnvironmentSettingsResults result = apiInstance.getEnvironmentSettings(deploymentEnvironmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentApi#getEnvironmentSettings");
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
| **deploymentEnvironmentId** | **Integer**| Deployment Environment ID (&#x60;deploymentEnvironmentId&#x60; property of &#x60;DeploymentEnvironment&#x60;)  | |

### Return type

[**DeploymentEnvironmentSettingsResults**](DeploymentEnvironmentSettingsResults.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getEnvironments"></a>
# **getEnvironments**
> List&lt;DeploymentEnvironmentLookupModel&gt; getEnvironments()

Get environments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    EnvironmentApi apiInstance = new EnvironmentApi(defaultClient);
    try {
      List<DeploymentEnvironmentLookupModel> result = apiInstance.getEnvironments();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentApi#getEnvironments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;DeploymentEnvironmentLookupModel&gt;**](DeploymentEnvironmentLookupModel.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="updateEnvironment"></a>
# **updateEnvironment**
> DeploymentEnvironmentWithSettings updateEnvironment(body)

Update environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    EnvironmentApi apiInstance = new EnvironmentApi(defaultClient);
    DeploymentEnvironmentWithSettings body = new DeploymentEnvironmentWithSettings(); // DeploymentEnvironmentWithSettings | 
    try {
      DeploymentEnvironmentWithSettings result = apiInstance.updateEnvironment(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentApi#updateEnvironment");
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
| **body** | [**DeploymentEnvironmentWithSettings**](DeploymentEnvironmentWithSettings.md)|  | |

### Return type

[**DeploymentEnvironmentWithSettings**](DeploymentEnvironmentWithSettings.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |


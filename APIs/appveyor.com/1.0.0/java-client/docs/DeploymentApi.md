# DeploymentApi

All URIs are relative to *https://ci.appveyor.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelDeployment**](DeploymentApi.md#cancelDeployment) | **PUT** /deployments/stop | Cancel deployment |
| [**getDeployment**](DeploymentApi.md#getDeployment) | **GET** /deployments/{deploymentId} | Get deployment |
| [**startDeployment**](DeploymentApi.md#startDeployment) | **POST** /deployments | Start deployment |


<a id="cancelDeployment"></a>
# **cancelDeployment**
> cancelDeployment(body)

Cancel deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    DeploymentApi apiInstance = new DeploymentApi(defaultClient);
    DeploymentCancellation body = new DeploymentCancellation(); // DeploymentCancellation | 
    try {
      apiInstance.cancelDeployment(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentApi#cancelDeployment");
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
| **body** | [**DeploymentCancellation**](DeploymentCancellation.md)|  | |

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="getDeployment"></a>
# **getDeployment**
> ProjectDeployment getDeployment(deploymentId)

Get deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    DeploymentApi apiInstance = new DeploymentApi(defaultClient);
    Integer deploymentId = 56; // Integer | Deployment ID (`deploymentId` property of `Deployment`)
    try {
      ProjectDeployment result = apiInstance.getDeployment(deploymentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentApi#getDeployment");
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
| **deploymentId** | **Integer**| Deployment ID (&#x60;deploymentId&#x60; property of &#x60;Deployment&#x60;) | |

### Return type

[**ProjectDeployment**](ProjectDeployment.md)

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

<a id="startDeployment"></a>
# **startDeployment**
> Deployment startDeployment(body)

Start deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    DeploymentApi apiInstance = new DeploymentApi(defaultClient);
    DeploymentStartRequest body = new DeploymentStartRequest(); // DeploymentStartRequest | 
    try {
      Deployment result = apiInstance.startDeployment(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentApi#startDeployment");
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
| **body** | [**DeploymentStartRequest**](DeploymentStartRequest.md)|  | |

### Return type

[**Deployment**](Deployment.md)

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


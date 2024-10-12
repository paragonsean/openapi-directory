# DeploymentScriptsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deploymentScriptsCreate**](DeploymentScriptsApi.md#deploymentScriptsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName} |  |
| [**deploymentScriptsDelete**](DeploymentScriptsApi.md#deploymentScriptsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName} |  |
| [**deploymentScriptsGet**](DeploymentScriptsApi.md#deploymentScriptsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName} |  |
| [**deploymentScriptsGetLogs**](DeploymentScriptsApi.md#deploymentScriptsGetLogs) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}/logs |  |
| [**deploymentScriptsGetLogsDefault**](DeploymentScriptsApi.md#deploymentScriptsGetLogsDefault) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}/logs/default |  |
| [**deploymentScriptsListByResourceGroup**](DeploymentScriptsApi.md#deploymentScriptsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts |  |
| [**deploymentScriptsListBySubscription**](DeploymentScriptsApi.md#deploymentScriptsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deploymentScripts |  |
| [**deploymentScriptsUpdate**](DeploymentScriptsApi.md#deploymentScriptsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName} |  |


<a id="deploymentScriptsCreate"></a>
# **deploymentScriptsCreate**
> DeploymentScript deploymentScriptsCreate(subscriptionId, resourceGroupName, scriptName, apiVersion, deploymentScript)



Creates a deployment script.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentScriptsApi apiInstance = new DeploymentScriptsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String scriptName = "scriptName_example"; // String | Name of the deployment script.
    String apiVersion = "apiVersion_example"; // String | Client Api version.
    DeploymentScript deploymentScript = new DeploymentScript(); // DeploymentScript | Deployment script supplied to the operation.
    try {
      DeploymentScript result = apiInstance.deploymentScriptsCreate(subscriptionId, resourceGroupName, scriptName, apiVersion, deploymentScript);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentScriptsApi#deploymentScriptsCreate");
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
| **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **scriptName** | **String**| Name of the deployment script. | |
| **apiVersion** | **String**| Client Api version. | |
| **deploymentScript** | [**DeploymentScript**](DeploymentScript.md)| Deployment script supplied to the operation. | |

### Return type

[**DeploymentScript**](DeploymentScript.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Deployment script is updated. |  -  |
| **201** | Created -- Deployment script created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentScriptsDelete"></a>
# **deploymentScriptsDelete**
> deploymentScriptsDelete(subscriptionId, resourceGroupName, scriptName, apiVersion)



Deletes a deployment script. When operation completes, status code 200 returned without content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentScriptsApi apiInstance = new DeploymentScriptsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String scriptName = "scriptName_example"; // String | Name of the deployment script.
    String apiVersion = "apiVersion_example"; // String | Client Api version.
    try {
      apiInstance.deploymentScriptsDelete(subscriptionId, resourceGroupName, scriptName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentScriptsApi#deploymentScriptsDelete");
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
| **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **scriptName** | **String**| Name of the deployment script. | |
| **apiVersion** | **String**| Client Api version. | |

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
| **200** | OK -- Deployment script deleted. |  -  |
| **204** | Deployment script does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentScriptsGet"></a>
# **deploymentScriptsGet**
> DeploymentScript deploymentScriptsGet(subscriptionId, resourceGroupName, scriptName, apiVersion)



Gets a deployment script with a given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentScriptsApi apiInstance = new DeploymentScriptsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String scriptName = "scriptName_example"; // String | Name of the deployment script.
    String apiVersion = "apiVersion_example"; // String | Client Api version.
    try {
      DeploymentScript result = apiInstance.deploymentScriptsGet(subscriptionId, resourceGroupName, scriptName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentScriptsApi#deploymentScriptsGet");
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
| **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **scriptName** | **String**| Name of the deployment script. | |
| **apiVersion** | **String**| Client Api version. | |

### Return type

[**DeploymentScript**](DeploymentScript.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Returns information about the deployment script. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentScriptsGetLogs"></a>
# **deploymentScriptsGetLogs**
> ScriptLogsList deploymentScriptsGetLogs(subscriptionId, resourceGroupName, scriptName, apiVersion)



Gets deployment script logs for a given deployment script name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentScriptsApi apiInstance = new DeploymentScriptsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String scriptName = "scriptName_example"; // String | Name of the deployment script.
    String apiVersion = "apiVersion_example"; // String | Client Api version.
    try {
      ScriptLogsList result = apiInstance.deploymentScriptsGetLogs(subscriptionId, resourceGroupName, scriptName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentScriptsApi#deploymentScriptsGetLogs");
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
| **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **scriptName** | **String**| Name of the deployment script. | |
| **apiVersion** | **String**| Client Api version. | |

### Return type

[**ScriptLogsList**](ScriptLogsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Returns deployment script logs if available. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentScriptsGetLogsDefault"></a>
# **deploymentScriptsGetLogsDefault**
> ScriptLog deploymentScriptsGetLogsDefault(subscriptionId, resourceGroupName, scriptName, apiVersion)



Gets deployment script logs for a given deployment script name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentScriptsApi apiInstance = new DeploymentScriptsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String scriptName = "scriptName_example"; // String | Name of the deployment script.
    String apiVersion = "apiVersion_example"; // String | Client Api version.
    try {
      ScriptLog result = apiInstance.deploymentScriptsGetLogsDefault(subscriptionId, resourceGroupName, scriptName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentScriptsApi#deploymentScriptsGetLogsDefault");
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
| **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **scriptName** | **String**| Name of the deployment script. | |
| **apiVersion** | **String**| Client Api version. | |

### Return type

[**ScriptLog**](ScriptLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Returns deployment script logs if available. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentScriptsListByResourceGroup"></a>
# **deploymentScriptsListByResourceGroup**
> DeploymentScriptListResult deploymentScriptsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists deployments scripts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentScriptsApi apiInstance = new DeploymentScriptsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api version.
    try {
      DeploymentScriptListResult result = apiInstance.deploymentScriptsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentScriptsApi#deploymentScriptsListByResourceGroup");
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
| **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| Client Api version. | |

### Return type

[**DeploymentScriptListResult**](DeploymentScriptListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Returns a list of deployment scripts. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentScriptsListBySubscription"></a>
# **deploymentScriptsListBySubscription**
> DeploymentScriptListResult deploymentScriptsListBySubscription(subscriptionId, apiVersion)



Lists all deployment scripts for a given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentScriptsApi apiInstance = new DeploymentScriptsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api version.
    try {
      DeploymentScriptListResult result = apiInstance.deploymentScriptsListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentScriptsApi#deploymentScriptsListBySubscription");
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
| **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api version. | |

### Return type

[**DeploymentScriptListResult**](DeploymentScriptListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Returns a list of deployment scripts. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deploymentScriptsUpdate"></a>
# **deploymentScriptsUpdate**
> DeploymentScript deploymentScriptsUpdate(subscriptionId, resourceGroupName, scriptName, apiVersion, deploymentScript)



Updates deployment script tags with specified values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeploymentScriptsApi apiInstance = new DeploymentScriptsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String scriptName = "scriptName_example"; // String | Name of the deployment script.
    String apiVersion = "apiVersion_example"; // String | Client Api version.
    DeploymentScriptUpdateParameter deploymentScript = new DeploymentScriptUpdateParameter(); // DeploymentScriptUpdateParameter | Deployment script resource with the tags to be updated.
    try {
      DeploymentScript result = apiInstance.deploymentScriptsUpdate(subscriptionId, resourceGroupName, scriptName, apiVersion, deploymentScript);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentScriptsApi#deploymentScriptsUpdate");
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
| **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **scriptName** | **String**| Name of the deployment script. | |
| **apiVersion** | **String**| Client Api version. | |
| **deploymentScript** | [**DeploymentScriptUpdateParameter**](DeploymentScriptUpdateParameter.md)| Deployment script resource with the tags to be updated. | [optional] |

### Return type

[**DeploymentScript**](DeploymentScript.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Deployment script tags are updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


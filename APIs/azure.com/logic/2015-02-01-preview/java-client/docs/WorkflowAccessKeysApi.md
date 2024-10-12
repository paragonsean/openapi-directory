# WorkflowAccessKeysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workflowAccessKeysCreateOrUpdate**](WorkflowAccessKeysApi.md#workflowAccessKeysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys/{accessKeyName} |  |
| [**workflowAccessKeysDelete**](WorkflowAccessKeysApi.md#workflowAccessKeysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys/{accessKeyName} |  |
| [**workflowAccessKeysGet**](WorkflowAccessKeysApi.md#workflowAccessKeysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys/{accessKeyName} |  |
| [**workflowAccessKeysList**](WorkflowAccessKeysApi.md#workflowAccessKeysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys |  |
| [**workflowAccessKeysListSecretKeys**](WorkflowAccessKeysApi.md#workflowAccessKeysListSecretKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys/{accessKeyName}/list |  |
| [**workflowAccessKeysRegenerateSecretKey**](WorkflowAccessKeysApi.md#workflowAccessKeysRegenerateSecretKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys/{accessKeyName}/regenerate |  |


<a id="workflowAccessKeysCreateOrUpdate"></a>
# **workflowAccessKeysCreateOrUpdate**
> WorkflowAccessKey workflowAccessKeysCreateOrUpdate(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, workflowAccesskey)



Creates or updates a workflow access key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowAccessKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowAccessKeysApi apiInstance = new WorkflowAccessKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String accessKeyName = "accessKeyName_example"; // String | The workflow access key name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    WorkflowAccessKey workflowAccesskey = new WorkflowAccessKey(); // WorkflowAccessKey | The workflow access key.
    try {
      WorkflowAccessKey result = apiInstance.workflowAccessKeysCreateOrUpdate(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, workflowAccesskey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAccessKeysApi#workflowAccessKeysCreateOrUpdate");
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
| **workflowName** | **String**| The workflow name. | |
| **accessKeyName** | **String**| The workflow access key name. | |
| **apiVersion** | **String**| The API version. | |
| **workflowAccesskey** | [**WorkflowAccessKey**](WorkflowAccessKey.md)| The workflow access key. | |

### Return type

[**WorkflowAccessKey**](WorkflowAccessKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="workflowAccessKeysDelete"></a>
# **workflowAccessKeysDelete**
> workflowAccessKeysDelete(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion)



Deletes a workflow access key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowAccessKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowAccessKeysApi apiInstance = new WorkflowAccessKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String accessKeyName = "accessKeyName_example"; // String | The workflow access key name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.workflowAccessKeysDelete(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAccessKeysApi#workflowAccessKeysDelete");
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
| **workflowName** | **String**| The workflow name. | |
| **accessKeyName** | **String**| The workflow access key name. | |
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

<a id="workflowAccessKeysGet"></a>
# **workflowAccessKeysGet**
> WorkflowAccessKey workflowAccessKeysGet(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion)



Gets a workflow access key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowAccessKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowAccessKeysApi apiInstance = new WorkflowAccessKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String accessKeyName = "accessKeyName_example"; // String | The workflow access key name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowAccessKey result = apiInstance.workflowAccessKeysGet(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAccessKeysApi#workflowAccessKeysGet");
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
| **workflowName** | **String**| The workflow name. | |
| **accessKeyName** | **String**| The workflow access key name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowAccessKey**](WorkflowAccessKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowAccessKeysList"></a>
# **workflowAccessKeysList**
> WorkflowAccessKeyListResult workflowAccessKeysList(subscriptionId, resourceGroupName, workflowName, apiVersion, $top)



Gets a list of workflow access keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowAccessKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowAccessKeysApi apiInstance = new WorkflowAccessKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    try {
      WorkflowAccessKeyListResult result = apiInstance.workflowAccessKeysList(subscriptionId, resourceGroupName, workflowName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAccessKeysApi#workflowAccessKeysList");
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
| **workflowName** | **String**| The workflow name. | |
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |

### Return type

[**WorkflowAccessKeyListResult**](WorkflowAccessKeyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowAccessKeysListSecretKeys"></a>
# **workflowAccessKeysListSecretKeys**
> WorkflowSecretKeys workflowAccessKeysListSecretKeys(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion)



Lists secret keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowAccessKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowAccessKeysApi apiInstance = new WorkflowAccessKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String accessKeyName = "accessKeyName_example"; // String | The workflow access key name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowSecretKeys result = apiInstance.workflowAccessKeysListSecretKeys(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAccessKeysApi#workflowAccessKeysListSecretKeys");
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
| **workflowName** | **String**| The workflow name. | |
| **accessKeyName** | **String**| The workflow access key name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowSecretKeys**](WorkflowSecretKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowAccessKeysRegenerateSecretKey"></a>
# **workflowAccessKeysRegenerateSecretKey**
> WorkflowSecretKeys workflowAccessKeysRegenerateSecretKey(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, parameters)



Regenerates secret key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowAccessKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowAccessKeysApi apiInstance = new WorkflowAccessKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String accessKeyName = "accessKeyName_example"; // String | The workflow access key name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    RegenerateSecretKeyParameters parameters = new RegenerateSecretKeyParameters(); // RegenerateSecretKeyParameters | The parameters.
    try {
      WorkflowSecretKeys result = apiInstance.workflowAccessKeysRegenerateSecretKey(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowAccessKeysApi#workflowAccessKeysRegenerateSecretKey");
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
| **workflowName** | **String**| The workflow name. | |
| **accessKeyName** | **String**| The workflow access key name. | |
| **apiVersion** | **String**| The API version. | |
| **parameters** | [**RegenerateSecretKeyParameters**](RegenerateSecretKeyParameters.md)| The parameters. | |

### Return type

[**WorkflowSecretKeys**](WorkflowSecretKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


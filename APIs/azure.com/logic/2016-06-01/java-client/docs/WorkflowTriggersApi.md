# WorkflowTriggersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workflowTriggersGet**](WorkflowTriggersApi.md#workflowTriggersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName} |  |
| [**workflowTriggersGetSchemaJson**](WorkflowTriggersApi.md#workflowTriggersGetSchemaJson) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/schemas/json |  |
| [**workflowTriggersList**](WorkflowTriggersApi.md#workflowTriggersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers |  |
| [**workflowTriggersListCallbackUrl**](WorkflowTriggersApi.md#workflowTriggersListCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/listCallbackUrl |  |
| [**workflowTriggersReset**](WorkflowTriggersApi.md#workflowTriggersReset) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/reset |  |
| [**workflowTriggersRun**](WorkflowTriggersApi.md#workflowTriggersRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/run |  |
| [**workflowTriggersSetState**](WorkflowTriggersApi.md#workflowTriggersSetState) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/setState |  |
| [**workflowVersionsListCallbackUrl**](WorkflowTriggersApi.md#workflowVersionsListCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/versions/{versionId}/triggers/{triggerName}/listCallbackUrl |  |


<a id="workflowTriggersGet"></a>
# **workflowTriggersGet**
> WorkflowTrigger workflowTriggersGet(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion)



Gets a workflow trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowTriggersApi apiInstance = new WorkflowTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String triggerName = "triggerName_example"; // String | The workflow trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowTrigger result = apiInstance.workflowTriggersGet(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTriggersApi#workflowTriggersGet");
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
| **triggerName** | **String**| The workflow trigger name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowTrigger**](WorkflowTrigger.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowTriggersGetSchemaJson"></a>
# **workflowTriggersGetSchemaJson**
> JsonSchema workflowTriggersGetSchemaJson(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion)



Get the trigger schema as JSON.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowTriggersApi apiInstance = new WorkflowTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String triggerName = "triggerName_example"; // String | The workflow trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      JsonSchema result = apiInstance.workflowTriggersGetSchemaJson(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTriggersApi#workflowTriggersGetSchemaJson");
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
| **triggerName** | **String**| The workflow trigger name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**JsonSchema**](JsonSchema.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowTriggersList"></a>
# **workflowTriggersList**
> WorkflowTriggerListResult workflowTriggersList(subscriptionId, resourceGroupName, workflowName, apiVersion, $top, $filter)



Gets a list of workflow triggers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowTriggersApi apiInstance = new WorkflowTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      WorkflowTriggerListResult result = apiInstance.workflowTriggersList(subscriptionId, resourceGroupName, workflowName, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTriggersApi#workflowTriggersList");
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
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**WorkflowTriggerListResult**](WorkflowTriggerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowTriggersListCallbackUrl"></a>
# **workflowTriggersListCallbackUrl**
> WorkflowTriggerCallbackUrl workflowTriggersListCallbackUrl(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion)



Get the callback URL for a workflow trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowTriggersApi apiInstance = new WorkflowTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String triggerName = "triggerName_example"; // String | The workflow trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowTriggerCallbackUrl result = apiInstance.workflowTriggersListCallbackUrl(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTriggersApi#workflowTriggersListCallbackUrl");
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
| **triggerName** | **String**| The workflow trigger name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowTriggersReset"></a>
# **workflowTriggersReset**
> workflowTriggersReset(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion)



Resets a workflow trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowTriggersApi apiInstance = new WorkflowTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String triggerName = "triggerName_example"; // String | The workflow trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.workflowTriggersReset(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTriggersApi#workflowTriggersReset");
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
| **triggerName** | **String**| The workflow trigger name. | |
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

<a id="workflowTriggersRun"></a>
# **workflowTriggersRun**
> Object workflowTriggersRun(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion)



Runs a workflow trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowTriggersApi apiInstance = new WorkflowTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String triggerName = "triggerName_example"; // String | The workflow trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      Object result = apiInstance.workflowTriggersRun(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTriggersApi#workflowTriggersRun");
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
| **triggerName** | **String**| The workflow trigger name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | All status codes are acceptable. |  -  |

<a id="workflowTriggersSetState"></a>
# **workflowTriggersSetState**
> workflowTriggersSetState(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, setState)



Sets the state of a workflow trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowTriggersApi apiInstance = new WorkflowTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String triggerName = "triggerName_example"; // String | The workflow trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    SetTriggerStateActionDefinition setState = new SetTriggerStateActionDefinition(); // SetTriggerStateActionDefinition | The workflow trigger state.
    try {
      apiInstance.workflowTriggersSetState(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, setState);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTriggersApi#workflowTriggersSetState");
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
| **triggerName** | **String**| The workflow trigger name. | |
| **apiVersion** | **String**| The API version. | |
| **setState** | [**SetTriggerStateActionDefinition**](SetTriggerStateActionDefinition.md)| The workflow trigger state. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowVersionsListCallbackUrl"></a>
# **workflowVersionsListCallbackUrl**
> WorkflowTriggerCallbackUrl workflowVersionsListCallbackUrl(subscriptionId, resourceGroupName, workflowName, versionId, triggerName, apiVersion, parameters)



Get the callback url for a trigger of a workflow version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowTriggersApi apiInstance = new WorkflowTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String versionId = "versionId_example"; // String | The workflow versionId.
    String triggerName = "triggerName_example"; // String | The workflow trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    GetCallbackUrlParameters parameters = new GetCallbackUrlParameters(); // GetCallbackUrlParameters | The callback URL parameters.
    try {
      WorkflowTriggerCallbackUrl result = apiInstance.workflowVersionsListCallbackUrl(subscriptionId, resourceGroupName, workflowName, versionId, triggerName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTriggersApi#workflowVersionsListCallbackUrl");
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
| **versionId** | **String**| The workflow versionId. | |
| **triggerName** | **String**| The workflow trigger name. | |
| **apiVersion** | **String**| The API version. | |
| **parameters** | [**GetCallbackUrlParameters**](GetCallbackUrlParameters.md)| The callback URL parameters. | [optional] |

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


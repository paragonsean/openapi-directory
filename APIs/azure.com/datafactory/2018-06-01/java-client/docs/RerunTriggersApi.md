# RerunTriggersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rerunTriggersCancel**](RerunTriggersApi.md#rerunTriggersCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/rerunTriggers/{rerunTriggerName}/cancel |  |
| [**rerunTriggersCreate**](RerunTriggersApi.md#rerunTriggersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/rerunTriggers/{rerunTriggerName} |  |
| [**rerunTriggersListByTrigger**](RerunTriggersApi.md#rerunTriggersListByTrigger) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/rerunTriggers |  |
| [**rerunTriggersStart**](RerunTriggersApi.md#rerunTriggersStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/rerunTriggers/{rerunTriggerName}/start |  |
| [**rerunTriggersStop**](RerunTriggersApi.md#rerunTriggersStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/rerunTriggers/{rerunTriggerName}/stop |  |


<a id="rerunTriggersCancel"></a>
# **rerunTriggersCancel**
> rerunTriggersCancel(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion)



Cancels a trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RerunTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RerunTriggersApi apiInstance = new RerunTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String rerunTriggerName = "rerunTriggerName_example"; // String | The rerun trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.rerunTriggersCancel(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RerunTriggersApi#rerunTriggersCancel");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **triggerName** | **String**| The trigger name. | |
| **rerunTriggerName** | **String**| The rerun trigger name. | |
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
| **200** | Trigger has been canceled successfully. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="rerunTriggersCreate"></a>
# **rerunTriggersCreate**
> TriggerResource rerunTriggersCreate(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion, rerunTumblingWindowTriggerActionParameters)



Creates a rerun trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RerunTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RerunTriggersApi apiInstance = new RerunTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String rerunTriggerName = "rerunTriggerName_example"; // String | The rerun trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    RerunTumblingWindowTriggerActionParameters rerunTumblingWindowTriggerActionParameters = new RerunTumblingWindowTriggerActionParameters(); // RerunTumblingWindowTriggerActionParameters | Rerun tumbling window trigger action parameters.
    try {
      TriggerResource result = apiInstance.rerunTriggersCreate(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion, rerunTumblingWindowTriggerActionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RerunTriggersApi#rerunTriggersCreate");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **triggerName** | **String**| The trigger name. | |
| **rerunTriggerName** | **String**| The rerun trigger name. | |
| **apiVersion** | **String**| The API version. | |
| **rerunTumblingWindowTriggerActionParameters** | [**RerunTumblingWindowTriggerActionParameters**](RerunTumblingWindowTriggerActionParameters.md)| Rerun tumbling window trigger action parameters. | |

### Return type

[**TriggerResource**](TriggerResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="rerunTriggersListByTrigger"></a>
# **rerunTriggersListByTrigger**
> RerunTriggerListResponse rerunTriggersListByTrigger(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion)



Lists rerun triggers by an original trigger name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RerunTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RerunTriggersApi apiInstance = new RerunTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      RerunTriggerListResponse result = apiInstance.rerunTriggersListByTrigger(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RerunTriggersApi#rerunTriggersListByTrigger");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **triggerName** | **String**| The trigger name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**RerunTriggerListResponse**](RerunTriggerListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="rerunTriggersStart"></a>
# **rerunTriggersStart**
> rerunTriggersStart(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion)



Starts a trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RerunTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RerunTriggersApi apiInstance = new RerunTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String rerunTriggerName = "rerunTriggerName_example"; // String | The rerun trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.rerunTriggersStart(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RerunTriggersApi#rerunTriggersStart");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **triggerName** | **String**| The trigger name. | |
| **rerunTriggerName** | **String**| The rerun trigger name. | |
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
| **200** | Trigger has been started successfully. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="rerunTriggersStop"></a>
# **rerunTriggersStop**
> rerunTriggersStop(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion)



Stops a trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RerunTriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RerunTriggersApi apiInstance = new RerunTriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String rerunTriggerName = "rerunTriggerName_example"; // String | The rerun trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.rerunTriggersStop(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RerunTriggersApi#rerunTriggersStop");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **triggerName** | **String**| The trigger name. | |
| **rerunTriggerName** | **String**| The rerun trigger name. | |
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
| **200** | Trigger has been stopped successfully. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |


# TriggersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**triggersCreateOrUpdate**](TriggersApi.md#triggersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName} |  |
| [**triggersDelete**](TriggersApi.md#triggersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName} |  |
| [**triggersGetEventSubscriptionStatus**](TriggersApi.md#triggersGetEventSubscriptionStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/getEventSubscriptionStatus |  |
| [**triggersListByFactory**](TriggersApi.md#triggersListByFactory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers |  |
| [**triggersStart**](TriggersApi.md#triggersStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/start |  |
| [**triggersStop**](TriggersApi.md#triggersStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/stop |  |
| [**triggersSubscribeToEvents**](TriggersApi.md#triggersSubscribeToEvents) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/subscribeToEvents |  |
| [**triggersUnsubscribeFromEvents**](TriggersApi.md#triggersUnsubscribeFromEvents) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/unsubscribeFromEvents |  |


<a id="triggersCreateOrUpdate"></a>
# **triggersCreateOrUpdate**
> TriggerResource triggersCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion, trigger, ifMatch)



Creates or updates a trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    TriggerResource trigger = new TriggerResource(); // TriggerResource | Trigger resource definition.
    String ifMatch = "ifMatch_example"; // String | ETag of the trigger entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    try {
      TriggerResource result = apiInstance.triggersCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion, trigger, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersCreateOrUpdate");
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
| **trigger** | [**TriggerResource**](TriggerResource.md)| Trigger resource definition. | |
| **ifMatch** | **String**| ETag of the trigger entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] |

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

<a id="triggersDelete"></a>
# **triggersDelete**
> triggersDelete(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion)



Deletes a trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.triggersDelete(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersDelete");
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

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **204** | No Content. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="triggersGetEventSubscriptionStatus"></a>
# **triggersGetEventSubscriptionStatus**
> TriggerSubscriptionOperationStatus triggersGetEventSubscriptionStatus(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion)



Get a trigger&#39;s event subscription status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      TriggerSubscriptionOperationStatus result = apiInstance.triggersGetEventSubscriptionStatus(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersGetEventSubscriptionStatus");
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

[**TriggerSubscriptionOperationStatus**](TriggerSubscriptionOperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trigger event subscription state. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="triggersListByFactory"></a>
# **triggersListByFactory**
> TriggerListResponse triggersListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Lists triggers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      TriggerListResponse result = apiInstance.triggersListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersListByFactory");
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
| **apiVersion** | **String**| The API version. | |

### Return type

[**TriggerListResponse**](TriggerListResponse.md)

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

<a id="triggersStart"></a>
# **triggersStart**
> triggersStart(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion)



Starts a trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.triggersStart(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersStart");
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

<a id="triggersStop"></a>
# **triggersStop**
> triggersStop(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion)



Stops a trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.triggersStop(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersStop");
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

<a id="triggersSubscribeToEvents"></a>
# **triggersSubscribeToEvents**
> TriggerSubscriptionOperationStatus triggersSubscribeToEvents(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion)



Subscribe event trigger to events.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      TriggerSubscriptionOperationStatus result = apiInstance.triggersSubscribeToEvents(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersSubscribeToEvents");
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

[**TriggerSubscriptionOperationStatus**](TriggerSubscriptionOperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trigger is subscribed to events. |  -  |
| **202** | Accepted. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="triggersUnsubscribeFromEvents"></a>
# **triggersUnsubscribeFromEvents**
> TriggerSubscriptionOperationStatus triggersUnsubscribeFromEvents(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion)



Unsubscribe event trigger from events.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggersApi apiInstance = new TriggersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      TriggerSubscriptionOperationStatus result = apiInstance.triggersUnsubscribeFromEvents(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggersApi#triggersUnsubscribeFromEvents");
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

[**TriggerSubscriptionOperationStatus**](TriggerSubscriptionOperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trigger is unsubscribed from events. |  -  |
| **202** | Accepted. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |


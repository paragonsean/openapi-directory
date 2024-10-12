# QueuesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queuesCreateOrUpdate**](QueuesApi.md#queuesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName} |  |
| [**queuesCreateOrUpdateAuthorizationRule**](QueuesApi.md#queuesCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName} |  |
| [**queuesDelete**](QueuesApi.md#queuesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName} |  |
| [**queuesDeleteAuthorizationRule**](QueuesApi.md#queuesDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName} |  |
| [**queuesGet**](QueuesApi.md#queuesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName} |  |
| [**queuesGetAuthorizationRule**](QueuesApi.md#queuesGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName} |  |
| [**queuesListAuthorizationRules**](QueuesApi.md#queuesListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules |  |
| [**queuesListByNamespace**](QueuesApi.md#queuesListByNamespace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues |  |
| [**queuesListKeys**](QueuesApi.md#queuesListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName}/ListKeys |  |
| [**queuesRegenerateKeys**](QueuesApi.md#queuesRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/queues/{queueName}/authorizationRules/{authorizationRuleName}/regenerateKeys |  |


<a id="queuesCreateOrUpdate"></a>
# **queuesCreateOrUpdate**
> SBQueue queuesCreateOrUpdate(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId, parameters)



Creates or updates a Service Bus queue. This operation is idempotent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String queueName = "queueName_example"; // String | The queue name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SBQueue parameters = new SBQueue(); // SBQueue | Parameters supplied to create or update a queue resource.
    try {
      SBQueue result = apiInstance.queuesCreateOrUpdate(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#queuesCreateOrUpdate");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **queueName** | **String**| The queue name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**SBQueue**](SBQueue.md)| Parameters supplied to create or update a queue resource. | |

### Return type

[**SBQueue**](SBQueue.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Queue successfully created. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="queuesCreateOrUpdateAuthorizationRule"></a>
# **queuesCreateOrUpdateAuthorizationRule**
> SBAuthorizationRule queuesCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates an authorization rule for a queue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String queueName = "queueName_example"; // String | The queue name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SBAuthorizationRule parameters = new SBAuthorizationRule(); // SBAuthorizationRule | The shared access authorization rule.
    try {
      SBAuthorizationRule result = apiInstance.queuesCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#queuesCreateOrUpdateAuthorizationRule");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **queueName** | **String**| The queue name. | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**SBAuthorizationRule**](SBAuthorizationRule.md)| The shared access authorization rule. | |

### Return type

[**SBAuthorizationRule**](SBAuthorizationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorization rule successfully created. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="queuesDelete"></a>
# **queuesDelete**
> queuesDelete(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId)



Deletes a queue from the specified namespace in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String queueName = "queueName_example"; // String | The queue name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.queuesDelete(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#queuesDelete");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **queueName** | **String**| The queue name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Queue successfully deleted. |  -  |
| **204** | No content. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="queuesDeleteAuthorizationRule"></a>
# **queuesDeleteAuthorizationRule**
> queuesDeleteAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId)



Deletes a queue authorization rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String queueName = "queueName_example"; // String | The queue name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.queuesDeleteAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#queuesDeleteAuthorizationRule");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **queueName** | **String**| The queue name. | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Authorization rule successfully deleted. |  -  |
| **204** | No content. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="queuesGet"></a>
# **queuesGet**
> SBQueue queuesGet(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId)



Returns a description for the specified queue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String queueName = "queueName_example"; // String | The queue name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SBQueue result = apiInstance.queuesGet(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#queuesGet");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **queueName** | **String**| The queue name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SBQueue**](SBQueue.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Queue description successfully returned. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="queuesGetAuthorizationRule"></a>
# **queuesGetAuthorizationRule**
> SBAuthorizationRule queuesGetAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId)



Gets an authorization rule for a queue by rule name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String queueName = "queueName_example"; // String | The queue name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SBAuthorizationRule result = apiInstance.queuesGetAuthorizationRule(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#queuesGetAuthorizationRule");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **queueName** | **String**| The queue name. | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SBAuthorizationRule**](SBAuthorizationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorization rule successfully returned. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="queuesListAuthorizationRules"></a>
# **queuesListAuthorizationRules**
> SBAuthorizationRuleListResult queuesListAuthorizationRules(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId)



Gets all authorization rules for a queue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String queueName = "queueName_example"; // String | The queue name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SBAuthorizationRuleListResult result = apiInstance.queuesListAuthorizationRules(resourceGroupName, namespaceName, queueName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#queuesListAuthorizationRules");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **queueName** | **String**| The queue name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SBAuthorizationRuleListResult**](SBAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorization rules successfully returned. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="queuesListByNamespace"></a>
# **queuesListByNamespace**
> SBQueueListResult queuesListByNamespace(resourceGroupName, namespaceName, apiVersion, subscriptionId, $skip, $top)



Gets the queues within a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $skip = 56; // Integer | Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N usageDetails.
    try {
      SBQueueListResult result = apiInstance.queuesListByNamespace(resourceGroupName, namespaceName, apiVersion, subscriptionId, $skip, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#queuesListByNamespace");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$skip** | **Integer**| Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls. | [optional] |
| **$top** | **Integer**| May be used to limit the number of results to the most recent N usageDetails. | [optional] |

### Return type

[**SBQueueListResult**](SBQueueListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Queues successfully returned. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="queuesListKeys"></a>
# **queuesListKeys**
> AccessKeys queuesListKeys(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId)



Primary and secondary connection strings to the queue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String queueName = "queueName_example"; // String | The queue name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AccessKeys result = apiInstance.queuesListKeys(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#queuesListKeys");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **queueName** | **String**| The queue name. | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AccessKeys**](AccessKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connection strings successfully returned. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="queuesRegenerateKeys"></a>
# **queuesRegenerateKeys**
> AccessKeys queuesRegenerateKeys(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Regenerates the primary or secondary connection strings to the queue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String queueName = "queueName_example"; // String | The queue name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    RegenerateAccessKeyParameters parameters = new RegenerateAccessKeyParameters(); // RegenerateAccessKeyParameters | Parameters supplied to regenerate the authorization rule.
    try {
      AccessKeys result = apiInstance.queuesRegenerateKeys(resourceGroupName, namespaceName, queueName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#queuesRegenerateKeys");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **queueName** | **String**| The queue name. | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**RegenerateAccessKeyParameters**](RegenerateAccessKeyParameters.md)| Parameters supplied to regenerate the authorization rule. | |

### Return type

[**AccessKeys**](AccessKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connection strings successfully regenerated. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |


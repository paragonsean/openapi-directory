# TopicsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**topicsCreateOrUpdate**](TopicsApi.md#topicsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName} |  |
| [**topicsCreateOrUpdateAuthorizationRule**](TopicsApi.md#topicsCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName} |  |
| [**topicsDelete**](TopicsApi.md#topicsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName} |  |
| [**topicsDeleteAuthorizationRule**](TopicsApi.md#topicsDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName} |  |
| [**topicsGet**](TopicsApi.md#topicsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName} |  |
| [**topicsGetAuthorizationRule**](TopicsApi.md#topicsGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName} |  |
| [**topicsListAuthorizationRules**](TopicsApi.md#topicsListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules |  |
| [**topicsListByNamespace**](TopicsApi.md#topicsListByNamespace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics |  |
| [**topicsListKeys**](TopicsApi.md#topicsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName}/ListKeys |  |
| [**topicsRegenerateKeys**](TopicsApi.md#topicsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName}/regenerateKeys |  |


<a id="topicsCreateOrUpdate"></a>
# **topicsCreateOrUpdate**
> SBTopic topicsCreateOrUpdate(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId, parameters)



Creates a topic in the specified namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SBTopic parameters = new SBTopic(); // SBTopic | Parameters supplied to create a topic resource.
    try {
      SBTopic result = apiInstance.topicsCreateOrUpdate(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsCreateOrUpdate");
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
| **topicName** | **String**| The topic name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**SBTopic**](SBTopic.md)| Parameters supplied to create a topic resource. | |

### Return type

[**SBTopic**](SBTopic.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Topic successfully created. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="topicsCreateOrUpdateAuthorizationRule"></a>
# **topicsCreateOrUpdateAuthorizationRule**
> SBAuthorizationRule topicsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates an authorization rule for the specified topic.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SBAuthorizationRule parameters = new SBAuthorizationRule(); // SBAuthorizationRule | The shared access authorization rule.
    try {
      SBAuthorizationRule result = apiInstance.topicsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsCreateOrUpdateAuthorizationRule");
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
| **topicName** | **String**| The topic name. | |
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
| **200** | Topic authorization rule successfully created. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="topicsDelete"></a>
# **topicsDelete**
> topicsDelete(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId)



Deletes a topic from the specified namespace and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.topicsDelete(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsDelete");
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
| **topicName** | **String**| The topic name. | |
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
| **200** | Topic successfully deleted. |  -  |
| **204** | No Content |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="topicsDeleteAuthorizationRule"></a>
# **topicsDeleteAuthorizationRule**
> topicsDeleteAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId)



Deletes a topic authorization rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.topicsDeleteAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsDeleteAuthorizationRule");
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
| **topicName** | **String**| The topic name. | |
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
| **200** | Topic authorization rule successfully deleted. |  -  |
| **204** | No content. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="topicsGet"></a>
# **topicsGet**
> SBTopic topicsGet(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId)



Returns a description for the specified topic.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SBTopic result = apiInstance.topicsGet(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsGet");
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
| **topicName** | **String**| The topic name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SBTopic**](SBTopic.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Topic description successfully retrieved. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="topicsGetAuthorizationRule"></a>
# **topicsGetAuthorizationRule**
> SBAuthorizationRule topicsGetAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId)



Returns the specified authorization rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SBAuthorizationRule result = apiInstance.topicsGetAuthorizationRule(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsGetAuthorizationRule");
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
| **topicName** | **String**| The topic name. | |
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
| **200** | Topic authorization rule returned successfully. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="topicsListAuthorizationRules"></a>
# **topicsListAuthorizationRules**
> SBAuthorizationRuleListResult topicsListAuthorizationRules(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId)



Gets authorization rules for a topic.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SBAuthorizationRuleListResult result = apiInstance.topicsListAuthorizationRules(resourceGroupName, namespaceName, topicName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsListAuthorizationRules");
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
| **topicName** | **String**| The topic name. | |
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

<a id="topicsListByNamespace"></a>
# **topicsListByNamespace**
> SBTopicListResult topicsListByNamespace(resourceGroupName, namespaceName, apiVersion, subscriptionId, $skip, $top)



Gets all the topics in a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $skip = 56; // Integer | Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
    Integer $top = 56; // Integer | May be used to limit the number of results to the most recent N usageDetails.
    try {
      SBTopicListResult result = apiInstance.topicsListByNamespace(resourceGroupName, namespaceName, apiVersion, subscriptionId, $skip, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsListByNamespace");
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

[**SBTopicListResult**](SBTopicListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved list of topics. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="topicsListKeys"></a>
# **topicsListKeys**
> AccessKeys topicsListKeys(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId)



Gets the primary and secondary connection strings for the topic.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AccessKeys result = apiInstance.topicsListKeys(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsListKeys");
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
| **topicName** | **String**| The topic name. | |
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
| **200** | Connection strings successfully retrieved. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="topicsRegenerateKeys"></a>
# **topicsRegenerateKeys**
> AccessKeys topicsRegenerateKeys(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Regenerates primary or secondary connection strings for the topic.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String topicName = "topicName_example"; // String | The topic name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    RegenerateAccessKeyParameters parameters = new RegenerateAccessKeyParameters(); // RegenerateAccessKeyParameters | Parameters supplied to regenerate the authorization rule.
    try {
      AccessKeys result = apiInstance.topicsRegenerateKeys(resourceGroupName, namespaceName, topicName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsRegenerateKeys");
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
| **topicName** | **String**| The topic name. | |
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


# TopicsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**topicsCreateOrUpdate**](TopicsApi.md#topicsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName} | Create a topic |
| [**topicsDelete**](TopicsApi.md#topicsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName} | Delete a topic |
| [**topicsGet**](TopicsApi.md#topicsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName} | Get a topic |
| [**topicsListByResourceGroup**](TopicsApi.md#topicsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics | List topics under a resource group |
| [**topicsListBySubscription**](TopicsApi.md#topicsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/topics | List topics under an Azure subscription |
| [**topicsListEventTypes**](TopicsApi.md#topicsListEventTypes) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{providerNamespace}/{resourceTypeName}/{resourceName}/providers/Microsoft.EventGrid/eventTypes | List topic event types |
| [**topicsListSharedAccessKeys**](TopicsApi.md#topicsListSharedAccessKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}/listKeys | List keys for a topic |
| [**topicsRegenerateKey**](TopicsApi.md#topicsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}/regenerateKey | Regenerate key for a topic |
| [**topicsUpdate**](TopicsApi.md#topicsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName} | Update a topic |


<a id="topicsCreateOrUpdate"></a>
# **topicsCreateOrUpdate**
> Topic topicsCreateOrUpdate(subscriptionId, resourceGroupName, topicName, apiVersion, topicInfo)

Create a topic

Asynchronously creates a new topic with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String topicName = "topicName_example"; // String | Name of the topic
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    Topic topicInfo = new Topic(); // Topic | Topic information
    try {
      Topic result = apiInstance.topicsCreateOrUpdate(subscriptionId, resourceGroupName, topicName, apiVersion, topicInfo);
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **topicName** | **String**| Name of the topic | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **topicInfo** | [**Topic**](Topic.md)| Topic information | |

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="topicsDelete"></a>
# **topicsDelete**
> topicsDelete(subscriptionId, resourceGroupName, topicName, apiVersion)

Delete a topic

Delete existing topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String topicName = "topicName_example"; // String | Name of the topic
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.topicsDelete(subscriptionId, resourceGroupName, topicName, apiVersion);
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **topicName** | **String**| Name of the topic | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 404 Not Found.   * 500 Internal Server Error. |  -  |

<a id="topicsGet"></a>
# **topicsGet**
> Topic topicsGet(subscriptionId, resourceGroupName, topicName, apiVersion)

Get a topic

Get properties of a topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String topicName = "topicName_example"; // String | Name of the topic
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      Topic result = apiInstance.topicsGet(subscriptionId, resourceGroupName, topicName, apiVersion);
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **topicName** | **String**| Name of the topic | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="topicsListByResourceGroup"></a>
# **topicsListByResourceGroup**
> TopicsListResult topicsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)

List topics under a resource group

List all the topics under a resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      TopicsListResult result = apiInstance.topicsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsListByResourceGroup");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**TopicsListResult**](TopicsListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="topicsListBySubscription"></a>
# **topicsListBySubscription**
> TopicsListResult topicsListBySubscription(subscriptionId, apiVersion)

List topics under an Azure subscription

List all the topics under an Azure subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      TopicsListResult result = apiInstance.topicsListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsListBySubscription");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**TopicsListResult**](TopicsListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="topicsListEventTypes"></a>
# **topicsListEventTypes**
> EventTypesListResult topicsListEventTypes(subscriptionId, resourceGroupName, providerNamespace, resourceTypeName, resourceName, apiVersion)

List topic event types

List event types for a topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String providerNamespace = "providerNamespace_example"; // String | Namespace of the provider of the topic
    String resourceTypeName = "resourceTypeName_example"; // String | Name of the topic type
    String resourceName = "resourceName_example"; // String | Name of the topic
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      EventTypesListResult result = apiInstance.topicsListEventTypes(subscriptionId, resourceGroupName, providerNamespace, resourceTypeName, resourceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsListEventTypes");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **providerNamespace** | **String**| Namespace of the provider of the topic | |
| **resourceTypeName** | **String**| Name of the topic type | |
| **resourceName** | **String**| Name of the topic | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**EventTypesListResult**](EventTypesListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="topicsListSharedAccessKeys"></a>
# **topicsListSharedAccessKeys**
> TopicSharedAccessKeys topicsListSharedAccessKeys(subscriptionId, resourceGroupName, topicName, apiVersion)

List keys for a topic

List the two keys used to publish to a topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String topicName = "topicName_example"; // String | Name of the topic
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      TopicSharedAccessKeys result = apiInstance.topicsListSharedAccessKeys(subscriptionId, resourceGroupName, topicName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsListSharedAccessKeys");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **topicName** | **String**| Name of the topic | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**TopicSharedAccessKeys**](TopicSharedAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="topicsRegenerateKey"></a>
# **topicsRegenerateKey**
> TopicSharedAccessKeys topicsRegenerateKey(subscriptionId, resourceGroupName, topicName, apiVersion, regenerateKeyRequest)

Regenerate key for a topic

Regenerate a shared access key for a topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String topicName = "topicName_example"; // String | Name of the topic
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    TopicRegenerateKeyRequest regenerateKeyRequest = new TopicRegenerateKeyRequest(); // TopicRegenerateKeyRequest | Request body to regenerate key
    try {
      TopicSharedAccessKeys result = apiInstance.topicsRegenerateKey(subscriptionId, resourceGroupName, topicName, apiVersion, regenerateKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsRegenerateKey");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **topicName** | **String**| Name of the topic | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **regenerateKeyRequest** | [**TopicRegenerateKeyRequest**](TopicRegenerateKeyRequest.md)| Request body to regenerate key | |

### Return type

[**TopicSharedAccessKeys**](TopicSharedAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="topicsUpdate"></a>
# **topicsUpdate**
> Topic topicsUpdate(subscriptionId, resourceGroupName, topicName, apiVersion, topicUpdateParameters)

Update a topic

Asynchronously updates a topic with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TopicsApi apiInstance = new TopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String topicName = "topicName_example"; // String | Name of the topic
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    TopicUpdateParameters topicUpdateParameters = new TopicUpdateParameters(); // TopicUpdateParameters | Topic update information
    try {
      Topic result = apiInstance.topicsUpdate(subscriptionId, resourceGroupName, topicName, apiVersion, topicUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopicsApi#topicsUpdate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **topicName** | **String**| Name of the topic | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **topicUpdateParameters** | [**TopicUpdateParameters**](TopicUpdateParameters.md)| Topic update information | |

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Topic update request accepted. |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |


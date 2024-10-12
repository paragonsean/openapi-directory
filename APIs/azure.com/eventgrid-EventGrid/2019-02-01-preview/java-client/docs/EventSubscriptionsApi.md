# EventSubscriptionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventSubscriptionsCreateOrUpdate**](EventSubscriptionsApi.md#eventSubscriptionsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName} | Create or update an event subscription |
| [**eventSubscriptionsDelete**](EventSubscriptionsApi.md#eventSubscriptionsDelete) | **DELETE** /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName} | Delete an event subscription |
| [**eventSubscriptionsGet**](EventSubscriptionsApi.md#eventSubscriptionsGet) | **GET** /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName} | Get an event subscription |
| [**eventSubscriptionsGetFullUrl**](EventSubscriptionsApi.md#eventSubscriptionsGetFullUrl) | **POST** /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName}/getFullUrl | Get full URL of an event subscription |
| [**eventSubscriptionsListByDomainTopic**](EventSubscriptionsApi.md#eventSubscriptionsListByDomainTopic) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{topicName}/providers/Microsoft.EventGrid/eventSubscriptions | List all event subscriptions for a specific domain topic |
| [**eventSubscriptionsListByResource**](EventSubscriptionsApi.md#eventSubscriptionsListByResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{providerNamespace}/{resourceTypeName}/{resourceName}/providers/Microsoft.EventGrid/eventSubscriptions | List all event subscriptions for a specific topic |
| [**eventSubscriptionsListGlobalByResourceGroup**](EventSubscriptionsApi.md#eventSubscriptionsListGlobalByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/eventSubscriptions | List all global event subscriptions under an Azure subscription and resource group |
| [**eventSubscriptionsListGlobalByResourceGroupForTopicType**](EventSubscriptionsApi.md#eventSubscriptionsListGlobalByResourceGroupForTopicType) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topicTypes/{topicTypeName}/eventSubscriptions | List all global event subscriptions under a resource group for a topic type |
| [**eventSubscriptionsListGlobalBySubscription**](EventSubscriptionsApi.md#eventSubscriptionsListGlobalBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/eventSubscriptions | Get an aggregated list of all global event subscriptions under an Azure subscription |
| [**eventSubscriptionsListGlobalBySubscriptionForTopicType**](EventSubscriptionsApi.md#eventSubscriptionsListGlobalBySubscriptionForTopicType) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/topicTypes/{topicTypeName}/eventSubscriptions | List all global event subscriptions for a topic type |
| [**eventSubscriptionsListRegionalByResourceGroup**](EventSubscriptionsApi.md#eventSubscriptionsListRegionalByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/locations/{location}/eventSubscriptions | List all regional event subscriptions under an Azure subscription and resource group |
| [**eventSubscriptionsListRegionalByResourceGroupForTopicType**](EventSubscriptionsApi.md#eventSubscriptionsListRegionalByResourceGroupForTopicType) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/locations/{location}/topicTypes/{topicTypeName}/eventSubscriptions | List all regional event subscriptions under an Azure subscription and resource group for a topic type |
| [**eventSubscriptionsListRegionalBySubscription**](EventSubscriptionsApi.md#eventSubscriptionsListRegionalBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/locations/{location}/eventSubscriptions | List all regional event subscriptions under an Azure subscription |
| [**eventSubscriptionsListRegionalBySubscriptionForTopicType**](EventSubscriptionsApi.md#eventSubscriptionsListRegionalBySubscriptionForTopicType) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/locations/{location}/topicTypes/{topicTypeName}/eventSubscriptions | List all regional event subscriptions under an Azure subscription for a topic type |
| [**eventSubscriptionsUpdate**](EventSubscriptionsApi.md#eventSubscriptionsUpdate) | **PATCH** /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{eventSubscriptionName} | Update an event subscription |


<a id="eventSubscriptionsCreateOrUpdate"></a>
# **eventSubscriptionsCreateOrUpdate**
> EventSubscription eventSubscriptionsCreateOrUpdate(scope, eventSubscriptionName, apiVersion, eventSubscriptionInfo)

Create or update an event subscription

Asynchronously creates a new event subscription or updates an existing event subscription based on the specified scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String scope = "scope_example"; // String | The identifier of the resource to which the event subscription needs to be created or updated. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for a resource, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}' for an EventGrid topic.
    String eventSubscriptionName = "eventSubscriptionName_example"; // String | Name of the event subscription. Event subscription names must be between 3 and 64 characters in length and should use alphanumeric letters only.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    EventSubscription eventSubscriptionInfo = new EventSubscription(); // EventSubscription | Event subscription properties containing the destination and filter information
    try {
      EventSubscription result = apiInstance.eventSubscriptionsCreateOrUpdate(scope, eventSubscriptionName, apiVersion, eventSubscriptionInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsCreateOrUpdate");
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
| **scope** | **String**| The identifier of the resource to which the event subscription needs to be created or updated. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic. | |
| **eventSubscriptionName** | **String**| Name of the event subscription. Event subscription names must be between 3 and 64 characters in length and should use alphanumeric letters only. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **eventSubscriptionInfo** | [**EventSubscription**](EventSubscription.md)| Event subscription properties containing the destination and filter information | |

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | EventSubscription CreateOrUpdate request accepted. |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="eventSubscriptionsDelete"></a>
# **eventSubscriptionsDelete**
> eventSubscriptionsDelete(scope, eventSubscriptionName, apiVersion)

Delete an event subscription

Delete an existing event subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for a resource, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}' for an EventGrid topic.
    String eventSubscriptionName = "eventSubscriptionName_example"; // String | Name of the event subscription
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.eventSubscriptionsDelete(scope, eventSubscriptionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsDelete");
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
| **scope** | **String**| The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic. | |
| **eventSubscriptionName** | **String**| Name of the event subscription | |
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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 404 Not Found.   * 500 Internal Server Error. |  -  |

<a id="eventSubscriptionsGet"></a>
# **eventSubscriptionsGet**
> EventSubscription eventSubscriptionsGet(scope, eventSubscriptionName, apiVersion)

Get an event subscription

Get properties of an event subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for a resource, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}' for an EventGrid topic.
    String eventSubscriptionName = "eventSubscriptionName_example"; // String | Name of the event subscription
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      EventSubscription result = apiInstance.eventSubscriptionsGet(scope, eventSubscriptionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsGet");
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
| **scope** | **String**| The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic. | |
| **eventSubscriptionName** | **String**| Name of the event subscription | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**EventSubscription**](EventSubscription.md)

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

<a id="eventSubscriptionsGetFullUrl"></a>
# **eventSubscriptionsGetFullUrl**
> EventSubscriptionFullUrl eventSubscriptionsGetFullUrl(scope, eventSubscriptionName, apiVersion)

Get full URL of an event subscription

Get the full endpoint URL for an event subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for a resource, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}' for an EventGrid topic.
    String eventSubscriptionName = "eventSubscriptionName_example"; // String | Name of the event subscription
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      EventSubscriptionFullUrl result = apiInstance.eventSubscriptionsGetFullUrl(scope, eventSubscriptionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsGetFullUrl");
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
| **scope** | **String**| The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic. | |
| **eventSubscriptionName** | **String**| Name of the event subscription | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**EventSubscriptionFullUrl**](EventSubscriptionFullUrl.md)

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

<a id="eventSubscriptionsListByDomainTopic"></a>
# **eventSubscriptionsListByDomainTopic**
> EventSubscriptionsListResult eventSubscriptionsListByDomainTopic(subscriptionId, resourceGroupName, domainName, topicName, apiVersion, $filter, $top, label)

List all event subscriptions for a specific domain topic

List all event subscriptions that have been created for a specific domain topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Name of the top level domain
    String topicName = "topicName_example"; // String | Name of the domain topic
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    String label = "label_example"; // String | The label used to filter the results for event subscriptions list.
    try {
      EventSubscriptionsListResult result = apiInstance.eventSubscriptionsListByDomainTopic(subscriptionId, resourceGroupName, domainName, topicName, apiVersion, $filter, $top, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsListByDomainTopic");
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
| **domainName** | **String**| Name of the top level domain | |
| **topicName** | **String**| Name of the domain topic | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |
| **label** | **String**| The label used to filter the results for event subscriptions list. | [optional] |

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

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

<a id="eventSubscriptionsListByResource"></a>
# **eventSubscriptionsListByResource**
> EventSubscriptionsListResult eventSubscriptionsListByResource(subscriptionId, resourceGroupName, providerNamespace, resourceTypeName, resourceName, apiVersion, $filter, $top, label)

List all event subscriptions for a specific topic

List all event subscriptions that have been created for a specific topic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String providerNamespace = "providerNamespace_example"; // String | Namespace of the provider of the topic
    String resourceTypeName = "resourceTypeName_example"; // String | Name of the resource type
    String resourceName = "resourceName_example"; // String | Name of the resource
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    String label = "label_example"; // String | The label used to filter the results for event subscriptions list.
    try {
      EventSubscriptionsListResult result = apiInstance.eventSubscriptionsListByResource(subscriptionId, resourceGroupName, providerNamespace, resourceTypeName, resourceName, apiVersion, $filter, $top, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsListByResource");
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
| **resourceTypeName** | **String**| Name of the resource type | |
| **resourceName** | **String**| Name of the resource | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |
| **label** | **String**| The label used to filter the results for event subscriptions list. | [optional] |

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

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

<a id="eventSubscriptionsListGlobalByResourceGroup"></a>
# **eventSubscriptionsListGlobalByResourceGroup**
> EventSubscriptionsListResult eventSubscriptionsListGlobalByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top, label)

List all global event subscriptions under an Azure subscription and resource group

List all global event subscriptions under a specific Azure subscription and resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    String label = "label_example"; // String | The label used to filter the results for event subscriptions list.
    try {
      EventSubscriptionsListResult result = apiInstance.eventSubscriptionsListGlobalByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsListGlobalByResourceGroup");
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
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |
| **label** | **String**| The label used to filter the results for event subscriptions list. | [optional] |

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

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

<a id="eventSubscriptionsListGlobalByResourceGroupForTopicType"></a>
# **eventSubscriptionsListGlobalByResourceGroupForTopicType**
> EventSubscriptionsListResult eventSubscriptionsListGlobalByResourceGroupForTopicType(subscriptionId, resourceGroupName, topicTypeName, apiVersion, $filter, $top, label)

List all global event subscriptions under a resource group for a topic type

List all global event subscriptions under a resource group for a specific topic type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String topicTypeName = "topicTypeName_example"; // String | Name of the topic type
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    String label = "label_example"; // String | The label used to filter the results for event subscriptions list.
    try {
      EventSubscriptionsListResult result = apiInstance.eventSubscriptionsListGlobalByResourceGroupForTopicType(subscriptionId, resourceGroupName, topicTypeName, apiVersion, $filter, $top, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsListGlobalByResourceGroupForTopicType");
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
| **topicTypeName** | **String**| Name of the topic type | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |
| **label** | **String**| The label used to filter the results for event subscriptions list. | [optional] |

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

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

<a id="eventSubscriptionsListGlobalBySubscription"></a>
# **eventSubscriptionsListGlobalBySubscription**
> EventSubscriptionsListResult eventSubscriptionsListGlobalBySubscription(subscriptionId, apiVersion, $filter, $top, label)

Get an aggregated list of all global event subscriptions under an Azure subscription

List all aggregated global event subscriptions under a specific Azure subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    String label = "label_example"; // String | The label used to filter the results for event subscriptions list.
    try {
      EventSubscriptionsListResult result = apiInstance.eventSubscriptionsListGlobalBySubscription(subscriptionId, apiVersion, $filter, $top, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsListGlobalBySubscription");
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
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |
| **label** | **String**| The label used to filter the results for event subscriptions list. | [optional] |

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

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

<a id="eventSubscriptionsListGlobalBySubscriptionForTopicType"></a>
# **eventSubscriptionsListGlobalBySubscriptionForTopicType**
> EventSubscriptionsListResult eventSubscriptionsListGlobalBySubscriptionForTopicType(subscriptionId, topicTypeName, apiVersion, $filter, $top, label)

List all global event subscriptions for a topic type

List all global event subscriptions under an Azure subscription for a topic type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String topicTypeName = "topicTypeName_example"; // String | Name of the topic type
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    String label = "label_example"; // String | The label used to filter the results for event subscriptions list.
    try {
      EventSubscriptionsListResult result = apiInstance.eventSubscriptionsListGlobalBySubscriptionForTopicType(subscriptionId, topicTypeName, apiVersion, $filter, $top, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsListGlobalBySubscriptionForTopicType");
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
| **topicTypeName** | **String**| Name of the topic type | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |
| **label** | **String**| The label used to filter the results for event subscriptions list. | [optional] |

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

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

<a id="eventSubscriptionsListRegionalByResourceGroup"></a>
# **eventSubscriptionsListRegionalByResourceGroup**
> EventSubscriptionsListResult eventSubscriptionsListRegionalByResourceGroup(subscriptionId, resourceGroupName, location, apiVersion, $filter, $top, label)

List all regional event subscriptions under an Azure subscription and resource group

List all event subscriptions from the given location under a specific Azure subscription and resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String location = "location_example"; // String | Name of the location
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    String label = "label_example"; // String | The label used to filter the results for event subscriptions list.
    try {
      EventSubscriptionsListResult result = apiInstance.eventSubscriptionsListRegionalByResourceGroup(subscriptionId, resourceGroupName, location, apiVersion, $filter, $top, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsListRegionalByResourceGroup");
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
| **location** | **String**| Name of the location | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |
| **label** | **String**| The label used to filter the results for event subscriptions list. | [optional] |

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

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

<a id="eventSubscriptionsListRegionalByResourceGroupForTopicType"></a>
# **eventSubscriptionsListRegionalByResourceGroupForTopicType**
> EventSubscriptionsListResult eventSubscriptionsListRegionalByResourceGroupForTopicType(subscriptionId, resourceGroupName, location, topicTypeName, apiVersion, $filter, $top, label)

List all regional event subscriptions under an Azure subscription and resource group for a topic type

List all event subscriptions from the given location under a specific Azure subscription and resource group and topic type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String location = "location_example"; // String | Name of the location
    String topicTypeName = "topicTypeName_example"; // String | Name of the topic type
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    String label = "label_example"; // String | The label used to filter the results for event subscriptions list.
    try {
      EventSubscriptionsListResult result = apiInstance.eventSubscriptionsListRegionalByResourceGroupForTopicType(subscriptionId, resourceGroupName, location, topicTypeName, apiVersion, $filter, $top, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsListRegionalByResourceGroupForTopicType");
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
| **location** | **String**| Name of the location | |
| **topicTypeName** | **String**| Name of the topic type | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |
| **label** | **String**| The label used to filter the results for event subscriptions list. | [optional] |

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

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

<a id="eventSubscriptionsListRegionalBySubscription"></a>
# **eventSubscriptionsListRegionalBySubscription**
> EventSubscriptionsListResult eventSubscriptionsListRegionalBySubscription(subscriptionId, location, apiVersion, $filter, $top, label)

List all regional event subscriptions under an Azure subscription

List all event subscriptions from the given location under a specific Azure subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Name of the location
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    String label = "label_example"; // String | The label used to filter the results for event subscriptions list.
    try {
      EventSubscriptionsListResult result = apiInstance.eventSubscriptionsListRegionalBySubscription(subscriptionId, location, apiVersion, $filter, $top, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsListRegionalBySubscription");
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
| **location** | **String**| Name of the location | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |
| **label** | **String**| The label used to filter the results for event subscriptions list. | [optional] |

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

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

<a id="eventSubscriptionsListRegionalBySubscriptionForTopicType"></a>
# **eventSubscriptionsListRegionalBySubscriptionForTopicType**
> EventSubscriptionsListResult eventSubscriptionsListRegionalBySubscriptionForTopicType(subscriptionId, location, topicTypeName, apiVersion, $filter, $top, label)

List all regional event subscriptions under an Azure subscription for a topic type

List all event subscriptions from the given location under a specific Azure subscription and topic type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Name of the location
    String topicTypeName = "topicTypeName_example"; // String | Name of the topic type
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    String label = "label_example"; // String | The label used to filter the results for event subscriptions list.
    try {
      EventSubscriptionsListResult result = apiInstance.eventSubscriptionsListRegionalBySubscriptionForTopicType(subscriptionId, location, topicTypeName, apiVersion, $filter, $top, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsListRegionalBySubscriptionForTopicType");
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
| **location** | **String**| Name of the location | |
| **topicTypeName** | **String**| Name of the topic type | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |
| **label** | **String**| The label used to filter the results for event subscriptions list. | [optional] |

### Return type

[**EventSubscriptionsListResult**](EventSubscriptionsListResult.md)

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

<a id="eventSubscriptionsUpdate"></a>
# **eventSubscriptionsUpdate**
> EventSubscription eventSubscriptionsUpdate(scope, eventSubscriptionName, apiVersion, eventSubscriptionUpdateParameters)

Update an event subscription

Asynchronously updates an existing event subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventSubscriptionsApi apiInstance = new EventSubscriptionsApi(defaultClient);
    String scope = "scope_example"; // String | The scope of existing event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use '/subscriptions/{subscriptionId}/' for a subscription, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for a resource group, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}' for a resource, and '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}' for an EventGrid topic.
    String eventSubscriptionName = "eventSubscriptionName_example"; // String | Name of the event subscription to be updated
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    EventSubscriptionUpdateParameters eventSubscriptionUpdateParameters = new EventSubscriptionUpdateParameters(); // EventSubscriptionUpdateParameters | Updated event subscription information
    try {
      EventSubscription result = apiInstance.eventSubscriptionsUpdate(scope, eventSubscriptionName, apiVersion, eventSubscriptionUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSubscriptionsApi#eventSubscriptionsUpdate");
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
| **scope** | **String**| The scope of existing event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic. | |
| **eventSubscriptionName** | **String**| Name of the event subscription to be updated | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **eventSubscriptionUpdateParameters** | [**EventSubscriptionUpdateParameters**](EventSubscriptionUpdateParameters.md)| Updated event subscription information | |

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | EventSubscription update request accepted. |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |


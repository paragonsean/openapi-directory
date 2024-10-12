# ConsumerGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerGroupsCreateOrUpdate**](ConsumerGroupsApi.md#consumerGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName} |  |
| [**consumerGroupsDelete**](ConsumerGroupsApi.md#consumerGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName} |  |
| [**consumerGroupsGet**](ConsumerGroupsApi.md#consumerGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups/{consumerGroupName} |  |
| [**consumerGroupsListAll**](ConsumerGroupsApi.md#consumerGroupsListAll) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/consumergroups |  |


<a id="consumerGroupsCreateOrUpdate"></a>
# **consumerGroupsCreateOrUpdate**
> ConsumerGroupResource consumerGroupsCreateOrUpdate(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId, parameters)



Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsumerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConsumerGroupsApi apiInstance = new ConsumerGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String consumerGroupName = "consumerGroupName_example"; // String | The consumer group name
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ConsumerGroupCreateOrUpdateParameters parameters = new ConsumerGroupCreateOrUpdateParameters(); // ConsumerGroupCreateOrUpdateParameters | Parameters supplied to create or update a consumer group resource.
    try {
      ConsumerGroupResource result = apiInstance.consumerGroupsCreateOrUpdate(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsumerGroupsApi#consumerGroupsCreateOrUpdate");
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
| **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | |
| **namespaceName** | **String**| The Namespace name | |
| **eventHubName** | **String**| The Event Hub name | |
| **consumerGroupName** | **String**| The consumer group name | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ConsumerGroupCreateOrUpdateParameters**](ConsumerGroupCreateOrUpdateParameters.md)| Parameters supplied to create or update a consumer group resource. | |

### Return type

[**ConsumerGroupResource**](ConsumerGroupResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Consumer group successfully created. |  -  |

<a id="consumerGroupsDelete"></a>
# **consumerGroupsDelete**
> consumerGroupsDelete(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId)



Deletes a consumer group from the specified Event Hub and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsumerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConsumerGroupsApi apiInstance = new ConsumerGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String consumerGroupName = "consumerGroupName_example"; // String | The consumer group name
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.consumerGroupsDelete(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsumerGroupsApi#consumerGroupsDelete");
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
| **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | |
| **namespaceName** | **String**| The Namespace name | |
| **eventHubName** | **String**| The Event Hub name | |
| **consumerGroupName** | **String**| The consumer group name | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Consumer group deleted. |  -  |
| **204** | No content. |  -  |

<a id="consumerGroupsGet"></a>
# **consumerGroupsGet**
> ConsumerGroupResource consumerGroupsGet(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId)



Gets a description for the specified consumer group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsumerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConsumerGroupsApi apiInstance = new ConsumerGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String consumerGroupName = "consumerGroupName_example"; // String | The consumer group name
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ConsumerGroupResource result = apiInstance.consumerGroupsGet(resourceGroupName, namespaceName, eventHubName, consumerGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsumerGroupsApi#consumerGroupsGet");
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
| **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | |
| **namespaceName** | **String**| The Namespace name | |
| **eventHubName** | **String**| The Event Hub name | |
| **consumerGroupName** | **String**| The consumer group name | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ConsumerGroupResource**](ConsumerGroupResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the consumer group description. |  -  |

<a id="consumerGroupsListAll"></a>
# **consumerGroupsListAll**
> ConsumerGroupListResult consumerGroupsListAll(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId)



Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group exists in the Namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsumerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConsumerGroupsApi apiInstance = new ConsumerGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ConsumerGroupListResult result = apiInstance.consumerGroupsListAll(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsumerGroupsApi#consumerGroupsListAll");
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
| **resourceGroupName** | **String**| Name of the resource group within the azure subscription. | |
| **namespaceName** | **String**| The Namespace name | |
| **eventHubName** | **String**| The Event Hub name | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ConsumerGroupListResult**](ConsumerGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of consumer groups. |  -  |


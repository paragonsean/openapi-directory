# EventHubsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventHubsCreateOrUpdate**](EventHubsApi.md#eventHubsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName} |  |
| [**eventHubsCreateOrUpdateAuthorizationRule**](EventHubsApi.md#eventHubsCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName} |  |
| [**eventHubsDelete**](EventHubsApi.md#eventHubsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName} |  |
| [**eventHubsDeleteAuthorizationRule**](EventHubsApi.md#eventHubsDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName} |  |
| [**eventHubsGet**](EventHubsApi.md#eventHubsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName} |  |
| [**eventHubsGetAuthorizationRule**](EventHubsApi.md#eventHubsGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName} |  |
| [**eventHubsListAll**](EventHubsApi.md#eventHubsListAll) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs |  |
| [**eventHubsListAuthorizationRules**](EventHubsApi.md#eventHubsListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules |  |
| [**eventHubsListKeys**](EventHubsApi.md#eventHubsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName}/ListKeys |  |
| [**eventHubsPostAuthorizationRule**](EventHubsApi.md#eventHubsPostAuthorizationRule) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName} |  |
| [**eventHubsRegenerateKeys**](EventHubsApi.md#eventHubsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/eventhubs/{eventHubName}/authorizationRules/{authorizationRuleName}/regenerateKeys |  |


<a id="eventHubsCreateOrUpdate"></a>
# **eventHubsCreateOrUpdate**
> EventHubResource eventHubsCreateOrUpdate(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId, parameters)



Creates or updates a new Event Hub as a nested resource within a Namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    EventHubCreateOrUpdateParameters parameters = new EventHubCreateOrUpdateParameters(); // EventHubCreateOrUpdateParameters | Parameters supplied to create an Event Hub resource.
    try {
      EventHubResource result = apiInstance.eventHubsCreateOrUpdate(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsCreateOrUpdate");
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
| **parameters** | [**EventHubCreateOrUpdateParameters**](EventHubCreateOrUpdateParameters.md)| Parameters supplied to create an Event Hub resource. | |

### Return type

[**EventHubResource**](EventHubResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event Hub successfully created. |  -  |

<a id="eventHubsCreateOrUpdateAuthorizationRule"></a>
# **eventHubsCreateOrUpdateAuthorizationRule**
> SharedAccessAuthorizationRuleResource eventHubsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates or updates an AuthorizationRule for the specified Event Hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SharedAccessAuthorizationRuleCreateOrUpdateParameters parameters = new SharedAccessAuthorizationRuleCreateOrUpdateParameters(); // SharedAccessAuthorizationRuleCreateOrUpdateParameters | The shared access AuthorizationRule.
    try {
      SharedAccessAuthorizationRuleResource result = apiInstance.eventHubsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsCreateOrUpdateAuthorizationRule");
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
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**SharedAccessAuthorizationRuleCreateOrUpdateParameters**](SharedAccessAuthorizationRuleCreateOrUpdateParameters.md)| The shared access AuthorizationRule. | |

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event Hub AuthorizationRule successfully created. |  -  |

<a id="eventHubsDelete"></a>
# **eventHubsDelete**
> eventHubsDelete(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId)



Deletes an Event Hub from the specified Namespace and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.eventHubsDelete(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsDelete");
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

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event Hub successfully deleted. |  -  |
| **204** | No content. |  -  |

<a id="eventHubsDeleteAuthorizationRule"></a>
# **eventHubsDeleteAuthorizationRule**
> eventHubsDeleteAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId)



Deletes an Event Hub AuthorizationRule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.eventHubsDeleteAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsDeleteAuthorizationRule");
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
| **authorizationRuleName** | **String**| The authorization rule name. | |
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
| **200** | Event Hub AuthorizationRule successfully deleted. |  -  |
| **204** | No content. |  -  |

<a id="eventHubsGet"></a>
# **eventHubsGet**
> EventHubResource eventHubsGet(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId)



Gets an Event Hubs description for the specified Event Hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      EventHubResource result = apiInstance.eventHubsGet(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsGet");
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

[**EventHubResource**](EventHubResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the Event Hub description. |  -  |

<a id="eventHubsGetAuthorizationRule"></a>
# **eventHubsGetAuthorizationRule**
> SharedAccessAuthorizationRuleResource eventHubsGetAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId)



Gets an AuthorizationRule for an Event Hub by rule name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SharedAccessAuthorizationRuleResource result = apiInstance.eventHubsGetAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsGetAuthorizationRule");
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
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event Hub AuthorizationRule successfully returned. |  -  |

<a id="eventHubsListAll"></a>
# **eventHubsListAll**
> EventHubListResult eventHubsListAll(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Gets all the Event Hubs in a Namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      EventHubListResult result = apiInstance.eventHubsListAll(resourceGroupName, namespaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsListAll");
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
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**EventHubListResult**](EventHubListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of Event Hubs. |  -  |

<a id="eventHubsListAuthorizationRules"></a>
# **eventHubsListAuthorizationRules**
> SharedAccessAuthorizationRuleListResult eventHubsListAuthorizationRules(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId)



Gets the authorization rules for an Event Hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SharedAccessAuthorizationRuleListResult result = apiInstance.eventHubsListAuthorizationRules(resourceGroupName, namespaceName, eventHubName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsListAuthorizationRules");
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

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event Hub AuthorizationRule returned successfully. |  -  |

<a id="eventHubsListKeys"></a>
# **eventHubsListKeys**
> ResourceListKeys eventHubsListKeys(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId)



Gets the ACS and SAS connection strings for the Event Hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ResourceListKeys result = apiInstance.eventHubsListKeys(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsListKeys");
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
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ResourceListKeys**](ResourceListKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connection strings successfully returned. |  -  |

<a id="eventHubsPostAuthorizationRule"></a>
# **eventHubsPostAuthorizationRule**
> SharedAccessAuthorizationRuleResource eventHubsPostAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId)



Gets an AuthorizationRule for an Event Hub by rule name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SharedAccessAuthorizationRuleResource result = apiInstance.eventHubsPostAuthorizationRule(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsPostAuthorizationRule");
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
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event Hub AuthorizationRule successfully returned. |  -  |

<a id="eventHubsRegenerateKeys"></a>
# **eventHubsRegenerateKeys**
> ResourceListKeys eventHubsRegenerateKeys(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Regenerates the ACS and SAS connection strings for the Event Hub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventHubsApi apiInstance = new EventHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace name
    String eventHubName = "eventHubName_example"; // String | The Event Hub name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    RegenerateKeysParameters parameters = new RegenerateKeysParameters(); // RegenerateKeysParameters | Parameters supplied to regenerate the AuthorizationRule Keys (PrimaryKey/SecondaryKey).
    try {
      ResourceListKeys result = apiInstance.eventHubsRegenerateKeys(resourceGroupName, namespaceName, eventHubName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubsApi#eventHubsRegenerateKeys");
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
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**RegenerateKeysParameters**](RegenerateKeysParameters.md)| Parameters supplied to regenerate the AuthorizationRule Keys (PrimaryKey/SecondaryKey). | |

### Return type

[**ResourceListKeys**](ResourceListKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connection strings successfully regenerated. |  -  |


# EventsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventsDeleteEvent**](EventsApi.md#eventsDeleteEvent) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/migrateEvents/{eventName} | Delete the migrate event |
| [**eventsEnumerateEvents**](EventsApi.md#eventsEnumerateEvents) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/migrateEvents | Gets a list of events in the migrate project. |
| [**eventsGetEvent**](EventsApi.md#eventsGetEvent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/migrateEvents/{eventName} | Gets an event in the migrate project. |


<a id="eventsDeleteEvent"></a>
# **eventsDeleteEvent**
> eventsDeleteEvent(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, eventName)

Delete the migrate event

Delete the migrate event. Deleting non-existent migrate event is a no-operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    String eventName = "eventName_example"; // String | Unique name of an event within a migrate project.
    try {
      apiInstance.eventsDeleteEvent(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, eventName);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsDeleteEvent");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |
| **eventName** | **String**| Unique name of an event within a migrate project. | |

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

<a id="eventsEnumerateEvents"></a>
# **eventsEnumerateEvents**
> EventCollection eventsEnumerateEvents(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, continuationToken, pageSize, acceptLanguage)

Gets a list of events in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    String continuationToken = "continuationToken_example"; // String | The continuation token.
    Integer pageSize = 56; // Integer | The number of items to be returned in a single page. This value is honored only if it is less than the 100.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      EventCollection result = apiInstance.eventsEnumerateEvents(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, continuationToken, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsEnumerateEvents");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |
| **continuationToken** | **String**| The continuation token. | [optional] |
| **pageSize** | **Integer**| The number of items to be returned in a single page. This value is honored only if it is less than the 100. | [optional] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**EventCollection**](EventCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="eventsGetEvent"></a>
# **eventsGetEvent**
> MigrateEvent eventsGetEvent(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, eventName)

Gets an event in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    String eventName = "eventName_example"; // String | Unique name of an event within a migrate project.
    try {
      MigrateEvent result = apiInstance.eventsGetEvent(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, eventName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsGetEvent");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |
| **eventName** | **String**| Unique name of an event within a migrate project. | |

### Return type

[**MigrateEvent**](MigrateEvent.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


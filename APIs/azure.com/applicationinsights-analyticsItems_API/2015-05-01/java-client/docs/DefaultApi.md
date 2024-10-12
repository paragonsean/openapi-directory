# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyticsItemsDelete**](DefaultApi.md#analyticsItemsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item |  |
| [**analyticsItemsGet**](DefaultApi.md#analyticsItemsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item |  |
| [**analyticsItemsList**](DefaultApi.md#analyticsItemsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath} |  |
| [**analyticsItemsPut**](DefaultApi.md#analyticsItemsPut) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item |  |


<a id="analyticsItemsDelete"></a>
# **analyticsItemsDelete**
> analyticsItemsDelete(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, id, name)



Deletes a specific Analytics Items defined within an Application Insights component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String scopePath = "analyticsItems"; // String | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String id = "id_example"; // String | The Id of a specific item defined in the Application Insights component
    String name = "name_example"; // String | The name of a specific item defined in the Application Insights component
    try {
      apiInstance.analyticsItemsDelete(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, id, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyticsItemsDelete");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **scopePath** | **String**| Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | [enum: analyticsItems, myanalyticsItems] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **id** | **String**| The Id of a specific item defined in the Application Insights component | [optional] |
| **name** | **String**| The name of a specific item defined in the Application Insights component | [optional] |

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
| **200** | The item has been successfully removed from the Application Insights component |  -  |

<a id="analyticsItemsGet"></a>
# **analyticsItemsGet**
> ApplicationInsightsComponentAnalyticsItem analyticsItemsGet(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, id, name)



Gets a specific Analytics Items defined within an Application Insights component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String scopePath = "analyticsItems"; // String | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String id = "id_example"; // String | The Id of a specific item defined in the Application Insights component
    String name = "name_example"; // String | The name of a specific item defined in the Application Insights component
    try {
      ApplicationInsightsComponentAnalyticsItem result = apiInstance.analyticsItemsGet(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, id, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyticsItemsGet");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **scopePath** | **String**| Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | [enum: analyticsItems, myanalyticsItems] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **id** | **String**| The Id of a specific item defined in the Application Insights component | [optional] |
| **name** | **String**| The name of a specific item defined in the Application Insights component | [optional] |

### Return type

[**ApplicationInsightsComponentAnalyticsItem**](ApplicationInsightsComponentAnalyticsItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single item associated with the Application Insights component. |  -  |

<a id="analyticsItemsList"></a>
# **analyticsItemsList**
> List&lt;ApplicationInsightsComponentAnalyticsItem&gt; analyticsItemsList(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, scope, type, includeContent)



Gets a list of Analytics Items defined within an Application Insights component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String scopePath = "analyticsItems"; // String | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scope = "shared"; // String | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    String type = "none"; // String | Enum indicating the type of the Analytics item.
    Boolean includeContent = true; // Boolean | Flag indicating whether or not to return the content of each applicable item. If false, only return the item information.
    try {
      List<ApplicationInsightsComponentAnalyticsItem> result = apiInstance.analyticsItemsList(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, scope, type, includeContent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyticsItemsList");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **scopePath** | **String**| Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | [enum: analyticsItems, myanalyticsItems] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scope** | **String**| Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | [optional] [default to shared] [enum: shared, user] |
| **type** | **String**| Enum indicating the type of the Analytics item. | [optional] [default to none] [enum: none, query, function, folder, recent] |
| **includeContent** | **Boolean**| Flag indicating whether or not to return the content of each applicable item. If false, only return the item information. | [optional] |

### Return type

[**List&lt;ApplicationInsightsComponentAnalyticsItem&gt;**](ApplicationInsightsComponentAnalyticsItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more items associated with the Application Insights component. |  -  |

<a id="analyticsItemsPut"></a>
# **analyticsItemsPut**
> ApplicationInsightsComponentAnalyticsItem analyticsItemsPut(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, itemProperties, overrideItem)



Adds or Updates a specific Analytics Item within an Application Insights component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String scopePath = "analyticsItems"; // String | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    ApplicationInsightsComponentAnalyticsItem itemProperties = new ApplicationInsightsComponentAnalyticsItem(); // ApplicationInsightsComponentAnalyticsItem | Properties that need to be specified to create a new item and add it to an Application Insights component.
    Boolean overrideItem = true; // Boolean | Flag indicating whether or not to force save an item. This allows overriding an item if it already exists.
    try {
      ApplicationInsightsComponentAnalyticsItem result = apiInstance.analyticsItemsPut(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, itemProperties, overrideItem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyticsItemsPut");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **scopePath** | **String**| Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | [enum: analyticsItems, myanalyticsItems] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **itemProperties** | [**ApplicationInsightsComponentAnalyticsItem**](ApplicationInsightsComponentAnalyticsItem.md)| Properties that need to be specified to create a new item and add it to an Application Insights component. | |
| **overrideItem** | **Boolean**| Flag indicating whether or not to force save an item. This allows overriding an item if it already exists. | [optional] |

### Return type

[**ApplicationInsightsComponentAnalyticsItem**](ApplicationInsightsComponentAnalyticsItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new or updated item associated with the Application Insights component. |  -  |


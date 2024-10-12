# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**favoritesAdd**](DefaultApi.md#favoritesAdd) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId} |  |
| [**favoritesDelete**](DefaultApi.md#favoritesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId} |  |
| [**favoritesGet**](DefaultApi.md#favoritesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId} |  |
| [**favoritesList**](DefaultApi.md#favoritesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites |  |
| [**favoritesUpdate**](DefaultApi.md#favoritesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId} |  |


<a id="favoritesAdd"></a>
# **favoritesAdd**
> ApplicationInsightsComponentFavorite favoritesAdd(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId, favoriteProperties)



Adds a new favorites to an Application Insights component.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String favoriteId = "favoriteId_example"; // String | The Id of a specific favorite defined in the Application Insights component
    ApplicationInsightsComponentFavorite favoriteProperties = new ApplicationInsightsComponentFavorite(); // ApplicationInsightsComponentFavorite | Properties that need to be specified to create a new favorite and add it to an Application Insights component.
    try {
      ApplicationInsightsComponentFavorite result = apiInstance.favoritesAdd(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId, favoriteProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#favoritesAdd");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **favoriteId** | **String**| The Id of a specific favorite defined in the Application Insights component | |
| **favoriteProperties** | [**ApplicationInsightsComponentFavorite**](ApplicationInsightsComponentFavorite.md)| Properties that need to be specified to create a new favorite and add it to an Application Insights component. | |

### Return type

[**ApplicationInsightsComponentFavorite**](ApplicationInsightsComponentFavorite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The newly created favorite that is associated to the Application Insights component. |  -  |

<a id="favoritesDelete"></a>
# **favoritesDelete**
> favoritesDelete(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId)



Remove a favorite that is associated to an Application Insights component.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String favoriteId = "favoriteId_example"; // String | The Id of a specific favorite defined in the Application Insights component
    try {
      apiInstance.favoritesDelete(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#favoritesDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **favoriteId** | **String**| The Id of a specific favorite defined in the Application Insights component | |

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
| **200** | The favorite has been successfully removed from the Application Insights component. |  -  |

<a id="favoritesGet"></a>
# **favoritesGet**
> ApplicationInsightsComponentFavorite favoritesGet(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId)



Get a single favorite by its FavoriteId, defined within an Application Insights component.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String favoriteId = "favoriteId_example"; // String | The Id of a specific favorite defined in the Application Insights component
    try {
      ApplicationInsightsComponentFavorite result = apiInstance.favoritesGet(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#favoritesGet");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **favoriteId** | **String**| The Id of a specific favorite defined in the Application Insights component | |

### Return type

[**ApplicationInsightsComponentFavorite**](ApplicationInsightsComponentFavorite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A favorite definition associated to the Application Insights component. |  -  |

<a id="favoritesList"></a>
# **favoritesList**
> List&lt;ApplicationInsightsComponentFavorite&gt; favoritesList(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteType, sourceType, canFetchContent, tags)



Gets a list of favorites defined within an Application Insights component.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String favoriteType = "shared"; // String | The type of favorite. Value can be either shared or user.
    String sourceType = "retention"; // String | Source type of favorite to return. When left out, the source type defaults to 'other' (not present in this enum).
    Boolean canFetchContent = true; // Boolean | Flag indicating whether or not to return the full content for each applicable favorite. If false, only return summary content for favorites.
    List<String> tags = Arrays.asList(); // List<String> | Tags that must be present on each favorite returned.
    try {
      List<ApplicationInsightsComponentFavorite> result = apiInstance.favoritesList(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteType, sourceType, canFetchContent, tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#favoritesList");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **favoriteType** | **String**| The type of favorite. Value can be either shared or user. | [optional] [default to shared] [enum: shared, user] |
| **sourceType** | **String**| Source type of favorite to return. When left out, the source type defaults to &#39;other&#39; (not present in this enum). | [optional] [enum: retention, notebook, sessions, events, userflows, funnel, impact, segmentation] |
| **canFetchContent** | **Boolean**| Flag indicating whether or not to return the full content for each applicable favorite. If false, only return summary content for favorites. | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tags that must be present on each favorite returned. | [optional] |

### Return type

[**List&lt;ApplicationInsightsComponentFavorite&gt;**](ApplicationInsightsComponentFavorite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more favorite definitions associated to the Application Insights component. |  -  |

<a id="favoritesUpdate"></a>
# **favoritesUpdate**
> ApplicationInsightsComponentFavorite favoritesUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId, favoriteProperties)



Updates a favorite that has already been added to an Application Insights component.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String favoriteId = "favoriteId_example"; // String | The Id of a specific favorite defined in the Application Insights component
    ApplicationInsightsComponentFavorite favoriteProperties = new ApplicationInsightsComponentFavorite(); // ApplicationInsightsComponentFavorite | Properties that need to be specified to update the existing favorite.
    try {
      ApplicationInsightsComponentFavorite result = apiInstance.favoritesUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId, favoriteProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#favoritesUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **favoriteId** | **String**| The Id of a specific favorite defined in the Application Insights component | |
| **favoriteProperties** | [**ApplicationInsightsComponentFavorite**](ApplicationInsightsComponentFavorite.md)| Properties that need to be specified to update the existing favorite. | |

### Return type

[**ApplicationInsightsComponentFavorite**](ApplicationInsightsComponentFavorite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The favorite definition updated. |  -  |


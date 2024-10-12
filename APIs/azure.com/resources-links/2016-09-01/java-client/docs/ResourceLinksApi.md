# ResourceLinksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourceLinksCreateOrUpdate**](ResourceLinksApi.md#resourceLinksCreateOrUpdate) | **PUT** /{linkId} |  |
| [**resourceLinksDelete**](ResourceLinksApi.md#resourceLinksDelete) | **DELETE** /{linkId} |  |
| [**resourceLinksGet**](ResourceLinksApi.md#resourceLinksGet) | **GET** /{linkId} |  |
| [**resourceLinksListAtSourceScope**](ResourceLinksApi.md#resourceLinksListAtSourceScope) | **GET** /{scope}/providers/Microsoft.Resources/links |  |
| [**resourceLinksListAtSubscription**](ResourceLinksApi.md#resourceLinksListAtSubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/links |  |


<a id="resourceLinksCreateOrUpdate"></a>
# **resourceLinksCreateOrUpdate**
> ResourceLink resourceLinksCreateOrUpdate(linkId, apiVersion, parameters)



Creates or updates a resource link between the specified resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceLinksApi apiInstance = new ResourceLinksApi(defaultClient);
    String linkId = "linkId_example"; // String | The fully qualified ID of the resource link. Use the format, /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    ResourceLink parameters = new ResourceLink(); // ResourceLink | Parameters for creating or updating a resource link.
    try {
      ResourceLink result = apiInstance.resourceLinksCreateOrUpdate(linkId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceLinksApi#resourceLinksCreateOrUpdate");
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
| **linkId** | **String**| The fully qualified ID of the resource link. Use the format, /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **parameters** | [**ResourceLink**](ResourceLink.md)| Parameters for creating or updating a resource link. | |

### Return type

[**ResourceLink**](ResourceLink.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the link. |  -  |
| **201** | Created - Returns information about the link. |  -  |

<a id="resourceLinksDelete"></a>
# **resourceLinksDelete**
> resourceLinksDelete(linkId, apiVersion)



Deletes a resource link with the specified ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceLinksApi apiInstance = new ResourceLinksApi(defaultClient);
    String linkId = "linkId_example"; // String | The fully qualified ID of the resource link. Use the format, /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      apiInstance.resourceLinksDelete(linkId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceLinksApi#resourceLinksDelete");
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
| **linkId** | **String**| The fully qualified ID of the resource link. Use the format, /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink | |
| **apiVersion** | **String**| The API version to use for the operation. | |

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
| **204** | No Content |  -  |

<a id="resourceLinksGet"></a>
# **resourceLinksGet**
> ResourceLink resourceLinksGet(linkId, apiVersion)



Gets a resource link with the specified ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceLinksApi apiInstance = new ResourceLinksApi(defaultClient);
    String linkId = "linkId_example"; // String | The fully qualified Id of the resource link. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      ResourceLink result = apiInstance.resourceLinksGet(linkId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceLinksApi#resourceLinksGet");
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
| **linkId** | **String**| The fully qualified Id of the resource link. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**ResourceLink**](ResourceLink.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource link. |  -  |

<a id="resourceLinksListAtSourceScope"></a>
# **resourceLinksListAtSourceScope**
> ResourceLinkResult resourceLinksListAtSourceScope(scope, apiVersion, $filter)



Gets a list of resource links at and below the specified source scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceLinksApi apiInstance = new ResourceLinksApi(defaultClient);
    String scope = "scope_example"; // String | The fully qualified ID of the scope for getting the resource links. For example, to list resource links at and under a resource group, set the scope to /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String $filter = "atScope()"; // String | The filter to apply when getting resource links. To get links only at the specified scope (not below the scope), use Filter.atScope().
    try {
      ResourceLinkResult result = apiInstance.resourceLinksListAtSourceScope(scope, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceLinksApi#resourceLinksListAtSourceScope");
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
| **scope** | **String**| The fully qualified ID of the scope for getting the resource links. For example, to list resource links at and under a resource group, set the scope to /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **$filter** | **String**| The filter to apply when getting resource links. To get links only at the specified scope (not below the scope), use Filter.atScope(). | [optional] [enum: atScope()] |

### Return type

[**ResourceLinkResult**](ResourceLinkResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of links at the specified scope. |  -  |

<a id="resourceLinksListAtSubscription"></a>
# **resourceLinksListAtSubscription**
> ResourceLinkResult resourceLinksListAtSubscription(apiVersion, subscriptionId, $filter)



Gets all the linked resources for the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceLinksApi apiInstance = new ResourceLinksApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the list resource links operation. The supported filter for list resource links is targetId. For example, $filter=targetId eq {value}
    try {
      ResourceLinkResult result = apiInstance.resourceLinksListAtSubscription(apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceLinksApi#resourceLinksListAtSubscription");
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
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the list resource links operation. The supported filter for list resource links is targetId. For example, $filter&#x3D;targetId eq {value} | [optional] |

### Return type

[**ResourceLinkResult**](ResourceLinkResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of resource links for the subscription. |  -  |


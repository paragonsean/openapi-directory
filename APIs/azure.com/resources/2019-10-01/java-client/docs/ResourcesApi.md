# ResourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesCheckExistence**](ResourcesApi.md#resourcesCheckExistence) | **HEAD** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} |  |
| [**resourcesCheckExistenceById**](ResourcesApi.md#resourcesCheckExistenceById) | **HEAD** /{resourceId} |  |
| [**resourcesCreateOrUpdate**](ResourcesApi.md#resourcesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} |  |
| [**resourcesCreateOrUpdateById**](ResourcesApi.md#resourcesCreateOrUpdateById) | **PUT** /{resourceId} |  |
| [**resourcesDelete**](ResourcesApi.md#resourcesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} |  |
| [**resourcesDeleteById**](ResourcesApi.md#resourcesDeleteById) | **DELETE** /{resourceId} |  |
| [**resourcesGet**](ResourcesApi.md#resourcesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} |  |
| [**resourcesGetById**](ResourcesApi.md#resourcesGetById) | **GET** /{resourceId} |  |
| [**resourcesList**](ResourcesApi.md#resourcesList) | **GET** /subscriptions/{subscriptionId}/resources |  |
| [**resourcesMoveResources**](ResourcesApi.md#resourcesMoveResources) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{sourceResourceGroupName}/moveResources | Moves resources from one resource group to another resource group. |
| [**resourcesUpdate**](ResourcesApi.md#resourcesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} |  |
| [**resourcesUpdateById**](ResourcesApi.md#resourcesUpdateById) | **PATCH** /{resourceId} |  |
| [**resourcesValidateMoveResources**](ResourcesApi.md#resourcesValidateMoveResources) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{sourceResourceGroupName}/validateMoveResources | Validates whether resources can be moved from one resource group to another resource group. |


<a id="resourcesCheckExistence"></a>
# **resourcesCheckExistence**
> resourcesCheckExistence(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId)



Checks whether a resource exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource to check. The name is case insensitive.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The resource provider of the resource to check.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type.
    String resourceName = "resourceName_example"; // String | The name of the resource to check whether it exists.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.resourcesCheckExistence(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesCheckExistence");
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
| **resourceGroupName** | **String**| The name of the resource group containing the resource to check. The name is case insensitive. | |
| **resourceProviderNamespace** | **String**| The resource provider of the resource to check. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type. | |
| **resourceName** | **String**| The name of the resource to check whether it exists. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesCheckExistenceById"></a>
# **resourcesCheckExistenceById**
> resourcesCheckExistenceById(resourceId, apiVersion)



Checks by ID whether a resource exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String resourceId = "resourceId_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      apiInstance.resourcesCheckExistenceById(resourceId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesCheckExistenceById");
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
| **resourceId** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name} | |
| **apiVersion** | **String**| The API version to use for the operation. | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesCreateOrUpdate"></a>
# **resourcesCreateOrUpdate**
> GenericResource resourcesCreateOrUpdate(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, parameters)



Creates a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group for the resource. The name is case insensitive.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type of the resource to create.
    String resourceName = "resourceName_example"; // String | The name of the resource to create.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    GenericResource parameters = new GenericResource(); // GenericResource | Parameters for creating or updating the resource.
    try {
      GenericResource result = apiInstance.resourcesCreateOrUpdate(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group for the resource. The name is case insensitive. | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type of the resource to create. | |
| **resourceName** | **String**| The name of the resource to create. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**GenericResource**](GenericResource.md)| Parameters for creating or updating the resource. | |

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource. |  -  |
| **201** | Created - Returns information about the resource. |  -  |
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesCreateOrUpdateById"></a>
# **resourcesCreateOrUpdateById**
> GenericResource resourcesCreateOrUpdateById(resourceId, apiVersion, parameters)



Create a resource by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String resourceId = "resourceId_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    GenericResource parameters = new GenericResource(); // GenericResource | Create or update resource parameters.
    try {
      GenericResource result = apiInstance.resourcesCreateOrUpdateById(resourceId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesCreateOrUpdateById");
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
| **resourceId** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name} | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **parameters** | [**GenericResource**](GenericResource.md)| Create or update resource parameters. | |

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource. |  -  |
| **201** | Created - Returns information about the resource. |  -  |
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesDelete"></a>
# **resourcesDelete**
> resourcesDelete(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId)



Deletes a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource to delete. The name is case insensitive.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type.
    String resourceName = "resourceName_example"; // String | The name of the resource to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.resourcesDelete(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesDelete");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource to delete. The name is case insensitive. | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type. | |
| **resourceName** | **String**| The name of the resource to delete. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesDeleteById"></a>
# **resourcesDeleteById**
> resourcesDeleteById(resourceId, apiVersion)



Deletes a resource by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String resourceId = "resourceId_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      apiInstance.resourcesDeleteById(resourceId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesDeleteById");
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
| **resourceId** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name} | |
| **apiVersion** | **String**| The API version to use for the operation. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesGet"></a>
# **resourcesGet**
> GenericResource resourcesGet(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId)



Gets a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource to get. The name is case insensitive.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type of the resource.
    String resourceName = "resourceName_example"; // String | The name of the resource to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      GenericResource result = apiInstance.resourcesGet(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesGet");
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
| **resourceGroupName** | **String**| The name of the resource group containing the resource to get. The name is case insensitive. | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type of the resource. | |
| **resourceName** | **String**| The name of the resource to get. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesGetById"></a>
# **resourcesGetById**
> GenericResource resourcesGetById(resourceId, apiVersion)



Gets a resource by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String resourceId = "resourceId_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      GenericResource result = apiInstance.resourcesGetById(resourceId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesGetById");
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
| **resourceId** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name} | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesList"></a>
# **resourcesList**
> ResourceListResult resourcesList(apiVersion, subscriptionId, $filter, $expand, $top)



Get all the resources in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.<br><br>The properties you can use for eq (equals) or ne (not equals) are: location, resourceType, name, resourceGroup, identity, identity/principalId, plan, plan/publisher, plan/product, plan/name, plan/version, and plan/promotionCode.<br><br>For example, to filter by a resource type, use: $filter=resourceType eq 'Microsoft.Network/virtualNetworks'<br><br>You can use substringof(value, property) in the filter. The properties you can use for substring are: name and resourceGroup.<br><br>For example, to get all resources with 'demo' anywhere in the name, use: $filter=substringof('demo', name)<br><br>You can link more than one substringof together by adding and/or operators.<br><br>You can filter by tag names and values. For example, to filter for a tag name and value, use $filter=tagName eq 'tag1' and tagValue eq 'Value1'. When you filter by a tag name and value, the tags for each resource are not returned in the results.<br><br>You can use some properties together when filtering. The combinations you can use are: substringof and/or resourceType, plan and plan/publisher and plan/name, identity and identity/principalId.
    String $expand = "$expand_example"; // String | The $expand query parameter. You can expand createdTime and changedTime. For example, to expand both properties, use $expand=changedTime,createdTime
    Integer $top = 56; // Integer | The number of results to return. If null is passed, returns all resource groups.
    try {
      ResourceListResult result = apiInstance.resourcesList(apiVersion, subscriptionId, $filter, $expand, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesList");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation.&lt;br&gt;&lt;br&gt;The properties you can use for eq (equals) or ne (not equals) are: location, resourceType, name, resourceGroup, identity, identity/principalId, plan, plan/publisher, plan/product, plan/name, plan/version, and plan/promotionCode.&lt;br&gt;&lt;br&gt;For example, to filter by a resource type, use: $filter&#x3D;resourceType eq &#39;Microsoft.Network/virtualNetworks&#39;&lt;br&gt;&lt;br&gt;You can use substringof(value, property) in the filter. The properties you can use for substring are: name and resourceGroup.&lt;br&gt;&lt;br&gt;For example, to get all resources with &#39;demo&#39; anywhere in the name, use: $filter&#x3D;substringof(&#39;demo&#39;, name)&lt;br&gt;&lt;br&gt;You can link more than one substringof together by adding and/or operators.&lt;br&gt;&lt;br&gt;You can filter by tag names and values. For example, to filter for a tag name and value, use $filter&#x3D;tagName eq &#39;tag1&#39; and tagValue eq &#39;Value1&#39;. When you filter by a tag name and value, the tags for each resource are not returned in the results.&lt;br&gt;&lt;br&gt;You can use some properties together when filtering. The combinations you can use are: substringof and/or resourceType, plan and plan/publisher and plan/name, identity and identity/principalId. | [optional] |
| **$expand** | **String**| The $expand query parameter. You can expand createdTime and changedTime. For example, to expand both properties, use $expand&#x3D;changedTime,createdTime | [optional] |
| **$top** | **Integer**| The number of results to return. If null is passed, returns all resource groups. | [optional] |

### Return type

[**ResourceListResult**](ResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of resources. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesMoveResources"></a>
# **resourcesMoveResources**
> resourcesMoveResources(sourceResourceGroupName, apiVersion, subscriptionId, parameters)

Moves resources from one resource group to another resource group.

The resources to move must be in the same source resource group. The target resource group may be in a different subscription. When moving resources, both the source group and the target group are locked for the duration of the operation. Write and delete operations are blocked on the groups until the move completes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String sourceResourceGroupName = "sourceResourceGroupName_example"; // String | The name of the resource group containing the resources to move.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ResourcesMoveInfo parameters = new ResourcesMoveInfo(); // ResourcesMoveInfo | Parameters for moving resources.
    try {
      apiInstance.resourcesMoveResources(sourceResourceGroupName, apiVersion, subscriptionId, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesMoveResources");
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
| **sourceResourceGroupName** | **String**| The name of the resource group containing the resources to move. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**ResourcesMoveInfo**](ResourcesMoveInfo.md)| Parameters for moving resources. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesUpdate"></a>
# **resourcesUpdate**
> GenericResource resourcesUpdate(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, parameters)



Updates a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group for the resource. The name is case insensitive.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type of the resource to update.
    String resourceName = "resourceName_example"; // String | The name of the resource to update.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    GenericResource parameters = new GenericResource(); // GenericResource | Parameters for updating the resource.
    try {
      GenericResource result = apiInstance.resourcesUpdate(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group for the resource. The name is case insensitive. | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type of the resource to update. | |
| **resourceName** | **String**| The name of the resource to update. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**GenericResource**](GenericResource.md)| Parameters for updating the resource. | |

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource. |  -  |
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesUpdateById"></a>
# **resourcesUpdateById**
> GenericResource resourcesUpdateById(resourceId, apiVersion, parameters)



Updates a resource by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String resourceId = "resourceId_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    GenericResource parameters = new GenericResource(); // GenericResource | Update resource parameters.
    try {
      GenericResource result = apiInstance.resourcesUpdateById(resourceId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesUpdateById");
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
| **resourceId** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name} | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **parameters** | [**GenericResource**](GenericResource.md)| Update resource parameters. | |

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource. |  -  |
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="resourcesValidateMoveResources"></a>
# **resourcesValidateMoveResources**
> resourcesValidateMoveResources(sourceResourceGroupName, apiVersion, subscriptionId, parameters)

Validates whether resources can be moved from one resource group to another resource group.

This operation checks whether the specified resources can be moved to the target. The resources to move must be in the same source resource group. The target resource group may be in a different subscription. If validation succeeds, it returns HTTP response code 204 (no content). If validation fails, it returns HTTP response code 409 (Conflict) with an error message. Retrieve the URL in the Location header value to check the result of the long-running operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String sourceResourceGroupName = "sourceResourceGroupName_example"; // String | The name of the resource group containing the resources to validate for move.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ResourcesMoveInfo parameters = new ResourcesMoveInfo(); // ResourcesMoveInfo | Parameters for moving resources.
    try {
      apiInstance.resourcesValidateMoveResources(sourceResourceGroupName, apiVersion, subscriptionId, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#resourcesValidateMoveResources");
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
| **sourceResourceGroupName** | **String**| The name of the resource group containing the resources to validate for move. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**ResourcesMoveInfo**](ResourcesMoveInfo.md)| Parameters for moving resources. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |


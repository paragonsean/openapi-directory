# ResourceGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourceGroupsCheckExistence**](ResourceGroupsApi.md#resourceGroupsCheckExistence) | **HEAD** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName} |  |
| [**resourceGroupsCreateOrUpdate**](ResourceGroupsApi.md#resourceGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName} |  |
| [**resourceGroupsDelete**](ResourceGroupsApi.md#resourceGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName} | Deletes a resource group. |
| [**resourceGroupsExportTemplate**](ResourceGroupsApi.md#resourceGroupsExportTemplate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/exportTemplate |  |
| [**resourceGroupsGet**](ResourceGroupsApi.md#resourceGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName} |  |
| [**resourceGroupsList**](ResourceGroupsApi.md#resourceGroupsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups |  |
| [**resourceGroupsListResources**](ResourceGroupsApi.md#resourceGroupsListResources) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/resources |  |
| [**resourceGroupsPatch**](ResourceGroupsApi.md#resourceGroupsPatch) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName} | Updates a resource group. |


<a id="resourceGroupsCheckExistence"></a>
# **resourceGroupsCheckExistence**
> resourceGroupsCheckExistence(resourceGroupName, apiVersion, subscriptionId)



Checks whether a resource group exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to check. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.resourceGroupsCheckExistence(resourceGroupName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#resourceGroupsCheckExistence");
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
| **resourceGroupName** | **String**| The name of the resource group to check. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="resourceGroupsCreateOrUpdate"></a>
# **resourceGroupsCreateOrUpdate**
> ResourceGroup resourceGroupsCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, parameters)



Creates a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to create or update.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ResourceGroup parameters = new ResourceGroup(); // ResourceGroup | Parameters supplied to the create or update a resource group.
    try {
      ResourceGroup result = apiInstance.resourceGroupsCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#resourceGroupsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group to create or update. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**ResourceGroup**](ResourceGroup.md)| Parameters supplied to the create or update a resource group. | |

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the new resource group. |  -  |
| **201** | Created - Returns information about the new resource group. |  -  |

<a id="resourceGroupsDelete"></a>
# **resourceGroupsDelete**
> resourceGroupsDelete(resourceGroupName, apiVersion, subscriptionId)

Deletes a resource group.

When you delete a resource group, all of its resources are also deleted. Deleting a resource group deletes all of its template deployments and currently stored operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to delete. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.resourceGroupsDelete(resourceGroupName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#resourceGroupsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group to delete. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **202** | Accepted |  -  |

<a id="resourceGroupsExportTemplate"></a>
# **resourceGroupsExportTemplate**
> ResourceGroupExportResult resourceGroupsExportTemplate(resourceGroupName, apiVersion, subscriptionId, parameters)



Captures the specified resource group as a template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to export as a template.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ExportTemplateRequest parameters = new ExportTemplateRequest(); // ExportTemplateRequest | Parameters for exporting the template.
    try {
      ResourceGroupExportResult result = apiInstance.resourceGroupsExportTemplate(resourceGroupName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#resourceGroupsExportTemplate");
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
| **resourceGroupName** | **String**| The name of the resource group to export as a template. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**ExportTemplateRequest**](ExportTemplateRequest.md)| Parameters for exporting the template. | |

### Return type

[**ResourceGroupExportResult**](ResourceGroupExportResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the result of the export. |  -  |

<a id="resourceGroupsGet"></a>
# **resourceGroupsGet**
> ResourceGroup resourceGroupsGet(resourceGroupName, apiVersion, subscriptionId)



Gets a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      ResourceGroup result = apiInstance.resourceGroupsGet(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#resourceGroupsGet");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource group. |  -  |

<a id="resourceGroupsList"></a>
# **resourceGroupsList**
> ResourceGroupListResult resourceGroupsList(apiVersion, subscriptionId, $filter, $top)



Gets all the resource groups for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | The number of results to return. If null is passed, returns all resource groups.
    try {
      ResourceGroupListResult result = apiInstance.resourceGroupsList(apiVersion, subscriptionId, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#resourceGroupsList");
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
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**| The number of results to return. If null is passed, returns all resource groups. | [optional] |

### Return type

[**ResourceGroupListResult**](ResourceGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of resource groups. |  -  |

<a id="resourceGroupsListResources"></a>
# **resourceGroupsListResources**
> ResourceListResult resourceGroupsListResources(resourceGroupName, apiVersion, subscriptionId, $filter, $expand, $top)



Get all the resources for a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group with the resources to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    String $expand = "$expand_example"; // String | The $expand query parameter
    Integer $top = 56; // Integer | The number of results to return. If null is passed, returns all resources.
    try {
      ResourceListResult result = apiInstance.resourceGroupsListResources(resourceGroupName, apiVersion, subscriptionId, $filter, $expand, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#resourceGroupsListResources");
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
| **resourceGroupName** | **String**| The resource group with the resources to get. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$expand** | **String**| The $expand query parameter | [optional] |
| **$top** | **Integer**| The number of results to return. If null is passed, returns all resources. | [optional] |

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
| **200** | OK - Returns an array of resources |  -  |

<a id="resourceGroupsPatch"></a>
# **resourceGroupsPatch**
> ResourceGroup resourceGroupsPatch(resourceGroupName, apiVersion, subscriptionId, parameters)

Updates a resource group.

Resource groups can be updated through a simple PATCH operation to a group address. The format of the request is the same as that for creating a resource group. If a field is unspecified, the current value is retained.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to update. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ResourceGroup parameters = new ResourceGroup(); // ResourceGroup | Parameters supplied to update a resource group.
    try {
      ResourceGroup result = apiInstance.resourceGroupsPatch(resourceGroupName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#resourceGroupsPatch");
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
| **resourceGroupName** | **String**| The name of the resource group to update. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**ResourceGroup**](ResourceGroup.md)| Parameters supplied to update a resource group. | |

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource group. |  -  |


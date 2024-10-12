# AssetApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assetsCreate**](AssetApi.md#assetsCreate) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets | Create an Asset. |
| [**assetsDelete**](AssetApi.md#assetsDelete) | **DELETE** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets/{id} | Delete an Asset. |
| [**assetsListQuery**](AssetApi.md#assetsListQuery) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets | Query the list of Assets in a workspace. |
| [**assetsPatch**](AssetApi.md#assetsPatch) | **PATCH** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets/{id} | Update an Asset. |
| [**assetsQueryById**](AssetApi.md#assetsQueryById) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/assets/{id} | Get an Asset. |


<a id="assetsCreate"></a>
# **assetsCreate**
> Asset assetsCreate(subscriptionId, resourceGroup, workspace, asset)

Create an Asset.

Create an Asset from the provided payload.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    Asset asset = new Asset(); // Asset | The Asset to be created.
    try {
      Asset result = apiInstance.assetsCreate(subscriptionId, resourceGroup, workspace, asset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#assetsCreate");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **asset** | [**Asset**](Asset.md)| The Asset to be created. | [optional] |

### Return type

[**Asset**](Asset.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assetsDelete"></a>
# **assetsDelete**
> assetsDelete(subscriptionId, resourceGroup, workspace, id)

Delete an Asset.

Delete the specified Asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String id = "id_example"; // String | The Id of the Asset to delete.
    try {
      apiInstance.assetsDelete(subscriptionId, resourceGroup, workspace, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#assetsDelete");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **id** | **String**| The Id of the Asset to delete. | |

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
| **200** | The resource exists and was deleted successfully. |  -  |
| **204** | The resource does not exist and the request was well formed. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assetsListQuery"></a>
# **assetsListQuery**
> PaginatedAssetList assetsListQuery(subscriptionId, resourceGroup, workspace, runId, name, count, $skipToken, tags, properties, orderby)

Query the list of Assets in a workspace.

If no filter is passed, the query lists all the Assets in the given workspace. The returned list is paginated and the count of items in each page is an optional parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String runId = "runId_example"; // String | The run Id associated with the Assets.
    String name = "name_example"; // String | The object name.
    Integer count = 56; // Integer | The number of items to retrieve in a page.
    String $skipToken = "$skipToken_example"; // String | The continuation token to retrieve the next page.
    String tags = "tags_example"; // String | A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key=value              Example: tagKey1,tagKey2,tagKey3=value3
    String properties = "properties_example"; // String | A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key=value              Example: propKey1,propKey2,propKey3=value3
    String orderby = "CreatedAtDesc"; // String | An option for specifying how to order the list.
    try {
      PaginatedAssetList result = apiInstance.assetsListQuery(subscriptionId, resourceGroup, workspace, runId, name, count, $skipToken, tags, properties, orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#assetsListQuery");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **runId** | **String**| The run Id associated with the Assets. | [optional] |
| **name** | **String**| The object name. | [optional] |
| **count** | **Integer**| The number of items to retrieve in a page. | [optional] |
| **$skipToken** | **String**| The continuation token to retrieve the next page. | [optional] |
| **tags** | **String**| A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3 | [optional] |
| **properties** | **String**| A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3 | [optional] |
| **orderby** | **String**| An option for specifying how to order the list. | [optional] [default to CreatedAtDesc] [enum: CreatedAtDesc, CreatedAtAsc, UpdatedAtDesc, UpdatedAtAsc] |

### Return type

[**PaginatedAssetList**](PaginatedAssetList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assetsPatch"></a>
# **assetsPatch**
> Asset assetsPatch(subscriptionId, resourceGroup, workspace, id, patch)

Update an Asset.

Patch a specific Asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String id = "id_example"; // String | The Id of the Asset to patch.
    List<JsonPatchOperation> patch = Arrays.asList(); // List<JsonPatchOperation> | The payload that is used to patch an Asset.
    try {
      Asset result = apiInstance.assetsPatch(subscriptionId, resourceGroup, workspace, id, patch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#assetsPatch");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **id** | **String**| The Id of the Asset to patch. | |
| **patch** | [**List&lt;JsonPatchOperation&gt;**](JsonPatchOperation.md)| The payload that is used to patch an Asset. | |

### Return type

[**Asset**](Asset.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assetsQueryById"></a>
# **assetsQueryById**
> Asset assetsQueryById(subscriptionId, resourceGroup, workspace, id)

Get an Asset.

Get an Asset by Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String id = "id_example"; // String | The Asset Id.
    try {
      Asset result = apiInstance.assetsQueryById(subscriptionId, resourceGroup, workspace, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#assetsQueryById");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **id** | **String**| The Asset Id. | |

### Return type

[**Asset**](Asset.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error response describing why the operation failed. |  -  |


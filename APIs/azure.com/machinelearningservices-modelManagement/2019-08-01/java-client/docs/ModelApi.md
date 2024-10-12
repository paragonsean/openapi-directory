# ModelApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mLModelsDelete**](ModelApi.md#mLModelsDelete) | **DELETE** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id} | Delete the specified Model. |
| [**mLModelsGetMetrics**](ModelApi.md#mLModelsGetMetrics) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id}/metrics | Retrieve the metrics for a Model. |
| [**mLModelsListQuery**](ModelApi.md#mLModelsListQuery) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models | Query the list of Models in a workspace. |
| [**mLModelsPatch**](ModelApi.md#mLModelsPatch) | **PATCH** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id} | Patch a specific model. |
| [**mLModelsQueryById**](ModelApi.md#mLModelsQueryById) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models/{id} | Gets a model. |
| [**mLModelsRegister**](ModelApi.md#mLModelsRegister) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/models | Register a model. |


<a id="mLModelsDelete"></a>
# **mLModelsDelete**
> mLModelsDelete(subscriptionId, resourceGroup, workspace, id)

Delete the specified Model.

Deletes a model if it exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ModelApi apiInstance = new ModelApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String id = "id_example"; // String | The model id.
    try {
      apiInstance.mLModelsDelete(subscriptionId, resourceGroup, workspace, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#mLModelsDelete");
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
| **id** | **String**| The model id. | |

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

<a id="mLModelsGetMetrics"></a>
# **mLModelsGetMetrics**
> ModelOperationalState mLModelsGetMetrics(subscriptionId, resourceGroup, workspace, id, startDate, endDate)

Retrieve the metrics for a Model.

The operational events collected for the Model are returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ModelApi apiInstance = new ModelApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String id = "id_example"; // String | The Model Id.
    String startDate = "startDate_example"; // String | The start date from which to retrieve metrics, ISO 8601 literal format.
    String endDate = "endDate_example"; // String | The end date from which to retrieve metrics, ISO 8601 literal format.
    try {
      ModelOperationalState result = apiInstance.mLModelsGetMetrics(subscriptionId, resourceGroup, workspace, id, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#mLModelsGetMetrics");
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
| **id** | **String**| The Model Id. | |
| **startDate** | **String**| The start date from which to retrieve metrics, ISO 8601 literal format. | [optional] |
| **endDate** | **String**| The end date from which to retrieve metrics, ISO 8601 literal format. | [optional] |

### Return type

[**ModelOperationalState**](ModelOperationalState.md)

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

<a id="mLModelsListQuery"></a>
# **mLModelsListQuery**
> PaginatedModelList mLModelsListQuery(subscriptionId, resourceGroup, workspace, name, framework, description, count, $skipToken, tags, properties, runId, orderBy)

Query the list of Models in a workspace.

The result list can be filtered using tag and name. If no filter is passed, the query lists all the Models in the given workspace. The returned list is paginated and the count of items in each page is an optional parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ModelApi apiInstance = new ModelApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String name = "name_example"; // String | The object name.
    String framework = "framework_example"; // String | The framework.
    String description = "description_example"; // String | The object description.
    Integer count = 56; // Integer | The number of items to retrieve in a page.
    String $skipToken = "$skipToken_example"; // String | The continuation token to retrieve the next page.
    String tags = "tags_example"; // String | A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key=value              Example: tagKey1,tagKey2,tagKey3=value3
    String properties = "properties_example"; // String | A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key=value              Example: propKey1,propKey2,propKey3=value3
    String runId = "runId_example"; // String | The runId which created the model.
    String orderBy = "CreatedAtDesc"; // String | An option to specify how the models are ordered in the response.
    try {
      PaginatedModelList result = apiInstance.mLModelsListQuery(subscriptionId, resourceGroup, workspace, name, framework, description, count, $skipToken, tags, properties, runId, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#mLModelsListQuery");
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
| **name** | **String**| The object name. | [optional] |
| **framework** | **String**| The framework. | [optional] |
| **description** | **String**| The object description. | [optional] |
| **count** | **Integer**| The number of items to retrieve in a page. | [optional] |
| **$skipToken** | **String**| The continuation token to retrieve the next page. | [optional] |
| **tags** | **String**| A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key&#x3D;value              Example: tagKey1,tagKey2,tagKey3&#x3D;value3 | [optional] |
| **properties** | **String**| A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key&#x3D;value              Example: propKey1,propKey2,propKey3&#x3D;value3 | [optional] |
| **runId** | **String**| The runId which created the model. | [optional] |
| **orderBy** | **String**| An option to specify how the models are ordered in the response. | [optional] [default to CreatedAtDesc] [enum: CreatedAtDesc, CreatedAtAsc, UpdatedAtDesc, UpdatedAtAsc] |

### Return type

[**PaginatedModelList**](PaginatedModelList.md)

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

<a id="mLModelsPatch"></a>
# **mLModelsPatch**
> Model mLModelsPatch(subscriptionId, resourceGroup, workspace, id, patch)

Patch a specific model.

Updates an existing model with the specified patch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ModelApi apiInstance = new ModelApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String id = "id_example"; // String | The model id.
    List<JsonPatchOperation> patch = Arrays.asList(); // List<JsonPatchOperation> | The payload that is used to patch the model.
    try {
      Model result = apiInstance.mLModelsPatch(subscriptionId, resourceGroup, workspace, id, patch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#mLModelsPatch");
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
| **id** | **String**| The model id. | |
| **patch** | [**List&lt;JsonPatchOperation&gt;**](JsonPatchOperation.md)| The payload that is used to patch the model. | |

### Return type

[**Model**](Model.md)

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

<a id="mLModelsQueryById"></a>
# **mLModelsQueryById**
> Model mLModelsQueryById(subscriptionId, resourceGroup, workspace, id)

Gets a model.

Gets a model by model id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ModelApi apiInstance = new ModelApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String id = "id_example"; // String | The model id.
    try {
      Model result = apiInstance.mLModelsQueryById(subscriptionId, resourceGroup, workspace, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#mLModelsQueryById");
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
| **id** | **String**| The model id. | |

### Return type

[**Model**](Model.md)

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

<a id="mLModelsRegister"></a>
# **mLModelsRegister**
> Model mLModelsRegister(subscriptionId, resourceGroup, workspace, model)

Register a model.

Register the model provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ModelApi apiInstance = new ModelApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    Model model = new Model(); // Model | The payload that is used to register the model.
    try {
      Model result = apiInstance.mLModelsRegister(subscriptionId, resourceGroup, workspace, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelApi#mLModelsRegister");
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
| **model** | [**Model**](Model.md)| The payload that is used to register the model. | |

### Return type

[**Model**](Model.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The model registration was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


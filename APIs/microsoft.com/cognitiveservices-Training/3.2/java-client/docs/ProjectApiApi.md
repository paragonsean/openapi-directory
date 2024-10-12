# ProjectApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProject**](ProjectApiApi.md#createProject) | **POST** /projects | Create a project. |
| [**deleteIteration**](ProjectApiApi.md#deleteIteration) | **DELETE** /projects/{projectId}/iterations/{iterationId} | Delete a specific iteration of a project. |
| [**deleteProject**](ProjectApiApi.md#deleteProject) | **DELETE** /projects/{projectId} | Delete a specific project. |
| [**exportIteration**](ProjectApiApi.md#exportIteration) | **POST** /projects/{projectId}/iterations/{iterationId}/export | Export a trained iteration. |
| [**exportProject**](ProjectApiApi.md#exportProject) | **GET** /projects/{projectId}/export | Exports a project. |
| [**getExports**](ProjectApiApi.md#getExports) | **GET** /projects/{projectId}/iterations/{iterationId}/export | Get the list of exports for a specific iteration. |
| [**getImagePerformanceCount**](ProjectApiApi.md#getImagePerformanceCount) | **GET** /projects/{projectId}/iterations/{iterationId}/performance/images/count | Gets the number of images tagged with the provided {tagIds} that have prediction results from  training for the provided iteration {iterationId}. |
| [**getImagePerformances**](ProjectApiApi.md#getImagePerformances) | **GET** /projects/{projectId}/iterations/{iterationId}/performance/images | Get image with its prediction for a given project iteration. |
| [**getIteration**](ProjectApiApi.md#getIteration) | **GET** /projects/{projectId}/iterations/{iterationId} | Get a specific iteration. |
| [**getIterationPerformance**](ProjectApiApi.md#getIterationPerformance) | **GET** /projects/{projectId}/iterations/{iterationId}/performance | Get detailed performance information about an iteration. |
| [**getIterations**](ProjectApiApi.md#getIterations) | **GET** /projects/{projectId}/iterations | Get iterations for the project. |
| [**getProject**](ProjectApiApi.md#getProject) | **GET** /projects/{projectId} | Get a specific project. |
| [**getProjects**](ProjectApiApi.md#getProjects) | **GET** /projects | Get your projects. |
| [**importProject**](ProjectApiApi.md#importProject) | **POST** /projects/import | Imports a project. |
| [**publishIteration**](ProjectApiApi.md#publishIteration) | **POST** /projects/{projectId}/iterations/{iterationId}/publish | Publish a specific iteration. |
| [**trainProject**](ProjectApiApi.md#trainProject) | **POST** /projects/{projectId}/train | Queues project for training. |
| [**unpublishIteration**](ProjectApiApi.md#unpublishIteration) | **DELETE** /projects/{projectId}/iterations/{iterationId}/publish | Unpublish a specific iteration. |
| [**updateIteration**](ProjectApiApi.md#updateIteration) | **PATCH** /projects/{projectId}/iterations/{iterationId} | Update a specific iteration. |
| [**updateProject**](ProjectApiApi.md#updateProject) | **PATCH** /projects/{projectId} | Update a specific project. |


<a id="createProject"></a>
# **createProject**
> Project createProject(name, description, domainId, classificationType, targetExportPlatforms)

Create a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    String name = "My New Project"; // String | Name of the project.
    String description = "A test project"; // String | The description of the project.
    UUID domainId = UUID.fromString("ee85a74c-405e-4adc-bb47-ffa8ca0c9f31"); // UUID | The id of the domain to use for this project. Defaults to General.
    String classificationType = "Multiclass"; // String | The type of classifier to create for this project.
    List<String> targetExportPlatforms = Arrays.asList(); // List<String> | List of platforms the trained model is intending exporting to.
    try {
      Project result = apiInstance.createProject(name, description, domainId, classificationType, targetExportPlatforms);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#createProject");
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
| **name** | **String**| Name of the project. | |
| **description** | **String**| The description of the project. | [optional] |
| **domainId** | **UUID**| The id of the domain to use for this project. Defaults to General. | [optional] |
| **classificationType** | **String**| The type of classifier to create for this project. | [optional] [enum: Multiclass, Multilabel] |
| **targetExportPlatforms** | [**List&lt;String&gt;**](String.md)| List of platforms the trained model is intending exporting to. | [optional] [enum: CoreML, TensorFlow, DockerFile, ONNX, VAIDK] |

### Return type

[**Project**](Project.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="deleteIteration"></a>
# **deleteIteration**
> deleteIteration(projectId, iterationId)

Delete a specific iteration of a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | The iteration id.
    try {
      apiInstance.deleteIteration(projectId, iterationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#deleteIteration");
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
| **projectId** | **UUID**| The project id. | |
| **iterationId** | **UUID**| The iteration id. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response |  -  |

<a id="deleteProject"></a>
# **deleteProject**
> deleteProject(projectId)

Delete a specific project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id.
    try {
      apiInstance.deleteProject(projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#deleteProject");
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
| **projectId** | **UUID**| The project id. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response |  -  |

<a id="exportIteration"></a>
# **exportIteration**
> Export exportIteration(projectId, iterationId, platform, flavor)

Export a trained iteration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | The iteration id.
    String platform = "CoreML"; // String | The target platform.
    String flavor = "Linux"; // String | The flavor of the target platform.
    try {
      Export result = apiInstance.exportIteration(projectId, iterationId, platform, flavor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#exportIteration");
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
| **projectId** | **UUID**| The project id. | |
| **iterationId** | **UUID**| The iteration id. | |
| **platform** | **String**| The target platform. | [enum: CoreML, TensorFlow, DockerFile, ONNX, VAIDK] |
| **flavor** | **String**| The flavor of the target platform. | [optional] [enum: Linux, Windows, ONNX10, ONNX12, ARM, TensorFlowNormal, TensorFlowLite] |

### Return type

[**Export**](Export.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="exportProject"></a>
# **exportProject**
> ProjectExport exportProject(projectId)

Exports a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id of the project to export.
    try {
      ProjectExport result = apiInstance.exportProject(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#exportProject");
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
| **projectId** | **UUID**| The project id of the project to export. | |

### Return type

[**ProjectExport**](ProjectExport.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="getExports"></a>
# **getExports**
> List&lt;Export&gt; getExports(projectId, iterationId)

Get the list of exports for a specific iteration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | The iteration id.
    try {
      List<Export> result = apiInstance.getExports(projectId, iterationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#getExports");
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
| **projectId** | **UUID**| The project id. | |
| **iterationId** | **UUID**| The iteration id. | |

### Return type

[**List&lt;Export&gt;**](Export.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="getImagePerformanceCount"></a>
# **getImagePerformanceCount**
> Integer getImagePerformanceCount(projectId, iterationId, tagIds)

Gets the number of images tagged with the provided {tagIds} that have prediction results from  training for the provided iteration {iterationId}.

The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id.
    UUID iterationId = UUID.fromString("cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12"); // UUID | The iteration id. Defaults to workspace.
    List<UUID> tagIds = Arrays.asList(); // List<UUID> | A list of tags ids to filter the images to count. Defaults to all tags when null.
    try {
      Integer result = apiInstance.getImagePerformanceCount(projectId, iterationId, tagIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#getImagePerformanceCount");
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
| **projectId** | **UUID**| The project id. | |
| **iterationId** | **UUID**| The iteration id. Defaults to workspace. | |
| **tagIds** | [**List&lt;UUID&gt;**](UUID.md)| A list of tags ids to filter the images to count. Defaults to all tags when null. | [optional] |

### Return type

**Integer**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="getImagePerformances"></a>
# **getImagePerformances**
> List&lt;ImagePerformance&gt; getImagePerformances(projectId, iterationId, tagIds, orderBy, take, skip)

Get image with its prediction for a given project iteration.

This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.  The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id.
    UUID iterationId = UUID.fromString("b7b9d99c-a2c6-4658-9900-a98d2ff5bc66"); // UUID | The iteration id. Defaults to workspace.
    List<UUID> tagIds = Arrays.asList(); // List<UUID> | A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20.
    String orderBy = "Newest"; // String | The ordering. Defaults to newest.
    Integer take = 50; // Integer | Maximum number of images to return. Defaults to 50, limited to 256.
    Integer skip = 0; // Integer | Number of images to skip before beginning the image batch. Defaults to 0.
    try {
      List<ImagePerformance> result = apiInstance.getImagePerformances(projectId, iterationId, tagIds, orderBy, take, skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#getImagePerformances");
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
| **projectId** | **UUID**| The project id. | |
| **iterationId** | **UUID**| The iteration id. Defaults to workspace. | |
| **tagIds** | [**List&lt;UUID&gt;**](UUID.md)| A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20. | [optional] |
| **orderBy** | **String**| The ordering. Defaults to newest. | [optional] [enum: Newest, Oldest] |
| **take** | **Integer**| Maximum number of images to return. Defaults to 50, limited to 256. | [optional] [default to 50] |
| **skip** | **Integer**| Number of images to skip before beginning the image batch. Defaults to 0. | [optional] [default to 0] |

### Return type

[**List&lt;ImagePerformance&gt;**](ImagePerformance.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="getIteration"></a>
# **getIteration**
> Iteration getIteration(projectId, iterationId)

Get a specific iteration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The id of the project the iteration belongs to.
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | The id of the iteration to get.
    try {
      Iteration result = apiInstance.getIteration(projectId, iterationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#getIteration");
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
| **projectId** | **UUID**| The id of the project the iteration belongs to. | |
| **iterationId** | **UUID**| The id of the iteration to get. | |

### Return type

[**Iteration**](Iteration.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="getIterationPerformance"></a>
# **getIterationPerformance**
> IterationPerformance getIterationPerformance(projectId, iterationId, threshold, overlapThreshold)

Get detailed performance information about an iteration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The id of the project the iteration belongs to.
    UUID iterationId = UUID.fromString("fe1e83c4-6f50-4899-9544-6bb08cf0e15a"); // UUID | The id of the iteration to get.
    Float threshold = 0.9F; // Float | The threshold used to determine true predictions.
    Float overlapThreshold = 3.4F; // Float | If applicable, the bounding box overlap threshold used to determine true predictions.
    try {
      IterationPerformance result = apiInstance.getIterationPerformance(projectId, iterationId, threshold, overlapThreshold);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#getIterationPerformance");
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
| **projectId** | **UUID**| The id of the project the iteration belongs to. | |
| **iterationId** | **UUID**| The id of the iteration to get. | |
| **threshold** | **Float**| The threshold used to determine true predictions. | [optional] |
| **overlapThreshold** | **Float**| If applicable, the bounding box overlap threshold used to determine true predictions. | [optional] |

### Return type

[**IterationPerformance**](IterationPerformance.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="getIterations"></a>
# **getIterations**
> List&lt;Iteration&gt; getIterations(projectId)

Get iterations for the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    try {
      List<Iteration> result = apiInstance.getIterations(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#getIterations");
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
| **projectId** | **UUID**| The project id. | |

### Return type

[**List&lt;Iteration&gt;**](Iteration.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="getProject"></a>
# **getProject**
> Project getProject(projectId)

Get a specific project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The id of the project to get.
    try {
      Project result = apiInstance.getProject(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#getProject");
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
| **projectId** | **UUID**| The id of the project to get. | |

### Return type

[**Project**](Project.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="getProjects"></a>
# **getProjects**
> List&lt;Project&gt; getProjects()

Get your projects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    try {
      List<Project> result = apiInstance.getProjects();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#getProjects");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Project&gt;**](Project.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="importProject"></a>
# **importProject**
> Project importProject(token)

Imports a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    String token = "token"; // String | Token generated from the export project call.
    try {
      Project result = apiInstance.importProject(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#importProject");
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
| **token** | **String**| Token generated from the export project call. | |

### Return type

[**Project**](Project.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="publishIteration"></a>
# **publishIteration**
> Boolean publishIteration(projectId, iterationId, publishName, predictionId)

Publish a specific iteration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | The iteration id.
    String publishName = "Model1"; // String | The name to give the published iteration.
    String predictionId = "/subscriptions/{subscription}/resourceGroups/{resource group name}/providers/Microsoft.CognitiveServices/accounts/{resource name}"; // String | The id of the prediction resource to publish to.
    try {
      Boolean result = apiInstance.publishIteration(projectId, iterationId, publishName, predictionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#publishIteration");
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
| **projectId** | **UUID**| The project id. | |
| **iterationId** | **UUID**| The iteration id. | |
| **publishName** | **String**| The name to give the published iteration. | |
| **predictionId** | **String**| The id of the prediction resource to publish to. | |

### Return type

**Boolean**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="trainProject"></a>
# **trainProject**
> Iteration trainProject(projectId, trainingType, reservedBudgetInHours, forceTrain, notificationEmailAddress, trainingParameters)

Queues project for training.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    String trainingType = "Regular"; // String | The type of training to use to train the project (default: Regular).
    Integer reservedBudgetInHours = 0; // Integer | The number of hours reserved as budget for training (if applicable).
    Boolean forceTrain = false; // Boolean | Whether to force train even if dataset and configuration does not change (default: false).
    String notificationEmailAddress = "notificationEmailAddress_example"; // String | The email address to send notification to when training finishes (default: null).
    TrainingParameters trainingParameters = new TrainingParameters(); // TrainingParameters | Additional training parameters passed in to control how the project is trained.
    try {
      Iteration result = apiInstance.trainProject(projectId, trainingType, reservedBudgetInHours, forceTrain, notificationEmailAddress, trainingParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#trainProject");
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
| **projectId** | **UUID**| The project id. | |
| **trainingType** | **String**| The type of training to use to train the project (default: Regular). | [optional] [enum: Regular, Advanced] |
| **reservedBudgetInHours** | **Integer**| The number of hours reserved as budget for training (if applicable). | [optional] [default to 0] |
| **forceTrain** | **Boolean**| Whether to force train even if dataset and configuration does not change (default: false). | [optional] [default to false] |
| **notificationEmailAddress** | **String**| The email address to send notification to when training finishes (default: null). | [optional] |
| **trainingParameters** | [**TrainingParameters**](TrainingParameters.md)| Additional training parameters passed in to control how the project is trained. | [optional] |

### Return type

[**Iteration**](Iteration.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="unpublishIteration"></a>
# **unpublishIteration**
> unpublishIteration(projectId, iterationId)

Unpublish a specific iteration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id.
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | The iteration id.
    try {
      apiInstance.unpublishIteration(projectId, iterationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#unpublishIteration");
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
| **projectId** | **UUID**| The project id. | |
| **iterationId** | **UUID**| The iteration id. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response |  -  |

<a id="updateIteration"></a>
# **updateIteration**
> Iteration updateIteration(projectId, iterationId, iteration)

Update a specific iteration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | Project id.
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | Iteration id.
    Iteration iteration = new Iteration(); // Iteration | The updated iteration model.
    try {
      Iteration result = apiInstance.updateIteration(projectId, iterationId, iteration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#updateIteration");
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
| **projectId** | **UUID**| Project id. | |
| **iterationId** | **UUID**| Iteration id. | |
| **iteration** | [**Iteration**](Iteration.md)| The updated iteration model. | |

### Return type

[**Iteration**](Iteration.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="updateProject"></a>
# **updateProject**
> Project updateProject(projectId, project)

Update a specific project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The id of the project to update.
    Project project = new Project(); // Project | The updated project model.
    try {
      Project result = apiInstance.updateProject(projectId, project);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApiApi#updateProject");
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
| **projectId** | **UUID**| The id of the project to update. | |
| **project** | [**Project**](Project.md)| The updated project model. | |

### Return type

[**Project**](Project.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |


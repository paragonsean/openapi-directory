# ProjectApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProject**](ProjectApiApi.md#createProject) | **POST** /projects | Create a project |
| [**deleteIteration**](ProjectApiApi.md#deleteIteration) | **DELETE** /projects/{projectId}/iterations/{iterationId} | Delete a specific iteration of a project |
| [**deleteProject**](ProjectApiApi.md#deleteProject) | **DELETE** /projects/{projectId} | Delete a specific project |
| [**exportIteration**](ProjectApiApi.md#exportIteration) | **POST** /projects/{projectId}/iterations/{iterationId}/export | Export a trained iteration |
| [**getExports**](ProjectApiApi.md#getExports) | **GET** /projects/{projectId}/iterations/{iterationId}/export | Get the list of exports for a specific iteration |
| [**getIteration**](ProjectApiApi.md#getIteration) | **GET** /projects/{projectId}/iterations/{iterationId} | Get a specific iteration |
| [**getIterationPerformance**](ProjectApiApi.md#getIterationPerformance) | **GET** /projects/{projectId}/iterations/{iterationId}/performance | Get detailed performance information about a trained iteration |
| [**getIterations**](ProjectApiApi.md#getIterations) | **GET** /projects/{projectId}/iterations | Get iterations for the project |
| [**getProject**](ProjectApiApi.md#getProject) | **GET** /projects/{projectId} | Get a specific project |
| [**getProjects**](ProjectApiApi.md#getProjects) | **GET** /projects | Get your projects |
| [**trainProject**](ProjectApiApi.md#trainProject) | **POST** /projects/{projectId}/train | Queues project for training |
| [**updateIteration**](ProjectApiApi.md#updateIteration) | **PATCH** /projects/{projectId}/iterations/{iterationId} | Update a specific iteration |
| [**updateProject**](ProjectApiApi.md#updateProject) | **PATCH** /projects/{projectId} | Update a specific project |


<a id="createProject"></a>
# **createProject**
> Project createProject(name, trainingKey, description, domainId)

Create a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    String name = "My New Project"; // String | Name of the project
    String trainingKey = "{API Key}"; // String | 
    String description = "A test project"; // String | The description of the project
    UUID domainId = UUID.fromString("ee85a74c-405e-4adc-bb47-ffa8ca0c9f31"); // UUID | The id of the domain to use for this project. Defaults to General
    try {
      Project result = apiInstance.createProject(name, trainingKey, description, domainId);
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
| **name** | **String**| Name of the project | |
| **trainingKey** | **String**|  | |
| **description** | **String**| The description of the project | [optional] |
| **domainId** | **UUID**| The id of the domain to use for this project. Defaults to General | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteIteration"></a>
# **deleteIteration**
> deleteIteration(projectId, iterationId, trainingKey)

Delete a specific iteration of a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | The iteration id
    String trainingKey = "{API Key}"; // String | 
    try {
      apiInstance.deleteIteration(projectId, iterationId, trainingKey);
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
| **projectId** | **UUID**| The project id | |
| **iterationId** | **UUID**| The iteration id | |
| **trainingKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="deleteProject"></a>
# **deleteProject**
> deleteProject(projectId, trainingKey)

Delete a specific project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    try {
      apiInstance.deleteProject(projectId, trainingKey);
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="exportIteration"></a>
# **exportIteration**
> Export exportIteration(projectId, iterationId, platform, trainingKey)

Export a trained iteration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | The iteration id
    String platform = "tensorflow"; // String | The target platform (coreml or tensorflow)
    String trainingKey = "{API Key}"; // String | 
    try {
      Export result = apiInstance.exportIteration(projectId, iterationId, platform, trainingKey);
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
| **projectId** | **UUID**| The project id | |
| **iterationId** | **UUID**| The iteration id | |
| **platform** | **String**| The target platform (coreml or tensorflow) | |
| **trainingKey** | **String**|  | |

### Return type

[**Export**](Export.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getExports"></a>
# **getExports**
> List&lt;Export&gt; getExports(projectId, iterationId, trainingKey)

Get the list of exports for a specific iteration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | The iteration id
    String trainingKey = "{API Key}"; // String | 
    try {
      List<Export> result = apiInstance.getExports(projectId, iterationId, trainingKey);
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
| **projectId** | **UUID**| The project id | |
| **iterationId** | **UUID**| The iteration id | |
| **trainingKey** | **String**|  | |

### Return type

[**List&lt;Export&gt;**](Export.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getIteration"></a>
# **getIteration**
> Iteration getIteration(projectId, iterationId, trainingKey)

Get a specific iteration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The id of the project the iteration belongs to
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | The id of the iteration to get
    String trainingKey = "{API Key}"; // String | 
    try {
      Iteration result = apiInstance.getIteration(projectId, iterationId, trainingKey);
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
| **projectId** | **UUID**| The id of the project the iteration belongs to | |
| **iterationId** | **UUID**| The id of the iteration to get | |
| **trainingKey** | **String**|  | |

### Return type

[**Iteration**](Iteration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getIterationPerformance"></a>
# **getIterationPerformance**
> IterationPerformance getIterationPerformance(projectId, iterationId, threshold, trainingKey)

Get detailed performance information about a trained iteration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id
    UUID iterationId = UUID.fromString("fe1e83c4-6f50-4899-9544-6bb08cf0e15a"); // UUID | The id of the trained iteration
    Float threshold = 0.9F; // Float | The 0 to 1 threshold to determine positive prediction
    String trainingKey = "{API Key}"; // String | 
    try {
      IterationPerformance result = apiInstance.getIterationPerformance(projectId, iterationId, threshold, trainingKey);
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
| **projectId** | **UUID**| The project id | |
| **iterationId** | **UUID**| The id of the trained iteration | |
| **threshold** | **Float**| The 0 to 1 threshold to determine positive prediction | |
| **trainingKey** | **String**|  | |

### Return type

[**IterationPerformance**](IterationPerformance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getIterations"></a>
# **getIterations**
> List&lt;Iteration&gt; getIterations(projectId, trainingKey)

Get iterations for the project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    try {
      List<Iteration> result = apiInstance.getIterations(projectId, trainingKey);
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |

### Return type

[**List&lt;Iteration&gt;**](Iteration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getProject"></a>
# **getProject**
> Project getProject(projectId, trainingKey)

Get a specific project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The id of the project to get
    String trainingKey = "{API Key}"; // String | 
    try {
      Project result = apiInstance.getProject(projectId, trainingKey);
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
| **projectId** | **UUID**| The id of the project to get | |
| **trainingKey** | **String**|  | |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getProjects"></a>
# **getProjects**
> List&lt;Project&gt; getProjects(trainingKey)

Get your projects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    String trainingKey = "{API Key}"; // String | 
    try {
      List<Project> result = apiInstance.getProjects(trainingKey);
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

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **trainingKey** | **String**|  | |

### Return type

[**List&lt;Project&gt;**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="trainProject"></a>
# **trainProject**
> Iteration trainProject(projectId, trainingKey)

Queues project for training

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    try {
      Iteration result = apiInstance.trainProject(projectId, trainingKey);
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |

### Return type

[**Iteration**](Iteration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateIteration"></a>
# **updateIteration**
> Iteration updateIteration(projectId, iterationId, trainingKey, iteration)

Update a specific iteration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | Project id
    UUID iterationId = UUID.fromString("e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"); // UUID | Iteration id
    String trainingKey = "{API Key}"; // String | 
    Iteration iteration = new Iteration(); // Iteration | The updated iteration model
    try {
      Iteration result = apiInstance.updateIteration(projectId, iterationId, trainingKey, iteration);
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
| **projectId** | **UUID**| Project id | |
| **iterationId** | **UUID**| Iteration id | |
| **trainingKey** | **String**|  | |
| **iteration** | [**Iteration**](Iteration.md)| The updated iteration model | |

### Return type

[**Iteration**](Iteration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateProject"></a>
# **updateProject**
> Project updateProject(projectId, trainingKey, project)

Update a specific project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ProjectApiApi apiInstance = new ProjectApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The id of the project to update
    String trainingKey = "{API Key}"; // String | 
    Project project = new Project(); // Project | The updated project model
    try {
      Project result = apiInstance.updateProject(projectId, trainingKey, project);
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
| **projectId** | **UUID**| The id of the project to update | |
| **trainingKey** | **String**|  | |
| **project** | [**Project**](Project.md)| The updated project model | |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


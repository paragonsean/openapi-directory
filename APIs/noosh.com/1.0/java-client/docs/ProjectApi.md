# ProjectApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attachProject**](ProjectApi.md#attachProject) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/children | Attach children projects to specific Project |
| [**deleteProject**](ProjectApi.md#deleteProject) | **DELETE** /v1/workgroups/{workgroup_id}/projects/{project_id} | Archieve a specific Project |
| [**getProject**](ProjectApi.md#getProject) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id} | Get a specific Project |
| [**getProjectList**](ProjectApi.md#getProjectList) | **GET** /v1/workgroups/{workgroup_id}/projects | List the projects |
| [**patchProject**](ProjectApi.md#patchProject) | **PATCH** /v1/workgroups/{workgroup_id}/projects/{project_id} | Patch a specific Project |
| [**postProject**](ProjectApi.md#postProject) | **POST** /v1/workgroups/{workgroup_id}/projects | Create a Project |
| [**putProject**](ProjectApi.md#putProject) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id} | Update a specific Project |


<a id="attachProject"></a>
# **attachProject**
> HTTPStatusVO attachProject(workgroupId, projectId, projectIdListVO)

Attach children projects to specific Project

Attach children projects to specific Project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    ProjectIdListVO projectIdListVO = new ProjectIdListVO(); // ProjectIdListVO | 
    try {
      HTTPStatusVO result = apiInstance.attachProject(workgroupId, projectId, projectIdListVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#attachProject");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **projectIdListVO** | [**ProjectIdListVO**](ProjectIdListVO.md)|  | [optional] |

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful update |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

<a id="deleteProject"></a>
# **deleteProject**
> HTTPStatusVO deleteProject(workgroupId, projectId)

Archieve a specific Project

Archieve a specific Project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      HTTPStatusVO result = apiInstance.deleteProject(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#deleteProject");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful archive |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

<a id="getProject"></a>
# **getProject**
> ProjectExpandVO getProject(workgroupId, projectId)

Get a specific Project

Get a specific Project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      ProjectExpandVO result = apiInstance.getProject(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProject");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |

### Return type

[**ProjectExpandVO**](ProjectExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getProjectList"></a>
# **getProjectList**
> ProjectListVO getProjectList(workgroupId)

List the projects

List the projects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      ProjectListVO result = apiInstance.getProjectList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectList");
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
| **workgroupId** | **String**|  | |

### Return type

[**ProjectListVO**](ProjectListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="patchProject"></a>
# **patchProject**
> HTTPStatusVO patchProject(workgroupId, projectId, projectPatchPO)

Patch a specific Project

Patch a specific Project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    ProjectPatchPO projectPatchPO = new ProjectPatchPO(); // ProjectPatchPO | 
    try {
      HTTPStatusVO result = apiInstance.patchProject(workgroupId, projectId, projectPatchPO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#patchProject");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **projectPatchPO** | [**ProjectPatchPO**](ProjectPatchPO.md)|  | [optional] |

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful patch |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

<a id="postProject"></a>
# **postProject**
> ProjectVO postProject(workgroupId, projectPersistVO)

Create a Project

Create a Project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    ProjectPersistVO projectPersistVO = new ProjectPersistVO(); // ProjectPersistVO | 
    try {
      ProjectVO result = apiInstance.postProject(workgroupId, projectPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#postProject");
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
| **workgroupId** | **String**|  | |
| **projectPersistVO** | [**ProjectPersistVO**](ProjectPersistVO.md)|  | [optional] |

### Return type

[**ProjectVO**](ProjectVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful created |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

<a id="putProject"></a>
# **putProject**
> HTTPStatusVO putProject(workgroupId, projectId, projectPersistVO)

Update a specific Project

Update a specific Project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    ProjectPersistVO projectPersistVO = new ProjectPersistVO(); // ProjectPersistVO | 
    try {
      HTTPStatusVO result = apiInstance.putProject(workgroupId, projectId, projectPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#putProject");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **projectPersistVO** | [**ProjectPersistVO**](ProjectPersistVO.md)|  | [optional] |

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful update |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |


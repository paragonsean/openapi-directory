# JobApi

All URIs are relative to *http://microcks.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateImportJob**](JobApi.md#activateImportJob) | **PUT** /jobs/{id}/activate | Activate an ImportJob |
| [**createImportJob**](JobApi.md#createImportJob) | **POST** /jobs | Create ImportJob |
| [**deleteImportJob**](JobApi.md#deleteImportJob) | **DELETE** /jobs/{id} | Delete ImportJob |
| [**getImportJobCounter**](JobApi.md#getImportJobCounter) | **GET** /jobs/count | Get the ImportJobs counter |
| [**getImportJobs**](JobApi.md#getImportJobs) | **GET** /jobs | Get ImportJobs |
| [**jobsIdGet**](JobApi.md#jobsIdGet) | **GET** /jobs/{id} | Get ImportJob |
| [**jobsIdPost**](JobApi.md#jobsIdPost) | **POST** /jobs/{id} | Update ImportJob |
| [**startImportJob**](JobApi.md#startImportJob) | **PUT** /jobs/{id}/start | Start an ImportJob |
| [**stopImportJob**](JobApi.md#stopImportJob) | **PUT** /jobs/{id}/stop | Stop an ImportJob |
| [**uploadArtifact**](JobApi.md#uploadArtifact) | **POST** /artifact/upload | Upload an artifact |


<a id="activateImportJob"></a>
# **activateImportJob**
> ImportJob activateImportJob(id)

Activate an ImportJob

Make an ImportJob active, so that it is executed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of ImportJob to manage
    try {
      ImportJob result = apiInstance.activateImportJob(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#activateImportJob");
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
| **id** | **String**| Unique identifier of ImportJob to manage | |

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ImportJob is activated |  -  |

<a id="createImportJob"></a>
# **createImportJob**
> ImportJob createImportJob(importJob)

Create ImportJob

Create a new ImportJob

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    ImportJob importJob = new ImportJob(); // ImportJob | 
    try {
      ImportJob result = apiInstance.createImportJob(importJob);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#createImportJob");
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
| **importJob** | [**ImportJob**](ImportJob.md)|  | |

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created ImportJob |  -  |

<a id="deleteImportJob"></a>
# **deleteImportJob**
> deleteImportJob(id)

Delete ImportJob

Delete an ImportJob

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of ImportJob to manage
    try {
      apiInstance.deleteImportJob(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#deleteImportJob");
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
| **id** | **String**| Unique identifier of ImportJob to manage | |

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ImportJob deleted |  -  |

<a id="getImportJobCounter"></a>
# **getImportJobCounter**
> Counter getImportJobCounter()

Get the ImportJobs counter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    try {
      Counter result = apiInstance.getImportJobCounter();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#getImportJobCounter");
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

[**Counter**](Counter.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number of ImportJobs in datastore |  -  |

<a id="getImportJobs"></a>
# **getImportJobs**
> List&lt;ImportJob&gt; getImportJobs(page, size, name)

Get ImportJobs

Retrieve a list of ImportJobs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    Integer page = 56; // Integer | Page of ImportJobs to retrieve (starts at and defaults to 0)
    Integer size = 56; // Integer | Size of a page. Maximum number of ImportJobs to include in a response (defaults to 20)
    String name = "name_example"; // String | Name like criterion for query
    try {
      List<ImportJob> result = apiInstance.getImportJobs(page, size, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#getImportJobs");
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
| **page** | **Integer**| Page of ImportJobs to retrieve (starts at and defaults to 0) | [optional] |
| **size** | **Integer**| Size of a page. Maximum number of ImportJobs to include in a response (defaults to 20) | [optional] |
| **name** | **String**| Name like criterion for query | [optional] |

### Return type

[**List&lt;ImportJob&gt;**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of found ImportJobs |  -  |

<a id="jobsIdGet"></a>
# **jobsIdGet**
> ImportJob jobsIdGet(id)

Get ImportJob

Retrieve an ImportJob using its identifier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of ImportJob to manage
    try {
      ImportJob result = apiInstance.jobsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobsIdGet");
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
| **id** | **String**| Unique identifier of ImportJob to manage | |

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Found ImportJob |  -  |

<a id="jobsIdPost"></a>
# **jobsIdPost**
> ImportJob jobsIdPost(id, importJob)

Update ImportJob

Update an ImportJob

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of ImportJob to manage
    ImportJob importJob = new ImportJob(); // ImportJob | 
    try {
      ImportJob result = apiInstance.jobsIdPost(id, importJob);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobsIdPost");
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
| **id** | **String**| Unique identifier of ImportJob to manage | |
| **importJob** | [**ImportJob**](ImportJob.md)|  | |

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated ImportJob |  -  |

<a id="startImportJob"></a>
# **startImportJob**
> ImportJob startImportJob(id)

Start an ImportJob

Starting an ImportJob forces it to immediatly import mock definitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of ImportJob to manage
    try {
      ImportJob result = apiInstance.startImportJob(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#startImportJob");
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
| **id** | **String**| Unique identifier of ImportJob to manage | |

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Started ImportJob |  -  |

<a id="stopImportJob"></a>
# **stopImportJob**
> ImportJob stopImportJob(id)

Stop an ImportJob

Stopping an ImportJob desactivate it, so that it won&#39;t execute at next schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of ImportJob to manage
    try {
      ImportJob result = apiInstance.stopImportJob(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#stopImportJob");
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
| **id** | **String**| Unique identifier of ImportJob to manage | |

### Return type

[**ImportJob**](ImportJob.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stopped ImportJob |  -  |

<a id="uploadArtifact"></a>
# **uploadArtifact**
> String uploadArtifact(mainArtifact, _file)

Upload an artifact

Uploads an artifact to be imported by Microcks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    Boolean mainArtifact = true; // Boolean | Flag telling if this should be considered as primary or secondary artifact. Default to 'true'
    File _file = new File("/path/to/file"); // File | The artifact to upload
    try {
      String result = apiInstance.uploadArtifact(mainArtifact, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#uploadArtifact");
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
| **mainArtifact** | **Boolean**| Flag telling if this should be considered as primary or secondary artifact. Default to &#39;true&#39; | |
| **_file** | **File**| The artifact to upload | |

### Return type

**String**

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Artifact was imported and Service found |  -  |
| **204** | No file attribute found in uploaded data |  -  |
| **400** | Artifact content is invalid and not understood |  -  |


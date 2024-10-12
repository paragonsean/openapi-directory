# TasksClassicApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addFile**](TasksClassicApi.md#addFile) | **POST** /tasks/{taskId}/files/input | Adds files to a given task. |
| [**delete14**](TasksClassicApi.md#delete14) | **DELETE** /tasks/{taskId} | Removes a task. |
| [**getContacts1**](TasksClassicApi.md#getContacts1) | **GET** /tasks/{taskId}/contacts | Returns contacts of a given task. |
| [**getCustomFields7**](TasksClassicApi.md#getCustomFields7) | **GET** /tasks/{taskId}/customFields | Returns custom fields of a given task. |
| [**getDates3**](TasksClassicApi.md#getDates3) | **GET** /tasks/{taskId}/dates | Returns dates of a given task. |
| [**getInstructions2**](TasksClassicApi.md#getInstructions2) | **GET** /tasks/{taskId}/instructions | Returns instructions of a given task. |
| [**getProgress**](TasksClassicApi.md#getProgress) | **GET** /tasks/{taskId}/progress | Returns progress of a given task. |
| [**getTaskFiles**](TasksClassicApi.md#getTaskFiles) | **GET** /tasks/{taskId}/files | Returns lists of files of a given task. |
| [**start1**](TasksClassicApi.md#start1) | **POST** /tasks/{taskId}/start | Starts a task. |
| [**updateClientTaskPONumber**](TasksClassicApi.md#updateClientTaskPONumber) | **PUT** /tasks/{taskId}/clientTaskPONumber | Updates Client Task PO Number of a given task. |
| [**updateContacts1**](TasksClassicApi.md#updateContacts1) | **PUT** /tasks/{taskId}/contacts | Updates contacts of a given task. |
| [**updateCustomFields5**](TasksClassicApi.md#updateCustomFields5) | **PUT** /tasks/{taskId}/customFields | Updates custom fields of a given task. |
| [**updateDates2**](TasksClassicApi.md#updateDates2) | **PUT** /tasks/{taskId}/dates | Updates dates of a given task. |
| [**updateInstructions3**](TasksClassicApi.md#updateInstructions3) | **PUT** /tasks/{taskId}/instructions | Updates instructions of a given task. |
| [**updateName**](TasksClassicApi.md#updateName) | **PUT** /tasks/{taskId}/name | Updates name of a given task. |


<a id="addFile"></a>
# **addFile**
> addFile(taskId, fileDTO)

Adds files to a given task.

Adds files to a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    FileDTO fileDTO = new FileDTO(); // FileDTO | 
    try {
      apiInstance.addFile(taskId, fileDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#addFile");
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
| **taskId** | **String**| task&#39;s internal identifier | |
| **fileDTO** | [**FileDTO**](FileDTO.md)|  | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="delete14"></a>
# **delete14**
> delete14(taskId, removeFilesFromDisc, removeExternalProjects, forceJobsRemoval)

Removes a task.

Removes a task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    Boolean removeFilesFromDisc = true; // Boolean | remove files from disc
    Boolean removeExternalProjects = true; // Boolean | remove external projects (ie. from CAT Tool)
    Boolean forceJobsRemoval = true; // Boolean | force jobs removal (ie. started or ready)
    try {
      apiInstance.delete14(taskId, removeFilesFromDisc, removeExternalProjects, forceJobsRemoval);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#delete14");
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
| **taskId** | **String**| task&#39;s internal identifier | |
| **removeFilesFromDisc** | **Boolean**| remove files from disc | [optional] |
| **removeExternalProjects** | **Boolean**| remove external projects (ie. from CAT Tool) | [optional] |
| **forceJobsRemoval** | **Boolean**| force jobs removal (ie. started or ready) | [optional] |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="getContacts1"></a>
# **getContacts1**
> ContactsDTO getContacts1(taskId)

Returns contacts of a given task.

Returns contacts of a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    try {
      ContactsDTO result = apiInstance.getContacts1(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#getContacts1");
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
| **taskId** | **String**| task&#39;s internal identifier | |

### Return type

[**ContactsDTO**](ContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getCustomFields7"></a>
# **getCustomFields7**
> List&lt;CustomFieldDTO&gt; getCustomFields7(taskId)

Returns custom fields of a given task.

Returns custom fields of a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    try {
      List<CustomFieldDTO> result = apiInstance.getCustomFields7(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#getCustomFields7");
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
| **taskId** | **String**| task&#39;s internal identifier | |

### Return type

[**List&lt;CustomFieldDTO&gt;**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDates3"></a>
# **getDates3**
> ProjectDatesDTO getDates3(taskId)

Returns dates of a given task.

Returns dates of a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    try {
      ProjectDatesDTO result = apiInstance.getDates3(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#getDates3");
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
| **taskId** | **String**| task&#39;s internal identifier | |

### Return type

[**ProjectDatesDTO**](ProjectDatesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getInstructions2"></a>
# **getInstructions2**
> InstructionsDTO getInstructions2(taskId)

Returns instructions of a given task.

Returns instructions of a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    try {
      InstructionsDTO result = apiInstance.getInstructions2(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#getInstructions2");
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
| **taskId** | **String**| task&#39;s internal identifier | |

### Return type

[**InstructionsDTO**](InstructionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getProgress"></a>
# **getProgress**
> TaskProgressDTO getProgress(taskId)

Returns progress of a given task.

Returns progress of a given task. Progress contains information about task&#39;s status (ie. opened or ready) and current phase (ie. translation). Workflow phase is defined as the first one which contains not ready jobs (ie. opened or started). When no such job exists then workflow phase is not included.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    try {
      TaskProgressDTO result = apiInstance.getProgress(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#getProgress");
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
| **taskId** | **String**| task&#39;s internal identifier | |

### Return type

[**TaskProgressDTO**](TaskProgressDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getTaskFiles"></a>
# **getTaskFiles**
> TaskFilesDTO getTaskFiles(taskId)

Returns lists of files of a given task.

Returns several lists of files for a given task: input files divided by type, output files, bundles, files per job, preview files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    try {
      TaskFilesDTO result = apiInstance.getTaskFiles(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#getTaskFiles");
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
| **taskId** | **String**| task&#39;s internal identifier | |

### Return type

[**TaskFilesDTO**](TaskFilesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="start1"></a>
# **start1**
> start1(taskId)

Starts a task.

Starts a task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    try {
      apiInstance.start1(taskId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#start1");
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
| **taskId** | **String**| task&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateClientTaskPONumber"></a>
# **updateClientTaskPONumber**
> StringDTO updateClientTaskPONumber(taskId, stringDTO)

Updates Client Task PO Number of a given task.

Updates Client Task PO Number of a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | Updated Client Task PO Number of a given task.
    try {
      StringDTO result = apiInstance.updateClientTaskPONumber(taskId, stringDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#updateClientTaskPONumber");
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
| **taskId** | **String**| task&#39;s internal identifier | |
| **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Client Task PO Number of a given task. | |

### Return type

[**StringDTO**](StringDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateContacts1"></a>
# **updateContacts1**
> ContactsDTO updateContacts1(taskId, contactsDTO)

Updates contacts of a given task.

Updates contacts of a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    ContactsDTO contactsDTO = new ContactsDTO(); // ContactsDTO | Updated contacts of given task.
    try {
      ContactsDTO result = apiInstance.updateContacts1(taskId, contactsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#updateContacts1");
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
| **taskId** | **String**| task&#39;s internal identifier | |
| **contactsDTO** | [**ContactsDTO**](ContactsDTO.md)| Updated contacts of given task. | |

### Return type

[**ContactsDTO**](ContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateCustomFields5"></a>
# **updateCustomFields5**
> List&lt;CustomFieldDTO&gt; updateCustomFields5(taskId, customFieldDTO)

Updates custom fields of a given task.

Updates custom fields of a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    List<CustomFieldDTO> customFieldDTO = new CustomFieldDTO(); // List<CustomFieldDTO> | Updated custom fields
    try {
      List<CustomFieldDTO> result = apiInstance.updateCustomFields5(taskId, customFieldDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#updateCustomFields5");
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
| **taskId** | **String**| task&#39;s internal identifier | |
| **customFieldDTO** | [**List&lt;CustomFieldDTO&gt;**](CustomFieldDTO.md)| Updated custom fields | |

### Return type

[**List&lt;CustomFieldDTO&gt;**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateDates2"></a>
# **updateDates2**
> ProjectDatesDTO updateDates2(taskId, projectDatesDTO)

Updates dates of a given task.

Updates dates of a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    ProjectDatesDTO projectDatesDTO = new ProjectDatesDTO(); // ProjectDatesDTO | Updated dates of a given task.
    try {
      ProjectDatesDTO result = apiInstance.updateDates2(taskId, projectDatesDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#updateDates2");
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
| **taskId** | **String**| task&#39;s internal identifier | |
| **projectDatesDTO** | [**ProjectDatesDTO**](ProjectDatesDTO.md)| Updated dates of a given task. | |

### Return type

[**ProjectDatesDTO**](ProjectDatesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateInstructions3"></a>
# **updateInstructions3**
> InstructionsDTO updateInstructions3(taskId, instructionsDTO)

Updates instructions of a given task.

Updates instructions of a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    InstructionsDTO instructionsDTO = new InstructionsDTO(); // InstructionsDTO | Updated instructions of a given task.
    try {
      InstructionsDTO result = apiInstance.updateInstructions3(taskId, instructionsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#updateInstructions3");
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
| **taskId** | **String**| task&#39;s internal identifier | |
| **instructionsDTO** | [**InstructionsDTO**](InstructionsDTO.md)| Updated instructions of a given task. | |

### Return type

[**InstructionsDTO**](InstructionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateName"></a>
# **updateName**
> StringDTO updateName(taskId, stringDTO)

Updates name of a given task.

Updates name of a given task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    TasksClassicApi apiInstance = new TasksClassicApi(defaultClient);
    String taskId = "taskId_example"; // String | task's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | 
    try {
      StringDTO result = apiInstance.updateName(taskId, stringDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksClassicApi#updateName");
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
| **taskId** | **String**| task&#39;s internal identifier | |
| **stringDTO** | [**StringDTO**](StringDTO.md)|  | |

### Return type

[**StringDTO**](StringDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


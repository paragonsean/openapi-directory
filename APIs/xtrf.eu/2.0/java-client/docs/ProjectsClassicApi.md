# ProjectsClassicApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**create5**](ProjectsClassicApi.md#create5) | **POST** /projects | Creates a new Classic Project. |
| [**createLanguageCombination**](ProjectsClassicApi.md#createLanguageCombination) | **POST** /projects/{projectId}/languageCombinations | Creates a new language combination for a given project without creating a task. |
| [**createPayable**](ProjectsClassicApi.md#createPayable) | **POST** /projects/{projectId}/finance/payables | Adds a payable to a project. |
| [**createReceivable**](ProjectsClassicApi.md#createReceivable) | **POST** /projects/{projectId}/finance/receivables | Adds a receivable to a project. |
| [**createTask**](ProjectsClassicApi.md#createTask) | **POST** /projects/{projectId}/tasks | Creates a new task for a given project. |
| [**delete12**](ProjectsClassicApi.md#delete12) | **DELETE** /projects/{projectId} | Removes a project. |
| [**deletePayable**](ProjectsClassicApi.md#deletePayable) | **DELETE** /projects/{projectId}/finance/payables/{payableId} | Deletes a payable. |
| [**deleteReceivable**](ProjectsClassicApi.md#deleteReceivable) | **DELETE** /projects/{projectId}/finance/receivables/{receivableId} | Deletes a receivable. |
| [**getAllIds6**](ProjectsClassicApi.md#getAllIds6) | **GET** /projects/ids | Returns projects&#39; internal identifiers. |
| [**getById7**](ProjectsClassicApi.md#getById7) | **GET** /projects/{projectId} | Returns project details. |
| [**getContacts**](ProjectsClassicApi.md#getContacts) | **GET** /projects/{projectId}/contacts | Returns contacts of a given project. |
| [**getCustomFields5**](ProjectsClassicApi.md#getCustomFields5) | **GET** /projects/{projectId}/customFields | Returns custom fields of a given project. |
| [**getDates1**](ProjectsClassicApi.md#getDates1) | **GET** /projects/{projectId}/dates | Returns dates of a given project. |
| [**getFileById**](ProjectsClassicApi.md#getFileById) | **GET** /projects/files/{fileId}/download | Downloads a file. |
| [**getFinance**](ProjectsClassicApi.md#getFinance) | **GET** /projects/{projectId}/finance | Returns finance of a given project. |
| [**getInstructions**](ProjectsClassicApi.md#getInstructions) | **GET** /projects/{projectId}/instructions | Returns instructions of a given project. |
| [**updateContacts**](ProjectsClassicApi.md#updateContacts) | **PUT** /projects/{projectId}/contacts | Updates contacts of a given project. |
| [**updateCustomFields3**](ProjectsClassicApi.md#updateCustomFields3) | **PUT** /projects/{projectId}/customFields | Updates custom fields of a given project. |
| [**updateDates1**](ProjectsClassicApi.md#updateDates1) | **PUT** /projects/{projectId}/dates | Updates dates of a given project. |
| [**updateInstructions1**](ProjectsClassicApi.md#updateInstructions1) | **PUT** /projects/{projectId}/instructions | Updates instructions of a given project. |
| [**updatePayable**](ProjectsClassicApi.md#updatePayable) | **PUT** /projects/{projectId}/finance/payables/{payableId} | Updates a payable. |
| [**updateReceivable**](ProjectsClassicApi.md#updateReceivable) | **PUT** /projects/{projectId}/finance/receivables/{receivableId} | Updates a receivable. |


<a id="create5"></a>
# **create5**
> ProjectDTOv1 create5(classicProjectCreateDTO)

Creates a new Classic Project.

Creates a new Classic Project. If the specified service ID refers to Smart Project, 400 Bad Request is returned instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    ClassicProjectCreateDTO classicProjectCreateDTO = new ClassicProjectCreateDTO(); // ClassicProjectCreateDTO | Created a new Classic Project.
    try {
      ProjectDTOv1 result = apiInstance.create5(classicProjectCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#create5");
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
| **classicProjectCreateDTO** | [**ClassicProjectCreateDTO**](ClassicProjectCreateDTO.md)| Created a new Classic Project. | |

### Return type

[**ProjectDTOv1**](ProjectDTOv1.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="createLanguageCombination"></a>
# **createLanguageCombination**
> CommonLanguageCombinationDTO createLanguageCombination(projectId, commonLanguageCombinationDTO)

Creates a new language combination for a given project without creating a task.

Creates a new language combination for a given project without creating a task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    CommonLanguageCombinationDTO commonLanguageCombinationDTO = new CommonLanguageCombinationDTO(); // CommonLanguageCombinationDTO | Created language combination for a given project without creating a task.
    try {
      CommonLanguageCombinationDTO result = apiInstance.createLanguageCombination(projectId, commonLanguageCombinationDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#createLanguageCombination");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **commonLanguageCombinationDTO** | [**CommonLanguageCombinationDTO**](CommonLanguageCombinationDTO.md)| Created language combination for a given project without creating a task. | |

### Return type

[**CommonLanguageCombinationDTO**](CommonLanguageCombinationDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="createPayable"></a>
# **createPayable**
> PayableDTO createPayable(projectId, payableCreateDTO)

Adds a payable to a project.

Adds a payable to a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    PayableCreateDTO payableCreateDTO = new PayableCreateDTO(); // PayableCreateDTO | 
    try {
      PayableDTO result = apiInstance.createPayable(projectId, payableCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#createPayable");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **payableCreateDTO** | [**PayableCreateDTO**](PayableCreateDTO.md)|  | |

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="createReceivable"></a>
# **createReceivable**
> ReceivableDTO createReceivable(projectId, receivableCreateDTO)

Adds a receivable to a project.

Adds a receivable to a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    ReceivableCreateDTO receivableCreateDTO = new ReceivableCreateDTO(); // ReceivableCreateDTO | 
    try {
      ReceivableDTO result = apiInstance.createReceivable(projectId, receivableCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#createReceivable");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **receivableCreateDTO** | [**ReceivableCreateDTO**](ReceivableCreateDTO.md)|  | |

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="createTask"></a>
# **createTask**
> TaskDTO createTask(projectId, taskCreateDTO)

Creates a new task for a given project.

Creates a new task for a given project.&lt;p&gt;   Required fields:   &lt;ul&gt;     &lt;li&gt;languageCombination&lt;/li&gt;     &lt;li&gt;specializationId&lt;/li&gt;     &lt;li&gt;workflowId&lt;/li&gt;   &lt;/ul&gt; &lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    TaskCreateDTO taskCreateDTO = new TaskCreateDTO(); // TaskCreateDTO | Created new task for a given project.
    try {
      TaskDTO result = apiInstance.createTask(projectId, taskCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#createTask");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **taskCreateDTO** | [**TaskCreateDTO**](TaskCreateDTO.md)| Created new task for a given project. | |

### Return type

[**TaskDTO**](TaskDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="delete12"></a>
# **delete12**
> delete12(projectId)

Removes a project.

Removes a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      apiInstance.delete12(projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#delete12");
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
| **projectId** | **String**| project&#39;s internal identifier | |

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

<a id="deletePayable"></a>
# **deletePayable**
> deletePayable(projectId, payableId)

Deletes a payable.

Deletes a payable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    Long payableId = 56L; // Long | payable's internal identifier
    try {
      apiInstance.deletePayable(projectId, payableId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#deletePayable");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **payableId** | **Long**| payable&#39;s internal identifier | |

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

<a id="deleteReceivable"></a>
# **deleteReceivable**
> deleteReceivable(projectId, receivableId)

Deletes a receivable.

Deletes a receivable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    Long receivableId = 56L; // Long | receivable's internal identifier
    try {
      apiInstance.deleteReceivable(projectId, receivableId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#deleteReceivable");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **receivableId** | **Long**| receivable&#39;s internal identifier | |

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

<a id="getAllIds6"></a>
# **getAllIds6**
> List&lt;Integer&gt; getAllIds6(updatedSince)

Returns projects&#39; internal identifiers.

Returns projects&#39; internal identifiers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    Long updatedSince = 56L; // Long | only projects modified since this timestamp
    try {
      List<Integer> result = apiInstance.getAllIds6(updatedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#getAllIds6");
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
| **updatedSince** | **Long**| only projects modified since this timestamp | [optional] |

### Return type

**List&lt;Integer&gt;**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getById7"></a>
# **getById7**
> ProjectDTOv1 getById7(projectId, embed)

Returns project details.

Returns project details. If the specified project ID refers to Smart Project, 400 Bad Request is returned instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    String embed = "embed_example"; // String | list of additional fields which should be embedded in the response (available options: tasks)
    try {
      ProjectDTOv1 result = apiInstance.getById7(projectId, embed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#getById7");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **embed** | **String**| list of additional fields which should be embedded in the response (available options: tasks) | [optional] |

### Return type

[**ProjectDTOv1**](ProjectDTOv1.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getContacts"></a>
# **getContacts**
> ContactsDTO getContacts(projectId)

Returns contacts of a given project.

Returns contacts of a given project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      ContactsDTO result = apiInstance.getContacts(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#getContacts");
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
| **projectId** | **String**| project&#39;s internal identifier | |

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
| **0** | Success |  -  |

<a id="getCustomFields5"></a>
# **getCustomFields5**
> List&lt;CustomFieldDTO&gt; getCustomFields5(projectId)

Returns custom fields of a given project.

Returns custom fields of a given project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      List<CustomFieldDTO> result = apiInstance.getCustomFields5(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#getCustomFields5");
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
| **projectId** | **String**| project&#39;s internal identifier | |

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
| **0** | Success |  -  |

<a id="getDates1"></a>
# **getDates1**
> ProjectDatesDTO getDates1(projectId)

Returns dates of a given project.

Returns dates of a given project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      ProjectDatesDTO result = apiInstance.getDates1(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#getDates1");
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
| **projectId** | **String**| project&#39;s internal identifier | |

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
| **0** | Success |  -  |

<a id="getFileById"></a>
# **getFileById**
> getFileById(fileId)

Downloads a file.

Downloads a file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String fileId = "fileId_example"; // String | file's internal identifier
    try {
      apiInstance.getFileById(fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#getFileById");
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
| **fileId** | **String**| file&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success! |  -  |

<a id="getFinance"></a>
# **getFinance**
> FinanceDTO getFinance(projectId)

Returns finance of a given project.

Returns finance of a given project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      FinanceDTO result = apiInstance.getFinance(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#getFinance");
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
| **projectId** | **String**| project&#39;s internal identifier | |

### Return type

[**FinanceDTO**](FinanceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getInstructions"></a>
# **getInstructions**
> InstructionsDTO getInstructions(projectId)

Returns instructions of a given project.

Returns instructions of a given project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      InstructionsDTO result = apiInstance.getInstructions(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#getInstructions");
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
| **projectId** | **String**| project&#39;s internal identifier | |

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
| **0** | Success |  -  |

<a id="updateContacts"></a>
# **updateContacts**
> ContactsDTO updateContacts(projectId, contactsDTO)

Updates contacts of a given project.

Updates contacts of a given project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    ContactsDTO contactsDTO = new ContactsDTO(); // ContactsDTO | Updated contacts of a given project.
    try {
      ContactsDTO result = apiInstance.updateContacts(projectId, contactsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#updateContacts");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **contactsDTO** | [**ContactsDTO**](ContactsDTO.md)| Updated contacts of a given project. | |

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
| **0** | Success |  -  |

<a id="updateCustomFields3"></a>
# **updateCustomFields3**
> List&lt;CustomFieldDTO&gt; updateCustomFields3(projectId, customFieldDTO)

Updates custom fields of a given project.

Updates custom fields of a given project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    List<CustomFieldDTO> customFieldDTO = new CustomFieldDTO(); // List<CustomFieldDTO> | Updated custom fields of a given project.
    try {
      List<CustomFieldDTO> result = apiInstance.updateCustomFields3(projectId, customFieldDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#updateCustomFields3");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **customFieldDTO** | [**List&lt;CustomFieldDTO&gt;**](CustomFieldDTO.md)| Updated custom fields of a given project. | |

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
| **0** | Success |  -  |

<a id="updateDates1"></a>
# **updateDates1**
> ProjectDatesDTO updateDates1(projectId, projectDatesDTO)

Updates dates of a given project.

Updates dates of a given project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    ProjectDatesDTO projectDatesDTO = new ProjectDatesDTO(); // ProjectDatesDTO | Updated dates of a given project..
    try {
      ProjectDatesDTO result = apiInstance.updateDates1(projectId, projectDatesDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#updateDates1");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **projectDatesDTO** | [**ProjectDatesDTO**](ProjectDatesDTO.md)| Updated dates of a given project.. | |

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
| **0** | Success |  -  |

<a id="updateInstructions1"></a>
# **updateInstructions1**
> InstructionsDTO updateInstructions1(projectId, instructionsDTO)

Updates instructions of a given project.

Updates instructions of a given project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    InstructionsDTO instructionsDTO = new InstructionsDTO(); // InstructionsDTO | Updated instructions of a given project.
    try {
      InstructionsDTO result = apiInstance.updateInstructions1(projectId, instructionsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#updateInstructions1");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **instructionsDTO** | [**InstructionsDTO**](InstructionsDTO.md)| Updated instructions of a given project. | |

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
| **0** | Success |  -  |

<a id="updatePayable"></a>
# **updatePayable**
> PayableDTO updatePayable(projectId, payableId, payableDTO)

Updates a payable.

Updates a payable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    Long payableId = 56L; // Long | payable's internal identifier
    PayableDTO payableDTO = new PayableDTO(); // PayableDTO | 
    try {
      PayableDTO result = apiInstance.updatePayable(projectId, payableId, payableDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#updatePayable");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **payableId** | **Long**| payable&#39;s internal identifier | |
| **payableDTO** | [**PayableDTO**](PayableDTO.md)|  | |

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateReceivable"></a>
# **updateReceivable**
> ReceivableDTO updateReceivable(projectId, receivableId, receivableDTO)

Updates a receivable.

Updates a receivable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsClassicApi apiInstance = new ProjectsClassicApi(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    Long receivableId = 56L; // Long | receivable's internal identifier
    ReceivableDTO receivableDTO = new ReceivableDTO(); // ReceivableDTO | 
    try {
      ReceivableDTO result = apiInstance.updateReceivable(projectId, receivableId, receivableDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsClassicApi#updateReceivable");
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
| **projectId** | **String**| project&#39;s internal identifier | |
| **receivableId** | **Long**| receivable&#39;s internal identifier | |
| **receivableDTO** | [**ReceivableDTO**](ReceivableDTO.md)|  | |

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |


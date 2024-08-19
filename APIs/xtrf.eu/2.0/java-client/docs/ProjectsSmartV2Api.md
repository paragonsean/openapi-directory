# ProjectsSmartV2Api

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addExternalFileLinks**](ProjectsSmartV2Api.md#addExternalFileLinks) | **POST** /v2/projects/{projectId}/files/addExternalLink |  |
| [**addFileLinks1**](ProjectsSmartV2Api.md#addFileLinks1) | **POST** /v2/projects/{projectId}/files/addLink | Adds file links to the project as added by PM. |
| [**addFiles1**](ProjectsSmartV2Api.md#addFiles1) | **PUT** /v2/projects/{projectId}/files/add | Adds files to the project as added by PM. |
| [**addJobToProcess**](ProjectsSmartV2Api.md#addJobToProcess) | **POST** /v2/projects/{projectId}/addJob | Returns process id. |
| [**archive**](ProjectsSmartV2Api.md#archive) | **POST** /v2/projects/files/archive | Prepares a ZIP archive that contains the specified files. |
| [**changeStatus2**](ProjectsSmartV2Api.md#changeStatus2) | **PUT** /v2/projects/{projectId}/status | Changes project status if possible (400 Bad Request is returned otherwise). |
| [**create6**](ProjectsSmartV2Api.md#create6) | **POST** /v2/projects | Creates a new Smart Project. |
| [**createPayable2**](ProjectsSmartV2Api.md#createPayable2) | **POST** /v2/projects/{projectId}/finance/payables | Adds a payable to a project. |
| [**createReceivable2**](ProjectsSmartV2Api.md#createReceivable2) | **POST** /v2/projects/{projectId}/finance/receivables | Adds a receivable to a project. |
| [**deletePayable2**](ProjectsSmartV2Api.md#deletePayable2) | **DELETE** /v2/projects/{projectId}/finance/payables/{payableId} | Deletes a payable. |
| [**deleteReceivable2**](ProjectsSmartV2Api.md#deleteReceivable2) | **DELETE** /v2/projects/{projectId}/finance/receivables/{receivableId} | Deletes a receivable. |
| [**getByExternalId1**](ProjectsSmartV2Api.md#getByExternalId1) | **GET** /v2/projects/for-external-id/{externalProjectId} | Returns project details. |
| [**getById9**](ProjectsSmartV2Api.md#getById9) | **GET** /v2/projects/{projectId} | Returns project details. |
| [**getCATToolProjectInfo**](ProjectsSmartV2Api.md#getCATToolProjectInfo) | **GET** /v2/projects/{projectId}/catToolProject | Returns if cat tool project is created or queued. |
| [**getContacts2**](ProjectsSmartV2Api.md#getContacts2) | **GET** /v2/projects/{projectId}/clientContacts | Returns Client Contacts information for a project. |
| [**getCustomFields8**](ProjectsSmartV2Api.md#getCustomFields8) | **GET** /v2/projects/{projectId}/customFields | Returns a list of custom field keys and values for a project. |
| [**getDeliverableFiles**](ProjectsSmartV2Api.md#getDeliverableFiles) | **GET** /v2/projects/{projectId}/files/deliverable | Returns list of files in a project, that are ready to be delivered to client. |
| [**getFileById2**](ProjectsSmartV2Api.md#getFileById2) | **GET** /v2/projects/files/{fileId} | Returns details of a file. |
| [**getFileContentById**](ProjectsSmartV2Api.md#getFileContentById) | **GET** /v2/projects/files/{fileId}/download/{fileName} | Downloads a file content. |
| [**getFiles**](ProjectsSmartV2Api.md#getFiles) | **GET** /v2/projects/{projectId}/files | Returns list of files in a project. |
| [**getFinance2**](ProjectsSmartV2Api.md#getFinance2) | **GET** /v2/projects/{projectId}/finance | Returns finance information for a project. |
| [**getJobs**](ProjectsSmartV2Api.md#getJobs) | **GET** /v2/projects/{projectId}/jobs | Returns list of jobs in a project. |
| [**getProcessId**](ProjectsSmartV2Api.md#getProcessId) | **GET** /v2/projects/{projectId}/process | Returns process id. |
| [**updateClientDeadline**](ProjectsSmartV2Api.md#updateClientDeadline) | **PUT** /v2/projects/{projectId}/clientDeadline | Updates Client Deadline for a project. |
| [**updateClientNotes**](ProjectsSmartV2Api.md#updateClientNotes) | **PUT** /v2/projects/{projectId}/clientNotes | Updates Client Notes for a project. |
| [**updateClientReferenceNumber**](ProjectsSmartV2Api.md#updateClientReferenceNumber) | **PUT** /v2/projects/{projectId}/clientReferenceNumber | Updates Client Reference Number for a project. |
| [**updateContacts2**](ProjectsSmartV2Api.md#updateContacts2) | **PUT** /v2/projects/{projectId}/clientContacts | Updates Client Contacts for a project. |
| [**updateCustomField2**](ProjectsSmartV2Api.md#updateCustomField2) | **PUT** /v2/projects/{projectId}/customFields/{key} | Updates a custom field with a specified key in a project |
| [**updateInternalNotes**](ProjectsSmartV2Api.md#updateInternalNotes) | **PUT** /v2/projects/{projectId}/internalNotes | Updates Internal Notes for a project. |
| [**updateOrderedOn**](ProjectsSmartV2Api.md#updateOrderedOn) | **PUT** /v2/projects/{projectId}/orderDate | Updates Order Date for a project. |
| [**updatePayable2**](ProjectsSmartV2Api.md#updatePayable2) | **PUT** /v2/projects/{projectId}/finance/payables/{payableId} | Updates a payable. |
| [**updateReceivable2**](ProjectsSmartV2Api.md#updateReceivable2) | **PUT** /v2/projects/{projectId}/finance/receivables/{receivableId} | Updates a receivable. |
| [**updateSourceLanguage**](ProjectsSmartV2Api.md#updateSourceLanguage) | **PUT** /v2/projects/{projectId}/sourceLanguage | Updates source language for a project. |
| [**updateSpecialization**](ProjectsSmartV2Api.md#updateSpecialization) | **PUT** /v2/projects/{projectId}/specialization | Updates specialization for a project. |
| [**updateTargetLanguages**](ProjectsSmartV2Api.md#updateTargetLanguages) | **PUT** /v2/projects/{projectId}/targetLanguages | Updates target languages for a project. |
| [**updateVendorInstructions**](ProjectsSmartV2Api.md#updateVendorInstructions) | **PUT** /v2/projects/{projectId}/vendorInstructions | Updates instructions for all vendors performing the jobs in a project. |
| [**updateVolume**](ProjectsSmartV2Api.md#updateVolume) | **PUT** /v2/projects/{projectId}/volume | Updates volume for a project. |
| [**uploadFile2**](ProjectsSmartV2Api.md#uploadFile2) | **POST** /v2/projects/{projectId}/files/upload | Uploads file to the project as a file uploaded by PM. |


<a id="addExternalFileLinks"></a>
# **addExternalFileLinks**
> addExternalFileLinks(projectId, externalFileDto)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    ExternalFileDto externalFileDto = new ExternalFileDto(); // ExternalFileDto | Added file links to the project as added by PM.
    try {
      apiInstance.addExternalFileLinks(projectId, externalFileDto);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#addExternalFileLinks");
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
| **externalFileDto** | [**ExternalFileDto**](ExternalFileDto.md)| Added file links to the project as added by PM. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | default response |  -  |

<a id="addFileLinks1"></a>
# **addFileLinks1**
> FilesDto addFileLinks1(projectId, fileLinkCategorizationsDto)

Adds file links to the project as added by PM.

Adds file links to the project as added by PM. The following properties can be specified for each file link:&lt;ul&gt;&lt;li&gt;url (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    FileLinkCategorizationsDto fileLinkCategorizationsDto = new FileLinkCategorizationsDto(); // FileLinkCategorizationsDto | Added file links to the project as added by PM.
    try {
      FilesDto result = apiInstance.addFileLinks1(projectId, fileLinkCategorizationsDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#addFileLinks1");
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
| **fileLinkCategorizationsDto** | [**FileLinkCategorizationsDto**](FileLinkCategorizationsDto.md)| Added file links to the project as added by PM. | |

### Return type

[**FilesDto**](FilesDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="addFiles1"></a>
# **addFiles1**
> addFiles1(projectId, fileCategorizationsDto)

Adds files to the project as added by PM.

Adds files to the project as added by PM. The files have to be uploaded beforehand (see \&quot;POST /v2/projects/{projectId}/files/upload\&quot; operation). The following properties can be specified for each file:&lt;ul&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    FileCategorizationsDto fileCategorizationsDto = new FileCategorizationsDto(); // FileCategorizationsDto | Added files to the project as added by PM.
    try {
      apiInstance.addFiles1(projectId, fileCategorizationsDto);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#addFiles1");
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
| **fileCategorizationsDto** | [**FileCategorizationsDto**](FileCategorizationsDto.md)| Added files to the project as added by PM. | |

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

<a id="addJobToProcess"></a>
# **addJobToProcess**
> CATToolProjectDTO addJobToProcess(projectId)

Returns process id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | 
    try {
      CATToolProjectDTO result = apiInstance.addJobToProcess(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#addJobToProcess");
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
| **projectId** | **String**|  | |

### Return type

[**CATToolProjectDTO**](CATToolProjectDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="archive"></a>
# **archive**
> FilesArchiveDto archive(filesDto)

Prepares a ZIP archive that contains the specified files.

Prepares a ZIP archive that contains the specified files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    FilesDto filesDto = new FilesDto(); // FilesDto | Prepared ZIP archive that contains the specified files.
    try {
      FilesArchiveDto result = apiInstance.archive(filesDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#archive");
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
| **filesDto** | [**FilesDto**](FilesDto.md)| Prepared ZIP archive that contains the specified files. | |

### Return type

[**FilesArchiveDto**](FilesArchiveDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="changeStatus2"></a>
# **changeStatus2**
> changeStatus2(projectId, projectStatusDTO)

Changes project status if possible (400 Bad Request is returned otherwise).

Changes project status if possible (400 Bad Request is returned otherwise). The status has to be specified using one of the following keys: &lt;ul&gt;&lt;li&gt;CANCELLED – available when the job has one of the following statuses: OPEN, STARTED&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    ProjectStatusDTO projectStatusDTO = new ProjectStatusDTO(); // ProjectStatusDTO | Changed project status.
    try {
      apiInstance.changeStatus2(projectId, projectStatusDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#changeStatus2");
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
| **projectStatusDTO** | [**ProjectStatusDTO**](ProjectStatusDTO.md)| Changed project status. | |

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

<a id="create6"></a>
# **create6**
> ProjectDTOv2 create6(projectCreateDTO)

Creates a new Smart Project.

Creates a new Smart Project. If the specified service ID refers to Classic Project, 400 Bad Request is returned instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    ProjectCreateDTO projectCreateDTO = new ProjectCreateDTO(); // ProjectCreateDTO | 
    try {
      ProjectDTOv2 result = apiInstance.create6(projectCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#create6");
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
| **projectCreateDTO** | [**ProjectCreateDTO**](ProjectCreateDTO.md)|  | [optional] |

### Return type

[**ProjectDTOv2**](ProjectDTOv2.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |

<a id="createPayable2"></a>
# **createPayable2**
> PayableDTO createPayable2(projectId, payableCreateDTO)

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
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    PayableCreateDTO payableCreateDTO = new PayableCreateDTO(); // PayableCreateDTO | 
    try {
      PayableDTO result = apiInstance.createPayable2(projectId, payableCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#createPayable2");
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

<a id="createReceivable2"></a>
# **createReceivable2**
> ReceivableDTO createReceivable2(projectId, receivableCreateDTO)

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
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    ReceivableCreateDTO receivableCreateDTO = new ReceivableCreateDTO(); // ReceivableCreateDTO | 
    try {
      ReceivableDTO result = apiInstance.createReceivable2(projectId, receivableCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#createReceivable2");
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

<a id="deletePayable2"></a>
# **deletePayable2**
> deletePayable2(projectId, payableId)

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
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    Long payableId = 56L; // Long | payable's internal identifier
    try {
      apiInstance.deletePayable2(projectId, payableId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#deletePayable2");
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

<a id="deleteReceivable2"></a>
# **deleteReceivable2**
> deleteReceivable2(projectId, receivableId)

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
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    Long receivableId = 56L; // Long | receivable's internal identifier
    try {
      apiInstance.deleteReceivable2(projectId, receivableId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#deleteReceivable2");
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

<a id="getByExternalId1"></a>
# **getByExternalId1**
> ProjectDTOv2 getByExternalId1(externalProjectId)

Returns project details.

Returns project details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String externalProjectId = "externalProjectId_example"; // String | project's external identifier
    try {
      ProjectDTOv2 result = apiInstance.getByExternalId1(externalProjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getByExternalId1");
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
| **externalProjectId** | **String**| project&#39;s external identifier | |

### Return type

[**ProjectDTOv2**](ProjectDTOv2.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getById9"></a>
# **getById9**
> ProjectDTOv2 getById9(projectId)

Returns project details.

Returns project details. If the specified project ID refers to Classic Project, 400 Bad Request is returned instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      ProjectDTOv2 result = apiInstance.getById9(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getById9");
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

[**ProjectDTOv2**](ProjectDTOv2.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getCATToolProjectInfo"></a>
# **getCATToolProjectInfo**
> CATToolProjectDTO getCATToolProjectInfo(projectId)

Returns if cat tool project is created or queued.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | 
    try {
      CATToolProjectDTO result = apiInstance.getCATToolProjectInfo(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getCATToolProjectInfo");
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
| **projectId** | **String**|  | |

### Return type

[**CATToolProjectDTO**](CATToolProjectDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getContacts2"></a>
# **getContacts2**
> SmartContactsDTO getContacts2(projectId)

Returns Client Contacts information for a project.

Returns Client Contacts information for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      SmartContactsDTO result = apiInstance.getContacts2(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getContacts2");
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

[**SmartContactsDTO**](SmartContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getCustomFields8"></a>
# **getCustomFields8**
> List&lt;CustomFieldDTO&gt; getCustomFields8(projectId)

Returns a list of custom field keys and values for a project.

Returns a list of custom field keys and values for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      List<CustomFieldDTO> result = apiInstance.getCustomFields8(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getCustomFields8");
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
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getDeliverableFiles"></a>
# **getDeliverableFiles**
> List&lt;ProjectFileDto&gt; getDeliverableFiles(projectId)

Returns list of files in a project, that are ready to be delivered to client.

Returns list of files in a project, that are ready to be delivered to client. A file is considered deliverable to client when all of the following criteria are met:&lt;ul&gt;&lt;li&gt;the file was added to a job in the last step in the process&lt;/li&gt;&lt;li&gt;the file is marked as verified (if it was added in a verification step and the file is verifiable, according to its category)&lt;/li&gt;&lt;li&gt;the job is finished (has Ready status)&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      List<ProjectFileDto> result = apiInstance.getDeliverableFiles(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getDeliverableFiles");
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

[**List&lt;ProjectFileDto&gt;**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getFileById2"></a>
# **getFileById2**
> ProjectFileDto getFileById2(fileId)

Returns details of a file.

Returns details of a file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String fileId = "fileId_example"; // String | file's internal identifier
    try {
      ProjectFileDto result = apiInstance.getFileById2(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getFileById2");
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

[**ProjectFileDto**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getFileContentById"></a>
# **getFileContentById**
> getFileContentById(fileId, fileName)

Downloads a file content.

Downloads a file content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String fileId = "fileId_example"; // String | file's internal identifier
    String fileName = "fileName_example"; // String | file's name
    try {
      apiInstance.getFileContentById(fileId, fileName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getFileContentById");
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
| **fileName** | **String**| file&#39;s name | |

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
| **0** | Success |  -  |

<a id="getFiles"></a>
# **getFiles**
> List&lt;ProjectFileDto&gt; getFiles(projectId)

Returns list of files in a project.

Returns list of files in a project. Only files added to the project (i.e. files that have assigned category and languages) are listed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      List<ProjectFileDto> result = apiInstance.getFiles(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getFiles");
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

[**List&lt;ProjectFileDto&gt;**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getFinance2"></a>
# **getFinance2**
> FinanceDTO getFinance2(projectId)

Returns finance information for a project.

Returns finance information for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      FinanceDTO result = apiInstance.getFinance2(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getFinance2");
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
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getJobs"></a>
# **getJobs**
> List&lt;JobDto&gt; getJobs(projectId)

Returns list of jobs in a project.

Returns list of jobs in a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    try {
      List<JobDto> result = apiInstance.getJobs(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getJobs");
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

[**List&lt;JobDto&gt;**](JobDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getProcessId"></a>
# **getProcessId**
> CATToolProjectDTO getProcessId(projectId)

Returns process id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | 
    try {
      CATToolProjectDTO result = apiInstance.getProcessId(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#getProcessId");
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
| **projectId** | **String**|  | |

### Return type

[**CATToolProjectDTO**](CATToolProjectDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateClientDeadline"></a>
# **updateClientDeadline**
> updateClientDeadline(projectId, timeDTO)

Updates Client Deadline for a project.

Updates Client Deadline for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    TimeDTO timeDTO = new TimeDTO(); // TimeDTO | Updated Client Deadline for a project.
    try {
      apiInstance.updateClientDeadline(projectId, timeDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateClientDeadline");
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
| **timeDTO** | [**TimeDTO**](TimeDTO.md)| Updated Client Deadline for a project. | |

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

<a id="updateClientNotes"></a>
# **updateClientNotes**
> updateClientNotes(projectId, stringDTO)

Updates Client Notes for a project.

Updates Client Notes for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | Updated Client Notes for a project.
    try {
      apiInstance.updateClientNotes(projectId, stringDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateClientNotes");
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
| **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Client Notes for a project. | |

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

<a id="updateClientReferenceNumber"></a>
# **updateClientReferenceNumber**
> updateClientReferenceNumber(projectId, stringDTO)

Updates Client Reference Number for a project.

Updates Client Reference Number for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | Updated Client Reference Number for a project.
    try {
      apiInstance.updateClientReferenceNumber(projectId, stringDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateClientReferenceNumber");
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
| **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Client Reference Number for a project. | |

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

<a id="updateContacts2"></a>
# **updateContacts2**
> SmartContactsDTO updateContacts2(projectId, smartContactsDTO)

Updates Client Contacts for a project.

Updates Client Contacts for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    SmartContactsDTO smartContactsDTO = new SmartContactsDTO(); // SmartContactsDTO | Updated Client Contacts for a project.
    try {
      SmartContactsDTO result = apiInstance.updateContacts2(projectId, smartContactsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateContacts2");
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
| **smartContactsDTO** | [**SmartContactsDTO**](SmartContactsDTO.md)| Updated Client Contacts for a project. | |

### Return type

[**SmartContactsDTO**](SmartContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateCustomField2"></a>
# **updateCustomField2**
> updateCustomField2(projectId, key, smartCustomFieldDTO)

Updates a custom field with a specified key in a project

Updates a custom field with a specified key in a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    String key = "key_example"; // String | custom field's key
    SmartCustomFieldDTO smartCustomFieldDTO = new SmartCustomFieldDTO(); // SmartCustomFieldDTO | Updated custom field with a specified key in a project.
    try {
      apiInstance.updateCustomField2(projectId, key, smartCustomFieldDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateCustomField2");
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
| **key** | **String**| custom field&#39;s key | |
| **smartCustomFieldDTO** | [**SmartCustomFieldDTO**](SmartCustomFieldDTO.md)| Updated custom field with a specified key in a project. | |

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

<a id="updateInternalNotes"></a>
# **updateInternalNotes**
> updateInternalNotes(projectId, stringDTO)

Updates Internal Notes for a project.

Updates Internal Notes for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | Updated Internal Notes for a project.
    try {
      apiInstance.updateInternalNotes(projectId, stringDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateInternalNotes");
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
| **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Internal Notes for a project. | |

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

<a id="updateOrderedOn"></a>
# **updateOrderedOn**
> updateOrderedOn(projectId, timeDTO)

Updates Order Date for a project.

Updates Order Date for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    TimeDTO timeDTO = new TimeDTO(); // TimeDTO | Updated Order Date for a project.
    try {
      apiInstance.updateOrderedOn(projectId, timeDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateOrderedOn");
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
| **timeDTO** | [**TimeDTO**](TimeDTO.md)| Updated Order Date for a project. | |

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

<a id="updatePayable2"></a>
# **updatePayable2**
> PayableDTO updatePayable2(projectId, payableId, payableDTO)

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
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    Long payableId = 56L; // Long | payable's internal identifier
    PayableDTO payableDTO = new PayableDTO(); // PayableDTO | 
    try {
      PayableDTO result = apiInstance.updatePayable2(projectId, payableId, payableDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updatePayable2");
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

<a id="updateReceivable2"></a>
# **updateReceivable2**
> ReceivableDTO updateReceivable2(projectId, receivableId, receivableDTO)

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
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    Long receivableId = 56L; // Long | receivable's internal identifier
    ReceivableDTO receivableDTO = new ReceivableDTO(); // ReceivableDTO | 
    try {
      ReceivableDTO result = apiInstance.updateReceivable2(projectId, receivableId, receivableDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateReceivable2");
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

<a id="updateSourceLanguage"></a>
# **updateSourceLanguage**
> updateSourceLanguage(projectId, sourceLanguageDTO)

Updates source language for a project.

Updates source language for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    SourceLanguageDTO sourceLanguageDTO = new SourceLanguageDTO(); // SourceLanguageDTO | Updated source language for a project.
    try {
      apiInstance.updateSourceLanguage(projectId, sourceLanguageDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateSourceLanguage");
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
| **sourceLanguageDTO** | [**SourceLanguageDTO**](SourceLanguageDTO.md)| Updated source language for a project. | |

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

<a id="updateSpecialization"></a>
# **updateSpecialization**
> updateSpecialization(projectId, specializationDTO)

Updates specialization for a project.

Updates specialization for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    SpecializationDTO specializationDTO = new SpecializationDTO(); // SpecializationDTO | Updated specialization for a project.
    try {
      apiInstance.updateSpecialization(projectId, specializationDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateSpecialization");
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
| **specializationDTO** | [**SpecializationDTO**](SpecializationDTO.md)| Updated specialization for a project. | |

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

<a id="updateTargetLanguages"></a>
# **updateTargetLanguages**
> updateTargetLanguages(projectId, targetLanguagesDTO)

Updates target languages for a project.

Updates target languages for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    TargetLanguagesDTO targetLanguagesDTO = new TargetLanguagesDTO(); // TargetLanguagesDTO | Updated target languages for a project.
    try {
      apiInstance.updateTargetLanguages(projectId, targetLanguagesDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateTargetLanguages");
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
| **targetLanguagesDTO** | [**TargetLanguagesDTO**](TargetLanguagesDTO.md)| Updated target languages for a project. | |

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

<a id="updateVendorInstructions"></a>
# **updateVendorInstructions**
> updateVendorInstructions(projectId, stringDTO)

Updates instructions for all vendors performing the jobs in a project.

Updates instructions for all vendors performing the jobs in a project. See also \&quot;PUT /jobs/{jobId}/instructions\&quot; for updating instructions for a specific job in a project or quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | Updated instructions for all vendors performing the jobs in a project.
    try {
      apiInstance.updateVendorInstructions(projectId, stringDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateVendorInstructions");
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
| **stringDTO** | [**StringDTO**](StringDTO.md)| Updated instructions for all vendors performing the jobs in a project. | |

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

<a id="updateVolume"></a>
# **updateVolume**
> updateVolume(projectId, bigDecimalDTO)

Updates volume for a project.

Updates volume for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    BigDecimalDTO bigDecimalDTO = new BigDecimalDTO(); // BigDecimalDTO | Updated volume for a project.
    try {
      apiInstance.updateVolume(projectId, bigDecimalDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#updateVolume");
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
| **bigDecimalDTO** | [**BigDecimalDTO**](BigDecimalDTO.md)| Updated volume for a project. | |

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

<a id="uploadFile2"></a>
# **uploadFile2**
> FileDto uploadFile2(projectId, _file)

Uploads file to the project as a file uploaded by PM.

Uploads file to the project as a file uploaded by PM. Only one file can be uploaded at once. When the upload is finished the file has to be added by specifying its category and languages (see \&quot;PUT /v2/projects/{projectId}/files/add\&quot; operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    ProjectsSmartV2Api apiInstance = new ProjectsSmartV2Api(defaultClient);
    String projectId = "projectId_example"; // String | project's internal identifier
    File _file = new File("/path/to/file"); // File | 
    try {
      FileDto result = apiInstance.uploadFile2(projectId, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsSmartV2Api#uploadFile2");
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
| **_file** | **File**|  | [optional] |

### Return type

[**FileDto**](FileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |


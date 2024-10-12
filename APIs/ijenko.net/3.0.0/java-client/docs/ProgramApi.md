# ProgramApi

All URIs are relative to *https://ioe2api.ijenko.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**placeNewProgram**](ProgramApi.md#placeNewProgram) | **POST** /places/{placeId}/programs | Create a Program |
| [**placePrograms**](ProgramApi.md#placePrograms) | **GET** /places/{placeId}/programs | List Programs |
| [**programDelete**](ProgramApi.md#programDelete) | **DELETE** /programs/{programId} | Delete a Program |
| [**programGetMetadata**](ProgramApi.md#programGetMetadata) | **GET** /programs/{programId}/metadata | List metadata |
| [**programLog**](ProgramApi.md#programLog) | **GET** /programs/{programId}/log | History of executions of a Program |
| [**programPatch**](ProgramApi.md#programPatch) | **PATCH** /programs/{programId} | Modify a Program |
| [**programPatchMetadata**](ProgramApi.md#programPatchMetadata) | **PATCH** /programs/{programId}/metadata | Modify metadata of a Program |
| [**programRun**](ProgramApi.md#programRun) | **POST** /programs/{programId}/run | Run the Program |
| [**programsGet**](ProgramApi.md#programsGet) | **GET** /programs/{programId} | Information about a Program |


<a id="placeNewProgram"></a>
# **placeNewProgram**
> ProgramCreated placeNewProgram(placeId, programInfo)

Create a Program

Create a new *Program*.  **Note**: requires full access to the *Account*. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ProgramApi apiInstance = new ProgramApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    ProgramNew programInfo = new ProgramNew(); // ProgramNew | 
    try {
      ProgramCreated result = apiInstance.placeNewProgram(placeId, programInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramApi#placeNewProgram");
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
| **placeId** | **String**| Unique identifier of a *Place*. | |
| **programInfo** | [**ProgramNew**](ProgramNew.md)|  | |

### Return type

[**ProgramCreated**](ProgramCreated.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | *Program* successfully created. |  * Location - Path of the Program created (&#x60;/programs/{id}&#x60;) <br>  |
| **403** | *Place* doesn&#39;t exist or the requester doesn&#39;t have access.  |  -  |
| **0** | Other error. |  -  |

<a id="placePrograms"></a>
# **placePrograms**
> Set&lt;ProgramItem&gt; placePrograms(placeId, embedMetadata)

List Programs

Get the list of *Programs* available in this *Place*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ProgramApi apiInstance = new ProgramApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    List<String> embedMetadata = Arrays.asList(); // List<String> | Request to include the given keys of metadata in the response. If a key doesn't exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
    try {
      Set<ProgramItem> result = apiInstance.placePrograms(placeId, embedMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramApi#placePrograms");
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
| **placeId** | **String**| Unique identifier of a *Place*. | |
| **embedMetadata** | [**List&lt;String&gt;**](String.md)| Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources.  | [optional] |

### Return type

[**Set&lt;ProgramItem&gt;**](ProgramItem.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="programDelete"></a>
# **programDelete**
> programDelete(programId)

Delete a Program

Delete a *Program*.  **Note**: requires full access to the *Account*. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ProgramApi apiInstance = new ProgramApi(defaultClient);
    String programId = "programId_example"; // String | Unique identifier of a *Program*.
    try {
      apiInstance.programDelete(programId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramApi#programDelete");
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
| **programId** | **String**| Unique identifier of a *Program*. | |

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Resource successfully deleted. |  -  |
| **403** | *Program* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="programGetMetadata"></a>
# **programGetMetadata**
> Map&lt;String, Object&gt; programGetMetadata(programId)

List metadata

Get the metadata of the *Program*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ProgramApi apiInstance = new ProgramApi(defaultClient);
    String programId = "programId_example"; // String | Unique identifier of a *Program*.
    try {
      Map<String, Object> result = apiInstance.programGetMetadata(programId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramApi#programGetMetadata");
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
| **programId** | **String**| Unique identifier of a *Program*. | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="programLog"></a>
# **programLog**
> Set&lt;ProgramLog&gt; programLog(programId, from, to)

History of executions of a Program

Get the execution history list of this *Program*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ProgramApi apiInstance = new ProgramApi(defaultClient);
    String programId = "programId_example"; // String | Unique identifier of a *Program*.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Beginning of the time interval.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | End of the interval. Default: now. 
    try {
      Set<ProgramLog> result = apiInstance.programLog(programId, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramApi#programLog");
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
| **programId** | **String**| Unique identifier of a *Program*. | |
| **from** | **OffsetDateTime**| Beginning of the time interval. | |
| **to** | **OffsetDateTime**| End of the interval. Default: now.  | [optional] |

### Return type

[**Set&lt;ProgramLog&gt;**](ProgramLog.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **403** | *Program* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="programPatch"></a>
# **programPatch**
> programPatch(programId, programPatch)

Modify a Program

Modify a *Program*: - name - status (enabled/disabled) - code  **Note**: requires full access to the *Account*. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ProgramApi apiInstance = new ProgramApi(defaultClient);
    String programId = "programId_example"; // String | Unique identifier of a *Program*.
    ProgramPatch programPatch = new ProgramPatch(); // ProgramPatch | 
    try {
      apiInstance.programPatch(programId, programPatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramApi#programPatch");
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
| **programId** | **String**| Unique identifier of a *Program*. | |
| **programPatch** | [**ProgramPatch**](ProgramPatch.md)|  | |

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Modification successful. |  -  |
| **304** | Successful, but nothing changed. |  -  |
| **403** | *Program* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="programPatchMetadata"></a>
# **programPatchMetadata**
> Map&lt;String, Object&gt; programPatchMetadata(programId, metadataPatch)

Modify metadata of a Program

Modify the metadata of a *Program*. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ProgramApi apiInstance = new ProgramApi(defaultClient);
    String programId = "programId_example"; // String | Unique identifier of a *Program*.
    MetadataPatch metadataPatch = new MetadataPatch(); // MetadataPatch | Modifications to apply to the metadata of the resource. 
    try {
      Map<String, Object> result = apiInstance.programPatchMetadata(programId, metadataPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramApi#programPatchMetadata");
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
| **programId** | **String**| Unique identifier of a *Program*. | |
| **metadataPatch** | [**MetadataPatch**](MetadataPatch.md)| Modifications to apply to the metadata of the resource.  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. The new metadata is returned. |  -  |
| **304** | Successful, but nothing changed. |  -  |
| **403** | *Program* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="programRun"></a>
# **programRun**
> programRun(programId)

Run the Program

Launch the *Program*. The result will be available later in the run history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ProgramApi apiInstance = new ProgramApi(defaultClient);
    String programId = "programId_example"; // String | Unique identifier of a *Program*.
    try {
      apiInstance.programRun(programId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramApi#programRun");
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
| **programId** | **String**| Unique identifier of a *Program*. | |

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | *Program* successfully launched. |  -  |
| **403** | *Program* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="programsGet"></a>
# **programsGet**
> Program programsGet(programId)

Information about a Program

Get information about a *Program*. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ProgramApi apiInstance = new ProgramApi(defaultClient);
    String programId = "programId_example"; // String | Unique identifier of a *Program*.
    try {
      Program result = apiInstance.programsGet(programId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgramApi#programsGet");
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
| **programId** | **String**| Unique identifier of a *Program*. | |

### Return type

[**Program**](Program.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **403** | *Program* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |


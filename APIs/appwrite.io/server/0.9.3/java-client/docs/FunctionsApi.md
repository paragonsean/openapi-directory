# FunctionsApi

All URIs are relative to *https://appwrite.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**functionsCreate**](FunctionsApi.md#functionsCreate) | **POST** /functions | Create Function |
| [**functionsCreateExecution**](FunctionsApi.md#functionsCreateExecution) | **POST** /functions/{functionId}/executions | Create Execution |
| [**functionsCreateTag**](FunctionsApi.md#functionsCreateTag) | **POST** /functions/{functionId}/tags | Create Tag |
| [**functionsDelete**](FunctionsApi.md#functionsDelete) | **DELETE** /functions/{functionId} | Delete Function |
| [**functionsDeleteTag**](FunctionsApi.md#functionsDeleteTag) | **DELETE** /functions/{functionId}/tags/{tagId} | Delete Tag |
| [**functionsGet**](FunctionsApi.md#functionsGet) | **GET** /functions/{functionId} | Get Function |
| [**functionsGetExecution**](FunctionsApi.md#functionsGetExecution) | **GET** /functions/{functionId}/executions/{executionId} | Get Execution |
| [**functionsGetTag**](FunctionsApi.md#functionsGetTag) | **GET** /functions/{functionId}/tags/{tagId} | Get Tag |
| [**functionsList**](FunctionsApi.md#functionsList) | **GET** /functions | List Functions |
| [**functionsListExecutions**](FunctionsApi.md#functionsListExecutions) | **GET** /functions/{functionId}/executions | List Executions |
| [**functionsListTags**](FunctionsApi.md#functionsListTags) | **GET** /functions/{functionId}/tags | List Tags |
| [**functionsUpdate**](FunctionsApi.md#functionsUpdate) | **PUT** /functions/{functionId} | Update Function |
| [**functionsUpdateTag**](FunctionsApi.md#functionsUpdateTag) | **PATCH** /functions/{functionId}/tag | Update Function Tag |


<a id="functionsCreate"></a>
# **functionsCreate**
> Function functionsCreate(functionsCreateRequest)

Create Function

Create a new function. You can pass a list of [permissions](/docs/permissions) to allow different project users or team with access to execute the function using the client API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    FunctionsCreateRequest functionsCreateRequest = new FunctionsCreateRequest(); // FunctionsCreateRequest | 
    try {
      Function result = apiInstance.functionsCreate(functionsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsCreate");
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
| **functionsCreateRequest** | [**FunctionsCreateRequest**](FunctionsCreateRequest.md)|  | [optional] |

### Return type

[**Function**](Function.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Function |  -  |

<a id="functionsCreateExecution"></a>
# **functionsCreateExecution**
> Execution functionsCreateExecution(functionId, functionsCreateExecutionRequest)

Create Execution

Trigger a function execution. The returned object will return you the current execution status. You can ping the &#x60;Get Execution&#x60; endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    FunctionsCreateExecutionRequest functionsCreateExecutionRequest = new FunctionsCreateExecutionRequest(); // FunctionsCreateExecutionRequest | 
    try {
      Execution result = apiInstance.functionsCreateExecution(functionId, functionsCreateExecutionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsCreateExecution");
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
| **functionId** | **String**| Function unique ID. | |
| **functionsCreateExecutionRequest** | [**FunctionsCreateExecutionRequest**](FunctionsCreateExecutionRequest.md)|  | [optional] |

### Return type

[**Execution**](Execution.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Execution |  -  |

<a id="functionsCreateTag"></a>
# **functionsCreateTag**
> Tag functionsCreateTag(functionId, code, command)

Create Tag

Create a new function code tag. Use this endpoint to upload a new version of your code function. To execute your newly uploaded code, you&#39;ll need to update the function&#39;s tag to use your new tag UID.  This endpoint accepts a tar.gz file compressed with your code. Make sure to include any dependencies your code has within the compressed file. You can learn more about code packaging in the [Appwrite Cloud Functions tutorial](/docs/functions).  Use the \&quot;command\&quot; param to set the entry point used to execute your code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    String code = "code_example"; // String | Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.
    String command = "command_example"; // String | Code execution command.
    try {
      Tag result = apiInstance.functionsCreateTag(functionId, code, command);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsCreateTag");
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
| **functionId** | **String**| Function unique ID. | |
| **code** | **String**| Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory. | |
| **command** | **String**| Code execution command. | |

### Return type

[**Tag**](Tag.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Tag |  -  |

<a id="functionsDelete"></a>
# **functionsDelete**
> functionsDelete(functionId)

Delete Function

Delete a function by its unique ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    try {
      apiInstance.functionsDelete(functionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsDelete");
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
| **functionId** | **String**| Function unique ID. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="functionsDeleteTag"></a>
# **functionsDeleteTag**
> functionsDeleteTag(functionId, tagId)

Delete Tag

Delete a code tag by its unique ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    String tagId = "tagId_example"; // String | Tag unique ID.
    try {
      apiInstance.functionsDeleteTag(functionId, tagId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsDeleteTag");
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
| **functionId** | **String**| Function unique ID. | |
| **tagId** | **String**| Tag unique ID. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="functionsGet"></a>
# **functionsGet**
> Function functionsGet(functionId)

Get Function

Get a function by its unique ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    try {
      Function result = apiInstance.functionsGet(functionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsGet");
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
| **functionId** | **String**| Function unique ID. | |

### Return type

[**Function**](Function.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Function |  -  |

<a id="functionsGetExecution"></a>
# **functionsGetExecution**
> Execution functionsGetExecution(functionId, executionId)

Get Execution

Get a function execution log by its unique ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    String executionId = "executionId_example"; // String | Execution unique ID.
    try {
      Execution result = apiInstance.functionsGetExecution(functionId, executionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsGetExecution");
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
| **functionId** | **String**| Function unique ID. | |
| **executionId** | **String**| Execution unique ID. | |

### Return type

[**Execution**](Execution.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Execution |  -  |

<a id="functionsGetTag"></a>
# **functionsGetTag**
> Tag functionsGetTag(functionId, tagId)

Get Tag

Get a code tag by its unique ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    String tagId = "tagId_example"; // String | Tag unique ID.
    try {
      Tag result = apiInstance.functionsGetTag(functionId, tagId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsGetTag");
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
| **functionId** | **String**| Function unique ID. | |
| **tagId** | **String**| Tag unique ID. | |

### Return type

[**Tag**](Tag.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tag |  -  |

<a id="functionsList"></a>
# **functionsList**
> FunctionList functionsList(search, limit, offset, orderType)

List Functions

Get a list of all the project&#39;s functions. You can use the query params to filter your results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String search = ""; // String | Search term to filter your list results. Max length: 256 chars.
    Integer limit = 25; // Integer | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    Integer offset = 0; // Integer | Results offset. The default value is 0. Use this param to manage pagination.
    String orderType = "ASC"; // String | Order result by ASC or DESC order.
    try {
      FunctionList result = apiInstance.functionsList(search, limit, offset, orderType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsList");
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
| **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to ] |
| **limit** | **Integer**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25] |
| **offset** | **Integer**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0] |
| **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to ASC] |

### Return type

[**FunctionList**](FunctionList.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Functions List |  -  |

<a id="functionsListExecutions"></a>
# **functionsListExecutions**
> ExecutionList functionsListExecutions(functionId, search, limit, offset, orderType)

List Executions

Get a list of all the current user function execution logs. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s executions. [Learn more about different API modes](/docs/admin).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    String search = ""; // String | Search term to filter your list results. Max length: 256 chars.
    Integer limit = 25; // Integer | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    Integer offset = 0; // Integer | Results offset. The default value is 0. Use this param to manage pagination.
    String orderType = "ASC"; // String | Order result by ASC or DESC order.
    try {
      ExecutionList result = apiInstance.functionsListExecutions(functionId, search, limit, offset, orderType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsListExecutions");
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
| **functionId** | **String**| Function unique ID. | |
| **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to ] |
| **limit** | **Integer**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25] |
| **offset** | **Integer**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0] |
| **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to ASC] |

### Return type

[**ExecutionList**](ExecutionList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Executions List |  -  |

<a id="functionsListTags"></a>
# **functionsListTags**
> TagList functionsListTags(functionId, search, limit, offset, orderType)

List Tags

Get a list of all the project&#39;s code tags. You can use the query params to filter your results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    String search = ""; // String | Search term to filter your list results. Max length: 256 chars.
    Integer limit = 25; // Integer | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    Integer offset = 0; // Integer | Results offset. The default value is 0. Use this param to manage pagination.
    String orderType = "ASC"; // String | Order result by ASC or DESC order.
    try {
      TagList result = apiInstance.functionsListTags(functionId, search, limit, offset, orderType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsListTags");
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
| **functionId** | **String**| Function unique ID. | |
| **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to ] |
| **limit** | **Integer**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25] |
| **offset** | **Integer**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0] |
| **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to ASC] |

### Return type

[**TagList**](TagList.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tags List |  -  |

<a id="functionsUpdate"></a>
# **functionsUpdate**
> Function functionsUpdate(functionId, functionsUpdateRequest)

Update Function

Update function by its unique ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    FunctionsUpdateRequest functionsUpdateRequest = new FunctionsUpdateRequest(); // FunctionsUpdateRequest | 
    try {
      Function result = apiInstance.functionsUpdate(functionId, functionsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsUpdate");
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
| **functionId** | **String**| Function unique ID. | |
| **functionsUpdateRequest** | [**FunctionsUpdateRequest**](FunctionsUpdateRequest.md)|  | [optional] |

### Return type

[**Function**](Function.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Function |  -  |

<a id="functionsUpdateTag"></a>
# **functionsUpdateTag**
> Function functionsUpdateTag(functionId, functionsUpdateTagRequest)

Update Function Tag

Update the function code tag ID using the unique function ID. Use this endpoint to switch the code tag that should be executed by the execution endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String functionId = "functionId_example"; // String | Function unique ID.
    FunctionsUpdateTagRequest functionsUpdateTagRequest = new FunctionsUpdateTagRequest(); // FunctionsUpdateTagRequest | 
    try {
      Function result = apiInstance.functionsUpdateTag(functionId, functionsUpdateTagRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#functionsUpdateTag");
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
| **functionId** | **String**| Function unique ID. | |
| **functionsUpdateTagRequest** | [**FunctionsUpdateTagRequest**](FunctionsUpdateTagRequest.md)|  | [optional] |

### Return type

[**Function**](Function.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Function |  -  |


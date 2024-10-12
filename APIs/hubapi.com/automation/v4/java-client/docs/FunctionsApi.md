# FunctionsApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType**](FunctionsApi.md#deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType) | **DELETE** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType} | Delete a function for a definition |
| [**deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive**](FunctionsApi.md#deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive) | **DELETE** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId} | Archive a function for a definition |
| [**getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById**](FunctionsApi.md#getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById) | **GET** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId} | Get a function for a given definition |
| [**getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType**](FunctionsApi.md#getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType) | **GET** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType} | Get all functions by a type for a given definition |
| [**getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage**](FunctionsApi.md#getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage) | **GET** /automation/v4/actions/{appId}/{definitionId}/functions | Get all functions for a given definition |
| [**putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType**](FunctionsApi.md#putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType) | **PUT** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType} | Insert a function for a definition |
| [**putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace**](FunctionsApi.md#putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace) | **PUT** /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId} | Insert a function for a definition |


<a id="deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType"></a>
# **deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType**
> deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType(definitionId, functionType, appId)

Delete a function for a definition

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    String functionType = "PRE_ACTION_EXECUTION"; // String | 
    Integer appId = 56; // Integer | 
    try {
      apiInstance.deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType(definitionId, functionType, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeArchiveByFunctionType");
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
| **definitionId** | **String**|  | |
| **functionType** | **String**|  | [enum: PRE_ACTION_EXECUTION, PRE_FETCH_OPTIONS, POST_FETCH_OPTIONS, POST_ACTION_EXECUTION] |
| **appId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | An error occurred. |  -  |

<a id="deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive"></a>
# **deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive**
> deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive(definitionId, functionType, functionId, appId)

Archive a function for a definition

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    String functionType = "PRE_ACTION_EXECUTION"; // String | 
    String functionId = "functionId_example"; // String | 
    Integer appId = 56; // Integer | 
    try {
      apiInstance.deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive(definitionId, functionType, functionId, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#deleteAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdArchive");
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
| **definitionId** | **String**|  | |
| **functionType** | **String**|  | [enum: PRE_ACTION_EXECUTION, PRE_FETCH_OPTIONS, POST_FETCH_OPTIONS, POST_ACTION_EXECUTION] |
| **functionId** | **String**|  | |
| **appId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | An error occurred. |  -  |

<a id="getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById"></a>
# **getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById**
> PublicActionFunction getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById(definitionId, functionType, functionId, appId)

Get a function for a given definition

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    String functionType = "PRE_ACTION_EXECUTION"; // String | 
    String functionId = "functionId_example"; // String | 
    Integer appId = 56; // Integer | 
    try {
      PublicActionFunction result = apiInstance.getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById(definitionId, functionType, functionId, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdGetById");
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
| **definitionId** | **String**|  | |
| **functionType** | **String**|  | [enum: PRE_ACTION_EXECUTION, PRE_FETCH_OPTIONS, POST_FETCH_OPTIONS, POST_ACTION_EXECUTION] |
| **functionId** | **String**|  | |
| **appId** | **Integer**|  | |

### Return type

[**PublicActionFunction**](PublicActionFunction.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType"></a>
# **getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType**
> PublicActionFunction getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType(definitionId, functionType, appId)

Get all functions by a type for a given definition

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    String functionType = "PRE_ACTION_EXECUTION"; // String | 
    Integer appId = 56; // Integer | 
    try {
      PublicActionFunction result = apiInstance.getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType(definitionId, functionType, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#getAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeGetByFunctionType");
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
| **definitionId** | **String**|  | |
| **functionType** | **String**|  | [enum: PRE_ACTION_EXECUTION, PRE_FETCH_OPTIONS, POST_FETCH_OPTIONS, POST_ACTION_EXECUTION] |
| **appId** | **Integer**|  | |

### Return type

[**PublicActionFunction**](PublicActionFunction.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage"></a>
# **getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage**
> CollectionResponsePublicActionFunctionIdentifierNoPaging getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage(definitionId, appId)

Get all functions for a given definition

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    Integer appId = 56; // Integer | 
    try {
      CollectionResponsePublicActionFunctionIdentifierNoPaging result = apiInstance.getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage(definitionId, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#getAutomationV4ActionsAppIdDefinitionIdFunctionsGetPage");
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
| **definitionId** | **String**|  | |
| **appId** | **Integer**|  | |

### Return type

[**CollectionResponsePublicActionFunctionIdentifierNoPaging**](CollectionResponsePublicActionFunctionIdentifierNoPaging.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType"></a>
# **putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType**
> PublicActionFunctionIdentifier putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType(definitionId, functionType, appId, body)

Insert a function for a definition

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    String functionType = "PRE_ACTION_EXECUTION"; // String | 
    Integer appId = 56; // Integer | 
    String body = "body_example"; // String | 
    try {
      PublicActionFunctionIdentifier result = apiInstance.putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType(definitionId, functionType, appId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeCreateOrReplaceByFunctionType");
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
| **definitionId** | **String**|  | |
| **functionType** | **String**|  | [enum: PRE_ACTION_EXECUTION, PRE_FETCH_OPTIONS, POST_FETCH_OPTIONS, POST_ACTION_EXECUTION] |
| **appId** | **Integer**|  | |
| **body** | **String**|  | |

### Return type

[**PublicActionFunctionIdentifier**](PublicActionFunctionIdentifier.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace"></a>
# **putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace**
> PublicActionFunctionIdentifier putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace(definitionId, functionType, functionId, appId, body)

Insert a function for a definition

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    FunctionsApi apiInstance = new FunctionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    String functionType = "PRE_ACTION_EXECUTION"; // String | 
    String functionId = "functionId_example"; // String | 
    Integer appId = 56; // Integer | 
    String body = "body_example"; // String | 
    try {
      PublicActionFunctionIdentifier result = apiInstance.putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace(definitionId, functionType, functionId, appId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionsApi#putAutomationV4ActionsAppIdDefinitionIdFunctionsFunctionTypeFunctionIdCreateOrReplace");
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
| **definitionId** | **String**|  | |
| **functionType** | **String**|  | [enum: PRE_ACTION_EXECUTION, PRE_FETCH_OPTIONS, POST_FETCH_OPTIONS, POST_ACTION_EXECUTION] |
| **functionId** | **String**|  | |
| **appId** | **Integer**|  | |
| **body** | **String**|  | |

### Return type

[**PublicActionFunctionIdentifier**](PublicActionFunctionIdentifier.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |


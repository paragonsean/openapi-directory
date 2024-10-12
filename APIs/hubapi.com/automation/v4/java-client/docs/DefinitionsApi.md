# DefinitionsApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAutomationV4ActionsAppIdDefinitionIdArchive**](DefinitionsApi.md#deleteAutomationV4ActionsAppIdDefinitionIdArchive) | **DELETE** /automation/v4/actions/{appId}/{definitionId} | Archive an extension definition |
| [**getAutomationV4ActionsAppIdDefinitionIdGetById**](DefinitionsApi.md#getAutomationV4ActionsAppIdDefinitionIdGetById) | **GET** /automation/v4/actions/{appId}/{definitionId} | Get extension definition by Id |
| [**getAutomationV4ActionsAppIdGetPage**](DefinitionsApi.md#getAutomationV4ActionsAppIdGetPage) | **GET** /automation/v4/actions/{appId} | Get paged extension definitions |
| [**patchAutomationV4ActionsAppIdDefinitionIdUpdate**](DefinitionsApi.md#patchAutomationV4ActionsAppIdDefinitionIdUpdate) | **PATCH** /automation/v4/actions/{appId}/{definitionId} | Patch an existing extension definition |
| [**postAutomationV4ActionsAppIdCreate**](DefinitionsApi.md#postAutomationV4ActionsAppIdCreate) | **POST** /automation/v4/actions/{appId} | Create a new extension definition |


<a id="deleteAutomationV4ActionsAppIdDefinitionIdArchive"></a>
# **deleteAutomationV4ActionsAppIdDefinitionIdArchive**
> deleteAutomationV4ActionsAppIdDefinitionIdArchive(definitionId, appId)

Archive an extension definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    DefinitionsApi apiInstance = new DefinitionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    Integer appId = 56; // Integer | 
    try {
      apiInstance.deleteAutomationV4ActionsAppIdDefinitionIdArchive(definitionId, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinitionsApi#deleteAutomationV4ActionsAppIdDefinitionIdArchive");
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

<a id="getAutomationV4ActionsAppIdDefinitionIdGetById"></a>
# **getAutomationV4ActionsAppIdDefinitionIdGetById**
> PublicActionDefinition getAutomationV4ActionsAppIdDefinitionIdGetById(definitionId, appId, archived)

Get extension definition by Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    DefinitionsApi apiInstance = new DefinitionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    Integer appId = 56; // Integer | 
    Boolean archived = false; // Boolean | Whether to return only results that have been archived.
    try {
      PublicActionDefinition result = apiInstance.getAutomationV4ActionsAppIdDefinitionIdGetById(definitionId, appId, archived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinitionsApi#getAutomationV4ActionsAppIdDefinitionIdGetById");
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
| **archived** | **Boolean**| Whether to return only results that have been archived. | [optional] [default to false] |

### Return type

[**PublicActionDefinition**](PublicActionDefinition.md)

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

<a id="getAutomationV4ActionsAppIdGetPage"></a>
# **getAutomationV4ActionsAppIdGetPage**
> CollectionResponsePublicActionDefinitionForwardPaging getAutomationV4ActionsAppIdGetPage(appId, limit, after, archived)

Get paged extension definitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    DefinitionsApi apiInstance = new DefinitionsApi(defaultClient);
    Integer appId = 56; // Integer | 
    Integer limit = 56; // Integer | The maximum number of results to display per page.
    String after = "after_example"; // String | The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
    Boolean archived = false; // Boolean | Whether to return only results that have been archived.
    try {
      CollectionResponsePublicActionDefinitionForwardPaging result = apiInstance.getAutomationV4ActionsAppIdGetPage(appId, limit, after, archived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinitionsApi#getAutomationV4ActionsAppIdGetPage");
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
| **appId** | **Integer**|  | |
| **limit** | **Integer**| The maximum number of results to display per page. | [optional] |
| **after** | **String**| The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results. | [optional] |
| **archived** | **Boolean**| Whether to return only results that have been archived. | [optional] [default to false] |

### Return type

[**CollectionResponsePublicActionDefinitionForwardPaging**](CollectionResponsePublicActionDefinitionForwardPaging.md)

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

<a id="patchAutomationV4ActionsAppIdDefinitionIdUpdate"></a>
# **patchAutomationV4ActionsAppIdDefinitionIdUpdate**
> PublicActionDefinition patchAutomationV4ActionsAppIdDefinitionIdUpdate(definitionId, appId, publicActionDefinitionPatch)

Patch an existing extension definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    DefinitionsApi apiInstance = new DefinitionsApi(defaultClient);
    String definitionId = "definitionId_example"; // String | 
    Integer appId = 56; // Integer | 
    PublicActionDefinitionPatch publicActionDefinitionPatch = new PublicActionDefinitionPatch(); // PublicActionDefinitionPatch | 
    try {
      PublicActionDefinition result = apiInstance.patchAutomationV4ActionsAppIdDefinitionIdUpdate(definitionId, appId, publicActionDefinitionPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinitionsApi#patchAutomationV4ActionsAppIdDefinitionIdUpdate");
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
| **publicActionDefinitionPatch** | [**PublicActionDefinitionPatch**](PublicActionDefinitionPatch.md)|  | |

### Return type

[**PublicActionDefinition**](PublicActionDefinition.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="postAutomationV4ActionsAppIdCreate"></a>
# **postAutomationV4ActionsAppIdCreate**
> PublicActionDefinition postAutomationV4ActionsAppIdCreate(appId, publicActionDefinitionEgg)

Create a new extension definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    DefinitionsApi apiInstance = new DefinitionsApi(defaultClient);
    Integer appId = 56; // Integer | 
    PublicActionDefinitionEgg publicActionDefinitionEgg = new PublicActionDefinitionEgg(); // PublicActionDefinitionEgg | 
    try {
      PublicActionDefinition result = apiInstance.postAutomationV4ActionsAppIdCreate(appId, publicActionDefinitionEgg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinitionsApi#postAutomationV4ActionsAppIdCreate");
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
| **appId** | **Integer**|  | |
| **publicActionDefinitionEgg** | [**PublicActionDefinitionEgg**](PublicActionDefinitionEgg.md)|  | |

### Return type

[**PublicActionDefinition**](PublicActionDefinition.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **0** | An error occurred. |  -  |


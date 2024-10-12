# KnowledgebasesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**knowledgebaseCreate**](KnowledgebasesApi.md#knowledgebaseCreate) | **POST** /knowledgebases/create | Asynchronous operation to create a new knowledgebase. |
| [**knowledgebaseDelete**](KnowledgebasesApi.md#knowledgebaseDelete) | **DELETE** /knowledgebases/{kbId} | Deletes the knowledgebase and all its data. |
| [**knowledgebaseDownload**](KnowledgebasesApi.md#knowledgebaseDownload) | **GET** /knowledgebases/{kbId}/{environment}/qna | Download the knowledgebase. |
| [**knowledgebaseGetDetails**](KnowledgebasesApi.md#knowledgebaseGetDetails) | **GET** /knowledgebases/{kbId} | Gets details of a specific knowledgebase. |
| [**knowledgebaseListAll**](KnowledgebasesApi.md#knowledgebaseListAll) | **GET** /knowledgebases | Gets all knowledgebases for a user. |
| [**knowledgebasePublish**](KnowledgebasesApi.md#knowledgebasePublish) | **POST** /knowledgebases/{kbId} | Publishes all changes in test index of a knowledgebase to its prod index. |
| [**knowledgebaseReplace**](KnowledgebasesApi.md#knowledgebaseReplace) | **PUT** /knowledgebases/{kbId} | Replace knowledgebase contents. |
| [**knowledgebaseUpdate**](KnowledgebasesApi.md#knowledgebaseUpdate) | **PATCH** /knowledgebases/{kbId} | Asynchronous operation to modify a knowledgebase. |


<a id="knowledgebaseCreate"></a>
# **knowledgebaseCreate**
> Operation knowledgebaseCreate(createKbPayload)

Asynchronous operation to create a new knowledgebase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KnowledgebasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    KnowledgebasesApi apiInstance = new KnowledgebasesApi(defaultClient);
    CreateKbDTO createKbPayload = new CreateKbDTO(); // CreateKbDTO | Post body of the request.
    try {
      Operation result = apiInstance.knowledgebaseCreate(createKbPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KnowledgebasesApi#knowledgebaseCreate");
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
| **createKbPayload** | [**CreateKbDTO**](CreateKbDTO.md)| Post body of the request. | |

### Return type

[**Operation**](Operation.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Details of the asynchronous operation. |  -  |
| **0** | Error response. |  -  |

<a id="knowledgebaseDelete"></a>
# **knowledgebaseDelete**
> knowledgebaseDelete(kbId)

Deletes the knowledgebase and all its data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KnowledgebasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    KnowledgebasesApi apiInstance = new KnowledgebasesApi(defaultClient);
    String kbId = "kbId_example"; // String | Knowledgebase id.
    try {
      apiInstance.knowledgebaseDelete(kbId);
    } catch (ApiException e) {
      System.err.println("Exception when calling KnowledgebasesApi#knowledgebaseDelete");
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
| **kbId** | **String**| Knowledgebase id. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | HTTP 204 No content. |  -  |
| **0** | Error response. |  -  |

<a id="knowledgebaseDownload"></a>
# **knowledgebaseDownload**
> QnADocumentsDTO knowledgebaseDownload(kbId, environment)

Download the knowledgebase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KnowledgebasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    KnowledgebasesApi apiInstance = new KnowledgebasesApi(defaultClient);
    String kbId = "kbId_example"; // String | Knowledgebase id.
    String environment = "Prod"; // String | Specifies whether environment is Test or Prod.
    try {
      QnADocumentsDTO result = apiInstance.knowledgebaseDownload(kbId, environment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KnowledgebasesApi#knowledgebaseDownload");
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
| **kbId** | **String**| Knowledgebase id. | |
| **environment** | **String**| Specifies whether environment is Test or Prod. | [enum: Prod, Test] |

### Return type

[**QnADocumentsDTO**](QnADocumentsDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection of all Q-A in the knowledgebase. |  -  |
| **0** | Error response. |  -  |

<a id="knowledgebaseGetDetails"></a>
# **knowledgebaseGetDetails**
> KnowledgebaseDTO knowledgebaseGetDetails(kbId)

Gets details of a specific knowledgebase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KnowledgebasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    KnowledgebasesApi apiInstance = new KnowledgebasesApi(defaultClient);
    String kbId = "kbId_example"; // String | Knowledgebase id.
    try {
      KnowledgebaseDTO result = apiInstance.knowledgebaseGetDetails(kbId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KnowledgebasesApi#knowledgebaseGetDetails");
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
| **kbId** | **String**| Knowledgebase id. | |

### Return type

[**KnowledgebaseDTO**](KnowledgebaseDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the knowledgebase. |  -  |
| **0** | Error response. |  -  |

<a id="knowledgebaseListAll"></a>
# **knowledgebaseListAll**
> KnowledgebasesDTO knowledgebaseListAll()

Gets all knowledgebases for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KnowledgebasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    KnowledgebasesApi apiInstance = new KnowledgebasesApi(defaultClient);
    try {
      KnowledgebasesDTO result = apiInstance.knowledgebaseListAll();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KnowledgebasesApi#knowledgebaseListAll");
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

[**KnowledgebasesDTO**](KnowledgebasesDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection of knowledgebases. |  -  |
| **0** | Error response. |  -  |

<a id="knowledgebasePublish"></a>
# **knowledgebasePublish**
> knowledgebasePublish(kbId)

Publishes all changes in test index of a knowledgebase to its prod index.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KnowledgebasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    KnowledgebasesApi apiInstance = new KnowledgebasesApi(defaultClient);
    String kbId = "kbId_example"; // String | Knowledgebase id.
    try {
      apiInstance.knowledgebasePublish(kbId);
    } catch (ApiException e) {
      System.err.println("Exception when calling KnowledgebasesApi#knowledgebasePublish");
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
| **kbId** | **String**| Knowledgebase id. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | HTTP 204 No content. |  -  |
| **0** | Error response. |  -  |

<a id="knowledgebaseReplace"></a>
# **knowledgebaseReplace**
> knowledgebaseReplace(kbId, replaceKb)

Replace knowledgebase contents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KnowledgebasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    KnowledgebasesApi apiInstance = new KnowledgebasesApi(defaultClient);
    String kbId = "kbId_example"; // String | Knowledgebase id.
    ReplaceKbDTO replaceKb = new ReplaceKbDTO(); // ReplaceKbDTO | An instance of ReplaceKbDTO which contains list of qnas to be uploaded
    try {
      apiInstance.knowledgebaseReplace(kbId, replaceKb);
    } catch (ApiException e) {
      System.err.println("Exception when calling KnowledgebasesApi#knowledgebaseReplace");
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
| **kbId** | **String**| Knowledgebase id. | |
| **replaceKb** | [**ReplaceKbDTO**](ReplaceKbDTO.md)| An instance of ReplaceKbDTO which contains list of qnas to be uploaded | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | HTTP 204 No content. |  -  |
| **0** | Error response. |  -  |

<a id="knowledgebaseUpdate"></a>
# **knowledgebaseUpdate**
> Operation knowledgebaseUpdate(kbId, updateKb)

Asynchronous operation to modify a knowledgebase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KnowledgebasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    KnowledgebasesApi apiInstance = new KnowledgebasesApi(defaultClient);
    String kbId = "kbId_example"; // String | Knowledgebase id.
    UpdateKbOperationDTO updateKb = new UpdateKbOperationDTO(); // UpdateKbOperationDTO | Post body of the request.
    try {
      Operation result = apiInstance.knowledgebaseUpdate(kbId, updateKb);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KnowledgebasesApi#knowledgebaseUpdate");
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
| **kbId** | **String**| Knowledgebase id. | |
| **updateKb** | [**UpdateKbOperationDTO**](UpdateKbOperationDTO.md)| Post body of the request. | |

### Return type

[**Operation**](Operation.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Details of the asynchronous operation. |  * Location - Relative URI to the target location of the asynchronous operation. Client should poll this resource to get status of the operation. <br>  |
| **0** | Error response. |  -  |


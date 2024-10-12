# DefaultApi

All URIs are relative to *https://api.doqs.dev/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTemplateDesignerTemplatesPost**](DefaultApi.md#createTemplateDesignerTemplatesPost) | **POST** /designer/templates | Create Template |
| [**deleteDesignerTemplatesIdDelete**](DefaultApi.md#deleteDesignerTemplatesIdDelete) | **DELETE** /designer/templates/{id} | Delete |
| [**generatePdfDesignerTemplatesIdGeneratePost**](DefaultApi.md#generatePdfDesignerTemplatesIdGeneratePost) | **POST** /designer/templates/{id}/generate | Generate Pdf |
| [**listTemplatesDesignerTemplatesGet**](DefaultApi.md#listTemplatesDesignerTemplatesGet) | **GET** /designer/templates | List Templates |
| [**listTemplatesDesignerTemplatesIdGet**](DefaultApi.md#listTemplatesDesignerTemplatesIdGet) | **GET** /designer/templates/{id} | List Templates |
| [**previewDesignerTemplatesPreviewPost**](DefaultApi.md#previewDesignerTemplatesPreviewPost) | **POST** /designer/templates/preview | Preview |
| [**updateTemplateDesignerTemplatesIdPut**](DefaultApi.md#updateTemplateDesignerTemplatesIdPut) | **PUT** /designer/templates/{id} | Update Template |


<a id="createTemplateDesignerTemplatesPost"></a>
# **createTemplateDesignerTemplatesPost**
> ResponseOkDesignerTemplate createTemplateDesignerTemplatesPost(createOrUpdateTemplateRequest)

Create Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.doqs.dev/v1");
    
    // Configure API key authorization: apiKeyAuth
    ApiKeyAuth apiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyAuth");
    apiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateOrUpdateTemplateRequest createOrUpdateTemplateRequest = new CreateOrUpdateTemplateRequest(); // CreateOrUpdateTemplateRequest | 
    try {
      ResponseOkDesignerTemplate result = apiInstance.createTemplateDesignerTemplatesPost(createOrUpdateTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createTemplateDesignerTemplatesPost");
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
| **createOrUpdateTemplateRequest** | [**CreateOrUpdateTemplateRequest**](CreateOrUpdateTemplateRequest.md)|  | |

### Return type

[**ResponseOkDesignerTemplate**](ResponseOkDesignerTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **4XX** | Client Error |  -  |
| **5XX** | Server Error |  -  |

<a id="deleteDesignerTemplatesIdDelete"></a>
# **deleteDesignerTemplatesIdDelete**
> ResponseOkNoneType deleteDesignerTemplatesIdDelete(id)

Delete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.doqs.dev/v1");
    
    // Configure API key authorization: apiKeyAuth
    ApiKeyAuth apiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyAuth");
    apiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      ResponseOkNoneType result = apiInstance.deleteDesignerTemplatesIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDesignerTemplatesIdDelete");
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
| **id** | **String**|  | |

### Return type

[**ResponseOkNoneType**](ResponseOkNoneType.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **4XX** | Client Error |  -  |
| **5XX** | Server Error |  -  |

<a id="generatePdfDesignerTemplatesIdGeneratePost"></a>
# **generatePdfDesignerTemplatesIdGeneratePost**
> Object generatePdfDesignerTemplatesIdGeneratePost(id, generatePDFPayload)

Generate Pdf

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.doqs.dev/v1");
    
    // Configure API key authorization: apiKeyAuth
    ApiKeyAuth apiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyAuth");
    apiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    GeneratePDFPayload generatePDFPayload = new GeneratePDFPayload(); // GeneratePDFPayload | 
    try {
      Object result = apiInstance.generatePdfDesignerTemplatesIdGeneratePost(id, generatePDFPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#generatePdfDesignerTemplatesIdGeneratePost");
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
| **id** | **String**|  | |
| **generatePDFPayload** | [**GeneratePDFPayload**](GeneratePDFPayload.md)|  | |

### Return type

**Object**

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **4XX** | Client Error |  -  |
| **5XX** | Server Error |  -  |

<a id="listTemplatesDesignerTemplatesGet"></a>
# **listTemplatesDesignerTemplatesGet**
> ResponseOkListFillrEntitiesDesignerTemplateDesignerTemplate listTemplatesDesignerTemplatesGet(limit, offset)

List Templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.doqs.dev/v1");
    
    // Configure API key authorization: apiKeyAuth
    ApiKeyAuth apiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyAuth");
    apiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 100; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      ResponseOkListFillrEntitiesDesignerTemplateDesignerTemplate result = apiInstance.listTemplatesDesignerTemplatesGet(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTemplatesDesignerTemplatesGet");
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
| **limit** | **Integer**|  | [optional] [default to 100] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ResponseOkListFillrEntitiesDesignerTemplateDesignerTemplate**](ResponseOkListFillrEntitiesDesignerTemplateDesignerTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **4XX** | Client Error |  -  |
| **5XX** | Server Error |  -  |

<a id="listTemplatesDesignerTemplatesIdGet"></a>
# **listTemplatesDesignerTemplatesIdGet**
> ResponseOkDesignerTemplate listTemplatesDesignerTemplatesIdGet(id)

List Templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.doqs.dev/v1");
    
    // Configure API key authorization: apiKeyAuth
    ApiKeyAuth apiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyAuth");
    apiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      ResponseOkDesignerTemplate result = apiInstance.listTemplatesDesignerTemplatesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTemplatesDesignerTemplatesIdGet");
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
| **id** | **String**|  | |

### Return type

[**ResponseOkDesignerTemplate**](ResponseOkDesignerTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **4XX** | Client Error |  -  |
| **5XX** | Server Error |  -  |

<a id="previewDesignerTemplatesPreviewPost"></a>
# **previewDesignerTemplatesPreviewPost**
> ResponseOkPreviewResponse previewDesignerTemplatesPreviewPost(previewModel)

Preview

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.doqs.dev/v1");
    
    // Configure API key authorization: apiKeyAuth
    ApiKeyAuth apiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyAuth");
    apiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PreviewModel previewModel = new PreviewModel(); // PreviewModel | 
    try {
      ResponseOkPreviewResponse result = apiInstance.previewDesignerTemplatesPreviewPost(previewModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#previewDesignerTemplatesPreviewPost");
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
| **previewModel** | [**PreviewModel**](PreviewModel.md)|  | |

### Return type

[**ResponseOkPreviewResponse**](ResponseOkPreviewResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **4XX** | Client Error |  -  |
| **5XX** | Server Error |  -  |

<a id="updateTemplateDesignerTemplatesIdPut"></a>
# **updateTemplateDesignerTemplatesIdPut**
> ResponseOkDesignerTemplate updateTemplateDesignerTemplatesIdPut(id, createOrUpdateTemplateRequest)

Update Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.doqs.dev/v1");
    
    // Configure API key authorization: apiKeyAuth
    ApiKeyAuth apiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyAuth");
    apiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyAuth.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    CreateOrUpdateTemplateRequest createOrUpdateTemplateRequest = new CreateOrUpdateTemplateRequest(); // CreateOrUpdateTemplateRequest | 
    try {
      ResponseOkDesignerTemplate result = apiInstance.updateTemplateDesignerTemplatesIdPut(id, createOrUpdateTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateTemplateDesignerTemplatesIdPut");
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
| **id** | **String**|  | |
| **createOrUpdateTemplateRequest** | [**CreateOrUpdateTemplateRequest**](CreateOrUpdateTemplateRequest.md)|  | |

### Return type

[**ResponseOkDesignerTemplate**](ResponseOkDesignerTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **4XX** | Client Error |  -  |
| **5XX** | Server Error |  -  |


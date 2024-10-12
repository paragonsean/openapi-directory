# TranslationRequestsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**translationRequestsCreateTranslationRequest**](TranslationRequestsApi.md#translationRequestsCreateTranslationRequest) | **POST** /api/v2/TranslationRequests | Create a translation request. Accepts a TranslationRequest object. Returns the Id of the created object. The state of the TranslationRequest must be ‘NotSubmitted’. |
| [**translationRequestsGetTranslationRequest**](TranslationRequestsApi.md#translationRequestsGetTranslationRequest) | **GET** /api/v2/TranslationRequests/{Id} | Get a TranslationRequest object by id. Returns TranslationRequest object with its language ids and string ids. |
| [**translationRequestsGetTranslationRequests**](TranslationRequestsApi.md#translationRequestsGetTranslationRequests) | **GET** /api/v2/TranslationRequests | Get all TranslationRequest objects. Returns a PagedResponse of TranslationRequest objects with their language ids and string ids. |
| [**translationRequestsUpdateTranslationRequest**](TranslationRequestsApi.md#translationRequestsUpdateTranslationRequest) | **PUT** /api/v2/TranslationRequests/{Id} | Update a TranslationRequest object by id. Accepts a TranslationRequest object. |
| [**translationRequestsUpdateTranslationRequestStrings**](TranslationRequestsApi.md#translationRequestsUpdateTranslationRequestStrings) | **PUT** /api/v2/TranslationRequests/{Id}/Strings | No Documentation Found. |


<a id="translationRequestsCreateTranslationRequest"></a>
# **translationRequestsCreateTranslationRequest**
> Integer translationRequestsCreateTranslationRequest(globalResourcesSharedModelsTranslationRequest)

Create a translation request. Accepts a TranslationRequest object. Returns the Id of the created object. The state of the TranslationRequest must be ‘NotSubmitted’.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationRequestsApi apiInstance = new TranslationRequestsApi(defaultClient);
    GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest = new GlobalResourcesSharedModelsTranslationRequest(); // GlobalResourcesSharedModelsTranslationRequest | 
    try {
      Integer result = apiInstance.translationRequestsCreateTranslationRequest(globalResourcesSharedModelsTranslationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationRequestsApi#translationRequestsCreateTranslationRequest");
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
| **globalResourcesSharedModelsTranslationRequest** | [**GlobalResourcesSharedModelsTranslationRequest**](GlobalResourcesSharedModelsTranslationRequest.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationRequestsGetTranslationRequest"></a>
# **translationRequestsGetTranslationRequest**
> GlobalResourcesSharedModelsTranslationRequest translationRequestsGetTranslationRequest(id)

Get a TranslationRequest object by id. Returns TranslationRequest object with its language ids and string ids.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationRequestsApi apiInstance = new TranslationRequestsApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      GlobalResourcesSharedModelsTranslationRequest result = apiInstance.translationRequestsGetTranslationRequest(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationRequestsApi#translationRequestsGetTranslationRequest");
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
| **id** | **Integer**|  | |

### Return type

[**GlobalResourcesSharedModelsTranslationRequest**](GlobalResourcesSharedModelsTranslationRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationRequestsGetTranslationRequests"></a>
# **translationRequestsGetTranslationRequests**
> APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest translationRequestsGetTranslationRequests(limit, offset)

Get all TranslationRequest objects. Returns a PagedResponse of TranslationRequest objects with their language ids and string ids.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationRequestsApi apiInstance = new TranslationRequestsApi(defaultClient);
    Integer limit = 56; // Integer | 
    Integer offset = 56; // Integer | 
    try {
      APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest result = apiInstance.translationRequestsGetTranslationRequests(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationRequestsApi#translationRequestsGetTranslationRequests");
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
| **limit** | **Integer**|  | [optional] |
| **offset** | **Integer**|  | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest**](APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="translationRequestsUpdateTranslationRequest"></a>
# **translationRequestsUpdateTranslationRequest**
> translationRequestsUpdateTranslationRequest(id, globalResourcesSharedModelsTranslationRequest, doResendRequest)

Update a TranslationRequest object by id. Accepts a TranslationRequest object.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationRequestsApi apiInstance = new TranslationRequestsApi(defaultClient);
    Integer id = 56; // Integer | 
    GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest = new GlobalResourcesSharedModelsTranslationRequest(); // GlobalResourcesSharedModelsTranslationRequest | 
    Boolean doResendRequest = true; // Boolean | 
    try {
      apiInstance.translationRequestsUpdateTranslationRequest(id, globalResourcesSharedModelsTranslationRequest, doResendRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationRequestsApi#translationRequestsUpdateTranslationRequest");
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
| **id** | **Integer**|  | |
| **globalResourcesSharedModelsTranslationRequest** | [**GlobalResourcesSharedModelsTranslationRequest**](GlobalResourcesSharedModelsTranslationRequest.md)|  | |
| **doResendRequest** | **Boolean**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="translationRequestsUpdateTranslationRequestStrings"></a>
# **translationRequestsUpdateTranslationRequestStrings**
> translationRequestsUpdateTranslationRequestStrings(id, requestBody)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranslationRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    TranslationRequestsApi apiInstance = new TranslationRequestsApi(defaultClient);
    Integer id = 56; // Integer | 
    List<String> requestBody = Arrays.asList(); // List<String> | 
    try {
      apiInstance.translationRequestsUpdateTranslationRequestStrings(id, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranslationRequestsApi#translationRequestsUpdateTranslationRequestStrings");
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
| **id** | **Integer**|  | |
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |


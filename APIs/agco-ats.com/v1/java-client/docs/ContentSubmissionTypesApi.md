# ContentSubmissionTypesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentSubmissionTypesDeleteContentSubmissionType**](ContentSubmissionTypesApi.md#contentSubmissionTypesDeleteContentSubmissionType) | **DELETE** /api/v2/ContentSubmissionTypes/{id} | Remove a Content Submission Type |
| [**contentSubmissionTypesGetContentSubmissionType**](ContentSubmissionTypesApi.md#contentSubmissionTypesGetContentSubmissionType) | **GET** /api/v2/ContentSubmissionTypes/{id} | Retrieves a Content Submission Type by its ID. |
| [**contentSubmissionTypesGetContentSubmissionTypes**](ContentSubmissionTypesApi.md#contentSubmissionTypesGetContentSubmissionTypes) | **GET** /api/v2/ContentSubmissionTypes | Returns available Content Submission Types. |
| [**contentSubmissionTypesPostContentSubmissionType**](ContentSubmissionTypesApi.md#contentSubmissionTypesPostContentSubmissionType) | **POST** /api/v2/ContentSubmissionTypes | Add a Content Submission Type |
| [**contentSubmissionTypesPutContentSubmissionType**](ContentSubmissionTypesApi.md#contentSubmissionTypesPutContentSubmissionType) | **PUT** /api/v2/ContentSubmissionTypes/{id} | Update a Content Submission Type |


<a id="contentSubmissionTypesDeleteContentSubmissionType"></a>
# **contentSubmissionTypesDeleteContentSubmissionType**
> contentSubmissionTypesDeleteContentSubmissionType(id)

Remove a Content Submission Type

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionTypesApi apiInstance = new ContentSubmissionTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Content Submission Type
    try {
      apiInstance.contentSubmissionTypesDeleteContentSubmissionType(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionTypesApi#contentSubmissionTypesDeleteContentSubmissionType");
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
| **id** | **Integer**| The ID of the Content Submission Type | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="contentSubmissionTypesGetContentSubmissionType"></a>
# **contentSubmissionTypesGetContentSubmissionType**
> ContentSubmissionSharedBusinessEntitiesContentSubmissionType contentSubmissionTypesGetContentSubmissionType(id)

Retrieves a Content Submission Type by its ID.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionTypesApi apiInstance = new ContentSubmissionTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Content Submission Type
    try {
      ContentSubmissionSharedBusinessEntitiesContentSubmissionType result = apiInstance.contentSubmissionTypesGetContentSubmissionType(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionTypesApi#contentSubmissionTypesGetContentSubmissionType");
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
| **id** | **Integer**| The ID of the Content Submission Type | |

### Return type

[**ContentSubmissionSharedBusinessEntitiesContentSubmissionType**](ContentSubmissionSharedBusinessEntitiesContentSubmissionType.md)

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

<a id="contentSubmissionTypesGetContentSubmissionTypes"></a>
# **contentSubmissionTypesGetContentSubmissionTypes**
> List&lt;ContentSubmissionSharedBusinessEntitiesContentSubmissionType&gt; contentSubmissionTypesGetContentSubmissionTypes(enabled)

Returns available Content Submission Types.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionTypesApi apiInstance = new ContentSubmissionTypesApi(defaultClient);
    Boolean enabled = true; // Boolean | 
    try {
      List<ContentSubmissionSharedBusinessEntitiesContentSubmissionType> result = apiInstance.contentSubmissionTypesGetContentSubmissionTypes(enabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionTypesApi#contentSubmissionTypesGetContentSubmissionTypes");
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
| **enabled** | **Boolean**|  | [optional] |

### Return type

[**List&lt;ContentSubmissionSharedBusinessEntitiesContentSubmissionType&gt;**](ContentSubmissionSharedBusinessEntitiesContentSubmissionType.md)

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

<a id="contentSubmissionTypesPostContentSubmissionType"></a>
# **contentSubmissionTypesPostContentSubmissionType**
> Integer contentSubmissionTypesPostContentSubmissionType(contentSubmissionSharedBusinessEntitiesContentSubmissionType)

Add a Content Submission Type

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionTypesApi apiInstance = new ContentSubmissionTypesApi(defaultClient);
    ContentSubmissionSharedBusinessEntitiesContentSubmissionType contentSubmissionSharedBusinessEntitiesContentSubmissionType = new ContentSubmissionSharedBusinessEntitiesContentSubmissionType(); // ContentSubmissionSharedBusinessEntitiesContentSubmissionType | The Content Submission Type
    try {
      Integer result = apiInstance.contentSubmissionTypesPostContentSubmissionType(contentSubmissionSharedBusinessEntitiesContentSubmissionType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionTypesApi#contentSubmissionTypesPostContentSubmissionType");
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
| **contentSubmissionSharedBusinessEntitiesContentSubmissionType** | [**ContentSubmissionSharedBusinessEntitiesContentSubmissionType**](ContentSubmissionSharedBusinessEntitiesContentSubmissionType.md)| The Content Submission Type | |

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

<a id="contentSubmissionTypesPutContentSubmissionType"></a>
# **contentSubmissionTypesPutContentSubmissionType**
> contentSubmissionTypesPutContentSubmissionType(id, contentSubmissionSharedBusinessEntitiesContentSubmissionType)

Update a Content Submission Type

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentSubmissionTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentSubmissionTypesApi apiInstance = new ContentSubmissionTypesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Content Submission Type
    ContentSubmissionSharedBusinessEntitiesContentSubmissionType contentSubmissionSharedBusinessEntitiesContentSubmissionType = new ContentSubmissionSharedBusinessEntitiesContentSubmissionType(); // ContentSubmissionSharedBusinessEntitiesContentSubmissionType | The Content Submission Type
    try {
      apiInstance.contentSubmissionTypesPutContentSubmissionType(id, contentSubmissionSharedBusinessEntitiesContentSubmissionType);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentSubmissionTypesApi#contentSubmissionTypesPutContentSubmissionType");
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
| **id** | **Integer**| The ID of the Content Submission Type | |
| **contentSubmissionSharedBusinessEntitiesContentSubmissionType** | [**ContentSubmissionSharedBusinessEntitiesContentSubmissionType**](ContentSubmissionSharedBusinessEntitiesContentSubmissionType.md)| The Content Submission Type | |

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


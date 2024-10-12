# DocumentsDocumentTypeApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**documentsDocumenttypeGet**](DocumentsDocumentTypeApi.md#documentsDocumenttypeGet) | **GET** /Documents/DocumentType | DocumentType: List All Possible Types |
| [**documentsDocumenttypeGetId**](DocumentsDocumentTypeApi.md#documentsDocumenttypeGetId) | **GET** /Documents/DocumentType/{id} | DocumentType: Get by Id |
| [**documentsDocumenttypeTypeidGetTypeId**](DocumentsDocumentTypeApi.md#documentsDocumenttypeTypeidGetTypeId) | **GET** /Documents/DocumentType/TypeId/{type_id} | DocumentType: Get By Type Id |


<a id="documentsDocumenttypeGet"></a>
# **documentsDocumenttypeGet**
> List&lt;DocumentType&gt; documentsDocumenttypeGet()

DocumentType: List All Possible Types

List Types: Use this method to retreive a list of possible options for the DocumentType type. Use the Id from oneof the returned elements on to make changes to elements in the Documents object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsDocumentTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    DocumentsDocumentTypeApi apiInstance = new DocumentsDocumentTypeApi(defaultClient);
    try {
      List<DocumentType> result = apiInstance.documentsDocumenttypeGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsDocumentTypeApi#documentsDocumenttypeGet");
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

[**List&lt;DocumentType&gt;**](DocumentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="documentsDocumenttypeGetId"></a>
# **documentsDocumenttypeGetId**
> DocumentType documentsDocumenttypeGetId(id)

DocumentType: Get by Id

Get by Id: Use this method to retrieve a DocumentType object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsDocumentTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    DocumentsDocumentTypeApi apiInstance = new DocumentsDocumentTypeApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      DocumentType result = apiInstance.documentsDocumenttypeGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsDocumentTypeApi#documentsDocumenttypeGetId");
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
| **id** | **UUID**|  | |

### Return type

[**DocumentType**](DocumentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="documentsDocumenttypeTypeidGetTypeId"></a>
# **documentsDocumenttypeTypeidGetTypeId**
> DocumentType documentsDocumenttypeTypeidGetTypeId(typeId)

DocumentType: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsDocumentTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    DocumentsDocumentTypeApi apiInstance = new DocumentsDocumentTypeApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      DocumentType result = apiInstance.documentsDocumenttypeTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsDocumentTypeApi#documentsDocumenttypeTypeidGetTypeId");
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
| **typeId** | **Integer**|  | |

### Return type

[**DocumentType**](DocumentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |


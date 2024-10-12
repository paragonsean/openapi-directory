# AnnotationLayersApi

All URIs are relative to *http://superset.apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**annotationLayerDelete**](AnnotationLayersApi.md#annotationLayerDelete) | **DELETE** /annotation_layer/ |  |
| [**annotationLayerGet**](AnnotationLayersApi.md#annotationLayerGet) | **GET** /annotation_layer/ |  |
| [**annotationLayerInfoGet**](AnnotationLayersApi.md#annotationLayerInfoGet) | **GET** /annotation_layer/_info |  |
| [**annotationLayerPkAnnotationAnnotationIdDelete**](AnnotationLayersApi.md#annotationLayerPkAnnotationAnnotationIdDelete) | **DELETE** /annotation_layer/{pk}/annotation/{annotation_id} |  |
| [**annotationLayerPkAnnotationAnnotationIdGet**](AnnotationLayersApi.md#annotationLayerPkAnnotationAnnotationIdGet) | **GET** /annotation_layer/{pk}/annotation/{annotation_id} |  |
| [**annotationLayerPkAnnotationAnnotationIdPut**](AnnotationLayersApi.md#annotationLayerPkAnnotationAnnotationIdPut) | **PUT** /annotation_layer/{pk}/annotation/{annotation_id} |  |
| [**annotationLayerPkAnnotationDelete**](AnnotationLayersApi.md#annotationLayerPkAnnotationDelete) | **DELETE** /annotation_layer/{pk}/annotation/ |  |
| [**annotationLayerPkAnnotationGet**](AnnotationLayersApi.md#annotationLayerPkAnnotationGet) | **GET** /annotation_layer/{pk}/annotation/ |  |
| [**annotationLayerPkAnnotationPost**](AnnotationLayersApi.md#annotationLayerPkAnnotationPost) | **POST** /annotation_layer/{pk}/annotation/ |  |
| [**annotationLayerPkDelete**](AnnotationLayersApi.md#annotationLayerPkDelete) | **DELETE** /annotation_layer/{pk} |  |
| [**annotationLayerPkGet**](AnnotationLayersApi.md#annotationLayerPkGet) | **GET** /annotation_layer/{pk} |  |
| [**annotationLayerPkPut**](AnnotationLayersApi.md#annotationLayerPkPut) | **PUT** /annotation_layer/{pk} |  |
| [**annotationLayerPost**](AnnotationLayersApi.md#annotationLayerPost) | **POST** /annotation_layer/ |  |
| [**annotationLayerRelatedColumnNameGet**](AnnotationLayersApi.md#annotationLayerRelatedColumnNameGet) | **GET** /annotation_layer/related/{column_name} |  |


<a id="annotationLayerDelete"></a>
# **annotationLayerDelete**
> AnnotationLayerGet400Response annotationLayerDelete(q)



Deletes multiple annotation layers in a bulk operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      AnnotationLayerGet400Response result = apiInstance.annotationLayerDelete(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerDelete");
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
| **q** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CSS templates bulk delete |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerGet"></a>
# **annotationLayerGet**
> AnnotationLayerGet200Response annotationLayerGet(q)



Get a list of Annotation layers, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    GetListSchema q = new GetListSchema(); // GetListSchema | 
    try {
      AnnotationLayerGet200Response result = apiInstance.annotationLayerGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerGet");
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
| **q** | [**GetListSchema**](.md)|  | [optional] |

### Return type

[**AnnotationLayerGet200Response**](AnnotationLayerGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Items from Model |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerInfoGet"></a>
# **annotationLayerInfoGet**
> AnnotationLayerInfoGet200Response annotationLayerInfoGet(q)



Get metadata information about this API resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    GetInfoSchema q = new GetInfoSchema(); // GetInfoSchema | 
    try {
      AnnotationLayerInfoGet200Response result = apiInstance.annotationLayerInfoGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerInfoGet");
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
| **q** | [**GetInfoSchema**](.md)|  | [optional] |

### Return type

[**AnnotationLayerInfoGet200Response**](AnnotationLayerInfoGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item from Model |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerPkAnnotationAnnotationIdDelete"></a>
# **annotationLayerPkAnnotationAnnotationIdDelete**
> AnnotationLayerGet400Response annotationLayerPkAnnotationAnnotationIdDelete(pk, annotationId)



Delete Annotation layer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    Integer pk = 56; // Integer | The annotation layer pk for this annotation
    Integer annotationId = 56; // Integer | The annotation pk for this annotation
    try {
      AnnotationLayerGet400Response result = apiInstance.annotationLayerPkAnnotationAnnotationIdDelete(pk, annotationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerPkAnnotationAnnotationIdDelete");
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
| **pk** | **Integer**| The annotation layer pk for this annotation | |
| **annotationId** | **Integer**| The annotation pk for this annotation | |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item deleted |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerPkAnnotationAnnotationIdGet"></a>
# **annotationLayerPkAnnotationAnnotationIdGet**
> AnnotationLayerPkAnnotationAnnotationIdGet200Response annotationLayerPkAnnotationAnnotationIdGet(pk, annotationId, q)



Get an Annotation layer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    Integer pk = 56; // Integer | The annotation layer pk for this annotation
    Integer annotationId = 56; // Integer | The annotation pk
    GetItemSchema q = new GetItemSchema(); // GetItemSchema | 
    try {
      AnnotationLayerPkAnnotationAnnotationIdGet200Response result = apiInstance.annotationLayerPkAnnotationAnnotationIdGet(pk, annotationId, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerPkAnnotationAnnotationIdGet");
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
| **pk** | **Integer**| The annotation layer pk for this annotation | |
| **annotationId** | **Integer**| The annotation pk | |
| **q** | [**GetItemSchema**](.md)|  | [optional] |

### Return type

[**AnnotationLayerPkAnnotationAnnotationIdGet200Response**](AnnotationLayerPkAnnotationAnnotationIdGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item from Model |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerPkAnnotationAnnotationIdPut"></a>
# **annotationLayerPkAnnotationAnnotationIdPut**
> AnnotationLayerPkAnnotationAnnotationIdPut200Response annotationLayerPkAnnotationAnnotationIdPut(pk, annotationId, annotationRestApiPut)



Update an Annotation layer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    Integer pk = 56; // Integer | The annotation layer pk for this annotation
    Integer annotationId = 56; // Integer | The annotation pk for this annotation
    AnnotationRestApiPut annotationRestApiPut = new AnnotationRestApiPut(); // AnnotationRestApiPut | Annotation schema
    try {
      AnnotationLayerPkAnnotationAnnotationIdPut200Response result = apiInstance.annotationLayerPkAnnotationAnnotationIdPut(pk, annotationId, annotationRestApiPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerPkAnnotationAnnotationIdPut");
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
| **pk** | **Integer**| The annotation layer pk for this annotation | |
| **annotationId** | **Integer**| The annotation pk for this annotation | |
| **annotationRestApiPut** | [**AnnotationRestApiPut**](AnnotationRestApiPut.md)| Annotation schema | |

### Return type

[**AnnotationLayerPkAnnotationAnnotationIdPut200Response**](AnnotationLayerPkAnnotationAnnotationIdPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Annotation changed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerPkAnnotationDelete"></a>
# **annotationLayerPkAnnotationDelete**
> AnnotationLayerGet400Response annotationLayerPkAnnotationDelete(pk, q)



Deletes multiple annotation in a bulk operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    Integer pk = 56; // Integer | The annotation layer pk for this annotation
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      AnnotationLayerGet400Response result = apiInstance.annotationLayerPkAnnotationDelete(pk, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerPkAnnotationDelete");
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
| **pk** | **Integer**| The annotation layer pk for this annotation | |
| **q** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Annotations bulk delete |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerPkAnnotationGet"></a>
# **annotationLayerPkAnnotationGet**
> AnnotationLayerPkAnnotationGet200Response annotationLayerPkAnnotationGet(pk, q)



Get a list of Annotation layers, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    Integer pk = 56; // Integer | The annotation layer id for this annotation
    GetListSchema q = new GetListSchema(); // GetListSchema | 
    try {
      AnnotationLayerPkAnnotationGet200Response result = apiInstance.annotationLayerPkAnnotationGet(pk, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerPkAnnotationGet");
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
| **pk** | **Integer**| The annotation layer id for this annotation | |
| **q** | [**GetListSchema**](.md)|  | [optional] |

### Return type

[**AnnotationLayerPkAnnotationGet200Response**](AnnotationLayerPkAnnotationGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Items from Annotations |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerPkAnnotationPost"></a>
# **annotationLayerPkAnnotationPost**
> AnnotationLayerPkAnnotationPost201Response annotationLayerPkAnnotationPost(pk, annotationRestApiPost)



Create an Annotation layer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    Integer pk = 56; // Integer | The annotation layer pk for this annotation
    AnnotationRestApiPost annotationRestApiPost = new AnnotationRestApiPost(); // AnnotationRestApiPost | Annotation schema
    try {
      AnnotationLayerPkAnnotationPost201Response result = apiInstance.annotationLayerPkAnnotationPost(pk, annotationRestApiPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerPkAnnotationPost");
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
| **pk** | **Integer**| The annotation layer pk for this annotation | |
| **annotationRestApiPost** | [**AnnotationRestApiPost**](AnnotationRestApiPost.md)| Annotation schema | |

### Return type

[**AnnotationLayerPkAnnotationPost201Response**](AnnotationLayerPkAnnotationPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Annotation added |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerPkDelete"></a>
# **annotationLayerPkDelete**
> AnnotationLayerGet400Response annotationLayerPkDelete(pk)



Delete Annotation layer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    Integer pk = 56; // Integer | The annotation layer pk for this annotation
    try {
      AnnotationLayerGet400Response result = apiInstance.annotationLayerPkDelete(pk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerPkDelete");
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
| **pk** | **Integer**| The annotation layer pk for this annotation | |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item deleted |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerPkGet"></a>
# **annotationLayerPkGet**
> AnnotationLayerPkGet200Response annotationLayerPkGet(pk, q)



Get an Annotation layer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    Integer pk = 56; // Integer | 
    GetItemSchema q = new GetItemSchema(); // GetItemSchema | 
    try {
      AnnotationLayerPkGet200Response result = apiInstance.annotationLayerPkGet(pk, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerPkGet");
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
| **pk** | **Integer**|  | |
| **q** | [**GetItemSchema**](.md)|  | [optional] |

### Return type

[**AnnotationLayerPkGet200Response**](AnnotationLayerPkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item from Model |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerPkPut"></a>
# **annotationLayerPkPut**
> AnnotationLayerPkPut200Response annotationLayerPkPut(pk, annotationLayerRestApiPut)



Update an Annotation layer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    Integer pk = 56; // Integer | The annotation layer pk for this annotation
    AnnotationLayerRestApiPut annotationLayerRestApiPut = new AnnotationLayerRestApiPut(); // AnnotationLayerRestApiPut | Annotation schema
    try {
      AnnotationLayerPkPut200Response result = apiInstance.annotationLayerPkPut(pk, annotationLayerRestApiPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerPkPut");
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
| **pk** | **Integer**| The annotation layer pk for this annotation | |
| **annotationLayerRestApiPut** | [**AnnotationLayerRestApiPut**](AnnotationLayerRestApiPut.md)| Annotation schema | |

### Return type

[**AnnotationLayerPkPut200Response**](AnnotationLayerPkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Annotation changed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerPost"></a>
# **annotationLayerPost**
> AnnotationLayerPost201Response annotationLayerPost(annotationLayerRestApiPost)



Create an Annotation layer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    AnnotationLayerRestApiPost annotationLayerRestApiPost = new AnnotationLayerRestApiPost(); // AnnotationLayerRestApiPost | Annotation Layer schema
    try {
      AnnotationLayerPost201Response result = apiInstance.annotationLayerPost(annotationLayerRestApiPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerPost");
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
| **annotationLayerRestApiPost** | [**AnnotationLayerRestApiPost**](AnnotationLayerRestApiPost.md)| Annotation Layer schema | |

### Return type

[**AnnotationLayerPost201Response**](AnnotationLayerPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Annotation added |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="annotationLayerRelatedColumnNameGet"></a>
# **annotationLayerRelatedColumnNameGet**
> RelatedResponseSchema annotationLayerRelatedColumnNameGet(columnName, q)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationLayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    AnnotationLayersApi apiInstance = new AnnotationLayersApi(defaultClient);
    String columnName = "columnName_example"; // String | 
    GetRelatedSchema q = new GetRelatedSchema(); // GetRelatedSchema | 
    try {
      RelatedResponseSchema result = apiInstance.annotationLayerRelatedColumnNameGet(columnName, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationLayersApi#annotationLayerRelatedColumnNameGet");
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
| **columnName** | **String**|  | |
| **q** | [**GetRelatedSchema**](.md)|  | [optional] |

### Return type

[**RelatedResponseSchema**](RelatedResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related column data |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |


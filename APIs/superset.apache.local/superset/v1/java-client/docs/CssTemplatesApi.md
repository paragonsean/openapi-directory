# CssTemplatesApi

All URIs are relative to *http://superset.apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cssTemplateDelete**](CssTemplatesApi.md#cssTemplateDelete) | **DELETE** /css_template/ |  |
| [**cssTemplateGet**](CssTemplatesApi.md#cssTemplateGet) | **GET** /css_template/ |  |
| [**cssTemplateInfoGet**](CssTemplatesApi.md#cssTemplateInfoGet) | **GET** /css_template/_info |  |
| [**cssTemplatePkDelete**](CssTemplatesApi.md#cssTemplatePkDelete) | **DELETE** /css_template/{pk} |  |
| [**cssTemplatePkGet**](CssTemplatesApi.md#cssTemplatePkGet) | **GET** /css_template/{pk} |  |
| [**cssTemplatePkPut**](CssTemplatesApi.md#cssTemplatePkPut) | **PUT** /css_template/{pk} |  |
| [**cssTemplatePost**](CssTemplatesApi.md#cssTemplatePost) | **POST** /css_template/ |  |
| [**cssTemplateRelatedColumnNameGet**](CssTemplatesApi.md#cssTemplateRelatedColumnNameGet) | **GET** /css_template/related/{column_name} |  |


<a id="cssTemplateDelete"></a>
# **cssTemplateDelete**
> AnnotationLayerGet400Response cssTemplateDelete(q)



Deletes multiple css templates in a bulk operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CssTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    CssTemplatesApi apiInstance = new CssTemplatesApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      AnnotationLayerGet400Response result = apiInstance.cssTemplateDelete(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CssTemplatesApi#cssTemplateDelete");
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

<a id="cssTemplateGet"></a>
# **cssTemplateGet**
> CssTemplateGet200Response cssTemplateGet(q)



Get a list of CSS templates, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CssTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    CssTemplatesApi apiInstance = new CssTemplatesApi(defaultClient);
    GetListSchema q = new GetListSchema(); // GetListSchema | 
    try {
      CssTemplateGet200Response result = apiInstance.cssTemplateGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CssTemplatesApi#cssTemplateGet");
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

[**CssTemplateGet200Response**](CssTemplateGet200Response.md)

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

<a id="cssTemplateInfoGet"></a>
# **cssTemplateInfoGet**
> AnnotationLayerInfoGet200Response cssTemplateInfoGet(q)



Get metadata information about this API resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CssTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    CssTemplatesApi apiInstance = new CssTemplatesApi(defaultClient);
    GetInfoSchema q = new GetInfoSchema(); // GetInfoSchema | 
    try {
      AnnotationLayerInfoGet200Response result = apiInstance.cssTemplateInfoGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CssTemplatesApi#cssTemplateInfoGet");
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

<a id="cssTemplatePkDelete"></a>
# **cssTemplatePkDelete**
> AnnotationLayerGet400Response cssTemplatePkDelete(pk)



Delete CSS template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CssTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    CssTemplatesApi apiInstance = new CssTemplatesApi(defaultClient);
    Integer pk = 56; // Integer | 
    try {
      AnnotationLayerGet400Response result = apiInstance.cssTemplatePkDelete(pk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CssTemplatesApi#cssTemplatePkDelete");
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

<a id="cssTemplatePkGet"></a>
# **cssTemplatePkGet**
> CssTemplatePkGet200Response cssTemplatePkGet(pk, q)



Get a CSS template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CssTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    CssTemplatesApi apiInstance = new CssTemplatesApi(defaultClient);
    Integer pk = 56; // Integer | 
    GetItemSchema q = new GetItemSchema(); // GetItemSchema | 
    try {
      CssTemplatePkGet200Response result = apiInstance.cssTemplatePkGet(pk, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CssTemplatesApi#cssTemplatePkGet");
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

[**CssTemplatePkGet200Response**](CssTemplatePkGet200Response.md)

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

<a id="cssTemplatePkPut"></a>
# **cssTemplatePkPut**
> CssTemplatePkPut200Response cssTemplatePkPut(pk, cssTemplateRestApiPut)



Update a CSS template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CssTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    CssTemplatesApi apiInstance = new CssTemplatesApi(defaultClient);
    Integer pk = 56; // Integer | 
    CssTemplateRestApiPut cssTemplateRestApiPut = new CssTemplateRestApiPut(); // CssTemplateRestApiPut | Model schema
    try {
      CssTemplatePkPut200Response result = apiInstance.cssTemplatePkPut(pk, cssTemplateRestApiPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CssTemplatesApi#cssTemplatePkPut");
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
| **cssTemplateRestApiPut** | [**CssTemplateRestApiPut**](CssTemplateRestApiPut.md)| Model schema | |

### Return type

[**CssTemplatePkPut200Response**](CssTemplatePkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item changed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="cssTemplatePost"></a>
# **cssTemplatePost**
> CssTemplatePost201Response cssTemplatePost(cssTemplateRestApiPost)



Create a CSS template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CssTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    CssTemplatesApi apiInstance = new CssTemplatesApi(defaultClient);
    CssTemplateRestApiPost cssTemplateRestApiPost = new CssTemplateRestApiPost(); // CssTemplateRestApiPost | Model schema
    try {
      CssTemplatePost201Response result = apiInstance.cssTemplatePost(cssTemplateRestApiPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CssTemplatesApi#cssTemplatePost");
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
| **cssTemplateRestApiPost** | [**CssTemplateRestApiPost**](CssTemplateRestApiPost.md)| Model schema | |

### Return type

[**CssTemplatePost201Response**](CssTemplatePost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Item inserted |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="cssTemplateRelatedColumnNameGet"></a>
# **cssTemplateRelatedColumnNameGet**
> RelatedResponseSchema cssTemplateRelatedColumnNameGet(columnName, q)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CssTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    CssTemplatesApi apiInstance = new CssTemplatesApi(defaultClient);
    String columnName = "columnName_example"; // String | 
    GetRelatedSchema q = new GetRelatedSchema(); // GetRelatedSchema | 
    try {
      RelatedResponseSchema result = apiInstance.cssTemplateRelatedColumnNameGet(columnName, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CssTemplatesApi#cssTemplateRelatedColumnNameGet");
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


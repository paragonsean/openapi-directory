# AssociationTypeApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**associationTypesGet**](AssociationTypeApi.md#associationTypesGet) | **GET** /api/rest/v1/association-types/{code} | Get an association type |
| [**associationTypesGetList**](AssociationTypeApi.md#associationTypesGetList) | **GET** /api/rest/v1/association-types | Get a list of association types |
| [**associationTypesPatch**](AssociationTypeApi.md#associationTypesPatch) | **PATCH** /api/rest/v1/association-types/{code} | Update/create an association type |
| [**associationTypesPost**](AssociationTypeApi.md#associationTypesPost) | **POST** /api/rest/v1/association-types | Create a new association type |
| [**severalAssociationTypesPatch**](AssociationTypeApi.md#severalAssociationTypesPatch) | **PATCH** /api/rest/v1/association-types | Update/create several association types |


<a id="associationTypesGet"></a>
# **associationTypesGet**
> AssociationTypesPostRequest associationTypesGet(code)

Get an association type

This endpoint allows you to get the information about a given association type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssociationTypeApi apiInstance = new AssociationTypeApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      AssociationTypesPostRequest result = apiInstance.associationTypesGet(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationTypeApi#associationTypesGet");
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
| **code** | **String**| Code of the resource | |

### Return type

[**AssociationTypesPostRequest**](AssociationTypesPostRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Resource not found |  -  |
| **406** | Not Acceptable |  -  |

<a id="associationTypesGetList"></a>
# **associationTypesGetList**
> AssociationTypes associationTypesGetList(page, limit, withCount)

Get a list of association types

This endpoint allows you to get a list of association types. Association types are paginated and sorted by code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssociationTypeApi apiInstance = new AssociationTypeApi(defaultClient);
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 10; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Boolean withCount = false; // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    try {
      AssociationTypes result = apiInstance.associationTypesGetList(page, limit, withCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationTypeApi#associationTypesGetList");
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
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10] |
| **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false] |

### Return type

[**AssociationTypes**](AssociationTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, current_page, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return association types paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="associationTypesPatch"></a>
# **associationTypesPatch**
> associationTypesPatch(code, body)

Update/create an association type

This endpoint allows you to update a given association type. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no association type exists for the given code, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssociationTypeApi apiInstance = new AssociationTypeApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    AssociationTypesPostRequest body = new AssociationTypesPostRequest(); // AssociationTypesPostRequest | 
    try {
      apiInstance.associationTypesPatch(code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationTypeApi#associationTypesPatch");
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
| **code** | **String**| Code of the resource | |
| **body** | [**AssociationTypesPostRequest**](AssociationTypesPostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - URI of the created resource <br>  |
| **204** | No content to return |  * Location - URI of the created resource <br>  |
| **400** | Bad request |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

<a id="associationTypesPost"></a>
# **associationTypesPost**
> associationTypesPost(body)

Create a new association type

This endpoint allows you to create a new association type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssociationTypeApi apiInstance = new AssociationTypeApi(defaultClient);
    AssociationTypesPostRequest body = new AssociationTypesPostRequest(); // AssociationTypesPostRequest | 
    try {
      apiInstance.associationTypesPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationTypeApi#associationTypesPost");
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
| **body** | [**AssociationTypesPostRequest**](AssociationTypesPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - URI of the created resource <br>  |
| **400** | Bad request |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

<a id="severalAssociationTypesPatch"></a>
# **severalAssociationTypesPatch**
> PatchAssetCategories200Response severalAssociationTypesPatch(body)

Update/create several association types

This endpoint allows you to update and/or create several association types at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssociationTypeApi apiInstance = new AssociationTypeApi(defaultClient);
    SeveralAssociationTypesPatchRequest body = new SeveralAssociationTypesPatchRequest(); // SeveralAssociationTypesPatchRequest | 
    try {
      PatchAssetCategories200Response result = apiInstance.severalAssociationTypesPatch(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationTypeApi#severalAssociationTypesPatch");
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
| **body** | [**SeveralAssociationTypesPatchRequest**](SeveralAssociationTypesPatchRequest.md)|  | [optional] |

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **413** | Request Entity Too Large |  -  |
| **415** | Unsupported Media type |  -  |


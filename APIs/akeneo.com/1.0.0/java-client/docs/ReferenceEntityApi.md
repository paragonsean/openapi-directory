# ReferenceEntityApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReferenceEntities**](ReferenceEntityApi.md#getReferenceEntities) | **GET** /api/rest/v1/reference-entities | Get list of reference entities |
| [**getReferenceEntitiesCode**](ReferenceEntityApi.md#getReferenceEntitiesCode) | **GET** /api/rest/v1/reference-entities/{code} | Get a reference entity |
| [**patchReferenceEntityCode**](ReferenceEntityApi.md#patchReferenceEntityCode) | **PATCH** /api/rest/v1/reference-entities/{code} | Update/create a reference entity |


<a id="getReferenceEntities"></a>
# **getReferenceEntities**
> ReferenceEntities getReferenceEntities(searchAfter)

Get list of reference entities

This endpoint allows you to get a list of reference entities. Reference entities are paginated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityApi apiInstance = new ReferenceEntityApi(defaultClient);
    String searchAfter = "cursor to the first page"; // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    try {
      ReferenceEntities result = apiInstance.getReferenceEntities(searchAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityApi#getReferenceEntities");
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
| **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page] |

### Return type

[**ReferenceEntities**](ReferenceEntities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return reference entities paginated |  -  |
| **401** | Authentication required |  -  |
| **406** | Not Acceptable |  -  |

<a id="getReferenceEntitiesCode"></a>
# **getReferenceEntitiesCode**
> GetReferenceEntitiesCode200Response getReferenceEntitiesCode(code)

Get a reference entity

This endpoint allows you to get the information about a given reference entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityApi apiInstance = new ReferenceEntityApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      GetReferenceEntitiesCode200Response result = apiInstance.getReferenceEntitiesCode(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityApi#getReferenceEntitiesCode");
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

[**GetReferenceEntitiesCode200Response**](GetReferenceEntitiesCode200Response.md)

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
| **404** | Resource not found |  -  |
| **406** | Not Acceptable |  -  |

<a id="patchReferenceEntityCode"></a>
# **patchReferenceEntityCode**
> patchReferenceEntityCode(code, body)

Update/create a reference entity

This endpoint allows you to update a given reference entity. Note that if the reference entity does not already exist, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityApi apiInstance = new ReferenceEntityApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    PatchReferenceEntityCodeRequest body = new PatchReferenceEntityCodeRequest(); // PatchReferenceEntityCodeRequest | 
    try {
      apiInstance.patchReferenceEntityCode(code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityApi#patchReferenceEntityCode");
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
| **body** | [**PatchReferenceEntityCodeRequest**](PatchReferenceEntityCodeRequest.md)|  | |

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
| **401** | Authentication required |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |


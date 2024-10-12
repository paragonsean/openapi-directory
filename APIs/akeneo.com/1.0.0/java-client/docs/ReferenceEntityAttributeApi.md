# ReferenceEntityAttributeApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReferenceEntitiesCodeAttributes**](ReferenceEntityAttributeApi.md#getReferenceEntitiesCodeAttributes) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes | Get the list of attributes of a given reference entity |
| [**getReferenceEntityAttributesCode**](ReferenceEntityAttributeApi.md#getReferenceEntityAttributesCode) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{code} | Get an attribute of a given reference entity |
| [**patchReferenceEntityAttributesCode**](ReferenceEntityAttributeApi.md#patchReferenceEntityAttributesCode) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{code} | Update/create an attribute of a given reference entity |


<a id="getReferenceEntitiesCodeAttributes"></a>
# **getReferenceEntitiesCodeAttributes**
> List&lt;GetReferenceEntitiesCodeAttributes200ResponseInner&gt; getReferenceEntitiesCodeAttributes(referenceEntityCode)

Get the list of attributes of a given reference entity

This endpoint allows you to get the list of attributes of a given reference entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityAttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityAttributeApi apiInstance = new ReferenceEntityAttributeApi(defaultClient);
    String referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
    try {
      List<GetReferenceEntitiesCodeAttributes200ResponseInner> result = apiInstance.getReferenceEntitiesCodeAttributes(referenceEntityCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityAttributeApi#getReferenceEntitiesCodeAttributes");
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
| **referenceEntityCode** | **String**| Code of the reference entity | |

### Return type

[**List&lt;GetReferenceEntitiesCodeAttributes200ResponseInner&gt;**](GetReferenceEntitiesCodeAttributes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the attributes of the given reference entity |  -  |
| **401** | Authentication required |  -  |
| **406** | Not Acceptable |  -  |

<a id="getReferenceEntityAttributesCode"></a>
# **getReferenceEntityAttributesCode**
> GetReferenceEntitiesCodeAttributes200ResponseInner getReferenceEntityAttributesCode(referenceEntityCode, code)

Get an attribute of a given reference entity

This endpoint allows you to get the information about a given attribute for a given reference entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityAttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityAttributeApi apiInstance = new ReferenceEntityAttributeApi(defaultClient);
    String referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
    String code = "code_example"; // String | Code of the resource
    try {
      GetReferenceEntitiesCodeAttributes200ResponseInner result = apiInstance.getReferenceEntityAttributesCode(referenceEntityCode, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityAttributeApi#getReferenceEntityAttributesCode");
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
| **referenceEntityCode** | **String**| Code of the reference entity | |
| **code** | **String**| Code of the resource | |

### Return type

[**GetReferenceEntitiesCodeAttributes200ResponseInner**](GetReferenceEntitiesCodeAttributes200ResponseInner.md)

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

<a id="patchReferenceEntityAttributesCode"></a>
# **patchReferenceEntityAttributesCode**
> patchReferenceEntityAttributesCode(referenceEntityCode, code, body)

Update/create an attribute of a given reference entity

This endpoint allows you to update a given attribute for a given renference entity. Note that if the attribute does not already exist for the given reference entity, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityAttributeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityAttributeApi apiInstance = new ReferenceEntityAttributeApi(defaultClient);
    String referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
    String code = "code_example"; // String | Code of the resource
    GetReferenceEntitiesCodeAttributes200ResponseInner body = new GetReferenceEntitiesCodeAttributes200ResponseInner(); // GetReferenceEntitiesCodeAttributes200ResponseInner | 
    try {
      apiInstance.patchReferenceEntityAttributesCode(referenceEntityCode, code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityAttributeApi#patchReferenceEntityAttributesCode");
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
| **referenceEntityCode** | **String**| Code of the reference entity | |
| **code** | **String**| Code of the resource | |
| **body** | [**GetReferenceEntitiesCodeAttributes200ResponseInner**](GetReferenceEntitiesCodeAttributes200ResponseInner.md)|  | |

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


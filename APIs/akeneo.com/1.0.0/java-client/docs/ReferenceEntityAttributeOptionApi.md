# ReferenceEntityAttributeOptionApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReferenceEntityAttributesAttributeCodeOptions**](ReferenceEntityAttributeOptionApi.md#getReferenceEntityAttributesAttributeCodeOptions) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{attribute_code}/options | Get a list of attribute options of a given attribute for a given reference entity |
| [**getReferenceEntityAttributesAttributeCodeOptionsCode**](ReferenceEntityAttributeOptionApi.md#getReferenceEntityAttributesAttributeCodeOptionsCode) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{attribute_code}/options/{code} | Get an attribute option for a given attribute of a given reference entity |
| [**patchReferenceEntityAttributesAttributeCodeOptionsCode**](ReferenceEntityAttributeOptionApi.md#patchReferenceEntityAttributesAttributeCodeOptionsCode) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{attribute_code}/options/{code} | Update/create a reference entity attribute option |


<a id="getReferenceEntityAttributesAttributeCodeOptions"></a>
# **getReferenceEntityAttributesAttributeCodeOptions**
> List&lt;GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner&gt; getReferenceEntityAttributesAttributeCodeOptions(referenceEntityCode, attributeCode)

Get a list of attribute options of a given attribute for a given reference entity

This endpoint allows you to get a list of attribute options for a given reference entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityAttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityAttributeOptionApi apiInstance = new ReferenceEntityAttributeOptionApi(defaultClient);
    String referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    try {
      List<GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner> result = apiInstance.getReferenceEntityAttributesAttributeCodeOptions(referenceEntityCode, attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityAttributeOptionApi#getReferenceEntityAttributesAttributeCodeOptions");
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
| **attributeCode** | **String**| Code of the attribute | |

### Return type

[**List&lt;GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner&gt;**](GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the options of the given attributes of the given reference entity |  -  |
| **401** | Authentication required |  -  |
| **406** | Not Acceptable |  -  |

<a id="getReferenceEntityAttributesAttributeCodeOptionsCode"></a>
# **getReferenceEntityAttributesAttributeCodeOptionsCode**
> GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner getReferenceEntityAttributesAttributeCodeOptionsCode(referenceEntityCode, attributeCode, code)

Get an attribute option for a given attribute of a given reference entity

This endpoint allows you to get the information about a given attribute option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityAttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityAttributeOptionApi apiInstance = new ReferenceEntityAttributeOptionApi(defaultClient);
    String referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    String code = "code_example"; // String | Code of the resource
    try {
      GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner result = apiInstance.getReferenceEntityAttributesAttributeCodeOptionsCode(referenceEntityCode, attributeCode, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityAttributeOptionApi#getReferenceEntityAttributesAttributeCodeOptionsCode");
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
| **attributeCode** | **String**| Code of the attribute | |
| **code** | **String**| Code of the resource | |

### Return type

[**GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner**](GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner.md)

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

<a id="patchReferenceEntityAttributesAttributeCodeOptionsCode"></a>
# **patchReferenceEntityAttributesAttributeCodeOptionsCode**
> patchReferenceEntityAttributesAttributeCodeOptionsCode(referenceEntityCode, attributeCode, code, body)

Update/create a reference entity attribute option

This endpoint allows you to update a given option for a given attribute and a given reference entity. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#patch-reference-entity-record-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the option does not already exist for the given attribute of the given reference entity, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityAttributeOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityAttributeOptionApi apiInstance = new ReferenceEntityAttributeOptionApi(defaultClient);
    String referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
    String attributeCode = "attributeCode_example"; // String | Code of the attribute
    String code = "code_example"; // String | Code of the resource
    GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner body = new GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner(); // GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner | 
    try {
      apiInstance.patchReferenceEntityAttributesAttributeCodeOptionsCode(referenceEntityCode, attributeCode, code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityAttributeOptionApi#patchReferenceEntityAttributesAttributeCodeOptionsCode");
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
| **attributeCode** | **String**| Code of the attribute | |
| **code** | **String**| Code of the resource | |
| **body** | [**GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner**](GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner.md)|  | |

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


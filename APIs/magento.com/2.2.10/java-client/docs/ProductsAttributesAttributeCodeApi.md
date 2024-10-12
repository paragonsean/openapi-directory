# ProductsAttributesAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductAttributeRepositoryV1DeleteByIdDelete**](ProductsAttributesAttributeCodeApi.md#catalogProductAttributeRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/attributes/{attributeCode} | products/attributes/{attributeCode} |
| [**catalogProductAttributeRepositoryV1GetGet**](ProductsAttributesAttributeCodeApi.md#catalogProductAttributeRepositoryV1GetGet) | **GET** /V1/products/attributes/{attributeCode} | products/attributes/{attributeCode} |
| [**catalogProductAttributeRepositoryV1SavePut**](ProductsAttributesAttributeCodeApi.md#catalogProductAttributeRepositoryV1SavePut) | **PUT** /V1/products/attributes/{attributeCode} | products/attributes/{attributeCode} |


<a id="catalogProductAttributeRepositoryV1DeleteByIdDelete"></a>
# **catalogProductAttributeRepositoryV1DeleteByIdDelete**
> Boolean catalogProductAttributeRepositoryV1DeleteByIdDelete(attributeCode)

products/attributes/{attributeCode}

Delete Attribute by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributesAttributeCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributesAttributeCodeApi apiInstance = new ProductsAttributesAttributeCodeApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    try {
      Boolean result = apiInstance.catalogProductAttributeRepositoryV1DeleteByIdDelete(attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributesAttributeCodeApi#catalogProductAttributeRepositoryV1DeleteByIdDelete");
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
| **attributeCode** | **String**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="catalogProductAttributeRepositoryV1GetGet"></a>
# **catalogProductAttributeRepositoryV1GetGet**
> CatalogDataProductAttributeInterface catalogProductAttributeRepositoryV1GetGet(attributeCode)

products/attributes/{attributeCode}

Retrieve specific attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributesAttributeCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributesAttributeCodeApi apiInstance = new ProductsAttributesAttributeCodeApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    try {
      CatalogDataProductAttributeInterface result = apiInstance.catalogProductAttributeRepositoryV1GetGet(attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributesAttributeCodeApi#catalogProductAttributeRepositoryV1GetGet");
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
| **attributeCode** | **String**|  | |

### Return type

[**CatalogDataProductAttributeInterface**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="catalogProductAttributeRepositoryV1SavePut"></a>
# **catalogProductAttributeRepositoryV1SavePut**
> CatalogDataProductAttributeInterface catalogProductAttributeRepositoryV1SavePut(attributeCode, catalogProductAttributeRepositoryV1SavePostRequest)

products/attributes/{attributeCode}

Save attribute data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributesAttributeCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributesAttributeCodeApi apiInstance = new ProductsAttributesAttributeCodeApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    CatalogProductAttributeRepositoryV1SavePostRequest catalogProductAttributeRepositoryV1SavePostRequest = new CatalogProductAttributeRepositoryV1SavePostRequest(); // CatalogProductAttributeRepositoryV1SavePostRequest | 
    try {
      CatalogDataProductAttributeInterface result = apiInstance.catalogProductAttributeRepositoryV1SavePut(attributeCode, catalogProductAttributeRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributesAttributeCodeApi#catalogProductAttributeRepositoryV1SavePut");
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
| **attributeCode** | **String**|  | |
| **catalogProductAttributeRepositoryV1SavePostRequest** | [**CatalogProductAttributeRepositoryV1SavePostRequest**](CatalogProductAttributeRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**CatalogDataProductAttributeInterface**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |


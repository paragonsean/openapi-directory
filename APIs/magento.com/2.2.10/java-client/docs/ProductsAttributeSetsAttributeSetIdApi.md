# ProductsAttributeSetsAttributeSetIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogAttributeSetRepositoryV1DeleteByIdDelete**](ProductsAttributeSetsAttributeSetIdApi.md#catalogAttributeSetRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/attribute-sets/{attributeSetId} | products/attribute-sets/{attributeSetId} |
| [**catalogAttributeSetRepositoryV1GetGet**](ProductsAttributeSetsAttributeSetIdApi.md#catalogAttributeSetRepositoryV1GetGet) | **GET** /V1/products/attribute-sets/{attributeSetId} | products/attribute-sets/{attributeSetId} |
| [**catalogAttributeSetRepositoryV1SavePut**](ProductsAttributeSetsAttributeSetIdApi.md#catalogAttributeSetRepositoryV1SavePut) | **PUT** /V1/products/attribute-sets/{attributeSetId} | products/attribute-sets/{attributeSetId} |


<a id="catalogAttributeSetRepositoryV1DeleteByIdDelete"></a>
# **catalogAttributeSetRepositoryV1DeleteByIdDelete**
> Boolean catalogAttributeSetRepositoryV1DeleteByIdDelete(attributeSetId)

products/attribute-sets/{attributeSetId}

Remove attribute set by given ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributeSetsAttributeSetIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributeSetsAttributeSetIdApi apiInstance = new ProductsAttributeSetsAttributeSetIdApi(defaultClient);
    Integer attributeSetId = 56; // Integer | 
    try {
      Boolean result = apiInstance.catalogAttributeSetRepositoryV1DeleteByIdDelete(attributeSetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributeSetsAttributeSetIdApi#catalogAttributeSetRepositoryV1DeleteByIdDelete");
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
| **attributeSetId** | **Integer**|  | |

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

<a id="catalogAttributeSetRepositoryV1GetGet"></a>
# **catalogAttributeSetRepositoryV1GetGet**
> EavDataAttributeSetInterface catalogAttributeSetRepositoryV1GetGet(attributeSetId)

products/attribute-sets/{attributeSetId}

Retrieve attribute set information based on given ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributeSetsAttributeSetIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributeSetsAttributeSetIdApi apiInstance = new ProductsAttributeSetsAttributeSetIdApi(defaultClient);
    Integer attributeSetId = 56; // Integer | 
    try {
      EavDataAttributeSetInterface result = apiInstance.catalogAttributeSetRepositoryV1GetGet(attributeSetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributeSetsAttributeSetIdApi#catalogAttributeSetRepositoryV1GetGet");
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
| **attributeSetId** | **Integer**|  | |

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

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

<a id="catalogAttributeSetRepositoryV1SavePut"></a>
# **catalogAttributeSetRepositoryV1SavePut**
> EavDataAttributeSetInterface catalogAttributeSetRepositoryV1SavePut(attributeSetId, eavAttributeSetRepositoryV1SavePutRequest)

products/attribute-sets/{attributeSetId}

Save attribute set data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsAttributeSetsAttributeSetIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsAttributeSetsAttributeSetIdApi apiInstance = new ProductsAttributeSetsAttributeSetIdApi(defaultClient);
    String attributeSetId = "attributeSetId_example"; // String | 
    EavAttributeSetRepositoryV1SavePutRequest eavAttributeSetRepositoryV1SavePutRequest = new EavAttributeSetRepositoryV1SavePutRequest(); // EavAttributeSetRepositoryV1SavePutRequest | 
    try {
      EavDataAttributeSetInterface result = apiInstance.catalogAttributeSetRepositoryV1SavePut(attributeSetId, eavAttributeSetRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsAttributeSetsAttributeSetIdApi#catalogAttributeSetRepositoryV1SavePut");
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
| **attributeSetId** | **String**|  | |
| **eavAttributeSetRepositoryV1SavePutRequest** | [**EavAttributeSetRepositoryV1SavePutRequest**](EavAttributeSetRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |


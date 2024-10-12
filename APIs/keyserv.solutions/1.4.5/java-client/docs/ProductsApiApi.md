# ProductsApiApi

All URIs are relative to *https://keyserv.solutions*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsApiCount**](ProductsApiApi.md#productsApiCount) | **POST** /v1/ProductsApi/Count |  |
| [**productsApiDeleteProduct**](ProductsApiApi.md#productsApiDeleteProduct) | **DELETE** /v1/ProductsApi/{serial} |  |
| [**productsApiDeleteProduct2**](ProductsApiApi.md#productsApiDeleteProduct2) | **POST** /v1/ProductsApi/{serial} |  |
| [**productsApiFind**](ProductsApiApi.md#productsApiFind) | **POST** /v1/ProductsApi/Find |  |
| [**productsApiList**](ProductsApiApi.md#productsApiList) | **POST** /v1/ProductsApi/List |  |
| [**productsApiPatchProduct**](ProductsApiApi.md#productsApiPatchProduct) | **PATCH** /v1/ProductsApi |  |
| [**productsApiPatchProduct2**](ProductsApiApi.md#productsApiPatchProduct2) | **POST** /v1/ProductsApi |  |
| [**productsApiSave**](ProductsApiApi.md#productsApiSave) | **POST** /v1/ProductsApi/Save |  |


<a id="productsApiCount"></a>
# **productsApiCount**
> ProductsApiCount200Response productsApiCount(productsApiCountRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    ProductsApiApi apiInstance = new ProductsApiApi(defaultClient);
    ProductsApiCountRequest productsApiCountRequest = new ProductsApiCountRequest(); // ProductsApiCountRequest | 
    try {
      ProductsApiCount200Response result = apiInstance.productsApiCount(productsApiCountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApiApi#productsApiCount");
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
| **productsApiCountRequest** | [**ProductsApiCountRequest**](ProductsApiCountRequest.md)|  | |

### Return type

[**ProductsApiCount200Response**](ProductsApiCount200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="productsApiDeleteProduct"></a>
# **productsApiDeleteProduct**
> productsApiDeleteProduct(xApiKey, serial)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    ProductsApiApi apiInstance = new ProductsApiApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | 
    String serial = "serial_example"; // String | 
    try {
      apiInstance.productsApiDeleteProduct(xApiKey, serial);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApiApi#productsApiDeleteProduct");
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
| **xApiKey** | **String**|  | |
| **serial** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="productsApiDeleteProduct2"></a>
# **productsApiDeleteProduct2**
> productsApiDeleteProduct2(xApiKey, serial)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    ProductsApiApi apiInstance = new ProductsApiApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | 
    String serial = "serial_example"; // String | 
    try {
      apiInstance.productsApiDeleteProduct2(xApiKey, serial);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApiApi#productsApiDeleteProduct2");
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
| **xApiKey** | **String**|  | |
| **serial** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="productsApiFind"></a>
# **productsApiFind**
> ProductsApiFind200Response productsApiFind(productsApiFindRequest, page)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    ProductsApiApi apiInstance = new ProductsApiApi(defaultClient);
    ProductsApiFindRequest productsApiFindRequest = new ProductsApiFindRequest(); // ProductsApiFindRequest | 
    Integer page = 56; // Integer | 
    try {
      ProductsApiFind200Response result = apiInstance.productsApiFind(productsApiFindRequest, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApiApi#productsApiFind");
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
| **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | |
| **page** | **Integer**|  | [optional] |

### Return type

[**ProductsApiFind200Response**](ProductsApiFind200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="productsApiList"></a>
# **productsApiList**
> List&lt;ProductView&gt; productsApiList(productsApiCountRequest, page)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    ProductsApiApi apiInstance = new ProductsApiApi(defaultClient);
    ProductsApiCountRequest productsApiCountRequest = new ProductsApiCountRequest(); // ProductsApiCountRequest | 
    Integer page = 56; // Integer | 
    try {
      List<ProductView> result = apiInstance.productsApiList(productsApiCountRequest, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApiApi#productsApiList");
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
| **productsApiCountRequest** | [**ProductsApiCountRequest**](ProductsApiCountRequest.md)|  | |
| **page** | **Integer**|  | [optional] |

### Return type

[**List&lt;ProductView&gt;**](ProductView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="productsApiPatchProduct"></a>
# **productsApiPatchProduct**
> productsApiPatchProduct(productsApiPatchProduct2Request)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    ProductsApiApi apiInstance = new ProductsApiApi(defaultClient);
    ProductsApiPatchProduct2Request productsApiPatchProduct2Request = new ProductsApiPatchProduct2Request(); // ProductsApiPatchProduct2Request | 
    try {
      apiInstance.productsApiPatchProduct(productsApiPatchProduct2Request);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApiApi#productsApiPatchProduct");
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
| **productsApiPatchProduct2Request** | [**ProductsApiPatchProduct2Request**](ProductsApiPatchProduct2Request.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="productsApiPatchProduct2"></a>
# **productsApiPatchProduct2**
> productsApiPatchProduct2(productsApiPatchProduct2Request)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    ProductsApiApi apiInstance = new ProductsApiApi(defaultClient);
    ProductsApiPatchProduct2Request productsApiPatchProduct2Request = new ProductsApiPatchProduct2Request(); // ProductsApiPatchProduct2Request | 
    try {
      apiInstance.productsApiPatchProduct2(productsApiPatchProduct2Request);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApiApi#productsApiPatchProduct2");
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
| **productsApiPatchProduct2Request** | [**ProductsApiPatchProduct2Request**](ProductsApiPatchProduct2Request.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="productsApiSave"></a>
# **productsApiSave**
> ProductsApiFind200Response productsApiSave(productsApiPatchProduct2Request)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    ProductsApiApi apiInstance = new ProductsApiApi(defaultClient);
    ProductsApiPatchProduct2Request productsApiPatchProduct2Request = new ProductsApiPatchProduct2Request(); // ProductsApiPatchProduct2Request | 
    try {
      ProductsApiFind200Response result = apiInstance.productsApiSave(productsApiPatchProduct2Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApiApi#productsApiSave");
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
| **productsApiPatchProduct2Request** | [**ProductsApiPatchProduct2Request**](ProductsApiPatchProduct2Request.md)|  | |

### Return type

[**ProductsApiFind200Response**](ProductsApiFind200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |


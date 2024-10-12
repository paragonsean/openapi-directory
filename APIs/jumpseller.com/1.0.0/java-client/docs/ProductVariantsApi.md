# ProductVariantsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsIdVariantsCountJsonGet**](ProductVariantsApi.md#productsIdVariantsCountJsonGet) | **GET** /products/{id}/variants/count.json | Count all Product Variants. |
| [**productsIdVariantsJsonGet**](ProductVariantsApi.md#productsIdVariantsJsonGet) | **GET** /products/{id}/variants.json | Retrieve all Product Variants. |
| [**productsIdVariantsJsonPost**](ProductVariantsApi.md#productsIdVariantsJsonPost) | **POST** /products/{id}/variants.json | Create a new Product Variant. |
| [**productsIdVariantsVariantIdJsonGet**](ProductVariantsApi.md#productsIdVariantsVariantIdJsonGet) | **GET** /products/{id}/variants/{variant_id}.json | Retrieve a single Product Variant. |
| [**productsIdVariantsVariantIdJsonPut**](ProductVariantsApi.md#productsIdVariantsVariantIdJsonPut) | **PUT** /products/{id}/variants/{variant_id}.json | Modify an existing Product Variant. |


<a id="productsIdVariantsCountJsonGet"></a>
# **productsIdVariantsCountJsonGet**
> Count productsIdVariantsCountJsonGet(login, authtoken, id)

Count all Product Variants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductVariantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductVariantsApi apiInstance = new ProductVariantsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      Count result = apiInstance.productsIdVariantsCountJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductVariantsApi#productsIdVariantsCountJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| ID of the Product | |

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product Not Found. |  -  |

<a id="productsIdVariantsJsonGet"></a>
# **productsIdVariantsJsonGet**
> List&lt;Variant&gt; productsIdVariantsJsonGet(login, authtoken, id)

Retrieve all Product Variants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductVariantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductVariantsApi apiInstance = new ProductVariantsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      List<Variant> result = apiInstance.productsIdVariantsJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductVariantsApi#productsIdVariantsJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| ID of the Product | |

### Return type

[**List&lt;Variant&gt;**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product Not Found. |  -  |

<a id="productsIdVariantsJsonPost"></a>
# **productsIdVariantsJsonPost**
> Variant productsIdVariantsJsonPost(login, authtoken, id, variantEdit)

Create a new Product Variant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductVariantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductVariantsApi apiInstance = new ProductVariantsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    VariantEdit variantEdit = new VariantEdit(); // VariantEdit | Product Variant parameters.
    try {
      Variant result = apiInstance.productsIdVariantsJsonPost(login, authtoken, id, variantEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductVariantsApi#productsIdVariantsJsonPost");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Product | |
| **variantEdit** | [**VariantEdit**](VariantEdit.md)| Product Variant parameters. | |

### Return type

[**Variant**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product Not Found. |  -  |

<a id="productsIdVariantsVariantIdJsonGet"></a>
# **productsIdVariantsVariantIdJsonGet**
> Variant productsIdVariantsVariantIdJsonGet(login, authtoken, id, variantId)

Retrieve a single Product Variant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductVariantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductVariantsApi apiInstance = new ProductVariantsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer variantId = 56; // Integer | Id of the Product Variant
    try {
      Variant result = apiInstance.productsIdVariantsVariantIdJsonGet(login, authtoken, id, variantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductVariantsApi#productsIdVariantsVariantIdJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Product | |
| **variantId** | **Integer**| Id of the Product Variant | |

### Return type

[**Variant**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product Not Found. |  -  |

<a id="productsIdVariantsVariantIdJsonPut"></a>
# **productsIdVariantsVariantIdJsonPut**
> Variant productsIdVariantsVariantIdJsonPut(login, authtoken, id, variantId, variantEdit)

Modify an existing Product Variant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductVariantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductVariantsApi apiInstance = new ProductVariantsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer variantId = 56; // Integer | Id of the Product Variant
    VariantEdit variantEdit = new VariantEdit(); // VariantEdit | Product Variant parameters to change
    try {
      Variant result = apiInstance.productsIdVariantsVariantIdJsonPut(login, authtoken, id, variantId, variantEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductVariantsApi#productsIdVariantsVariantIdJsonPut");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Product | |
| **variantId** | **Integer**| Id of the Product Variant | |
| **variantEdit** | [**VariantEdit**](VariantEdit.md)| Product Variant parameters to change | |

### Return type

[**Variant**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Product Not Found. |  -  |


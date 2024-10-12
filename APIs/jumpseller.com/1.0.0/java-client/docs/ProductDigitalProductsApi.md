# ProductDigitalProductsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsIdDigitalProductsCountJsonGet**](ProductDigitalProductsApi.md#productsIdDigitalProductsCountJsonGet) | **GET** /products/{id}/digital_products/count.json | Count all Product DigitalProducts. |
| [**productsIdDigitalProductsDigitalProductIdJsonDelete**](ProductDigitalProductsApi.md#productsIdDigitalProductsDigitalProductIdJsonDelete) | **DELETE** /products/{id}/digital_products/{digital_product_id}.json | Delete a Product DigitalProduct. |
| [**productsIdDigitalProductsDigitalProductIdJsonGet**](ProductDigitalProductsApi.md#productsIdDigitalProductsDigitalProductIdJsonGet) | **GET** /products/{id}/digital_products/{digital_product_id}.json | Retrieve a single Product DigitalProduct. |
| [**productsIdDigitalProductsJsonGet**](ProductDigitalProductsApi.md#productsIdDigitalProductsJsonGet) | **GET** /products/{id}/digital_products.json | Retrieve all Product DigitalProducts. |
| [**productsIdDigitalProductsJsonPost**](ProductDigitalProductsApi.md#productsIdDigitalProductsJsonPost) | **POST** /products/{id}/digital_products.json | Create a new Product DigitalProduct. |


<a id="productsIdDigitalProductsCountJsonGet"></a>
# **productsIdDigitalProductsCountJsonGet**
> Count productsIdDigitalProductsCountJsonGet(login, authtoken, id)

Count all Product DigitalProducts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDigitalProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductDigitalProductsApi apiInstance = new ProductDigitalProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      Count result = apiInstance.productsIdDigitalProductsCountJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDigitalProductsApi#productsIdDigitalProductsCountJsonGet");
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

<a id="productsIdDigitalProductsDigitalProductIdJsonDelete"></a>
# **productsIdDigitalProductsDigitalProductIdJsonDelete**
> String productsIdDigitalProductsDigitalProductIdJsonDelete(login, authtoken, id, digitalProductId)

Delete a Product DigitalProduct.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDigitalProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductDigitalProductsApi apiInstance = new ProductDigitalProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer digitalProductId = 56; // Integer | Id of the Product DigitalProduct
    try {
      String result = apiInstance.productsIdDigitalProductsDigitalProductIdJsonDelete(login, authtoken, id, digitalProductId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDigitalProductsApi#productsIdDigitalProductsDigitalProductIdJsonDelete");
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
| **digitalProductId** | **Integer**| Id of the Product DigitalProduct | |

### Return type

**String**

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

<a id="productsIdDigitalProductsDigitalProductIdJsonGet"></a>
# **productsIdDigitalProductsDigitalProductIdJsonGet**
> DigitalProduct productsIdDigitalProductsDigitalProductIdJsonGet(login, authtoken, id, digitalProductId)

Retrieve a single Product DigitalProduct.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDigitalProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductDigitalProductsApi apiInstance = new ProductDigitalProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    Integer digitalProductId = 56; // Integer | Id of the Product DigitalProduct
    try {
      DigitalProduct result = apiInstance.productsIdDigitalProductsDigitalProductIdJsonGet(login, authtoken, id, digitalProductId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDigitalProductsApi#productsIdDigitalProductsDigitalProductIdJsonGet");
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
| **digitalProductId** | **Integer**| Id of the Product DigitalProduct | |

### Return type

[**DigitalProduct**](DigitalProduct.md)

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

<a id="productsIdDigitalProductsJsonGet"></a>
# **productsIdDigitalProductsJsonGet**
> List&lt;DigitalProduct&gt; productsIdDigitalProductsJsonGet(login, authtoken, id)

Retrieve all Product DigitalProducts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDigitalProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductDigitalProductsApi apiInstance = new ProductDigitalProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    try {
      List<DigitalProduct> result = apiInstance.productsIdDigitalProductsJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDigitalProductsApi#productsIdDigitalProductsJsonGet");
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

[**List&lt;DigitalProduct&gt;**](DigitalProduct.md)

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

<a id="productsIdDigitalProductsJsonPost"></a>
# **productsIdDigitalProductsJsonPost**
> DigitalProduct productsIdDigitalProductsJsonPost(login, authtoken, id, digitalProductEdit)

Create a new Product DigitalProduct.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDigitalProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductDigitalProductsApi apiInstance = new ProductDigitalProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    DigitalProductEdit digitalProductEdit = new DigitalProductEdit(); // DigitalProductEdit | Product DigitalProduct parameters.
    try {
      DigitalProduct result = apiInstance.productsIdDigitalProductsJsonPost(login, authtoken, id, digitalProductEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDigitalProductsApi#productsIdDigitalProductsJsonPost");
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
| **digitalProductEdit** | [**DigitalProductEdit**](DigitalProductEdit.md)| Product DigitalProduct parameters. | |

### Return type

[**DigitalProduct**](DigitalProduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


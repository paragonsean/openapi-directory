# ProductsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsAfterIdJsonGet**](ProductsApi.md#productsAfterIdJsonGet) | **GET** /products/after/{id}.json | Retrieves Products after the given id. |
| [**productsCategoryCategoryIdCountJsonGet**](ProductsApi.md#productsCategoryCategoryIdCountJsonGet) | **GET** /products/category/{category_id}/count.json | Count Products filtered by category. |
| [**productsCategoryCategoryIdJsonGet**](ProductsApi.md#productsCategoryCategoryIdJsonGet) | **GET** /products/category/{category_id}.json | Retrieve Products filtered by category. |
| [**productsCountJsonGet**](ProductsApi.md#productsCountJsonGet) | **GET** /products/count.json | Count all Products. |
| [**productsIdJsonDelete**](ProductsApi.md#productsIdJsonDelete) | **DELETE** /products/{id}.json | Delete an existing Product. |
| [**productsIdJsonGet**](ProductsApi.md#productsIdJsonGet) | **GET** /products/{id}.json | Retrieve a single Product. |
| [**productsIdJsonPut**](ProductsApi.md#productsIdJsonPut) | **PUT** /products/{id}.json | Modify an existing Product. |
| [**productsJsonGet**](ProductsApi.md#productsJsonGet) | **GET** /products.json | Retrieve all Products. |
| [**productsJsonPost**](ProductsApi.md#productsJsonPost) | **POST** /products.json | Create a new Product. |
| [**productsSearchJsonGet**](ProductsApi.md#productsSearchJsonGet) | **GET** /products/search.json | Retrieve a Product List from a query. |
| [**productsStatusStatusCountJsonGet**](ProductsApi.md#productsStatusStatusCountJsonGet) | **GET** /products/status/{status}/count.json | Count Products filtered by status. |
| [**productsStatusStatusJsonGet**](ProductsApi.md#productsStatusStatusJsonGet) | **GET** /products/status/{status}.json | Retrieve Products filtered by status. |


<a id="productsAfterIdJsonGet"></a>
# **productsAfterIdJsonGet**
> List&lt;Product&gt; productsAfterIdJsonGet(login, authtoken, id, locale)

Retrieves Products after the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    String locale = "locale_example"; // String | Locale code of the translation
    try {
      List<Product> result = apiInstance.productsAfterIdJsonGet(login, authtoken, id, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsAfterIdJsonGet");
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
| **locale** | **String**| Locale code of the translation | [optional] |

### Return type

[**List&lt;Product&gt;**](Product.md)

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

<a id="productsCategoryCategoryIdCountJsonGet"></a>
# **productsCategoryCategoryIdCountJsonGet**
> Count productsCategoryCategoryIdCountJsonGet(login, authtoken, categoryId, locale)

Count Products filtered by category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer categoryId = 56; // Integer | Category ID of the Product used as filter
    String locale = "locale_example"; // String | Locale code of the translation
    try {
      Count result = apiInstance.productsCategoryCategoryIdCountJsonGet(login, authtoken, categoryId, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsCategoryCategoryIdCountJsonGet");
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
| **categoryId** | **Integer**| Category ID of the Product used as filter | |
| **locale** | **String**| Locale code of the translation | [optional] |

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
| **404** | Category Not Found. |  -  |

<a id="productsCategoryCategoryIdJsonGet"></a>
# **productsCategoryCategoryIdJsonGet**
> List&lt;Product&gt; productsCategoryCategoryIdJsonGet(login, authtoken, categoryId, locale)

Retrieve Products filtered by category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer categoryId = 56; // Integer | Category ID of the Product used as filter
    String locale = "locale_example"; // String | Locale code of the translation
    try {
      List<Product> result = apiInstance.productsCategoryCategoryIdJsonGet(login, authtoken, categoryId, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsCategoryCategoryIdJsonGet");
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
| **categoryId** | **Integer**| Category ID of the Product used as filter | |
| **locale** | **String**| Locale code of the translation | [optional] |

### Return type

[**List&lt;Product&gt;**](Product.md)

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

<a id="productsCountJsonGet"></a>
# **productsCountJsonGet**
> Count productsCountJsonGet(login, authtoken)

Count all Products.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    try {
      Count result = apiInstance.productsCountJsonGet(login, authtoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsCountJsonGet");
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

<a id="productsIdJsonDelete"></a>
# **productsIdJsonDelete**
> String productsIdJsonDelete(login, authtoken, id)

Delete an existing Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    try {
      String result = apiInstance.productsIdJsonDelete(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsIdJsonDelete");
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

<a id="productsIdJsonGet"></a>
# **productsIdJsonGet**
> Product productsIdJsonGet(login, authtoken, id, locale)

Retrieve a single Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | ID of the Product
    String locale = "locale_example"; // String | Locale code of the translation
    try {
      Product result = apiInstance.productsIdJsonGet(login, authtoken, id, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsIdJsonGet");
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
| **locale** | **String**| Locale code of the translation | [optional] |

### Return type

[**Product**](Product.md)

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

<a id="productsIdJsonPut"></a>
# **productsIdJsonPut**
> Product productsIdJsonPut(login, authtoken, id, productEdit, locale)

Modify an existing Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Product
    ProductEdit productEdit = new ProductEdit(); // ProductEdit | Product parameters to change
    String locale = "locale_example"; // String | Locale code of the translation
    try {
      Product result = apiInstance.productsIdJsonPut(login, authtoken, id, productEdit, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsIdJsonPut");
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
| **productEdit** | [**ProductEdit**](ProductEdit.md)| Product parameters to change | |
| **locale** | **String**| Locale code of the translation | [optional] |

### Return type

[**Product**](Product.md)

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

<a id="productsJsonGet"></a>
# **productsJsonGet**
> List&lt;Product&gt; productsJsonGet(login, authtoken, limit, page, locale)

Retrieve all Products.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer limit = 50; // Integer | List restriction
    Integer page = 1; // Integer | List page
    String locale = "locale_example"; // String | Locale code of the translation
    try {
      List<Product> result = apiInstance.productsJsonGet(login, authtoken, limit, page, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsJsonGet");
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
| **limit** | **Integer**| List restriction | [optional] [default to 50] |
| **page** | **Integer**| List page | [optional] [default to 1] |
| **locale** | **String**| Locale code of the translation | [optional] |

### Return type

[**List&lt;Product&gt;**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productsJsonPost"></a>
# **productsJsonPost**
> Product productsJsonPost(login, authtoken, productEdit, locale)

Create a new Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    ProductEdit productEdit = new ProductEdit(); // ProductEdit | Product parameters.
    String locale = "locale_example"; // String | Locale code of the translation
    try {
      Product result = apiInstance.productsJsonPost(login, authtoken, productEdit, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsJsonPost");
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
| **productEdit** | [**ProductEdit**](ProductEdit.md)| Product parameters. | |
| **locale** | **String**| Locale code of the translation | [optional] |

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productsSearchJsonGet"></a>
# **productsSearchJsonGet**
> List&lt;Product&gt; productsSearchJsonGet(login, authtoken, query, locale, fields)

Retrieve a Product List from a query.

Endpoint example:   &#x60;&#x60;&#x60;text https://api.jumpseller.com/v1/products/search.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;XXXXX&amp;query&#x3D;test&amp;fields&#x3D;name,description  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String query = "query_example"; // String | Text to query for the Product
    String locale = "locale_example"; // String | Locale code of the translation
    String fields = "sku"; // String | Comma separated values of the fields to query for the Product
    try {
      List<Product> result = apiInstance.productsSearchJsonGet(login, authtoken, query, locale, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsSearchJsonGet");
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
| **query** | **String**| Text to query for the Product | |
| **locale** | **String**| Locale code of the translation | [optional] |
| **fields** | **String**| Comma separated values of the fields to query for the Product | [optional] [enum: sku, barcode, brand, name, description, variants, option_name, custom_fields, custom_fields_selects] |

### Return type

[**List&lt;Product&gt;**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of products |  -  |
| **404** | Invalid query. |  -  |

<a id="productsStatusStatusCountJsonGet"></a>
# **productsStatusStatusCountJsonGet**
> Count productsStatusStatusCountJsonGet(login, authtoken, status, locale)

Count Products filtered by status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String status = "available"; // String | Status of the Product used as filter
    String locale = "locale_example"; // String | Locale code of the translation
    try {
      Count result = apiInstance.productsStatusStatusCountJsonGet(login, authtoken, status, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsStatusStatusCountJsonGet");
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
| **status** | **String**| Status of the Product used as filter | [enum: available, not-available, disabled] |
| **locale** | **String**| Locale code of the translation | [optional] |

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
| **404** | Status Invalid. |  -  |

<a id="productsStatusStatusJsonGet"></a>
# **productsStatusStatusJsonGet**
> List&lt;Product&gt; productsStatusStatusJsonGet(login, authtoken, status, locale)

Retrieve Products filtered by status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String status = "available"; // String | Status of the Product used as filter
    String locale = "locale_example"; // String | Locale code of the translation
    try {
      List<Product> result = apiInstance.productsStatusStatusJsonGet(login, authtoken, status, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsStatusStatusJsonGet");
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
| **status** | **String**| Status of the Product used as filter | [enum: available, not-available, disabled] |
| **locale** | **String**| Locale code of the translation | [optional] |

### Return type

[**List&lt;Product&gt;**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Status Invalid. |  -  |


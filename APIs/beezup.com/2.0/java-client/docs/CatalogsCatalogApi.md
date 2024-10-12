# CatalogsCatalogApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogChangeCatalogColumnUserName**](CatalogsCatalogApi.md#catalogChangeCatalogColumnUserName) | **POST** /v2/user/catalogs/{storeId}/catalogColumns/{columnId}/rename | Change Catalog Column User Name |
| [**catalogChangeCustomColumnExpression**](CatalogsCatalogApi.md#catalogChangeCustomColumnExpression) | **PUT** /v2/user/catalogs/{storeId}/customColumns/{columnId}/expression | Change custom column expression |
| [**catalogChangeCustomColumnUserName**](CatalogsCatalogApi.md#catalogChangeCustomColumnUserName) | **POST** /v2/user/catalogs/{storeId}/customColumns/{columnId}/rename | Change Custom Column User Name |
| [**catalogComputeExpression**](CatalogsCatalogApi.md#catalogComputeExpression) | **POST** /v2/user/catalogs/{storeId}/customColumns/computeExpression | Compute the expression for this catalog. |
| [**catalogDeleteCustomColumn**](CatalogsCatalogApi.md#catalogDeleteCustomColumn) | **DELETE** /v2/user/catalogs/{storeId}/customColumns/{columnId} | Delete custom column |
| [**catalogGetCatalogColumns**](CatalogsCatalogApi.md#catalogGetCatalogColumns) | **GET** /v2/user/catalogs/{storeId}/catalogColumns | Get catalog column list |
| [**catalogGetCategories**](CatalogsCatalogApi.md#catalogGetCategories) | **GET** /v2/user/catalogs/{storeId}/categories | Get category list |
| [**catalogGetCustomColumnExpression**](CatalogsCatalogApi.md#catalogGetCustomColumnExpression) | **GET** /v2/user/catalogs/{storeId}/customColumns/{columnId}/expression | Get the encrypted custom column expression |
| [**catalogGetCustomColumns**](CatalogsCatalogApi.md#catalogGetCustomColumns) | **GET** /v2/user/catalogs/{storeId}/customColumns | Get custom column list |
| [**catalogGetProductByProductId**](CatalogsCatalogApi.md#catalogGetProductByProductId) | **GET** /v2/user/catalogs/{storeId}/products/{productId} | Get product by ProductId |
| [**catalogGetProductBySku**](CatalogsCatalogApi.md#catalogGetProductBySku) | **GET** /v2/user/catalogs/{storeId}/products | Get product by Sku |
| [**catalogGetProducts**](CatalogsCatalogApi.md#catalogGetProducts) | **POST** /v2/user/catalogs/{storeId}/products/list | Get product list |
| [**catalogGetRandomProducts**](CatalogsCatalogApi.md#catalogGetRandomProducts) | **GET** /v2/user/catalogs/{storeId}/products/random | Get random product list |
| [**catalogSaveCustomColumn**](CatalogsCatalogApi.md#catalogSaveCustomColumn) | **PUT** /v2/user/catalogs/{storeId}/customColumns/{columnId} | Create or replace a custom column |
| [**catalogStoreIndex**](CatalogsCatalogApi.md#catalogStoreIndex) | **GET** /v2/user/catalogs/{storeId} | Get the index of the catalog API for this store |
| [**importationGetManualUpdateLastInputConfig**](CatalogsCatalogApi.md#importationGetManualUpdateLastInputConfig) | **GET** /v2/user/catalogs/{storeId}/inputConfiguration | Get the last input configuration |


<a id="catalogChangeCatalogColumnUserName"></a>
# **catalogChangeCatalogColumnUserName**
> catalogChangeCatalogColumnUserName(storeId, columnId, changeUserColumnNameRequest)

Change Catalog Column User Name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String columnId = "columnId_example"; // String | The catalog column identifier
    ChangeUserColumnNameRequest changeUserColumnNameRequest = new ChangeUserColumnNameRequest(); // ChangeUserColumnNameRequest | 
    try {
      apiInstance.catalogChangeCatalogColumnUserName(storeId, columnId, changeUserColumnNameRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogChangeCatalogColumnUserName");
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
| **storeId** | **String**| Your store identifier | |
| **columnId** | **String**| The catalog column identifier | |
| **changeUserColumnNameRequest** | [**ChangeUserColumnNameRequest**](ChangeUserColumnNameRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Catalog column user name changed |  -  |
| **400** | When a user column name is duplicate. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when a catalog column is not found. |  -  |
| **409** | A catalog importation is already in progress! |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogChangeCustomColumnExpression"></a>
# **catalogChangeCustomColumnExpression**
> catalogChangeCustomColumnExpression(storeId, columnId, changeCustomColumnExpressionRequest)

Change custom column expression

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String columnId = "columnId_example"; // String | The custom column identifier
    ChangeCustomColumnExpressionRequest changeCustomColumnExpressionRequest = new ChangeCustomColumnExpressionRequest(); // ChangeCustomColumnExpressionRequest | 
    try {
      apiInstance.catalogChangeCustomColumnExpression(storeId, columnId, changeCustomColumnExpressionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogChangeCustomColumnExpression");
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
| **storeId** | **String**| Your store identifier | |
| **columnId** | **String**| The custom column identifier | |
| **changeCustomColumnExpressionRequest** | [**ChangeCustomColumnExpressionRequest**](ChangeCustomColumnExpressionRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Custom column expression saved |  -  |
| **403** | Occurs when the user try to change a custom column related to a Category. If you want to change this custom column expression you have to make a new manual importation. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when a catalog custom column is not found. |  -  |
| **409** | A catalog importation is already in progress! |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogChangeCustomColumnUserName"></a>
# **catalogChangeCustomColumnUserName**
> catalogChangeCustomColumnUserName(storeId, columnId, changeUserColumnNameRequest)

Change Custom Column User Name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String columnId = "columnId_example"; // String | The custom column identifier
    ChangeUserColumnNameRequest changeUserColumnNameRequest = new ChangeUserColumnNameRequest(); // ChangeUserColumnNameRequest | 
    try {
      apiInstance.catalogChangeCustomColumnUserName(storeId, columnId, changeUserColumnNameRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogChangeCustomColumnUserName");
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
| **storeId** | **String**| Your store identifier | |
| **columnId** | **String**| The custom column identifier | |
| **changeUserColumnNameRequest** | [**ChangeUserColumnNameRequest**](ChangeUserColumnNameRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Custom column renamed |  -  |
| **400** | When a user column name is duplicate. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when a catalog column is not found. |  -  |
| **409** | A catalog importation is already in progress! |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogComputeExpression"></a>
# **catalogComputeExpression**
> String catalogComputeExpression(storeId, computeExpressionRequest)

Compute the expression for this catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    ComputeExpressionRequest computeExpressionRequest = new ComputeExpressionRequest(); // ComputeExpressionRequest | 
    try {
      String result = apiInstance.catalogComputeExpression(storeId, computeExpressionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogComputeExpression");
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
| **storeId** | **String**| Your store identifier | |
| **computeExpressionRequest** | [**ComputeExpressionRequest**](ComputeExpressionRequest.md)|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Compute an expression |  -  |
| **400** | Occurs when the expression cannot be computed |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogDeleteCustomColumn"></a>
# **catalogDeleteCustomColumn**
> catalogDeleteCustomColumn(storeId, columnId)

Delete custom column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String columnId = "columnId_example"; // String | The custom column identifier
    try {
      apiInstance.catalogDeleteCustomColumn(storeId, columnId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogDeleteCustomColumn");
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
| **storeId** | **String**| Your store identifier | |
| **columnId** | **String**| The custom column identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Custom column deleted |  -  |
| **403** | Occurs when the parent category is not found. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. |  -  |
| **409** | When a catalog importation is already in progress! |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogGetCatalogColumns"></a>
# **catalogGetCatalogColumns**
> CatalogColumnList catalogGetCatalogColumns(storeId)

Get catalog column list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      CatalogColumnList result = apiInstance.catalogGetCatalogColumns(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogGetCatalogColumns");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**CatalogColumnList**](CatalogColumnList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog column list |  -  |
| **404** | StoreId not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogGetCategories"></a>
# **catalogGetCategories**
> CategoryList catalogGetCategories(storeId, acceptEncoding)

Get category list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    List<String> acceptEncoding = Arrays.asList(); // List<String> | Indicates that the client accepts that the response will be compressed to reduce traffic size.
    try {
      CategoryList result = apiInstance.catalogGetCategories(storeId, acceptEncoding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogGetCategories");
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
| **storeId** | **String**| Your store identifier | |
| **acceptEncoding** | [**List&lt;String&gt;**](String.md)| Indicates that the client accepts that the response will be compressed to reduce traffic size. | |

### Return type

[**CategoryList**](CategoryList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Categories |  * Content-Encoding - Indicates the compression use in the response <br>  |
| **404** | StoreId not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogGetCustomColumnExpression"></a>
# **catalogGetCustomColumnExpression**
> String catalogGetCustomColumnExpression(storeId, columnId)

Get the encrypted custom column expression

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String columnId = "columnId_example"; // String | The custom column identifier
    try {
      String result = apiInstance.catalogGetCustomColumnExpression(storeId, columnId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogGetCustomColumnExpression");
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
| **storeId** | **String**| Your store identifier | |
| **columnId** | **String**| The custom column identifier | |

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
| **200** | Encrypted expression |  -  |
| **404** | Occurs when a user tries to work on the wrong store. Occurs when a catalog custom column is not found. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogGetCustomColumns"></a>
# **catalogGetCustomColumns**
> CustomColumnList catalogGetCustomColumns(storeId)

Get custom column list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      CustomColumnList result = apiInstance.catalogGetCustomColumns(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogGetCustomColumns");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**CustomColumnList**](CustomColumnList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom column list |  -  |
| **404** | StoreId not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogGetProductByProductId"></a>
# **catalogGetProductByProductId**
> Product catalogGetProductByProductId(storeId, productId)

Get product by ProductId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String productId = "productId_example"; // String | The product identifier you want to get
    try {
      Product result = apiInstance.catalogGetProductByProductId(storeId, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogGetProductByProductId");
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
| **storeId** | **String**| Your store identifier | |
| **productId** | **String**| The product identifier you want to get | |

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
| **200** | Product |  -  |
| **404** | StoreId not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogGetProductBySku"></a>
# **catalogGetProductBySku**
> Product catalogGetProductBySku(storeId, sku)

Get product by Sku

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String sku = "sku_example"; // String | The product sku you want to get
    try {
      Product result = apiInstance.catalogGetProductBySku(storeId, sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogGetProductBySku");
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
| **storeId** | **String**| Your store identifier | |
| **sku** | **String**| The product sku you want to get | |

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
| **200** | Product |  -  |
| **404** | StoreId or Product not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogGetProducts"></a>
# **catalogGetProducts**
> ProductList catalogGetProducts(storeId, getProductsRequest)

Get product list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    GetProductsRequest getProductsRequest = new GetProductsRequest(); // GetProductsRequest | 
    try {
      ProductList result = apiInstance.catalogGetProducts(storeId, getProductsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogGetProducts");
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
| **storeId** | **String**| Your store identifier | |
| **getProductsRequest** | [**GetProductsRequest**](GetProductsRequest.md)|  | |

### Return type

[**ProductList**](ProductList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product list |  -  |
| **404** | StoreId not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogGetRandomProducts"></a>
# **catalogGetRandomProducts**
> RandomProductList catalogGetRandomProducts(storeId)

Get random product list

We will return 10 products randomly selected with all product values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      RandomProductList result = apiInstance.catalogGetRandomProducts(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogGetRandomProducts");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**RandomProductList**](RandomProductList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Random product list |  -  |
| **404** | StoreId not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogSaveCustomColumn"></a>
# **catalogSaveCustomColumn**
> catalogSaveCustomColumn(storeId, columnId, createCustomColumnRequest)

Create or replace a custom column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String columnId = "columnId_example"; // String | The custom column identifier
    CreateCustomColumnRequest createCustomColumnRequest = new CreateCustomColumnRequest(); // CreateCustomColumnRequest | 
    try {
      apiInstance.catalogSaveCustomColumn(storeId, columnId, createCustomColumnRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogSaveCustomColumn");
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
| **storeId** | **String**| Your store identifier | |
| **columnId** | **String**| The custom column identifier | |
| **createCustomColumnRequest** | [**CreateCustomColumnRequest**](CreateCustomColumnRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Custom column saved |  -  |
| **400** | Occurs when a catalog custom column id is already used by a catalog column. When the catalog custom column count limit has been reached. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. |  -  |
| **409** | A catalog importation is already in progress! |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogStoreIndex"></a>
# **catalogStoreIndex**
> CatalogStoreIndex catalogStoreIndex(storeId)

Get the index of the catalog API for this store

The operation will give you all the operations you will be able to do on this store for this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      CatalogStoreIndex result = apiInstance.catalogStoreIndex(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#catalogStoreIndex");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**CatalogStoreIndex**](CatalogStoreIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The catalog index |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationGetManualUpdateLastInputConfig"></a>
# **importationGetManualUpdateLastInputConfig**
> LastManualImportInputConfiguration importationGetManualUpdateLastInputConfig(storeId)

Get the last input configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsCatalogApi apiInstance = new CatalogsCatalogApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      LastManualImportInputConfiguration result = apiInstance.importationGetManualUpdateLastInputConfig(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsCatalogApi#importationGetManualUpdateLastInputConfig");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**LastManualImportInputConfiguration**](LastManualImportInputConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | StoreId or Manual Update last configuration not found |  -  |
| **0** | Occurs when something goes wrong |  -  |


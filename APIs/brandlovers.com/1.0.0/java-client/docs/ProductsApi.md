# ProductsApi

All URIs are relative to *https://api.brandlovers.com/marketplace/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productSkuSellerIdPut**](ProductsApi.md#productSkuSellerIdPut) | **PUT** /product/{skuSellerId} | Update product details |
| [**productsGet**](ProductsApi.md#productsGet) | **GET** /products | Returns a list of products loaded into BrandLovers Marketplace |
| [**productsPost**](ProductsApi.md#productsPost) | **POST** /products | Allows new products from the seller to be loaded into the marketplace |
| [**productsPricesPut**](ProductsApi.md#productsPricesPut) | **PUT** /products/prices | Allows bulk update of product prices. |
| [**productsStatusGet**](ProductsApi.md#productsStatusGet) | **GET** /products/status | Returns seller products status in the marketplace |
| [**productsStatusPut**](ProductsApi.md#productsStatusPut) | **PUT** /products/status | Bulk enable/disable products in the marketplace |
| [**productsStatusSellingGet**](ProductsApi.md#productsStatusSellingGet) | **GET** /products/status/selling | Returns products that are successfully listed for sale. |
| [**productsStocksPut**](ProductsApi.md#productsStocksPut) | **PUT** /products/stocks | Bulk product stock update |


<a id="productSkuSellerIdPut"></a>
# **productSkuSellerIdPut**
> productSkuSellerIdPut(authorization, skuSellerId, body)

Update product details

Update a single product information such as name, brand, attribute, dimension, etc. Please note that data from your request will be merged with existing data. This allows you to easliy update only certain fields without the need to re-inform the other unchanged fields. For example in order to update just the field &#x60;title&#x60; simply send just this field with new information, remaining fields will not be changed. In order to erase an item the field must be informed as its default value, for example in order to erase the &#x60;videos&#x60; field must be sent as videos:[]. The &#x60;skuSellerId&#x60; field is always mandatory in the path and in the product json Object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");
    
    // Configure API key authorization: authorization
    ApiKeyAuth authorization = (ApiKeyAuth) defaultClient.getAuthentication("authorization");
    authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //authorization.setApiKeyPrefix("Token");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String skuSellerId = "skuSellerId_example"; // String | Unique Product Id (SKU) in the seller system that will be updated.
    ProductUpdate body = new ProductUpdate(); // ProductUpdate | New product information.
    try {
      apiInstance.productSkuSellerIdPut(authorization, skuSellerId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productSkuSellerIdPut");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **skuSellerId** | **String**| Unique Product Id (SKU) in the seller system that will be updated. | |
| **body** | [**ProductUpdate**](ProductUpdate.md)| New product information. | |

### Return type

null (empty response body)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **403** | Server refused to process your request. Please check the API SLA and reduce number of requests per second. |  -  |
| **404** | Object not found. |  -  |

<a id="productsGet"></a>
# **productsGet**
> GetProductsResponse productsGet(authorization, offset, limit)

Returns a list of products loaded into BrandLovers Marketplace

Get a list of my products loaded into the Marketplace. This dosen&#39;t means that products are eligible for sale, just that they are loaded in the database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");
    
    // Configure API key authorization: authorization
    ApiKeyAuth authorization = (ApiKeyAuth) defaultClient.getAuthentication("authorization");
    authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //authorization.setApiKeyPrefix("Token");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number of items to retun. Defaults to 100. Max alowed is 200. Use this conjuction with `offset` to paginate across the results.
    try {
      GetProductsResponse result = apiInstance.productsGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsGet");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number of items to retun. Defaults to 100. Max alowed is 200. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetProductsResponse**](GetProductsResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **403** | Server refused to process your request. Please check the API SLA and reduce number of requests per second. |  -  |

<a id="productsPost"></a>
# **productsPost**
> productsPost(authorization, products)

Allows new products from the seller to be loaded into the marketplace

This enpoint to creates new products in the Marketplace using &#x60;skuSellerId&#x60; as a primary key. This enpoint expects a json document with array of products. The server will load each product as an individual item that can be manipulated using your own &#x60;skuSellerId&#x60;. All requests to This endpoint are idenpontent with respect of the &#x60;skuSellerId&#x60;, this means that once a &#x60;skuSellerId&#x60; is created it cannot be re-created using this tool. In order to update use the PUT method with the correct &#x60;skuSellerId&#x60;. You can also use the POST /product to create a single product per request

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    List<Product> products = Arrays.asList(); // List<Product> | JSON with a list of new products to be updloaded to the platform
    try {
      apiInstance.productsPost(authorization, products);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsPost");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **products** | [**List&lt;Product&gt;**](Product.md)| JSON with a list of new products to be updloaded to the platform | |

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
| **200** | Sucess! Server received your request and will start background processing. |  -  |
| **400** | Bad Request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |

<a id="productsPricesPut"></a>
# **productsPricesPut**
> productsPricesPut(authorization, body)

Allows bulk update of product prices.

Allows bulk update of product prices. This endpoint expects a json document with an array of products with the &#x60;skuSellerId&#x60; and the new price. Server will process each new product update individually and will ackwlodge as much updates as possible, even if a single product update fails. After this request you can query product final status with GET /product/status

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    List<SellerItemPrices> body = Arrays.asList(); // List<SellerItemPrices> | Data for bulk product price update
    try {
      apiInstance.productsPricesPut(authorization, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsPricesPut");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **body** | [**List&lt;SellerItemPrices&gt;**](SellerItemPrices.md)| Data for bulk product price update | |

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
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |

<a id="productsStatusGet"></a>
# **productsStatusGet**
> GetSellerProductsStatus productsStatusGet(authorization, offset, limit)

Returns seller products status in the marketplace

Returns a list with seller products status. Please note that this endpoint will not return all details of each product, just the skuSellerId and status. Also please note that this endpoint will return 250 products per call. For full details of a given procuct use GET /product/{skuSellerId}

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number of items to return in this query. Defaults to 250. Maximum 1000. Use this conjuction with `offset` to paginate across the results.
    try {
      GetSellerProductsStatus result = apiInstance.productsStatusGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsStatusGet");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number of items to return in this query. Defaults to 250. Maximum 1000. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetSellerProductsStatus**](GetSellerProductsStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success fetching results. |  -  |
| **403** | Server refused to process your request. Please check the API SLA and reduce number of requests per second. |  -  |

<a id="productsStatusPut"></a>
# **productsStatusPut**
> productsStatusPut(authorization, body)

Bulk enable/disable products in the marketplace

Bulk enable/disable products in the marketplace. This endpoint requires an array of objects with the seller SKU &#x60;skuSellerId&#x60; and boolean value that defines if the product is enabled or not for sale. This endpoint can be used to set a single product or many products.

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    List<ProductStatusUpdate> body = Arrays.asList(); // List<ProductStatusUpdate> | List of seller products with new status information
    try {
      apiInstance.productsStatusPut(authorization, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsStatusPut");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **body** | [**List&lt;ProductStatusUpdate&gt;**](ProductStatusUpdate.md)| List of seller products with new status information | |

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
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |

<a id="productsStatusSellingGet"></a>
# **productsStatusSellingGet**
> GetProductsStatusSelling productsStatusSellingGet(authorization, offset, limit)

Returns products that are successfully listed for sale.

Returns products that are successfully listed for sale.

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
    try {
      GetProductsStatusSelling result = apiInstance.productsStatusSellingGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsStatusSellingGet");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetProductsStatusSelling**](GetProductsStatusSelling.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **403** | Server refused to process your request. Please check the API SLA and reduce number of requests per second. |  -  |

<a id="productsStocksPut"></a>
# **productsStocksPut**
> productsStocksPut(authorization, body)

Bulk product stock update

Bulk product stock update. This endpoint expect a array of products &#x60;skuSellerId&#x60; with new inventory data

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    List<ProductStock> body = Arrays.asList(); // List<ProductStock> | Array of product SKUs.
    try {
      apiInstance.productsStocksPut(authorization, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsStocksPut");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **body** | [**List&lt;ProductStock&gt;**](ProductStock.md)| Array of product SKUs. | |

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
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |


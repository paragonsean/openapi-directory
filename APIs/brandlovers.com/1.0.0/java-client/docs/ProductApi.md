# ProductApi

All URIs are relative to *https://api.brandlovers.com/marketplace/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productPost**](ProductApi.md#productPost) | **POST** /product | Create a new product to the marketplace |
| [**productSkuSellerIdGet**](ProductApi.md#productSkuSellerIdGet) | **GET** /product/{skuSellerId} | Returns details of a single product using the seller &#x60;skuSellerId&#x60; |
| [**productSkuSellerIdPricesPut**](ProductApi.md#productSkuSellerIdPricesPut) | **PUT** /product/{skuSellerId}/prices | Allows seller to update prices of a single SKU |
| [**productSkuSellerIdStatusPut**](ProductApi.md#productSkuSellerIdStatusPut) | **PUT** /product/{skuSellerId}/status | Enable/disable a single product in the Marketplace |
| [**productSkuSellerIdStockPut**](ProductApi.md#productSkuSellerIdStockPut) | **PUT** /product/{skuSellerId}/stock | Update a single product stock |


<a id="productPost"></a>
# **productPost**
> productPost(authorization, product)

Create a new product to the marketplace

Use this enpoint to create a single new product to the Marketplace. This enpoint expects a json document with one product. If you whant to upload multiple products in a single API call use POST /products method. The server will load each product as an individual item that can be manipulated using your own &#x60;skuSellerId&#x60;. This system is idenpontent, this means that once a &#x60;skuSellerId&#x60; is created it cannot be re-created using this tool. In order to update, edit a product use the PUT method with the correct reference to your &#x60;skuSellerId&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Product product = new Product(); // Product | New Produt that will be create
    try {
      apiInstance.productPost(authorization, product);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productPost");
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
| **product** | [**Product**](Product.md)| New Produt that will be create | |

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

<a id="productSkuSellerIdGet"></a>
# **productSkuSellerIdGet**
> GetProduct productSkuSellerIdGet(authorization, skuSellerId)

Returns details of a single product using the seller &#x60;skuSellerId&#x60;

Returns detailed information of a single product with the seller &#x60;skuSellerId&#x60;. This service will return a json document with product detail, status, price, invetory among other infomarion availble in the Brand Lovers marketplace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");
    
    // Configure API key authorization: authorization
    ApiKeyAuth authorization = (ApiKeyAuth) defaultClient.getAuthentication("authorization");
    authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //authorization.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String skuSellerId = "skuSellerId_example"; // String | SKU ID do Lojista.
    try {
      GetProduct result = apiInstance.productSkuSellerIdGet(authorization, skuSellerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productSkuSellerIdGet");
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
| **skuSellerId** | **String**| SKU ID do Lojista. | |

### Return type

[**GetProduct**](GetProduct.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success! |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **403** | Server refused to process your request. Please check the API SLA and reduce number of requests per second. |  -  |
| **404** | Object not found. In general this means a invalid skuSellerId. |  -  |

<a id="productSkuSellerIdPricesPut"></a>
# **productSkuSellerIdPricesPut**
> productSkuSellerIdPricesPut(authorization, skuSellerId, body)

Allows seller to update prices of a single SKU

Allows seller to set the SKU prices (MSRP and/or offer price). All prices must be informed in cents. No commas or periods are accepeted. For example one dollar should be informed as 100. Same as $1,2345.67 must be informed solely as 1234567

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String skuSellerId = "skuSellerId_example"; // String | Product SKU
    ProductPrice body = new ProductPrice(); // ProductPrice | JSON document with the SKU price
    try {
      apiInstance.productSkuSellerIdPricesPut(authorization, skuSellerId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productSkuSellerIdPricesPut");
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
| **skuSellerId** | **String**| Product SKU | |
| **body** | [**ProductPrice**](ProductPrice.md)| JSON document with the SKU price | |

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

<a id="productSkuSellerIdStatusPut"></a>
# **productSkuSellerIdStatusPut**
> productSkuSellerIdStatusPut(authorization, skuSellerId, body)

Enable/disable a single product in the Marketplace

Update product status in the Marketplace. Set to &#x60;true&#x60; to enable, &#x60;false&#x60; to disable sale.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String skuSellerId = "skuSellerId_example"; // String | Unique Product Id (SKU) in the seller system
    SellerItemStatus body = new SellerItemStatus(); // SellerItemStatus | Seller SKU that will be enabled or disabled
    try {
      apiInstance.productSkuSellerIdStatusPut(authorization, skuSellerId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productSkuSellerIdStatusPut");
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
| **skuSellerId** | **String**| Unique Product Id (SKU) in the seller system | |
| **body** | [**SellerItemStatus**](SellerItemStatus.md)| Seller SKU that will be enabled or disabled | |

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

<a id="productSkuSellerIdStockPut"></a>
# **productSkuSellerIdStockPut**
> productSkuSellerIdStockPut(authorization, skuSellerId, body)

Update a single product stock

Update a single product inventory information. Products with zero stock will not be eligible for sale.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String skuSellerId = "skuSellerId_example"; // String | Unique Product Id (SKU) in the seller system that will be updated
    Stock body = new Stock(); // Stock | New product inventory information
    try {
      apiInstance.productSkuSellerIdStockPut(authorization, skuSellerId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productSkuSellerIdStockPut");
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
| **skuSellerId** | **String**| Unique Product Id (SKU) in the seller system that will be updated | |
| **body** | [**Stock**](Stock.md)| New product inventory information | |

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


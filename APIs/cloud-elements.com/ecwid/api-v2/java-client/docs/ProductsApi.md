# ProductsApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProduct**](ProductsApi.md#createProduct) | **POST** /products | Create a new product in eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Product&#39; model are those required to create a new product |
| [**deleteProductById**](ProductsApi.md#deleteProductById) | **DELETE** /products/{id} | Delete a product associated with a given ID from your eCommerce system. Specifying a product associated with a given ID that does not exist will result in an error message |
| [**getProductById**](ProductsApi.md#getProductById) | **GET** /products/{id} | Retrieve a product associated with a given ID from the eCommerce system. Specifying a product with an ID that does not exist will result in an error response |
| [**getProducts**](ProductsApi.md#getProducts) | **GET** /products | Find products in the eCommerce system, using the provided CEQL search expression. The search expression in CEQL is the WHERE clause in a typical SQL query, but without the WHERE keyword.  If no search expression is provided, all records will be retrieved |
| [**updateProductById**](ProductsApi.md#updateProductById) | **PATCH** /products/{id} | Update a product associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the product object will be updated, and those fields not provided will be left alone. Updating a product with a specified ID that does not exist will result in an error response. &lt;p&gt;&lt;strong&gt;Update supports the following fields: sku, quantity, trackQuantity, quantityDelta, warningLimit, name, price, weight, tangible, enabled, fixedShippingRateOnly, fixedShippingRate, description, wholesalePrices, compareAtPrice, productClassId&lt;/strong&gt; |


<a id="createProduct"></a>
# **createProduct**
> Product createProduct(authorization, product)

Create a new product in eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Product&#39; model are those required to create a new product

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    ProductPost product = new ProductPost(); // ProductPost | The product object to be created
    try {
      Product result = apiInstance.createProduct(authorization, product);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#createProduct");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **product** | [**ProductPost**](ProductPost.md)| The product object to be created | |

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="deleteProductById"></a>
# **deleteProductById**
> deleteProductById(authorization, id)

Delete a product associated with a given ID from your eCommerce system. Specifying a product associated with a given ID that does not exist will result in an error message

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the product to delete from the eCommerce system
    try {
      apiInstance.deleteProductById(authorization, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#deleteProductById");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the product to delete from the eCommerce system | |

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
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getProductById"></a>
# **getProductById**
> Product getProductById(authorization, id)

Retrieve a product associated with a given ID from the eCommerce system. Specifying a product with an ID that does not exist will result in an error response

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the product to retrieve from the eCommerce system
    try {
      Product result = apiInstance.getProductById(authorization, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductById");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the product to retrieve from the eCommerce system | |

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getProducts"></a>
# **getProducts**
> List&lt;Product&gt; getProducts(authorization, where, pageSize, nextPage, fields)

Find products in the eCommerce system, using the provided CEQL search expression. The search expression in CEQL is the WHERE clause in a typical SQL query, but without the WHERE keyword.  If no search expression is provided, all records will be retrieved

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String where = "where_example"; // String | The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field='value'). <p>Supported search terms: category, hidden_products. All other search criteria are ignored
    Long pageSize = 56L; // Long | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    String nextPage = "nextPage_example"; // String | The next page cursor, taken from the response header: `elements-next-page-token`
    String fields = "fields_example"; // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
    try {
      List<Product> result = apiInstance.getProducts(authorization, where, pageSize, nextPage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProducts");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **where** | **String**| The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field&#x3D;&#39;value&#39;). &lt;p&gt;Supported search terms: category, hidden_products. All other search criteria are ignored | [optional] |
| **pageSize** | **Long**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] |
| **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] |
| **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] |

### Return type

[**List&lt;Product&gt;**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="updateProductById"></a>
# **updateProductById**
> Product updateProductById(authorization, id, product)

Update a product associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the product object will be updated, and those fields not provided will be left alone. Updating a product with a specified ID that does not exist will result in an error response. &lt;p&gt;&lt;strong&gt;Update supports the following fields: sku, quantity, trackQuantity, quantityDelta, warningLimit, name, price, weight, tangible, enabled, fixedShippingRateOnly, fixedShippingRate, description, wholesalePrices, compareAtPrice, productClassId&lt;/strong&gt;

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the product to update in the eCommerce system
    ProductPatch product = new ProductPatch(); // ProductPatch | The product object, with those fields that are to be updated
    try {
      Product result = apiInstance.updateProductById(authorization, id, product);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#updateProductById");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the product to update in the eCommerce system | |
| **product** | [**ProductPatch**](ProductPatch.md)| The product object, with those fields that are to be updated | |

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |


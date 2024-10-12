# ProductApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProduct**](ProductApi.md#getProduct) | **GET** /api/catalog-seller-portal/products/{productId} | Get Product by ID |
| [**getProductDescription**](ProductApi.md#getProductDescription) | **GET** /api/catalog-seller-portal/products/{productId}/description | Get Product Description by Product ID |
| [**getProductQuery**](ProductApi.md#getProductQuery) | **GET** /api/catalog-seller-portal/products/{param} | Get Product by external ID,  SKU ID, SKU external ID or slug |
| [**postProduct**](ProductApi.md#postProduct) | **POST** /api/catalog-seller-portal/products | Create Product |
| [**putProduct**](ProductApi.md#putProduct) | **PUT** /api/catalog-seller-portal/products/{productId} | Update Product |
| [**putProductDescription**](ProductApi.md#putProductDescription) | **PUT** /api/catalog-seller-portal/products/{productId}/description | Update Product Description by Product ID |


<a id="getProduct"></a>
# **getProduct**
> GetProduct200Response getProduct(contentType, accept, productId)

Get Product by ID

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about a product by its ID. The response also has information about the product&#39;s SKUs.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;id\&quot;: \&quot;189371\&quot;,      \&quot;status\&quot;: \&quot;active\&quot;,      \&quot;name\&quot;: \&quot;VTEX 10 Shirt\&quot;,      \&quot;brandId\&quot;: \&quot;1\&quot;,      \&quot;brandName\&quot;: \&quot;AOC\&quot;,      \&quot;categoryIds\&quot;: [          \&quot;732\&quot;      ],      \&quot;categoryNames\&quot;: [          \&quot;/sandboxintegracao/Acessórios/\&quot;      ],      \&quot;specs\&quot;: [          {              \&quot;name\&quot;: \&quot;Color\&quot;,              \&quot;values\&quot;: [                  \&quot;Black\&quot;,                  \&quot;White\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;Size\&quot;,              \&quot;values\&quot;: [                  \&quot;S\&quot;,                  \&quot;M\&quot;,                  \&quot;L\&quot;              ]          }      ],      \&quot;attributes\&quot;: [          {              \&quot;name\&quot;: \&quot;Fabric\&quot;,              \&quot;value\&quot;: \&quot;Cotton\&quot;          },          {              \&quot;name\&quot;: \&quot;Gender\&quot;,              \&quot;value\&quot;: \&quot;Feminine\&quot;          }      ],      \&quot;slug\&quot;: \&quot;/vtex-shirt\&quot;,      \&quot;images\&quot;: [          {              \&quot;id\&quot;: \&quot;vtex_logo.jpg\&quot;,              \&quot;url\&quot;: \&quot;https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\&quot;,              \&quot;alt\&quot;: \&quot;VTEX\&quot;          }      ],      \&quot;skus\&quot;: [          {              \&quot;id\&quot;: \&quot;182907\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234567\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;Black\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;S\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          },          {              \&quot;id\&quot;: \&quot;182908\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234568\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;White\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;L\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          }      ],      \&quot;transportModal\&quot;: \&quot;123\&quot;,      \&quot;taxCode\&quot;: \&quot;100\&quot;,      \&quot;origin\&quot;: \&quot;vtxleo7778\&quot;,      \&quot;createdAt\&quot;: \&quot;2022-10-31T16:28:25.578067Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-10-31T17:09:12.639088Z\&quot;  }  &#x60;&#x60;&#x60;

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
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String productId = "189371"; // String | Product unique identifier number.
    try {
      GetProduct200Response result = apiInstance.getProduct(contentType, accept, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#getProduct");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **String**| Product unique identifier number. | |

### Return type

[**GetProduct200Response**](GetProduct200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getProductDescription"></a>
# **getProductDescription**
> GetProductDescription200Response getProductDescription(contentType, accept, productId)

Get Product Description by Product ID

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves the description of a product given a Product ID.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;productId\&quot;: \&quot;61\&quot;,      \&quot;description\&quot;: \&quot;Beautifully handmade laptop case/sleeve made in the Nepal Himalaya. It can be slipped inside your backpack or carried alone with space for all your work bits and pieces!\&quot;,      \&quot;createdAt\&quot;: \&quot;2022-10-10T19:18:45.612317Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-10-11T18:12:58.825544Z\&quot;  }  &#x60;&#x60;&#x60;

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
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String productId = "189371"; // String | Product unique identifier number.
    try {
      GetProductDescription200Response result = apiInstance.getProductDescription(contentType, accept, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#getProductDescription");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **String**| Product unique identifier number. | |

### Return type

[**GetProductDescription200Response**](GetProductDescription200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getProductQuery"></a>
# **getProductQuery**
> GetProductQuery200Response getProductQuery(contentType, accept, param)

Get Product by external ID,  SKU ID, SKU external ID or slug

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about a product by its external ID, SKU ID, SKU external ID or product slug. The response also has information about the product&#39;s SKUs.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;id\&quot;: \&quot;189371\&quot;,      \&quot;status\&quot;: \&quot;active\&quot;,      \&quot;name\&quot;: \&quot;VTEX 10 Shirt\&quot;,      \&quot;brandId\&quot;: \&quot;1\&quot;,      \&quot;brandName\&quot;: \&quot;AOC\&quot;,      \&quot;categoryIds\&quot;: [          \&quot;732\&quot;      ],      \&quot;categoryNames\&quot;: [          \&quot;/sandboxintegracao/Acessórios/\&quot;      ],      \&quot;specs\&quot;: [          {              \&quot;name\&quot;: \&quot;Color\&quot;,              \&quot;values\&quot;: [                  \&quot;Black\&quot;,                  \&quot;White\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;Size\&quot;,              \&quot;values\&quot;: [                  \&quot;S\&quot;,                  \&quot;M\&quot;,                  \&quot;L\&quot;              ]          }      ],      \&quot;attributes\&quot;: [          {              \&quot;name\&quot;: \&quot;Fabric\&quot;,              \&quot;value\&quot;: \&quot;Cotton\&quot;          },          {              \&quot;name\&quot;: \&quot;Gender\&quot;,              \&quot;value\&quot;: \&quot;Feminine\&quot;          }      ],      \&quot;slug\&quot;: \&quot;/vtex-shirt\&quot;,      \&quot;images\&quot;: [          {              \&quot;id\&quot;: \&quot;vtex_logo.jpg\&quot;,              \&quot;url\&quot;: \&quot;https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\&quot;,              \&quot;alt\&quot;: \&quot;VTEX\&quot;          }      ],      \&quot;skus\&quot;: [          {              \&quot;id\&quot;: \&quot;182907\&quot;,              \&quot;name\&quot;: \&quot;VTEX Shirt Black Size S\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234567\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;Black\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;S\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          },          {              \&quot;id\&quot;: \&quot;182908\&quot;,              \&quot;name\&quot;: \&quot;VTEX Shirt White Size L\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234568\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;White\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;L\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          }      ],      \&quot;transportModal\&quot;: \&quot;123\&quot;,      \&quot;taxCode\&quot;: \&quot;100\&quot;,      \&quot;origin\&quot;: \&quot;vtxleo7778\&quot;,      \&quot;createdAt\&quot;: \&quot;2022-10-31T16:28:25.578067Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-10-31T16:28:25.578067Z\&quot;  }  &#x60;&#x60;&#x60;

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
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String param = "external-id=189371"; // String | This part of the path must follow this format: `{param}={value}`. Replace `{param}` with the name of the parameter used to fetch a product, which can be one of the following: `external-id` (product reference unique identifier number in the store), `sku-id` (SKU unique identifier number), `sku-external-id` (SKU reference unique identifier number in the store) or `slug` (reference of the product in the URL of the store). Replace `{value}` with the value of the selected param. Make sure there is a `=` between them.
    try {
      GetProductQuery200Response result = apiInstance.getProductQuery(contentType, accept, param);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#getProductQuery");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **param** | **String**| This part of the path must follow this format: &#x60;{param}&#x3D;{value}&#x60;. Replace &#x60;{param}&#x60; with the name of the parameter used to fetch a product, which can be one of the following: &#x60;external-id&#x60; (product reference unique identifier number in the store), &#x60;sku-id&#x60; (SKU unique identifier number), &#x60;sku-external-id&#x60; (SKU reference unique identifier number in the store) or &#x60;slug&#x60; (reference of the product in the URL of the store). Replace &#x60;{value}&#x60; with the value of the selected param. Make sure there is a &#x60;&#x3D;&#x60; between them. | |

### Return type

[**GetProductQuery200Response**](GetProductQuery200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="postProduct"></a>
# **postProduct**
> PostProduct200Response postProduct(contentType, accept, postProductRequest)

Create Product

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Creates a new product and its SKUs.       ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;status\&quot;: \&quot;active\&quot;,      \&quot;name\&quot;: \&quot;VTEX 10 Shirt\&quot;,      \&quot;description\&quot;: \&quot;Shirt number 10 by VTEX.\&quot;,      \&quot;brandId\&quot;: \&quot;1\&quot;,      \&quot;categoryIds\&quot;: [          \&quot;732\&quot;      ],      \&quot;specs\&quot;: [          {              \&quot;name\&quot;: \&quot;Color\&quot;,              \&quot;values\&quot;: [                  \&quot;Black\&quot;,                  \&quot;White\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;Size\&quot;,              \&quot;values\&quot;: [                  \&quot;S\&quot;,                  \&quot;M\&quot;,                  \&quot;L\&quot;              ]          }      ],      \&quot;attributes\&quot;: [          {              \&quot;name\&quot;: \&quot;Fabric\&quot;,              \&quot;value\&quot;: \&quot;Cotton\&quot;          },          {              \&quot;name\&quot;: \&quot;Gender\&quot;,              \&quot;value\&quot;: \&quot;Feminine\&quot;          }      ],      \&quot;slug\&quot;: \&quot;/vtex-shirt\&quot;,      \&quot;images\&quot;: [          {              \&quot;id\&quot;: \&quot;vtex_logo.jpg\&quot;,              \&quot;url\&quot;: \&quot;https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\&quot;,              \&quot;alt\&quot;: \&quot;VTEX\&quot;          }      ],      \&quot;skus\&quot;: [          {              \&quot;name\&quot;: \&quot;VTEX Shirt Black Size S\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234567\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;Black\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;S\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;VTEX Shirt White Size L\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234568\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;White\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;L\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          }      ],      \&quot;origin\&quot;: \&quot;vtxleo7778\&quot;,      \&quot;transportModal\&quot;: \&quot;110\&quot;,      \&quot;taxCode\&quot;: \&quot;234\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;id\&quot;: \&quot;189371\&quot;,      \&quot;status\&quot;: \&quot;active\&quot;,      \&quot;name\&quot;: \&quot;VTEX 10 Shirt\&quot;,      \&quot;brandId\&quot;: \&quot;1\&quot;,      \&quot;brandName\&quot;: \&quot;AOC\&quot;,      \&quot;categoryIds\&quot;: [          \&quot;732\&quot;      ],      \&quot;categoryNames\&quot;: [          \&quot;/Men/Acessories/\&quot;      ],      \&quot;specs\&quot;: [          {              \&quot;name\&quot;: \&quot;Color\&quot;,              \&quot;values\&quot;: [                  \&quot;Black\&quot;,                  \&quot;White\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;Size\&quot;,              \&quot;values\&quot;: [                  \&quot;S\&quot;,                  \&quot;M\&quot;,                  \&quot;L\&quot;              ]          }      ],      \&quot;attributes\&quot;: [          {              \&quot;name\&quot;: \&quot;Fabric\&quot;,              \&quot;value\&quot;: \&quot;Cotton\&quot;          },          {              \&quot;name\&quot;: \&quot;Gender\&quot;,              \&quot;value\&quot;: \&quot;Feminine\&quot;          }      ],      \&quot;slug\&quot;: \&quot;/vtex-shirt\&quot;,      \&quot;images\&quot;: [          {              \&quot;id\&quot;: \&quot;vtex_logo.jpg\&quot;,              \&quot;url\&quot;: \&quot;https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\&quot;,              \&quot;alt\&quot;: \&quot;VTEX\&quot;          }      ],      \&quot;skus\&quot;: [          {              \&quot;id\&quot;: \&quot;182907\&quot;,              \&quot;name\&quot;: \&quot;VTEX Shirt Black Size S\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234567\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;Black\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;S\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          },          {              \&quot;id\&quot;: \&quot;182908\&quot;,              \&quot;name\&quot;: \&quot;VTEX Shirt White Size L\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234568\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;White\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;L\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          }      ],      \&quot;origin\&quot;: \&quot;vtxleo7778\&quot;,      \&quot;transportModal\&quot;: \&quot;110\&quot;,      \&quot;taxCode\&quot;: \&quot;234\&quot;,      \&quot;createdAt\&quot;: \&quot;2022-11-01T14:15:54.262702Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-11-01T14:15:54.262702Z\&quot;  }  &#x60;&#x60;&#x60;

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
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    PostProductRequest postProductRequest = new PostProductRequest(); // PostProductRequest | 
    try {
      PostProduct200Response result = apiInstance.postProduct(contentType, accept, postProductRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#postProduct");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **postProductRequest** | [**PostProductRequest**](PostProductRequest.md)|  | [optional] |

### Return type

[**PostProduct200Response**](PostProduct200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |

<a id="putProduct"></a>
# **putProduct**
> putProduct(contentType, accept, productId, putProductRequest)

Update Product

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Updates an existing product and its SKUs.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;id\&quot;: \&quot;189371\&quot;,      \&quot;status\&quot;: \&quot;active\&quot;,      \&quot;name\&quot;: \&quot;VTEX 10 Shirt\&quot;,      \&quot;description\&quot;: \&quot;Shirt number 10 by VTEX.\&quot;,      \&quot;brandId\&quot;: \&quot;1\&quot;,      \&quot;categoryIds\&quot;: [          \&quot;732\&quot;      ],      \&quot;specs\&quot;: [          {              \&quot;name\&quot;: \&quot;Color\&quot;,              \&quot;values\&quot;: [                  \&quot;Black\&quot;,                  \&quot;White\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;Size\&quot;,              \&quot;values\&quot;: [                  \&quot;S\&quot;,                  \&quot;M\&quot;,                  \&quot;L\&quot;              ]          }      ],      \&quot;attributes\&quot;: [          {              \&quot;name\&quot;: \&quot;Fabric\&quot;,              \&quot;value\&quot;: \&quot;Cotton\&quot;          },          {              \&quot;name\&quot;: \&quot;Gender\&quot;,              \&quot;value\&quot;: \&quot;Feminine\&quot;          }      ],      \&quot;slug\&quot;: \&quot;/vtex-shirt\&quot;,      \&quot;transportModal\&quot;: null,      \&quot;taxCode\&quot;: null,      \&quot;images\&quot;: [          {              \&quot;id\&quot;: \&quot;vtex_logo.jpg\&quot;,              \&quot;url\&quot;: \&quot;https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\&quot;,              \&quot;alt\&quot;: \&quot;VTEX\&quot;          }      ],      \&quot;skus\&quot;: [          {              \&quot;name\&quot;: \&quot;VTEX Shirt Black Size S\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234567\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;Black\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;S\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;VTEX Shirt White Size L\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234568\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;White\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;L\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          }      ],      \&quot;origin\&quot;: \&quot;vtxleo7778\&quot;  }  &#x60;&#x60;&#x60;

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
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String productId = "189371"; // String | Product unique identifier number.
    PutProductRequest putProductRequest = new PutProductRequest(); // PutProductRequest | 
    try {
      apiInstance.putProduct(contentType, accept, productId, putProductRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#putProduct");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **String**| Product unique identifier number. | |
| **putProductRequest** | [**PutProductRequest**](PutProductRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="putProductDescription"></a>
# **putProductDescription**
> putProductDescription(contentType, accept, productId, putProductDescriptionRequest)

Update Product Description by Product ID

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Updates the description of a product given a Product ID.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;productId\&quot;: \&quot;71\&quot;,      \&quot;description\&quot;: \&quot;White shirt.\&quot;  }  &#x60;&#x60;&#x60;

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
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String productId = "71"; // String | Product unique identifier number.
    PutProductDescriptionRequest putProductDescriptionRequest = new PutProductDescriptionRequest(); // PutProductDescriptionRequest | 
    try {
      apiInstance.putProductDescription(contentType, accept, productId, putProductDescriptionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#putProductDescription");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **String**| Product unique identifier number. | |
| **putProductDescriptionRequest** | [**PutProductDescriptionRequest**](PutProductDescriptionRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |


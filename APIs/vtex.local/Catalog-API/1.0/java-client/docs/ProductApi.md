# ProductApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtProductPost**](ProductApi.md#apiCatalogPvtProductPost) | **POST** /api/catalog/pvt/product | Create Product with Category and Brand |
| [**apiCatalogPvtProductProductIdPut**](ProductApi.md#apiCatalogPvtProductProductIdPut) | **PUT** /api/catalog/pvt/product/{productId} | Update Product |
| [**getProductbyid**](ProductApi.md#getProductbyid) | **GET** /api/catalog/pvt/product/{productId} | Get Product by ID |
| [**productAndSkuIds**](ProductApi.md#productAndSkuIds) | **GET** /api/catalog_system/pvt/products/GetProductAndSkuIds | Get Product and SKU IDs |
| [**productVariations**](ProductApi.md#productVariations) | **GET** /api/catalog_system/pub/products/variations/{productId} | Get Product&#39;s SKUs by Product ID |
| [**productandTradePolicy**](ProductApi.md#productandTradePolicy) | **GET** /api/catalog_system/pvt/products/productget/{productId} | Get Product and its general context |
| [**productbyRefId**](ProductApi.md#productbyRefId) | **GET** /api/catalog_system/pvt/products/productgetbyrefid/{refId} | Get Product by RefId |
| [**reviewRateProduct**](ProductApi.md#reviewRateProduct) | **GET** /api/addon/pvt/review/GetProductRate/{productId} | Get Product Review Rate by Product ID |


<a id="apiCatalogPvtProductPost"></a>
# **apiCatalogPvtProductPost**
> ApiCatalogPvtProductPost200Response apiCatalogPvtProductPost(contentType, accept, apiCatalogPvtProductPostRequest)

Create Product with Category and Brand

This endpoint allows two types of request:    **Type 1:** Creating a new Product as well as a new Category path (including subcategories) and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60; parameters.    **Type 2:** Creating a new Product given an existing &#x60;BrandId&#x60; and an existing &#x60;CategoryId&#x60;.    When creating a product, regardless of the type of request, if there is a need to create a new product with a specific custom product ID, specify the &#x60;Id&#x60; (integer) in the request body. Otherwise, VTEX will generate the ID automatically.     ## Request body examples     ### Type 1     Request to create a product, associating it to a new Category and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60;:    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;CategoryPath\&quot;: \&quot;Mens/Clothing/T-Shirts\&quot;,      \&quot;BrandName\&quot;: \&quot;Nike\&quot;,      \&quot;RefId\&quot;: \&quot;31011706925\&quot;,      \&quot;Title\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;LinkId\&quot;: \&quot;tshirt-black\&quot;,      \&quot;Description\&quot;: \&quot;This is a cool Tshirt\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2022-01-01T00:00:00\&quot;,      \&quot;IsVisible\&quot;: true,      \&quot;IsActive\&quot;: true,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;MetaTagDescription\&quot;: \&quot;tshirt black\&quot;,      \&quot;ShowWithoutStock\&quot;: true,      \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ### Type 2    Request to create a product, associating it to an existing &#x60;CategoryId&#x60; and &#x60;BrandId&#x60;:    &#x60;&#x60;&#x60;json  {     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 52,     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;      &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.

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
    ApiCatalogPvtProductPostRequest apiCatalogPvtProductPostRequest = new ApiCatalogPvtProductPostRequest(); // ApiCatalogPvtProductPostRequest | 
    try {
      ApiCatalogPvtProductPost200Response result = apiInstance.apiCatalogPvtProductPost(contentType, accept, apiCatalogPvtProductPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#apiCatalogPvtProductPost");
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
| **apiCatalogPvtProductPostRequest** | [**ApiCatalogPvtProductPostRequest**](ApiCatalogPvtProductPostRequest.md)|  | [optional] |

### Return type

[**ApiCatalogPvtProductPost200Response**](ApiCatalogPvtProductPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtProductProductIdPut"></a>
# **apiCatalogPvtProductProductIdPut**
> ApiCatalogPvtProductPost200Response apiCatalogPvtProductProductIdPut(contentType, accept, productId, apiCatalogPvtProductProductIdPutRequest)

Update Product

Updates an existing Product.

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
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    ApiCatalogPvtProductProductIdPutRequest apiCatalogPvtProductProductIdPutRequest = new ApiCatalogPvtProductProductIdPutRequest(); // ApiCatalogPvtProductProductIdPutRequest | 
    try {
      ApiCatalogPvtProductPost200Response result = apiInstance.apiCatalogPvtProductProductIdPut(contentType, accept, productId, apiCatalogPvtProductProductIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#apiCatalogPvtProductProductIdPut");
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
| **productId** | **Integer**| Product’s unique numerical identifier. | |
| **apiCatalogPvtProductProductIdPutRequest** | [**ApiCatalogPvtProductProductIdPutRequest**](ApiCatalogPvtProductProductIdPutRequest.md)|  | [optional] |

### Return type

[**ApiCatalogPvtProductPost200Response**](ApiCatalogPvtProductPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getProductbyid"></a>
# **getProductbyid**
> GetProductbyid200Response getProductbyid(contentType, accept, productId)

Get Product by ID

Retrieves a specific Product by its ID. This information is exactly what is needed to create a new Product.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String productId = "productId_example"; // String | Product’s unique numerical identifier.
    try {
      GetProductbyid200Response result = apiInstance.getProductbyid(contentType, accept, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#getProductbyid");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **String**| Product’s unique numerical identifier. | |

### Return type

[**GetProductbyid200Response**](GetProductbyid200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productAndSkuIds"></a>
# **productAndSkuIds**
> ProductAndSkuIds200Response productAndSkuIds(contentType, accept, categoryId, from, to)

Get Product and SKU IDs

Retrieves the IDs of products and SKUs.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer categoryId = 1; // Integer | ID of the category from which you need to retrieve Products and SKUs.
    Integer from = 1; // Integer | Insert the ID that will start the request result.
    Integer to = 10; // Integer | Insert the ID that will end the request result.
    try {
      ProductAndSkuIds200Response result = apiInstance.productAndSkuIds(contentType, accept, categoryId, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productAndSkuIds");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **categoryId** | **Integer**| ID of the category from which you need to retrieve Products and SKUs. | [optional] |
| **from** | **Integer**| Insert the ID that will start the request result. | [optional] |
| **to** | **Integer**| Insert the ID that will end the request result. | [optional] |

### Return type

[**ProductAndSkuIds200Response**](ProductAndSkuIds200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productVariations"></a>
# **productVariations**
> ProductVariations200Response productVariations(contentType, accept, productId)

Get Product&#39;s SKUs by Product ID

Retrieves data about the product and all SKUs related to it by the product&#39;s ID.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;productId\&quot;: 9,      \&quot;name\&quot;: \&quot;Camisa Masculina\&quot;,      \&quot;salesChannel\&quot;: \&quot;2\&quot;,      \&quot;available\&quot;: true,      \&quot;displayMode\&quot;: \&quot;lista\&quot;,      \&quot;dimensions\&quot;: [          \&quot;Cores\&quot;,          \&quot;Tamanho\&quot;,          \&quot;País de origem\&quot;,          \&quot;Gênero\&quot;      ],      \&quot;dimensionsInputType\&quot;: {          \&quot;Cores\&quot;: \&quot;Combo\&quot;,          \&quot;Tamanho\&quot;: \&quot;Combo\&quot;,          \&quot;País de origem\&quot;: \&quot;Combo\&quot;,          \&quot;Gênero\&quot;: \&quot;Combo\&quot;      },      \&quot;dimensionsMap\&quot;: {          \&quot;Cores\&quot;: [              \&quot;Amarelo\&quot;,              \&quot;Azul\&quot;,              \&quot;Vermelho\&quot;          ],          \&quot;Tamanho\&quot;: [              \&quot;P\&quot;,              \&quot;M\&quot;,              \&quot;G\&quot;          ],          \&quot;País de origem\&quot;: [              \&quot;Brasil\&quot;          ],          \&quot;Gênero\&quot;: [              \&quot;Masculino\&quot;          ]      },      \&quot;skus\&quot;: [          {              \&quot;sku\&quot;: 310118454,              \&quot;skuname\&quot;: \&quot;Amarela - G\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Amarelo\&quot;,                  \&quot;Tamanho\&quot;: \&quot;G\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: false,              \&quot;availablequantity\&quot;: 0,              \&quot;cacheVersionUsedToCallCheckout\&quot;: null,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 9.999.876,00\&quot;,              \&quot;bestPrice\&quot;: 999987600,              \&quot;spotPrice\&quot;: 999987600,              \&quot;installments\&quot;: 0,              \&quot;installmentsValue\&quot;: 0,              \&quot;installmentsInsterestRate\&quot;: null,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155467-292-292/image-5d7ad76ad1954c53adecab4138319034.jpg?v&#x3D;637321899584500000\&quot;,              \&quot;sellerId\&quot;: \&quot;1\&quot;,              \&quot;seller\&quot;: \&quot;lojadobreno\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 1.0000,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          },          {              \&quot;sku\&quot;: 310118455,              \&quot;skuname\&quot;: \&quot;Vermelha - M\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Vermelho\&quot;,                  \&quot;Tamanho\&quot;: \&quot;M\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: true,              \&quot;availablequantity\&quot;: 99999,              \&quot;cacheVersionUsedToCallCheckout\&quot;: \&quot;38395F1AEF59DF5CEAEDE472328145CD_\&quot;,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 20,00\&quot;,              \&quot;bestPrice\&quot;: 2000,              \&quot;spotPrice\&quot;: 2000,              \&quot;installments\&quot;: 1,              \&quot;installmentsValue\&quot;: 2000,              \&quot;installmentsInsterestRate\&quot;: 0,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155468-292-292/image-601a6099aace48b89d26fc9f22e8e611.jpg?v&#x3D;637321906602470000\&quot;,              \&quot;sellerId\&quot;: \&quot;pedrostore\&quot;,              \&quot;seller\&quot;: \&quot;pedrostore\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 0.4167,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          }      ]  }  &#x60;&#x60;&#x60;

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    try {
      ProductVariations200Response result = apiInstance.productVariations(contentType, accept, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariations");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |

### Return type

[**ProductVariations200Response**](ProductVariations200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productandTradePolicy"></a>
# **productandTradePolicy**
> ProductandTradePolicy200Response productandTradePolicy(contentType, accept, productId)

Get Product and its general context

Retrieves a specific product&#39;s general information as name, description and the trade policies that it is included.

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    try {
      ProductandTradePolicy200Response result = apiInstance.productandTradePolicy(contentType, accept, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productandTradePolicy");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |

### Return type

[**ProductandTradePolicy200Response**](ProductandTradePolicy200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productbyRefId"></a>
# **productbyRefId**
> ProductbyRefId200Response productbyRefId(contentType, accept, refId)

Get Product by RefId

Retrieves a specific product by its Reference ID.

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String refId = "refId_example"; // String | Product Referecial Code
    try {
      ProductbyRefId200Response result = apiInstance.productbyRefId(contentType, accept, refId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productbyRefId");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **refId** | **String**| Product Referecial Code | |

### Return type

[**ProductbyRefId200Response**](ProductbyRefId200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewRateProduct"></a>
# **reviewRateProduct**
> BigDecimal reviewRateProduct(contentType, accept, productId)

Get Product Review Rate by Product ID

Retrieves the review rate of a product by this product&#39;s ID.

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    try {
      BigDecimal result = apiInstance.reviewRateProduct(contentType, accept, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#reviewRateProduct");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |

### Return type

[**BigDecimal**](BigDecimal.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


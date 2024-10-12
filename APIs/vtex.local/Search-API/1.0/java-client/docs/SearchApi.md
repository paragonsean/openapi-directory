# SearchApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productSearch**](SearchApi.md#productSearch) | **GET** /api/catalog_system/pub/products/search/{search} | Search for Products |
| [**productSearchFilteredandOrdered**](SearchApi.md#productSearchFilteredandOrdered) | **GET** /api/catalog_system/pub/products/search | Search for Products with Filter, Order and Pagination |
| [**searchbyproducturl**](SearchApi.md#searchbyproducturl) | **GET** /api/catalog_system/pub/products/search/{product-text-link}/p | Search Product by Product URL |


<a id="productSearch"></a>
# **productSearch**
> List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt; productSearch(accept, contentType, search)

Search for Products

Retrieves general information about the products related to the term searched.   This is the main search used by the store. The user can type anything to be searched.      For example, if they search for a \&quot;decanter\&quot;, this is the URL: &#x60;https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pub/products/search/decanter&#x60;.     Note that maybe the response can be HTTP 200 or 206, 206 means that it&#39;s a partial content response.    If it is a 206 take a look at the Headers, will be an entry called resources. E.g.: resources → 0-9/19. This means that the response is showing items from 0 to 9, 10 items, but there were 19 items found. See more information at the paging route example.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String search = "jacket"; // String | Term used to search products
    try {
      List<ProductSearchWhoBoughtAlsoBought200ResponseInner> result = apiInstance.productSearch(accept, contentType, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#productSearch");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **search** | **String**| Term used to search products | |

### Return type

[**List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt;**](ProductSearchWhoBoughtAlsoBought200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productSearchFilteredandOrdered"></a>
# **productSearchFilteredandOrdered**
> List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt; productSearchFilteredandOrdered(accept, contentType, from, to, ft, fq, O)

Search for Products with Filter, Order and Pagination

Retrieves general information about the store products. This information can be filtered and ordered by a number of options. It also can be paginated, filtered and ordered.     ## Filters      - **Filter by full text** - &#x60;ft&#x3D;{searchWord}&#x60;    E.g.: &#x60;ft&#x3D;television&#x60;    - **Filter by category** - &#x60;fq&#x3D;C:/{a}/{b}&#x60;    &#x60;{a}&#x60; and &#x60;{b}&#x60; are Category IDs     E.g.: &#x60;fq&#x3D;C:/1000041/1000049/&#x60;    - **Filter by brand** - &#x60;fq&#x3D;B:/{a}/{b}&#x60;    &#x60;{a}&#x60; and &#x60;{b}&#x60; are Brand IDs  E.g.: &#x60;fq&#x3D;B:/189385/189387/&#x60;    - **Filter by specification** - &#x60;fq&#x3D;specificationFilter_{a}:{b}&#x60;    &#x60;{a}&#x60; is the specification ID  &#x60;{b}&#x60; is the specification value  E.g.: To filter products where the color is Blue, find the specification ID for color. Suppose it is 123, then the query will be: &#x60;fq&#x3D;specificationFilter_123:Blue&#x60;    - **Filter by price range** - &#x60;fq&#x3D;P:[{a} TO {b}]&#x60;    &#x60;{a}&#x60;  is the minimum price \&quot;from\&quot;  &#x60;{b}&#x60; is the highest price \&quot;to\&quot;    E.g.: &#x60;fq&#x3D;P:[0 TO 20]&#x60; will search products between 0.00 and 20.00.      - **Filter by collection** - &#x60;fq&#x3D;productClusterIds:{{productClusterId}}&#x60;   &#x60;productClusterId&#x60; is the same as &#x60;collectionId&#x60;    For more information about collections, read [Creating a product collection](https://help.vtex.com/en/tutorial/creating-a-product-collection).    - **Filter by product ID** - &#x60;fq&#x3D;productId:{{productId}}&#x60;    - **Filter by SKU ID** - &#x60;fq&#x3D;skuId:{{skuId}}&#x60;    - **Filter by referenceId** - &#x60;fq&#x3D;alternateIds_RefId:{{referenceId}}&#x60;    - **Filter by EAN13** - &#x60;fq&#x3D;alternateIds_Ean:{{ean13}}&#x60;    - **Filter by availability at a specific sales channel** - &#x60;fq&#x3D;isAvailablePerSalesChannel_{{sc}}:{{bool}}&#x60;    &#x60;{{sc}}&#x60; is the desired sales channel    &#x60;{{bool}}&#x60; is true ou false, 1 or 0.    E.g.: seaching available products for the sales channel 4 would be &#x60;fq&#x3D;isAvailablePerSalesChannel_4:1&#x60;    - **Filter by available at a specific seller** - &#x60;fq&#x3D;sellerId:{{sellerId}}&#x60;  The search does not include White Label Sellers.    ## Pagination    - **Initial item number** - &#x60;_from&#x3D;{{first}}&#x60;  - **Final item number** - &#x60;_to&#x3D;{{last}}&#x60;    &gt;⚠️ This endpoint returns a maximum of 50 items per response, so the difference between &#x60;_from&#x60; and &#x60;_to&#x60; should not exceed this number. The result order is descending, from the highest product ID to the lowest.    ## Sorting    - **Price**    &#x60;O&#x3D;OrderByPriceDESC&#x60;    &#x60;O&#x3D;OrderByPriceASC&#x60;    - **Top Selling Products**    &#x60;O&#x3D;OrderByTopSaleDESC&#x60;    - **Best Reviews**    &#x60;O&#x3D;OrderByReviewRateDESC&#x60;    - **Name**    &#x60;O&#x3D;OrderByNameASC&#x60;    &#x60;O&#x3D;OrderByNameDESC&#x60;    - **Release Date**    &#x60;O&#x3D;OrderByReleaseDateDESC&#x60;    - **Best Discounts**    &#x60;O&#x3D;OrderByBestDiscountDESC&#x60;    - **Score**    &#x60;O&#x3D;OrderByScoreDESC&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String from = "1"; // String | Starter page range. These parameters allow the API to be paginated. Take into account that the initial and final pages cannot have a separation superior to 50 pages. Thus, it will be displayed 50 items per page.
    String to = "50"; // String | Finisher page range. These parameters allow the API to be paginated. Take into account that the initial and final pages cannot have a separation superior to 50 pages. Thus, it will be displayed 50 items per page.
    String ft = "television"; // String | Filter by full text. The form is`ft={searchWord}`
    String fq = "C:/1000041/1000049/"; // String | General filter. It can be by category (`fq=C:/{a}/{b}`), by specification (`fq=specificationFilter_{a}:{b}`),  by price range (`fq=P:[{a} TO {b}]`), by collection (`fq=productClusterIds:{{productClusterId}}`), by product ID (`fq=productId:{{productId}}`),  by SKU ID (`fq=skuId:{{skuId}}`), by Reference ID (`fq=alternateIds_RefId:{{referenceId}}`), by EAN13 (`fq=alternateIds_Ean:{{ean13}}`), by availability at a specific sales channel (`fq=isAvailablePerSalesChannel_{{sc}}:{{bool}}`), by available at a specific seller (`fq=sellerId:{{sellerId}}`)
    String O = "OrderByNameASC"; // String | Sorting method. It can be by Price (`O=OrderByPriceDESC` or `O=OrderByPriceASC`), by Top Selling Products (`O=OrderByTopSaleDESC`), by Best Reviews (`O=OrderByReviewRateDESC`), by Name (`O=OrderByNameASC` or `O=OrderByNameDESC`), by Release Date (`O=OrderByReleaseDateDESC`), by Best Discounts (`O=OrderByBestDiscountDESC`), by Score (`O=OrderByScoreDESC`)
    try {
      List<ProductSearchWhoBoughtAlsoBought200ResponseInner> result = apiInstance.productSearchFilteredandOrdered(accept, contentType, from, to, ft, fq, O);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#productSearchFilteredandOrdered");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **from** | **String**| Starter page range. These parameters allow the API to be paginated. Take into account that the initial and final pages cannot have a separation superior to 50 pages. Thus, it will be displayed 50 items per page. | [optional] |
| **to** | **String**| Finisher page range. These parameters allow the API to be paginated. Take into account that the initial and final pages cannot have a separation superior to 50 pages. Thus, it will be displayed 50 items per page. | [optional] |
| **ft** | **String**| Filter by full text. The form is&#x60;ft&#x3D;{searchWord}&#x60; | [optional] |
| **fq** | **String**| General filter. It can be by category (&#x60;fq&#x3D;C:/{a}/{b}&#x60;), by specification (&#x60;fq&#x3D;specificationFilter_{a}:{b}&#x60;),  by price range (&#x60;fq&#x3D;P:[{a} TO {b}]&#x60;), by collection (&#x60;fq&#x3D;productClusterIds:{{productClusterId}}&#x60;), by product ID (&#x60;fq&#x3D;productId:{{productId}}&#x60;),  by SKU ID (&#x60;fq&#x3D;skuId:{{skuId}}&#x60;), by Reference ID (&#x60;fq&#x3D;alternateIds_RefId:{{referenceId}}&#x60;), by EAN13 (&#x60;fq&#x3D;alternateIds_Ean:{{ean13}}&#x60;), by availability at a specific sales channel (&#x60;fq&#x3D;isAvailablePerSalesChannel_{{sc}}:{{bool}}&#x60;), by available at a specific seller (&#x60;fq&#x3D;sellerId:{{sellerId}}&#x60;) | [optional] |
| **O** | **String**| Sorting method. It can be by Price (&#x60;O&#x3D;OrderByPriceDESC&#x60; or &#x60;O&#x3D;OrderByPriceASC&#x60;), by Top Selling Products (&#x60;O&#x3D;OrderByTopSaleDESC&#x60;), by Best Reviews (&#x60;O&#x3D;OrderByReviewRateDESC&#x60;), by Name (&#x60;O&#x3D;OrderByNameASC&#x60; or &#x60;O&#x3D;OrderByNameDESC&#x60;), by Release Date (&#x60;O&#x3D;OrderByReleaseDateDESC&#x60;), by Best Discounts (&#x60;O&#x3D;OrderByBestDiscountDESC&#x60;), by Score (&#x60;O&#x3D;OrderByScoreDESC&#x60;) | [optional] |

### Return type

[**List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt;**](ProductSearchWhoBoughtAlsoBought200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="searchbyproducturl"></a>
# **searchbyproducturl**
> List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt; searchbyproducturl(accept, contentType, productTextLink)

Search Product by Product URL

Retrieves general information about the product of the URL you searched for.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String productTextLink = "blue-shirt"; // String | Product URL
    try {
      List<ProductSearchWhoBoughtAlsoBought200ResponseInner> result = apiInstance.searchbyproducturl(accept, contentType, productTextLink);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchbyproducturl");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **productTextLink** | **String**| Product URL | |

### Return type

[**List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt;**](ProductSearchWhoBoughtAlsoBought200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |


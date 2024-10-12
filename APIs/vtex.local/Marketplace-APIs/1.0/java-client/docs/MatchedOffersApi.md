# MatchedOffersApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProductoffers**](MatchedOffersApi.md#getProductoffers) | **GET** /offer-manager/pvt/product/{productId} | Get Matched Offer&#39;s Data by Product ID |
| [**getSKUoffers**](MatchedOffersApi.md#getSKUoffers) | **GET** /offer-manager/pvt/product/{productId}/sku/{skuId} | Get Matched Offer&#39;s Data by SKU ID |
| [**getofferslist**](MatchedOffersApi.md#getofferslist) | **GET** /offer-manager/pvt/offers | Get Matched Offers List |


<a id="getProductoffers"></a>
# **getProductoffers**
> getProductoffers(accountName, environment, contentType, accept, productId)

Get Matched Offer&#39;s Data by Product ID

Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.   This endpoint retrieves the available offers for a speciic Product ID in the marketplace&#39;s catalog. It differs from the Get Suggestions endpoints, since it retrieves products that were already matched by the marketplace operator, and are currently active in its catalog.   The call returns a list of offers for that ID, that contain the following data:   - Seller that sells the SKU   - Correspondent SKU ID   - SKU&#39;s price value   - Inventory level   - Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) that it is available at.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MatchedOffersApi;

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

    MatchedOffersApi apiInstance = new MatchedOffersApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account. Used as part of the URL.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String productId = "123456"; // String | A string that identifies the seller's product. This is the ID that the marketplace will use for all references to this product, such as price and inventory notifications.
    try {
      apiInstance.getProductoffers(accountName, environment, contentType, accept, productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MatchedOffersApi#getProductoffers");
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
| **accountName** | **String**| Name of the VTEX account. Used as part of the URL. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **String**| A string that identifies the seller&#39;s product. This is the ID that the marketplace will use for all references to this product, such as price and inventory notifications. | [default to 123456] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getSKUoffers"></a>
# **getSKUoffers**
> getSKUoffers(accountName, environment, contentType, accept, productId, skuId)

Get Matched Offer&#39;s Data by SKU ID

Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.   This endpoint retrieves the available offers for a speciic SKU ID in the marketplace&#39;s catalog. It differs from the Get Suggestions endpoints, since it retrieves products that were already matched by the marketplace operator, and are currently active in its catalog.   The call returns a list of offers for that ID, that contain the following data:   - Seller that sells the SKU   - Correspondent SKU ID   - SKU&#39;s price value   - Inventory level   - Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) that it is available at.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MatchedOffersApi;

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

    MatchedOffersApi apiInstance = new MatchedOffersApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account. Used as part of the URL.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String productId = "123456"; // String | A string that identifies the seller's product. This is the ID that the marketplace will use for all references to this product, such as price and inventory notifications.
    String skuId = "1234"; // String | A string that identifies the seller's SKU. This is the ID that the marketplace will use for all references to this SKU, such as price and inventory notifications.
    try {
      apiInstance.getSKUoffers(accountName, environment, contentType, accept, productId, skuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MatchedOffersApi#getSKUoffers");
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
| **accountName** | **String**| Name of the VTEX account. Used as part of the URL. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **String**| A string that identifies the seller&#39;s product. This is the ID that the marketplace will use for all references to this product, such as price and inventory notifications. | [default to 123456] |
| **skuId** | **String**| A string that identifies the seller&#39;s SKU. This is the ID that the marketplace will use for all references to this SKU, such as price and inventory notifications. | [default to 1234] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getofferslist"></a>
# **getofferslist**
> List&lt;GetMatchedOffersResponse&gt; getofferslist(accountName, contentType, environment, accept, sort, rows, start, fq)

Get Matched Offers List

Offers are seller&#39;s products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.    This endpoint retrieves the available offers in a marketplace. It differs from the Get Suggestions endpoints, since it retrieves products that were already matched by the marketplace, and are currently in its catalog.   It is possible to filter the search through the following parameters:   - rows  - sort   - start   - fq

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MatchedOffersApi;

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

    MatchedOffersApi apiInstance = new MatchedOffersApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account. Used as part of the URL
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String sort = "availability,desc"; // String | Criteria used to sort the list of offers. For sorting values in ascending order, use `asc`, while for descending order, use `desc`. To fill in the field, insert the sorting criteria, followed by 'asc', or 'desc', separated by a comma. You can sort by the following criteria:   - **price:** sorts offers by price. *Ascending* goes from lowest to highest price, while *Descending* goes from highest to lowest price.   - **name:** sorts offers by *productName*, in alphabetical order. *Ascending* goes from *A* to *Z*, while *Descending* goes from *Z* to *A*.   - **availability:** availability in the sales channel (sc). The default value is 1.   Ex. sort=availability,desc   Ex. sort=name,asc   Ex. price,desc
    Integer rows = 20; // Integer | Number of rows included in the response. Each row corresponds to a single offer. The default amount of rows in the response is 1, and the maximum amount is 50. To have more than one offer listed in the response, please add the `rows` parameter with a number greater than 1.
    Integer start = 21; // Integer | Number corresponding to the row from which the offer list will begin, used for pagination. Filters the list of offers by retrieving the offers starting from the row defined. The default value is 0, if the param is not included in the call.
    String fq = "skuId:172"; // String | This filter query can be used to filter offers by the criteria described below. It should be filled in by following the format: `fq={{criteriaName}}:{{criteriaValue}}`.   - **productId:** integer of the product ID   - **productName:** string of the product's name   - **skuId:** integer of the SKU ID   - **eanId:** string of the EAN ID   - **refId:** string of the Ref ID   - **categoryId:** integer of the category ID   - **brandId:** integer of the brand ID   - **sellerId:** string of the seller ID   - **sc:** integer of the sales channel's ID (trade policy in VTEX)   Ex: skuId:172   Ex: categoryId:13   Ex. productName:Product example-123
    try {
      List<GetMatchedOffersResponse> result = apiInstance.getofferslist(accountName, contentType, environment, accept, sort, rows, start, fq);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MatchedOffersApi#getofferslist");
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
| **accountName** | **String**| Name of the VTEX account. Used as part of the URL | [default to apiexamples] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sort** | **String**| Criteria used to sort the list of offers. For sorting values in ascending order, use &#x60;asc&#x60;, while for descending order, use &#x60;desc&#x60;. To fill in the field, insert the sorting criteria, followed by &#39;asc&#39;, or &#39;desc&#39;, separated by a comma. You can sort by the following criteria:   - **price:** sorts offers by price. *Ascending* goes from lowest to highest price, while *Descending* goes from highest to lowest price.   - **name:** sorts offers by *productName*, in alphabetical order. *Ascending* goes from *A* to *Z*, while *Descending* goes from *Z* to *A*.   - **availability:** availability in the sales channel (sc). The default value is 1.   Ex. sort&#x3D;availability,desc   Ex. sort&#x3D;name,asc   Ex. price,desc | [optional] |
| **rows** | **Integer**| Number of rows included in the response. Each row corresponds to a single offer. The default amount of rows in the response is 1, and the maximum amount is 50. To have more than one offer listed in the response, please add the &#x60;rows&#x60; parameter with a number greater than 1. | [optional] [default to 20] |
| **start** | **Integer**| Number corresponding to the row from which the offer list will begin, used for pagination. Filters the list of offers by retrieving the offers starting from the row defined. The default value is 0, if the param is not included in the call. | [optional] [default to 21] |
| **fq** | **String**| This filter query can be used to filter offers by the criteria described below. It should be filled in by following the format: &#x60;fq&#x3D;{{criteriaName}}:{{criteriaValue}}&#x60;.   - **productId:** integer of the product ID   - **productName:** string of the product&#39;s name   - **skuId:** integer of the SKU ID   - **eanId:** string of the EAN ID   - **refId:** string of the Ref ID   - **categoryId:** integer of the category ID   - **brandId:** integer of the brand ID   - **sellerId:** string of the seller ID   - **sc:** integer of the sales channel&#39;s ID (trade policy in VTEX)   Ex: skuId:172   Ex: categoryId:13   Ex. productName:Product example-123 | [optional] |

### Return type

[**List&lt;GetMatchedOffersResponse&gt;**](GetMatchedOffersResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


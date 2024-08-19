# ProductsApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**articleCreateArticle**](ProductsApi.md#articleCreateArticle) | **POST** /api/v1/products | Creates a new product |
| [**articleDeleteArticle**](ProductsApi.md#articleDeleteArticle) | **DELETE** /api/v1/products/{id} | Deletes a product |
| [**articleDeleteImage**](ProductsApi.md#articleDeleteImage) | **DELETE** /api/v1/products/images/{imageId} | Deletes a single image by id |
| [**articleDeleteImageFromProduct**](ProductsApi.md#articleDeleteImageFromProduct) | **DELETE** /api/v1/products/{productId}/images/{imageId} | Deletes a single image from a product |
| [**articleDeleteImages**](ProductsApi.md#articleDeleteImages) | **POST** /api/v1/products/images/delete | Delete multiple images by id |
| [**articleGetArticle**](ProductsApi.md#articleGetArticle) | **GET** /api/v1/products/{id} | Queries a single article by id or by sku |
| [**articleGetCategory**](ProductsApi.md#articleGetCategory) | **GET** /api/v1/products/category | GEts a list of all defined categories |
| [**articleGetCustomField**](ProductsApi.md#articleGetCustomField) | **GET** /api/v1/products/custom-fields/{id} | Queries a single custom field |
| [**articleGetCustomFields**](ProductsApi.md#articleGetCustomFields) | **GET** /api/v1/products/custom-fields | Queries a list of all custom fields |
| [**articleGetImage**](ProductsApi.md#articleGetImage) | **GET** /api/v1/products/images/{imageId} | Returns a single image by id |
| [**articleGetImageFromProduct**](ProductsApi.md#articleGetImageFromProduct) | **GET** /api/v1/products/{productId}/images/{imageId} | Returns a single image by id |
| [**articleGetImages**](ProductsApi.md#articleGetImages) | **GET** /api/v1/products/{productId}/images | Returns a list of all images of the product |
| [**articleGetList**](ProductsApi.md#articleGetList) | **GET** /api/v1/products | Get a list of all products |
| [**articleGetPatchableFields**](ProductsApi.md#articleGetPatchableFields) | **GET** /api/v1/products/PatchableFields | Returns a list of fields which can be updated with the patch call |
| [**articleGetReservedAmount**](ProductsApi.md#articleGetReservedAmount) | **GET** /api/v1/products/reservedamount | Queries the reserved amount for a single article by id or by sku |
| [**articleGetStocks**](ProductsApi.md#articleGetStocks) | **GET** /api/v1/products/stocks | Query all defined stock locations |
| [**articlePatchArticle**](ProductsApi.md#articlePatchArticle) | **PATCH** /api/v1/products/{id} | Updates one or more fields of a product |
| [**articlePutImage**](ProductsApi.md#articlePutImage) | **PUT** /api/v1/products/{productId}/images/{imageId} | Add or update an existing image of a product |
| [**articlePutImages**](ProductsApi.md#articlePutImages) | **PUT** /api/v1/products/{productId}/images | Add multiple images to a product or replace the product images by the given images |
| [**articleUpdateStock**](ProductsApi.md#articleUpdateStock) | **POST** /api/v1/products/updatestock | Update the stock qty of an article |
| [**articleUpdateStockCode**](ProductsApi.md#articleUpdateStockCode) | **POST** /api/v1/products/updatestockcode | Update the stock code of an article |
| [**articleUpdateStockMultiple**](ProductsApi.md#articleUpdateStockMultiple) | **POST** /api/v1/products/updatestockmultiple | Update the stock qty for multiple articles at once |
| [**searchSearch**](ProductsApi.md#searchSearch) | **POST** /api/v1/search | Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax |


<a id="articleCreateArticle"></a>
# **articleCreateArticle**
> Object articleCreateArticle(billbeeInterfacesBillbeeAPIModelArticleApiModel)

Creates a new product

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    BillbeeInterfacesBillbeeAPIModelArticleApiModel billbeeInterfacesBillbeeAPIModelArticleApiModel = new BillbeeInterfacesBillbeeAPIModelArticleApiModel(); // BillbeeInterfacesBillbeeAPIModelArticleApiModel | 
    try {
      Object result = apiInstance.articleCreateArticle(billbeeInterfacesBillbeeAPIModelArticleApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleCreateArticle");
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
| **billbeeInterfacesBillbeeAPIModelArticleApiModel** | [**BillbeeInterfacesBillbeeAPIModelArticleApiModel**](BillbeeInterfacesBillbeeAPIModelArticleApiModel.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleDeleteArticle"></a>
# **articleDeleteArticle**
> Object articleDeleteArticle(id)

Deletes a product

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Long id = 56L; // Long | The id of the Product
    try {
      Object result = apiInstance.articleDeleteArticle(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleDeleteArticle");
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
| **id** | **Long**| The id of the Product | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleDeleteImage"></a>
# **articleDeleteImage**
> Object articleDeleteImage(imageId)

Deletes a single image by id

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Long imageId = 56L; // Long | The image id
    try {
      Object result = apiInstance.articleDeleteImage(imageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleDeleteImage");
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
| **imageId** | **Long**| The image id | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleDeleteImageFromProduct"></a>
# **articleDeleteImageFromProduct**
> Object articleDeleteImageFromProduct(productId, imageId)

Deletes a single image from a product

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Long productId = 56L; // Long | The product id
    Long imageId = 56L; // Long | The image id
    try {
      Object result = apiInstance.articleDeleteImageFromProduct(productId, imageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleDeleteImageFromProduct");
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
| **productId** | **Long**| The product id | |
| **imageId** | **Long**| The image id | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleDeleteImages"></a>
# **articleDeleteImages**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel articleDeleteImages(requestBody)

Delete multiple images by id

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    List<Long> requestBody = Arrays.asList(); // List<Long> | 
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel result = apiInstance.articleDeleteImages(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleDeleteImages");
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
| **requestBody** | [**List&lt;Long&gt;**](Long.md)|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetArticle"></a>
# **articleGetArticle**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel articleGetArticle(id, lookupBy)

Queries a single article by id or by sku

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String id = "id_example"; // String | The id or the sku of the article to query
    String lookupBy = "lookupBy_example"; // String | Either the value id, ean or the value sku to specify the meaning of the id parameter.
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel result = apiInstance.articleGetArticle(id, lookupBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetArticle");
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
| **id** | **String**| The id or the sku of the article to query | |
| **lookupBy** | **String**| Either the value id, ean or the value sku to specify the meaning of the id parameter. | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetCategory"></a>
# **articleGetCategory**
> Object articleGetCategory()

GEts a list of all defined categories

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      Object result = apiInstance.articleGetCategory();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetCategory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetCustomField"></a>
# **articleGetCustomField**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel articleGetCustomField(id)

Queries a single custom field

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Long id = 56L; // Long | The id of the custom field to query
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel result = apiInstance.articleGetCustomField(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetCustomField");
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
| **id** | **Long**| The id of the custom field to query | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetCustomFields"></a>
# **articleGetCustomFields**
> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel articleGetCustomFields(page, pageSize)

Queries a list of all custom fields

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Integer page = 56; // Integer | 
    Integer pageSize = 56; // Integer | 
    try {
      RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel result = apiInstance.articleGetCustomFields(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetCustomFields");
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
| **page** | **Integer**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetImage"></a>
# **articleGetImage**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel articleGetImage(imageId)

Returns a single image by id

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Long imageId = 56L; // Long | The Id of the image
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel result = apiInstance.articleGetImage(imageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetImage");
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
| **imageId** | **Long**| The Id of the image | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetImageFromProduct"></a>
# **articleGetImageFromProduct**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel articleGetImageFromProduct(productId, imageId)

Returns a single image by id

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Long productId = 56L; // Long | The Id of the product
    Long imageId = 56L; // Long | The Id of the image
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel result = apiInstance.articleGetImageFromProduct(productId, imageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetImageFromProduct");
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
| **productId** | **Long**| The Id of the product | |
| **imageId** | **Long**| The Id of the image | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetImages"></a>
# **articleGetImages**
> RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel articleGetImages(productId)

Returns a list of all images of the product

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Long productId = 56L; // Long | The Id of the product
    try {
      RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel result = apiInstance.articleGetImages(productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetImages");
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
| **productId** | **Long**| The Id of the product | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetList"></a>
# **articleGetList**
> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel articleGetList(page, pageSize, minCreatedAt, minimumBillBeeArticleId, maximumBillBeeArticleId)

Get a list of all products

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Integer page = 56; // Integer | The current page to request starting with 1
    Integer pageSize = 56; // Integer | The pagesize for the result list. Values between 1 and 250 are allowed
    OffsetDateTime minCreatedAt = OffsetDateTime.now(); // OffsetDateTime | Optional the oldest create date of the articles to be returned
    Long minimumBillBeeArticleId = 56L; // Long | 
    Long maximumBillBeeArticleId = 56L; // Long | 
    try {
      RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel result = apiInstance.articleGetList(page, pageSize, minCreatedAt, minimumBillBeeArticleId, maximumBillBeeArticleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetList");
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
| **page** | **Integer**| The current page to request starting with 1 | [optional] |
| **pageSize** | **Integer**| The pagesize for the result list. Values between 1 and 250 are allowed | [optional] |
| **minCreatedAt** | **OffsetDateTime**| Optional the oldest create date of the articles to be returned | [optional] |
| **minimumBillBeeArticleId** | **Long**|  | [optional] |
| **maximumBillBeeArticleId** | **Long**|  | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetPatchableFields"></a>
# **articleGetPatchableFields**
> Object articleGetPatchableFields()

Returns a list of fields which can be updated with the patch call

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      Object result = apiInstance.articleGetPatchableFields();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetPatchableFields");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetReservedAmount"></a>
# **articleGetReservedAmount**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData articleGetReservedAmount(id, lookupBy, stockId)

Queries the reserved amount for a single article by id or by sku

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String id = "id_example"; // String | The id or the sku of the article to query
    String lookupBy = "lookupBy_example"; // String | Either the value id or the value sku to specify the meaning of the id parameter
    Long stockId = 56L; // Long | Optional the stock id if the multi stock feature is enabled
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData result = apiInstance.articleGetReservedAmount(id, lookupBy, stockId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetReservedAmount");
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
| **id** | **String**| The id or the sku of the article to query | |
| **lookupBy** | **String**| Either the value id or the value sku to specify the meaning of the id parameter | [optional] |
| **stockId** | **Long**| Optional the stock id if the multi stock feature is enabled | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleGetStocks"></a>
# **articleGetStocks**
> RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelStockResponseData articleGetStocks()

Query all defined stock locations

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelStockResponseData result = apiInstance.articleGetStocks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleGetStocks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelStockResponseData**](RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelStockResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articlePatchArticle"></a>
# **articlePatchArticle**
> Object articlePatchArticle(id, body)

Updates one or more fields of a product

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Long id = 56L; // Long | The id of the Product
    Object body = null; // Object | 
    try {
      Object result = apiInstance.articlePatchArticle(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articlePatchArticle");
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
| **id** | **Long**| The id of the Product | |
| **body** | **Object**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articlePutImage"></a>
# **articlePutImage**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel articlePutImage(productId, imageId, billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel)

Add or update an existing image of a product

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Long productId = 56L; // Long | The product id
    Long imageId = 56L; // Long | The image id. If you pass 0, the image will be added
    BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel = new BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel(); // BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel | The ArticleApiImageModel
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel result = apiInstance.articlePutImage(productId, imageId, billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articlePutImage");
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
| **productId** | **Long**| The product id | |
| **imageId** | **Long**| The image id. If you pass 0, the image will be added | |
| **billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel** | [**BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)| The ArticleApiImageModel | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articlePutImages"></a>
# **articlePutImages**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel articlePutImages(productId, billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel, replace)

Add multiple images to a product or replace the product images by the given images

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Long productId = 56L; // Long | The id of the product
    List<BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel> billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel = Arrays.asList(); // List<BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel> | An array of ArticleApiImageModel
    Boolean replace = true; // Boolean | If you pass true, the images will be replaced by the passed images. Otherwise the passed images will be appended to the product.
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel result = apiInstance.articlePutImages(productId, billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel, replace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articlePutImages");
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
| **productId** | **Long**| The id of the product | |
| **billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel** | [**List&lt;BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel&gt;**](BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)| An array of ArticleApiImageModel | |
| **replace** | **Boolean**| If you pass true, the images will be replaced by the passed images. Otherwise the passed images will be appended to the product. | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleUpdateStock"></a>
# **articleUpdateStock**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData articleUpdateStock(billbeeInterfacesBillbeeAPIModelUpdateStockApiModel)

Update the stock qty of an article

The article is specified by sku. You have to send the absolute value for the current stock

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel billbeeInterfacesBillbeeAPIModelUpdateStockApiModel = new BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel(); // BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel | 
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData result = apiInstance.articleUpdateStock(billbeeInterfacesBillbeeAPIModelUpdateStockApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleUpdateStock");
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
| **billbeeInterfacesBillbeeAPIModelUpdateStockApiModel** | [**BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel**](BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel.md)|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleUpdateStockCode"></a>
# **articleUpdateStockCode**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData articleUpdateStockCode(billbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel)

Update the stock code of an article

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel billbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel = new BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel(); // BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel | 
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData result = apiInstance.articleUpdateStockCode(billbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleUpdateStockCode");
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
| **billbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel** | [**BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel**](BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel.md)|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="articleUpdateStockMultiple"></a>
# **articleUpdateStockMultiple**
> List&lt;RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData&gt; articleUpdateStockMultiple(billbeeInterfacesBillbeeAPIModelUpdateStockApiModel)

Update the stock qty for multiple articles at once

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    List<BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel> billbeeInterfacesBillbeeAPIModelUpdateStockApiModel = Arrays.asList(); // List<BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel> | 
    try {
      List<RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData> result = apiInstance.articleUpdateStockMultiple(billbeeInterfacesBillbeeAPIModelUpdateStockApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#articleUpdateStockMultiple");
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
| **billbeeInterfacesBillbeeAPIModelUpdateStockApiModel** | [**List&lt;BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel&gt;**](BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel.md)|  | |

### Return type

[**List&lt;RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData&gt;**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="searchSearch"></a>
# **searchSearch**
> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel searchSearch(rechnungsdruckWebAppControllersApiSearchControllerSearchModel)

Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax

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
    defaultClient.setBasePath("https://app.billbee.io");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    RechnungsdruckWebAppControllersApiSearchControllerSearchModel rechnungsdruckWebAppControllersApiSearchControllerSearchModel = new RechnungsdruckWebAppControllersApiSearchControllerSearchModel(); // RechnungsdruckWebAppControllersApiSearchControllerSearchModel | 
    try {
      RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel result = apiInstance.searchSearch(rechnungsdruckWebAppControllersApiSearchControllerSearchModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#searchSearch");
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
| **rechnungsdruckWebAppControllersApiSearchControllerSearchModel** | [**RechnungsdruckWebAppControllersApiSearchControllerSearchModel**](RechnungsdruckWebAppControllersApiSearchControllerSearchModel.md)|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel**](RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


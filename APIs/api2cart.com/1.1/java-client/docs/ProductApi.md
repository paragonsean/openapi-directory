# ProductApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productAdd**](ProductApi.md#productAdd) | **POST** /product.add.json |  |
| [**productAttributeList**](ProductApi.md#productAttributeList) | **GET** /product.attribute.list.json |  |
| [**productAttributeValueSet**](ProductApi.md#productAttributeValueSet) | **POST** /product.attribute.value.set.json |  |
| [**productAttributeValueUnset**](ProductApi.md#productAttributeValueUnset) | **POST** /product.attribute.value.unset.json |  |
| [**productBrandList**](ProductApi.md#productBrandList) | **GET** /product.brand.list.json |  |
| [**productChildItemFind**](ProductApi.md#productChildItemFind) | **GET** /product.child_item.find.json |  |
| [**productChildItemInfo**](ProductApi.md#productChildItemInfo) | **GET** /product.child_item.info.json |  |
| [**productChildItemList**](ProductApi.md#productChildItemList) | **GET** /product.child_item.list.json |  |
| [**productCount**](ProductApi.md#productCount) | **GET** /product.count.json |  |
| [**productCurrencyAdd**](ProductApi.md#productCurrencyAdd) | **POST** /product.currency.add.json |  |
| [**productCurrencyList**](ProductApi.md#productCurrencyList) | **GET** /product.currency.list.json |  |
| [**productDelete**](ProductApi.md#productDelete) | **DELETE** /product.delete.json |  |
| [**productFields**](ProductApi.md#productFields) | **GET** /product.fields.json |  |
| [**productFind**](ProductApi.md#productFind) | **GET** /product.find.json |  |
| [**productImageAdd**](ProductApi.md#productImageAdd) | **POST** /product.image.add.json |  |
| [**productImageDelete**](ProductApi.md#productImageDelete) | **DELETE** /product.image.delete.json |  |
| [**productImageUpdate**](ProductApi.md#productImageUpdate) | **PUT** /product.image.update.json |  |
| [**productInfo**](ProductApi.md#productInfo) | **GET** /product.info.json |  |
| [**productList**](ProductApi.md#productList) | **GET** /product.list.json |  |
| [**productManufacturerAdd**](ProductApi.md#productManufacturerAdd) | **POST** /product.manufacturer.add.json |  |
| [**productOptionAdd**](ProductApi.md#productOptionAdd) | **POST** /product.option.add.json |  |
| [**productOptionAssign**](ProductApi.md#productOptionAssign) | **POST** /product.option.assign.json |  |
| [**productOptionList**](ProductApi.md#productOptionList) | **GET** /product.option.list.json |  |
| [**productOptionValueAdd**](ProductApi.md#productOptionValueAdd) | **POST** /product.option.value.add.json |  |
| [**productOptionValueAssign**](ProductApi.md#productOptionValueAssign) | **POST** /product.option.value.assign.json |  |
| [**productOptionValueUpdate**](ProductApi.md#productOptionValueUpdate) | **PUT** /product.option.value.update.json |  |
| [**productPriceAdd**](ProductApi.md#productPriceAdd) | **POST** /product.price.add.json |  |
| [**productPriceDelete**](ProductApi.md#productPriceDelete) | **DELETE** /product.price.delete.json |  |
| [**productPriceUpdate**](ProductApi.md#productPriceUpdate) | **PUT** /product.price.update.json |  |
| [**productReviewList**](ProductApi.md#productReviewList) | **GET** /product.review.list.json |  |
| [**productStoreAssign**](ProductApi.md#productStoreAssign) | **POST** /product.store.assign.json |  |
| [**productTaxAdd**](ProductApi.md#productTaxAdd) | **POST** /product.tax.add.json |  |
| [**productUpdate**](ProductApi.md#productUpdate) | **PUT** /product.update.json |  |
| [**productVariantAdd**](ProductApi.md#productVariantAdd) | **POST** /product.variant.add.json |  |
| [**productVariantCount**](ProductApi.md#productVariantCount) | **GET** /product.variant.count.json |  |
| [**productVariantDelete**](ProductApi.md#productVariantDelete) | **DELETE** /product.variant.delete.json |  |
| [**productVariantImageAdd**](ProductApi.md#productVariantImageAdd) | **POST** /product.variant.image.add.json |  |
| [**productVariantImageDelete**](ProductApi.md#productVariantImageDelete) | **DELETE** /product.variant.image.delete.json |  |
| [**productVariantInfo**](ProductApi.md#productVariantInfo) | **GET** /product.variant.info.json |  |
| [**productVariantList**](ProductApi.md#productVariantList) | **GET** /product.variant.list.json |  |
| [**productVariantPriceAdd**](ProductApi.md#productVariantPriceAdd) | **POST** /product.variant.price.add.json |  |
| [**productVariantPriceDelete**](ProductApi.md#productVariantPriceDelete) | **DELETE** /product.variant.price.delete.json |  |
| [**productVariantPriceUpdate**](ProductApi.md#productVariantPriceUpdate) | **PUT** /product.variant.price.update.json |  |
| [**productVariantUpdate**](ProductApi.md#productVariantUpdate) | **PUT** /product.variant.update.json |  |


<a id="productAdd"></a>
# **productAdd**
> ProductAdd200Response productAdd(productAdd)



Add new product to store.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductAdd productAdd = new ProductAdd(); // ProductAdd | 
    try {
      ProductAdd200Response result = apiInstance.productAdd(productAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productAdd");
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
| **productAdd** | [**ProductAdd**](ProductAdd.md)|  | |

### Return type

[**ProductAdd200Response**](ProductAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productAttributeList"></a>
# **productAttributeList**
> ModelResponseProductAttributeList productAttributeList(productId, attributeId, variantId, pageCursor, start, count, attributeGroupId, setName, langId, storeId, sortBy, sortDirection, params, responseFields, exclude)



Get list of attributes and values.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Retrieves attributes specified by product id
    String attributeId = "attributeId_example"; // String | Retrieves info for specified attribute_id
    String variantId = "variantId_example"; // String | Defines product's variants specified by variant id
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String attributeGroupId = "attributeGroupId_example"; // String | Filter by attribute_group_id
    String setName = "setName_example"; // String | Retrieves attributes specified by set_name in Magento
    String langId = "langId_example"; // String | Retrieves attributes specified by language id
    String storeId = "storeId_example"; // String | Retrieves attributes specified by store id
    String sortBy = "attribute_id"; // String | Set field to sort by
    String sortDirection = "asc"; // String | Set sorting direction
    String params = "attribute_id,name"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    try {
      ModelResponseProductAttributeList result = apiInstance.productAttributeList(productId, attributeId, variantId, pageCursor, start, count, attributeGroupId, setName, langId, storeId, sortBy, sortDirection, params, responseFields, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productAttributeList");
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
| **productId** | **String**| Retrieves attributes specified by product id | |
| **attributeId** | **String**| Retrieves info for specified attribute_id | [optional] |
| **variantId** | **String**| Defines product&#39;s variants specified by variant id | [optional] |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **attributeGroupId** | **String**| Filter by attribute_group_id | [optional] |
| **setName** | **String**| Retrieves attributes specified by set_name in Magento | [optional] |
| **langId** | **String**| Retrieves attributes specified by language id | [optional] |
| **storeId** | **String**| Retrieves attributes specified by store id | [optional] |
| **sortBy** | **String**| Set field to sort by | [optional] [default to attribute_id] |
| **sortDirection** | **String**| Set sorting direction | [optional] [default to asc] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to attribute_id,name] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |

### Return type

[**ModelResponseProductAttributeList**](ModelResponseProductAttributeList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productAttributeValueSet"></a>
# **productAttributeValueSet**
> ProductAttributeValueSet200Response productAttributeValueSet(productId, attributeId, attributeGroupId, attributeName, value, valueId, langId, storeId)



Set attribute value to product.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Defines product id where the attribute should be added
    String attributeId = "attributeId_example"; // String | Filter by attribute_id
    String attributeGroupId = "attributeGroupId_example"; // String | Filter by attribute_group_id
    String attributeName = "attributeName_example"; // String | Define attribute name
    String value = "value_example"; // String | Define attribute value
    Integer valueId = 56; // Integer | Define attribute value id
    String langId = "langId_example"; // String | Language id
    String storeId = "storeId_example"; // String | Store Id
    try {
      ProductAttributeValueSet200Response result = apiInstance.productAttributeValueSet(productId, attributeId, attributeGroupId, attributeName, value, valueId, langId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productAttributeValueSet");
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
| **productId** | **String**| Defines product id where the attribute should be added | |
| **attributeId** | **String**| Filter by attribute_id | [optional] |
| **attributeGroupId** | **String**| Filter by attribute_group_id | [optional] |
| **attributeName** | **String**| Define attribute name | [optional] |
| **value** | **String**| Define attribute value | [optional] |
| **valueId** | **Integer**| Define attribute value id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**ProductAttributeValueSet200Response**](ProductAttributeValueSet200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productAttributeValueUnset"></a>
# **productAttributeValueUnset**
> ProductAttributeValueUnset200Response productAttributeValueUnset(productId, attributeId, storeId, includeDefault, reindex, clearCache)



Removes attribute value for a product.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Product id
    String attributeId = "attributeId_example"; // String | Attribute Id
    String storeId = "storeId_example"; // String | Store Id
    Boolean includeDefault = false; // Boolean | Boolean, whether or not to unset default value of the attribute, if applicable
    Boolean reindex = true; // Boolean | Is reindex required
    Boolean clearCache = true; // Boolean | Is cache clear required
    try {
      ProductAttributeValueUnset200Response result = apiInstance.productAttributeValueUnset(productId, attributeId, storeId, includeDefault, reindex, clearCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productAttributeValueUnset");
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
| **productId** | **String**| Product id | |
| **attributeId** | **String**| Attribute Id | |
| **storeId** | **String**| Store Id | [optional] |
| **includeDefault** | **Boolean**| Boolean, whether or not to unset default value of the attribute, if applicable | [optional] [default to false] |
| **reindex** | **Boolean**| Is reindex required | [optional] [default to true] |
| **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true] |

### Return type

[**ProductAttributeValueUnset200Response**](ProductAttributeValueUnset200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productBrandList"></a>
# **productBrandList**
> ProductBrandList200Response productBrandList(start, count, params, brandIds, exclude, storeId, langId, createdFrom, createdTo, modifiedFrom, modifiedTo, responseFields)



Get list of brands from your store.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String params = "id,name,short_description,active,url"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String brandIds = "brandIds_example"; // String | Retrieves brands specified by brand ids
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    try {
      ProductBrandList200Response result = apiInstance.productBrandList(start, count, params, brandIds, exclude, storeId, langId, createdFrom, createdTo, modifiedFrom, modifiedTo, responseFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productBrandList");
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
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,short_description,active,url] |
| **brandIds** | **String**| Retrieves brands specified by brand ids | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |

### Return type

[**ProductBrandList200Response**](ProductBrandList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productChildItemFind"></a>
# **productChildItemFind**
> ProductChildItemFind200Response productChildItemFind(findValue, findWhere, findParams, storeId)



Search product child item (bundled item or configurable product variant) in store catalog.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String findValue = "findValue_example"; // String | Entity search that is specified by some value
    String findWhere = "name"; // String | Entity search that is specified by the comma-separated unique fields
    String findParams = "whole_words"; // String | Entity search that is specified by comma-separated parameters
    String storeId = "storeId_example"; // String | Store Id
    try {
      ProductChildItemFind200Response result = apiInstance.productChildItemFind(findValue, findWhere, findParams, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productChildItemFind");
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
| **findValue** | **String**| Entity search that is specified by some value | |
| **findWhere** | **String**| Entity search that is specified by the comma-separated unique fields | [optional] [default to name] |
| **findParams** | **String**| Entity search that is specified by comma-separated parameters | [optional] [default to whole_words] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**ProductChildItemFind200Response**](ProductChildItemFind200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productChildItemInfo"></a>
# **productChildItemInfo**
> ProductChildItemInfo200Response productChildItemInfo(productId, id, params, responseFields, exclude, storeId, langId, currencyId)



Get child for specific product.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Filter by parent product id
    String id = "id_example"; // String | Entity id
    String params = "force_all"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    String currencyId = "currencyId_example"; // String | Currency Id
    try {
      ProductChildItemInfo200Response result = apiInstance.productChildItemInfo(productId, id, params, responseFields, exclude, storeId, langId, currencyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productChildItemInfo");
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
| **productId** | **String**| Filter by parent product id | |
| **id** | **String**| Entity id | |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **currencyId** | **String**| Currency Id | [optional] |

### Return type

[**ProductChildItemInfo200Response**](ProductChildItemInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productChildItemList"></a>
# **productChildItemList**
> ModelResponseProductChildItemList productChildItemList(pageCursor, start, count, params, responseFields, exclude, createdFrom, createdTo, modifiedFrom, modifiedTo, productId, productIds, storeId, langId, currencyId, availSale, reportRequestId, disableReportCache)



Get child items list of specific product(s).

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String pageCursor = "pageCursor_example"; // String | Used to retrieve products child items via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String params = "force_all"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String productId = "productId_example"; // String | Filter by parent product id
    String productIds = "productIds_example"; // String | Filter by parent product ids
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    String currencyId = "currencyId_example"; // String | Currency Id
    Boolean availSale = true; // Boolean | Specifies the set of available/not available products for sale
    String reportRequestId = "reportRequestId_example"; // String | Report request id
    Boolean disableReportCache = false; // Boolean | Disable report cache for current request
    try {
      ModelResponseProductChildItemList result = apiInstance.productChildItemList(pageCursor, start, count, params, responseFields, exclude, createdFrom, createdTo, modifiedFrom, modifiedTo, productId, productIds, storeId, langId, currencyId, availSale, reportRequestId, disableReportCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productChildItemList");
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
| **pageCursor** | **String**| Used to retrieve products child items via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **productId** | **String**| Filter by parent product id | [optional] |
| **productIds** | **String**| Filter by parent product ids | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **currencyId** | **String**| Currency Id | [optional] |
| **availSale** | **Boolean**| Specifies the set of available/not available products for sale | [optional] |
| **reportRequestId** | **String**| Report request id | [optional] |
| **disableReportCache** | **Boolean**| Disable report cache for current request | [optional] [default to false] |

### Return type

[**ModelResponseProductChildItemList**](ModelResponseProductChildItemList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productCount"></a>
# **productCount**
> ProductCount200Response productCount(categoryId, createdFrom, createdTo, modifiedFrom, modifiedTo, availView, availSale, storeId, langId, productIds, reportRequestId, disableReportCache, brandName, productAttributes, status, type)



Count products in store.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String categoryId = "categoryId_example"; // String | Counts products specified by category id
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    Boolean availView = true; // Boolean | Specifies the set of visible/invisible products
    Boolean availSale = true; // Boolean | Specifies the set of available/not available products for sale
    String storeId = "storeId_example"; // String | Counts products specified by store id
    String langId = "langId_example"; // String | Counts products specified by language id
    String productIds = "productIds_example"; // String | Counts products specified by product ids
    String reportRequestId = "reportRequestId_example"; // String | Report request id
    Boolean disableReportCache = false; // Boolean | Disable report cache for current request
    String brandName = "brandName_example"; // String | Retrieves brands specified by brand name
    List<String> productAttributes = Arrays.asList(); // List<String> | Defines product attributes
    String status = "status_example"; // String | Defines product's status
    String type = "type_example"; // String | Defines products's type
    try {
      ProductCount200Response result = apiInstance.productCount(categoryId, createdFrom, createdTo, modifiedFrom, modifiedTo, availView, availSale, storeId, langId, productIds, reportRequestId, disableReportCache, brandName, productAttributes, status, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productCount");
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
| **categoryId** | **String**| Counts products specified by category id | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **availView** | **Boolean**| Specifies the set of visible/invisible products | [optional] |
| **availSale** | **Boolean**| Specifies the set of available/not available products for sale | [optional] |
| **storeId** | **String**| Counts products specified by store id | [optional] |
| **langId** | **String**| Counts products specified by language id | [optional] |
| **productIds** | **String**| Counts products specified by product ids | [optional] |
| **reportRequestId** | **String**| Report request id | [optional] |
| **disableReportCache** | **Boolean**| Disable report cache for current request | [optional] [default to false] |
| **brandName** | **String**| Retrieves brands specified by brand name | [optional] |
| **productAttributes** | [**List&lt;String&gt;**](String.md)| Defines product attributes | [optional] |
| **status** | **String**| Defines product&#39;s status | [optional] |
| **type** | **String**| Defines products&#39;s type | [optional] |

### Return type

[**ProductCount200Response**](ProductCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productCurrencyAdd"></a>
# **productCurrencyAdd**
> ProductCurrencyAdd200Response productCurrencyAdd(iso3, rate, name, avail, symbolLeft, symbolRight, _default)



Add currency and/or set default in store

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String iso3 = "iso3_example"; // String | Specifies standardized currency code
    BigDecimal rate = new BigDecimal(78); // BigDecimal | Defines the numerical identifier against to the major currency
    String name = "name_example"; // String | Defines currency's name
    Boolean avail = true; // Boolean | Specifies whether the currency is available
    String symbolLeft = "symbolLeft_example"; // String | Defines the symbol that is located before the currency
    String symbolRight = "symbolRight_example"; // String | Defines the symbol that is located after the currency
    Boolean _default = false; // Boolean | Specifies currency's default meaning
    try {
      ProductCurrencyAdd200Response result = apiInstance.productCurrencyAdd(iso3, rate, name, avail, symbolLeft, symbolRight, _default);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productCurrencyAdd");
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
| **iso3** | **String**| Specifies standardized currency code | |
| **rate** | **BigDecimal**| Defines the numerical identifier against to the major currency | |
| **name** | **String**| Defines currency&#39;s name | [optional] |
| **avail** | **Boolean**| Specifies whether the currency is available | [optional] [default to true] |
| **symbolLeft** | **String**| Defines the symbol that is located before the currency | [optional] |
| **symbolRight** | **String**| Defines the symbol that is located after the currency | [optional] |
| **_default** | **Boolean**| Specifies currency&#39;s default meaning | [optional] [default to false] |

### Return type

[**ProductCurrencyAdd200Response**](ProductCurrencyAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productCurrencyList"></a>
# **productCurrencyList**
> ProductCurrencyList200Response productCurrencyList(start, count, params, pageCursor, exclude, responseFields, _default, avail)



Get list of currencies

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String params = "name,iso3,default,avail"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    Boolean _default = true; // Boolean | Specifies the set of default/not default currencies
    Boolean avail = true; // Boolean | Specifies the set of available/not available currencies
    try {
      ProductCurrencyList200Response result = apiInstance.productCurrencyList(start, count, params, pageCursor, exclude, responseFields, _default, avail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productCurrencyList");
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
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to name,iso3,default,avail] |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **_default** | **Boolean**| Specifies the set of default/not default currencies | [optional] |
| **avail** | **Boolean**| Specifies the set of available/not available currencies | [optional] |

### Return type

[**ProductCurrencyList200Response**](ProductCurrencyList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productDelete"></a>
# **productDelete**
> ProductDelete200Response productDelete(id)



Product delete

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String id = "id_example"; // String | Product id that will be removed
    try {
      ProductDelete200Response result = apiInstance.productDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productDelete");
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
| **id** | **String**| Product id that will be removed | |

### Return type

[**ProductDelete200Response**](ProductDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productFields"></a>
# **productFields**
> CartConfigUpdate200Response productFields()



Retrieve all available fields for product item in store.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    try {
      CartConfigUpdate200Response result = apiInstance.productFields();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productFields");
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

[**CartConfigUpdate200Response**](CartConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productFind"></a>
# **productFind**
> ProductFind200Response productFind(findValue, findWhere, findParams, findWhat, langId, storeId)



Search product in store catalog. \&quot;Apple\&quot; is specified here by default.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String findValue = "findValue_example"; // String | Entity search that is specified by some value
    String findWhere = "name"; // String | Entity search that is specified by the comma-separated unique fields
    String findParams = "whole_words"; // String | Entity search that is specified by comma-separated parameters
    String findWhat = "product"; // String | Parameter's value specifies the entity that has to be found
    String langId = "langId_example"; // String | Search products specified by language id
    String storeId = "storeId_example"; // String | Store Id
    try {
      ProductFind200Response result = apiInstance.productFind(findValue, findWhere, findParams, findWhat, langId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productFind");
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
| **findValue** | **String**| Entity search that is specified by some value | |
| **findWhere** | **String**| Entity search that is specified by the comma-separated unique fields | [optional] [default to name] |
| **findParams** | **String**| Entity search that is specified by comma-separated parameters | [optional] [default to whole_words] |
| **findWhat** | **String**| Parameter&#39;s value specifies the entity that has to be found | [optional] [default to product] |
| **langId** | **String**| Search products specified by language id | [optional] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**ProductFind200Response**](ProductFind200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productImageAdd"></a>
# **productImageAdd**
> ProductImageAdd200Response productImageAdd(productImageAdd)



Add image to product

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductImageAdd productImageAdd = new ProductImageAdd(); // ProductImageAdd | 
    try {
      ProductImageAdd200Response result = apiInstance.productImageAdd(productImageAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productImageAdd");
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
| **productImageAdd** | [**ProductImageAdd**](ProductImageAdd.md)|  | |

### Return type

[**ProductImageAdd200Response**](ProductImageAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productImageDelete"></a>
# **productImageDelete**
> AttributeDelete200Response productImageDelete(productId, id, storeId)



Delete image

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Defines product id where the image should be deleted
    String id = "id_example"; // String | Entity id
    String storeId = "storeId_example"; // String | Store Id
    try {
      AttributeDelete200Response result = apiInstance.productImageDelete(productId, id, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productImageDelete");
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
| **productId** | **String**| Defines product id where the image should be deleted | |
| **id** | **String**| Entity id | |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productImageUpdate"></a>
# **productImageUpdate**
> ProductImageUpdate200Response productImageUpdate(productId, id, variantIds, imageName, type, label, position, storeId, langId, hidden)



Update details of image

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Defines product id where the image should be updated
    String id = "id_example"; // String | Defines image update specified by image id
    String variantIds = "variantIds_example"; // String | Defines product's variants ids
    String imageName = "imageName_example"; // String | Defines image's name
    String type = "additional"; // String | Defines image's types that are specified by comma-separated list
    String label = "label_example"; // String | Defines alternative text that has to be attached to the picture
    Integer position = 56; // Integer | Defines image’s position in the list
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    Boolean hidden = true; // Boolean | Define is hide image
    try {
      ProductImageUpdate200Response result = apiInstance.productImageUpdate(productId, id, variantIds, imageName, type, label, position, storeId, langId, hidden);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productImageUpdate");
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
| **productId** | **String**| Defines product id where the image should be updated | |
| **id** | **String**| Defines image update specified by image id | |
| **variantIds** | **String**| Defines product&#39;s variants ids | [optional] |
| **imageName** | **String**| Defines image&#39;s name | [optional] |
| **type** | **String**| Defines image&#39;s types that are specified by comma-separated list | [optional] [default to additional] |
| **label** | **String**| Defines alternative text that has to be attached to the picture | [optional] |
| **position** | **Integer**| Defines image’s position in the list | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **hidden** | **Boolean**| Define is hide image | [optional] |

### Return type

[**ProductImageUpdate200Response**](ProductImageUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productInfo"></a>
# **productInfo**
> ProductInfo200Response productInfo(id, params, responseFields, exclude, storeId, langId, currencyId, reportRequestId, disableReportCache)



Get product info about product ID *** or specify other product ID.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String id = "id_example"; // String | Retrieves product's info specified by product id
    String params = "id,name,description,price,categories_ids"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String storeId = "storeId_example"; // String | Retrieves product info specified by store id
    String langId = "langId_example"; // String | Retrieves product info specified by language id
    String currencyId = "currencyId_example"; // String | Currency Id
    String reportRequestId = "reportRequestId_example"; // String | Report request id
    Boolean disableReportCache = false; // Boolean | Disable report cache for current request
    try {
      ProductInfo200Response result = apiInstance.productInfo(id, params, responseFields, exclude, storeId, langId, currencyId, reportRequestId, disableReportCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productInfo");
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
| **id** | **String**| Retrieves product&#39;s info specified by product id | |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description,price,categories_ids] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **storeId** | **String**| Retrieves product info specified by store id | [optional] |
| **langId** | **String**| Retrieves product info specified by language id | [optional] |
| **currencyId** | **String**| Currency Id | [optional] |
| **reportRequestId** | **String**| Report request id | [optional] |
| **disableReportCache** | **Boolean**| Disable report cache for current request | [optional] [default to false] |

### Return type

[**ProductInfo200Response**](ProductInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productList"></a>
# **productList**
> ModelResponseProductList productList(pageCursor, start, count, params, responseFields, exclude, categoryId, createdFrom, createdTo, modifiedFrom, modifiedTo, availView, availSale, storeId, langId, currencyId, productIds, sinceId, reportRequestId, disableReportCache, sortBy, sortDirection, sku, disableCache, brandName, productAttributes, status, type)



Get list of products from your store. Returns 10 products by default.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String pageCursor = "pageCursor_example"; // String | Used to retrieve products via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String params = "id,name,description,price,categories_ids"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String categoryId = "categoryId_example"; // String | Retrieves products specified by category id
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    Boolean availView = true; // Boolean | Specifies the set of visible/invisible products
    Boolean availSale = true; // Boolean | Specifies the set of available/not available products for sale
    String storeId = "storeId_example"; // String | Retrieves products specified by store id
    String langId = "langId_example"; // String | Retrieves products specified by language id
    String currencyId = "currencyId_example"; // String | Currency Id
    String productIds = "productIds_example"; // String | Retrieves products specified by product ids
    Integer sinceId = 56; // Integer | Retrieve entities starting from the specified id.
    String reportRequestId = "reportRequestId_example"; // String | Report request id
    Boolean disableReportCache = false; // Boolean | Disable report cache for current request
    String sortBy = "id"; // String | Set field to sort by
    String sortDirection = "asc"; // String | Set sorting direction
    String sku = "sku_example"; // String | Filter by product's sku
    Boolean disableCache = false; // Boolean | Disable cache for current request
    String brandName = "brandName_example"; // String | Retrieves brands specified by brand name
    List<String> productAttributes = Arrays.asList(); // List<String> | Defines product attributes
    String status = "status_example"; // String | Defines product's status
    String type = "type_example"; // String | Defines products's type
    try {
      ModelResponseProductList result = apiInstance.productList(pageCursor, start, count, params, responseFields, exclude, categoryId, createdFrom, createdTo, modifiedFrom, modifiedTo, availView, availSale, storeId, langId, currencyId, productIds, sinceId, reportRequestId, disableReportCache, sortBy, sortDirection, sku, disableCache, brandName, productAttributes, status, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productList");
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
| **pageCursor** | **String**| Used to retrieve products via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description,price,categories_ids] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **categoryId** | **String**| Retrieves products specified by category id | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **availView** | **Boolean**| Specifies the set of visible/invisible products | [optional] |
| **availSale** | **Boolean**| Specifies the set of available/not available products for sale | [optional] |
| **storeId** | **String**| Retrieves products specified by store id | [optional] |
| **langId** | **String**| Retrieves products specified by language id | [optional] |
| **currencyId** | **String**| Currency Id | [optional] |
| **productIds** | **String**| Retrieves products specified by product ids | [optional] |
| **sinceId** | **Integer**| Retrieve entities starting from the specified id. | [optional] |
| **reportRequestId** | **String**| Report request id | [optional] |
| **disableReportCache** | **Boolean**| Disable report cache for current request | [optional] [default to false] |
| **sortBy** | **String**| Set field to sort by | [optional] [default to id] |
| **sortDirection** | **String**| Set sorting direction | [optional] [default to asc] |
| **sku** | **String**| Filter by product&#39;s sku | [optional] |
| **disableCache** | **Boolean**| Disable cache for current request | [optional] [default to false] |
| **brandName** | **String**| Retrieves brands specified by brand name | [optional] |
| **productAttributes** | [**List&lt;String&gt;**](String.md)| Defines product attributes | [optional] |
| **status** | **String**| Defines product&#39;s status | [optional] |
| **type** | **String**| Defines products&#39;s type | [optional] |

### Return type

[**ModelResponseProductList**](ModelResponseProductList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productManufacturerAdd"></a>
# **productManufacturerAdd**
> ProductManufacturerAdd200Response productManufacturerAdd(productId, manufacturer)



Add manufacturer to store and assign to product

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Defines products specified by product id
    String manufacturer = "manufacturer_example"; // String | Defines product’s manufacturer's name
    try {
      ProductManufacturerAdd200Response result = apiInstance.productManufacturerAdd(productId, manufacturer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productManufacturerAdd");
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
| **productId** | **String**| Defines products specified by product id | |
| **manufacturer** | **String**| Defines product’s manufacturer&#39;s name | |

### Return type

[**ProductManufacturerAdd200Response**](ProductManufacturerAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productOptionAdd"></a>
# **productOptionAdd**
> ProductOptionAdd200Response productOptionAdd(name, type, productId, defaultOptionValue, optionValues, description, avail, sortOrder, required, clearCache)



Add product option from store.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String name = "name_example"; // String | Defines option's name
    String type = "option_type_select"; // String | Defines option's type that has to be added
    String productId = "productId_example"; // String | Defines product id where the option should be added
    String defaultOptionValue = "defaultOptionValue_example"; // String | Defines default option value that has to be added
    String optionValues = "optionValues_example"; // String | Defines option values that has to be added
    String description = "description_example"; // String | Defines option's description
    Boolean avail = true; // Boolean | Defines whether the option is available
    Integer sortOrder = 0; // Integer | Sort number in the list
    Boolean required = false; // Boolean | Defines if the option is required
    Boolean clearCache = true; // Boolean | Is cache clear required
    try {
      ProductOptionAdd200Response result = apiInstance.productOptionAdd(name, type, productId, defaultOptionValue, optionValues, description, avail, sortOrder, required, clearCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productOptionAdd");
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
| **name** | **String**| Defines option&#39;s name | |
| **type** | **String**| Defines option&#39;s type that has to be added | [enum: option_type_select, option_type_text, option_type_radio, option_type_checkbox, option_type_textarea, option_type_readonly, option_type_multiselect, option_type_multicheckbox, option_type_file, option_type_date, option_type_datetime, option_type_time] |
| **productId** | **String**| Defines product id where the option should be added | [optional] |
| **defaultOptionValue** | **String**| Defines default option value that has to be added | [optional] |
| **optionValues** | **String**| Defines option values that has to be added | [optional] |
| **description** | **String**| Defines option&#39;s description | [optional] |
| **avail** | **Boolean**| Defines whether the option is available | [optional] [default to true] |
| **sortOrder** | **Integer**| Sort number in the list | [optional] [default to 0] |
| **required** | **Boolean**| Defines if the option is required | [optional] [default to false] |
| **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true] |

### Return type

[**ProductOptionAdd200Response**](ProductOptionAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productOptionAssign"></a>
# **productOptionAssign**
> ProductOptionAssign200Response productOptionAssign(productId, optionId, required, sortOrder, optionValues, clearCache)



Assign option from product.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Defines product id where the option should be assigned
    String optionId = "optionId_example"; // String | Defines option id which has to be assigned
    Boolean required = false; // Boolean | Defines if the option is required
    Integer sortOrder = 0; // Integer | Sort number in the list
    String optionValues = "optionValues_example"; // String | Defines option values that has to be assigned
    Boolean clearCache = true; // Boolean | Is cache clear required
    try {
      ProductOptionAssign200Response result = apiInstance.productOptionAssign(productId, optionId, required, sortOrder, optionValues, clearCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productOptionAssign");
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
| **productId** | **String**| Defines product id where the option should be assigned | |
| **optionId** | **String**| Defines option id which has to be assigned | |
| **required** | **Boolean**| Defines if the option is required | [optional] [default to false] |
| **sortOrder** | **Integer**| Sort number in the list | [optional] [default to 0] |
| **optionValues** | **String**| Defines option values that has to be assigned | [optional] |
| **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true] |

### Return type

[**ProductOptionAssign200Response**](ProductOptionAssign200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productOptionList"></a>
# **productOptionList**
> ProductOptionList200Response productOptionList(start, count, params, exclude, responseFields, productId, langId, storeId)



Get list of options.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String params = "id,name,description"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String productId = "productId_example"; // String | Retrieves products' options specified by product id
    String langId = "langId_example"; // String | Language id
    String storeId = "storeId_example"; // String | Store Id
    try {
      ProductOptionList200Response result = apiInstance.productOptionList(start, count, params, exclude, responseFields, productId, langId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productOptionList");
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
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **productId** | **String**| Retrieves products&#39; options specified by product id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**ProductOptionList200Response**](ProductOptionList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productOptionValueAdd"></a>
# **productOptionValueAdd**
> ProductOptionValueAdd200Response productOptionValueAdd(productId, optionId, optionValue, sortOrder, clearCache)



Add product option item from option.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Defines product id where the option value should be added
    String optionId = "optionId_example"; // String | Defines option id where the value has to be added
    String optionValue = "optionValue_example"; // String | Defines option value that has to be added
    Integer sortOrder = 0; // Integer | Sort number in the list
    Boolean clearCache = true; // Boolean | Is cache clear required
    try {
      ProductOptionValueAdd200Response result = apiInstance.productOptionValueAdd(productId, optionId, optionValue, sortOrder, clearCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productOptionValueAdd");
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
| **productId** | **String**| Defines product id where the option value should be added | |
| **optionId** | **String**| Defines option id where the value has to be added | |
| **optionValue** | **String**| Defines option value that has to be added | |
| **sortOrder** | **Integer**| Sort number in the list | [optional] [default to 0] |
| **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true] |

### Return type

[**ProductOptionValueAdd200Response**](ProductOptionValueAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productOptionValueAssign"></a>
# **productOptionValueAssign**
> ProductOptionValueAssign200Response productOptionValueAssign(productOptionId, optionValueId, clearCache)



Assign product option item from product.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    Integer productOptionId = 56; // Integer | Defines product's option id where the value has to be assigned
    Integer optionValueId = 56; // Integer | Defines value id that has to be assigned
    Boolean clearCache = true; // Boolean | Is cache clear required
    try {
      ProductOptionValueAssign200Response result = apiInstance.productOptionValueAssign(productOptionId, optionValueId, clearCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productOptionValueAssign");
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
| **productOptionId** | **Integer**| Defines product&#39;s option id where the value has to be assigned | |
| **optionValueId** | **Integer**| Defines value id that has to be assigned | |
| **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true] |

### Return type

[**ProductOptionValueAssign200Response**](ProductOptionValueAssign200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productOptionValueUpdate"></a>
# **productOptionValueUpdate**
> AccountConfigUpdate200Response productOptionValueUpdate(productId, optionId, optionValueId, optionValue, price, quantity, clearCache)



Update product option item from option.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Defines product id where the option value should be updated
    String optionId = "optionId_example"; // String | Defines option id where the value has to be updated
    Integer optionValueId = 56; // Integer | Defines value id that has to be assigned
    String optionValue = "optionValue_example"; // String | Defines option value that has to be added
    BigDecimal price = new BigDecimal(78); // BigDecimal | Defines new product option price
    BigDecimal quantity = new BigDecimal(78); // BigDecimal | Defines new products' options quantity
    Boolean clearCache = true; // Boolean | Is cache clear required
    try {
      AccountConfigUpdate200Response result = apiInstance.productOptionValueUpdate(productId, optionId, optionValueId, optionValue, price, quantity, clearCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productOptionValueUpdate");
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
| **productId** | **String**| Defines product id where the option value should be updated | |
| **optionId** | **String**| Defines option id where the value has to be updated | |
| **optionValueId** | **Integer**| Defines value id that has to be assigned | |
| **optionValue** | **String**| Defines option value that has to be added | |
| **price** | **BigDecimal**| Defines new product option price | [optional] |
| **quantity** | **BigDecimal**| Defines new products&#39; options quantity | [optional] |
| **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true] |

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productPriceAdd"></a>
# **productPriceAdd**
> CartValidate200Response productPriceAdd(productPriceAdd)



Add some prices to the product.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductPriceAdd productPriceAdd = new ProductPriceAdd(); // ProductPriceAdd | 
    try {
      CartValidate200Response result = apiInstance.productPriceAdd(productPriceAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productPriceAdd");
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
| **productPriceAdd** | [**ProductPriceAdd**](ProductPriceAdd.md)|  | |

### Return type

[**CartValidate200Response**](CartValidate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productPriceDelete"></a>
# **productPriceDelete**
> AttributeDelete200Response productPriceDelete(productId, groupPrices)



Delete some prices of the product

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Defines the product where the price has to be deleted
    String groupPrices = "groupPrices_example"; // String | Defines product's group prices
    try {
      AttributeDelete200Response result = apiInstance.productPriceDelete(productId, groupPrices);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productPriceDelete");
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
| **productId** | **String**| Defines the product where the price has to be deleted | |
| **groupPrices** | **String**| Defines product&#39;s group prices | [optional] |

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productPriceUpdate"></a>
# **productPriceUpdate**
> AccountConfigUpdate200Response productPriceUpdate(productPriceUpdate)



Update some prices of the product.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductPriceUpdate productPriceUpdate = new ProductPriceUpdate(); // ProductPriceUpdate | 
    try {
      AccountConfigUpdate200Response result = apiInstance.productPriceUpdate(productPriceUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productPriceUpdate");
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
| **productPriceUpdate** | [**ProductPriceUpdate**](ProductPriceUpdate.md)|  | |

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productReviewList"></a>
# **productReviewList**
> ProductReviewList200Response productReviewList(productId, start, pageCursor, count, ids, storeId, status, params, exclude, responseFields)



Get reviews of a specific product.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Product id
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String ids = "ids_example"; // String | Retrieves reviews specified by ids
    String storeId = "storeId_example"; // String | Store Id
    String status = "status_example"; // String | Defines status
    String params = "id,customer_id,email,message,status,product_id,nick_name,summary,rating,ratings,status,created_time"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    try {
      ProductReviewList200Response result = apiInstance.productReviewList(productId, start, pageCursor, count, ids, storeId, status, params, exclude, responseFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productReviewList");
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
| **productId** | **String**| Product id | |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **ids** | **String**| Retrieves reviews specified by ids | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **status** | **String**| Defines status | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,customer_id,email,message,status,product_id,nick_name,summary,rating,ratings,status,created_time] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |

### Return type

[**ProductReviewList200Response**](ProductReviewList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productStoreAssign"></a>
# **productStoreAssign**
> AccountConfigUpdate200Response productStoreAssign(productId, storeId)



Assign product to store

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Defines id of the product which should be assigned to a store
    String storeId = "storeId_example"; // String | Defines id of the store product should be assigned to
    try {
      AccountConfigUpdate200Response result = apiInstance.productStoreAssign(productId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productStoreAssign");
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
| **productId** | **String**| Defines id of the product which should be assigned to a store | |
| **storeId** | **String**| Defines id of the store product should be assigned to | |

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productTaxAdd"></a>
# **productTaxAdd**
> ProductTaxAdd200Response productTaxAdd(productTaxAdd)



Add tax class and tax rate to store and assign to product.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductTaxAdd productTaxAdd = new ProductTaxAdd(); // ProductTaxAdd | 
    try {
      ProductTaxAdd200Response result = apiInstance.productTaxAdd(productTaxAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productTaxAdd");
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
| **productTaxAdd** | [**ProductTaxAdd**](ProductTaxAdd.md)|  | |

### Return type

[**ProductTaxAdd200Response**](ProductTaxAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productUpdate"></a>
# **productUpdate**
> AccountConfigUpdate200Response productUpdate(productUpdate)



Update price and quantity for a specific product

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductUpdate productUpdate = new ProductUpdate(); // ProductUpdate | 
    try {
      AccountConfigUpdate200Response result = apiInstance.productUpdate(productUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productUpdate");
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
| **productUpdate** | [**ProductUpdate**](ProductUpdate.md)|  | |

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantAdd"></a>
# **productVariantAdd**
> ProductVariantAdd200Response productVariantAdd(productVariantAdd)



Add variant to product.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductVariantAdd productVariantAdd = new ProductVariantAdd(); // ProductVariantAdd | 
    try {
      ProductVariantAdd200Response result = apiInstance.productVariantAdd(productVariantAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantAdd");
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
| **productVariantAdd** | [**ProductVariantAdd**](ProductVariantAdd.md)|  | |

### Return type

[**ProductVariantAdd200Response**](ProductVariantAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantCount"></a>
# **productVariantCount**
> ProductVariantCount200Response productVariantCount(productId, createdFrom, createdTo, modifiedFrom, modifiedTo, categoryId, storeId)



Get count variants.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Retrieves products' variants specified by product id
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String categoryId = "categoryId_example"; // String | Counts products’ variants specified by category id
    String storeId = "storeId_example"; // String | Retrieves variants specified by store id
    try {
      ProductVariantCount200Response result = apiInstance.productVariantCount(productId, createdFrom, createdTo, modifiedFrom, modifiedTo, categoryId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantCount");
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
| **productId** | **String**| Retrieves products&#39; variants specified by product id | |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **categoryId** | **String**| Counts products’ variants specified by category id | [optional] |
| **storeId** | **String**| Retrieves variants specified by store id | [optional] |

### Return type

[**ProductVariantCount200Response**](ProductVariantCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantDelete"></a>
# **productVariantDelete**
> AttributeDelete200Response productVariantDelete(id, productId)



Delete variant.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String id = "id_example"; // String | Defines variant removal, specified by variant id
    String productId = "productId_example"; // String | Defines product's id where the variant has to be deleted
    try {
      AttributeDelete200Response result = apiInstance.productVariantDelete(id, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantDelete");
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
| **id** | **String**| Defines variant removal, specified by variant id | |
| **productId** | **String**| Defines product&#39;s id where the variant has to be deleted | |

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantImageAdd"></a>
# **productVariantImageAdd**
> ProductImageAdd200Response productVariantImageAdd(productVariantImageAdd)



Add image to product

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductVariantImageAdd productVariantImageAdd = new ProductVariantImageAdd(); // ProductVariantImageAdd | 
    try {
      ProductImageAdd200Response result = apiInstance.productVariantImageAdd(productVariantImageAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantImageAdd");
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
| **productVariantImageAdd** | [**ProductVariantImageAdd**](ProductVariantImageAdd.md)|  | |

### Return type

[**ProductImageAdd200Response**](ProductImageAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantImageDelete"></a>
# **productVariantImageDelete**
> AttributeDelete200Response productVariantImageDelete(productId, productVariantId, id, storeId)



Delete  image to product

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String productId = "productId_example"; // String | Defines product id where the variant image should be deleted
    Integer productVariantId = 56; // Integer | Defines product's variants specified by variant id
    String id = "id_example"; // String | Entity id
    String storeId = "storeId_example"; // String | Store Id
    try {
      AttributeDelete200Response result = apiInstance.productVariantImageDelete(productId, productVariantId, id, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantImageDelete");
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
| **productId** | **String**| Defines product id where the variant image should be deleted | |
| **productVariantId** | **Integer**| Defines product&#39;s variants specified by variant id | |
| **id** | **String**| Entity id | |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantInfo"></a>
# **productVariantInfo**
> ProductInfo200Response productVariantInfo(id, params, exclude, storeId)



Get variant info. This method is deprecated, and its development is stopped. Please use \&quot;product.child_item.info\&quot; instead.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String id = "id_example"; // String | Retrieves variant's info specified by variant id
    String params = "id,name,description,price"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String storeId = "storeId_example"; // String | Retrieves variant info specified by store id
    try {
      ProductInfo200Response result = apiInstance.productVariantInfo(id, params, exclude, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantInfo");
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
| **id** | **String**| Retrieves variant&#39;s info specified by variant id | |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description,price] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **storeId** | **String**| Retrieves variant info specified by store id | [optional] |

### Return type

[**ProductInfo200Response**](ProductInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantList"></a>
# **productVariantList**
> ProductVariantList200Response productVariantList(start, count, params, exclude, createdFrom, createdTo, modifiedFrom, modifiedTo, categoryId, productId, storeId)



Get a list of variants. This method is deprecated, and its development is stopped. Please use \&quot;product.child_item.list\&quot; instead.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String params = "id,name,description,price"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String categoryId = "categoryId_example"; // String | Retrieves products’ variants specified by category id
    String productId = "productId_example"; // String | Retrieves products' variants specified by product id
    String storeId = "storeId_example"; // String | Retrieves variants specified by store id
    try {
      ProductVariantList200Response result = apiInstance.productVariantList(start, count, params, exclude, createdFrom, createdTo, modifiedFrom, modifiedTo, categoryId, productId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantList");
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
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description,price] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **categoryId** | **String**| Retrieves products’ variants specified by category id | [optional] |
| **productId** | **String**| Retrieves products&#39; variants specified by product id | [optional] |
| **storeId** | **String**| Retrieves variants specified by store id | [optional] |

### Return type

[**ProductVariantList200Response**](ProductVariantList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantPriceAdd"></a>
# **productVariantPriceAdd**
> CartValidate200Response productVariantPriceAdd(productVariantPriceAdd)



Add some prices to the product variant.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductVariantPriceAdd productVariantPriceAdd = new ProductVariantPriceAdd(); // ProductVariantPriceAdd | 
    try {
      CartValidate200Response result = apiInstance.productVariantPriceAdd(productVariantPriceAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantPriceAdd");
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
| **productVariantPriceAdd** | [**ProductVariantPriceAdd**](ProductVariantPriceAdd.md)|  | |

### Return type

[**CartValidate200Response**](CartValidate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantPriceDelete"></a>
# **productVariantPriceDelete**
> AttributeDelete200Response productVariantPriceDelete(id, productId, groupPrices)



Delete some prices of the product variant.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String id = "id_example"; // String | Defines the variant where the price has to be deleted
    String productId = "productId_example"; // String | Product id
    String groupPrices = "groupPrices_example"; // String | Defines variants's group prices
    try {
      AttributeDelete200Response result = apiInstance.productVariantPriceDelete(id, productId, groupPrices);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantPriceDelete");
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
| **id** | **String**| Defines the variant where the price has to be deleted | |
| **productId** | **String**| Product id | |
| **groupPrices** | **String**| Defines variants&#39;s group prices | |

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantPriceUpdate"></a>
# **productVariantPriceUpdate**
> AccountConfigUpdate200Response productVariantPriceUpdate(productVariantPriceUpdate)



Update some prices of the product variant.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductVariantPriceUpdate productVariantPriceUpdate = new ProductVariantPriceUpdate(); // ProductVariantPriceUpdate | 
    try {
      AccountConfigUpdate200Response result = apiInstance.productVariantPriceUpdate(productVariantPriceUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantPriceUpdate");
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
| **productVariantPriceUpdate** | [**ProductVariantPriceUpdate**](ProductVariantPriceUpdate.md)|  | |

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="productVariantUpdate"></a>
# **productVariantUpdate**
> AccountConfigUpdate200Response productVariantUpdate(productVariantUpdate)



Update variant.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    ProductApi apiInstance = new ProductApi(defaultClient);
    ProductVariantUpdate productVariantUpdate = new ProductVariantUpdate(); // ProductVariantUpdate | 
    try {
      AccountConfigUpdate200Response result = apiInstance.productVariantUpdate(productVariantUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#productVariantUpdate");
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
| **productVariantUpdate** | [**ProductVariantUpdate**](ProductVariantUpdate.md)|  | |

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


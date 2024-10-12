# CartApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bridgeDownload**](CartApi.md#bridgeDownload) | **GET** /bridge.download.file |  |
| [**cartBridge**](CartApi.md#cartBridge) | **GET** /cart.bridge.json |  |
| [**cartCatalogPriceRulesCount**](CartApi.md#cartCatalogPriceRulesCount) | **GET** /cart.catalog_price_rules.count.json |  |
| [**cartCatalogPriceRulesList**](CartApi.md#cartCatalogPriceRulesList) | **GET** /cart.catalog_price_rules.list.json |  |
| [**cartClearCache**](CartApi.md#cartClearCache) | **POST** /cart.clear_cache.json |  |
| [**cartConfig**](CartApi.md#cartConfig) | **GET** /cart.config.json |  |
| [**cartConfigUpdate**](CartApi.md#cartConfigUpdate) | **PUT** /cart.config.update.json |  |
| [**cartCouponAdd**](CartApi.md#cartCouponAdd) | **POST** /cart.coupon.add.json |  |
| [**cartCouponConditionAdd**](CartApi.md#cartCouponConditionAdd) | **POST** /cart.coupon.condition.add.json |  |
| [**cartCouponCount**](CartApi.md#cartCouponCount) | **GET** /cart.coupon.count.json |  |
| [**cartCouponDelete**](CartApi.md#cartCouponDelete) | **DELETE** /cart.coupon.delete.json |  |
| [**cartCouponList**](CartApi.md#cartCouponList) | **GET** /cart.coupon.list.json |  |
| [**cartCreate**](CartApi.md#cartCreate) | **POST** /cart.create.json |  |
| [**cartDelete**](CartApi.md#cartDelete) | **DELETE** /cart.delete.json |  |
| [**cartDisconnect**](CartApi.md#cartDisconnect) | **GET** /cart.disconnect.json |  |
| [**cartGiftcardAdd**](CartApi.md#cartGiftcardAdd) | **POST** /cart.giftcard.add.json |  |
| [**cartGiftcardCount**](CartApi.md#cartGiftcardCount) | **GET** /cart.giftcard.count.json |  |
| [**cartGiftcardList**](CartApi.md#cartGiftcardList) | **GET** /cart.giftcard.list.json |  |
| [**cartInfo**](CartApi.md#cartInfo) | **GET** /cart.info.json |  |
| [**cartList**](CartApi.md#cartList) | **GET** /cart.list.json |  |
| [**cartMetaDataList**](CartApi.md#cartMetaDataList) | **GET** /cart.meta_data.list.json |  |
| [**cartMetaDataSet**](CartApi.md#cartMetaDataSet) | **POST** /cart.meta_data.set.json |  |
| [**cartMetaDataUnset**](CartApi.md#cartMetaDataUnset) | **DELETE** /cart.meta_data.unset.json |  |
| [**cartMethods**](CartApi.md#cartMethods) | **GET** /cart.methods.json |  |
| [**cartPluginList**](CartApi.md#cartPluginList) | **GET** /cart.plugin.list.json |  |
| [**cartScriptAdd**](CartApi.md#cartScriptAdd) | **POST** /cart.script.add.json |  |
| [**cartScriptDelete**](CartApi.md#cartScriptDelete) | **DELETE** /cart.script.delete.json |  |
| [**cartScriptList**](CartApi.md#cartScriptList) | **GET** /cart.script.list.json |  |
| [**cartShippingZonesList**](CartApi.md#cartShippingZonesList) | **GET** /cart.shipping_zones.list.json |  |
| [**cartValidate**](CartApi.md#cartValidate) | **GET** /cart.validate.json |  |


<a id="bridgeDownload"></a>
# **bridgeDownload**
> File bridgeDownload(whitelabel)



Download bridge for store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    Boolean whitelabel = false; // Boolean | Identifies if there is a necessity to download whitelabel bridge.
    try {
      File result = apiInstance.bridgeDownload(whitelabel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#bridgeDownload");
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
| **whitelabel** | **Boolean**| Identifies if there is a necessity to download whitelabel bridge. | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartBridge"></a>
# **cartBridge**
> CartBridge200Response cartBridge()



Get bridge key and store key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CartApi apiInstance = new CartApi(defaultClient);
    try {
      CartBridge200Response result = apiInstance.cartBridge();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartBridge");
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

[**CartBridge200Response**](CartBridge200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartCatalogPriceRulesCount"></a>
# **cartCatalogPriceRulesCount**
> CartCatalogPriceRulesCount200Response cartCatalogPriceRulesCount()



Get count of cart catalog price rules discounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    try {
      CartCatalogPriceRulesCount200Response result = apiInstance.cartCatalogPriceRulesCount();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartCatalogPriceRulesCount");
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

[**CartCatalogPriceRulesCount200Response**](CartCatalogPriceRulesCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartCatalogPriceRulesList"></a>
# **cartCatalogPriceRulesList**
> ModelResponseCartCatalogPriceRulesList cartCatalogPriceRulesList(pageCursor, start, count, ids, params, responseFields, exclude)



Get cart catalog price rules discounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String ids = "ids_example"; // String | Retrieves  catalog_price_rules by ids
    String params = "id,name,description"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    try {
      ModelResponseCartCatalogPriceRulesList result = apiInstance.cartCatalogPriceRulesList(pageCursor, start, count, ids, params, responseFields, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartCatalogPriceRulesList");
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
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **ids** | **String**| Retrieves  catalog_price_rules by ids | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |

### Return type

[**ModelResponseCartCatalogPriceRulesList**](ModelResponseCartCatalogPriceRulesList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartClearCache"></a>
# **cartClearCache**
> CartClearCache200Response cartClearCache(cacheType)



Clear cache on store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String cacheType = "cacheType_example"; // String | Defines which cache should be cleared.
    try {
      CartClearCache200Response result = apiInstance.cartClearCache(cacheType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartClearCache");
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
| **cacheType** | **String**| Defines which cache should be cleared. | |

### Return type

[**CartClearCache200Response**](CartClearCache200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartConfig"></a>
# **cartConfig**
> CartConfig200Response cartConfig(params, exclude)



Get list of cart configs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String params = "store_name,store_url,db_prefix"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    try {
      CartConfig200Response result = apiInstance.cartConfig(params, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartConfig");
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
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to store_name,store_url,db_prefix] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |

### Return type

[**CartConfig200Response**](CartConfig200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartConfigUpdate"></a>
# **cartConfigUpdate**
> CartConfigUpdate200Response cartConfigUpdate(cartConfigUpdate)



Use this API method to update custom data in client database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    CartConfigUpdate cartConfigUpdate = new CartConfigUpdate(); // CartConfigUpdate | 
    try {
      CartConfigUpdate200Response result = apiInstance.cartConfigUpdate(cartConfigUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartConfigUpdate");
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
| **cartConfigUpdate** | [**CartConfigUpdate**](CartConfigUpdate.md)|  | |

### Return type

[**CartConfigUpdate200Response**](CartConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartCouponAdd"></a>
# **cartCouponAdd**
> CartCouponAdd200Response cartCouponAdd(cartCouponAdd)



Create new coupon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    CartCouponAdd cartCouponAdd = new CartCouponAdd(); // CartCouponAdd | 
    try {
      CartCouponAdd200Response result = apiInstance.cartCouponAdd(cartCouponAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartCouponAdd");
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
| **cartCouponAdd** | [**CartCouponAdd**](CartCouponAdd.md)|  | |

### Return type

[**CartCouponAdd200Response**](CartCouponAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartCouponConditionAdd"></a>
# **cartCouponConditionAdd**
> BasketLiveShippingServiceDelete200Response cartCouponConditionAdd(couponId, entity, key, operator, value, storeId, target)



Create new coupon condition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String couponId = "couponId_example"; // String | Coupon Id
    String entity = "order"; // String | Defines condition entity type
    String key = "total"; // String | Defines condition entity attribute key
    String operator = "=="; // String | Defines condition operator
    String value = "value_example"; // String | Defines condition value, can be comma separated according to the operator.
    String storeId = "storeId_example"; // String | Store Id
    String target = "coupon_prerequisite"; // String | Defines condition operator
    try {
      BasketLiveShippingServiceDelete200Response result = apiInstance.cartCouponConditionAdd(couponId, entity, key, operator, value, storeId, target);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartCouponConditionAdd");
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
| **couponId** | **String**| Coupon Id | |
| **entity** | **String**| Defines condition entity type | [enum: order, order_shipping_address, product, customer] |
| **key** | **String**| Defines condition entity attribute key | [enum: total, subtotal, shipping_total, total_quantity, total_weight, country, product_id, variant_id, category_id, customer_id, item_price, item_total_price, item_quantity] |
| **operator** | **String**| Defines condition operator | [enum: ==, <, <=, >, >=, ONE_OF] |
| **value** | **String**| Defines condition value, can be comma separated according to the operator. | |
| **storeId** | **String**| Store Id | [optional] |
| **target** | **String**| Defines condition operator | [optional] [default to coupon_prerequisite] |

### Return type

[**BasketLiveShippingServiceDelete200Response**](BasketLiveShippingServiceDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartCouponCount"></a>
# **cartCouponCount**
> CartCouponCount200Response cartCouponCount(storeId, dateStartFrom, dateStartTo, dateEndFrom, dateEndTo, avail)



Get cart coupons count.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String storeId = "storeId_example"; // String | Store Id
    String dateStartFrom = "dateStartFrom_example"; // String | Filter entity by date_start (greater or equal)
    String dateStartTo = "dateStartTo_example"; // String | Filter entity by date_start (less or equal)
    String dateEndFrom = "dateEndFrom_example"; // String | Filter entity by date_end (greater or equal)
    String dateEndTo = "dateEndTo_example"; // String | Filter entity by date_end (less or equal)
    Boolean avail = true; // Boolean | Defines category's visibility status
    try {
      CartCouponCount200Response result = apiInstance.cartCouponCount(storeId, dateStartFrom, dateStartTo, dateEndFrom, dateEndTo, avail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartCouponCount");
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
| **storeId** | **String**| Store Id | [optional] |
| **dateStartFrom** | **String**| Filter entity by date_start (greater or equal) | [optional] |
| **dateStartTo** | **String**| Filter entity by date_start (less or equal) | [optional] |
| **dateEndFrom** | **String**| Filter entity by date_end (greater or equal) | [optional] |
| **dateEndTo** | **String**| Filter entity by date_end (less or equal) | [optional] |
| **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true] |

### Return type

[**CartCouponCount200Response**](CartCouponCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartCouponDelete"></a>
# **cartCouponDelete**
> AttributeDelete200Response cartCouponDelete(id, storeId)



Delete coupon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String id = "id_example"; // String | Entity id
    String storeId = "storeId_example"; // String | Store Id
    try {
      AttributeDelete200Response result = apiInstance.cartCouponDelete(id, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartCouponDelete");
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

<a id="cartCouponList"></a>
# **cartCouponList**
> ModelResponseCartCouponList cartCouponList(pageCursor, start, count, couponsIds, storeId, dateStartFrom, dateStartTo, dateEndFrom, dateEndTo, avail, langId, params, responseFields, exclude)



Get cart coupon discounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String couponsIds = "couponsIds_example"; // String | Filter coupons by ids
    String storeId = "storeId_example"; // String | Filter coupons by store id
    String dateStartFrom = "dateStartFrom_example"; // String | Filter entity by date_start (greater or equal)
    String dateStartTo = "dateStartTo_example"; // String | Filter entity by date_start (less or equal)
    String dateEndFrom = "dateEndFrom_example"; // String | Filter entity by date_end (greater or equal)
    String dateEndTo = "dateEndTo_example"; // String | Filter entity by date_end (less or equal)
    Boolean avail = true; // Boolean | Filter coupons by avail status
    String langId = "langId_example"; // String | Language id
    String params = "id,code,name,description"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    try {
      ModelResponseCartCouponList result = apiInstance.cartCouponList(pageCursor, start, count, couponsIds, storeId, dateStartFrom, dateStartTo, dateEndFrom, dateEndTo, avail, langId, params, responseFields, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartCouponList");
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
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **couponsIds** | **String**| Filter coupons by ids | [optional] |
| **storeId** | **String**| Filter coupons by store id | [optional] |
| **dateStartFrom** | **String**| Filter entity by date_start (greater or equal) | [optional] |
| **dateStartTo** | **String**| Filter entity by date_start (less or equal) | [optional] |
| **dateEndFrom** | **String**| Filter entity by date_end (greater or equal) | [optional] |
| **dateEndTo** | **String**| Filter entity by date_end (less or equal) | [optional] |
| **avail** | **Boolean**| Filter coupons by avail status | [optional] |
| **langId** | **String**| Language id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,code,name,description] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |

### Return type

[**ModelResponseCartCouponList**](ModelResponseCartCouponList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartCreate"></a>
# **cartCreate**
> AccountCartAdd200Response cartCreate(cartId, storeUrl, etsyClientId, etsyRefreshToken, storeId, bridgeUrl, storeRoot, storeKey, sharedSecret, validateVersion, verify, dbTablesPrefix, ftpHost, ftpUser, ftpPassword, ftpPort, ftpStoreDir, apiKey3dcart, adminAccount, apiPath, apiKey, clientId, accessToken, context, accessToken2, apiKeyShopify, apiPassword, accessTokenShopify, apiKey2, apiUsername, encryptedPassword, login, apiUserAdnsf, apiPass, privateKey, appToken, etsyKeystring, etsySharedSecret, tokenSecret, ebayClientId, ebayClientSecret, ebayRuname, ebayAccessToken, ebayRefreshToken, ebayEnvironment, ebaySiteId, dwClientId, dwApiPass, demandwareUserName, demandwareUserPassword, sellerId, amazonSecretKey, amazonAccessKeyId, marketplacesIds, environment, hybrisClientId, hybrisClientSecret, hybrisUsername, hybrisPassword, hybrisWebsites, walmartClientId, walmartClientSecret, walmartEnvironment, walmartChannelType, lightspeedApiKey, lightspeedApiSecret, shopwareAccessKey, shopwareApiKey, shopwareApiSecret, commercehqApiKey, commercehqApiPassword, _3dcartPrivateKey, _3dcartAccessToken, wcConsumerKey, wcConsumerSecret, magentoConsumerKey, magentoConsumerSecret, magentoAccessToken, magentoTokenSecret, prestashopWebserviceKey, wixAppId, wixAppSecretKey, wixRefreshToken, mercadoLibreAppId, mercadoLibreAppSecretKey, mercadoLibreRefreshToken, zidClientId, zidClientSecret, zidAccessToken, zidAuthorization, zidRefreshToken)



Add store to the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CartApi apiInstance = new CartApi(defaultClient);
    String cartId = "3DCart"; // String | Store’s identifier which you can get from cart_list method
    String storeUrl = "storeUrl_example"; // String | A web address of a store that you would like to connect to API2Cart
    String etsyClientId = "etsyClientId_example"; // String | Etsy Client Id
    String etsyRefreshToken = "etsyRefreshToken_example"; // String | Etsy Refresh token
    String storeId = "storeId_example"; // String | Store Id
    String bridgeUrl = "bridgeUrl_example"; // String | This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store)
    String storeRoot = "storeRoot_example"; // String | Absolute path to the store root directory (used with \"bridge_url\" parameter)
    String storeKey = "storeKey_example"; // String | Set this parameter if bridge is already uploaded to store
    String sharedSecret = "sharedSecret_example"; // String | Shared secret
    Boolean validateVersion = false; // Boolean | Specify if api2cart should validate cart version
    Boolean verify = true; // Boolean | Enables or disables cart's verification
    String dbTablesPrefix = "dbTablesPrefix_example"; // String | DB tables prefix
    String ftpHost = "ftpHost_example"; // String | FTP connection host
    String ftpUser = "ftpUser_example"; // String | FTP User
    String ftpPassword = "ftpPassword_example"; // String | FTP Password
    Integer ftpPort = 56; // Integer | FTP Port
    String ftpStoreDir = "ftpStoreDir_example"; // String | FTP Store dir
    String apiKey3dcart = "apiKey3dcart_example"; // String | 3DCart API Key
    String adminAccount = "adminAccount_example"; // String | It's a BigCommerce account for which API is enabled
    String apiPath = "apiPath_example"; // String | BigCommerce API URL
    String apiKey = "apiKey_example"; // String | Bigcommerce API Key
    String clientId = "clientId_example"; // String | Client ID of the requesting app
    String accessToken = "accessToken_example"; // String | Access token authorizing the app to access resources on behalf of a user
    String context = "context_example"; // String | API Path section unique to the store
    String accessToken2 = "accessToken_example"; // String | Access token authorizing the app to access resources on behalf of a user
    String apiKeyShopify = "apiKeyShopify_example"; // String | Shopify API Key
    String apiPassword = "apiPassword_example"; // String | Shopify API Password
    String accessTokenShopify = "accessTokenShopify_example"; // String | Access token authorizing the app to access resources on behalf of a user
    String apiKey2 = "apiKey_example"; // String | Neto API Key
    String apiUsername = "apiUsername_example"; // String | Neto User Name
    String encryptedPassword = "encryptedPassword_example"; // String | Volusion API Password
    String login = "login_example"; // String | It's a Volusion account for which API is enabled
    String apiUserAdnsf = "apiUserAdnsf_example"; // String | It's a AspDotNetStorefront account for which API is available
    String apiPass = "apiPass_example"; // String | AspDotNetStorefront API Password
    String privateKey = "privateKey_example"; // String | 3DCart Application Private Key
    String appToken = "appToken_example"; // String | 3DCart Token from Application
    String etsyKeystring = "etsyKeystring_example"; // String | Etsy keystring
    String etsySharedSecret = "etsySharedSecret_example"; // String | Etsy shared secret
    String tokenSecret = "tokenSecret_example"; // String | Secret token authorizing the app to access resources on behalf of a user
    String ebayClientId = "ebayClientId_example"; // String | Application ID (AppID).
    String ebayClientSecret = "ebayClientSecret_example"; // String | Shared Secret from eBay application
    String ebayRuname = "ebayRuname_example"; // String | The RuName value that eBay assigns to your application.
    String ebayAccessToken = "ebayAccessToken_example"; // String | Used to authenticate API requests.
    String ebayRefreshToken = "ebayRefreshToken_example"; // String | Used to renew the access token.
    String ebayEnvironment = "production"; // String | eBay environment
    Integer ebaySiteId = 0; // Integer | eBay global ID
    String dwClientId = "dwClientId_example"; // String | Demandware client id
    String dwApiPass = "dwApiPass_example"; // String | Demandware api password
    String demandwareUserName = "demandwareUserName_example"; // String | Demandware user name
    String demandwareUserPassword = "demandwareUserPassword_example"; // String | Demandware user password
    String sellerId = "sellerId_example"; // String | Seller Id
    String amazonSecretKey = "amazonSecretKey_example"; // String | Amazon Secret Key
    String amazonAccessKeyId = "amazonAccessKeyId_example"; // String | Amazon Secret Key Id
    String marketplacesIds = "marketplacesIds_example"; // String | Comma separated marketplaces ids
    String environment = "production"; // String | 
    String hybrisClientId = "hybrisClientId_example"; // String | Omni Commerce Connector Client ID
    String hybrisClientSecret = "hybrisClientSecret_example"; // String | Omni Commerce Connector Client Secret
    String hybrisUsername = "hybrisUsername_example"; // String | User Name
    String hybrisPassword = "hybrisPassword_example"; // String | User password
    List<String> hybrisWebsites = Arrays.asList(); // List<String> | Websites to stores mapping data
    String walmartClientId = "walmartClientId_example"; // String | Walmart client ID
    String walmartClientSecret = "walmartClientSecret_example"; // String | Walmart client secret
    String walmartEnvironment = "production"; // String | Walmart environment
    String walmartChannelType = "walmartChannelType_example"; // String | Walmart WM_CONSUMER.CHANNEL.TYPE header
    String lightspeedApiKey = "lightspeedApiKey_example"; // String | LightSpeed api key
    String lightspeedApiSecret = "lightspeedApiSecret_example"; // String | LightSpeed api secret
    String shopwareAccessKey = "shopwareAccessKey_example"; // String | Shopware access key
    String shopwareApiKey = "shopwareApiKey_example"; // String | Shopware api key
    String shopwareApiSecret = "shopwareApiSecret_example"; // String | Shopware client secret access key
    String commercehqApiKey = "commercehqApiKey_example"; // String | CommerceHQ api key
    String commercehqApiPassword = "commercehqApiPassword_example"; // String | CommerceHQ api password
    String _3dcartPrivateKey = "_3dcartPrivateKey_example"; // String | 3DCart Private Key
    String _3dcartAccessToken = "_3dcartAccessToken_example"; // String | 3DCart Token
    String wcConsumerKey = "wcConsumerKey_example"; // String | Woocommerce consumer key
    String wcConsumerSecret = "wcConsumerSecret_example"; // String | Woocommerce consumer secret
    String magentoConsumerKey = "magentoConsumerKey_example"; // String | Magento Consumer Key
    String magentoConsumerSecret = "magentoConsumerSecret_example"; // String | Magento Consumer Secret
    String magentoAccessToken = "magentoAccessToken_example"; // String | Magento Access Token
    String magentoTokenSecret = "magentoTokenSecret_example"; // String | Magento Token Secret
    String prestashopWebserviceKey = "prestashopWebserviceKey_example"; // String | Prestashop webservice key
    String wixAppId = "wixAppId_example"; // String | Wix App ID
    String wixAppSecretKey = "wixAppSecretKey_example"; // String | Wix App Secret Key
    String wixRefreshToken = "wixRefreshToken_example"; // String | Wix refresh token
    String mercadoLibreAppId = "mercadoLibreAppId_example"; // String | Mercado Libre App ID
    String mercadoLibreAppSecretKey = "mercadoLibreAppSecretKey_example"; // String | Mercado Libre App Secret Key
    String mercadoLibreRefreshToken = "mercadoLibreRefreshToken_example"; // String | Mercado Libre Refresh Token
    Integer zidClientId = 56; // Integer | Zid Client ID
    String zidClientSecret = "zidClientSecret_example"; // String | Zid Client Secret
    String zidAccessToken = "zidAccessToken_example"; // String | Zid Access Token
    String zidAuthorization = "zidAuthorization_example"; // String | Zid Authorization
    String zidRefreshToken = "zidRefreshToken_example"; // String | Zid refresh token
    try {
      AccountCartAdd200Response result = apiInstance.cartCreate(cartId, storeUrl, etsyClientId, etsyRefreshToken, storeId, bridgeUrl, storeRoot, storeKey, sharedSecret, validateVersion, verify, dbTablesPrefix, ftpHost, ftpUser, ftpPassword, ftpPort, ftpStoreDir, apiKey3dcart, adminAccount, apiPath, apiKey, clientId, accessToken, context, accessToken2, apiKeyShopify, apiPassword, accessTokenShopify, apiKey2, apiUsername, encryptedPassword, login, apiUserAdnsf, apiPass, privateKey, appToken, etsyKeystring, etsySharedSecret, tokenSecret, ebayClientId, ebayClientSecret, ebayRuname, ebayAccessToken, ebayRefreshToken, ebayEnvironment, ebaySiteId, dwClientId, dwApiPass, demandwareUserName, demandwareUserPassword, sellerId, amazonSecretKey, amazonAccessKeyId, marketplacesIds, environment, hybrisClientId, hybrisClientSecret, hybrisUsername, hybrisPassword, hybrisWebsites, walmartClientId, walmartClientSecret, walmartEnvironment, walmartChannelType, lightspeedApiKey, lightspeedApiSecret, shopwareAccessKey, shopwareApiKey, shopwareApiSecret, commercehqApiKey, commercehqApiPassword, _3dcartPrivateKey, _3dcartAccessToken, wcConsumerKey, wcConsumerSecret, magentoConsumerKey, magentoConsumerSecret, magentoAccessToken, magentoTokenSecret, prestashopWebserviceKey, wixAppId, wixAppSecretKey, wixRefreshToken, mercadoLibreAppId, mercadoLibreAppSecretKey, mercadoLibreRefreshToken, zidClientId, zidClientSecret, zidAccessToken, zidAuthorization, zidRefreshToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartCreate");
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
| **cartId** | **String**| Store’s identifier which you can get from cart_list method | [enum: 3DCart, 3DCartApi, AceShop, AmazonSP, Amazon, AspDotNetStorefront, BigcommerceApi, Creloaded, CommerceHQ, Cscart, Cubecart, Demandware, EBay, Ecwid, Etsy, EtsyAPIv3, Gambio, JooCart, Magento1212, Magento2Api, MijoShop, Neto, Opencart14, LightSpeed, Oscmax2, Oscommerce22ms2, Oxid, Pinnacle, Prestashop, PrestashopApi, SSPremium, Shopify, Squarespace, Shopware, ShopwareApi, Tomatocart, Ubercart, Virtuemart, Volusion, WPecommerce, Walmart, WebAsyst, Woocommerce, WoocommerceApi, Wix, Xcart, Xtcommerce, XtcommerceVeyton, Zencart137, Hybris, MercadoLibre, Zid, Zoey] |
| **storeUrl** | **String**| A web address of a store that you would like to connect to API2Cart | |
| **etsyClientId** | **String**| Etsy Client Id | |
| **etsyRefreshToken** | **String**| Etsy Refresh token | |
| **storeId** | **String**| Store Id | |
| **bridgeUrl** | **String**| This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store) | [optional] |
| **storeRoot** | **String**| Absolute path to the store root directory (used with \&quot;bridge_url\&quot; parameter) | [optional] |
| **storeKey** | **String**| Set this parameter if bridge is already uploaded to store | [optional] |
| **sharedSecret** | **String**| Shared secret | [optional] |
| **validateVersion** | **Boolean**| Specify if api2cart should validate cart version | [optional] [default to false] |
| **verify** | **Boolean**| Enables or disables cart&#39;s verification | [optional] [default to true] |
| **dbTablesPrefix** | **String**| DB tables prefix | [optional] |
| **ftpHost** | **String**| FTP connection host | [optional] |
| **ftpUser** | **String**| FTP User | [optional] |
| **ftpPassword** | **String**| FTP Password | [optional] |
| **ftpPort** | **Integer**| FTP Port | [optional] |
| **ftpStoreDir** | **String**| FTP Store dir | [optional] |
| **apiKey3dcart** | **String**| 3DCart API Key | [optional] |
| **adminAccount** | **String**| It&#39;s a BigCommerce account for which API is enabled | [optional] |
| **apiPath** | **String**| BigCommerce API URL | [optional] |
| **apiKey** | **String**| Bigcommerce API Key | [optional] |
| **clientId** | **String**| Client ID of the requesting app | [optional] |
| **accessToken** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] |
| **context** | **String**| API Path section unique to the store | [optional] |
| **accessToken2** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] |
| **apiKeyShopify** | **String**| Shopify API Key | [optional] |
| **apiPassword** | **String**| Shopify API Password | [optional] |
| **accessTokenShopify** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] |
| **apiKey2** | **String**| Neto API Key | [optional] |
| **apiUsername** | **String**| Neto User Name | [optional] |
| **encryptedPassword** | **String**| Volusion API Password | [optional] |
| **login** | **String**| It&#39;s a Volusion account for which API is enabled | [optional] |
| **apiUserAdnsf** | **String**| It&#39;s a AspDotNetStorefront account for which API is available | [optional] |
| **apiPass** | **String**| AspDotNetStorefront API Password | [optional] |
| **privateKey** | **String**| 3DCart Application Private Key | [optional] |
| **appToken** | **String**| 3DCart Token from Application | [optional] |
| **etsyKeystring** | **String**| Etsy keystring | [optional] |
| **etsySharedSecret** | **String**| Etsy shared secret | [optional] |
| **tokenSecret** | **String**| Secret token authorizing the app to access resources on behalf of a user | [optional] |
| **ebayClientId** | **String**| Application ID (AppID). | [optional] |
| **ebayClientSecret** | **String**| Shared Secret from eBay application | [optional] |
| **ebayRuname** | **String**| The RuName value that eBay assigns to your application. | [optional] |
| **ebayAccessToken** | **String**| Used to authenticate API requests. | [optional] |
| **ebayRefreshToken** | **String**| Used to renew the access token. | [optional] |
| **ebayEnvironment** | **String**| eBay environment | [optional] [default to production] |
| **ebaySiteId** | **Integer**| eBay global ID | [optional] [default to 0] |
| **dwClientId** | **String**| Demandware client id | [optional] |
| **dwApiPass** | **String**| Demandware api password | [optional] |
| **demandwareUserName** | **String**| Demandware user name | [optional] |
| **demandwareUserPassword** | **String**| Demandware user password | [optional] |
| **sellerId** | **String**| Seller Id | [optional] |
| **amazonSecretKey** | **String**| Amazon Secret Key | [optional] |
| **amazonAccessKeyId** | **String**| Amazon Secret Key Id | [optional] |
| **marketplacesIds** | **String**| Comma separated marketplaces ids | [optional] |
| **environment** | **String**|  | [optional] [default to production] |
| **hybrisClientId** | **String**| Omni Commerce Connector Client ID | [optional] |
| **hybrisClientSecret** | **String**| Omni Commerce Connector Client Secret | [optional] |
| **hybrisUsername** | **String**| User Name | [optional] |
| **hybrisPassword** | **String**| User password | [optional] |
| **hybrisWebsites** | [**List&lt;String&gt;**](String.md)| Websites to stores mapping data | [optional] |
| **walmartClientId** | **String**| Walmart client ID | [optional] |
| **walmartClientSecret** | **String**| Walmart client secret | [optional] |
| **walmartEnvironment** | **String**| Walmart environment | [optional] [default to production] |
| **walmartChannelType** | **String**| Walmart WM_CONSUMER.CHANNEL.TYPE header | [optional] |
| **lightspeedApiKey** | **String**| LightSpeed api key | [optional] |
| **lightspeedApiSecret** | **String**| LightSpeed api secret | [optional] |
| **shopwareAccessKey** | **String**| Shopware access key | [optional] |
| **shopwareApiKey** | **String**| Shopware api key | [optional] |
| **shopwareApiSecret** | **String**| Shopware client secret access key | [optional] |
| **commercehqApiKey** | **String**| CommerceHQ api key | [optional] |
| **commercehqApiPassword** | **String**| CommerceHQ api password | [optional] |
| **_3dcartPrivateKey** | **String**| 3DCart Private Key | [optional] |
| **_3dcartAccessToken** | **String**| 3DCart Token | [optional] |
| **wcConsumerKey** | **String**| Woocommerce consumer key | [optional] |
| **wcConsumerSecret** | **String**| Woocommerce consumer secret | [optional] |
| **magentoConsumerKey** | **String**| Magento Consumer Key | [optional] |
| **magentoConsumerSecret** | **String**| Magento Consumer Secret | [optional] |
| **magentoAccessToken** | **String**| Magento Access Token | [optional] |
| **magentoTokenSecret** | **String**| Magento Token Secret | [optional] |
| **prestashopWebserviceKey** | **String**| Prestashop webservice key | [optional] |
| **wixAppId** | **String**| Wix App ID | [optional] |
| **wixAppSecretKey** | **String**| Wix App Secret Key | [optional] |
| **wixRefreshToken** | **String**| Wix refresh token | [optional] |
| **mercadoLibreAppId** | **String**| Mercado Libre App ID | [optional] |
| **mercadoLibreAppSecretKey** | **String**| Mercado Libre App Secret Key | [optional] |
| **mercadoLibreRefreshToken** | **String**| Mercado Libre Refresh Token | [optional] |
| **zidClientId** | **Integer**| Zid Client ID | [optional] |
| **zidClientSecret** | **String**| Zid Client Secret | [optional] |
| **zidAccessToken** | **String**| Zid Access Token | [optional] |
| **zidAuthorization** | **String**| Zid Authorization | [optional] |
| **zidRefreshToken** | **String**| Zid refresh token | [optional] |

### Return type

[**AccountCartAdd200Response**](AccountCartAdd200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartDelete"></a>
# **cartDelete**
> CartDelete200Response cartDelete(deleteBridge)



Remove store from API2Cart

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    Boolean deleteBridge = true; // Boolean | Identifies if there is a necessity to delete bridge
    try {
      CartDelete200Response result = apiInstance.cartDelete(deleteBridge);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartDelete");
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
| **deleteBridge** | **Boolean**| Identifies if there is a necessity to delete bridge | [optional] [default to true] |

### Return type

[**CartDelete200Response**](CartDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartDisconnect"></a>
# **cartDisconnect**
> CartDisconnect200Response cartDisconnect(deleteBridge)



Disconnect with the store and clear store session data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    Boolean deleteBridge = false; // Boolean | Identifies if there is a necessity to delete bridge
    try {
      CartDisconnect200Response result = apiInstance.cartDisconnect(deleteBridge);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartDisconnect");
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
| **deleteBridge** | **Boolean**| Identifies if there is a necessity to delete bridge | [optional] [default to false] |

### Return type

[**CartDisconnect200Response**](CartDisconnect200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartGiftcardAdd"></a>
# **cartGiftcardAdd**
> CartGiftcardAdd200Response cartGiftcardAdd(amount, code, ownerEmail, recipientEmail)



Create new gift card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    BigDecimal amount = new BigDecimal(78); // BigDecimal | Defines the gift card amount value.
    String code = "code_example"; // String | Gift card code
    String ownerEmail = "ownerEmail_example"; // String | Gift card owner email
    String recipientEmail = "recipientEmail_example"; // String | Gift card recipient email
    try {
      CartGiftcardAdd200Response result = apiInstance.cartGiftcardAdd(amount, code, ownerEmail, recipientEmail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartGiftcardAdd");
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
| **amount** | **BigDecimal**| Defines the gift card amount value. | |
| **code** | **String**| Gift card code | [optional] |
| **ownerEmail** | **String**| Gift card owner email | [optional] |
| **recipientEmail** | **String**| Gift card recipient email | [optional] |

### Return type

[**CartGiftcardAdd200Response**](CartGiftcardAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartGiftcardCount"></a>
# **cartGiftcardCount**
> CartGiftcardCount200Response cartGiftcardCount(storeId)



Get gift cards count.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String storeId = "storeId_example"; // String | Store Id
    try {
      CartGiftcardCount200Response result = apiInstance.cartGiftcardCount(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartGiftcardCount");
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
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**CartGiftcardCount200Response**](CartGiftcardCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartGiftcardList"></a>
# **cartGiftcardList**
> ModelResponseCartGiftCardList cartGiftcardList(pageCursor, start, count, storeId, params, responseFields, exclude)



Get gift cards list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String storeId = "storeId_example"; // String | Store Id
    String params = "id,code,name"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    try {
      ModelResponseCartGiftCardList result = apiInstance.cartGiftcardList(pageCursor, start, count, storeId, params, responseFields, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartGiftcardList");
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
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **storeId** | **String**| Store Id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,code,name] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |

### Return type

[**ModelResponseCartGiftCardList**](ModelResponseCartGiftCardList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartInfo"></a>
# **cartInfo**
> CartInfo200Response cartInfo(params, responseFields, exclude, storeId)



Get cart information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String params = "store_name,store_url,db_prefix"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String storeId = "storeId_example"; // String | Store Id
    try {
      CartInfo200Response result = apiInstance.cartInfo(params, responseFields, exclude, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartInfo");
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
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to store_name,store_url,db_prefix] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**CartInfo200Response**](CartInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartList"></a>
# **cartList**
> CartList200Response cartList()



Get list of supported carts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CartApi apiInstance = new CartApi(defaultClient);
    try {
      CartList200Response result = apiInstance.cartList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartList");
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

[**CartList200Response**](CartList200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartMetaDataList"></a>
# **cartMetaDataList**
> ModelResponseCartMetaDataList cartMetaDataList(entityId, entity, storeId, langId, key, count, pageCursor, params, responseFields, exclude)



Get entity meta data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String entityId = "entityId_example"; // String | Entity Id
    String entity = "product"; // String | Entity
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    String key = "key_example"; // String | Key
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    String params = "key,value"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    try {
      ModelResponseCartMetaDataList result = apiInstance.cartMetaDataList(entityId, entity, storeId, langId, key, count, pageCursor, params, responseFields, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartMetaDataList");
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
| **entityId** | **String**| Entity Id | |
| **entity** | **String**| Entity | [optional] [default to product] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **key** | **String**| Key | [optional] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to key,value] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |

### Return type

[**ModelResponseCartMetaDataList**](ModelResponseCartMetaDataList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartMetaDataSet"></a>
# **cartMetaDataSet**
> AttributeAdd200Response cartMetaDataSet(entityId, key, value, namespace, entity, storeId, langId)



Set meta data for a specific entity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String entityId = "entityId_example"; // String | Entity Id
    String key = "key_example"; // String | Key
    String value = "value_example"; // String | Value
    String namespace = "namespace_example"; // String | Metafield namespace
    String entity = "product"; // String | Entity
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    try {
      AttributeAdd200Response result = apiInstance.cartMetaDataSet(entityId, key, value, namespace, entity, storeId, langId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartMetaDataSet");
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
| **entityId** | **String**| Entity Id | |
| **key** | **String**| Key | |
| **value** | **String**| Value | |
| **namespace** | **String**| Metafield namespace | |
| **entity** | **String**| Entity | [optional] [default to product] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |

### Return type

[**AttributeAdd200Response**](AttributeAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartMetaDataUnset"></a>
# **cartMetaDataUnset**
> BasketLiveShippingServiceDelete200Response cartMetaDataUnset(entityId, key, id, entity, storeId)



Unset meta data for a specific entity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String entityId = "entityId_example"; // String | Entity Id
    String key = "key_example"; // String | Key
    String id = "id_example"; // String | Entity id
    String entity = "product"; // String | Entity
    String storeId = "storeId_example"; // String | Store Id
    try {
      BasketLiveShippingServiceDelete200Response result = apiInstance.cartMetaDataUnset(entityId, key, id, entity, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartMetaDataUnset");
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
| **entityId** | **String**| Entity Id | |
| **key** | **String**| Key | |
| **id** | **String**| Entity id | |
| **entity** | **String**| Entity | [optional] [default to product] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**BasketLiveShippingServiceDelete200Response**](BasketLiveShippingServiceDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartMethods"></a>
# **cartMethods**
> CartMethods200Response cartMethods()



Get list of cart methods

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    try {
      CartMethods200Response result = apiInstance.cartMethods();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartMethods");
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

[**CartMethods200Response**](CartMethods200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartPluginList"></a>
# **cartPluginList**
> CartPluginList200Response cartPluginList(storeKey, storeId, start, count)



Get list of installed plugins

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String storeKey = "storeKey_example"; // String | Set this parameter if bridge is already uploaded to store
    String storeId = "storeId_example"; // String | Store Id
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    try {
      CartPluginList200Response result = apiInstance.cartPluginList(storeKey, storeId, start, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartPluginList");
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
| **storeKey** | **String**| Set this parameter if bridge is already uploaded to store | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |

### Return type

[**CartPluginList200Response**](CartPluginList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartScriptAdd"></a>
# **cartScriptAdd**
> CartScriptAdd200Response cartScriptAdd(name, description, html, src, loadMethod, scope, storeId)



Add new script to the storefront

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String name = "name_example"; // String | The user-friendly script name
    String description = "description_example"; // String | The user-friendly description
    String html = "html_example"; // String | An html string containing exactly one `script` tag.
    String src = "src_example"; // String | The URL of the remote script
    String loadMethod = "loadMethod_example"; // String | The load method to use for the script
    String scope = "storefront"; // String | The page or pages on the online store where the script should be included
    String storeId = "storeId_example"; // String | Store Id
    try {
      CartScriptAdd200Response result = apiInstance.cartScriptAdd(name, description, html, src, loadMethod, scope, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartScriptAdd");
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
| **name** | **String**| The user-friendly script name | [optional] |
| **description** | **String**| The user-friendly description | [optional] |
| **html** | **String**| An html string containing exactly one &#x60;script&#x60; tag. | [optional] |
| **src** | **String**| The URL of the remote script | [optional] |
| **loadMethod** | **String**| The load method to use for the script | [optional] |
| **scope** | **String**| The page or pages on the online store where the script should be included | [optional] [default to storefront] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**CartScriptAdd200Response**](CartScriptAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartScriptDelete"></a>
# **cartScriptDelete**
> BridgeDelete200Response cartScriptDelete(id, storeId)



Remove script from the storefront

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String id = "id_example"; // String | Entity id
    String storeId = "storeId_example"; // String | Store Id
    try {
      BridgeDelete200Response result = apiInstance.cartScriptDelete(id, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartScriptDelete");
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
| **id** | **String**| Entity id | |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**BridgeDelete200Response**](BridgeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartScriptList"></a>
# **cartScriptList**
> ModelResponseCartScriptList cartScriptList(pageCursor, start, count, createdFrom, createdTo, modifiedFrom, modifiedTo, scriptIds, storeId, params, responseFields, exclude)



Get scripts installed to the storefront

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String scriptIds = "scriptIds_example"; // String | Retrieves only scripts with specific ids
    String storeId = "storeId_example"; // String | Store Id
    String params = "id,name,description"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    try {
      ModelResponseCartScriptList result = apiInstance.cartScriptList(pageCursor, start, count, createdFrom, createdTo, modifiedFrom, modifiedTo, scriptIds, storeId, params, responseFields, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartScriptList");
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
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **scriptIds** | **String**| Retrieves only scripts with specific ids | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,description] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |

### Return type

[**ModelResponseCartScriptList**](ModelResponseCartScriptList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartShippingZonesList"></a>
# **cartShippingZonesList**
> CartShippingZonesList200Response cartShippingZonesList(storeId, start, count, params, responseFields, exclude)



Get list of shipping zones

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    String storeId = "storeId_example"; // String | Store Id
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String params = "id,name,enabled"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    try {
      CartShippingZonesList200Response result = apiInstance.cartShippingZonesList(storeId, start, count, params, responseFields, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartShippingZonesList");
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
| **storeId** | **String**| Store Id | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,enabled] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |

### Return type

[**CartShippingZonesList200Response**](CartShippingZonesList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cartValidate"></a>
# **cartValidate**
> CartValidate200Response cartValidate(validateVersion)



Check store availability, bridge connection for the downloadable carts, identify DB prefix, validate API accesses for API carts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartApi;

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

    CartApi apiInstance = new CartApi(defaultClient);
    Boolean validateVersion = false; // Boolean | Specify if api2cart should validate cart version
    try {
      CartValidate200Response result = apiInstance.cartValidate(validateVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartApi#cartValidate");
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
| **validateVersion** | **Boolean**| Specify if api2cart should validate cart version | [optional] [default to false] |

### Return type

[**CartValidate200Response**](CartValidate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


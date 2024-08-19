# V1ProductApi

All URIs are relative to *https://api.kompany.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productAvailability**](V1ProductApi.md#productAvailability) | **GET** /api/v1/product/availability/{sku}/{subjectId} | Retrieves a document availability result |
| [**productCatalog**](V1ProductApi.md#productCatalog) | **GET** /api/v1/product/catalog/{country} | Returns a catalog of products |
| [**productNotifier**](V1ProductApi.md#productNotifier) | **GET** /api/v1/product/notifier/{notifierId} | Returns metadata for a notifier |
| [**productNotifierCreate**](V1ProductApi.md#productNotifierCreate) | **POST** /api/v1/product/notifier/{orderId}/{type}/{uri} | Creates a notifier for an order |
| [**productOrder**](V1ProductApi.md#productOrder) | **POST** /api/v1/product/order/{sku}/{subjectId} | Places a product order |
| [**productOrderConcierge**](V1ProductApi.md#productOrderConcierge) | **POST** /api/v1/product/order/concierge | Places a concierge order |
| [**productOrderUbo**](V1ProductApi.md#productOrderUbo) | **POST** /api/v1/product/order/ubo | Places a UBO order |
| [**productOrderWithOption**](V1ProductApi.md#productOrderWithOption) | **POST** /api/v1/product/order/{sku}/{option}/{subjectId} | Places a product order |
| [**productRetrieve**](V1ProductApi.md#productRetrieve) | **GET** /api/v1/product/{orderId} | Retrieves the result of an order |
| [**productSearch**](V1ProductApi.md#productSearch) | **GET** /api/v1/product/search/{subjectId} | Returns a list of products |
| [**productStatus**](V1ProductApi.md#productStatus) | **GET** /api/v1/product/status/{orderId} | Returns metadata for a order |
| [**productUpdateAction**](V1ProductApi.md#productUpdateAction) | **POST** /api/v1/product/update/{action}/{orderId} | Updates metadata of an order |


<a id="productAvailability"></a>
# **productAvailability**
> ProductAvailability200Response productAvailability(sku, subjectId)

Retrieves a document availability result

Check availability and valid options for a particular product for a particular company identfied by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String sku = "sku_example"; // String | SKU - 9 character value from a Product object
    String subjectId = "subjectId_example"; // String | Subject (e.g. Company) ID - 32 character hex value
    try {
      ProductAvailability200Response result = apiInstance.productAvailability(sku, subjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productAvailability");
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
| **sku** | **String**| SKU - 9 character value from a Product object | |
| **subjectId** | **String**| Subject (e.g. Company) ID - 32 character hex value | |

### Return type

[**ProductAvailability200Response**](ProductAvailability200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product details |  -  |
| **0** |  |  -  |

<a id="productCatalog"></a>
# **productCatalog**
> ProductCatalog200Response productCatalog(country)

Returns a catalog of products

Returns a catalog of purchasable products available with some metadata for a particular country

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String country = "country_example"; // String | two letter country code in upper case
    try {
      ProductCatalog200Response result = apiInstance.productCatalog(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productCatalog");
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
| **country** | **String**| two letter country code in upper case | |

### Return type

[**ProductCatalog200Response**](ProductCatalog200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product with details like URI to purchase it |  -  |
| **0** |  |  -  |

<a id="productNotifier"></a>
# **productNotifier**
> productNotifier(notifierId)

Returns metadata for a notifier

Queries and returns all metadata associated with a notifier identified by its notifer id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String notifierId = "notifierId_example"; // String | ID of the ProductOrderNotifier as returned from a /notifier POST call - 32 character hex value
    try {
      apiInstance.productNotifier(notifierId);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productNotifier");
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
| **notifierId** | **String**| ID of the ProductOrderNotifier as returned from a /notifier POST call - 32 character hex value | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="productNotifierCreate"></a>
# **productNotifierCreate**
> ProductNotifierCreate200Response productNotifierCreate(orderId, type, uri)

Creates a notifier for an order

Create a notifier for a particular order. Parameters can be supplied in the path

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String orderId = "orderId_example"; // String | ID of the ProductOrder as returned from a /product/buy call - 32 character hex value
    String type = "type_example"; // String | Type of the notifier - indicates the action the notifier will perform. Currently GET and POST are supported which performs an http(s) GET/POST to the supplied uri with appended notifierId= and orderId= parameters when the order processing is completed. Upon the POST request the order object is sent as a JSON body
    String uri = "uri_example"; // String | URI of the notifier for the 'complete' action. Currently only a GET method HTTP(s) URL is supported. 1 to 250 characters long. Every slash in the URI must be replaced by a ~
    try {
      ProductNotifierCreate200Response result = apiInstance.productNotifierCreate(orderId, type, uri);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productNotifierCreate");
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
| **orderId** | **String**| ID of the ProductOrder as returned from a /product/buy call - 32 character hex value | |
| **type** | **String**| Type of the notifier - indicates the action the notifier will perform. Currently GET and POST are supported which performs an http(s) GET/POST to the supplied uri with appended notifierId&#x3D; and orderId&#x3D; parameters when the order processing is completed. Upon the POST request the order object is sent as a JSON body | |
| **uri** | **String**| URI of the notifier for the &#39;complete&#39; action. Currently only a GET method HTTP(s) URL is supported. 1 to 250 characters long. Every slash in the URI must be replaced by a ~ | |

### Return type

[**ProductNotifierCreate200Response**](ProductNotifierCreate200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of configured product order notification |  -  |
| **0** |  |  -  |

<a id="productOrder"></a>
# **productOrder**
> ProductOrder200Response productOrder(sku, subjectId)

Places a product order

Place an order for a particular product identified by its SKU for a particular company identified by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String sku = "sku_example"; // String | SKU - 9 character value from a Product object
    String subjectId = "subjectId_example"; // String | Subject (e.g. Company) ID - 32 character hex value
    try {
      ProductOrder200Response result = apiInstance.productOrder(sku, subjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productOrder");
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
| **sku** | **String**| SKU - 9 character value from a Product object | |
| **subjectId** | **String**| Subject (e.g. Company) ID - 32 character hex value | |

### Return type

[**ProductOrder200Response**](ProductOrder200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product order details |  -  |
| **0** |  |  -  |

<a id="productOrderConcierge"></a>
# **productOrderConcierge**
> productOrderConcierge(companyName, contactEmail, contactPhone, costConfirmation, country, financialData, historicInformation, informationRequirements, locationInvestigation, priority, registerData, registerNumber, subjectId)

Places a concierge order

Place an order for a concierge product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String companyName = "companyName_example"; // String | Name of the company for which a document should be ordered. (Not required if subjectId is given)
    String contactEmail = "contactEmail_example"; // String | Contact E-Mail, will be contacted if concierge costs are exceeding the threshhold configured on your plan
    String contactPhone = "contactPhone_example"; // String | Contact phone, will be contacted if concierge costs are exceeding the threshhold configured on your plan
    Boolean costConfirmation = true; // Boolean | If the concierge cost should require additional confirmation if a threshold is reached (configured on your plan)
    String country = "country_example"; // String | Two letter ISO code of the country of the company
    Boolean financialData = true; // Boolean | If you want financial data of the company to be retrieved
    Boolean historicInformation = true; // Boolean | If you want historical data of the company to be retrieved
    String informationRequirements = "informationRequirements_example"; // String | Requirements on what document or information should be provided. Please be very precise
    Boolean locationInvestigation = true; // Boolean | If the companies residency should be investigated
    String priority = "priority_example"; // String | Priority of order: standard/express are allowed
    Boolean registerData = true; // Boolean | If you want register data of the company to be retrieved
    String registerNumber = "registerNumber_example"; // String | Registration number of the company for which a document should be ordered. (Not required if subjectId is given)
    String subjectId = "subjectId_example"; // String | Kompanyid of the company you want to place the order for
    try {
      apiInstance.productOrderConcierge(companyName, contactEmail, contactPhone, costConfirmation, country, financialData, historicInformation, informationRequirements, locationInvestigation, priority, registerData, registerNumber, subjectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productOrderConcierge");
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
| **companyName** | **String**| Name of the company for which a document should be ordered. (Not required if subjectId is given) | [optional] |
| **contactEmail** | **String**| Contact E-Mail, will be contacted if concierge costs are exceeding the threshhold configured on your plan | [optional] |
| **contactPhone** | **String**| Contact phone, will be contacted if concierge costs are exceeding the threshhold configured on your plan | [optional] |
| **costConfirmation** | **Boolean**| If the concierge cost should require additional confirmation if a threshold is reached (configured on your plan) | [optional] |
| **country** | **String**| Two letter ISO code of the country of the company | [optional] |
| **financialData** | **Boolean**| If you want financial data of the company to be retrieved | [optional] |
| **historicInformation** | **Boolean**| If you want historical data of the company to be retrieved | [optional] |
| **informationRequirements** | **String**| Requirements on what document or information should be provided. Please be very precise | [optional] |
| **locationInvestigation** | **Boolean**| If the companies residency should be investigated | [optional] |
| **priority** | **String**| Priority of order: standard/express are allowed | [optional] |
| **registerData** | **Boolean**| If you want register data of the company to be retrieved | [optional] |
| **registerNumber** | **String**| Registration number of the company for which a document should be ordered. (Not required if subjectId is given) | [optional] |
| **subjectId** | **String**| Kompanyid of the company you want to place the order for | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="productOrderUbo"></a>
# **productOrderUbo**
> productOrderUbo(subjectId, callbackUrl, credits, includeDocs, levels, strategy)

Places a UBO order

Place an order for a UBO (ultimate beneficial owner) discovery report

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String subjectId = "subjectId_example"; // String | KYC API Id (32 byte hexid) of the company you want to place the order for
    String callbackUrl = "callbackUrl_example"; // String | An optional callback URL to which updates about the order will be sent (for instance if credits are exceeded)
    BigDecimal credits = new BigDecimal(78); // BigDecimal | Specify a maximum amount of credits which should be used. To disable use -1
    Boolean includeDocs = true; // Boolean | Include purchase of register document to ubo report
    String levels = "levels_example"; // String | Define a threshold for different levels of crawling
    String strategy = "strategy_example"; // String | Choose a matching strategy. Available options (FULL,LEVELS)
    try {
      apiInstance.productOrderUbo(subjectId, callbackUrl, credits, includeDocs, levels, strategy);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productOrderUbo");
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
| **subjectId** | **String**| KYC API Id (32 byte hexid) of the company you want to place the order for | |
| **callbackUrl** | **String**| An optional callback URL to which updates about the order will be sent (for instance if credits are exceeded) | [optional] |
| **credits** | **BigDecimal**| Specify a maximum amount of credits which should be used. To disable use -1 | [optional] |
| **includeDocs** | **Boolean**| Include purchase of register document to ubo report | [optional] |
| **levels** | **String**| Define a threshold for different levels of crawling | [optional] |
| **strategy** | **String**| Choose a matching strategy. Available options (FULL,LEVELS) | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="productOrderWithOption"></a>
# **productOrderWithOption**
> productOrderWithOption(sku, option, subjectId)

Places a product order

Place an order for a particular product identified by its SKU with a particular option for a particular company identified by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String sku = "sku_example"; // String | SKU - 9 character value from a Product object
    String option = "option_example"; // String | Product option (e.g. Accounts year) from a previous Availability call
    String subjectId = "subjectId_example"; // String | Subject (e.g. Company) ID - 32 character hex value
    try {
      apiInstance.productOrderWithOption(sku, option, subjectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productOrderWithOption");
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
| **sku** | **String**| SKU - 9 character value from a Product object | |
| **option** | **String**| Product option (e.g. Accounts year) from a previous Availability call | |
| **subjectId** | **String**| Subject (e.g. Company) ID - 32 character hex value | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="productRetrieve"></a>
# **productRetrieve**
> ProductRetrieve200Response productRetrieve(orderId)

Retrieves the result of an order

Retrieves the document or structured data associated with a completed order identified with its order id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String orderId = "orderId_example"; // String | ID of the ProductOrder as returned from a /product/buy call - 32 character hex value
    try {
      ProductRetrieve200Response result = apiInstance.productRetrieve(orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productRetrieve");
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
| **orderId** | **String**| ID of the ProductOrder as returned from a /product/buy call - 32 character hex value | |

### Return type

[**ProductRetrieve200Response**](ProductRetrieve200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details for retrieval of a delivered product |  -  |
| **0** |  |  -  |

<a id="productSearch"></a>
# **productSearch**
> List&lt;ProductSearch200ResponseInner&gt; productSearch(subjectId)

Returns a list of products

Search for possible products for a particular company identified by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String subjectId = "subjectId_example"; // String | Subject (e.g. Company) ID - 32 character hex value
    try {
      List<ProductSearch200ResponseInner> result = apiInstance.productSearch(subjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productSearch");
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
| **subjectId** | **String**| Subject (e.g. Company) ID - 32 character hex value | |

### Return type

[**List&lt;ProductSearch200ResponseInner&gt;**](ProductSearch200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of products |  -  |
| **0** |  |  -  |

<a id="productStatus"></a>
# **productStatus**
> productStatus(orderId)

Returns metadata for a order

Retrieve the current status of an order identified by its order id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String orderId = "orderId_example"; // String | ID of the ProductOrder as returned from a /product/buy call - 32 character hex value
    try {
      apiInstance.productStatus(orderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productStatus");
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
| **orderId** | **String**| ID of the ProductOrder as returned from a /product/buy call - 32 character hex value | |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="productUpdateAction"></a>
# **productUpdateAction**
> productUpdateAction(action, orderId, credits)

Updates metadata of an order

Update an existing order identified by its order id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1ProductApi apiInstance = new V1ProductApi(defaultClient);
    String action = "action_example"; // String | The action you want to perform for the order
    String orderId = "orderId_example"; // String | ID of the ProductOrder as returned from a /product/buy call - 32 character hex value
    BigDecimal credits = new BigDecimal(78); // BigDecimal | Specify an amount of credits which should be added to the order
    try {
      apiInstance.productUpdateAction(action, orderId, credits);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1ProductApi#productUpdateAction");
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
| **action** | **String**| The action you want to perform for the order | |
| **orderId** | **String**| ID of the ProductOrder as returned from a /product/buy call - 32 character hex value | |
| **credits** | **BigDecimal**| Specify an amount of credits which should be added to the order | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |


# TerminalOrdersCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCompaniesCompanyIdBillingEntities**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdBillingEntities) | **GET** /companies/{companyId}/billingEntities | Get a list of billing entities |
| [**getCompaniesCompanyIdShippingLocations**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdShippingLocations) | **GET** /companies/{companyId}/shippingLocations | Get a list of shipping locations |
| [**getCompaniesCompanyIdTerminalModels**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdTerminalModels) | **GET** /companies/{companyId}/terminalModels | Get a list of terminal models |
| [**getCompaniesCompanyIdTerminalOrders**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdTerminalOrders) | **GET** /companies/{companyId}/terminalOrders | Get a list of orders |
| [**getCompaniesCompanyIdTerminalOrdersOrderId**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdTerminalOrdersOrderId) | **GET** /companies/{companyId}/terminalOrders/{orderId} | Get an order |
| [**getCompaniesCompanyIdTerminalProducts**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdTerminalProducts) | **GET** /companies/{companyId}/terminalProducts | Get a list of terminal products |
| [**patchCompaniesCompanyIdTerminalOrdersOrderId**](TerminalOrdersCompanyLevelApi.md#patchCompaniesCompanyIdTerminalOrdersOrderId) | **PATCH** /companies/{companyId}/terminalOrders/{orderId} | Update an order |
| [**postCompaniesCompanyIdShippingLocations**](TerminalOrdersCompanyLevelApi.md#postCompaniesCompanyIdShippingLocations) | **POST** /companies/{companyId}/shippingLocations | Create a shipping location |
| [**postCompaniesCompanyIdTerminalOrders**](TerminalOrdersCompanyLevelApi.md#postCompaniesCompanyIdTerminalOrders) | **POST** /companies/{companyId}/terminalOrders | Create an order |
| [**postCompaniesCompanyIdTerminalOrdersOrderIdCancel**](TerminalOrdersCompanyLevelApi.md#postCompaniesCompanyIdTerminalOrdersOrderIdCancel) | **POST** /companies/{companyId}/terminalOrders/{orderId}/cancel | Cancel an order |


<a id="getCompaniesCompanyIdBillingEntities"></a>
# **getCompaniesCompanyIdBillingEntities**
> BillingEntitiesResponse getCompaniesCompanyIdBillingEntities(companyId, name)

Get a list of billing entities

Returns the billing entities of the company identified in the path and all merchant accounts belonging to the company. A billing entity is a legal entity where we charge orders to. An order for terminal products must contain the ID of a billing entity.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalOrdersCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalOrdersCompanyLevelApi apiInstance = new TerminalOrdersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String name = "name_example"; // String | The name of the billing entity.
    try {
      BillingEntitiesResponse result = apiInstance.getCompaniesCompanyIdBillingEntities(companyId, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalOrdersCompanyLevelApi#getCompaniesCompanyIdBillingEntities");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **name** | **String**| The name of the billing entity. | [optional] |

### Return type

[**BillingEntitiesResponse**](BillingEntitiesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdShippingLocations"></a>
# **getCompaniesCompanyIdShippingLocations**
> ShippingLocationsResponse getCompaniesCompanyIdShippingLocations(companyId, name, offset, limit)

Get a list of shipping locations

Returns the shipping locations for the company identified in the path and all merchant accounts belonging to the company. A shipping location includes the address where orders can be delivered, and an ID which you need to specify when ordering terminal products.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalOrdersCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalOrdersCompanyLevelApi apiInstance = new TerminalOrdersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String name = "name_example"; // String | The name of the shipping location.
    Integer offset = 56; // Integer | The number of locations to skip.
    Integer limit = 56; // Integer | The number of locations to return.
    try {
      ShippingLocationsResponse result = apiInstance.getCompaniesCompanyIdShippingLocations(companyId, name, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalOrdersCompanyLevelApi#getCompaniesCompanyIdShippingLocations");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **name** | **String**| The name of the shipping location. | [optional] |
| **offset** | **Integer**| The number of locations to skip. | [optional] |
| **limit** | **Integer**| The number of locations to return. | [optional] |

### Return type

[**ShippingLocationsResponse**](ShippingLocationsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdTerminalModels"></a>
# **getCompaniesCompanyIdTerminalModels**
> TerminalModelsResponse getCompaniesCompanyIdTerminalModels(companyId)

Get a list of terminal models

Returns a list of payment terminal models that the company identified in the path has access to. The response includes the terminal model ID, which can be used as a query parameter when getting a list of terminals or a list of products for ordering.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalOrdersCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalOrdersCompanyLevelApi apiInstance = new TerminalOrdersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    try {
      TerminalModelsResponse result = apiInstance.getCompaniesCompanyIdTerminalModels(companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalOrdersCompanyLevelApi#getCompaniesCompanyIdTerminalModels");
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
| **companyId** | **String**| The unique identifier of the company account. | |

### Return type

[**TerminalModelsResponse**](TerminalModelsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdTerminalOrders"></a>
# **getCompaniesCompanyIdTerminalOrders**
> TerminalOrdersResponse getCompaniesCompanyIdTerminalOrders(companyId, customerOrderReference, status, offset, limit)

Get a list of orders

Returns a lists of terminal products orders for the company identified in the path. To filter the list, use one or more of the query parameters.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalOrdersCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalOrdersCompanyLevelApi apiInstance = new TerminalOrdersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String customerOrderReference = "customerOrderReference_example"; // String | Your purchase order number.
    String status = "status_example"; // String | The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped, Delivered.
    Integer offset = 56; // Integer | The number of orders to skip.
    Integer limit = 56; // Integer | The number of orders to return.
    try {
      TerminalOrdersResponse result = apiInstance.getCompaniesCompanyIdTerminalOrders(companyId, customerOrderReference, status, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalOrdersCompanyLevelApi#getCompaniesCompanyIdTerminalOrders");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **customerOrderReference** | **String**| Your purchase order number. | [optional] |
| **status** | **String**| The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped, Delivered. | [optional] |
| **offset** | **Integer**| The number of orders to skip. | [optional] |
| **limit** | **Integer**| The number of orders to return. | [optional] |

### Return type

[**TerminalOrdersResponse**](TerminalOrdersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdTerminalOrdersOrderId"></a>
# **getCompaniesCompanyIdTerminalOrdersOrderId**
> TerminalOrder getCompaniesCompanyIdTerminalOrdersOrderId(companyId, orderId)

Get an order

Returns the details of the terminal products order identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalOrdersCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalOrdersCompanyLevelApi apiInstance = new TerminalOrdersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String orderId = "orderId_example"; // String | The unique identifier of the order.
    try {
      TerminalOrder result = apiInstance.getCompaniesCompanyIdTerminalOrdersOrderId(companyId, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalOrdersCompanyLevelApi#getCompaniesCompanyIdTerminalOrdersOrderId");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **orderId** | **String**| The unique identifier of the order. | |

### Return type

[**TerminalOrder**](TerminalOrder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdTerminalProducts"></a>
# **getCompaniesCompanyIdTerminalProducts**
> TerminalProductsResponse getCompaniesCompanyIdTerminalProducts(companyId, country, terminalModelId, offset, limit)

Get a list of terminal products

Returns a country-specific list of payment terminal packages and parts that the company identified in the path has access to.   To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalOrdersCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalOrdersCompanyLevelApi apiInstance = new TerminalOrdersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String country = "country_example"; // String | The country to return products for, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **US**
    String terminalModelId = "terminalModelId_example"; // String | The terminal model to return products for. Use the ID returned in the [GET `/terminalModels`](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels) response. For example, **Verifone.M400**
    Integer offset = 56; // Integer | The number of products to skip.
    Integer limit = 56; // Integer | The number of products to return.
    try {
      TerminalProductsResponse result = apiInstance.getCompaniesCompanyIdTerminalProducts(companyId, country, terminalModelId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalOrdersCompanyLevelApi#getCompaniesCompanyIdTerminalProducts");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **country** | **String**| The country to return products for, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **US** | |
| **terminalModelId** | **String**| The terminal model to return products for. Use the ID returned in the [GET &#x60;/terminalModels&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels) response. For example, **Verifone.M400** | [optional] |
| **offset** | **Integer**| The number of products to skip. | [optional] |
| **limit** | **Integer**| The number of products to return. | [optional] |

### Return type

[**TerminalProductsResponse**](TerminalProductsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchCompaniesCompanyIdTerminalOrdersOrderId"></a>
# **patchCompaniesCompanyIdTerminalOrdersOrderId**
> TerminalOrder patchCompaniesCompanyIdTerminalOrdersOrderId(companyId, orderId, terminalOrderRequest)

Update an order

Updates the terminal products order identified in the path. Updating is only possible while the order has the status **Placed**.  The request body only needs to contain what you want to change.  However, to update the products in the &#x60;items&#x60; array, you must provide the entire array. For example, if the array has three items:  To remove one item, the array must include the remaining two items. Or to add one item, the array must include all four items.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalOrdersCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalOrdersCompanyLevelApi apiInstance = new TerminalOrdersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String orderId = "orderId_example"; // String | The unique identifier of the order.
    TerminalOrderRequest terminalOrderRequest = new TerminalOrderRequest(); // TerminalOrderRequest | 
    try {
      TerminalOrder result = apiInstance.patchCompaniesCompanyIdTerminalOrdersOrderId(companyId, orderId, terminalOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalOrdersCompanyLevelApi#patchCompaniesCompanyIdTerminalOrdersOrderId");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **orderId** | **String**| The unique identifier of the order. | |
| **terminalOrderRequest** | [**TerminalOrderRequest**](TerminalOrderRequest.md)|  | [optional] |

### Return type

[**TerminalOrder**](TerminalOrder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCompaniesCompanyIdShippingLocations"></a>
# **postCompaniesCompanyIdShippingLocations**
> ShippingLocation postCompaniesCompanyIdShippingLocations(companyId, shippingLocation)

Create a shipping location

Creates a shipping location for the company identified in the path. A shipping location defines an address where orders can be delivered.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalOrdersCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalOrdersCompanyLevelApi apiInstance = new TerminalOrdersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    ShippingLocation shippingLocation = new ShippingLocation(); // ShippingLocation | 
    try {
      ShippingLocation result = apiInstance.postCompaniesCompanyIdShippingLocations(companyId, shippingLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalOrdersCompanyLevelApi#postCompaniesCompanyIdShippingLocations");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **shippingLocation** | [**ShippingLocation**](ShippingLocation.md)|  | [optional] |

### Return type

[**ShippingLocation**](ShippingLocation.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCompaniesCompanyIdTerminalOrders"></a>
# **postCompaniesCompanyIdTerminalOrders**
> TerminalOrder postCompaniesCompanyIdTerminalOrders(companyId, terminalOrderRequest)

Create an order

Creates an order for payment terminal products for the company identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write &gt;Requests to the Management API test endpoint do not create actual orders for test terminals. To order test terminals, you need to [submit a sales order](https://docs.adyen.com/point-of-sale/managing-terminals/order-terminals/#sales-order-steps) in your Customer Area.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalOrdersCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalOrdersCompanyLevelApi apiInstance = new TerminalOrdersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    TerminalOrderRequest terminalOrderRequest = new TerminalOrderRequest(); // TerminalOrderRequest | 
    try {
      TerminalOrder result = apiInstance.postCompaniesCompanyIdTerminalOrders(companyId, terminalOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalOrdersCompanyLevelApi#postCompaniesCompanyIdTerminalOrders");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **terminalOrderRequest** | [**TerminalOrderRequest**](TerminalOrderRequest.md)|  | [optional] |

### Return type

[**TerminalOrder**](TerminalOrder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCompaniesCompanyIdTerminalOrdersOrderIdCancel"></a>
# **postCompaniesCompanyIdTerminalOrdersOrderIdCancel**
> TerminalOrder postCompaniesCompanyIdTerminalOrdersOrderIdCancel(companyId, orderId)

Cancel an order

Cancels the terminal products order identified in the path. Cancelling is only possible while the order has the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the full order details, but with the status changed to **Cancelled**.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalOrdersCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalOrdersCompanyLevelApi apiInstance = new TerminalOrdersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String orderId = "orderId_example"; // String | The unique identifier of the order.
    try {
      TerminalOrder result = apiInstance.postCompaniesCompanyIdTerminalOrdersOrderIdCancel(companyId, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalOrdersCompanyLevelApi#postCompaniesCompanyIdTerminalOrdersOrderIdCancel");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **orderId** | **String**| The unique identifier of the order. | |

### Return type

[**TerminalOrder**](TerminalOrder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |


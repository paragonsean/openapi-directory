# BillingApi

All URIs are relative to *https://api.illumidesk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingCardsCreate**](BillingApi.md#billingCardsCreate) | **POST** /v1/{namespace}/billing/cards/ | Create new credit card |
| [**billingCardsDelete**](BillingApi.md#billingCardsDelete) | **DELETE** /v1/{namespace}/billing/cards/{id}/ | Delete a credit card |
| [**billingCardsList**](BillingApi.md#billingCardsList) | **GET** /v1/{namespace}/billing/cards/ | Get credit cards |
| [**billingCardsRead**](BillingApi.md#billingCardsRead) | **GET** /v1/{namespace}/billing/cards/{id}/ | Get credit card by id |
| [**billingCardsReplace**](BillingApi.md#billingCardsReplace) | **PUT** /v1/{namespace}/billing/cards/{id}/ | Replace a credit card |
| [**billingCardsUpdate**](BillingApi.md#billingCardsUpdate) | **PATCH** /v1/{namespace}/billing/cards/{id}/ | Update a credit card |
| [**billingInvoiceItemsList**](BillingApi.md#billingInvoiceItemsList) | **GET** /v1/{namespace}/billing/invoices/{invoice_id}/invoice-items/ | Get invoice items for a given invoice. |
| [**billingInvoiceItemsRead**](BillingApi.md#billingInvoiceItemsRead) | **GET** /v1/{namespace}/billing/invoices/{invoice_id}/invoice-items/{id} | Get a specific InvoiceItem. |
| [**billingInvoicesList**](BillingApi.md#billingInvoicesList) | **GET** /v1/{namespace}/billing/invoices/ | Get invoices |
| [**billingInvoicesRead**](BillingApi.md#billingInvoicesRead) | **GET** /v1/{namespace}/billing/invoices/{id}/ | Get an invoice |
| [**billingPlansList**](BillingApi.md#billingPlansList) | **GET** /v1/{namespace}/billing/plans/ | Get billing plans |
| [**billingPlansRead**](BillingApi.md#billingPlansRead) | **GET** /v1/{namespace}/billing/plans/{id}/ | Get a billing plan |
| [**billingSubscriptionsCreate**](BillingApi.md#billingSubscriptionsCreate) | **POST** /v1/{namespace}/billing/subscriptions/ | Create a new subscription |
| [**billingSubscriptionsDelete**](BillingApi.md#billingSubscriptionsDelete) | **DELETE** /v1/{namespace}/billing/subscriptions/{id}/ | Delete a subscription |
| [**billingSubscriptionsList**](BillingApi.md#billingSubscriptionsList) | **GET** /v1/{namespace}/billing/subscriptions/ | Get active subscriptons |
| [**billingSubscriptionsRead**](BillingApi.md#billingSubscriptionsRead) | **GET** /v1/{namespace}/billing/subscriptions/{id}/ | Get a subscriptions |
| [**teamsBillingInvoiceItemsList_0**](BillingApi.md#teamsBillingInvoiceItemsList_0) | **GET** /v1/teams/{team}/billing/invoices/{invoice_id}/invoice-items/ | Get team invoice items for a given invoice. |
| [**teamsBillingInvoiceItemsRead_0**](BillingApi.md#teamsBillingInvoiceItemsRead_0) | **GET** /v1/teams/{team}/billing/invoices/{invoice_id}/invoice-items/{id} | Get a specific team InvoiceItem. |
| [**teamsBillingInvoicesList_0**](BillingApi.md#teamsBillingInvoicesList_0) | **GET** /v1/teams/{team}/billing/invoices/ | Get team invoices |
| [**teamsBillingInvoicesRead_0**](BillingApi.md#teamsBillingInvoicesRead_0) | **GET** /v1/teams/{team}/billing/invoices/{id}/ | Get an invoice |
| [**teamsBillingSubscriptionsCreate_0**](BillingApi.md#teamsBillingSubscriptionsCreate_0) | **POST** /v1/teams/{team}/billing/subscriptions/ | Create a new team subscription |
| [**teamsBillingSubscriptionsDelete_0**](BillingApi.md#teamsBillingSubscriptionsDelete_0) | **DELETE** /v1/teams/{team}/billing/subscriptions/{id}/ | Delete a subscription |
| [**teamsBillingSubscriptionsList_0**](BillingApi.md#teamsBillingSubscriptionsList_0) | **GET** /v1/teams/{team}/billing/subscriptions/ | Get active team subscriptons |
| [**teamsBillingSubscriptionsRead_0**](BillingApi.md#teamsBillingSubscriptionsRead_0) | **GET** /v1/teams/{team}/billing/subscriptions/{id}/ | Get team subscriptions |


<a id="billingCardsCreate"></a>
# **billingCardsCreate**
> Card billingCardsCreate(namespace, cardData)

Create new credit card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    CardDataPost cardData = new CardDataPost(); // CardDataPost | 
    try {
      Card result = apiInstance.billingCardsCreate(namespace, cardData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingCardsCreate");
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
| **namespace** | **String**| User or team name. | |
| **cardData** | [**CardDataPost**](CardDataPost.md)|  | [optional] |

### Return type

[**Card**](Card.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Card created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="billingCardsDelete"></a>
# **billingCardsDelete**
> billingCardsDelete(namespace, id)

Delete a credit card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Card unique identifier expressed as UUID.
    try {
      apiInstance.billingCardsDelete(namespace, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingCardsDelete");
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
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Card unique identifier expressed as UUID. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Card deleted. |  -  |
| **404** | Card not found. |  -  |

<a id="billingCardsList"></a>
# **billingCardsList**
> List&lt;Card&gt; billingCardsList(namespace, limit, offset, ordering)

Get credit cards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Set limit when retrieving credit or debit cards.
    String offset = "offset_example"; // String | Set offset when retriving cards.
    String ordering = "ordering_example"; // String | Order when retrieving cards.
    try {
      List<Card> result = apiInstance.billingCardsList(namespace, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingCardsList");
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
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Set limit when retrieving credit or debit cards. | [optional] |
| **offset** | **String**| Set offset when retriving cards. | [optional] |
| **ordering** | **String**| Order when retrieving cards. | [optional] |

### Return type

[**List&lt;Card&gt;**](Card.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card list |  -  |

<a id="billingCardsRead"></a>
# **billingCardsRead**
> Card billingCardsRead(namespace, id)

Get credit card by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | User unique identifier expressed as UUID.
    try {
      Card result = apiInstance.billingCardsRead(namespace, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingCardsRead");
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
| **namespace** | **String**| User or team name. | |
| **id** | **String**| User unique identifier expressed as UUID. | |

### Return type

[**Card**](Card.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card retrieved. |  -  |
| **404** | Card not found. |  -  |

<a id="billingCardsReplace"></a>
# **billingCardsReplace**
> Card billingCardsReplace(namespace, id, cardData)

Replace a credit card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | 
    CardDataPutandPatch cardData = new CardDataPutandPatch(); // CardDataPutandPatch | 
    try {
      Card result = apiInstance.billingCardsReplace(namespace, id, cardData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingCardsReplace");
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
| **namespace** | **String**| User or team name. | |
| **id** | **String**|  | |
| **cardData** | [**CardDataPutandPatch**](CardDataPutandPatch.md)|  | [optional] |

### Return type

[**Card**](Card.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card updated |  -  |
| **400** | Invalid data supplied |  -  |

<a id="billingCardsUpdate"></a>
# **billingCardsUpdate**
> Card billingCardsUpdate(namespace, id, cardData)

Update a credit card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Card unique identifier.
    CardDataPutandPatch cardData = new CardDataPutandPatch(); // CardDataPutandPatch | 
    try {
      Card result = apiInstance.billingCardsUpdate(namespace, id, cardData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingCardsUpdate");
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
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Card unique identifier. | |
| **cardData** | [**CardDataPutandPatch**](CardDataPutandPatch.md)|  | [optional] |

### Return type

[**Card**](Card.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Card not found |  -  |

<a id="billingInvoiceItemsList"></a>
# **billingInvoiceItemsList**
> List&lt;InvoiceItem&gt; billingInvoiceItemsList(namespace, invoiceId, limit, offset, ordering)

Get invoice items for a given invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    String ordering = "ordering_example"; // String | Ordering when getting items.
    try {
      List<InvoiceItem> result = apiInstance.billingInvoiceItemsList(namespace, invoiceId, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingInvoiceItemsList");
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
| **namespace** | **String**| User or team name. | |
| **invoiceId** | **String**| Invoice id, expressed as UUID. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |
| **ordering** | **String**| Ordering when getting items. | [optional] |

### Return type

[**List&lt;InvoiceItem&gt;**](InvoiceItem.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InvoiceItem list. |  -  |

<a id="billingInvoiceItemsRead"></a>
# **billingInvoiceItemsRead**
> InvoiceItem billingInvoiceItemsRead(namespace, invoiceId, id)

Get a specific InvoiceItem.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
    String id = "id_example"; // String | InvoiceItem id, expressed as UUID.
    try {
      InvoiceItem result = apiInstance.billingInvoiceItemsRead(namespace, invoiceId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingInvoiceItemsRead");
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
| **namespace** | **String**| User or team name. | |
| **invoiceId** | **String**| Invoice id, expressed as UUID. | |
| **id** | **String**| InvoiceItem id, expressed as UUID. | |

### Return type

[**InvoiceItem**](InvoiceItem.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InvoiceItem retrieved. |  -  |
| **404** | InvoiceItem not found. |  -  |

<a id="billingInvoicesList"></a>
# **billingInvoicesList**
> List&lt;Invoice&gt; billingInvoicesList(namespace, limit, offset, ordering)

Get invoices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    String ordering = "ordering_example"; // String | Ordering when getting items.
    try {
      List<Invoice> result = apiInstance.billingInvoicesList(namespace, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingInvoicesList");
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
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |
| **ordering** | **String**| Ordering when getting items. | [optional] |

### Return type

[**List&lt;Invoice&gt;**](Invoice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoice list. |  -  |

<a id="billingInvoicesRead"></a>
# **billingInvoicesRead**
> Invoice billingInvoicesRead(namespace, id)

Get an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Invoice unique identifier expressed as UUID.
    try {
      Invoice result = apiInstance.billingInvoicesRead(namespace, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingInvoicesRead");
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
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Invoice unique identifier expressed as UUID. | |

### Return type

[**Invoice**](Invoice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoice retrieved. |  -  |
| **404** | Invoice not found. |  -  |

<a id="billingPlansList"></a>
# **billingPlansList**
> List&lt;Plan&gt; billingPlansList(namespace, limit, offset, ordering)

Get billing plans

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    String ordering = "ordering_example"; // String | Ordering when getting items.
    try {
      List<Plan> result = apiInstance.billingPlansList(namespace, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingPlansList");
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
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |
| **ordering** | **String**| Ordering when getting items. | [optional] |

### Return type

[**List&lt;Plan&gt;**](Plan.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Plan list. |  -  |

<a id="billingPlansRead"></a>
# **billingPlansRead**
> Plan billingPlansRead(namespace, id)

Get a billing plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Plan unique identifier expressed as UUID.
    try {
      Plan result = apiInstance.billingPlansRead(namespace, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingPlansRead");
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
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Plan unique identifier expressed as UUID. | |

### Return type

[**Plan**](Plan.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Plan retrieved |  -  |
| **404** | Plan not found |  -  |

<a id="billingSubscriptionsCreate"></a>
# **billingSubscriptionsCreate**
> Subscription billingSubscriptionsCreate(namespace, subscriptionData)

Create a new subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    SubscriptionData subscriptionData = new SubscriptionData(); // SubscriptionData | 
    try {
      Subscription result = apiInstance.billingSubscriptionsCreate(namespace, subscriptionData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingSubscriptionsCreate");
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
| **namespace** | **String**| User or team name. | |
| **subscriptionData** | [**SubscriptionData**](SubscriptionData.md)|  | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Subscription created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="billingSubscriptionsDelete"></a>
# **billingSubscriptionsDelete**
> billingSubscriptionsDelete(namespace, id)

Delete a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Subscription unique identifier expressed as UUID.
    try {
      apiInstance.billingSubscriptionsDelete(namespace, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingSubscriptionsDelete");
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
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Subscription unique identifier expressed as UUID. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Subscription deleted. |  -  |
| **404** | Subscription not found. |  -  |

<a id="billingSubscriptionsList"></a>
# **billingSubscriptionsList**
> List&lt;Subscription&gt; billingSubscriptionsList(namespace, limit, offset, ordering)

Get active subscriptons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    String ordering = "ordering_example"; // String | Ordering when getting items.
    try {
      List<Subscription> result = apiInstance.billingSubscriptionsList(namespace, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingSubscriptionsList");
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
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |
| **ordering** | **String**| Ordering when getting items. | [optional] |

### Return type

[**List&lt;Subscription&gt;**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription list. |  -  |

<a id="billingSubscriptionsRead"></a>
# **billingSubscriptionsRead**
> Subscription billingSubscriptionsRead(namespace, id)

Get a subscriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Unique identifier expressed as UUID.
    try {
      Subscription result = apiInstance.billingSubscriptionsRead(namespace, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingSubscriptionsRead");
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
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Unique identifier expressed as UUID. | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription retrieved. |  -  |
| **404** | Subscription not found. |  -  |

<a id="teamsBillingInvoiceItemsList_0"></a>
# **teamsBillingInvoiceItemsList_0**
> List&lt;InvoiceItem&gt; teamsBillingInvoiceItemsList_0(team, invoiceId, limit, offset, ordering)

Get team invoice items for a given invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    String ordering = "ordering_example"; // String | Ordering when getting items.
    try {
      List<InvoiceItem> result = apiInstance.teamsBillingInvoiceItemsList_0(team, invoiceId, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#teamsBillingInvoiceItemsList_0");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **invoiceId** | **String**| Invoice id, expressed as UUID. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |
| **ordering** | **String**| Ordering when getting items. | [optional] |

### Return type

[**List&lt;InvoiceItem&gt;**](InvoiceItem.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team invoiceItem list. |  -  |

<a id="teamsBillingInvoiceItemsRead_0"></a>
# **teamsBillingInvoiceItemsRead_0**
> InvoiceItem teamsBillingInvoiceItemsRead_0(team, invoiceId, id)

Get a specific team InvoiceItem.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
    String id = "id_example"; // String | InvoiceItem id, expressed as UUID.
    try {
      InvoiceItem result = apiInstance.teamsBillingInvoiceItemsRead_0(team, invoiceId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#teamsBillingInvoiceItemsRead_0");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **invoiceId** | **String**| Invoice id, expressed as UUID. | |
| **id** | **String**| InvoiceItem id, expressed as UUID. | |

### Return type

[**InvoiceItem**](InvoiceItem.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team invoiceItem retrieved. |  -  |
| **404** | InvoiceItem not found. |  -  |

<a id="teamsBillingInvoicesList_0"></a>
# **teamsBillingInvoicesList_0**
> List&lt;Invoice&gt; teamsBillingInvoicesList_0(team, limit, offset)

Get team invoices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    try {
      List<Invoice> result = apiInstance.teamsBillingInvoicesList_0(team, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#teamsBillingInvoicesList_0");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |

### Return type

[**List&lt;Invoice&gt;**](Invoice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoice list. |  -  |

<a id="teamsBillingInvoicesRead_0"></a>
# **teamsBillingInvoicesRead_0**
> Invoice teamsBillingInvoicesRead_0(team, id)

Get an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String id = "id_example"; // String | Invoice unique identifier expressed as UUID.
    try {
      Invoice result = apiInstance.teamsBillingInvoicesRead_0(team, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#teamsBillingInvoicesRead_0");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **id** | **String**| Invoice unique identifier expressed as UUID. | |

### Return type

[**Invoice**](Invoice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team invoice retrieved. |  -  |
| **404** | Team invoice not found. |  -  |

<a id="teamsBillingSubscriptionsCreate_0"></a>
# **teamsBillingSubscriptionsCreate_0**
> Subscription teamsBillingSubscriptionsCreate_0(team, subscriptionData)

Create a new team subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    SubscriptionData subscriptionData = new SubscriptionData(); // SubscriptionData | 
    try {
      Subscription result = apiInstance.teamsBillingSubscriptionsCreate_0(team, subscriptionData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#teamsBillingSubscriptionsCreate_0");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **subscriptionData** | [**SubscriptionData**](SubscriptionData.md)|  | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Team subscription created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="teamsBillingSubscriptionsDelete_0"></a>
# **teamsBillingSubscriptionsDelete_0**
> teamsBillingSubscriptionsDelete_0(team, id)

Delete a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String id = "id_example"; // String | Subscription unique identifier expressed as UUID.
    try {
      apiInstance.teamsBillingSubscriptionsDelete_0(team, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#teamsBillingSubscriptionsDelete_0");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **id** | **String**| Subscription unique identifier expressed as UUID. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Subscription deleted. |  -  |
| **404** | Subscription not found. |  -  |

<a id="teamsBillingSubscriptionsList_0"></a>
# **teamsBillingSubscriptionsList_0**
> List&lt;Subscription&gt; teamsBillingSubscriptionsList_0(team, limit, offset, ordering)

Get active team subscriptons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String limit = "limit_example"; // String | Limit when getting items.
    String offset = "offset_example"; // String | Offset when getting items.
    String ordering = "ordering_example"; // String | Ordering when getting items.
    try {
      List<Subscription> result = apiInstance.teamsBillingSubscriptionsList_0(team, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#teamsBillingSubscriptionsList_0");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **limit** | **String**| Limit when getting items. | [optional] |
| **offset** | **String**| Offset when getting items. | [optional] |
| **ordering** | **String**| Ordering when getting items. | [optional] |

### Return type

[**List&lt;Subscription&gt;**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Teams subscription list. |  -  |

<a id="teamsBillingSubscriptionsRead_0"></a>
# **teamsBillingSubscriptionsRead_0**
> Subscription teamsBillingSubscriptionsRead_0(team, id)

Get team subscriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String team = "team_example"; // String | Team unique identifier expressed as UUID or name.
    String id = "id_example"; // String | Unique identifier expressed as UUID.
    try {
      Subscription result = apiInstance.teamsBillingSubscriptionsRead_0(team, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#teamsBillingSubscriptionsRead_0");
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
| **team** | **String**| Team unique identifier expressed as UUID or name. | |
| **id** | **String**| Unique identifier expressed as UUID. | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team subscription retrieved. |  -  |
| **404** | Subscription not found. |  -  |


# InvoicesApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelInvoice**](InvoicesApi.md#cancelInvoice) | **POST** /v2/invoices/{invoice_id}/cancel | CancelInvoice |
| [**createInvoice**](InvoicesApi.md#createInvoice) | **POST** /v2/invoices | CreateInvoice |
| [**deleteInvoice**](InvoicesApi.md#deleteInvoice) | **DELETE** /v2/invoices/{invoice_id} | DeleteInvoice |
| [**getInvoice**](InvoicesApi.md#getInvoice) | **GET** /v2/invoices/{invoice_id} | GetInvoice |
| [**listInvoices**](InvoicesApi.md#listInvoices) | **GET** /v2/invoices | ListInvoices |
| [**publishInvoice**](InvoicesApi.md#publishInvoice) | **POST** /v2/invoices/{invoice_id}/publish | PublishInvoice |
| [**searchInvoices**](InvoicesApi.md#searchInvoices) | **POST** /v2/invoices/search | SearchInvoices |
| [**updateInvoice**](InvoicesApi.md#updateInvoice) | **PUT** /v2/invoices/{invoice_id} | UpdateInvoice |


<a id="cancelInvoice"></a>
# **cancelInvoice**
> CancelInvoiceResponse cancelInvoice(invoiceId, cancelInvoiceRequest)

CancelInvoice

Cancels an invoice. The seller cannot collect payments for  the canceled invoice.  You cannot cancel an invoice in the &#x60;DRAFT&#x60; state or in a terminal state: &#x60;PAID&#x60;, &#x60;REFUNDED&#x60;, &#x60;CANCELED&#x60;, or &#x60;FAILED&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String invoiceId = "invoiceId_example"; // String | The ID of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel.
    CancelInvoiceRequest cancelInvoiceRequest = new CancelInvoiceRequest(); // CancelInvoiceRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CancelInvoiceResponse result = apiInstance.cancelInvoice(invoiceId, cancelInvoiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#cancelInvoice");
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
| **invoiceId** | **String**| The ID of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel. | |
| **cancelInvoiceRequest** | [**CancelInvoiceRequest**](CancelInvoiceRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CancelInvoiceResponse**](CancelInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="createInvoice"></a>
# **createInvoice**
> CreateInvoiceResponse createInvoice(createInvoiceRequest)

CreateInvoice

Creates a draft [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice)  for an order created using the Orders API.  A draft invoice remains in your account and no action is taken.  You must publish the invoice before Square can process it (send it to the customer&#39;s email address or charge the customer’s card on file).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    CreateInvoiceRequest createInvoiceRequest = new CreateInvoiceRequest(); // CreateInvoiceRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateInvoiceResponse result = apiInstance.createInvoice(createInvoiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#createInvoice");
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
| **createInvoiceRequest** | [**CreateInvoiceRequest**](CreateInvoiceRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateInvoiceResponse**](CreateInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deleteInvoice"></a>
# **deleteInvoice**
> DeleteInvoiceResponse deleteInvoice(invoiceId, version)

DeleteInvoice

Deletes the specified invoice. When an invoice is deleted, the  associated order status changes to CANCELED. You can only delete a draft  invoice (you cannot delete a published invoice, including one that is scheduled for processing).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String invoiceId = "invoiceId_example"; // String | The ID of the invoice to delete.
    Integer version = 56; // Integer | The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to delete. If you do not know the version, you can call [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or  [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices).
    try {
      DeleteInvoiceResponse result = apiInstance.deleteInvoice(invoiceId, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#deleteInvoice");
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
| **invoiceId** | **String**| The ID of the invoice to delete. | |
| **version** | **Integer**| The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to delete. If you do not know the version, you can call [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or  [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices). | [optional] |

### Return type

[**DeleteInvoiceResponse**](DeleteInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getInvoice"></a>
# **getInvoice**
> GetInvoiceResponse getInvoice(invoiceId)

GetInvoice

Retrieves an invoice by invoice ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String invoiceId = "invoiceId_example"; // String | The ID of the invoice to retrieve.
    try {
      GetInvoiceResponse result = apiInstance.getInvoice(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#getInvoice");
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
| **invoiceId** | **String**| The ID of the invoice to retrieve. | |

### Return type

[**GetInvoiceResponse**](GetInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listInvoices"></a>
# **listInvoices**
> ListInvoicesResponse listInvoices(locationId, cursor, limit)

ListInvoices

Returns a list of invoices for a given location. The response  is paginated. If truncated, the response includes a &#x60;cursor&#x60; that you     use in a subsequent request to retrieve the next set of invoices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String locationId = "locationId_example"; // String | The ID of the location for which to list invoices.
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint.  Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    Integer limit = 56; // Integer | The maximum number of invoices to return (200 is the maximum `limit`).  If not provided, the server uses a default limit of 100 invoices.
    try {
      ListInvoicesResponse result = apiInstance.listInvoices(locationId, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#listInvoices");
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
| **locationId** | **String**| The ID of the location for which to list invoices. | |
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint.  Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] |
| **limit** | **Integer**| The maximum number of invoices to return (200 is the maximum &#x60;limit&#x60;).  If not provided, the server uses a default limit of 100 invoices. | [optional] |

### Return type

[**ListInvoicesResponse**](ListInvoicesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="publishInvoice"></a>
# **publishInvoice**
> PublishInvoiceResponse publishInvoice(invoiceId, publishInvoiceRequest)

PublishInvoice

Publishes the specified draft invoice.   After an invoice is published, Square  follows up based on the invoice configuration. For example, Square  sends the invoice to the customer&#39;s email address, charges the customer&#39;s card on file, or does  nothing. Square also makes the invoice available on a Square-hosted invoice page.   The invoice &#x60;status&#x60; also changes from &#x60;DRAFT&#x60; to a status  based on the invoice configuration. For example, the status changes to &#x60;UNPAID&#x60; if  Square emails the invoice or &#x60;PARTIALLY_PAID&#x60; if Square charge a card on file for a portion of the  invoice amount.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String invoiceId = "invoiceId_example"; // String | The ID of the invoice to publish.
    PublishInvoiceRequest publishInvoiceRequest = new PublishInvoiceRequest(); // PublishInvoiceRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      PublishInvoiceResponse result = apiInstance.publishInvoice(invoiceId, publishInvoiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#publishInvoice");
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
| **invoiceId** | **String**| The ID of the invoice to publish. | |
| **publishInvoiceRequest** | [**PublishInvoiceRequest**](PublishInvoiceRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**PublishInvoiceResponse**](PublishInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="searchInvoices"></a>
# **searchInvoices**
> SearchInvoicesResponse searchInvoices(searchInvoicesRequest)

SearchInvoices

Searches for invoices from a location specified in  the filter. You can optionally specify customers in the filter for whom to  retrieve invoices. In the current implementation, you can only specify one location and  optionally one customer.  The response is paginated. If truncated, the response includes a &#x60;cursor&#x60;  that you use in a subsequent request to retrieve the next set of invoices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    SearchInvoicesRequest searchInvoicesRequest = new SearchInvoicesRequest(); // SearchInvoicesRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      SearchInvoicesResponse result = apiInstance.searchInvoices(searchInvoicesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#searchInvoices");
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
| **searchInvoicesRequest** | [**SearchInvoicesRequest**](SearchInvoicesRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**SearchInvoicesResponse**](SearchInvoicesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateInvoice"></a>
# **updateInvoice**
> UpdateInvoiceResponse updateInvoice(invoiceId, updateInvoiceRequest)

UpdateInvoice

Updates an invoice by modifying fields, clearing fields, or both. For most updates, you can use a sparse  &#x60;Invoice&#x60; object to add fields or change values and use the &#x60;fields_to_clear&#x60; field to specify fields to clear.  However, some restrictions apply. For example, you cannot change the &#x60;order_id&#x60; or &#x60;location_id&#x60; field and you  must provide the complete &#x60;custom_fields&#x60; list to update a custom field. Published invoices have additional restrictions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String invoiceId = "invoiceId_example"; // String | The ID of the invoice to update.
    UpdateInvoiceRequest updateInvoiceRequest = new UpdateInvoiceRequest(); // UpdateInvoiceRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      UpdateInvoiceResponse result = apiInstance.updateInvoice(invoiceId, updateInvoiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#updateInvoice");
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
| **invoiceId** | **String**| The ID of the invoice to update. | |
| **updateInvoiceRequest** | [**UpdateInvoiceRequest**](UpdateInvoiceRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**UpdateInvoiceResponse**](UpdateInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


# InvoicesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkDeleteInvoices**](InvoicesApi.md#bulkDeleteInvoices) | **DELETE** /invoices/bulkDelete | Bulk delete invoices |
| [**invoicesGet**](InvoicesApi.md#invoicesGet) | **GET** /invoices | View list of invoices |
| [**invoicesInvoiceIdCopyPost**](InvoicesApi.md#invoicesInvoiceIdCopyPost) | **POST** /invoices/{invoice_id}/copy | Create a copy of an invoice |
| [**invoicesInvoiceIdDelete**](InvoicesApi.md#invoicesInvoiceIdDelete) | **DELETE** /invoices/{invoice_id} | Delete invoice |
| [**invoicesInvoiceIdGet**](InvoicesApi.md#invoicesInvoiceIdGet) | **GET** /invoices/{invoice_id} | View invoice |
| [**invoicesInvoiceIdLinkProjectPdfPost**](InvoicesApi.md#invoicesInvoiceIdLinkProjectPdfPost) | **POST** /invoices/{invoice_id}/linkProjectPdf | Creates an invoice file containing the project&#39;s pdf overview |
| [**invoicesInvoiceIdPut**](InvoicesApi.md#invoicesInvoiceIdPut) | **PUT** /invoices/{invoice_id} | Edit invoice |
| [**invoicesInvoiceIdUnlinkProjectPdfPost**](InvoicesApi.md#invoicesInvoiceIdUnlinkProjectPdfPost) | **POST** /invoices/{invoice_id}/unlinkProjectPdf | Deletes the linked project overview pdf |
| [**invoicesPost**](InvoicesApi.md#invoicesPost) | **POST** /invoices | Add invoice |
| [**invoicesVatOptionsGet**](InvoicesApi.md#invoicesVatOptionsGet) | **GET** /invoices/vatOptions | List VAT options |


<a id="bulkDeleteInvoices"></a>
# **bulkDeleteInvoices**
> EmptySuccessResponse bulkDeleteInvoices(bulkActionRequestBody)

Bulk delete invoices

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
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | Invoices ids
    try {
      EmptySuccessResponse result = apiInstance.bulkDeleteInvoices(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#bulkDeleteInvoices");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Invoices ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="invoicesGet"></a>
# **invoicesGet**
> InvoicesGet200Response invoicesGet(contactId, projectId, invoiceNumber, offerNumber, isDraft, isOffer, isLocked, isFixedPrice, dateFrom, dateTo, issuedDate, sentAsDraft)

View list of invoices

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
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    UUID contactId = UUID.randomUUID(); // UUID | Used to filter on the `contact_id` of the invoices
    UUID projectId = UUID.randomUUID(); // UUID | Used to filter on the `project_id` of the invoices
    String invoiceNumber = "invoiceNumber_example"; // String | Used to filter on the `invoice_number` of the invoices
    String offerNumber = "offerNumber_example"; // String | 
    Integer isDraft = 0; // Integer | 
    Integer isOffer = 0; // Integer | 
    Integer isLocked = 0; // Integer | 
    Integer isFixedPrice = 0; // Integer | 
    LocalDate dateFrom = LocalDate.now(); // LocalDate | 
    LocalDate dateTo = LocalDate.now(); // LocalDate | 
    LocalDate issuedDate = LocalDate.now(); // LocalDate | 
    Integer sentAsDraft = 56; // Integer | Used to filter invoices which are sent as draft to integration
    try {
      InvoicesGet200Response result = apiInstance.invoicesGet(contactId, projectId, invoiceNumber, offerNumber, isDraft, isOffer, isLocked, isFixedPrice, dateFrom, dateTo, issuedDate, sentAsDraft);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#invoicesGet");
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
| **contactId** | **UUID**| Used to filter on the &#x60;contact_id&#x60; of the invoices | [optional] |
| **projectId** | **UUID**| Used to filter on the &#x60;project_id&#x60; of the invoices | [optional] |
| **invoiceNumber** | **String**| Used to filter on the &#x60;invoice_number&#x60; of the invoices | [optional] |
| **offerNumber** | **String**|  | [optional] |
| **isDraft** | **Integer**|  | [optional] [enum: 0, 1] |
| **isOffer** | **Integer**|  | [optional] [enum: 0, 1] |
| **isLocked** | **Integer**|  | [optional] [enum: 0, 1] |
| **isFixedPrice** | **Integer**|  | [optional] [enum: 0, 1] |
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **issuedDate** | **LocalDate**|  | [optional] |
| **sentAsDraft** | **Integer**| Used to filter invoices which are sent as draft to integration | [optional] |

### Return type

[**InvoicesGet200Response**](InvoicesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoicesInvoiceIdCopyPost"></a>
# **invoicesInvoiceIdCopyPost**
> CreateSuccessResponse invoicesInvoiceIdCopyPost(invoiceId, projectId, contactId)

Create a copy of an invoice

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
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    UUID invoiceId = UUID.randomUUID(); // UUID | 
    UUID projectId = UUID.randomUUID(); // UUID | 
    UUID contactId = UUID.randomUUID(); // UUID | 
    try {
      CreateSuccessResponse result = apiInstance.invoicesInvoiceIdCopyPost(invoiceId, projectId, contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#invoicesInvoiceIdCopyPost");
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
| **invoiceId** | **UUID**|  | |
| **projectId** | **UUID**|  | [optional] |
| **contactId** | **UUID**|  | [optional] |

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |
| **422** | Validation error |  -  |

<a id="invoicesInvoiceIdDelete"></a>
# **invoicesInvoiceIdDelete**
> ClockingRecordsClockingRecordIdPut200Response invoicesInvoiceIdDelete(invoiceId)

Delete invoice

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
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String invoiceId = "invoiceId_example"; // String | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.invoicesInvoiceIdDelete(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#invoicesInvoiceIdDelete");
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
| **invoiceId** | **String**|  | |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoicesInvoiceIdGet"></a>
# **invoicesInvoiceIdGet**
> InvoicesInvoiceIdGet200Response invoicesInvoiceIdGet(invoiceId)

View invoice

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
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String invoiceId = "invoiceId_example"; // String | 
    try {
      InvoicesInvoiceIdGet200Response result = apiInstance.invoicesInvoiceIdGet(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#invoicesInvoiceIdGet");
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
| **invoiceId** | **String**|  | |

### Return type

[**InvoicesInvoiceIdGet200Response**](InvoicesInvoiceIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoicesInvoiceIdLinkProjectPdfPost"></a>
# **invoicesInvoiceIdLinkProjectPdfPost**
> EmptySuccessResponse invoicesInvoiceIdLinkProjectPdfPost(invoiceId)

Creates an invoice file containing the project&#39;s pdf overview

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
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    UUID invoiceId = UUID.randomUUID(); // UUID | 
    try {
      EmptySuccessResponse result = apiInstance.invoicesInvoiceIdLinkProjectPdfPost(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#invoicesInvoiceIdLinkProjectPdfPost");
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
| **invoiceId** | **UUID**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |
| **422** | Validation error |  -  |

<a id="invoicesInvoiceIdPut"></a>
# **invoicesInvoiceIdPut**
> ClockingRecordsClockingRecordIdPut200Response invoicesInvoiceIdPut(invoiceId, invoicesInvoiceIdPutRequest)

Edit invoice

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
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String invoiceId = "invoiceId_example"; // String | 
    InvoicesInvoiceIdPutRequest invoicesInvoiceIdPutRequest = new InvoicesInvoiceIdPutRequest(); // InvoicesInvoiceIdPutRequest | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.invoicesInvoiceIdPut(invoiceId, invoicesInvoiceIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#invoicesInvoiceIdPut");
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
| **invoiceId** | **String**|  | |
| **invoicesInvoiceIdPutRequest** | [**InvoicesInvoiceIdPutRequest**](InvoicesInvoiceIdPutRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoicesInvoiceIdUnlinkProjectPdfPost"></a>
# **invoicesInvoiceIdUnlinkProjectPdfPost**
> EmptySuccessResponse invoicesInvoiceIdUnlinkProjectPdfPost(invoiceId)

Deletes the linked project overview pdf

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
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    UUID invoiceId = UUID.randomUUID(); // UUID | 
    try {
      EmptySuccessResponse result = apiInstance.invoicesInvoiceIdUnlinkProjectPdfPost(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#invoicesInvoiceIdUnlinkProjectPdfPost");
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
| **invoiceId** | **UUID**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |
| **422** | Validation error |  -  |

<a id="invoicesPost"></a>
# **invoicesPost**
> ClockingRecordsPost201Response invoicesPost(invoicesPostRequest)

Add invoice

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
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    InvoicesPostRequest invoicesPostRequest = new InvoicesPostRequest(); // InvoicesPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.invoicesPost(invoicesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#invoicesPost");
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
| **invoicesPostRequest** | [**InvoicesPostRequest**](InvoicesPostRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **422** | Validation error |  -  |

<a id="invoicesVatOptionsGet"></a>
# **invoicesVatOptionsGet**
> IntegrationsProductsSyncGet200Response invoicesVatOptionsGet()

List VAT options

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
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    try {
      IntegrationsProductsSyncGet200Response result = apiInstance.invoicesVatOptionsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#invoicesVatOptionsGet");
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

[**IntegrationsProductsSyncGet200Response**](IntegrationsProductsSyncGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


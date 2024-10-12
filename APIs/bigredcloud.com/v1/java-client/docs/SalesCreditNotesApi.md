# SalesCreditNotesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesCreditNotesDelete**](SalesCreditNotesApi.md#salesCreditNotesDelete) | **DELETE** /v1/salesCreditNotes/{id} | Removes an existing Sales Credit Note. |
| [**salesCreditNotesGet**](SalesCreditNotesApi.md#salesCreditNotesGet) | **GET** /v1/salesCreditNotes | Returns a list of company&#39;s Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field. |
| [**salesCreditNotesPost**](SalesCreditNotesApi.md#salesCreditNotesPost) | **POST** /v1/salesCreditNotes | Creates a new Sales Credit Note. |
| [**salesCreditNotesProcessBatch**](SalesCreditNotesApi.md#salesCreditNotesProcessBatch) | **PUT** /v1/salesCreditNotes/batch | Processes a batch of Sales Credit Notes. |
| [**salesCreditNotesPut**](SalesCreditNotesApi.md#salesCreditNotesPut) | **PUT** /v1/salesCreditNotes/{id} | Updates an existing Sales Credit Note. |
| [**v1SalesCreditNotesIdGet**](SalesCreditNotesApi.md#v1SalesCreditNotesIdGet) | **GET** /v1/salesCreditNotes/{id} | Returns information about a single Sales Credit Note. |


<a id="salesCreditNotesDelete"></a>
# **salesCreditNotesDelete**
> Object salesCreditNotesDelete(id, timestamp)

Removes an existing Sales Credit Note.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesCreditNotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesCreditNotesApi apiInstance = new SalesCreditNotesApi(defaultClient);
    Long id = 56L; // Long | Id of Sales Credit Note to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Sales Credit Note to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.salesCreditNotesDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesCreditNotesApi#salesCreditNotesDelete");
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
| **id** | **Long**| Id of Sales Credit Note to remove. | |
| **timestamp** | **String**| Timestamp of Sales Credit Note to remove. Should be encoded in Base64. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesCreditNotesGet"></a>
# **salesCreditNotesGet**
> PageResultSalesCreditNoteQueryDto salesCreditNotesGet()

Returns a list of company&#39;s Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesCreditNotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesCreditNotesApi apiInstance = new SalesCreditNotesApi(defaultClient);
    try {
      PageResultSalesCreditNoteQueryDto result = apiInstance.salesCreditNotesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesCreditNotesApi#salesCreditNotesGet");
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

[**PageResultSalesCreditNoteQueryDto**](PageResultSalesCreditNoteQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesCreditNotesPost"></a>
# **salesCreditNotesPost**
> Object salesCreditNotesPost(salesInvoiceCreditNoteDto)

Creates a new Sales Credit Note.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesCreditNotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesCreditNotesApi apiInstance = new SalesCreditNotesApi(defaultClient);
    SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto = new SalesInvoiceCreditNoteDto(); // SalesInvoiceCreditNoteDto | Information of Sales Credit Note to create.
    try {
      Object result = apiInstance.salesCreditNotesPost(salesInvoiceCreditNoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesCreditNotesApi#salesCreditNotesPost");
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
| **salesInvoiceCreditNoteDto** | [**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)| Information of Sales Credit Note to create. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesCreditNotesProcessBatch"></a>
# **salesCreditNotesProcessBatch**
> Object salesCreditNotesProcessBatch(batchItemSalesInvoiceCreditNoteDto)

Processes a batch of Sales Credit Notes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesCreditNotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesCreditNotesApi apiInstance = new SalesCreditNotesApi(defaultClient);
    List<BatchItemSalesInvoiceCreditNoteDto> batchItemSalesInvoiceCreditNoteDto = Arrays.asList(); // List<BatchItemSalesInvoiceCreditNoteDto> | Batch of Sales Credit Notes to process.
    try {
      Object result = apiInstance.salesCreditNotesProcessBatch(batchItemSalesInvoiceCreditNoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesCreditNotesApi#salesCreditNotesProcessBatch");
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
| **batchItemSalesInvoiceCreditNoteDto** | [**List&lt;BatchItemSalesInvoiceCreditNoteDto&gt;**](BatchItemSalesInvoiceCreditNoteDto.md)| Batch of Sales Credit Notes to process. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesCreditNotesPut"></a>
# **salesCreditNotesPut**
> Object salesCreditNotesPut(id, salesInvoiceCreditNoteDto)

Updates an existing Sales Credit Note.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesCreditNotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesCreditNotesApi apiInstance = new SalesCreditNotesApi(defaultClient);
    Long id = 56L; // Long | Id of Sales Credit Note to update.
    SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto = new SalesInvoiceCreditNoteDto(); // SalesInvoiceCreditNoteDto | Information of Sales Credit Note to update.
    try {
      Object result = apiInstance.salesCreditNotesPut(id, salesInvoiceCreditNoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesCreditNotesApi#salesCreditNotesPut");
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
| **id** | **Long**| Id of Sales Credit Note to update. | |
| **salesInvoiceCreditNoteDto** | [**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)| Information of Sales Credit Note to update. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v1SalesCreditNotesIdGet"></a>
# **v1SalesCreditNotesIdGet**
> SalesInvoiceCreditNoteDto v1SalesCreditNotesIdGet(id)

Returns information about a single Sales Credit Note.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesCreditNotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesCreditNotesApi apiInstance = new SalesCreditNotesApi(defaultClient);
    Long id = 56L; // Long | Id of Sales Credit Note to return.
    try {
      SalesInvoiceCreditNoteDto result = apiInstance.v1SalesCreditNotesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesCreditNotesApi#v1SalesCreditNotesIdGet");
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
| **id** | **Long**| Id of Sales Credit Note to return. | |

### Return type

[**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


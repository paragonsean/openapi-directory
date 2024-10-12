# SalesInvoicesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesInvoicesDelete**](SalesInvoicesApi.md#salesInvoicesDelete) | **DELETE** /v1/salesInvoices/{id} | Removes an existing Sales Invoice. |
| [**salesInvoicesGet**](SalesInvoicesApi.md#salesInvoicesGet) | **GET** /v1/salesInvoices | Returns a list of company&#39;s Sales Invoices. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field. |
| [**salesInvoicesPost**](SalesInvoicesApi.md#salesInvoicesPost) | **POST** /v1/salesInvoices | Creates a new Sales Invoice. |
| [**salesInvoicesPostCreateSaleInvoiceWithGeneratingReference**](SalesInvoicesApi.md#salesInvoicesPostCreateSaleInvoiceWithGeneratingReference) | **POST** /v1/salesInvoices/createSaleInvoiceWithGeneratingReference | Creates a new Sale Invoice with auto generating reference. |
| [**salesInvoicesProcessBatch**](SalesInvoicesApi.md#salesInvoicesProcessBatch) | **PUT** /v1/salesInvoices/batch | Processes a batch of Sales Invoices. |
| [**salesInvoicesPut**](SalesInvoicesApi.md#salesInvoicesPut) | **PUT** /v1/salesInvoices/{id} | Updates an existing Sales Invoice. |
| [**v1SalesInvoicesIdGet**](SalesInvoicesApi.md#v1SalesInvoicesIdGet) | **GET** /v1/salesInvoices/{id} | Returns information about a single Sales Invoice. |


<a id="salesInvoicesDelete"></a>
# **salesInvoicesDelete**
> Object salesInvoicesDelete(id, timestamp)

Removes an existing Sales Invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesInvoicesApi apiInstance = new SalesInvoicesApi(defaultClient);
    Long id = 56L; // Long | Id of Sales Invoice to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Sales Invoice to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.salesInvoicesDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesInvoicesApi#salesInvoicesDelete");
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
| **id** | **Long**| Id of Sales Invoice to remove. | |
| **timestamp** | **String**| Timestamp of Sales Invoice to remove. Should be encoded in Base64. | |

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

<a id="salesInvoicesGet"></a>
# **salesInvoicesGet**
> PageResultSalesInvoiceQueryDto salesInvoicesGet()

Returns a list of company&#39;s Sales Invoices. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesInvoicesApi apiInstance = new SalesInvoicesApi(defaultClient);
    try {
      PageResultSalesInvoiceQueryDto result = apiInstance.salesInvoicesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesInvoicesApi#salesInvoicesGet");
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

[**PageResultSalesInvoiceQueryDto**](PageResultSalesInvoiceQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesInvoicesPost"></a>
# **salesInvoicesPost**
> Object salesInvoicesPost(salesInvoiceCreditNoteDto)

Creates a new Sales Invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesInvoicesApi apiInstance = new SalesInvoicesApi(defaultClient);
    SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto = new SalesInvoiceCreditNoteDto(); // SalesInvoiceCreditNoteDto | Information of Sales Invoice to create.
    try {
      Object result = apiInstance.salesInvoicesPost(salesInvoiceCreditNoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesInvoicesApi#salesInvoicesPost");
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
| **salesInvoiceCreditNoteDto** | [**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)| Information of Sales Invoice to create. | |

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

<a id="salesInvoicesPostCreateSaleInvoiceWithGeneratingReference"></a>
# **salesInvoicesPostCreateSaleInvoiceWithGeneratingReference**
> Object salesInvoicesPostCreateSaleInvoiceWithGeneratingReference(salesInvoiceCreditNoteDto)

Creates a new Sale Invoice with auto generating reference.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesInvoicesApi apiInstance = new SalesInvoicesApi(defaultClient);
    SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto = new SalesInvoiceCreditNoteDto(); // SalesInvoiceCreditNoteDto | Information of Sale Invoice to create.
    try {
      Object result = apiInstance.salesInvoicesPostCreateSaleInvoiceWithGeneratingReference(salesInvoiceCreditNoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesInvoicesApi#salesInvoicesPostCreateSaleInvoiceWithGeneratingReference");
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
| **salesInvoiceCreditNoteDto** | [**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)| Information of Sale Invoice to create. | |

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

<a id="salesInvoicesProcessBatch"></a>
# **salesInvoicesProcessBatch**
> Object salesInvoicesProcessBatch(batchItemSalesInvoiceCreditNoteDto)

Processes a batch of Sales Invoices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesInvoicesApi apiInstance = new SalesInvoicesApi(defaultClient);
    List<BatchItemSalesInvoiceCreditNoteDto> batchItemSalesInvoiceCreditNoteDto = Arrays.asList(); // List<BatchItemSalesInvoiceCreditNoteDto> | Batch of Sales Invoices to process.
    try {
      Object result = apiInstance.salesInvoicesProcessBatch(batchItemSalesInvoiceCreditNoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesInvoicesApi#salesInvoicesProcessBatch");
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
| **batchItemSalesInvoiceCreditNoteDto** | [**List&lt;BatchItemSalesInvoiceCreditNoteDto&gt;**](BatchItemSalesInvoiceCreditNoteDto.md)| Batch of Sales Invoices to process. | |

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

<a id="salesInvoicesPut"></a>
# **salesInvoicesPut**
> Object salesInvoicesPut(id, salesInvoiceCreditNoteDto)

Updates an existing Sales Invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesInvoicesApi apiInstance = new SalesInvoicesApi(defaultClient);
    Long id = 56L; // Long | Id of Sales Invoice to update.
    SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto = new SalesInvoiceCreditNoteDto(); // SalesInvoiceCreditNoteDto | Information of Sales Invoice to update.
    try {
      Object result = apiInstance.salesInvoicesPut(id, salesInvoiceCreditNoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesInvoicesApi#salesInvoicesPut");
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
| **id** | **Long**| Id of Sales Invoice to update. | |
| **salesInvoiceCreditNoteDto** | [**SalesInvoiceCreditNoteDto**](SalesInvoiceCreditNoteDto.md)| Information of Sales Invoice to update. | |

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

<a id="v1SalesInvoicesIdGet"></a>
# **v1SalesInvoicesIdGet**
> SalesInvoiceCreditNoteDto v1SalesInvoicesIdGet(id)

Returns information about a single Sales Invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesInvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesInvoicesApi apiInstance = new SalesInvoicesApi(defaultClient);
    Long id = 56L; // Long | Id of Sales Invoice to return.
    try {
      SalesInvoiceCreditNoteDto result = apiInstance.v1SalesInvoicesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesInvoicesApi#v1SalesInvoicesIdGet");
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
| **id** | **Long**| Id of Sales Invoice to return. | |

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


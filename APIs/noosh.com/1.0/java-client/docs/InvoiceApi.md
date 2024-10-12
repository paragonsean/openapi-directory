# InvoiceApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInvoice**](InvoiceApi.md#getInvoice) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/{invoice_id} | List a specific invoice of project Level |
| [**getInvoiceFiles**](InvoiceApi.md#getInvoiceFiles) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/{invoice_id}/files | List files of invoice Level |
| [**getInvoices**](InvoiceApi.md#getInvoices) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/orders/{order_id} | List invoices by a specific order |


<a id="getInvoice"></a>
# **getInvoice**
> InvoiceExpandVO getInvoice(workgroupId, projectId, invoiceId)

List a specific invoice of project Level

List a specific invoice of project Level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String invoiceId = "invoiceId_example"; // String | 
    try {
      InvoiceExpandVO result = apiInstance.getInvoice(workgroupId, projectId, invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#getInvoice");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **invoiceId** | **String**|  | |

### Return type

[**InvoiceExpandVO**](InvoiceExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getInvoiceFiles"></a>
# **getInvoiceFiles**
> FileListResponseVO getInvoiceFiles(workgroupId, projectId, invoiceId)

List files of invoice Level

List files of invoice Level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String invoiceId = "invoiceId_example"; // String | 
    try {
      FileListResponseVO result = apiInstance.getInvoiceFiles(workgroupId, projectId, invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#getInvoiceFiles");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **invoiceId** | **String**|  | |

### Return type

[**FileListResponseVO**](FileListResponseVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getInvoices"></a>
# **getInvoices**
> InvoiceDetailListExpandVO getInvoices(workgroupId, projectId, orderId)

List invoices by a specific order

List invoices by a specific order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String orderId = "orderId_example"; // String | 
    try {
      InvoiceDetailListExpandVO result = apiInstance.getInvoices(workgroupId, projectId, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#getInvoices");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **orderId** | **String**|  | |

### Return type

[**InvoiceDetailListExpandVO**](InvoiceDetailListExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |


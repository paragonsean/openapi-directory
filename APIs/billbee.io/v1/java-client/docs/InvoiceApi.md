# InvoiceApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**orderApiCreateInvoice_0**](InvoiceApi.md#orderApiCreateInvoice_0) | **POST** /api/v1/orders/CreateInvoice/{id} | Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes. |
| [**orderApiGetInvoiceList_0**](InvoiceApi.md#orderApiGetInvoiceList_0) | **GET** /api/v1/orders/invoices | Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate |


<a id="orderApiCreateInvoice_0"></a>
# **orderApiCreateInvoice_0**
> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice orderApiCreateInvoice_0(id, includeInvoicePdf, templateId, sendToCloudId)

Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

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
    defaultClient.setBasePath("https://app.billbee.io");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    Long id = 56L; // Long | The internal billbee id of the order
    Boolean includeInvoicePdf = true; // Boolean | If true, the PDF is included in the response as base64 encoded string
    Long templateId = 56L; // Long | You can pass the id of an invoice template to overwrite the assigned template for invoice creation
    Long sendToCloudId = 56L; // Long | You can pass the id of a connected cloud printer/storage to send the invoice to it
    try {
      RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice result = apiInstance.orderApiCreateInvoice_0(id, includeInvoicePdf, templateId, sendToCloudId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#orderApiCreateInvoice_0");
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
| **id** | **Long**| The internal billbee id of the order | |
| **includeInvoicePdf** | **Boolean**| If true, the PDF is included in the response as base64 encoded string | [optional] |
| **templateId** | **Long**| You can pass the id of an invoice template to overwrite the assigned template for invoice creation | [optional] |
| **sendToCloudId** | **Long**| You can pass the id of a connected cloud printer/storage to send the invoice to it | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice**](RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiGetInvoiceList_0"></a>
# **orderApiGetInvoiceList_0**
> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel orderApiGetInvoiceList_0(minInvoiceDate, maxInvoiceDate, page, pageSize, shopId, orderStateId, tag, minPayDate, maxPayDate, includePositions, excludeTags)

Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate

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
    defaultClient.setBasePath("https://app.billbee.io");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    OffsetDateTime minInvoiceDate = OffsetDateTime.now(); // OffsetDateTime | Specifies the oldest invoice date to include
    OffsetDateTime maxInvoiceDate = OffsetDateTime.now(); // OffsetDateTime | Specifies the newest invoice date to include
    Integer page = 56; // Integer | Specifies the page to request
    Integer pageSize = 56; // Integer | Specifies the pagesize. Defaults to 50, max value is 250
    List<Long> shopId = Arrays.asList(); // List<Long> | Specifies a list of shop ids for which invoices should be included
    List<Integer> orderStateId = Arrays.asList(); // List<Integer> | Specifies a list of state ids to include in the response
    List<String> tag = Arrays.asList(); // List<String> | 
    OffsetDateTime minPayDate = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime maxPayDate = OffsetDateTime.now(); // OffsetDateTime | 
    Boolean includePositions = true; // Boolean | 
    Boolean excludeTags = true; // Boolean | If true the list of tags passed to the call are used to filter orders to not include these tags
    try {
      RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel result = apiInstance.orderApiGetInvoiceList_0(minInvoiceDate, maxInvoiceDate, page, pageSize, shopId, orderStateId, tag, minPayDate, maxPayDate, includePositions, excludeTags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#orderApiGetInvoiceList_0");
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
| **minInvoiceDate** | **OffsetDateTime**| Specifies the oldest invoice date to include | [optional] |
| **maxInvoiceDate** | **OffsetDateTime**| Specifies the newest invoice date to include | [optional] |
| **page** | **Integer**| Specifies the page to request | [optional] |
| **pageSize** | **Integer**| Specifies the pagesize. Defaults to 50, max value is 250 | [optional] |
| **shopId** | [**List&lt;Long&gt;**](Long.md)| Specifies a list of shop ids for which invoices should be included | [optional] |
| **orderStateId** | [**List&lt;Integer&gt;**](Integer.md)| Specifies a list of state ids to include in the response | [optional] |
| **tag** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **minPayDate** | **OffsetDateTime**|  | [optional] |
| **maxPayDate** | **OffsetDateTime**|  | [optional] |
| **includePositions** | **Boolean**|  | [optional] |
| **excludeTags** | **Boolean**| If true the list of tags passed to the call are used to filter orders to not include these tags | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


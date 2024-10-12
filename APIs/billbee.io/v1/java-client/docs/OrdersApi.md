# OrdersApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**layoutApiGetList**](OrdersApi.md#layoutApiGetList) | **GET** /api/v1/layouts |  |
| [**orderApiAddShipment**](OrdersApi.md#orderApiAddShipment) | **POST** /api/v1/orders/{id}/shipment | Add a shipment to a given order |
| [**orderApiCreateDeliveryNote**](OrdersApi.md#orderApiCreateDeliveryNote) | **POST** /api/v1/orders/CreateDeliveryNote/{id} | Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes. |
| [**orderApiCreateInvoice**](OrdersApi.md#orderApiCreateInvoice) | **POST** /api/v1/orders/CreateInvoice/{id} | Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes. |
| [**orderApiFind**](OrdersApi.md#orderApiFind) | **GET** /api/v1/orders/find/{id}/{partner} | Find a single order by its external id (order number) |
| [**orderApiGet**](OrdersApi.md#orderApiGet) | **GET** /api/v1/orders/{id} | Get a single order by its internal billbee id. This request is throttled to 6 calls per order in one minute |
| [**orderApiGetByExtRef**](OrdersApi.md#orderApiGetByExtRef) | **GET** /api/v1/orders/findbyextref/{extRef} | Get a single order by its external order number |
| [**orderApiGetInvoiceList**](OrdersApi.md#orderApiGetInvoiceList) | **GET** /api/v1/orders/invoices | Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate |
| [**orderApiGetList**](OrdersApi.md#orderApiGetList) | **GET** /api/v1/orders | Get a list of all orders optionally filtered by date |
| [**orderApiGetPatchableFields**](OrdersApi.md#orderApiGetPatchableFields) | **GET** /api/v1/orders/PatchableFields | Returns a list of fields which can be updated with the orders/{id} patch call |
| [**orderApiParsePlaceholders**](OrdersApi.md#orderApiParsePlaceholders) | **POST** /api/v1/orders/{id}/parse-placeholders | Parses a text and replaces all placeholders |
| [**orderApiPatchOrder**](OrdersApi.md#orderApiPatchOrder) | **PATCH** /api/v1/orders/{id} | Updates one or more fields of an order |
| [**orderApiPostNewOrder**](OrdersApi.md#orderApiPostNewOrder) | **POST** /api/v1/orders | Creates a new order in the Billbee account |
| [**orderApiSendMessage**](OrdersApi.md#orderApiSendMessage) | **POST** /api/v1/orders/{id}/send-message | Sends a message to the buyer |
| [**orderApiTagsCreate**](OrdersApi.md#orderApiTagsCreate) | **POST** /api/v1/orders/{id}/tags | Attach one or more tags to an order |
| [**orderApiTagsUpdate**](OrdersApi.md#orderApiTagsUpdate) | **PUT** /api/v1/orders/{id}/tags | Sets the tags attached to an order |
| [**orderApiTriggerEvent**](OrdersApi.md#orderApiTriggerEvent) | **POST** /api/v1/orders/{id}/trigger-event | Triggers a rule event |
| [**orderApiUpdateState**](OrdersApi.md#orderApiUpdateState) | **PUT** /api/v1/orders/{id}/orderstate | Changes the main state of a single order |
| [**searchSearch_1**](OrdersApi.md#searchSearch_1) | **POST** /api/v1/search | Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax |


<a id="layoutApiGetList"></a>
# **layoutApiGetList**
> RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate layoutApiGetList()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    try {
      RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate result = apiInstance.layoutApiGetList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#layoutApiGetList");
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

[**RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate**](RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiAddShipment"></a>
# **orderApiAddShipment**
> Object orderApiAddShipment(id, rechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel)

Add a shipment to a given order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | The internal billbee id of the order
    RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel rechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel = new RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel(); // RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel | The shipment data to create the shipment
    try {
      Object result = apiInstance.orderApiAddShipment(id, rechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiAddShipment");
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
| **rechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel** | [**RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel**](RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel.md)| The shipment data to create the shipment | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiCreateDeliveryNote"></a>
# **orderApiCreateDeliveryNote**
> Object orderApiCreateDeliveryNote(id, includePdf, sendToCloudId)

Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | The internal billbee id of the order
    Boolean includePdf = true; // Boolean | If true, the PDF is included in the response as base64 encoded string
    Long sendToCloudId = 56L; // Long | Optionally specify the id of a billbee connected cloud device to send the pdf to
    try {
      Object result = apiInstance.orderApiCreateDeliveryNote(id, includePdf, sendToCloudId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiCreateDeliveryNote");
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
| **includePdf** | **Boolean**| If true, the PDF is included in the response as base64 encoded string | [optional] |
| **sendToCloudId** | **Long**| Optionally specify the id of a billbee connected cloud device to send the pdf to | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiCreateInvoice"></a>
# **orderApiCreateInvoice**
> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice orderApiCreateInvoice(id, includeInvoicePdf, templateId, sendToCloudId)

Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | The internal billbee id of the order
    Boolean includeInvoicePdf = true; // Boolean | If true, the PDF is included in the response as base64 encoded string
    Long templateId = 56L; // Long | You can pass the id of an invoice template to overwrite the assigned template for invoice creation
    Long sendToCloudId = 56L; // Long | You can pass the id of a connected cloud printer/storage to send the invoice to it
    try {
      RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice result = apiInstance.orderApiCreateInvoice(id, includeInvoicePdf, templateId, sendToCloudId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiCreateInvoice");
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

<a id="orderApiFind"></a>
# **orderApiFind**
> Object orderApiFind(id, partner)

Find a single order by its external id (order number)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The order id from the external system
    String partner = "partner_example"; // String | Optional the name of the shop/marketplace the order was imported from
    try {
      Object result = apiInstance.orderApiFind(id, partner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiFind");
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
| **id** | **String**| The order id from the external system | |
| **partner** | **String**| Optional the name of the shop/marketplace the order was imported from | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiGet"></a>
# **orderApiGet**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder orderApiGet(id, articleTitleSource)

Get a single order by its internal billbee id. This request is throttled to 6 calls per order in one minute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | The internal billbee id of the order
    Integer articleTitleSource = 0; // Integer | The source field for the article title. 0 = Order Position (default), 1 = Article Title, 2 = Article Invoice Text
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder result = apiInstance.orderApiGet(id, articleTitleSource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiGet");
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
| **articleTitleSource** | **Integer**| The source field for the article title. 0 &#x3D; Order Position (default), 1 &#x3D; Article Title, 2 &#x3D; Article Invoice Text | [optional] [enum: 0, 1, 2, 3] |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiGetByExtRef"></a>
# **orderApiGetByExtRef**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder orderApiGetByExtRef(extRef)

Get a single order by its external order number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String extRef = "extRef_example"; // String | The extern order number of the order
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder result = apiInstance.orderApiGetByExtRef(extRef);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiGetByExtRef");
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
| **extRef** | **String**| The extern order number of the order | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiGetInvoiceList"></a>
# **orderApiGetInvoiceList**
> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel orderApiGetInvoiceList(minInvoiceDate, maxInvoiceDate, page, pageSize, shopId, orderStateId, tag, minPayDate, maxPayDate, includePositions, excludeTags)

Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
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
      RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel result = apiInstance.orderApiGetInvoiceList(minInvoiceDate, maxInvoiceDate, page, pageSize, shopId, orderStateId, tag, minPayDate, maxPayDate, includePositions, excludeTags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiGetInvoiceList");
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

<a id="orderApiGetList"></a>
# **orderApiGetList**
> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder orderApiGetList(minOrderDate, maxOrderDate, page, pageSize, shopId, orderStateId, tag, minimumBillBeeOrderId, modifiedAtMin, modifiedAtMax, articleTitleSource, excludeTags)

Get a list of all orders optionally filtered by date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    OffsetDateTime minOrderDate = OffsetDateTime.now(); // OffsetDateTime | Specifies the oldest order date to include in the response
    OffsetDateTime maxOrderDate = OffsetDateTime.now(); // OffsetDateTime | Specifies the newest order date to include in the response
    Integer page = 56; // Integer | Specifies the page to request
    Integer pageSize = 56; // Integer | Specifies the pagesize. Defaults to 50, max value is 250
    List<Long> shopId = Arrays.asList(); // List<Long> | Specifies a list of shop ids for which invoices should be included
    List<Integer> orderStateId = Arrays.asList(); // List<Integer> | Specifies a list of state ids to include in the response
    List<String> tag = Arrays.asList(); // List<String> | Specifies a list of tags the order must have attached to be included in the response
    Long minimumBillBeeOrderId = 56L; // Long | If given, all delivered orders have an Id greater than or equal to the given minimumOrderId
    OffsetDateTime modifiedAtMin = OffsetDateTime.now(); // OffsetDateTime | If given, the last modification has to be newer than the given date
    OffsetDateTime modifiedAtMax = OffsetDateTime.now(); // OffsetDateTime | If given, the last modification has to be older or equal than the given date.
    Integer articleTitleSource = 0; // Integer | The source field for the article title. 0 = Order Position (default), 1 = Article Title, 2 = Article Invoice Text
    Boolean excludeTags = true; // Boolean | If true the list of tags passed to the call are used to filter orders to not include these tags
    try {
      RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder result = apiInstance.orderApiGetList(minOrderDate, maxOrderDate, page, pageSize, shopId, orderStateId, tag, minimumBillBeeOrderId, modifiedAtMin, modifiedAtMax, articleTitleSource, excludeTags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiGetList");
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
| **minOrderDate** | **OffsetDateTime**| Specifies the oldest order date to include in the response | [optional] |
| **maxOrderDate** | **OffsetDateTime**| Specifies the newest order date to include in the response | [optional] |
| **page** | **Integer**| Specifies the page to request | [optional] |
| **pageSize** | **Integer**| Specifies the pagesize. Defaults to 50, max value is 250 | [optional] |
| **shopId** | [**List&lt;Long&gt;**](Long.md)| Specifies a list of shop ids for which invoices should be included | [optional] |
| **orderStateId** | [**List&lt;Integer&gt;**](Integer.md)| Specifies a list of state ids to include in the response | [optional] |
| **tag** | [**List&lt;String&gt;**](String.md)| Specifies a list of tags the order must have attached to be included in the response | [optional] |
| **minimumBillBeeOrderId** | **Long**| If given, all delivered orders have an Id greater than or equal to the given minimumOrderId | [optional] |
| **modifiedAtMin** | **OffsetDateTime**| If given, the last modification has to be newer than the given date | [optional] |
| **modifiedAtMax** | **OffsetDateTime**| If given, the last modification has to be older or equal than the given date. | [optional] |
| **articleTitleSource** | **Integer**| The source field for the article title. 0 &#x3D; Order Position (default), 1 &#x3D; Article Title, 2 &#x3D; Article Invoice Text | [optional] [enum: 0, 1, 2, 3] |
| **excludeTags** | **Boolean**| If true the list of tags passed to the call are used to filter orders to not include these tags | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiGetPatchableFields"></a>
# **orderApiGetPatchableFields**
> Object orderApiGetPatchableFields()

Returns a list of fields which can be updated with the orders/{id} patch call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    try {
      Object result = apiInstance.orderApiGetPatchableFields();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiGetPatchableFields");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiParsePlaceholders"></a>
# **orderApiParsePlaceholders**
> Object orderApiParsePlaceholders(id, rechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer)

Parses a text and replaces all placeholders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | The id of the order
    RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer rechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer = new RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer(); // RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer | 
    try {
      Object result = apiInstance.orderApiParsePlaceholders(id, rechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiParsePlaceholders");
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
| **id** | **Long**| The id of the order | |
| **rechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer** | [**RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer**](RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiPatchOrder"></a>
# **orderApiPatchOrder**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder orderApiPatchOrder(id, body)

Updates one or more fields of an order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | 
    Object body = null; // Object | 
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder result = apiInstance.orderApiPatchOrder(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiPatchOrder");
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
| **id** | **Long**|  | |
| **body** | **Object**|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiPostNewOrder"></a>
# **orderApiPostNewOrder**
> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder orderApiPostNewOrder(billbeeInterfacesBillbeeAPIModelOrder, shopId)

Creates a new order in the Billbee account

To create an order POST an JSON object to the orders endpoint with the shown properties.  Not all properties are required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    BillbeeInterfacesBillbeeAPIModelOrder billbeeInterfacesBillbeeAPIModelOrder = new BillbeeInterfacesBillbeeAPIModelOrder(); // BillbeeInterfacesBillbeeAPIModelOrder | 
    Long shopId = 56L; // Long | Deprecated, if orderData.ApiAccountId is set, it will be used instead of 'shopId'
    try {
      RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder result = apiInstance.orderApiPostNewOrder(billbeeInterfacesBillbeeAPIModelOrder, shopId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiPostNewOrder");
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
| **billbeeInterfacesBillbeeAPIModelOrder** | [**BillbeeInterfacesBillbeeAPIModelOrder**](BillbeeInterfacesBillbeeAPIModelOrder.md)|  | |
| **shopId** | **Long**| Deprecated, if orderData.ApiAccountId is set, it will be used instead of &#39;shopId&#39; | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The order was created successfully |  -  |
| **400** | Invalid data was received in the request |  -  |
| **500** | An internal exception occured. Order was not created |  -  |

<a id="orderApiSendMessage"></a>
# **orderApiSendMessage**
> Object orderApiSendMessage(id, rechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel)

Sends a message to the buyer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | The id of the order
    RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel rechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel = new RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel(); // RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel | The message model
    try {
      Object result = apiInstance.orderApiSendMessage(id, rechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiSendMessage");
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
| **id** | **Long**| The id of the order | |
| **rechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel** | [**RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel**](RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel.md)| The message model | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiTagsCreate"></a>
# **orderApiTagsCreate**
> Object orderApiTagsCreate(id, rechnungsdruckWebAppControllersApiOrderTagCreate)

Attach one or more tags to an order

When a tag is already attached, it is ignored. Tags are not case sensitive. All given tags are added to the existing tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | The internal id of the order
    RechnungsdruckWebAppControllersApiOrderTagCreate rechnungsdruckWebAppControllersApiOrderTagCreate = new RechnungsdruckWebAppControllersApiOrderTagCreate(); // RechnungsdruckWebAppControllersApiOrderTagCreate | Tags to attach
    try {
      Object result = apiInstance.orderApiTagsCreate(id, rechnungsdruckWebAppControllersApiOrderTagCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiTagsCreate");
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
| **id** | **Long**| The internal id of the order | |
| **rechnungsdruckWebAppControllersApiOrderTagCreate** | [**RechnungsdruckWebAppControllersApiOrderTagCreate**](RechnungsdruckWebAppControllersApiOrderTagCreate.md)| Tags to attach | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiTagsUpdate"></a>
# **orderApiTagsUpdate**
> Object orderApiTagsUpdate(id, rechnungsdruckWebAppControllersApiOrderTagCreate)

Sets the tags attached to an order

All existing tags will be replaced by the given list of new tags. To just add tags, use POST method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | The internal id of the order
    RechnungsdruckWebAppControllersApiOrderTagCreate rechnungsdruckWebAppControllersApiOrderTagCreate = new RechnungsdruckWebAppControllersApiOrderTagCreate(); // RechnungsdruckWebAppControllersApiOrderTagCreate | Tags to attach
    try {
      Object result = apiInstance.orderApiTagsUpdate(id, rechnungsdruckWebAppControllersApiOrderTagCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiTagsUpdate");
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
| **id** | **Long**| The internal id of the order | |
| **rechnungsdruckWebAppControllersApiOrderTagCreate** | [**RechnungsdruckWebAppControllersApiOrderTagCreate**](RechnungsdruckWebAppControllersApiOrderTagCreate.md)| Tags to attach | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiTriggerEvent"></a>
# **orderApiTriggerEvent**
> Object orderApiTriggerEvent(id, rechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer)

Triggers a rule event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | The id of the order
    RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer rechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer = new RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer(); // RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer | 
    try {
      Object result = apiInstance.orderApiTriggerEvent(id, rechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiTriggerEvent");
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
| **id** | **Long**| The id of the order | |
| **rechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer** | [**RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer**](RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiUpdateState"></a>
# **orderApiUpdateState**
> Object orderApiUpdateState(id, rechnungsdruckWebAppControllersApiOrderStateUpdate)

Changes the main state of a single order

### REMARKS ###  Use this call to change the state of an order to i.e. paid or sent.    The state is transfered to the external shop/marketplace if configured.  This is the list of known states:  - 1: ordered  - 2: confirmed  - 3: paid  - 4: shipped  - 5: reclamation  - 6: deleted  - 7: closed  - 8: canceled  - 9: archived  - 10: not used  - 11: demand note 1  - 12: demand note 2  - 13: packed  - 14: offered  - 15: payment reminder  - 16: fulfilling

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | The internal id of the order
    RechnungsdruckWebAppControllersApiOrderStateUpdate rechnungsdruckWebAppControllersApiOrderStateUpdate = new RechnungsdruckWebAppControllersApiOrderStateUpdate(); // RechnungsdruckWebAppControllersApiOrderStateUpdate | The data used to change the state
    try {
      Object result = apiInstance.orderApiUpdateState(id, rechnungsdruckWebAppControllersApiOrderStateUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderApiUpdateState");
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
| **id** | **Long**| The internal id of the order | |
| **rechnungsdruckWebAppControllersApiOrderStateUpdate** | [**RechnungsdruckWebAppControllersApiOrderStateUpdate**](RechnungsdruckWebAppControllersApiOrderStateUpdate.md)| The data used to change the state | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="searchSearch_1"></a>
# **searchSearch_1**
> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel searchSearch_1(rechnungsdruckWebAppControllersApiSearchControllerSearchModel)

Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    RechnungsdruckWebAppControllersApiSearchControllerSearchModel rechnungsdruckWebAppControllersApiSearchControllerSearchModel = new RechnungsdruckWebAppControllersApiSearchControllerSearchModel(); // RechnungsdruckWebAppControllersApiSearchControllerSearchModel | 
    try {
      RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel result = apiInstance.searchSearch_1(rechnungsdruckWebAppControllersApiSearchControllerSearchModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#searchSearch_1");
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
| **rechnungsdruckWebAppControllersApiSearchControllerSearchModel** | [**RechnungsdruckWebAppControllersApiSearchControllerSearchModel**](RechnungsdruckWebAppControllersApiSearchControllerSearchModel.md)|  | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel**](RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


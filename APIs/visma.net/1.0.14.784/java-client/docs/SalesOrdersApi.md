# SalesOrdersApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrdersAddLinesTypeorderIdlines**](SalesOrdersApi.md#salesOrdersAddLinesTypeorderIdlines) | **POST** /api/v3/SalesOrders/{type}/{orderId}/lines | Adds new lines to a existing sales order in the system |
| [**salesOrdersCreateNewItem**](SalesOrdersApi.md#salesOrdersCreateNewItem) | **POST** /api/v3/SalesOrders | Adds a new sales order to the system |
| [**salesOrdersDeleteLinesTypeorderIdlines**](SalesOrdersApi.md#salesOrdersDeleteLinesTypeorderIdlines) | **DELETE** /api/v3/SalesOrders/{type}/{orderId}/lines | Delete lines from an existing sales order |
| [**salesOrdersDeleteTypeorderId**](SalesOrdersApi.md#salesOrdersDeleteTypeorderId) | **DELETE** /api/v3/SalesOrders/{type}/{orderId} | Delete an existing sales order |
| [**salesOrdersGetItemAsyncTypeorderId**](SalesOrdersApi.md#salesOrdersGetItemAsyncTypeorderId) | **GET** /api/v3/SalesOrders/{type}/{orderId} | Gets information about a single sales order |
| [**salesOrdersGetItemCommissionsTypeorderIdcommissions**](SalesOrdersApi.md#salesOrdersGetItemCommissionsTypeorderIdcommissions) | **GET** /api/v3/SalesOrders/{type}/{orderId}/commissions | Gets commission information for a single sales order |
| [**salesOrdersGetItemDiscountsTypeorderIddiscounts**](SalesOrdersApi.md#salesOrdersGetItemDiscountsTypeorderIddiscounts) | **GET** /api/v3/SalesOrders/{type}/{orderId}/discounts | Gets discount details information for a single sales order |
| [**salesOrdersGetItemLineTypeorderIdlineslineId**](SalesOrdersApi.md#salesOrdersGetItemLineTypeorderIdlineslineId) | **GET** /api/v3/SalesOrders/{type}/{orderId}/lines/{lineId} | Gets a specific sales order line for a single sales order |
| [**salesOrdersGetItemLinesTypeorderIdlines**](SalesOrdersApi.md#salesOrdersGetItemLinesTypeorderIdlines) | **GET** /api/v3/SalesOrders/{type}/{orderId}/lines | Gets sales order lines for a single sales order |
| [**salesOrdersGetItemRotRutTypeorderIdrotrut**](SalesOrdersApi.md#salesOrdersGetItemRotRutTypeorderIdrotrut) | **GET** /api/v3/SalesOrders/{type}/{orderId}/rotrut | Gets ROT/RUT information for a single sales order |
| [**salesOrdersGetItemTaxTypeorderIdtax**](SalesOrdersApi.md#salesOrdersGetItemTaxTypeorderIdtax) | **GET** /api/v3/SalesOrders/{type}/{orderId}/tax | Gets tax information for a single sales order |
| [**salesOrdersGetList**](SalesOrdersApi.md#salesOrdersGetList) | **GET** /api/v3/SalesOrders | Gets a paged list with sales orders of any type |
| [**salesOrdersGetListType**](SalesOrdersApi.md#salesOrdersGetListType) | **GET** /api/v3/SalesOrders/{type} | Gets a paged list with sales orders of a specific type |
| [**salesOrdersGetSalesOrderShipmentTypeorderIdshipment**](SalesOrdersApi.md#salesOrdersGetSalesOrderShipmentTypeorderIdshipment) | **GET** /api/v3/SalesOrders/{type}/{orderId}/shipment | Gets shipment information for a single sales order |
| [**salesOrdersPatchLinesTypeorderIdlines**](SalesOrdersApi.md#salesOrdersPatchLinesTypeorderIdlines) | **PATCH** /api/v3/SalesOrders/{type}/{orderId}/lines | Make modifications to an existing sales order lines |
| [**salesOrdersPatchTypeorderId**](SalesOrdersApi.md#salesOrdersPatchTypeorderId) | **PATCH** /api/v3/SalesOrders/{type}/{orderId} | Make modifications to an existing sales order |


<a id="salesOrdersAddLinesTypeorderIdlines"></a>
# **salesOrdersAddLinesTypeorderIdlines**
> salesOrdersAddLinesTypeorderIdlines(type, orderId, addSalesOrderLinesCommand)

Adds new lines to a existing sales order in the system

If-Match header represents a version of Sales Order to be modified and must be included in request.  Value of current version is included in GET /salesorders/{type}/{orderId} and modification endpoints on that resource as ETag header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | 
    String orderId = "orderId_example"; // String | 
    AddSalesOrderLinesCommand addSalesOrderLinesCommand = new AddSalesOrderLinesCommand(); // AddSalesOrderLinesCommand | Information about the lines to create
    try {
      apiInstance.salesOrdersAddLinesTypeorderIdlines(type, orderId, addSalesOrderLinesCommand);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersAddLinesTypeorderIdlines");
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
| **type** | **String**|  | |
| **orderId** | **String**|  | |
| **addSalesOrderLinesCommand** | [**AddSalesOrderLinesCommand**](AddSalesOrderLinesCommand.md)| Information about the lines to create | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The order lines where created successfully, and the Location request header contains the address to call to GET the new sales order |  -  |
| **400** | If any of values in command is not present or active, or is outside the allowed range              &lt;response code&#x3D;\&quot;404\&quot;&gt;Specified order was not found&lt;/response&gt; |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |

<a id="salesOrdersCreateNewItem"></a>
# **salesOrdersCreateNewItem**
> salesOrdersCreateNewItem(newSalesOrderCommand)

Adds a new sales order to the system

Sample requests:                &#x60;&#x60;&#x60;  POST /salesorders  {      \&quot;customer\&quot;: {        \&quot;id\&quot;: \&quot;10001\&quot;,      },      \&quot;type\&quot;: \&quot;SO\&quot;  }  &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60;  POST /salesorders  {      \&quot;customer\&quot;: {        \&quot;id\&quot;: \&quot;10000\&quot;,        \&quot;order\&quot;: \&quot;some-customer-order-nbr\&quot;      },      \&quot;type\&quot;: \&quot;SO\&quot;,      \&quot;description\&quot;: \&quot;sample request order\&quot;,      \&quot;status\&quot;: \&quot;Hold\&quot;,      \&quot;orderLines\&quot;: [          {              \&quot;inventoryId\&quot;: \&quot;StockItem1\&quot;,              \&quot;quantity\&quot;: 4,              \&quot;unitPrice\&quot;: 101.25          }      ]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    NewSalesOrderCommand newSalesOrderCommand = new NewSalesOrderCommand(); // NewSalesOrderCommand | Information about the sales order to create
    try {
      apiInstance.salesOrdersCreateNewItem(newSalesOrderCommand);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersCreateNewItem");
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
| **newSalesOrderCommand** | [**NewSalesOrderCommand**](NewSalesOrderCommand.md)| Information about the sales order to create | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The order was created successfully, and the Location request header contains the address to call to GET the new sales order |  * Location - Location of the newly created resource <br>  |
| **400** | If any of values in command is not present or active, or is outside the allowed range               See &lt;a href&#x3D;\&quot;/swagger/v3/swagger.json#components/x-visma-erp-error-codes\&quot;&gt;#/components/x-visma-erp-error-codes&lt;/a&gt; for the full list of error codes. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Conflict |  -  |

<a id="salesOrdersDeleteLinesTypeorderIdlines"></a>
# **salesOrdersDeleteLinesTypeorderIdlines**
> salesOrdersDeleteLinesTypeorderIdlines(type, orderId, ids)

Delete lines from an existing sales order

If-Match header represents a version of Sales Order to be modified and must be included in request.  Value of current version is included in GET /salesorders/{type}/{orderId} and modification endpoints on that resource as ETag header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of the order to make modifications to
    String orderId = "orderId_example"; // String | The order number to make modifications to
    List<Integer> ids = Arrays.asList(); // List<Integer> | Lines to delete with comma seprator. Limit of line ids is 1000.
    try {
      apiInstance.salesOrdersDeleteLinesTypeorderIdlines(type, orderId, ids);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersDeleteLinesTypeorderIdlines");
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
| **type** | **String**| The type of the order to make modifications to | |
| **orderId** | **String**| The order number to make modifications to | |
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| Lines to delete with comma seprator. Limit of line ids is 1000. | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The lines were deleted successfully |  -  |
| **400** | If any of values in ids is outside the allowed range               See &lt;a href&#x3D;\&quot;/swagger/v3/swagger.json#components/x-visma-erp-error-codes\&quot;&gt;#/components/x-visma-erp-error-codes&lt;/a&gt; for the full list of error codes. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Specified order was not found |  -  |
| **405** | Method Not Allowed |  -  |

<a id="salesOrdersDeleteTypeorderId"></a>
# **salesOrdersDeleteTypeorderId**
> salesOrdersDeleteTypeorderId(type, orderId)

Delete an existing sales order

If-Match header represents a version of Sales Order to be modified and must be included in request.  Value of current version is included in GET /salesorders/{type}/{orderId} and modification endpoints on that resource as ETag header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of the order to delete
    String orderId = "orderId_example"; // String | The order number to delete
    try {
      apiInstance.salesOrdersDeleteTypeorderId(type, orderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersDeleteTypeorderId");
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
| **type** | **String**| The type of the order to delete | |
| **orderId** | **String**| The order number to delete | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The order was deleted successfully |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Specified order was not found |  -  |
| **405** | Method Not Allowed |  -  |

<a id="salesOrdersGetItemAsyncTypeorderId"></a>
# **salesOrdersGetItemAsyncTypeorderId**
> SalesOrderDto salesOrdersGetItemAsyncTypeorderId(type, orderId, expand)

Gets information about a single sales order

The expand query parameter corresponds to sections in the Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderDto.  If an expand value is not specified it will not be filled and returned in the response object.                Sample request:                &#x60;GET /salesorders/SO/000100?expand&#x3D;customer,payment&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of sales order to get
    String orderId = "orderId_example"; // String | The id of the sales order to get
    List<SalesOrderExpansions> expand = Arrays.asList(); // List<SalesOrderExpansions> | An optional specification of what details to include about the sales order. The default value if not supplied is \"None\"
    try {
      SalesOrderDto result = apiInstance.salesOrdersGetItemAsyncTypeorderId(type, orderId, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersGetItemAsyncTypeorderId");
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
| **type** | **String**| The type of sales order to get | |
| **orderId** | **String**| The id of the sales order to get | |
| **expand** | [**List&lt;SalesOrderExpansions&gt;**](SalesOrderExpansions.md)| An optional specification of what details to include about the sales order. The default value if not supplied is \&quot;None\&quot; | [optional] |

### Return type

[**SalesOrderDto**](SalesOrderDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderDto if found and accessible |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | If an order with type type and orderId is not found, or is not accessible. |  -  |

<a id="salesOrdersGetItemCommissionsTypeorderIdcommissions"></a>
# **salesOrdersGetItemCommissionsTypeorderIdcommissions**
> List&lt;SalesOrderCommissionDto&gt; salesOrdersGetItemCommissionsTypeorderIdcommissions(type, orderId)

Gets commission information for a single sales order

Sample request:                &#x60;GET /salesorders/SO/000101/commissions&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of sales order to get
    String orderId = "orderId_example"; // String | The id of the sales order to get
    try {
      List<SalesOrderCommissionDto> result = apiInstance.salesOrdersGetItemCommissionsTypeorderIdcommissions(type, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersGetItemCommissionsTypeorderIdcommissions");
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
| **type** | **String**| The type of sales order to get | |
| **orderId** | **String**| The id of the sales order to get | |

### Return type

[**List&lt;SalesOrderCommissionDto&gt;**](SalesOrderCommissionDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderCommissionDto if found and accessible |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | If an order with type type and orderId is not found, or is not accessible. |  -  |

<a id="salesOrdersGetItemDiscountsTypeorderIddiscounts"></a>
# **salesOrdersGetItemDiscountsTypeorderIddiscounts**
> List&lt;SalesOrderDiscountDto&gt; salesOrdersGetItemDiscountsTypeorderIddiscounts(type, orderId)

Gets discount details information for a single sales order

Sample request:                &#x60;GET /salesorders/SO/000101/discounts&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of sales order to get
    String orderId = "orderId_example"; // String | The id of the sales order to get
    try {
      List<SalesOrderDiscountDto> result = apiInstance.salesOrdersGetItemDiscountsTypeorderIddiscounts(type, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersGetItemDiscountsTypeorderIddiscounts");
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
| **type** | **String**| The type of sales order to get | |
| **orderId** | **String**| The id of the sales order to get | |

### Return type

[**List&lt;SalesOrderDiscountDto&gt;**](SalesOrderDiscountDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderDiscountDto if found and accessible |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | If an order with type type and orderId is not found, or is not accessible. |  -  |

<a id="salesOrdersGetItemLineTypeorderIdlineslineId"></a>
# **salesOrdersGetItemLineTypeorderIdlineslineId**
> SalesOrderLineDto salesOrdersGetItemLineTypeorderIdlineslineId(type, orderId, lineId)

Gets a specific sales order line for a single sales order

Sample request:                &#x60;GET /salesorders/SO/000101/lines/1&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of sales order to get
    String orderId = "orderId_example"; // String | The id of the sales order to get
    Integer lineId = 56; // Integer | The id of the line to get
    try {
      SalesOrderLineDto result = apiInstance.salesOrdersGetItemLineTypeorderIdlineslineId(type, orderId, lineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersGetItemLineTypeorderIdlineslineId");
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
| **type** | **String**| The type of sales order to get | |
| **orderId** | **String**| The id of the sales order to get | |
| **lineId** | **Integer**| The id of the line to get | |

### Return type

[**SalesOrderLineDto**](SalesOrderLineDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderLineDto object if sales order line is found and accessible |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | If an order with type type and orderId is not found, or is not accessible               or the line with the id lineId is not found |  -  |

<a id="salesOrdersGetItemLinesTypeorderIdlines"></a>
# **salesOrdersGetItemLinesTypeorderIdlines**
> SalesOrderLineDtoPagedResult salesOrdersGetItemLinesTypeorderIdlines(type, orderId, pageSize, pageIndex)

Gets sales order lines for a single sales order

Sample request:                &#x60;GET /salesorders/SO/000101/lines&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of sales order to get
    String orderId = "orderId_example"; // String | The id of the sales order to get
    Integer pageSize = 1000; // Integer | The number of lines retrieved per page, defaults to 1000 if not specified
    Integer pageIndex = 0; // Integer | The zero based page index to retrieve, defaults to 0 if not specified
    try {
      SalesOrderLineDtoPagedResult result = apiInstance.salesOrdersGetItemLinesTypeorderIdlines(type, orderId, pageSize, pageIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersGetItemLinesTypeorderIdlines");
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
| **type** | **String**| The type of sales order to get | |
| **orderId** | **String**| The id of the sales order to get | |
| **pageSize** | **Integer**| The number of lines retrieved per page, defaults to 1000 if not specified | [optional] [default to 1000] |
| **pageIndex** | **Integer**| The zero based page index to retrieve, defaults to 0 if not specified | [optional] [default to 0] |

### Return type

[**SalesOrderLineDtoPagedResult**](SalesOrderLineDtoPagedResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Visma.net.ERP.SalesOrders.Api.Dto.PagedResult&#x60;1 object if sales order is found and accessible |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | If an order with type type and orderId is not found, or is not accessible. |  -  |

<a id="salesOrdersGetItemRotRutTypeorderIdrotrut"></a>
# **salesOrdersGetItemRotRutTypeorderIdrotrut**
> SalesOrderRotRutDto salesOrdersGetItemRotRutTypeorderIdrotrut(type, orderId)

Gets ROT/RUT information for a single sales order

Sample request:                &#x60;GET /salesorders/SO/000123/rotrut&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of sales order to get
    String orderId = "orderId_example"; // String | The id of the sales order to get
    try {
      SalesOrderRotRutDto result = apiInstance.salesOrdersGetItemRotRutTypeorderIdrotrut(type, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersGetItemRotRutTypeorderIdrotrut");
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
| **type** | **String**| The type of sales order to get | |
| **orderId** | **String**| The id of the sales order to get | |

### Return type

[**SalesOrderRotRutDto**](SalesOrderRotRutDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderRotRutDto if found and accessible |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | If an order with type type and orderId is not found, or is not accessible. |  -  |

<a id="salesOrdersGetItemTaxTypeorderIdtax"></a>
# **salesOrdersGetItemTaxTypeorderIdtax**
> List&lt;SalesOrderTaxDto&gt; salesOrdersGetItemTaxTypeorderIdtax(type, orderId)

Gets tax information for a single sales order

Sample request:                &#x60;GET /salesorders/SO/000101/tax&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of sales order to get
    String orderId = "orderId_example"; // String | The id of the sales order to get
    try {
      List<SalesOrderTaxDto> result = apiInstance.salesOrdersGetItemTaxTypeorderIdtax(type, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersGetItemTaxTypeorderIdtax");
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
| **type** | **String**| The type of sales order to get | |
| **orderId** | **String**| The id of the sales order to get | |

### Return type

[**List&lt;SalesOrderTaxDto&gt;**](SalesOrderTaxDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderTaxDto if found and accessible |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | If an order with type type and orderId is not found, or is not accessible. |  -  |

<a id="salesOrdersGetList"></a>
# **salesOrdersGetList**
> SalesOrderListDtoPagedResult salesOrdersGetList(customerId, status, modifiedSince, pageSize, pageIndex, orderBy, filter)

Gets a paged list with sales orders of any type

Sample requests:                &#x60;GET /salesorders&#x60;                &#x60;GET /salesorders?customerId&#x3D;10000&amp;status&#x3D;Open&amp;pageSize&#x3D;10&#x60;                &#x60;GET /salesorders?orderBy&#x3D;lastModified%20asc&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String customerId = "customerId_example"; // String | The customer for which to retrieve orders. If omitted or empty, orders for all customers are included
    String status = "status_example"; // String | The order status to include in the result. If omitted or empty, orders with any status are included.
    OffsetDateTime modifiedSince = OffsetDateTime.now(); // OffsetDateTime | A date/time value for filtering when a sales order last changed.  Unless a specific time zone offset is included (e.g. '2012-12-24T12:15:14+02:00'), the date is considered to be in the UTC time zone.
    Integer pageSize = 100; // Integer | The number of customers retrieved per page
    Integer pageIndex = 0; // Integer | The zero based page index to retrieve
    String orderBy = "orderBy_example"; // String | The field to order the list by. Can be one of `created`, `lastModified`, or `orderId` followed by an optional sort direction (`asc` or `desc`), default direction is `asc` (ascending) if not present.
    String filter = "filter_example"; // String | A filter for the list, applied to the orderId
    try {
      SalesOrderListDtoPagedResult result = apiInstance.salesOrdersGetList(customerId, status, modifiedSince, pageSize, pageIndex, orderBy, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersGetList");
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
| **customerId** | **String**| The customer for which to retrieve orders. If omitted or empty, orders for all customers are included | [optional] |
| **status** | **String**| The order status to include in the result. If omitted or empty, orders with any status are included. | [optional] |
| **modifiedSince** | **OffsetDateTime**| A date/time value for filtering when a sales order last changed.  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T12:15:14+02:00&#39;), the date is considered to be in the UTC time zone. | [optional] |
| **pageSize** | **Integer**| The number of customers retrieved per page | [optional] [default to 100] |
| **pageIndex** | **Integer**| The zero based page index to retrieve | [optional] [default to 0] |
| **orderBy** | **String**| The field to order the list by. Can be one of &#x60;created&#x60;, &#x60;lastModified&#x60;, or &#x60;orderId&#x60; followed by an optional sort direction (&#x60;asc&#x60; or &#x60;desc&#x60;), default direction is &#x60;asc&#x60; (ascending) if not present. | [optional] |
| **filter** | **String**| A filter for the list, applied to the orderId | [optional] |

### Return type

[**SalesOrderListDtoPagedResult**](SalesOrderListDtoPagedResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderListDto found. |  -  |
| **400** | If &#x60;pageSize&#x60; or &#x60;pageIndex&#x60; is not within the allowed range, or if an invalid &#x60;orderBy&#x60; is specified |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="salesOrdersGetListType"></a>
# **salesOrdersGetListType**
> SalesOrderListDtoPagedResult salesOrdersGetListType(type, customerId, status, modifiedSince, pageSize, pageIndex, orderBy, filter)

Gets a paged list with sales orders of a specific type

Sample requests:                &#x60;GET /salesorders/SO&#x60;                &#x60;GET /salesorders/SO?customerId&#x3D;10000&amp;status&#x3D;Open&amp;pageSize&#x3D;10&#x60;                &#x60;GET /salesorders/SO?orderBy&#x3D;created%20desc&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of sales orders to get.
    String customerId = "customerId_example"; // String | The customer for which to retrieve orders. If omitted or empty, orders for all customers are included
    String status = "status_example"; // String | The order status to include in the result. If omitted or empty, orders with any status are included.
    OffsetDateTime modifiedSince = OffsetDateTime.now(); // OffsetDateTime | A date/time value for filtering when a sales order last changed.  Unless a specific time zone offset is included (e.g. '2012-12-24T12:15:14+02:00'), the date is considered to be in the UTC time zone.
    Integer pageSize = 100; // Integer | The number of customers retrieved per page
    Integer pageIndex = 0; // Integer | The zero based page index to retrieve
    String orderBy = "orderBy_example"; // String | The field to order the list by. Can be one of `created`, `lastModified`, or `orderId` followed by an optional sort direction (`asc` or `desc`), default direction is `asc` (ascending) if not present.
    String filter = "filter_example"; // String | A filter for the list, applied to the orderId
    try {
      SalesOrderListDtoPagedResult result = apiInstance.salesOrdersGetListType(type, customerId, status, modifiedSince, pageSize, pageIndex, orderBy, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersGetListType");
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
| **type** | **String**| The type of sales orders to get. | |
| **customerId** | **String**| The customer for which to retrieve orders. If omitted or empty, orders for all customers are included | [optional] |
| **status** | **String**| The order status to include in the result. If omitted or empty, orders with any status are included. | [optional] |
| **modifiedSince** | **OffsetDateTime**| A date/time value for filtering when a sales order last changed.  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T12:15:14+02:00&#39;), the date is considered to be in the UTC time zone. | [optional] |
| **pageSize** | **Integer**| The number of customers retrieved per page | [optional] [default to 100] |
| **pageIndex** | **Integer**| The zero based page index to retrieve | [optional] [default to 0] |
| **orderBy** | **String**| The field to order the list by. Can be one of &#x60;created&#x60;, &#x60;lastModified&#x60;, or &#x60;orderId&#x60; followed by an optional sort direction (&#x60;asc&#x60; or &#x60;desc&#x60;), default direction is &#x60;asc&#x60; (ascending) if not present. | [optional] |
| **filter** | **String**| A filter for the list, applied to the orderId | [optional] |

### Return type

[**SalesOrderListDtoPagedResult**](SalesOrderListDtoPagedResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderListDto found. |  -  |
| **400** | If &#x60;pageSize&#x60; or &#x60;pageIndex&#x60; is not within the allowed range, or if an invalid &#x60;orderBy&#x60; is specified |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="salesOrdersGetSalesOrderShipmentTypeorderIdshipment"></a>
# **salesOrdersGetSalesOrderShipmentTypeorderIdshipment**
> List&lt;SalesOrderShipmentDto&gt; salesOrdersGetSalesOrderShipmentTypeorderIdshipment(type, orderId)

Gets shipment information for a single sales order

Sample request:                &#x60;GET /salesorders/SO/000101/shipment&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of sales order to get
    String orderId = "orderId_example"; // String | The id of the sales order to get
    try {
      List<SalesOrderShipmentDto> result = apiInstance.salesOrdersGetSalesOrderShipmentTypeorderIdshipment(type, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersGetSalesOrderShipmentTypeorderIdshipment");
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
| **type** | **String**| The type of sales order to get | |
| **orderId** | **String**| The id of the sales order to get | |

### Return type

[**List&lt;SalesOrderShipmentDto&gt;**](SalesOrderShipmentDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderShipmentDto if found and accessible |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | If an order with type type and orderId is not found, or is not accessible. |  -  |

<a id="salesOrdersPatchLinesTypeorderIdlines"></a>
# **salesOrdersPatchLinesTypeorderIdlines**
> salesOrdersPatchLinesTypeorderIdlines(type, orderId, patchSalesOrderLinesCommand)

Make modifications to an existing sales order lines

If-Match header represents a version of Sales Order to be modified and must be included in request.  Value of current version is included in GET /salesorders/{type}/{orderId} and modification endpoints on that resource as ETag header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of the order to make modifications to
    String orderId = "orderId_example"; // String | The order number to make modifications to
    PatchSalesOrderLinesCommand patchSalesOrderLinesCommand = new PatchSalesOrderLinesCommand(); // PatchSalesOrderLinesCommand | Data to change about the sales order lines
    try {
      apiInstance.salesOrdersPatchLinesTypeorderIdlines(type, orderId, patchSalesOrderLinesCommand);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersPatchLinesTypeorderIdlines");
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
| **type** | **String**| The type of the order to make modifications to | |
| **orderId** | **String**| The order number to make modifications to | |
| **patchSalesOrderLinesCommand** | [**PatchSalesOrderLinesCommand**](PatchSalesOrderLinesCommand.md)| Data to change about the sales order lines | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The order was modified successfully |  -  |
| **400** | If any of values in command is outside the allowed range               See &lt;a href&#x3D;\&quot;/swagger/v3/swagger.json#components/x-visma-erp-error-codes\&quot;&gt;#/components/x-visma-erp-error-codes&lt;/a&gt; for the full list of error codes. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The order specified was not found |  -  |
| **405** | Method Not Allowed |  -  |
| **412** | Order version does not match with If-Match header |  -  |
| **428** | If-Match header was not supplied |  -  |

<a id="salesOrdersPatchTypeorderId"></a>
# **salesOrdersPatchTypeorderId**
> salesOrdersPatchTypeorderId(type, orderId, patchSalesOrderCommand)

Make modifications to an existing sales order

If-Match header represents a version of Sales Order to be modified and must be included in request.  Value of current version is included in GET /salesorders/{type}/{orderId} and modification endpoints on that resource as ETag header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SalesOrdersApi apiInstance = new SalesOrdersApi(defaultClient);
    String type = "type_example"; // String | The type of the order to make modifications to
    String orderId = "orderId_example"; // String | The order number to make modifications to
    PatchSalesOrderCommand patchSalesOrderCommand = new PatchSalesOrderCommand(); // PatchSalesOrderCommand | Data to change about the sales order
    try {
      apiInstance.salesOrdersPatchTypeorderId(type, orderId, patchSalesOrderCommand);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesOrdersApi#salesOrdersPatchTypeorderId");
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
| **type** | **String**| The type of the order to make modifications to | |
| **orderId** | **String**| The order number to make modifications to | |
| **patchSalesOrderCommand** | [**PatchSalesOrderCommand**](PatchSalesOrderCommand.md)| Data to change about the sales order | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The order was modified successfully |  -  |
| **400** | If any of values in command is outside the allowed range               See &lt;a href&#x3D;\&quot;/swagger/v3/swagger.json#components/x-visma-erp-error-codes\&quot;&gt;#/components/x-visma-erp-error-codes&lt;/a&gt; for the full list of error codes. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The order specified was not found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Order version does not match with If-Match header |  -  |
| **428** | If-Match header was not supplied |  -  |


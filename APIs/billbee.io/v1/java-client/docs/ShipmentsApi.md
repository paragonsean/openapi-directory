# ShipmentsApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**shipmentGetList**](ShipmentsApi.md#shipmentGetList) | **GET** /api/v1/shipment/shipments | Get a list of all shipments optionally filtered by date. All parameters are optional. |
| [**shipmentGetPing**](ShipmentsApi.md#shipmentGetPing) | **GET** /api/v1/shipment/ping |  |
| [**shipmentGetShippingCarrier**](ShipmentsApi.md#shipmentGetShippingCarrier) | **GET** /api/v1/shipment/shippingcarriers | Queries the currently available shipping carriers. |
| [**shipmentGetShippingproviders**](ShipmentsApi.md#shipmentGetShippingproviders) | **GET** /api/v1/shipment/shippingproviders | Query all defined shipping providers |
| [**shipmentPostShipment**](ShipmentsApi.md#shipmentPostShipment) | **POST** /api/v1/shipment/shipment | Creates a new shipment with the selected Shippingprovider |
| [**shipmentShipWithLabel**](ShipmentsApi.md#shipmentShipWithLabel) | **POST** /api/v1/shipment/shipwithlabel | Creates a shipment for an order in billbee |


<a id="shipmentGetList"></a>
# **shipmentGetList**
> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment shipmentGetList(page, pageSize, createdAtMin, createdAtMax, orderId, minimumShipmentId, shippingProviderId)

Get a list of all shipments optionally filtered by date. All parameters are optional.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    Integer page = 56; // Integer | Specifies the page to request.
    Integer pageSize = 56; // Integer | Specifies the pagesize. Defaults to 50, max value is 250
    OffsetDateTime createdAtMin = OffsetDateTime.now(); // OffsetDateTime | Specifies the oldest shipment date to include in the response
    OffsetDateTime createdAtMax = OffsetDateTime.now(); // OffsetDateTime | Specifies the newest shipment date to include in the response
    Long orderId = 56L; // Long | Get shipments for this order only.
    Long minimumShipmentId = 56L; // Long | Get Shipments with a shipment greater or equal than this id. New shipments have a greater id than older shipments.
    Long shippingProviderId = 56L; // Long | Get Shippings for the specified shipping provider only. <seealso cref=\"M:Rechnungsdruck.WebApp.Controllers.Api.ShipmentController.GetShippingproviders\" />
    try {
      RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment result = apiInstance.shipmentGetList(page, pageSize, createdAtMin, createdAtMax, orderId, minimumShipmentId, shippingProviderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#shipmentGetList");
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
| **page** | **Integer**| Specifies the page to request. | [optional] |
| **pageSize** | **Integer**| Specifies the pagesize. Defaults to 50, max value is 250 | [optional] |
| **createdAtMin** | **OffsetDateTime**| Specifies the oldest shipment date to include in the response | [optional] |
| **createdAtMax** | **OffsetDateTime**| Specifies the newest shipment date to include in the response | [optional] |
| **orderId** | **Long**| Get shipments for this order only. | [optional] |
| **minimumShipmentId** | **Long**| Get Shipments with a shipment greater or equal than this id. New shipments have a greater id than older shipments. | [optional] |
| **shippingProviderId** | **Long**| Get Shippings for the specified shipping provider only. &lt;seealso cref&#x3D;\&quot;M:Rechnungsdruck.WebApp.Controllers.Api.ShipmentController.GetShippingproviders\&quot; /&gt; | [optional] |

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="shipmentGetPing"></a>
# **shipmentGetPing**
> Object shipmentGetPing()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    try {
      Object result = apiInstance.shipmentGetPing();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#shipmentGetPing");
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

<a id="shipmentGetShippingCarrier"></a>
# **shipmentGetShippingCarrier**
> Object shipmentGetShippingCarrier()

Queries the currently available shipping carriers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    try {
      Object result = apiInstance.shipmentGetShippingCarrier();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#shipmentGetShippingCarrier");
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

<a id="shipmentGetShippingproviders"></a>
# **shipmentGetShippingproviders**
> Object shipmentGetShippingproviders()

Query all defined shipping providers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    try {
      Object result = apiInstance.shipmentGetShippingproviders();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#shipmentGetShippingproviders");
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

<a id="shipmentPostShipment"></a>
# **shipmentPostShipment**
> Object shipmentPostShipment(billbeeInterfacesBillbeeAPIModelCreateShipmentApiModel)

Creates a new shipment with the selected Shippingprovider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel billbeeInterfacesBillbeeAPIModelCreateShipmentApiModel = new BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel(); // BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel | Data to specify shipment parameters
    try {
      Object result = apiInstance.shipmentPostShipment(billbeeInterfacesBillbeeAPIModelCreateShipmentApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#shipmentPostShipment");
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
| **billbeeInterfacesBillbeeAPIModelCreateShipmentApiModel** | [**BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel**](BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel.md)| Data to specify shipment parameters | |

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

<a id="shipmentShipWithLabel"></a>
# **shipmentShipWithLabel**
> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult shipmentShipWithLabel(rechnungsdruckWebAppControllersApiShipmentWithLabel)

Creates a shipment for an order in billbee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    RechnungsdruckWebAppControllersApiShipmentWithLabel rechnungsdruckWebAppControllersApiShipmentWithLabel = new RechnungsdruckWebAppControllersApiShipmentWithLabel(); // RechnungsdruckWebAppControllersApiShipmentWithLabel | Details on the order and the shipping methods, that should be used.
    try {
      RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult result = apiInstance.shipmentShipWithLabel(rechnungsdruckWebAppControllersApiShipmentWithLabel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#shipmentShipWithLabel");
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
| **rechnungsdruckWebAppControllersApiShipmentWithLabel** | [**RechnungsdruckWebAppControllersApiShipmentWithLabel**](RechnungsdruckWebAppControllersApiShipmentWithLabel.md)| Details on the order and the shipping methods, that should be used. | |

### Return type

[**RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult**](RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


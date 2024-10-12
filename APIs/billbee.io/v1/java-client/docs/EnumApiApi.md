# EnumApiApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**enumApiGetOrderStates**](EnumApiApi.md#enumApiGetOrderStates) | **GET** /api/v1/enums/orderstates | Returns a list with all defined orderstates |
| [**enumApiGetPaymentTypes**](EnumApiApi.md#enumApiGetPaymentTypes) | **GET** /api/v1/enums/paymenttypes | Returns a list with all defined paymenttypes |
| [**enumApiGetShipmentTypes**](EnumApiApi.md#enumApiGetShipmentTypes) | **GET** /api/v1/enums/shipmenttypes | Returns a list with all defined shipmenttypes |
| [**enumApiGetShippingCarriers**](EnumApiApi.md#enumApiGetShippingCarriers) | **GET** /api/v1/enums/shippingcarriers | Returns a list with all defined shippingcarriers |


<a id="enumApiGetOrderStates"></a>
# **enumApiGetOrderStates**
> Object enumApiGetOrderStates()

Returns a list with all defined orderstates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnumApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    EnumApiApi apiInstance = new EnumApiApi(defaultClient);
    try {
      Object result = apiInstance.enumApiGetOrderStates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnumApiApi#enumApiGetOrderStates");
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

<a id="enumApiGetPaymentTypes"></a>
# **enumApiGetPaymentTypes**
> Object enumApiGetPaymentTypes()

Returns a list with all defined paymenttypes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnumApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    EnumApiApi apiInstance = new EnumApiApi(defaultClient);
    try {
      Object result = apiInstance.enumApiGetPaymentTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnumApiApi#enumApiGetPaymentTypes");
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

<a id="enumApiGetShipmentTypes"></a>
# **enumApiGetShipmentTypes**
> Object enumApiGetShipmentTypes()

Returns a list with all defined shipmenttypes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnumApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    EnumApiApi apiInstance = new EnumApiApi(defaultClient);
    try {
      Object result = apiInstance.enumApiGetShipmentTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnumApiApi#enumApiGetShipmentTypes");
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

<a id="enumApiGetShippingCarriers"></a>
# **enumApiGetShippingCarriers**
> Object enumApiGetShippingCarriers()

Returns a list with all defined shippingcarriers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnumApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    EnumApiApi apiInstance = new EnumApiApi(defaultClient);
    try {
      Object result = apiInstance.enumApiGetShippingCarriers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnumApiApi#enumApiGetShippingCarriers");
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


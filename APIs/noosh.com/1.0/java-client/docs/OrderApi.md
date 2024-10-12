# OrderApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBuyOrder**](OrderApi.md#getBuyOrder) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders/{order_id} | Get a specific buy order |
| [**getBuyOrderList**](OrderApi.md#getBuyOrderList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders | List the buy orders |
| [**getBuyOrderListOfWorkgroup**](OrderApi.md#getBuyOrderListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/buyOrders | List the buy orders of workgroup |
| [**getBuyOrderOfWorkgroup**](OrderApi.md#getBuyOrderOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/buyOrders/{order_id} | Get a specific buy order of workgroup |
| [**getOrder**](OrderApi.md#getOrder) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/orders/{order_id} | Get a specific buy/sell order |
| [**getSellOrder**](OrderApi.md#getSellOrder) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/sellOrders/{order_id} | Get a specific sell order |
| [**getSellOrderList**](OrderApi.md#getSellOrderList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/sellOrders | List the sell orders |
| [**getSellOrderListOfWorkgroup**](OrderApi.md#getSellOrderListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/sellOrders | List the sell orders of workgrop |
| [**getSellOrderOfWorkgroup**](OrderApi.md#getSellOrderOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/sellOrders/{order_id} | Get a specific sell order |
| [**postBuyOrder**](OrderApi.md#postBuyOrder) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders | Create a quick buy order |
| [**putBuyOrder**](OrderApi.md#putBuyOrder) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders/{order_id} | Update a specific buy order |
| [**putSellOrder**](OrderApi.md#putSellOrder) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id}/sellOrders/{order_id} | Update / Accept or Reject a specific sell order |


<a id="getBuyOrder"></a>
# **getBuyOrder**
> OrderDetailVO getBuyOrder(workgroupId, projectId, orderId)

Get a specific buy order

Get a specific buy order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String orderId = "orderId_example"; // String | 
    try {
      OrderDetailVO result = apiInstance.getBuyOrder(workgroupId, projectId, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#getBuyOrder");
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

[**OrderDetailVO**](OrderDetailVO.md)

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

<a id="getBuyOrderList"></a>
# **getBuyOrderList**
> OrderListVO getBuyOrderList(workgroupId, projectId)

List the buy orders

List the buy orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      OrderListVO result = apiInstance.getBuyOrderList(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#getBuyOrderList");
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

### Return type

[**OrderListVO**](OrderListVO.md)

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

<a id="getBuyOrderListOfWorkgroup"></a>
# **getBuyOrderListOfWorkgroup**
> OrderWorkgroupLevelListVO getBuyOrderListOfWorkgroup(workgroupId)

List the buy orders of workgroup

List the buy orders of workgroup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      OrderWorkgroupLevelListVO result = apiInstance.getBuyOrderListOfWorkgroup(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#getBuyOrderListOfWorkgroup");
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

### Return type

[**OrderWorkgroupLevelListVO**](OrderWorkgroupLevelListVO.md)

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

<a id="getBuyOrderOfWorkgroup"></a>
# **getBuyOrderOfWorkgroup**
> OrderExpandWorkgroupLevelVO getBuyOrderOfWorkgroup(workgroupId, orderId)

Get a specific buy order of workgroup

Get a specific buy order of workgroup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String orderId = "orderId_example"; // String | 
    try {
      OrderExpandWorkgroupLevelVO result = apiInstance.getBuyOrderOfWorkgroup(workgroupId, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#getBuyOrderOfWorkgroup");
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
| **orderId** | **String**|  | |

### Return type

[**OrderExpandWorkgroupLevelVO**](OrderExpandWorkgroupLevelVO.md)

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

<a id="getOrder"></a>
# **getOrder**
> OrderDetailWithIndicatorVO getOrder(workgroupId, projectId, orderId)

Get a specific buy/sell order

Get a specific buy/sell order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String orderId = "orderId_example"; // String | 
    try {
      OrderDetailWithIndicatorVO result = apiInstance.getOrder(workgroupId, projectId, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#getOrder");
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

[**OrderDetailWithIndicatorVO**](OrderDetailWithIndicatorVO.md)

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

<a id="getSellOrder"></a>
# **getSellOrder**
> OrderDetailVO getSellOrder(workgroupId, projectId, orderId)

Get a specific sell order

Get a specific sell order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String orderId = "orderId_example"; // String | 
    try {
      OrderDetailVO result = apiInstance.getSellOrder(workgroupId, projectId, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#getSellOrder");
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

[**OrderDetailVO**](OrderDetailVO.md)

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

<a id="getSellOrderList"></a>
# **getSellOrderList**
> OrderListVO getSellOrderList(workgroupId, projectId)

List the sell orders

List the sell orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      OrderListVO result = apiInstance.getSellOrderList(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#getSellOrderList");
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

### Return type

[**OrderListVO**](OrderListVO.md)

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

<a id="getSellOrderListOfWorkgroup"></a>
# **getSellOrderListOfWorkgroup**
> OrderWorkgroupLevelListVO getSellOrderListOfWorkgroup(workgroupId)

List the sell orders of workgrop

List the sell orders of workgrop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      OrderWorkgroupLevelListVO result = apiInstance.getSellOrderListOfWorkgroup(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#getSellOrderListOfWorkgroup");
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

### Return type

[**OrderWorkgroupLevelListVO**](OrderWorkgroupLevelListVO.md)

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

<a id="getSellOrderOfWorkgroup"></a>
# **getSellOrderOfWorkgroup**
> OrderExpandWorkgroupLevelVO getSellOrderOfWorkgroup(workgroupId, orderId)

Get a specific sell order

Get a specific sell order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String orderId = "orderId_example"; // String | 
    try {
      OrderExpandWorkgroupLevelVO result = apiInstance.getSellOrderOfWorkgroup(workgroupId, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#getSellOrderOfWorkgroup");
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
| **orderId** | **String**|  | |

### Return type

[**OrderExpandWorkgroupLevelVO**](OrderExpandWorkgroupLevelVO.md)

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

<a id="postBuyOrder"></a>
# **postBuyOrder**
> OrderPO postBuyOrder(workgroupId, projectId, orderPO)

Create a quick buy order

Create a quick buy order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    OrderPO orderPO = new OrderPO(); // OrderPO | 
    try {
      OrderPO result = apiInstance.postBuyOrder(workgroupId, projectId, orderPO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#postBuyOrder");
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
| **orderPO** | [**OrderPO**](OrderPO.md)|  | [optional] |

### Return type

[**OrderPO**](OrderPO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful created |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

<a id="putBuyOrder"></a>
# **putBuyOrder**
> OrderVO putBuyOrder(workgroupId, projectId, orderId, orderUpdPersistVO)

Update a specific buy order

Update a specific buy order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String orderId = "orderId_example"; // String | 
    OrderUpdPersistVO orderUpdPersistVO = new OrderUpdPersistVO(); // OrderUpdPersistVO | 
    try {
      OrderVO result = apiInstance.putBuyOrder(workgroupId, projectId, orderId, orderUpdPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#putBuyOrder");
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
| **orderUpdPersistVO** | [**OrderUpdPersistVO**](OrderUpdPersistVO.md)|  | [optional] |

### Return type

[**OrderVO**](OrderVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful updated |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="putSellOrder"></a>
# **putSellOrder**
> OrderVO putSellOrder(workgroupId, projectId, orderId, orderUpdPersistVO)

Update / Accept or Reject a specific sell order

Update / Accept or Reject a specific sell order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String orderId = "orderId_example"; // String | 
    OrderUpdPersistVO orderUpdPersistVO = new OrderUpdPersistVO(); // OrderUpdPersistVO | 
    try {
      OrderVO result = apiInstance.putSellOrder(workgroupId, projectId, orderId, orderUpdPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#putSellOrder");
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
| **orderUpdPersistVO** | [**OrderUpdPersistVO**](OrderUpdPersistVO.md)|  | [optional] |

### Return type

[**OrderVO**](OrderVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful updated |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |


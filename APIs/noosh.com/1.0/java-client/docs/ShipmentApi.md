# ShipmentApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getShipment**](ShipmentApi.md#getShipment) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/shipments/{shipment_id} | Get a specific shipment. |
| [**getShipmentList**](ShipmentApi.md#getShipmentList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/shipments | List shipments of project |
| [**postShipment**](ShipmentApi.md#postShipment) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/shipments | Create a shipment |
| [**putShipmentLocation**](ShipmentApi.md#putShipmentLocation) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id}/shipments/{shipment_id}/locations/{location_id} | Update a specific shipment location |


<a id="getShipment"></a>
# **getShipment**
> ShipmentExpandVO getShipment(workgroupId, projectId, shipmentId)

Get a specific shipment.

Get a specific shipment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ShipmentApi apiInstance = new ShipmentApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String shipmentId = "shipmentId_example"; // String | 
    try {
      ShipmentExpandVO result = apiInstance.getShipment(workgroupId, projectId, shipmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentApi#getShipment");
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
| **shipmentId** | **String**|  | |

### Return type

[**ShipmentExpandVO**](ShipmentExpandVO.md)

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

<a id="getShipmentList"></a>
# **getShipmentList**
> ShipmentListVO getShipmentList(workgroupId, projectId)

List shipments of project

List shipments of project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ShipmentApi apiInstance = new ShipmentApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      ShipmentListVO result = apiInstance.getShipmentList(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentApi#getShipmentList");
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

[**ShipmentListVO**](ShipmentListVO.md)

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

<a id="postShipment"></a>
# **postShipment**
> ShipmentLocationsPOSTResultVO postShipment(workgroupId, projectId, shipmentLocationPostPersistVO)

Create a shipment

Create a shipment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ShipmentApi apiInstance = new ShipmentApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    ShipmentLocationPostPersistVO shipmentLocationPostPersistVO = new ShipmentLocationPostPersistVO(); // ShipmentLocationPostPersistVO | 
    try {
      ShipmentLocationsPOSTResultVO result = apiInstance.postShipment(workgroupId, projectId, shipmentLocationPostPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentApi#postShipment");
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
| **shipmentLocationPostPersistVO** | [**ShipmentLocationPostPersistVO**](ShipmentLocationPostPersistVO.md)|  | [optional] |

### Return type

[**ShipmentLocationsPOSTResultVO**](ShipmentLocationsPOSTResultVO.md)

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

<a id="putShipmentLocation"></a>
# **putShipmentLocation**
> HTTPStatusVO putShipmentLocation(workgroupId, projectId, shipmentId, locationId, shipmentLocationPersistVO)

Update a specific shipment location

Update a specific shipment location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ShipmentApi apiInstance = new ShipmentApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String shipmentId = "shipmentId_example"; // String | 
    String locationId = "locationId_example"; // String | 
    ShipmentLocationPersistVO shipmentLocationPersistVO = new ShipmentLocationPersistVO(); // ShipmentLocationPersistVO | 
    try {
      HTTPStatusVO result = apiInstance.putShipmentLocation(workgroupId, projectId, shipmentId, locationId, shipmentLocationPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentApi#putShipmentLocation");
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
| **shipmentId** | **String**|  | |
| **locationId** | **String**|  | |
| **shipmentLocationPersistVO** | [**ShipmentLocationPersistVO**](ShipmentLocationPersistVO.md)|  | [optional] |

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successfully |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |


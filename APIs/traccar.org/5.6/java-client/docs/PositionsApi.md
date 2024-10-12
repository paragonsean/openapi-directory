# PositionsApi

All URIs are relative to *https://demo.traccar.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**positionsGet**](PositionsApi.md#positionsGet) | **GET** /positions | Fetches a list of Positions |


<a id="positionsGet"></a>
# **positionsGet**
> List&lt;Position&gt; positionsGet(deviceId, from, to, id)

Fetches a list of Positions

We strongly recommend using [Traccar WebSocket API](https://www.traccar.org/traccar-api/) instead of periodically polling positions endpoint. Without any params, it returns a list of last known positions for all the user&#39;s Devices. _from_ and _to_ fields are not required with _id_.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PositionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PositionsApi apiInstance = new PositionsApi(defaultClient);
    Integer deviceId = 56; // Integer | _deviceId_ is optional, but requires the _from_ and _to_ parameters when used
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    Integer id = 56; // Integer | To fetch one or more positions. Multiple params can be passed like `id=31&id=42`
    try {
      List<Position> result = apiInstance.positionsGet(deviceId, from, to, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PositionsApi#positionsGet");
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
| **deviceId** | **Integer**| _deviceId_ is optional, but requires the _from_ and _to_ parameters when used | [optional] |
| **from** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | [optional] |
| **to** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | [optional] |
| **id** | **Integer**| To fetch one or more positions. Multiple params can be passed like &#x60;id&#x3D;31&amp;id&#x3D;42&#x60; | [optional] |

### Return type

[**List&lt;Position&gt;**](Position.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/gpx+xml, application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


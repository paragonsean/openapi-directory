# EventsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkEvents**](EventsApi.md#getNetworkEvents) | **GET** /networks/{networkId}/events | List the events for the network |
| [**getNetworkEventsEventTypes**](EventsApi.md#getNetworkEventsEventTypes) | **GET** /networks/{networkId}/events/eventTypes | List the event type to human-readable description |


<a id="getNetworkEvents"></a>
# **getNetworkEvents**
> Object getNetworkEvents(networkId, productType, includedEventTypes, excludedEventTypes, deviceMac, deviceSerial, deviceName, clientIp, clientMac, clientName, smDeviceMac, smDeviceName, perPage, startingAfter, endingBefore)

List the events for the network

List the events for the network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String productType = "productType_example"; // String | The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and environmental
    List<String> includedEventTypes = Arrays.asList(); // List<String> | A list of event types. The returned events will be filtered to only include events with these types.
    List<String> excludedEventTypes = Arrays.asList(); // List<String> | A list of event types. The returned events will be filtered to exclude events with these types.
    String deviceMac = "deviceMac_example"; // String | The MAC address of the Meraki device which the list of events will be filtered with
    String deviceSerial = "deviceSerial_example"; // String | The serial of the Meraki device which the list of events will be filtered with
    String deviceName = "deviceName_example"; // String | The name of the Meraki device which the list of events will be filtered with
    String clientIp = "clientIp_example"; // String | The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks.
    String clientMac = "clientMac_example"; // String | The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks.
    String clientName = "clientName_example"; // String | The name, or partial name, of the client which the list of events will be filtered with
    String smDeviceMac = "smDeviceMac_example"; // String | The MAC address of the Systems Manager device which the list of events will be filtered with
    String smDeviceName = "smDeviceName_example"; // String | The name of the Systems Manager device which the list of events will be filtered with
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      Object result = apiInstance.getNetworkEvents(networkId, productType, includedEventTypes, excludedEventTypes, deviceMac, deviceSerial, deviceName, clientIp, clientMac, clientName, smDeviceMac, smDeviceName, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#getNetworkEvents");
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
| **networkId** | **String**|  | |
| **productType** | **String**| The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and environmental | [optional] |
| **includedEventTypes** | [**List&lt;String&gt;**](String.md)| A list of event types. The returned events will be filtered to only include events with these types. | [optional] |
| **excludedEventTypes** | [**List&lt;String&gt;**](String.md)| A list of event types. The returned events will be filtered to exclude events with these types. | [optional] |
| **deviceMac** | **String**| The MAC address of the Meraki device which the list of events will be filtered with | [optional] |
| **deviceSerial** | **String**| The serial of the Meraki device which the list of events will be filtered with | [optional] |
| **deviceName** | **String**| The name of the Meraki device which the list of events will be filtered with | [optional] |
| **clientIp** | **String**| The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks. | [optional] |
| **clientMac** | **String**| The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks. | [optional] |
| **clientName** | **String**| The name, or partial name, of the client which the list of events will be filtered with | [optional] |
| **smDeviceMac** | **String**| The MAC address of the Systems Manager device which the list of events will be filtered with | [optional] |
| **smDeviceName** | **String**| The name of the Systems Manager device which the list of events will be filtered with | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkEventsEventTypes"></a>
# **getNetworkEventsEventTypes**
> List&lt;Object&gt; getNetworkEventsEventTypes(networkId)

List the event type to human-readable description

List the event type to human-readable description

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkEventsEventTypes(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#getNetworkEventsEventTypes");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |


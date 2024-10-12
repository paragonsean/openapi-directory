# UplinkApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkCellularGatewayUplink_1**](UplinkApi.md#getNetworkCellularGatewayUplink_1) | **GET** /networks/{networkId}/cellularGateway/uplink | Returns the uplink settings for your MG network. |
| [**getOrganizationCellularGatewayUplinkStatuses_1**](UplinkApi.md#getOrganizationCellularGatewayUplinkStatuses_1) | **GET** /organizations/{organizationId}/cellularGateway/uplink/statuses | List the uplink status of every Meraki MG cellular gateway in the organization |
| [**updateNetworkCellularGatewayUplink_1**](UplinkApi.md#updateNetworkCellularGatewayUplink_1) | **PUT** /networks/{networkId}/cellularGateway/uplink | Updates the uplink settings for your MG network. |


<a id="getNetworkCellularGatewayUplink_1"></a>
# **getNetworkCellularGatewayUplink_1**
> Object getNetworkCellularGatewayUplink_1(networkId)

Returns the uplink settings for your MG network.

Returns the uplink settings for your MG network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinkApi apiInstance = new UplinkApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkCellularGatewayUplink_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinkApi#getNetworkCellularGatewayUplink_1");
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationCellularGatewayUplinkStatuses_1"></a>
# **getOrganizationCellularGatewayUplinkStatuses_1**
> List&lt;GetOrganizationCellularGatewayUplinkStatuses200ResponseInner&gt; getOrganizationCellularGatewayUplinkStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids)

List the uplink status of every Meraki MG cellular gateway in the organization

List the uplink status of every Meraki MG cellular gateway in the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinkApi apiInstance = new UplinkApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of network IDs. The returned devices will be filtered to only include these networks.
    List<String> serials = Arrays.asList(); // List<String> | A list of serial numbers. The returned devices will be filtered to only include these serials.
    List<String> iccids = Arrays.asList(); // List<String> | A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    try {
      List<GetOrganizationCellularGatewayUplinkStatuses200ResponseInner> result = apiInstance.getOrganizationCellularGatewayUplinkStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinkApi#getOrganizationCellularGatewayUplinkStatuses_1");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of network IDs. The returned devices will be filtered to only include these networks. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| A list of serial numbers. The returned devices will be filtered to only include these serials. | [optional] |
| **iccids** | [**List&lt;String&gt;**](String.md)| A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs. | [optional] |

### Return type

[**List&lt;GetOrganizationCellularGatewayUplinkStatuses200ResponseInner&gt;**](GetOrganizationCellularGatewayUplinkStatuses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="updateNetworkCellularGatewayUplink_1"></a>
# **updateNetworkCellularGatewayUplink_1**
> Object updateNetworkCellularGatewayUplink_1(networkId, updateNetworkCellularGatewayUplinkRequest)

Updates the uplink settings for your MG network.

Updates the uplink settings for your MG network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinkApi apiInstance = new UplinkApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkCellularGatewayUplinkRequest updateNetworkCellularGatewayUplinkRequest = new UpdateNetworkCellularGatewayUplinkRequest(); // UpdateNetworkCellularGatewayUplinkRequest | 
    try {
      Object result = apiInstance.updateNetworkCellularGatewayUplink_1(networkId, updateNetworkCellularGatewayUplinkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinkApi#updateNetworkCellularGatewayUplink_1");
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
| **updateNetworkCellularGatewayUplinkRequest** | [**UpdateNetworkCellularGatewayUplinkRequest**](UpdateNetworkCellularGatewayUplinkRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |


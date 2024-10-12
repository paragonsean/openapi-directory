# SubnetsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceApplianceDhcpSubnets_2**](SubnetsApi.md#getDeviceApplianceDhcpSubnets_2) | **GET** /devices/{serial}/appliance/dhcp/subnets | Return the DHCP subnet information for an appliance |


<a id="getDeviceApplianceDhcpSubnets_2"></a>
# **getDeviceApplianceDhcpSubnets_2**
> List&lt;Object&gt; getDeviceApplianceDhcpSubnets_2(serial)

Return the DHCP subnet information for an appliance

Return the DHCP subnet information for an appliance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubnetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SubnetsApi apiInstance = new SubnetsApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceApplianceDhcpSubnets_2(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubnetsApi#getDeviceApplianceDhcpSubnets_2");
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
| **serial** | **String**|  | |

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


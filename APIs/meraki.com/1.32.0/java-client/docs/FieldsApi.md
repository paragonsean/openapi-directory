# FieldsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateNetworkSmDevicesFields_2**](FieldsApi.md#updateNetworkSmDevicesFields_2) | **PUT** /networks/{networkId}/sm/devices/fields | Modify the fields of a device |


<a id="updateNetworkSmDevicesFields_2"></a>
# **updateNetworkSmDevicesFields_2**
> List&lt;UpdateNetworkSmDevicesFields200ResponseInner&gt; updateNetworkSmDevicesFields_2(networkId, updateNetworkSmDevicesFieldsRequest)

Modify the fields of a device

Modify the fields of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FieldsApi apiInstance = new FieldsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSmDevicesFieldsRequest updateNetworkSmDevicesFieldsRequest = new UpdateNetworkSmDevicesFieldsRequest(); // UpdateNetworkSmDevicesFieldsRequest | 
    try {
      List<UpdateNetworkSmDevicesFields200ResponseInner> result = apiInstance.updateNetworkSmDevicesFields_2(networkId, updateNetworkSmDevicesFieldsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldsApi#updateNetworkSmDevicesFields_2");
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
| **updateNetworkSmDevicesFieldsRequest** | [**UpdateNetworkSmDevicesFieldsRequest**](UpdateNetworkSmDevicesFieldsRequest.md)|  | |

### Return type

[**List&lt;UpdateNetworkSmDevicesFields200ResponseInner&gt;**](UpdateNetworkSmDevicesFields200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |


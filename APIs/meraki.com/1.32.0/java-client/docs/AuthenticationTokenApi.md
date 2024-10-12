# AuthenticationTokenApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeviceApplianceVmxAuthenticationToken_2**](AuthenticationTokenApi.md#createDeviceApplianceVmxAuthenticationToken_2) | **POST** /devices/{serial}/appliance/vmx/authenticationToken | Generate a new vMX authentication token |


<a id="createDeviceApplianceVmxAuthenticationToken_2"></a>
# **createDeviceApplianceVmxAuthenticationToken_2**
> CreateDeviceApplianceVmxAuthenticationToken201Response createDeviceApplianceVmxAuthenticationToken_2(serial)

Generate a new vMX authentication token

Generate a new vMX authentication token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationTokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AuthenticationTokenApi apiInstance = new AuthenticationTokenApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      CreateDeviceApplianceVmxAuthenticationToken201Response result = apiInstance.createDeviceApplianceVmxAuthenticationToken_2(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationTokenApi#createDeviceApplianceVmxAuthenticationToken_2");
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

[**CreateDeviceApplianceVmxAuthenticationToken201Response**](CreateDeviceApplianceVmxAuthenticationToken201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

